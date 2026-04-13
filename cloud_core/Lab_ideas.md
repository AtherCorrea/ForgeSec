Lab 01 — IAM Misconfiguration Scanner
Problema real: usuário com AdministratorAccess sem MFA. Script Python detecta e reporta automaticamente.
Output: relatório JSON com severity + remediation steps
Lab 02 — S3 Bucket Exposure Detector
Problema real: bucket público criado por engenheiro sem querer. Scanner identifica ACLs abertas e políticas permissivas.
Output: lista de buckets expostos + Terraform fix automático
Lab 03 — CloudTrail Anomaly Detection
Problema real: API calls suspeitas às 3h da manhã de IP desconhecido. Python analisa logs e sinaliza comportamento anômalo.
Output: alert com contexto do evento + TTPs mapeados no MITRE
Lab 04 — VPC Security Audit
Problema real: Security Group com porta 22 aberta para 0.0.0.0/0. Scan automático de todas as regras de SG.
Output: dashboard de exposição de portas por ambiente