<div align="center">
  <h1>🧠 KaLLia API 🧠</h1>
  <p><i>Cérebro centralizado e orquestrador de agentes autônomos para a assistente virtual KaLLia</i></p>
  
  ![Python](https://img.shields.io/badge/python-3.13-blue)
  ![Framework](https://img.shields.io/badge/agent%20framework-Agno-orange)
  ![API](https://img.shields.io/badge/api-FastAPI-green)
  ![Status](https://img.shields.io/badge/version-5.2-emerald)
</div>

---

## 🎯 Sobre o Projeto

**KaLLia API** é o servidor de inteligência central da assistente virtual KaLLia, construído sobre o framework [FastAPI](https://fastapi.tiangolo.com/) e o orquestrador de agentes [Agno](https://docs.agno.com).

A API gerencia raciocínio multimodal, execução segura de ferramentas (*function calling*), memória perene e fallback inteligente entre modelos de linguagem:

1. **Orquestração Multi-Modelo:** Suporte nativo ao Google Gemini com contingência automática para Groq (`openai/gpt-oss-120b`).
2. **Integração Financeira Nativa:** Ferramentas de leitura SQL direta para responder sobre investimentos e saldo.
3. **Telemetria de Hardware:** Monitoramento de CPU, temperatura, memória e energia do servidor / Raspberry Pi.

### 🌐 Ecossistema KaLLia (Repositórios Conectados)
- 🕹️ **[KaLLia-HQ](https://github.com/vitugrey/KaLLia-HQ):** Command Center 2D Isométrico Cyberpunk com painel de agentes, notificações, To-Do list, rotinas e chat por voz (AssemblyAI STT + Edge-TTS).
- 📊 **[KaLLia Finanças](https://github.com/vitugrey/kallia-financa):** Gestor financeiro em Django com controle de investimentos (B3 e manuais), rebalanceamento de carteira ARCA e fluxo orçamentário.

---

## ✨ Funcionalidades Principais

### 🛡️ Redundância e Fallback Robusto (120B)
- **Provedor Principal:** Google Gemini (`gemini-3.1-flash-lite` com suporte a visão e imagens Base64).
- **Fallback Automático:** Em caso de oscilação de cota ou erro 503, chaveia automaticamente para o **Groq** utilizando o modelo **`openai/gpt-oss-120b`** (120 bilhões de parâmetros) com execução de ferramentas (*function calling*).

### 💰 Consultas Financeiras
- Conexão segura em modo somente leitura (`SELECT`) ao banco de dados SQLite de finanças via `SQLiteTools`.
- Endpoint dedicado `/finance/saldo` para balanços mensais e anuais rápidos.

### 🧠 Memória Persistente e Sessões
- Persistência das últimas mensagens de contexto e consolidação de memórias de longo prazo via `SqliteDb` do Agno no banco `databases/kallia-agent.db`.

---

## 🛠️ Arquitetura do Repositório

```
kallia/
├── api/                  # Backend FastAPI e orquestrador de agentes Agno
│   ├── src/              # Rotas, agente, personalidade, ferramentas e fallback
│   ├── Dockerfile        # Containerização da API
│   └── pyproject.toml    # Dependências com UV
├── databases/            # Volume de bancos SQLite e logs (compartilhado)
│   ├── kallia-agent.db   # Sessões e memórias do Agno
│   ├── kallia-financa.db # Banco de dados financeiro relacional
│   └── kallia.log        # Logs rotativos do sistema
├── docker-compose.yml    # Orquestração do container da API
└── .env                  # Chaves de API e variáveis de ambiente
```

---

## 🚀 Como Executar

### 1. Pré-requisitos
- **Docker** e **Docker Compose** instalados (ou Python 3.12+ com [uv](https://docs.astral.sh/uv/)).
- Arquivo `.env` na raiz do projeto com as chaves:
  ```ini
  GOOGLE_API_KEY=sua_chave_gemini
  GROQ_API_KEY=sua_chave_groq
  ```

### 2. Inicialização via Docker
```bash
docker compose up -d --build
```

Endpoints disponíveis:
- **Documentação Swagger:** `http://localhost:1904/docs`
- **Health Check:** `GET http://localhost:1904/`
- **Chat com Agente:** `POST http://localhost:1904/chat`
- **Telemetria de Sistema:** `GET http://localhost:1904/status`
- **Saldo Financeiro:** `GET http://localhost:1904/finance/saldo`
