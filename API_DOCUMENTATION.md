# 🔌 API Documentation

## 🌐 Complete API Reference

This document provides comprehensive documentation for all API endpoints in the AI-Powered Blog CMS.

**Base URL:** `http://localhost:8000/api`

---

## 🔐 Authentication

All authenticated endpoints require a JWT token in the Authorization header:

```
Authorization: Bearer <your_access_token>
```

---

## 📋 Table of Contents

1. [Authentication Endpoints](#authentication-endpoints)
2. [User Endpoints](#user-endpoints)
3. [Blog Endpoints](#blog-endpoints)
4. [Category Endpoints](#category-endpoints)
5. [Tag Endpoints](#tag-endpoints)
6. [Comment Endpoints](#comment-endpoints)
7. [AI Service Endpoints](#ai-service-endpoints)

---

## 🔐 Authentication Endpoints

### **1. Login**

**Endpoint:** `POST /api/auth/login/`

**Description:** Authenticate user and receive JWT tokens

**Request Body:**
```json
{
  "username": "johndoe",
  "password": "password123"
}
```

**Response (200 OK):**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Error Response (401 Unauthorized):**
```json
{
  "detail": "No active account found with the given credentials"
}
```

---

### **2. Refresh Token**

**Endpoint:** `POST /api/auth/refresh/`

**Description:** Get new access token using refresh token

**Request Body:**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Response (200 OK):**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

---

### **3. Verify Token**

**Endpoint:** `POST /api/auth/verify/`

**Description:** Verify if token is valid

**Request Body:**
```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Response (200 OK):**
```json
{
  "valid": true
}
```

---

## 👥 User Endpoints

### **1. List Users**

**Endpoint:** `GET /api/users/`

**Description:** Get list of all users (Admin only)

**Authentication:** Required (Admin)

**Query Parameters:**
- `role`: Filter by role (admin/editor/author/viewer)
- `is_active_user`: Filter by active status (true/false)
- `search`: Search by username, email, first_name, last_name
- `ordering`: Order by field (created_at, username)

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "role": "author",
    "is_active_user": true,
    "created_at": "2025-10-19T10:00:00Z"
  }
]
```

---

### **2. Create User (Register)**

**Endpoint:** `POST /api/users/`

**Description:** Register a new user

**Authentication:** Not required

**Request Body:**
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "SecurePass123!",
  "password2": "SecurePass123!",
  "first_name": "John",
  "last_name": "Doe",
  "role": "author"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com",
  "message": "User registered successfully"
}
```

**Error Response (400 Bad Request):**
```json
{
  "password": ["Passwords don't match."]
}
```

---

### **3. Get User Detail**

**Endpoint:** `GET /api/users/{id}/`

**Description:** Get specific user details

**Authentication:** Required

**Response (200 OK):**
```json
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "role": "author",
  "bio": "Software developer",
  "is_active_user": true,
  "is_staff": false,
  "is_superuser": false,
  "created_at": "2025-10-19T10:00:00Z",
  "updated_at": "2025-10-19T10:00:00Z"
}
```

---

### **4. Update User**

**Endpoint:** `PUT /api/users/{id}/` or `PATCH /api/users/{id}/`

**Description:** Update user information (Admin only)

**Authentication:** Required (Admin)

**Request Body:**
```json
{
  "first_name": "John",
  "last_name": "Smith",
  "bio": "Updated bio"
}
```

**Response (200 OK):**
```json
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Smith",
  "role": "author",
  "bio": "Updated bio",
  "updated_at": "2025-10-19T11:00:00Z"
}
```

---

### **5. Delete User**

**Endpoint:** `DELETE /api/users/{id}/`

**Description:** Delete a user (Admin only)

**Authentication:** Required (Admin)

**Response (204 No Content):**

---

### **6. Get Current User Profile**

**Endpoint:** `GET /api/users/profile/`

**Description:** Get current authenticated user's profile

**Authentication:** Required

**Response (200 OK):**
```json
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "role": "author",
  "bio": "Software developer",
  "created_at": "2025-10-19T10:00:00Z"
}
```

---

### **7. Update Current User Profile**

**Endpoint:** `PUT /api/users/profile_update/`

**Description:** Update current user's own profile

**Authentication:** Required

**Request Body:**
```json
{
  "first_name": "John",
  "last_name": "Smith",
  "bio": "Updated bio"
}
```

**Response (200 OK):**
```json
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Smith",
  "bio": "Updated bio"
}
```

---

## 📝 Blog Endpoints

### **1. List Blogs**

**Endpoint:** `GET /api/blogs/blogs/`

**Description:** Get list of blogs

**Authentication:** Not required (for published blogs)

**Query Parameters:**
- `status`: Filter by status (draft/published/archived)
- `author`: Filter by author ID
- `category`: Filter by category ID
- `is_featured`: Filter featured blogs (true/false)
- `search`: Search in title and content
- `ordering`: Order by field (created_at, published_at, views_count)

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "title": "How AI is Transforming Healthcare",
    "slug": "how-ai-is-transforming-healthcare",
    "description": "Exploring the impact of AI in healthcare",
    "content": "Full blog content...",
    "author": {
      "id": 1,
      "username": "johndoe"
    },
    "category": {
      "id": 1,
      "name": "Technology"
    },
    "status": "published",
    "views_count": 150,
    "is_featured": true,
    "created_at": "2025-10-19T10:00:00Z",
    "published_at": "2025-10-19T10:00:00Z"
  }
]
```

---

### **2. Create Blog**

**Endpoint:** `POST /api/blogs/blogs/`

**Description:** Create a new blog post

**Authentication:** Required (Author/Editor/Admin)

**Request Body:**
```json
{
  "title": "My First Blog Post",
  "description": "This is my first blog post",
  "content": "# Welcome\n\nThis is the content...",
  "category": 1,
  "status": "published",
  "is_featured": false
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "title": "My First Blog Post",
  "slug": "my-first-blog-post",
  "description": "This is my first blog post",
  "content": "# Welcome\n\nThis is the content...",
  "author": {
    "id": 1,
    "username": "johndoe"
  },
  "status": "published",
  "created_at": "2025-10-19T10:00:00Z"
}
```

---

### **3. Get Blog Detail**

**Endpoint:** `GET /api/blogs/blogs/{id}/`

**Description:** Get specific blog details

**Authentication:** Not required (for published blogs)

**Response (200 OK):**
```json
{
  "id": 1,
  "title": "How AI is Transforming Healthcare",
  "slug": "how-ai-is-transforming-healthcare",
  "description": "Exploring the impact of AI in healthcare",
  "content": "Full blog content...",
  "featured_image": "/media/blog_images/ai-healthcare.jpg",
  "author": {
    "id": 1,
    "username": "johndoe",
    "first_name": "John",
    "last_name": "Doe"
  },
  "category": {
    "id": 1,
    "name": "Technology",
    "slug": "technology"
  },
  "tags": [
    {"id": 1, "name": "AI"},
    {"id": 2, "name": "Healthcare"}
  ],
  "status": "published",
  "views_count": 150,
  "is_featured": true,
  "created_at": "2025-10-19T10:00:00Z",
  "published_at": "2025-10-19T10:00:00Z",
  "ai_summary": {
    "summary": "This article explores how AI is transforming healthcare...",
    "key_points": ["Point 1", "Point 2"],
    "sentiment": "positive"
  }
}
```

---

### **4. Update Blog**

**Endpoint:** `PUT /api/blogs/blogs/{id}/` or `PATCH /api/blogs/blogs/{id}/`

**Description:** Update a blog post

**Authentication:** Required (Author can update own blogs, Editor/Admin can update any)

**Request Body:**
```json
{
  "title": "Updated Title",
  "description": "Updated description",
  "content": "Updated content..."
}
```

**Response (200 OK):**
```json
{
  "id": 1,
  "title": "Updated Title",
  "slug": "updated-title",
  "description": "Updated description",
  "content": "Updated content...",
  "updated_at": "2025-10-19T11:00:00Z"
}
```

---

### **5. Delete Blog**

**Endpoint:** `DELETE /api/blogs/blogs/{id}/`

**Description:** Delete a blog post

**Authentication:** Required (Author can delete own blogs, Editor/Admin can delete any)

**Response (204 No Content):**

---

### **6. Generate AI Summary**

**Endpoint:** `POST /api/blogs/blogs/{id}/generate_summary/`

**Description:** Generate AI summary for a blog post

**Authentication:** Required

**Response (200 OK):**
```json
{
  "summary": "This article explores how AI is transforming healthcare...",
  "key_points": [
    "AI improves diagnostic accuracy",
    "Automation reduces administrative burden",
    "Predictive analytics enhance patient care"
  ],
  "sentiment": "positive",
  "generated_at": "2025-10-19T11:00:00Z"
}
```

---

## 🏷️ Category Endpoints

### **1. List Categories**

**Endpoint:** `GET /api/blogs/categories/`

**Description:** Get list of all categories

**Authentication:** Not required

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "name": "Technology",
    "slug": "technology",
    "description": "Technology-related blogs",
    "created_at": "2025-10-19T10:00:00Z"
  }
]
```

---

### **2. Create Category**

**Endpoint:** `POST /api/blogs/categories/`

**Description:** Create a new category (Admin only)

**Authentication:** Required (Admin)

**Request Body:**
```json
{
  "name": "Programming",
  "description": "Programming tutorials and guides"
}
```

**Response (201 Created):**
```json
{
  "id": 2,
  "name": "Programming",
  "slug": "programming",
  "description": "Programming tutorials and guides",
  "created_at": "2025-10-19T11:00:00Z"
}
```

---

### **3. Get Category Detail**

**Endpoint:** `GET /api/blogs/categories/{id}/`

**Description:** Get specific category details

**Authentication:** Not required

**Response (200 OK):**
```json
{
  "id": 1,
  "name": "Technology",
  "slug": "technology",
  "description": "Technology-related blogs",
  "blogs_count": 15,
  "created_at": "2025-10-19T10:00:00Z"
}
```

---

## 🏷️ Tag Endpoints

### **1. List Tags**

**Endpoint:** `GET /api/blogs/tags/`

**Description:** Get list of all tags

**Authentication:** Not required

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "name": "Python",
    "slug": "python",
    "created_at": "2025-10-19T10:00:00Z"
  },
  {
    "id": 2,
    "name": "Django",
    "slug": "django",
    "created_at": "2025-10-19T10:00:00Z"
  }
]
```

