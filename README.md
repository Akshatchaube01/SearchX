# SearchX

<img width="1536" height="1024" alt="Workflow" src="https://github.com/user-attachments/assets/52aad74b-6373-4158-81f2-dbebda8b8c18" />

A complete distributed search engine system with a modern Next.js UI, FastAPI backend, and Celery workers.

## Project Structure

```
SearchX/
├── services/
│   ├── api/               # FastAPI backend
│   │   ├── main.py
│   │   ├── routes/
│   │   └── requirements.txt
│   └── worker/            # Celery worker for crawling
│       ├── tasks.py
│       ├── crawler/
│       ├── search/
│       ├── utils/
│       └── requirements.txt
├── ui/                    # Next.js frontend
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── package.json
│   └── README.md
├── docker-compose.yaml    # Service orchestration
└── README.md
```

## Quick Start

### With Docker Compose

```bash
# Start all services (API, Worker, Redis, Elasticsearch)
docker compose up -d

# View logs
docker compose logs -f

# Stop services
docker compose down
```

### Frontend Setup

```bash
cd ui
npm install
npm run dev
```

The UI will be available at http://localhost:3000

Configure the API endpoint in `ui/.env.local`:
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Available Endpoints

**API Server** (http://localhost:8000):
- `GET /search?q=<query>` - Search the index
- `POST /crawl` - Start crawling URLs
- `GET /health` - Health check

**Web UI** (http://localhost:3000):
- Search interface with real-time results
- Modern, responsive design

## Services

### API Service
- Framework: FastAPI
- Port: 8000
- Routes: `/search`, `/crawl`, `/health`

### Worker Service
- Framework: Celery
- Message Broker: Redis
- Tasks: Web crawling, content extraction, indexing
- Crawler: Fetches pages and extracts links
- Search: Elasticsearch integration

### Storage
- **Redis**: Message queue and caching
- **Elasticsearch**: Full-text search and indexing

## UI Features

- ⚡ Fast search interface built with Next.js
- 🎨 Modern responsive design
- 🔍 Real-time search results
- 📱 Mobile-friendly interface
- 🎯 TypeScript support

For more UI documentation, see [UI README](./ui/README.md)
