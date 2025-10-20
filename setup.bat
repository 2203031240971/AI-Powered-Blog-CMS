@echo off
REM Initial setup script for development on Windows

echo 🚀 AI-Powered Blog CMS - Development Setup
echo ==========================================

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.11+
    exit /b 1
)

REM Check Node
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js not found. Please install Node.js 18+
    exit /b 1
)

echo ✅ Python and Node.js found

REM Backend setup
echo.
echo 📦 Setting up backend...
cd backend

REM Create virtual environment
if not exist "venv" (
    python -m venv venv
    echo ✅ Virtual environment created
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install dependencies
pip install -r requirements.txt
echo ✅ Python dependencies installed

REM Copy .env if not exists
if not exist ".env" (
    copy .env.example .env
    echo ✅ .env file created - please edit with your configuration
)

REM Frontend setup
echo.
echo 📦 Setting up frontend...
cd ..\frontend

if not exist "node_modules" (
    call npm install
    echo ✅ Node dependencies installed
)

echo.
echo ==========================================
echo ✅ Setup complete!
echo.
echo Next steps:
echo 1. Edit backend\.env with your configuration
echo 2. Run: python manage.py migrate
echo 3. Run: python manage.py createsuperuser
echo 4. Run: python manage.py runserver
echo 5. In another terminal: cd frontend ^&^& npm start
echo.
echo Frontend: http://localhost:3000
echo Backend: http://localhost:8000
echo Admin: http://localhost:8000/admin
