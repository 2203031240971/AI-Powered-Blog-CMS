# Troubleshooting Guide - AI-Powered Blog CMS

## Common Issues and Solutions

### 1. **Links Not Working / No Output in Browser**

#### Problem
When clicking links in the application, nothing happens or the page stays blank.

#### Solution
This is usually caused by JWT authentication configuration mismatch. We've updated the project to use `djangorestframework-simplejwt` instead of the older JWT package.

**Steps to Fix:**

1. **Clear Cache and Reinstall Dependencies:**
   ```bash
   cd backend
   pip uninstall -y djangorestframework-jwt
   pip install -r requirements.txt
   ```

2. **Update Environment File:**
   ```bash
   # Copy example to actual .env file
   copy .env.example .env  # Windows
   cp .env.example .env    # Mac/Linux
   ```

3. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Create Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

5. **Restart Django Server:**
   - Kill any running Django processes
   - Run: `python manage.py runserver`

---

### 2. **401 Unauthorized Errors**

#### Problem
Getting 401 errors when trying to access protected endpoints.

#### Cause
Token format changed from `JWT <token>` to `Bearer <token>` in SimpleJWT.

#### Solution
The frontend API has been updated to use `Bearer` format. Make sure you're using the latest `api.js`:
- Check that `Authorization: Bearer ${token}` is in the header
- The token should be stored as `access_token` in localStorage
- The refresh token should be stored as `refresh_token`

---

### 3. **CORS Errors in Browser Console**

#### Problem
```
Access to XMLHttpRequest has been blocked by CORS policy
```

#### Solution
1. Ensure CORS_ALLOWED_ORIGINS in `backend/config/settings.py` includes:
   ```python
   CORS_ALLOWED_ORIGINS = [
       'http://localhost:3000',
       'http://localhost:8000',
   ]
   ```

2. Clear browser cache and restart both servers

3. Check browser DevTools → Network tab for actual CORS errors

---

### 4. **Database Connection Error**

#### Problem
```
could not connect to server: Connection refused
```

#### Solution
1. **Check if PostgreSQL is running:**
   - Windows: Use Services app or `net start postgresql-x64-15`
   - Mac: `brew services start postgresql@15`
   - Linux: `sudo service postgresql start`

2. **Or use SQLite for local development:**
   Edit `backend/config/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

3. **Configure .env correctly:**
   ```
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=blog_cms_db
   DB_USER=postgres
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

---

### 5. **Frontend Not Loading**

#### Problem
React app shows blank page or errors in console.

#### Solution
1. **Check if frontend is running:**
   ```bash
   cd frontend
   npm start
   ```

2. **Clear Node cache:**
   ```bash
   rm -rf node_modules package-lock.json  # Mac/Linux
   rmdir /s node_modules && del package-lock.json  # Windows
   npm install
   npm start
   ```

3. **Check backend is running:**
   ```bash
   cd backend
   python manage.py runserver
   ```

4. **Ensure REACT_APP_API_URL is correct:**
   Create `.env` in frontend folder:
   ```
   REACT_APP_API_URL=http://localhost:8000
   ```

---

### 6. **Celery Tasks Not Running**

#### Problem
AI summarization or background tasks don't execute.

#### Solution
1. **Start Redis:**
   - Windows: `redis-server`
   - Mac: `brew services start redis`
   - Linux: `sudo service redis-server start`

2. **Start Celery Worker:**
   ```bash
   cd backend
   celery -A config worker -l info
   ```

3. **Start Celery Beat (for scheduled tasks):**
   ```bash
   celery -A config beat -l info
   ```

---

### 7. **Static Files Not Loading (CSS/JS)**

#### Problem
CSS and JavaScript files return 404 errors.

#### Solution
1. **Collect static files:**
   ```bash
   python manage.py collectstatic --noinput
   ```

2. **Ensure DEBUG is True in development:**
   ```
   DEBUG=True
   ```

3. **Check STATIC_URL in settings:**
   ```python
   STATIC_URL = '/static/'
   STATIC_ROOT = BASE_DIR / 'staticfiles'
   ```

---

### 8. **Login/Register Not Working**

#### Problem
Form submission fails or redirects don't work.

#### Solution
1. **Check API endpoints are accessible:**
   ```bash
   # Test login endpoint
   curl -X POST http://localhost:8000/api/auth/login/ \
     -H "Content-Type: application/json" \
     -d '{"username":"admin","password":"password"}'
   ```