---

### **2. Create Tag**

**Endpoint:** `POST /api/blogs/tags/`

**Description:** Create a new tag (Admin only)

**Authentication:** Required (Admin)

**Request Body:**
```json
{
  "name": "React"
}
```

**Response (201 Created):**
```json
{
  "id": 3,
  "name": "React",
  "slug": "react",
  "created_at": "2025-10-19T11:00:00Z"
}
```

---

## 💬 Comment Endpoints

### **1. List Comments**

**Endpoint:** `GET /api/blogs/comments/`

**Description:** Get list of comments

**Authentication:** Not required

**Query Parameters:**
- `blog`: Filter by blog ID
- `is_approved`: Filter by approval status
- `author`: Filter by author ID

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "blog": {
      "id": 1,
      "title": "How AI is Transforming Healthcare"
    },
    "author": {
      "id": 2,
      "username": "janedoe"
    },
    "content": "Great article! Very informative.",
    "is_approved": true,
    "created_at": "2025-10-19T12:00:00Z"
  }
]
```

---

### **2. Create Comment**

**Endpoint:** `POST /api/blogs/comments/`

**Description:** Create a new comment

**Authentication:** Required

**Request Body:**
```json
{
  "blog": 1,
  "content": "This is a great article!"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "blog": 1,
  "author": {
    "id": 2,
    "username": "janedoe"
  },
  "content": "This is a great article!",
  "is_approved": false,
  "created_at": "2025-10-19T12:00:00Z"
}
```

---

### **3. Approve Comment**

**Endpoint:** `POST /api/blogs/comments/{id}/approve/`

**Description:** Approve a comment (Admin/Editor only)

**Authentication:** Required (Admin/Editor)

**Response (200 OK):**
```json
{
  "id": 1,
  "is_approved": true,
  "message": "Comment approved"
}
```

---

## 🤖 AI Service Endpoints

### **1. List AI Tasks**

**Endpoint:** `GET /api/ai/tasks/`

**Description:** Get list of AI processing tasks

**Authentication:** Required

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "blog_id": 1,
    "task_type": "summarize",
    "status": "completed",
    "result": {
      "summary": "AI-generated summary...",
      "key_points": ["Point 1", "Point 2"]
    },
    "created_at": "2025-10-19T10:00:00Z",
    "completed_at": "2025-10-19T10:00:05Z"
  }
]
```

