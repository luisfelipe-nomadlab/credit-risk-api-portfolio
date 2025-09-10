# Detecção de Fraude em Tempo Real
## Descrição

Este projeto implementa uma API REST em FastAPI para detecção de fraude em transações financeiras em tempo real.
A API oferece endpoints para checagem de saúde do sistema e predição de risco de fraude baseado em features transacionais simuladas.

O projeto utiliza **Python 3.11, Docker**, e integra boas práticas de logging e configuração centralizada.

## Funcionalidades

* Health Check: Verifica o status da aplicação e dos serviços integrados (ex.: Redis).

* Predição de Fraude: Endpoint para avaliar o risco de fraude em transações enviadas via JSON.

* Logging estruturado: Todos os eventos importantes são logados em formato JSON.

* CORS habilitado: Permite integração com aplicações front-end externas.

## Tecnologias Utilizadas

* Python 3.11
* FastAPI
* Pydantic / Pydantic Settings
* Docker
* Uvicorn
* Redis (opcional, integração futura)
* Logging estruturado com python-json-logger
* Pandas e NumPy (para cálculo de features)

deteccao_fraude_mlops/
│
├── app/
│   ├── api/
│   │   ├── core/
│   │   │   └── config.py       # Configurações globais
│   │   ├── utils/
│   │   │   └── logger.py       # Logging estruturado
│   │   └── v1/
│   │       ├── healt.py        # Endpoint de health check
│   │       └── fraud.py        # Endpoint de predição de fraude
│   │       └── fraud_engine.py # Engine dummy para cálculo de features
│   └── main.py                 # Entrada da aplicação FastAPI
│
├── requirements.txt            # Dependências do projeto
├── Dockerfile                  # Dockerfile para build da imagem
└── README.md

## Endpoints
1. Health Check
GET /api/v1/healt
**Resposta de exemplo:**
{
  "app": "Real time fraud detection",
  "status": "ok",
  "debug": false,
  "redis": "checagem ok"
}

Nota: Atualmente o cálculo de risco é dummy. Deve ser substituído pelo modelo de ML real.
