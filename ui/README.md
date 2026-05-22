# SearchX UI

A modern Next.js interface for the SearchX search engine.

## Features

- Fast and responsive search interface
- Real-time search results
- Built with Next.js and React
- TypeScript support
- CSS Modules for styling

## Getting Started

### Prerequisites

- Node.js 16+ 
- npm or yarn

### Installation

1. Navigate to the UI directory:
```bash
cd ui
```

2. Install dependencies:
```bash
npm install
```

3. Configure the API URL (optional):
Edit `.env.local` to point to your API server:
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Development

Run the development server:
```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser to see the application.

### Production

Build for production:
```bash
npm run build
```

Start the production server:
```bash
npm start
```

## Project Structure

```
ui/
├── app/                    # Next.js app directory
│   ├── layout.tsx         # Root layout
│   ├── page.tsx           # Home page
│   ├── page.module.css    # Home page styles
│   └── globals.css        # Global styles
├── components/            # React components
│   ├── SearchBar.tsx      # Search input component
│   └── ResultsList.tsx    # Search results display
├── lib/                   # Utility functions
│   └── api.ts            # API client
├── public/               # Static files
├── package.json          # Dependencies
├── next.config.js        # Next.js configuration
└── tsconfig.json         # TypeScript configuration
```

## Environment Variables

- `NEXT_PUBLIC_API_URL`: API server URL (default: http://localhost:8000)

## API Integration

The UI connects to the SearchX API with the following endpoints:

- `GET /search?q=<query>` - Search the engine
- `POST /crawl` - Crawl new URLs
- `GET /health` - API health check

## Styling

The application uses CSS Modules for component styling with a modern gradient design. Responsive design ensures the interface works well on all devices.
