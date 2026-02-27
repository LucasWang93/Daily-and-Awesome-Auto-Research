# Daily Papers Assistant

An automated daily literature management tool that collects, ranks, summarizes, and archives AI research papers from multiple sources.

## Features

- **Multi-source collection**: ArXiv API, HuggingFace Daily Papers, Nature journal RSS feeds
- **LLM-powered ranking**: GPT-based scoring on relevance, novelty, and impact (three dimensions, 1-10 scale)
- **Smart archival**: Only archives truly important papers (max 5/day) with deep Chinese summaries and PDF downloads
- **Daily reports**: Generates comprehensive Markdown reports in Chinese with trend highlights
- **Email notifications**: Optional SMTP email delivery of daily reports
- **Cron scheduling**: Easy setup for automated daily runs

## Architecture

```
ArXiv API ──┐
HF Daily ───┼──> Collector ──> Dedup ──> LLM Ranker ──> Top 20
Nature RSS ─┘                                │
                                             ├──> Summarizer ──> Markdown Report + Email
                                             └──> Importance Judge ──> Archiver (max 5)
                                                                        ├── PDF download
                                                                        └── Deep summary
```

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set up environment variables

```bash
# Required: Azure OpenAI credentials
export AZURE_ENDPOINT="https://your-endpoint.openai.azure.com/"
export AZURE_API_KEY="your-api-key"
export AZURE_API_VERSION="2024-12-01-preview"

# Optional: secondary endpoint for GPT-5 (auto-fallback to primary if unavailable)
export AZURE_ENDPOINT_2="https://your-secondary-endpoint.openai.azure.com/"
export AZURE_API_KEY_2="your-secondary-key"
export AZURE_API_VERSION_2="2024-12-01-preview"

# Optional: email password for SMTP notifications
export EMAIL_PASSWORD="your-app-password"
```

### 3. Configure

```bash
cp config.yaml.example config.yaml
# Edit config.yaml to customize topics, sources, email settings, etc.
```

### 4. Run

```bash
# Full pipeline: collect -> rank -> archive -> summarize -> email
python run.py

# Dry run: collect and rank only (no LLM calls for summary/archive)
python run.py --dry-run

# Custom config path
python run.py --config /path/to/config.yaml
```

### 5. Schedule daily runs (optional)

```bash
# Install cron job (default: 08:00 UTC daily)
bash setup_cron.sh

# Custom time (e.g., 09:30 UTC)
bash setup_cron.sh 9 30
```

## Output Structure

```
daily_papers/
  reports/
    2026-02-27.md          # Daily summary report
  archive/
    metadata.json           # Global archive index
    multi-modal_llm/
      2602.22897/
        2602.22897.pdf      # Downloaded paper
        summary.md          # Deep Chinese summary
        meta.json           # Paper metadata
    llm_agents/
      ...
```

## Configuration

See `config.yaml.example` for all options:

| Section | Key | Description |
|---------|-----|-------------|
| `topics` | - | List of research keywords to track |
| `sources.arxiv` | `max_per_keyword`, `days_lookback` | ArXiv search parameters |
| `sources.nature` | `journals` | Nature journal RSS feed slugs |
| `sources.huggingface` | `max_papers` | Max papers from HF Daily |
| `ranking` | `top_k`, `archive_max` | Top-K for report, max archive per day |
| `llm` | `model`, `temperature` | LLM model and parameters |
| `email` | `enabled`, `smtp_server`, ... | SMTP email configuration |

## Requirements

- Python >= 3.11
- Azure OpenAI API access (GPT-4o or GPT-5)
- Internet access for ArXiv, Nature, and HuggingFace APIs

## License

MIT
