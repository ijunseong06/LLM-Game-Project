@echo off

start "FastAPI Server" cmd /k "cd /d server && uvicorn app:app --reload --port 8000 --workers 1"

start "Flutter APP" cmd /k "cd /d client && npm run dev"