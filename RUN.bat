@echo off
echo.
echo ========================================
echo   AI-POWERED BLOG CMS - STARTING
echo ========================================
echo.

echo [1/4] Stopping any running servers...
taskkill /F /IM python.exe /FI "WINDOWTITLE eq *manage.py*" 2>nul
taskkill /F /IM node.exe 2>nul
timeout /t 2 /nobreak >nul

echo [2/4] Starting Backend Server...
start "Backend Server" cmd /k "cd /d %~dp0backend && venv\Scripts\activate && python manage.py runserver"

echo [3/4] Waiting for backend to start...
timeout /t 10 /nobreak >nul

echo [4/4] Starting Frontend Server...
start "Frontend Server" cmd /k "cd /d %~dp0frontend && npm start"

echo.
echo ========================================
echo   APPLICATION STARTED SUCCESSFULLY!
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3000
echo Admin:    http://localhost:8000/admin
echo.
echo Two windows will open - one for backend, one for frontend
echo Close those windows to stop the servers
echo.
echo Opening browser...
start http://localhost:3000
echo.
pause

