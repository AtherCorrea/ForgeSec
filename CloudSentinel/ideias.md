CloudSec Intelligence Engine · O projeto principal
Projeto âncora
Python
Claude API
AWS Security Hub
Prowler
PDF/Markdown
Lab 01 — Findings Ingestion Pipeline
Problema real: Security Hub retorna centenas de findings brutos sem contexto. Pipeline normaliza e agrupa por severidade e serviço.
Output: JSON estruturado pronto para análise de IA
Lab 02 — AI Executive Report Generator
Problema real: CISO precisa entender o risco sem ler 300 linhas técnicas. Claude API transforma findings em narrativa de risco de negócio.
Output: PDF executivo com risk score, top 3 riscos e recomendações
Lab 03 — Technical Remediation Report
Problema real: engenheiro precisa de passos exatos para corrigir. IA gera guia técnico com comandos prontos por finding.
Output: Markdown técnico com código de remediação por severidade
Lab 04 — Scheduled Scan + Slack Alert
Problema real: ninguém vê os relatórios se precisar buscar manualmente. Lambda roda scan diário e envia resumo no Slack.
Output: pipeline completo serverless com notificação automática