2. **Verify user exists:**
   ```bash
   python manage.py shell
   >>> from django.contrib.auth.models import User
   >>> User.objects.all()
   ```

3. **Check token response format:**
   SimpleJWT returns:
   ```json
   {
     "access": "eyJ0eXAi...",
     "refresh": "eyJ0eXAi..."
   }
   ```

---

### 9. **OpenAI API Not Working**

#### Problem
AI summarization fails or returns errors.

#### Solution
1. **Set OpenAI API Key:**
   Add to `.env`:
   ```
   OPENAI_API_KEY=sk-your-api-key-here
   ```

2. **Test API connection:**
   ```bash
   python manage.py shell
   >>> from apps.ai_service.service import AIService
   >>> AIService.summarize("sample text")
   ```

3. **Check Celery logs for errors**

---

### 10. **Port Already in Use**

#### Problem
```
Address already in use
```

#### Solution
1. **Change port:**
   ```bash
   # Backend on different port
   python manage.py runserver 8001
   
   # Frontend on different port
   npm start -- --port 3001
   ```

2. **Kill process using port:**
   - Windows: `netstat -ano | findstr :8000` then `taskkill /PID <PID> /F`
   - Mac/Linux: `lsof -i :8000` then `kill -9 <PID>`

---

### 11. **API Returns Empty Data**

#### Problem
API endpoints return empty lists or null values.

#### Solution
1. **Check if you have data in database:**
   ```bash
   python manage.py shell
   >>> from apps.blogs.models import Blog
   >>> Blog.objects.all()
   ```

2. **Check permissions:**
   - Some endpoints require authentication
   - Ensure you're sending Authorization header

3. **Check filters and pagination:**
   - Default page size is 10
   - Add `?page=2` to get next page

---

### 12. **Permission Denied (403) Errors**

#### Problem
```
"detail": "Permission denied"
```

#### Solution
1. **Check user permissions:**
   - Admin-only endpoints require `is_staff=True`
   - Some endpoints require the user to be the owner

2. **Update user as admin:**
   ```bash
   python manage.py shell
   >>> from apps.users.models import User
   >>> user = User.objects.get(username='admin')
   >>> user.is_staff = True
   >>> user.is_superuser = True
   >>> user.save()
   ```

3. **Check role-based access:**
   - Blog creation might require specific role
   - Admin dashboard requires admin role

---

## Quick Debugging Checklist

- [ ] Django server running: `python manage.py runserver`
- [ ] React frontend running: `npm start`
- [ ] PostgreSQL/SQLite database running
- [ ] Redis running (for Celery)
- [ ] `.env` file configured
- [ ] Migrations applied: `python manage.py migrate`
- [ ] CORS settings correct
- [ ] Browser cache cleared
- [ ] Correct API URL in frontend `.env`
- [ ] Bearer token format in headers

## Getting Help

1. **Check Django logs:**
   ```bash
   tail -f backend/logs/django.log
   ```

2. **Check browser console:**
   - F12 → Console tab
   - Look for JavaScript errors or API errors

3. **Check backend console output:**
   - Look for Django error traceback
   - Check request/response logs

4. **Enable debug mode:**
   - Set `DEBUG=True` in `.env`
   - Visit error page for detailed traceback

---

## Still Having Issues?

If you've tried all above steps:

1. **Restart everything:**
   ```bash
   # Kill all processes
   # Restart PostgreSQL
   # Restart Redis
   # Restart Django
   # Restart React
   ```

2. **Reset database:**
   ```bash
   # CAUTION: This deletes all data
   python manage.py migrate 0001
   python manage.py migrate
   python manage.py createsuperuser
   ```

3. **Fresh install:**
   ```bash
   # Backend
   rm -rf venv
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   
   # Frontend
   rm -rf node_modules package-lock.json
   npm install
   ```

---

## Contact & Support

For issues specific to:
- **Django**: Check [Django Documentation](https://docs.djangoproject.com)
- **React**: Check [React Documentation](https://react.dev)
- **DRF**: Check [DRF Documentation](https://www.django-rest-framework.org)
- **SimpleJWT**: Check [SimpleJWT Documentation](https://django-rest-framework-simplejwt.readthedocs.io)
