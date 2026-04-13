Security no pipeline · Shift-left na prática
GitHub Actions
Terraform
SAST
Checkov
Python
Lab 01 — IaC Security Scanner
Problema real: Terraform cria S3 sem encryption e SG aberto sem ninguém perceber. Checkov bloqueia o PR automaticamente.
Output: GitHub Action com gate de IaC security + relatório de violations
Lab 02 — Full Secure Pipeline
Problema real: pipeline sem nenhuma verificação de segurança em nenhuma etapa. Adiciona SAST + container scan + IaC scan + secrets check.
Output: pipeline completo como template reutilizável
