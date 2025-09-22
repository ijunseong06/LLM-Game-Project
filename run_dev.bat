@echo off

start "FastAPI Server" cmd /k "cd /d server && uvicorn app:app --reload"

start "Flutter APP" cmd /k "cd /d client && npm run dev"