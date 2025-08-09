# MindChat

Minimal SaaS MVP with FastAPI and RQ worker ready for Render deploy.

## Run locally
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export DATABASE_URL=sqlite:///./dev.db
uvicorn app.main:app --reload
```
Then in another terminal run the worker:
```bash
python -m app.workers.run
```
Test the health endpoint:
```bash
curl http://127.0.0.1:8000/health
```

## Deploy on Render
1. Push this repo to GitHub.
2. In Render dashboard: **New -> Blueprint** and select the repo.
3. Add environment variables (`DATABASE_URL`, `REDIS_URL`, etc.).
4. Deploy; services defined in `render.yaml` will start (web, worker, Postgres, Redis).
5. Render will run `alembic upgrade head` after deploy.

## Notes
- BYOK for DeepSeek supported via `api_key` in chat requests.
- FAISS indexes stored in `/data/faiss/{tenant}/{workspace}.index`.
