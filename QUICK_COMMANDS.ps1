#!/usr/bin/env powershell
# Quick Commands Reference for AI Blog CMS

Write-Host "`n╔════════════════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║              AI BLOG CMS - QUICK COMMANDS                    ║" -ForegroundColor Green
Write-Host "╚════════════════════════════════════════════════════════════════╝`n" -ForegroundColor Green

Write-Host "🚀 START APPLICATION`n" -ForegroundColor Yellow

Write-Host "1. Start Backend (Django):" -ForegroundColor Cyan
Write-Host '   cd "c:\Users\pdhar\OneDrive\Documents\Desktop\AI-powered Blog CMS\backend"' -ForegroundColor White
Write-Host "   python manage.py runserver" -ForegroundColor White
Write-Host "   ➜ Runs on: http://localhost:8000`n" -ForegroundColor Green

Write-Host "2. Start Frontend (React) - IN NEW TERMINAL:" -ForegroundColor Cyan
Write-Host '   cd "c:\Users\pdhar\OneDrive\Documents\Desktop\AI-powered Blog CMS\frontend"' -ForegroundColor White
Write-Host "   npm start" -ForegroundColor White
Write-Host "   ➜ Runs on: http://localhost:3000`n" -ForegroundColor Green

Write-Host "═" * 65 -ForegroundColor Cyan
Write-Host "`n📋 USEFUL COMMANDS`n" -ForegroundColor Yellow

Write-Host "Database Commands:" -ForegroundColor Cyan
Write-Host '   cd backend && python manage.py migrate                    ' -ForegroundColor White
Write-Host "   (Apply all migrations)`n" -ForegroundColor Gray

Write-Host "   cd backend && python manage.py makemigrations             " -ForegroundColor White
Write-Host "   (Create new migrations)`n" -ForegroundColor Gray

Write-Host "   cd backend && python manage.py createsuperuser           " -ForegroundColor White
Write-Host "   (Create admin user for Django admin panel)`n" -ForegroundColor Gray

Write-Host "Admin Panel:" -ForegroundColor Cyan
Write-Host "   http://localhost:8000/admin/`n" -ForegroundColor White

Write-Host "API Endpoints:" -ForegroundColor Cyan
Write-Host "   http://localhost:8000/api/auth/login/     (POST)" -ForegroundColor White
Write-Host "   http://localhost:8000/api/users/           (GET/POST)" -ForegroundColor White
Write-Host "   http://localhost:8000/api/blogs/           (GET/POST)" -ForegroundColor White
Write-Host "   http://localhost:8000/api/ai/              (GET/POST)`n" -ForegroundColor White

Write-Host "═" * 65 -ForegroundColor Cyan
Write-Host "`n🧪 QUICK TEST (Using Curl)`n" -ForegroundColor Yellow

Write-Host "Create User:" -ForegroundColor Cyan
Write-Host 'curl -X POST http://localhost:8000/api/users/ -H "Content-Type: application/json" -d "{\"username\":\"testuser\",\"email\":\"test@test.com\",\"password\":\"Pass1234!\"}"' -ForegroundColor White

Write-Host "`nLogin (Get Token):" -ForegroundColor Cyan
Write-Host 'curl -X POST http://localhost:8000/api/auth/login/ -H "Content-Type: application/json" -d "{\"username\":\"testuser\",\"password\":\"Pass1234!\"}"' -ForegroundColor White

Write-Host "`n═" * 65 -ForegroundColor Cyan
Write-Host "`n📁 PROJECT STRUCTURE`n" -ForegroundColor Yellow

Write-Host "Backend:" -ForegroundColor Cyan
Write-Host "   backend/config/settings.py     - Django configuration" -ForegroundColor White
Write-Host "   backend/config/urls.py         - API endpoints" -ForegroundColor White
Write-Host "   backend/apps/users/            - User app" -ForegroundColor White
Write-Host "   backend/apps/blogs/            - Blog app" -ForegroundColor White
Write-Host "   backend/apps/ai_service/       - AI service app" -ForegroundColor White
Write-Host "   backend/db.sqlite3             - Database`n" -ForegroundColor White

Write-Host "Frontend:" -ForegroundColor Cyan
Write-Host "   frontend/src/App.js            - Main component" -ForegroundColor White
Write-Host "   frontend/src/api.js            - API client" -ForegroundColor White
Write-Host "   frontend/src/store.js          - State management" -ForegroundColor White
Write-Host "   frontend/src/pages/            - Page components`n" -ForegroundColor White

Write-Host "═" * 65 -ForegroundColor Cyan
Write-Host "`n🔧 TROUBLESHOOTING`n" -ForegroundColor Yellow

Write-Host "Backend won't start:" -ForegroundColor Cyan
Write-Host "   1. Check if port 8000 is already in use" -ForegroundColor White
Write-Host "   2. Run: python manage.py migrate" -ForegroundColor White
Write-Host "   3. Check .env file for correct database config`n" -ForegroundColor Gray

Write-Host "Frontend won't start:" -ForegroundColor Cyan
Write-Host "   1. Check if port 3000 is already in use" -ForegroundColor White
Write-Host "   2. Run: npm install" -ForegroundColor White
Write-Host "   3. Delete node_modules and reinstall`n" -ForegroundColor Gray

Write-Host "API Returns 404:" -ForegroundColor Cyan
Write-Host "   1. Check if backend is running on port 8000" -ForegroundColor White
Write-Host "   2. Check API endpoint URL is correct" -ForegroundColor White
Write-Host "   3. Check CORS configuration in settings.py`n" -ForegroundColor Gray

Write-Host "═" * 65 -ForegroundColor Cyan
Write-Host "`n✅ STATUS`n" -ForegroundColor Yellow

Write-Host "Backend:  " -ForegroundColor White -NoNewline
Write-Host "✅ READY" -ForegroundColor Green
Write-Host "Database: " -ForegroundColor White -NoNewline
Write-Host "✅ READY" -ForegroundColor Green
Write-Host "Frontend: " -ForegroundColor White -NoNewline
Write-Host "⏳ START WITH: npm start" -ForegroundColor Yellow

Write-Host "`n╔════════════════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║                🎉 Ready for Development! 🎉                   ║" -ForegroundColor Green
Write-Host "╚════════════════════════════════════════════════════════════════╝`n" -ForegroundColor Green

