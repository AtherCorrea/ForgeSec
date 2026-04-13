GNITE Cloud · Ataque para entender a defesa
IAM escalation
SSRF
S3 abuse
Pacu
Python
Lab 01 — IAM Privilege Escalation
Problema real: atacante com iam:PassRole cria recurso que assume role de admin. Simula o ataque em ambiente isolado.
Output: playbook de ataque + detecção via CloudTrail + regra de prevenção
Lab 02 — SSRF to Metadata Service
Problema real: SSRF em app EC2 expõe credenciais do instance metadata (169.254.169.254). Demonstra exploit e IMDSv2 como defesa.
Output: exploit funcional + hardening com IMDSv2 obrigatório
Lab 03 — Secrets in Code Scanner
Problema real: AWS keys commitadas por acidente no GitHub público. Scanner encontra segredos em repos antes do atacante.
Output: pre-commit hook + GitHub Action com Trufflehog/Gitleaks