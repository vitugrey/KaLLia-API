<div align="center">
  <h1>🧠 KaLLia API & Bot 🧠</h1>
  <p><i>Cérebro centralizado, orquestrador de agentes autônomos e cliente Telegram para a assistente virtual KaLLia</i></p>
  
  ![Python](https://img.shields.io/badge/python-3.13-blue)
  ![Framework](https://img.shields.io/badge/agent%20framework-Agno-orange)
  ![API](https://img.shields.io/badge/api-FastAPI-green)
  ![Bot](https://img.shields.io/badge/telegram-Pyrogram-blue)
  ![Status](https://img.shields.io/badge/version-5.2-emerald)
</div>

---

## 🎯 Sobre o Projeto

**KaLLia** é o cérebro inteligente central da assistente virtual KaLLia. O repositório abriga a API de orquestração de IA e o bot cliente do Telegram, projetados para operar de forma modular e integrada aos demais subsistemas do ecossistema:

1. **KaLLia API (`/api`)**: Servidor [FastAPI](https://fastapi.tiangolo.com/) com framework de agentes [Agno](https://docs.agno.com). Orquestra ferramentas de consulta a banco de dados SQLite local (finanças e memórias), telemetria de hardware e contingência automática (fallback) entre provedores de IA.
2. **KaLLia Telegram Bot (`/telegram`)**: Bot cliente interativo desenvolvido com [Pyrogram](https://docs.pyrogram.org/), com suporte a visão computacional (análise de fotos/imagens em tempo real), consultas financeiras (`/saldo`), monitoramento de hardware (`/status`) e comandos de sessão.

### 🌐 Ecossistema KaLLia (Repositórios Conectados)
- 🕹️ **[KaLLia-HQ](https://github.com/vitugrey/KaLLia-HQ):** Command Center 2D Isométrico Cyberpunk com painel de agentes, notificações, To-Do list, rotinas e chat por voz (AssemblyAI STT + Edge-TTS).
- 📊 **[KaLLia Finanças](https://github.com/vitugrey/kallia-financa):** Gestor financeiro em Django com controle de investimentos (B3 e manuais), rebalanceamento de carteira ARCA e fluxo orçamentário.

---

## ✨ Funcionalidades Principais

### 🛡️ Redundância e Fallback Robusto (120B)
- **Provedor Principal:** Google Gemini (`gemini-3.1-flash-lite` com suporte a visão computacional).
- **Fallback Automático:** Em caso de oscilação de cota ou erro 503, chaveia automaticamente para o **Groq** utilizando o modelo **`openai/gpt-oss-120b`** (120 bilhões de parâmetros) com execução de ferramentas (*function calling*).

### 💰 Integração Financeira Nativa
- Conexão segura em modo somente leitura (`SELECT`) ao banco de dados SQLite de finanças.
- Consultas diretas via linguagem natural, comando `/saldo` no Telegram ou no endpoint `/finance/saldo`.

### 🧠 Memória Persistente e Sessões
- Persistência das últimas mensagens de contexto e consolidação de memórias de longo prazo via `SqliteDb` do Agno no banco `databases/kallia-agent.db`.

### 📸 Visão Computacional no Telegram
- Suporte a fotos comprimidas e imagens sem compressão enviadas como documento.
- Processamento em memória e resposta analítica da KaLLia.

---

## 🛠️ Arquitetura do Repositório

```
kallia/
├── api/                  # Backend FastAPI e orquestrador de agentes Agno
│   ├── src/              # Rotas, agente, personalidade, ferramentas e fallback
│   ├── Dockerfile        # Containerização da API
│   └── pyproject.toml    # Dependências com UV
├── telegram/             # Bot do Telegram Pyrogram
│   ├── bot.py            # Comandos rápidos, handlers de mensagens e fotos
│   ├── Dockerfile        # Containerização do Bot
│   └── pyproject.toml    # Dependências do bot
├── databases/            # Volume de bancos SQLite e logs (compartilhado)
│   ├── kallia-agent.db   # Sessões e memórias do Agno
│   ├── kallia-financa.db # Banco de dados financeiro relacional
│   └── kallia.log        # Logs rotativos do sistema
├── docker-compose.yml    # Orquestração local dos containers (api e telegram)
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
  TELEGRAM_BOT_TOKEN=token_do_bot
  TELEGRAM_API_ID=id_telegram
  TELEGRAM_API_HASH=hash_telegram
  TELEGRAM_ALLOWED_USER_ID=seu_telegram_id
  ```

### 2. Inicialização via Docker
```bash
docker compose up -d --build
```

Endpoints disponíveis:
- **KaLLia API:** `http://localhost:1904/docs`
- **Bot Telegram:** Conectado e ativo automaticamente
