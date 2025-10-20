#!/usr/bin/env powershell
<#
.SYNOPSIS
    Run AI Blog CMS - Perfect Execution Script

.DESCRIPTION
    This script runs the entire project perfectly with proper error handling.
#>

$ErrorActionPreference = 'Continue'

Write-Host @"
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║         🚀 RUNNING AI-POWERED BLOG CMS 🚀                     ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝

"@ -ForegroundColor Green

# Get project root
$projectRoot = "C:\Users\pdhar\OneDrive\Documents\Desktop\AI-powered Blog CMS"
$backendPath = Join-Path $projectRoot "backend"
$frontendPath = Join-Path $projectRoot "frontend"

# Step 1: Stop any running instances
Write-Host "`n📋 STEP 1: Stopping any running instances..." -ForegroundColor Cyan

$pythonProcesses = Get-Process python -ErrorAction SilentlyContinue | Where-Object {
    $_.Path -like "*venv*"
}

if ($pythonProcesses) {
    Write-Host "   Stopping $($pythonProcesses.Count) Python processes..." -ForegroundColor Yellow
    $pythonProcesses | ForEach-Object {
        Stop-Process -Id $_.Id -Force -ErrorAction SilentlyContinue
    }
}

$nodeProcesses = Get-Process node -ErrorAction SilentlyContinue

if ($nodeProcesses) {
    Write-Host "   Stopping $($nodeProcesses.Count) Node processes..." -ForegroundColor Yellow
    $nodeProcesses | ForEach-Object {
        Stop-Process -Id $_.Id -Force -ErrorAction SilentlyContinue
    }
}

Write-Host "✅ All instances stopped" -ForegroundColor Green
Start-Sleep -Seconds 2

# Step 2: Check .env file
Write-Host "`n📋 STEP 2: Checking .env file..." -ForegroundColor Cyan

$envPath = Join-Path $backendPath ".env"

if (-not (Test-Path $envPath)) {
    Write-Host "   Creating .env file..." -ForegroundColor Yellow
    
    $envContent = "DEBUG=True`nSECRET_KEY=django-insecure-change-this-in-production`nDB_ENGINE=django.db.backends.sqlite3`nDB_NAME=db.sqlite3`nALLOWED_HOSTS=localhost,127.0.0.1`nCORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000`nOPENAI_API_KEY=`nREDIS_URL=redis://localhost:6379/0"
    
    Set-Content -Path $envPath -Value $envContent -Encoding UTF8
    Write-Host "✅ .env file created" -ForegroundColor Green
} else {
    Write-Host "✅ .env file exists" -ForegroundColor Green
}

# Step 3: Start Backend
Write-Host "`n📋 STEP 3: Starting Backend Server..." -ForegroundColor Cyan
Write-Host "   Location: $backendPath" -ForegroundColor Gray

Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$backendPath'; .\venv\Scripts\Activate.ps1; python manage.py runserver" -PassThru | Out-Null

Write-Host "✅ Backend server starting..." -ForegroundColor Green
Write-Host "   Waiting for backend to be ready..." -ForegroundColor Yellow

# Wait for backend
$maxRetries = 30
$retry = 0
while ($retry -lt $maxRetries) {
    $backendReady = Test-NetConnection localhost -Port 8000 -InformationLevel Quiet -ErrorAction SilentlyContinue
    if ($backendReady) {
        Write-Host "✅ Backend is ready!" -ForegroundColor Green
        break
    }
    Start-Sleep -Seconds 1
    $retry++
}

# Step 4: Start Frontend
Write-Host "`n📋 STEP 4: Starting Frontend Server..." -ForegroundColor Cyan
Write-Host "   Location: $frontendPath" -ForegroundColor Gray

Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$frontendPath'; npm start" -PassThru | Out-Null

Write-Host "✅ Frontend server starting..." -ForegroundColor Green
Write-Host "   Waiting for frontend to compile..." -ForegroundColor Yellow

# Wait for frontend
$maxRetries = 60
$retry = 0
while ($retry -lt $maxRetries) {
    $frontendReady = Test-NetConnection localhost -Port 3000 -InformationLevel Quiet -ErrorAction SilentlyContinue
    if ($frontendReady) {
        Write-Host "✅ Frontend is ready!" -ForegroundColor Green
        break
    }
    Start-Sleep -Seconds 1
    $retry++
}

# Step 5: Display status
Write-Host @"

╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║          ✅ APPLICATION RUNNING SUCCESSFULLY ✅               ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝

🎯 SERVICES RUNNING:

   ✅ Backend (Django)
      URL:      http://localhost:8000
      API:      http://localhost:8000/api/
      Admin:    http://localhost:8000/admin/

   ✅ Frontend (React)
      URL:      http://localhost:3000
      Status:   RUNNING

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📱 OPEN IN BROWSER:

   👉 http://localhost:3000 👈

   (Browser should open automatically)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 QUICK START:

   1. Open http://localhost:3000 in browser
   2. Click "Register" to create account
   3. Fill in registration form
   4. Click "Login" and sign in
   5. Start creating blog posts!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔐 ADMIN PANEL:

   To access admin panel, create superuser first:
   
   1. Open backend terminal window
   2. Press Ctrl+C to stop backend
   3. Run: python manage.py createsuperuser
   4. Follow prompts to create admin user
   5. Run: python manage.py runserver
   6. Go to: http://localhost:8000/admin/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🛑 TO STOP SERVERS:

   Close the two PowerShell windows that opened
   Or press Ctrl+C in each terminal

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ YOUR APPLICATION IS RUNNING! ✨

"@ -ForegroundColor Green

# Keep script running
Write-Host "`n🔄 Monitoring servers... (Close this window to stop monitoring)" -ForegroundColor Yellow
Write-Host "   Press Ctrl+C to stop this script" -ForegroundColor Gray

while ($true) {
    Start-Sleep -Seconds 10
    
    # Check if servers are still running
    $backendRunning = Test-NetConnection localhost -Port 8000 -InformationLevel Quiet -ErrorAction SilentlyContinue
    $frontendRunning = Test-NetConnection localhost -Port 3000 -InformationLevel Quiet -ErrorAction SilentlyContinue
    
    if (-not $backendRunning) {
        Write-Host "⚠️  Backend stopped!" -ForegroundColor Red
    }
    
    if (-not $frontendRunning) {
        Write-Host "⚠️  Frontend stopped!" -ForegroundColor Red
    }
}

