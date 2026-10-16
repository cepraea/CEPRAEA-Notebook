# Decisão externa do operador — `STAGE_09`

```yaml
operator_decision: "AUTHORIZED_WITH_RESTRICTIONS"
stage_id: "STAGE_09"
responsible: "USER"
decided_at: "2026-10-16T01:36:28-03:00"
evidence: "Autorizar o início do STAGE_09 e gerar e revisar grants e políticas RLS candidatas."
authorized_action: "GENERATE_AND_REVIEW_GRANTS_AND_RLS_CANDIDATE"
authorized_inputs:
  - document_id: "ACCESS_REQUIREMENTS"
    version: "0.1.0"
    sha256: "bafce57a9d71ef3ea0ba54c79fac585f075d8d0efe5fe22967e62bde6c424c92"
    promoted_source_id: "c7f18856-d7c7-4b77-8feb-3266d60337c0"
  - document_id: "POSTGRESQL_SCHEMA_CANDIDATE"
    sha256: "f5224887f8dd85b82542e3645e0c68fbad77c336a5f0509c229a6f7867694828"
    promoted_source_id: "1f69f4e5-f4f3-43fd-b8b0-87f19b8b2c8b"
scope:
  public_resources: 9
  closed_resources: 23
  output: "09-politicas-rls.candidate.sql"
restrictions:
  - "Não executar SQL."
  - "Não criar nem aplicar migration."
  - "Não implantar ou carregar dados."
  - "Não iniciar os STAGE_10 a STAGE_15."
  - "Não promover o candidato sem nova aprovação humana."
  - "Não inventar relações, colunas, vínculos de identidade ou atribuições de papel ausentes do schema promovido."
  - "Não usar user_metadata como fonte de autorização."
  - "Não substituir vínculo persistido e auditável por alegações não demonstradas em JWT."
  - "Quando uma policy fiel não puder ser expressa com as entradas promovidas, emitir GENERATION_BLOCKED com a dependência ausente."
future_production_conditions:
  - "Concluir migrations, rollback e testes antes de qualquer implantação."
  - "Autorizar produção somente após STAGE_14 e STAGE_15 confirmarem evidências reproduzíveis."
result: "AUTHORIZED_TO_GENERATE_AND_REVIEW_CANDIDATE_ONLY"
```