---

### **2. Get Pending Tasks**

**Endpoint:** `GET /api/ai/tasks/pending/`

**Description:** Get list of pending AI tasks

**Authentication:** Required

**Response (200 OK):**
```json
[
  {
    "id": 2,
    "blog_id": 5,
    "task_type": "summarize",
    "status": "pending",
    "created_at": "2025-10-19T11:00:00Z"
  }
]
```

---

### **3. Get Failed Tasks**

**Endpoint:** `GET /api/ai/tasks/failed/`

**Description:** Get list of failed AI tasks

**Authentication:** Required

**Response (200 OK):**
```json
[
  {
    "id": 3,
    "blog_id": 7,
    "task_type": "summarize",
    "status": "failed",
    "error": "OpenAI API rate limit exceeded",
    "created_at": "2025-10-19T10:00:00Z"
  }
]
```

---

## 📊 Response Codes

| Code | Description |
|------|-------------|
| 200 | OK - Request successful |
| 201 | Created - Resource created successfully |
| 204 | No Content - Request successful, no content to return |
| 400 | Bad Request - Invalid request data |
| 401 | Unauthorized - Authentication required |
| 403 | Forbidden - Insufficient permissions |
| 404 | Not Found - Resource not found |
| 500 | Internal Server Error - Server error |

