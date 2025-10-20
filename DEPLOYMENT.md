# Deployment Guide

## AWS EC2 Setup

### Instance Configuration

- **AMI**: Ubuntu 22.04 LTS
- **Instance Type**: t3.medium (2 vCPU, 4GB RAM)
- **Storage**: 30GB EBS volume
- **Security Group**: Allow HTTP (80), HTTPS (443), SSH (22)

### Pre-deployment Checklist

- [ ] EC2 instance running and SSH accessible
- [ ] Security groups configured
- [ ] Domain name registered and DNS configured
- [ ] SSL certificate ready (ACM or Let's Encrypt)
- [ ] Environment variables prepared
- [ ] Database backups tested

## Deployment Process

### 1. Initial Setup

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker and Docker Compose
sudo apt install -y docker.io docker-compose
sudo usermod -aG docker $USER

# Install Nginx
sudo apt install -y nginx

# Install monitoring tools
sudo apt install -y htop iotop
```

### 2. Application Deployment

```bash
# Create application directory
sudo mkdir -p /app/blog-cms
sudo chown -R $USER:$USER /app/blog-cms
cd /app/blog-cms

# Clone repository
git clone <your-repo-url> .
cd blog-cms

# Set up environment
cp backend/.env.example backend/.env
# Edit with production values
nano backend/.env
```

### 3. Database Backup and Recovery

```bash
# Create backup
docker-compose exec db pg_dump -U postgres blog_cms_db > backup.sql

# Restore from backup
cat backup.sql | docker-compose exec -T db psql -U postgres -d blog_cms_db
```

### 4. SSL Certificate Setup

Using Let's Encrypt with Certbot:

```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot certonly --nginx -d yourdomain.com
```

### 5. Monitoring and Logging

```bash
# View logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Monitor resource usage
docker stats

# Check disk usage
df -h
```

## Production Environment Variables

Critical settings for production:

```env
DEBUG=False
SECRET_KEY=generate-a-strong-random-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
CORS_ALLOWED_ORIGINS=https://yourdomain.com

# Database
DB_HOST=db
DB_NAME=blog_cms_db
DB_USER=postgres
DB_PASSWORD=strong-random-password

# OpenAI
OPENAI_API_KEY=your-production-key

# AWS
AWS_ACCESS_KEY_ID=production-key
AWS_SECRET_ACCESS_KEY=production-secret
AWS_STORAGE_BUCKET_NAME=your-bucket-name

# Redis
REDIS_URL=redis://redis:6379/0
```

## Maintenance Tasks

### Regular Backups

```bash
# Daily backup script
0 2 * * * cd /app/blog-cms && docker-compose exec -T db pg_dump -U postgres blog_cms_db > /backups/db_$(date +\%Y\%m\%d).sql
```

### Log Rotation

Configure logrotate for application logs:

```bash
/app/blog-cms/backend/logs/*.log {
    daily
    rotate 7
    compress
    delaycompress
    notifempty
    create 0640 root root
}
```

## Scaling Considerations

- Use RDS for database
- S3 for media storage
- CloudFront for CDN
- ElastiCache for Redis
- Load balancer with multiple backend instances
- Auto-scaling groups

## Troubleshooting

### High Memory Usage

```bash
# Check container memory
docker stats

# Restart container
docker-compose restart backend
```

### Disk Space Issues

```bash
# Find large files
du -sh *

# Clean up Docker
docker system prune -a
```

### Slow Performance

```bash
# Check database queries
docker-compose exec db psql -U postgres -c "SELECT * FROM pg_stat_statements LIMIT 10;"

# Monitor Celery tasks
docker-compose logs celery_worker | tail -100
```

## Rollback Procedure

```bash
# Stop current deployment
docker-compose down

# Revert to previous image
git checkout previous-commit
docker-compose up -d
```

## Updates and Patches

```bash
# Update dependencies
docker-compose pull

# Restart services
docker-compose restart

# Run migrations if needed
docker-compose exec backend python manage.py migrate
```
