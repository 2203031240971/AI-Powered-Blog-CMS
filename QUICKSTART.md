# Quick Start Guide

## Prerequisites Checklist

- [ ] Python 3.11+ installed
- [ ] Node.js 18+ installed
- [ ] Docker and Docker Compose installed
- [ ] PostgreSQL and Redis installed (or using Docker)
- [ ] OpenAI API key obtained
- [ ] Git installed

## One-Command Docker Setup (Recommended)

```bash
# From project root
docker-compose up -d

# Wait for services to start
sleep 10

# Create superuser
docker-compose exec backend python manage.py createsuperuser

# Access:
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# Admin Panel: http://localhost:8000/admin
```

## Local Development Setup (5 minutes)

### Step 1: Backend Setup (2 minutes)

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy and configure environment
cp .env.example .env
# Edit .env - set DEBUG=True, SECRET_KEY, DB_PASSWORD, OPENAI_API_KEY

# Initialize database
python manage.py migrate
python manage.py createsuperuser

# Start server
python manage.py runserver
```

### Step 2: Frontend Setup (2 minutes)

```bash
cd frontend
npm install
npm start
```

Frontend will open at `http://localhost:3000`

### Step 3: Test Installation

```bash
# Backend API test
curl http://localhost:8000/api/users/profile/ \
  -H "Authorization: JWT your-token"

# Frontend loads at http://localhost:3000
```

## Environment Configuration

### Minimal Configuration (.env)

```env
DEBUG=True
SECRET_KEY=change-this-to-random-value
OPENAI_API_KEY=sk-...your-key...
DB_PASSWORD=postgres
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

### Production Configuration

```env
DEBUG=False
SECRET_KEY=very-long-random-string
OPENAI_API_KEY=sk-...production-key...
DB_HOST=your-db-host
DB_PASSWORD=very-strong-password
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
CORS_ALLOWED_ORIGINS=https://yourdomain.com
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_STORAGE_BUCKET_NAME=your-bucket
```

## Common Commands

### Database

```bash
# Create migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Backup database
docker-compose exec db pg_dump -U postgres blog_cms_db > backup.sql

# Restore database
cat backup.sql | docker-compose exec -T db psql -U postgres -d blog_cms_db
```

### Backend Server

```bash
# Development server
python manage.py runserver

# Production with Gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000

# Celery worker (in separate terminal)
celery -A config worker -l info

# Celery beat scheduler (in separate terminal)
celery -A config beat -l info
```

### Frontend

```bash
# Development
npm start

# Production build
npm run build

# Run tests
npm test
```

### Docker

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f backend

# Execute command in container
docker-compose exec backend python manage.py migrate

# Rebuild containers
docker-compose up -d --build
```

## API Usage Examples

### Authentication

```bash
# Login
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"password"}'

# Response: {"token": "jwt-token-here"}
```

### Create Blog Post

```bash
curl -X POST http://localhost:8000/api/blogs/blogs/ \
  -H "Authorization: JWT your-token" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Blog",
    "description": "A great article",
    "content": "# Hello\n\nThis is my blog post",
    "status": "published"
  }'
```

### Get AI Summary

```bash
curl -X GET http://localhost:8000/api/blogs/blogs/1/generate_summary/ \
  -H "Authorization: JWT your-token"
```

## Troubleshooting

### Port Already in Use

```bash
# Kill process using port 8000
# On Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# On Mac/Linux
lsof -ti:8000 | xargs kill -9
```

### Database Connection Error

```bash
# Check PostgreSQL is running
docker-compose logs db

# Recreate database
docker-compose down -v
docker-compose up -d
```

### Module Not Found Error

```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Or in Docker
docker-compose exec backend pip install -r requirements.txt
```

### CORS Error

Update `CORS_ALLOWED_ORIGINS` in `.env`:

```env
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
```

## Next Steps

1. ✅ Local setup complete
2. 📝 Create first blog post
3. 🤖 Set up OpenAI integration
4. 🎨 Customize frontend theme
5. 🚀 Deploy to AWS EC2

## Documentation

- **API Documentation**: See README.md
- **Deployment Guide**: See DEPLOYMENT.md
- **Architecture Overview**: See ARCHITECTURE.md
- **Database Schema**: See models.py files

## Getting Help

- Check logs: `docker-compose logs -f backend`
- Test API: Use Postman or curl
- Read Django docs: https://docs.djangoproject.com/
- Read React docs: https://react.dev/
- Check OpenAI docs: https://platform.openai.com/docs/

## Support

For issues:
1. Check troubleshooting section above
2. Review application logs
3. Verify environment configuration
4. Test API endpoints manually
5. Search GitHub issues
6. Create new issue with detailed error message

---

**Ready to build your AI-powered blog CMS?** Let's go! 🚀