---

## 🔒 Rate Limiting

**Default Limits:**
- Unauthenticated: 100 requests/hour
- Authenticated: 1000 requests/hour
- Admin: 5000 requests/hour

---

## 📝 Error Response Format

All errors follow this format:

```json
{
  "error": "Error message",
  "detail": "Detailed error description",
  "code": "ERROR_CODE"
}
```

**Example:**
```json
{
  "error": "Validation failed",
  "detail": "Password must be at least 8 characters",
  "code": "VALIDATION_ERROR"
}
```

---

## 🧪 Testing the API

### **Using cURL**

```bash
# Login
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"johndoe","password":"password123"}'

# Get blogs
curl -X GET http://localhost:8000/api/blogs/blogs/

# Create blog (with auth)
curl -X POST http://localhost:8000/api/blogs/blogs/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"My Blog","content":"Content here","status":"published"}'
```

### **Using Postman**

1. Import the API collection
2. Set base URL: `http://localhost:8000/api`
3. Add authentication token to headers
4. Test each endpoint

---

## 📚 Additional Resources

- **API Testing Guide**: See API_TESTING.md
- **Authentication Guide**: See README.md
- **Deployment Guide**: See DEPLOYMENT.md

---

*Generated: October 19, 2025*  
*Version: 1.0.0*  
*API Version: v1*

