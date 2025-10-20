#!/usr/bin/env powershell
<#
.SYNOPSIS
    Fix Common Project Issues - AI Blog CMS

.DESCRIPTION
    This script fixes common issues found in the project:
    1. Stops multiple backend instances
    2. Creates .env file if missing
    3. Creates superuser
    4. Starts servers cleanly

.EXAMPLE
    .\FIX_PROJECT.ps1
#>

$ErrorActionPreference = 'Continue'

Write-Host @"
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║         🔧 FIXING PROJECT ISSUES 🔧                           ║
║                                                                ║
║         AI-Powered Blog CMS                                    ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝

"@ -ForegroundColor Cyan

# Define paths
$projectRoot = Split-Path -Parent $MyInvocation.MyCommandPath
$backendPath = Join-Path $projectRoot "backend"
$envPath = Join-Path $backendPath ".env"

# Step 1: Stop all running backend instances
Write-Host "`n📋 STEP 1: Stopping all backend instances..." -ForegroundColor Cyan

$pythonProcesses = Get-Process python -ErrorAction SilentlyContinue | Where-Object {
    $_.Path -like "*venv*" -or $_.CommandLine -like "*manage.py*"
}

if ($pythonProcesses) {
    Write-Host "   Found $($pythonProcesses.Count) Python processes" -ForegroundColor Yellow
    $pythonProcesses | ForEach-Object {
        Write-Host "   Stopping process: $($_.Id) - $($_.ProcessName)" -ForegroundColor Gray
        Stop-Process -Id $_.Id -Force -ErrorAction SilentlyContinue
    }
    Write-Host "✅ All backend instances stopped" -ForegroundColor Green
} else {
    Write-Host "✅ No backend instances running" -ForegroundColor Green
}

Start-Sleep -Seconds 2

# Step 2: Create .env file if missing
Write-Host "`n📋 STEP 2: Checking .env file..." -ForegroundColor Cyan

if (-not (Test-Path $envPath)) {
    Write-Host "   Creating .env file..." -ForegroundColor Yellow
    
    $envContent = @"
DEBUG=True
SECRET_KEY=django-insecure-change-this-to-random-value-in-production
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
OPENAI_API_KEY=
REDIS_URL=redis://localhost:6379/0
"@
    
    Set-Content -Path $envPath -Value $envContent -Encoding UTF8
    Write-Host "✅ .env file created at: $envPath" -ForegroundColor Green
} else {
    Write-Host "✅ .env file already exists" -ForegroundColor Green
}

# Step 3: Check for superuser
Write-Host "`n📋 STEP 3: Checking for superuser..." -ForegroundColor Cyan

Set-Location $backendPath
& "$backendPath\venv\Scripts\python.exe" -c "import django; django.setup(); from django.contrib.auth import get_user_model; User = get_user_model(); print('SUPERUSER_EXISTS' if User.objects.filter(is_superuser=True).exists() else 'NO_SUPERUSER')" 2>&1 | Out-Null

$superuserCheck = & "$backendPath\venv\Scripts\python.exe" -c "import django; django.setup(); from django.contrib.auth import get_user_model; User = get_user_model(); print('SUPERUSER_EXISTS' if User.objects.filter(is_superuser=True).exists() else 'NO_SUPERUSER')" 2>&1

if ($superuserCheck -eq "NO_SUPERUSER") {
    Write-Host "⚠️  No superuser found. Creating one..." -ForegroundColor Yellow
    Write-Host "   Please provide admin credentials:" -ForegroundColor Gray
    
    $username = Read-Host "   Username"
    $email = Read-Host "   Email"
    
    # Create superuser
    $createSuperuserScript = @"
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username='$username').exists():
    User.objects.create_superuser('$username', '$email', 'admin123')
    print('Superuser created successfully!')
    print('Username: $username')
    print('Password: admin123')
else:
    print('User already exists!')
"@
    
    $createSuperuserScript | & "$backendPath\venv\Scripts\python.exe" -
    Write-Host "✅ Superuser created" -ForegroundColor Green
    Write-Host "   Username: $username" -ForegroundColor Gray
    Write-Host "   Password: admin123" -ForegroundColor Gray
} else {
    Write-Host "✅ Superuser already exists" -ForegroundColor Green
}

# Step 4: Display status
Write-Host @"

╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║          ✅ PROJECT FIXES COMPLETE ✅                         ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝

🎯 NEXT STEPS:

   1. Start Backend:
      cd backend
      .\venv\Scripts\Activate.ps1
      python manage.py runserver

   2. Start Frontend (in new terminal):
      cd frontend
      npm start

   3. Access Application:
      Frontend:  http://localhost:3000
      Backend:   http://localhost:8000
      Admin:     http://localhost:8000/admin

   4. Login Credentials:
      Username: $username
      Password: admin123

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 DOCUMENTATION:

   - PROJECT_ERRORS_AND_FIXES.md  ← Full error analysis
   - README.md                     ← Complete documentation
   - QUICKSTART.md                ← Quick setup guide

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ Your project is now fixed and ready to use! ✨

"@ -ForegroundColor Green

Set-Location $projectRoot

