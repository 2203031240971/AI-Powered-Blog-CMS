@echo off
REM AI Blog CMS - Simple Launcher
REM This batch file starts both backend and frontend with one command

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║                                                                ║
echo ║     🚀 STARTING AI BLOG CMS - BACKEND & FRONTEND 🚀          ║
echo ║                                                                ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Get project root
set "projectRoot=%~dp0"
set "backendPath=%projectRoot%backend"
set "frontendPath=%projectRoot%frontend"

echo 📋 Starting services...
echo.

REM Terminal 1: Backend
echo ✅ Starting Django Backend on port 8000...
start "Django Backend - http://localhost:8000" cmd /k "cd /d "%backendPath%" && python manage.py runserver"

REM Wait a bit for backend to start
timeout /t 3 /nobreak

REM Terminal 2: Frontend
echo ✅ Starting React Frontend on port 3000...
start "React Frontend - http://localhost:3000" cmd /k "cd /d "%frontendPath%" && npm start"

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║                                                                ║
echo ║          ✅ BOTH SERVERS STARTING ✅                          ║
echo ║                                                                ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

echo 🌐 Services will be available at:
echo    Backend:  http://localhost:8000
echo    Frontend: http://localhost:3000
echo.

echo 📱 Open http://localhost:3000 in your browser!
echo.

echo ⏳ Waiting for services to fully start (30 seconds)...
timeout /t 30 /nobreak

echo.
echo ✨ Both servers should now be running!
echo    Frontend should auto-open in browser
echo.

echo 📝 Quick Start:
echo    1. Register a new account
echo    2. Login with credentials
echo    3. Start creating blog posts!
echo.

pause

