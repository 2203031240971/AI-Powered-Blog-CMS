# Quick Fix Guide - Links Not Working Issue

## ⚡ The Problem
When clicking links in the application, nothing happens or the page stays blank. This was caused by JWT authentication configuration mismatch.

## ✅ The Solution

### What Changed
- **Old:** `djangorestframework-jwt` (deprecated)
- **New:** `djangorestframework-simplejwt` (modern, maintained)

### Files Updated
1. **`backend/config/settings.py`** - REST Framework configuration
2. **`backend/config/urls.py`** - Authentication endpoints
3. **`frontend/src/api.js`** - API client interceptors
4. **`backend/apps/users/views.py`** - User permissions

### Token Format Change
```
OLD: Authorization: JWT eyJ0eXAi...
NEW: Authorization: Bearer eyJ0eXAi...
```

---

## 🚀 Quick Start (3 Steps)

### Step 1: Clean Install Backend
```bash
cd backend

# Remove old JWT package
pip uninstall -y djangorestframework-jwt

# Reinstall all packages
pip install -r requirements.txt
```

### Step 2: Prepare Database
```bash
# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser
# Enter: username, email, password (2x)
```

### Step 3: Start the Application
```bash
# Terminal 1: Start Backend
python manage.py runserver
# Backend runs on: http://localhost:8000

# Terminal 2: Start Frontend
cd frontend
npm start
# Frontend runs on: http://localhost:3000
```

---

## ✨ Test It Works

### Test in Browser
1. Go to `http://localhost:3000`
2. Click "Register" → Create account
3. Click "Login" → Login with credentials
4. Click "View Blogs" → See published blogs
5. All links should work now!

### Test with API (cURL)

**1. Register:**
```bash
curl -X POST http://localhost:8000/api/users/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "TestPass123!",
    "password2": "TestPass123!"
  }'
```

**2. Login:**
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "TestPass123!"
  }'
```

**3. Use Token (copy access token from response):**
```bash
curl -X GET http://localhost:8000/api/users/profile/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN_HERE"
```

---

## 🐛 Still Not Working?

### Check 1: Is Backend Running?
```bash
# Should return status 200
curl http://localhost:8000/admin/
```

### Check 2: Is Frontend Running?
```bash
# Should open React app
start http://localhost:3000
```

### Check 3: Check Console Errors
1. Open browser F12 (DevTools)
2. Go to Console tab
3. Look for red errors
4. Check Network tab for failed requests

### Check 4: Check Django Errors
Look at the Django terminal where you ran `python manage.py runserver`:
- Red errors = Django errors
- Most common: Database connection issue

### Check 5: Database Connection
```bash
# Check if database exists and has tables
python manage.py shell
>>> from django.db import connection
>>> connection.cursor()
```

---

## 📝 Key Configuration Files

### Backend Environment (`.env`)
```
DEBUG=True
SECRET_KEY=your-secret-key
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
```

### Frontend Environment (`.env`)
```
REACT_APP_API_URL=http://localhost:8000
```

---

## 🔗 API Endpoints Now Available

| Endpoint | Method | Auth | Purpose |
|----------|--------|------|---------|
| `/api/users/register/` | POST | ❌ | Register new user |
| `/api/auth/login/` | POST | ❌ | Get access token |
| `/api/auth/refresh/` | POST | ❌ | Refresh access token |
| `/api/users/profile/` | GET | ✅ | Get current user profile |
| `/api/blogs/blogs/` | GET | ❌ | List public blogs |
| `/api/blogs/blogs/` | POST | ✅ | Create blog (authors) |
| `/api/blogs/blogs/{id}/` | GET | ❌ | Get blog detail |

---

## 🆘 Common Issues & Solutions

| Issue | Cause | Fix |
|-------|-------|-----|
| 401 Unauthorized | Bad token format | Use `Bearer` not `JWT` |
| CORS Error | Frontend URL not in whitelist | Add to `CORS_ALLOWED_ORIGINS` |
| Database error | DB not running or wrong config | Check `.env` DB settings |
| Port in use | Port 8000 or 3000 already taken | Use different port or kill process |
| Blank page | Frontend can't reach backend | Check API URL in frontend `.env` |
| 404 errors | Migrations not applied | Run `python manage.py migrate` |

---

## 📚 Full Documentation

- **TROUBLESHOOTING.md** - Detailed troubleshooting guide (12 issues)
- **API_TESTING.md** - Complete API reference with all endpoints
- **START_HERE.md** - Project overview
- **QUICKSTART.md** - 5-minute setup guide
- **DEPLOYMENT.md** - Production deployment guide

---

## 💡 Tips

1. **Development:**
   - Use SQLite for local development (easier setup)
   - Use `DEBUG=True` to see error pages
   - Keep DevTools (F12) open in browser

2. **Debugging:**
   - Check Django console for backend errors
   - Check browser console for frontend errors
   - Use cURL to test API independently

3. **Performance:**
   - Restart both servers if changes don't appear
   - Clear browser cache (Ctrl+Shift+Del)
   - Check for Python syntax errors (pip install)

---

## ✅ Verification Checklist

After following this guide:

- [ ] Backend dependencies installed
- [ ] Database migrations applied
- [ ] Superuser created
- [ ] Backend server running (Terminal 1)
- [ ] Frontend server running (Terminal 2)
- [ ] Can register new user
- [ ] Can login with credentials
- [ ] Can view blogs without login
- [ ] Can create blog when logged in
- [ ] No console errors in browser

---

## 🎯 Next Steps

1. **Test the application** - Follow "Test It Works" section
2. **Create sample blogs** - Use admin or API
3. **Customize** - Modify styles, add features
4. **Deploy** - Follow DEPLOYMENT.md when ready

---

## 📞 Need Help?

1. Check **TROUBLESHOOTING.md** for your specific issue
2. Check **API_TESTING.md** to test endpoints
3. Review error messages in console/terminal
4. Try restarting both servers
5. Delete database and start fresh if needed

---

**Last Updated:** October 19, 2025
**Status:** ✅ Production Ready
