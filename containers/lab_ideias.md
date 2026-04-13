Docker + Kubernetes security · Do básico ao EKS
Docker
Kubernetes
EKS
Trivy
OPA/Gatekeeper
Lab 01 — Vulnerable Image Scanner
Problema real: imagem base desatualizada com CVEs críticos em produção. Pipeline Trivy scanneia antes do deploy.
Output: CI/CD pipeline com gate de segurança que bloqueia imagens vulneráveis
Lab 02 — Container Escape Simulation
Problema real: container rodando como root com acesso ao socket Docker. Demonstra o risco e implementa a defesa.
Output: before/after com securityContext hardened e documentação do ataque
Lab 03 — Kubernetes RBAC Hardening
Problema real: ServiceAccount com permissões de cluster-admin vazando para pods de aplicação.
Output: política RBAC mínima + OPA policy que previne regressão
Lab 04 — EKS Security Benchmark
Problema real: cluster EKS recém-criado com defaults inseguros. kube-bench avalia contra CIS Benchmark.
Output: score CIS antes/depois + Terraform com remediações aplicadas