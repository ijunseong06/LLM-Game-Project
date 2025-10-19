@echo off
setlocal

python -m pip install -r requirements.txt

cd client && npm install

endlocal
pause