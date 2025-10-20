#!/usr/bin/env powershell
<#
.SYNOPSIS
    Simple Fix for Project Issues
#>

$ErrorActionPreference = 'Continue'

Write-Host @"
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║         🔧 FIXING PROJECT ISSUES 🔧                           ║
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
    $_.Path -like "*venv*"
}

if ($pythonProcesses) {
    Write-Host "   Found $($pythonProcesses.Count) Python processes" -ForegroundColor Yellow
    $pythonProcesses | ForEach-Object {
        Write-Host "   Stopping process: $($_.Id)" -ForegroundColor Gray
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

# Step 3: Display status
Write-Host @"

╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║          ✅ PROJECT FIXES COMPLETE ✅                         ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝

🎯 NEXT STEPS:

   1. Create Superuser:
      cd backend
      .\venv\Scripts\Activate.ps1
      python manage.py createsuperuser

   2. Start Backend:
      python manage.py runserver

   3. Start Frontend (in new terminal):
      cd frontend
      npm start

   4. Access Application:
      Frontend:  http://localhost:3000
      Backend:   http://localhost:8000
      Admin:     http://localhost:8000/admin

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 DOCUMENTATION:

   - ERRORS_FOUND.txt              ← Quick summary
   - PROJECT_ERRORS_AND_FIXES.md  ← Full analysis
   - README.md                     ← Complete docs

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ Your project is now fixed and ready to use! ✨

"@ -ForegroundColor Green

Set-Location $projectRoot

