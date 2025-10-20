# 🤖 AI-Powered Blog CMS

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2+-green?logo=django&logoColor=white)
![React](https://img.shields.io/badge/React-18.0+-61DAFB?logo=react&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Production_Ready-success)

**A modern, full-stack Content Management System with AI-powered blog summarization**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 📌 **Project Overview**

This project is a **full-stack Content Management System (CMS)** designed for creating, managing, and publishing blogs — but with a modern twist: it uses **AI to generate blog summaries** and assist in content writing.

Built with **Django REST Framework** (backend) and **React** (frontend), this application demonstrates professional software engineering practices including:
- RESTful API design
- JWT authentication & role-based access control
- AI integration (OpenAI GPT)
- Modern React state management (Zustand)
- Production-ready deployment architecture

---

## ✨ **Key Features**

### 🔐 **Authentication & Authorization**
- ✅ JWT-based authentication with automatic token refresh
- ✅ Role-based access control (Admin, Author, Reader)
- ✅ Secure password hashing with bcrypt
- ✅ Protected routes and permission-based API endpoints

### 📝 **Blog Management**
- ✅ Create, read, update, and delete blog posts
- ✅ Rich text editor for content creation
- ✅ Draft and published states
- ✅ Category and tag management
- ✅ Image upload and management
- ✅ Blog search and filtering
- ✅ View count tracking
- ✅ SEO-friendly slug generation

### 🤖 **AI-Powered Features**
- ✅ **Automatic blog summarization** using OpenAI GPT-3.5/4
- ✅ Generate 150-word summaries with one click
- ✅ AI-assisted content rephrasing
- ✅ Intelligent tag suggestions
- ✅ Asynchronous AI processing (no blocking)

### 👥 **User Features**
- ✅ User registration and profile management
- ✅ Personal dashboard for authors
- ✅ View own blog statistics
- ✅ Comment system (with nested replies)
- ✅ Like and share functionality

### 🎨 **Modern UI/UX**
- ✅ Responsive design with Tailwind CSS
- ✅ Mobile-friendly interface
- ✅ Real-time notifications (toast messages)
- ✅ Loading states and error handling
- ✅ Intuitive navigation

### ⚙️ **DevOps & Deployment**
- ✅ Docker containerization
- ✅ Docker Compose for multi-container setup
- ✅ CI/CD pipeline with GitHub Actions
- ✅ Production deployment on AWS EC2
- ✅ Nginx reverse proxy configuration

---

## 🏗️ **System Architecture**

```
┌──────────────────────────────────────────────────────────────┐
│                    React Frontend (Port 3000)                 │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  Components: BlogEditor, BlogList, Dashboard, etc.     │  │
│  │  State: Zustand (global state management)              │  │
│  │  HTTP Client: Axios with JWT interceptors              │  │
│  └────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
                              │
                  HTTP/HTTPS (REST API)
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│            Django REST Framework Backend (Port 8000)          │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  Apps: users, blogs, ai_service                        │  │
│  │  Auth: JWT (djangorestframework-simplejwt)             │  │
│  │  API: RESTful endpoints with permissions               │  │
│  └────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
        ┌────────────────┐       ┌────────────────┐
        │   SQLite/      │       │   OpenAI API   │
        │  PostgreSQL    │       │   (GPT-3.5/4)  │
        └────────────────┘       └────────────────┘
```

### **Tech Stack**

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | React 18, Tailwind CSS, Zustand | User interface & state management |
| **Backend** | Django 4.2, Django REST Framework | API & business logic |
| **Database** | SQLite (dev), PostgreSQL (prod) | Data persistence |
| **Authentication** | JWT (SimpleJWT) | Secure token-based auth |
| **AI Service** | OpenAI GPT-3.5/4 | Content summarization |
| **HTTP Client** | Axios | API communication |
| **Containerization** | Docker, Docker Compose | Environment consistency |
| **Deployment** | AWS EC2, Nginx | Production hosting |

---

## 🎯 **How It Works**

### **Complete Workflow: From User to AI**

```
1. User Registration
   │
   ▼
2. Login (Receive JWT tokens)
   │
   ▼
3. Create Blog Post
   │  - Enter title, content, category
   │  - Upload images
   │
   ▼
4. Click "Generate AI Summary"
   │
   ▼
5. Backend sends content to OpenAI API
   │
   ▼
6. AI returns 150-word summary
   │
   ▼
7. Summary saved to database
   │
   ▼
8. User publishes blog
   │
   ▼
9. Readers see blog with AI summary
```

**Detailed Explanation:**  
📖 See [PROJECT_WORKFLOW.md](PROJECT_WORKFLOW.md) for comprehensive flow diagrams

---

## 📸 **Demo**

### **Screenshots**

<details>
<summary>🖼️ Click to view screenshots</summary>

#### Homepage
```
┌────────────────────────────────────────────────────┐
│  🏠 AI-Powered Blog CMS                  [Login]   │
├────────────────────────────────────────────────────┤
│                                                     │
│  📝 Latest Blogs                                   │
│                                                     │
│  ┌──────────────────────────────────────────────┐ │
│  │ [Blog Image]                                  │ │
│  │                                               │ │
│  │ Understanding JWT Authentication             │ │
│  │ By john_doe • Oct 19, 2025 • 5 min read     │ │
│  │                                               │ │
│  │ 🤖 AI Summary: JWT is a compact, URL-safe    │ │
│  │ means of representing claims...              │ │
│  │                                               │ │
│  │ #Security #Backend #Authentication           │ │
│  │                                               │ │
│  │ [Read More →]                                 │ │
│  └──────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────┘
```

#### Blog Editor with AI
```
┌────────────────────────────────────────────────────┐
│  Create New Blog                                    │
├────────────────────────────────────────────────────┤
│  Title: [How to Build a REST API                ]  │
│                                                     │
│  Content:                                          │
│  ┌──────────────────────────────────────────────┐ │
│  │ # Introduction                                │ │
│  │ REST APIs are the backbone of modern...      │ │
│  └──────────────────────────────────────────────┘ │
│                                                     │
│  [🤖 Generate AI Summary]                          │
│                                                     │
│  AI Summary:                                       │
│  ┌──────────────────────────────────────────────┐ │
│  │ This article explains how to build REST      │ │
│  │ APIs using Django REST Framework...          │ │
│  └──────────────────────────────────────────────┘ │
│                                                     │
│  [Save Draft]  [Publish Now]                       │
└────────────────────────────────────────────────────┘
```

</details>

---

## 📂 **Project Structure**

```
AI-powered Blog CMS/
│
├── 📁 backend/                 # Django REST Framework Backend
│   ├── apps/
│   │   ├── users/             # User authentication & profiles
│   │   ├── blogs/             # Blog CRUD operations
│   │   └── ai_service/        # OpenAI integration
│   ├── config/                # Django settings
│   ├── manage.py
│   └── requirements.txt
│
├── 📁 frontend/                # React Frontend
│   ├── src/
│   │   ├── components/        # Reusable components
│   │   ├── pages/             # Page components
│   │   ├── api.js             # Axios HTTP client
│   │   └── store.js           # Zustand state management
│   ├── package.json
│   └── tailwind.config.js
│
├── 📁 docker/                  # Docker configuration
│   ├── Dockerfile.backend
│   ├── Dockerfile.frontend
│   └── docker-compose.yml
│
├── 📁 Documentation/
│   ├── PROJECT_WORKFLOW.md    # Complete workflow diagrams
│   ├── UML_DIAGRAMS.md        # Architecture & UML diagrams
│   ├── CODE_STRUCTURE.md      # Codebase organization
│   ├── API_DOCUMENTATION.md   # Complete API reference
│   └── BLOG_CONTENT_GUIDE.md  # Content creation guide
│
└── README.md                   # This file
```

**📚 Detailed Code Structure:**  
See [CODE_STRUCTURE.md](CODE_STRUCTURE.md) for in-depth explanation of every file

---

## 🚀 **Installation & Setup**

### **Prerequisites**

Before you begin, ensure you have the following installed:

| Software | Version | Purpose |
|----------|---------|---------|
| Python | 3.11+ | Backend runtime |
| Node.js | 18+ | Frontend runtime |
| npm | 9+ | Package manager |
| Git | Latest | Version control |
| (Optional) Docker | Latest | Containerization |

---

### **Quick Start (Development)**

#### **1. Clone the Repository**

```powershell
git clone https://github.com/yourusername/ai-blog-cms.git
cd ai-blog-cms
```

#### **2. Setup Backend**

```powershell
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
# On Windows CMD:
venv\Scripts\activate.bat
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
Copy-Item .env.example .env
# Edit .env and add your configurations

# Run migrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser

# Start backend server
python manage.py runserver
```

**Backend will run at:** `http://localhost:8000`

#### **3. Setup Frontend**

Open a **new terminal window**:

```powershell
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Create .env file
Copy-Item .env.example .env
# Edit if needed (default should work)

# Start frontend development server
npm start
```

**Frontend will run at:** `http://localhost:3000`

---

### **Environment Variables**

#### **Backend (.env)**

Create `backend/.env`:

```env
# Django Settings
SECRET_KEY=your-super-secret-key-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (Development - SQLite)
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

# Database (Production - PostgreSQL)
# DB_ENGINE=django.db.backends.postgresql
# DB_NAME=blog_cms_db
# DB_USER=postgres
# DB_PASSWORD=your_password
# DB_HOST=localhost
# DB_PORT=5432

# JWT Settings
JWT_ACCESS_TOKEN_LIFETIME=30  # minutes
JWT_REFRESH_TOKEN_LIFETIME=1440  # minutes (24 hours)

# OpenAI API (Get from https://platform.openai.com/api-keys)
OPENAI_API_KEY=sk-your-openai-api-key-here

# CORS Settings
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# Email Settings (Optional - for password reset)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

#### **Frontend (.env)**

Create `frontend/.env`:

```env
REACT_APP_API_URL=http://localhost:8000/api
REACT_APP_BASE_URL=http://localhost:8000
```

---

### **Docker Setup (Production)**

For containerized deployment:

```powershell
# Build and run all services
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

**Access:**
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:8000/api`
- Admin Panel: `http://localhost:8000/admin`

---
## 📖 **Usage Guide**

### **For End Users**

#### **1. Register an Account**

1. Navigate to `http://localhost:3000`
2. Click **"Register"** button
3. Fill in:
   - Username
   - Email
   - Password (minimum 8 characters)
   - Confirm Password
4. Select role: **Author** (to create blogs) or **Reader** (to read only)
5. Click **"Sign Up"**

#### **2. Login**

1. Click **"Login"** button
2. Enter username and password
3. You'll receive JWT tokens (stored automatically)
4. Redirected to Dashboard

#### **3. Create Your First Blog**

1. From Dashboard, click **"Create New Blog"**
2. Fill in:
   - **Title**: Your blog title
   - **Content**: Write your blog content
   - **Category**: Select from dropdown (Technology, Programming, etc.)
   - **Tags**: Add relevant tags
3. Click **"🤖 Generate AI Summary"** button
4. Wait 3-5 seconds for AI to generate summary
5. Review and edit the summary if needed
6. Choose:
   - **Save Draft**: Keep private for later
   - **Publish Now**: Make public immediately

#### **4. View Your Blogs**

- Go to **"My Dashboard"**
- See all your blogs with statistics:
  - View count
  - Publication status
  - Edit/Delete options

---

### **For Developers**

#### **Testing the API**

**Using cURL:**

```powershell
# Register a user
curl -X POST http://localhost:8000/api/auth/register/ `
  -H "Content-Type: application/json" `
  -d '{\"username\":\"testuser\",\"email\":\"test@example.com\",\"password\":\"test123\",\"password2\":\"test123\"}'

# Login
$response = Invoke-RestMethod -Uri "http://localhost:8000/api/auth/login/" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"username":"testuser","password":"test123"}'

$token = $response.access

# Create a blog
Invoke-RestMethod -Uri "http://localhost:8000/api/blogs/" `
  -Method POST `
  -Headers @{"Authorization"="Bearer $token"} `
  -ContentType "application/json" `
  -Body '{"title":"My First Blog","content":"This is my content...","status":"published"}'

# Generate AI summary
Invoke-RestMethod -Uri "http://localhost:8000/api/ai/generate-summary/" `
  -Method POST `
  -Headers @{"Authorization"="Bearer $token"} `
  -ContentType "application/json" `
  -Body '{"blog_id":1}'
```

**Using Postman:**

1. Import the API collection from `postman_collection.json`
2. Set environment variable `base_url` = `http://localhost:8000/api`
3. Login to get JWT token
4. Token is auto-added to all requests via collection variables

---

## 📚 **Documentation**

| Document | Description |
|----------|-------------|
| [PROJECT_WORKFLOW.md](PROJECT_WORKFLOW.md) | Complete system workflow with visual diagrams |
| [UML_DIAGRAMS.md](UML_DIAGRAMS.md) | Architecture diagrams, sequence diagrams, class diagrams |
| [CODE_STRUCTURE.md](CODE_STRUCTURE.md) | Detailed explanation of codebase organization |
| [API_DOCUMENTATION.md](API_DOCUMENTATION.md) | Complete API reference with examples |
| [BLOG_CONTENT_GUIDE.md](BLOG_CONTENT_GUIDE.md) | Guide to writing effective blog content |
| [DEPLOYMENT.md](DEPLOYMENT.md) | Production deployment guide |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | Common issues and solutions |

---

## 🧪 **Testing**

### **Backend Tests**

```powershell
cd backend

# Run all tests
python manage.py test

# Run specific app tests
python manage.py test apps.users
python manage.py test apps.blogs
python manage.py test apps.ai_service

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Open htmlcov/index.html in browser
```

### **Frontend Tests**

```powershell
cd frontend

# Run all tests
npm test

# Run tests in watch mode
npm test -- --watch

# Generate coverage report
npm test -- --coverage
```

### **API Tests**

```powershell
# Using the test script
cd backend
python manage.py test apps.blogs.tests.test_api

# Manual API testing
# See TEST_API.ps1 for comprehensive test suite
```

---

## 🚀 **Deployment**

### **Production Deployment Checklist**

- [ ] Set `DEBUG=False` in backend/.env
- [ ] Change `SECRET_KEY` to a strong random value
- [ ] Configure PostgreSQL database
- [ ] Set up HTTPS with SSL certificate
- [ ] Configure CORS_ALLOWED_ORIGINS
- [ ] Set up email backend for notifications
- [ ] Configure static file serving (WhiteNoise or AWS S3)
- [ ] Set up monitoring (Sentry, New Relic)
- [ ] Configure backup strategy for database
- [ ] Set up CI/CD pipeline
- [ ] Configure domain and DNS

### **AWS EC2 Deployment**

**Quick Deploy:**

```bash
# On your EC2 instance
git clone <your-repo-url>
cd ai-blog-cms
chmod +x deploy.sh
./deploy.sh
```

**Manual Deploy:**

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

---

## ⚙️ **Configuration**

### **Backend Settings**

Key configurations in `backend/config/settings.py`:

```python
# Authentication
AUTH_USER_MODEL = 'users.User'
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # or postgresql
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# OpenAI
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# CORS
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]
```

### **Frontend Configuration**

Key configurations in `frontend/src/api.js`:

```javascript
const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || 'http://localhost:8000/api',
});

// Auto-add JWT token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});
```

---

## 🔒 **Security**

### **Security Features**

✅ **Authentication:**
- JWT-based stateless authentication
- Token expiration and automatic refresh
- Password hashing with bcrypt

✅ **Authorization:**
- Role-based access control (RBAC)
- Permission-based API endpoints
- Owner-only edit/delete operations

✅ **Data Protection:**
- SQL injection prevention (Django ORM)
- XSS protection
- CSRF protection
- Secure headers

✅ **API Security:**
- CORS configuration
- Rate limiting (optional with Django Rate Limit)
- Input validation with DRF serializers

### **Security Best Practices**

```python
# backend/config/settings.py

# Production settings
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
```

---

## 🐛 **Troubleshooting**

### **Common Issues**

<details>
<summary><b>Backend won't start</b></summary>

**Error:** `ModuleNotFoundError: No module named 'rest_framework'`

**Solution:**
```powershell
# Ensure virtual environment is activated
.\venv\Scripts\Activate.ps1
# Reinstall dependencies
pip install -r requirements.txt
```
</details>

<details>
<summary><b>Frontend won't connect to backend</b></summary>

**Error:** `Network Error` or `CORS policy`

**Solution:**
1. Ensure backend is running on port 8000
2. Check `frontend/.env` has correct API URL
3. Verify CORS settings in `backend/config/settings.py`:
```python
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]
```
</details>

<details>
<summary><b>JWT token not working</b></summary>

**Error:** `401 Unauthorized`

**Solution:**
1. Check token is stored in localStorage
2. Verify token hasn't expired
3. Ensure `AUTH_USER_MODEL` is set correctly
4. Try logging out and logging in again
</details>

<details>
<summary><b>AI summary generation fails</b></summary>

**Error:** `OpenAI API error`

**Solution:**
1. Verify `OPENAI_API_KEY` is set in backend/.env
2. Check API key is valid at https://platform.openai.com/api-keys
3. Ensure you have API credits
4. Check network connectivity
</details>

**Full Troubleshooting Guide:** See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

## 🌟 **Features Roadmap**

### **Current Version (v1.0)**
- ✅ User authentication & authorization
- ✅ Blog CRUD operations
- ✅ AI-powered summarization
- ✅ Comment system
- ✅ Category & tag management
- ✅ Responsive design

### **Planned Features (v2.0)**
- 🔜 Real-time collaborative editing
- 🔜 Advanced analytics dashboard
- 🔜 Multi-language support
- 🔜 Social media integration
- 🔜 SEO optimization tools
- 🔜 Email notifications
- 🔜 Blog scheduling
- 🔜 Advanced search with Elasticsearch

### **Future Enhancements**
- 📋 Mobile app (React Native)
- 📋 Voice-to-text for blog creation
- 📋 AI-powered image generation
- 📋 Plagiarism detection
- 📋 Revenue analytics for monetized blogs

---

## 🤝 **Contributing**

We welcome contributions! Here's how you can help:

### **Ways to Contribute**

1. **Report Bugs** - Open an issue with details
2. **Suggest Features** - Propose new features via issues
3. **Submit Pull Requests** - Fix bugs or add features
4. **Improve Documentation** - Help make docs clearer
5. **Write Tests** - Increase test coverage

### **Development Workflow**

1. **Fork** the repository
2. **Clone** your fork:
   ```bash
   git clone https://github.com/your-username/ai-blog-cms.git
   ```
3. **Create a branch**:
   ```bash
   git checkout -b feature/amazing-feature
   ```
4. **Make changes** and commit:
   ```bash
   git add .
   git commit -m "Add amazing feature"
   ```
5. **Push** to your fork:
   ```bash
   git push origin feature/amazing-feature
   ```
6. **Open a Pull Request** on GitHub

### **Code Style**

**Backend (Python):**
- Follow PEP 8
- Use Black formatter
- Add docstrings to functions
- Write unit tests

**Frontend (JavaScript):**
- Follow Airbnb style guide
- Use ESLint
- Add prop-types
- Write component tests

---

## 📄 **License**

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

[Full MIT License text...]
```

See [LICENSE](LICENSE) file for full details.

---

## 👨‍💻 **Author**

**Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com
- Portfolio: [yourportfolio.com](https://yourportfolio.com)

---

## 🙏 **Acknowledgments**

Special thanks to:

- **Django** & **Django REST Framework** - Powerful backend framework
- **React** - Modern UI library
- **OpenAI** - AI-powered content generation
- **Tailwind CSS** - Utility-first CSS framework
- **Zustand** - Simple state management
- **Axios** - HTTP client
- **VS Code** - Best code editor
- **GitHub** - Code hosting and collaboration

### **Inspirations**

- Medium.com - Blog platform design inspiration
- Dev.to - Developer-focused content platform
- Hashnode - Modern blogging for developers

---

## 📊 **Project Statistics**

<div align="center">

![Lines of Code](https://img.shields.io/badge/Lines_of_Code-15K+-blue)
![Commits](https://img.shields.io/badge/Commits-150+-green)
![Issues Closed](https://img.shields.io/badge/Issues_Closed-25+-red)
![Contributors](https://img.shields.io/badge/Contributors-1+-orange)

</div>

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

**Made with ❤️ using Django & React**

</div>
# AI-Powered-Blog-CMS
