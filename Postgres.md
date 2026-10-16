# PostgreSQL Local - Testes

A criação de um banco de dados PostgreSQL local voltado para testes deve priorizar **isolamento**, **velocidade de inicialização** e **descartabilidade** (capacidade de recriar o estado limpo rapidamente sem poluir o sistema operacional hospedeiro).

A tabela abaixo resume as especificações técnicas das quatro abordagens principais para ambientes de desenvolvimento e testes:

| Abordagem | Isolamento | Persistência Padrão | Tempo de Boot | Caso de Uso Principal |
| --- | --- | --- | --- | --- |
| **Docker CLI (Efêmero)** | Alto (Container) | Nenhuma (RAM / `--rm`) | ~1 a 2 segundos | Testes rápidos de linha de comando e validação manual de schemas |
| **Docker Compose** | Alto (Container + Rede) | Configurável (Volume ou RAM) | ~2 a 3 segundos | Ambiente local padronizado do projeto e baterias de testes de integração |
| **Testcontainers** | Máximo (Por suíte/teste) | Nenhuma (Destruído pós-teste) | ~2 a 4 segundos | Automação de testes (Pytest, Jest, Go) e pipelines de CI/CD |
| **PGlite (WASM)** | Em processo (In-memory) | Nenhuma ou Arquivo local | Milissegundos | Testes unitários/integração ultrarrápidos em ecossistemas Node.js/TypeScript |

---

## 1. Docker Compose Otimizado para Testes (Recomendado para Projetos)

Para reduzir a sobrecarga operacional no dia a dia, um arquivo `docker-compose.test.yml` versionado no repositório garante que qualquer máquina ou pipeline suba exatamente a mesma versão do banco, já com otimizações de I/O e verificação de saúde (*healthcheck*).

### Especificação Técnica (`docker-compose.test.yml`)

```yaml
services:
  postgres-test:
    image: postgres:16-alpine
    container_name: pg_test_env
    ports:
      # Mapeia na 5433 do host para evitar conflito com eventual Postgres nativo na 5432
      - "5433:5432"
    environment:
      POSTGRES_USER: test_user
      POSTGRES_PASSWORD: test_password
      POSTGRES_DB: app_test_db
    # Monta o diretório de dados na memória RAM (tmpfs) para acelerar migrations e testes
    tmpfs:
      - /var/lib/postgresql/data
    # Parâmetros que desativam garantias de escrita em disco (seguro apenas para testes)
    command: >
      postgres
      -c fsync=off
      -c synchronous_commit=off
      -c full_page_writes=off
      -c max_connections=200
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U test_user -d app_test_db"]
      interval: 2s
      timeout: 2s
      retries: 10

```

### Comandos de Operação e Conexão

* **Subir o ambiente em background:**

```bash
docker compose -f docker-compose.test.yml up -d
```

* **String de conexão (Connection URI) para a aplicação/ORM:**

```text
postgresql://test_user:test_password@localhost:5433/app_test_db
```

* **Destruir o ambiente e limpar a memória:**

```bash
docker compose -f docker-compose.test.yml down -v
```

> **Inicialização automática de Schemas/Seeds:** Se você precisar que o banco já suba com tabelas ou extensões criadas (como `uuid-ossp` ou `pgcrypto`), basta adicionar um volume mapeando uma pasta local de scripts `.sql` ou `.sh` para `/docker-entrypoint-initdb.d` dentro do container. O PostgreSQL executará todos os arquivos dessa pasta em ordem alfabética no primeiro boot.

---

## 2. Docker CLI (Instância Rápida e Descartável)

Se você precisa apenas de um banco imediato para testar uma query, validar uma migração ou depurar um script sem criar arquivos de configuração, execute o container com a flag `--rm` (que apaga o container assim que ele é interrompido).

### Comando de Execução Direta

```bash
docker run --rm --name pg-quick-test \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=testdb \
  -p 5433:5432 \
  --tmpfs /var/lib/postgresql/data:rw \
  -d postgres:16-alpine

```

### Acesso ao Terminal SQL (`psql`) sem Instalar Cliente Local

Não é necessário instalar o pacote `postgresql-client` na sua máquina. Você pode executar o cliente diretamente de dentro do próprio container:

```bash
# Abrir o prompt interativo do psql
docker exec -it pg-quick-test psql -U postgres -d testdb

# Executar um arquivo SQL local diretamente no container
docker exec -i pg-quick-test psql -U postgres -d testdb < ./schema.sql

```

Para encerrar e apagar todos os vestígios do banco de testes:

```bash
docker stop pg-quick-test

```

---

## 3. Automação em Suítes de Teste (Testcontainers e CI/CD)

Em pipelines de integração contínua ou baterias de testes automatizados (como `pytest` em Python ou `jest`/`vitest` em Node.js), gerenciar o ciclo de vida do banco manualmente gera atrito operacional.

### Padrão Programático com Testcontainers (Exemplo em Python / Pytest)

A biblioteca `testcontainers` sobe um container PostgreSQL real antes da suíte de testes e o destrói automaticamente ao final da execução:

```python
import pytest
import sqlalchemy
from testcontainers.postgres import PostgresContainer

@pytest.fixture(scope="session")
def postgres_db():
    # Sobe o container automaticamente em uma porta livre aleatória
    with PostgresContainer("postgres:16-alpine") as postgres:
        engine = sqlalchemy.create_engine(postgres.get_connection_url())
        # Aqui você pode rodar suas migrations (ex: Alembic / Prisma / Django)
        yield engine
        # Ao sair do bloco 'with', o container é destruído automaticamente

```

---

## Análise Técnica e Recomendações Operacionais

Separando as especificações acima das decisões de arquitetura para o seu fluxo de trabalho, considere as seguintes práticas para evitar gargalos:

1. **Desacoplamento de Portas (`5433` vs `5432`):** Manter o banco de testes na porta `5433` (ou usar portas dinâmicas) evita dois problemas críticos: conflito de porta caso você já tenha um banco de desenvolvimento rodando na `5432`, e o risco acidental de a suíte de testes executar um `DROP DATABASE` ou `TRUNCATE` no seu banco de desenvolvimento local.
2. **Uso de `tmpfs` e `fsync=off`:** Em baterias de testes que recriam esquemas ou rodam centenas de transações (`INSERT`/`ROLLBACK`), o gargalo quase nunca é CPU, mas sim o I/O de disco. Montar `/var/lib/postgresql/data` em `tmpfs` (RAM) combinado com `fsync=off` reduz o tempo de execução das migrations e suítes de teste em até **40% a 70%**, sem qualquer risco, já que os dados de teste são descartáveis.
3. **Imagem `alpine`:** Prefira sempre a tag `postgres:16-alpine` (ou a versão exata utilizada em produção seguida de `-alpine`). Ela consome cerca de um terço do espaço em disco (~85 MB contra ~430 MB da imagem Debian padrão) e inicializa mais rápido.