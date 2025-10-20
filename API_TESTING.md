# API Testing Guide - AI-Powered Blog CMS

## Testing with cURL or Postman

### Prerequisites
- Backend running: `python manage.py runserver`
- Database configured and migrations applied

---

## 1. Authentication Endpoints

### Register a New User

**Endpoint:** `POST /api/users/register/`

**Request:**
```bash
curl -X POST http://localhost:8000/api/users/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "TestPassword123!",
    "password2": "TestPassword123!",
    "first_name": "Test",
    "last_name": "User"
  }'
```

**Response:**
```json
{
  "id": 1,
  "username": "testuser",
  "email": "test@example.com",
  "message": "User registered successfully"
}
```

---

### Login (Get Tokens)

**Endpoint:** `POST /api/auth/login/`

**Request:**
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "TestPassword123!"
  }'
```

**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Save these tokens:**
```bash
export ACCESS_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
export REFRESH_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
```

---

### Refresh Token

**Endpoint:** `POST /api/auth/refresh/`

**Request:**
```bash
curl -X POST http://localhost:8000/api/auth/refresh/ \
  -H "Content-Type: application/json" \
  -d "{
    \"refresh\": \"$REFRESH_TOKEN\"
  }"
```

**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

---

### Verify Token

**Endpoint:** `POST /api/auth/verify/`

**Request:**
```bash
curl -X POST http://localhost:8000/api/auth/verify/ \
  -H "Content-Type: application/json" \
  -d "{
    \"token\": \"$ACCESS_TOKEN\"
  }"
```

**Response:**
```json
{}
```

---

## 2. User Endpoints

### Get Current User Profile

**Endpoint:** `GET /api/users/profile/`

**Request:**
```bash
curl -X GET http://localhost:8000/api/users/profile/ \
  -H "Authorization: Bearer $ACCESS_TOKEN"
```

**Response:**
```json
{
  "id": 1,
  "username": "testuser",
  "email": "test@example.com",
  "first_name": "Test",
  "last_name": "User",
  "role": "author",
  "is_active_user": true,
  "created_at": "2025-10-19T10:30:00Z"
}
```

---

### Update User Profile

**Endpoint:** `PUT /api/users/profile_update/`

**Request:**
```bash
curl -X PUT http://localhost:8000/api/users/profile_update/ \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "TestUpdated",
    "last_name": "UserUpdated"
  }'
```

**Response:**
```json
{
  "id": 1,
  "username": "testuser",
  "email": "test@example.com",
  "first_name": "TestUpdated",
  "last_name": "UserUpdated",
  "role": "author",
  "is_active_user": true,
  "created_at": "2025-10-19T10:30:00Z"
}
```

---

### List All Users (Admin Only)

**Endpoint:** `GET /api/users/`

**Request:**
```bash
curl -X GET http://localhost:8000/api/users/ \
  -H "Authorization: Bearer $ACCESS_TOKEN"
```

**Response:**
```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "username": "testuser",
      "email": "test@example.com",
      "role": "author",
      "is_active_user": true
    }
  ]
}
```

---

## 3. Blog Endpoints

### List All Published Blogs (Public)

**Endpoint:** `GET /api/blogs/blogs/`

**Request:**
```bash
curl -X GET http://localhost:8000/api/blogs/blogs/
```

**Response:**
```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "My First Blog",
      "slug": "my-first-blog",
      "author": "testuser",
      "category": "Technology",
      "excerpt": "This is my first blog post",
      "status": "published",
      "views_count": 42,
      "created_at": "2025-10-19T10:00:00Z",
      "published_at": "2025-10-19T10:30:00Z"
    }
  ]
}
```

---

### Get Single Blog Detail

**Endpoint:** `GET /api/blogs/blogs/{id}/`

**Request:**
```bash
curl -X GET http://localhost:8000/api/blogs/blogs/1/
```

**Response:**
```json
{
  "id": 1,
  "title": "My First Blog",
  "slug": "my-first-blog",
  "author": "testuser",
  "author_id": 1,
  "category": "Technology",
  "category_id": 1,
  "description": "A detailed description",
  "content": "Blog content...",
  "excerpt": "This is my first blog post",
  "tags": [
    {
      "id": 1,
      "name": "python",
      "slug": "python"
    }
  ],
  "status": "published",
  "is_featured": false,
  "views_count": 42,
  "created_at": "2025-10-19T10:00:00Z",
  "published_at": "2025-10-19T10:30:00Z",
  "summary": {
    "id": 1,
    "content": "AI generated summary...",
    "key_points": ["Point 1", "Point 2"],
    "sentiment": "positive"
  },
  "comments": [
    {
      "id": 1,
      "author": "commenter",
      "content": "Great post!",
      "created_at": "2025-10-19T11:00:00Z",
      "is_approved": true
    }
  ]
}
```

---

### Create a New Blog (Authenticated)

**Endpoint:** `POST /api/blogs/blogs/`

**Request:**
```bash
curl -X POST http://localhost:8000/api/blogs/blogs/ \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Second Blog",
    "description": "Description of my blog",
    "content": "This is the full content of my blog post...",
    "excerpt": "A short excerpt",
    "category": 1,
    "tags": [1, 2],
    "status": "draft"
  }'
```

**Response:**
```json
{
  "id": 2,
  "title": "My Second Blog",
  "slug": "my-second-blog",
  "description": "Description of my blog",
  "content": "This is the full content...",
  "excerpt": "A short excerpt",
  "category": 1,
  "category_name": "Technology",
  "tags": [1, 2],
  "status": "draft",
  "is_featured": false,
  "views_count": 0,
  "created_at": "2025-10-19T12:00:00Z"
}
```

---

### Update Blog (Author Only)

**Endpoint:** `PUT /api/blogs/blogs/{id}/`

**Request:**
```bash
curl -X PUT http://localhost:8000/api/blogs/blogs/2/ \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Updated Blog",
    "status": "published"
  }'
```

**Response:**
```json
{
  "id": 2,
  "title": "My Updated Blog",
  "status": "published",
  "published_at": "2025-10-19T12:30:00Z",
  ...
}
```

---

### Get Featured Blogs

**Endpoint:** `GET /api/blogs/blogs/featured/`

**Request:**
```bash
curl -X GET http://localhost:8000/api/blogs/blogs/featured/
```

**Response:**
```json
[
  {
    "id": 1,
    "title": "Featured Blog",
    "is_featured": true,
    ...
  }
]
```

---

### Get Latest Blogs

**Endpoint:** `GET /api/blogs/blogs/latest/`

**Request:**
```bash
curl -X GET http://localhost:8000/api/blogs/blogs/latest/
```

**Response:**
```json
[
  {
    "id": 2,
    "title": "Latest Blog",
    "published_at": "2025-10-19T12:30:00Z",
    ...
  }
]
```

---

### Increment Blog Views

**Endpoint:** `GET /api/blogs/blogs/{id}/increment_views/`

**Request:**
```bash
curl -X GET http://localhost:8000/api/blogs/blogs/1/increment_views/
```

**Response:**
```json
{
  "views_count": 43
}
```

---

### Generate AI Summary

**Endpoint:** `GET /api/blogs/blogs/{id}/generate_summary/`

**Request:**
```bash
curl -X GET http://localhost:8000/api/blogs/blogs/1/generate_summary/ \
  -H "Authorization: Bearer $ACCESS_TOKEN"
```

**Response:**
```json
{
  "status": "Summary generation started",
  "blog_id": 1
}
```

---

### Get Blog Comments

**Endpoint:** `GET /api/blogs/blogs/{id}/comments/`

**Request:**
```bash
curl -X GET http://localhost:8000/api/blogs/blogs/1/comments/
```

**Response:**
```json
[
  {
    "id": 1,
    "blog": 1,
    "author": "commenter",
    "author_id": 2,
    "content": "Great post!",
    "created_at": "2025-10-19T11:00:00Z",
    "is_approved": true
  }
]
```

---

### Add Comment to Blog

**Endpoint:** `POST /api/blogs/blogs/{id}/comment/`

**Request:**
```bash
curl -X POST http://localhost:8000/api/blogs/blogs/1/comment/ \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "This is a great blog post!"
  }'
```

**Response:**
```json
{
  "id": 2,
  "blog": 1,
  "author": "testuser",
  "author_id": 1,
  "content": "This is a great blog post!",
  "created_at": "2025-10-19T13:00:00Z",
  "is_approved": false
}
```

---

## 4. Category Endpoints

### List Categories

**Endpoint:** `GET /api/blogs/categories/`

**Request:**
```bash
curl -X GET http://localhost:8000/api/blogs/categories/
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "Technology",
    "slug": "technology",
    "description": "Technology-related posts"
  }
]
```

---

### Create Category (Authenticated)

**Endpoint:** `POST /api/blogs/categories/`

**Request:**
```bash
curl -X POST http://localhost:8000/api/blogs/categories/ \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "AI & ML",
    "description": "Artificial Intelligence and Machine Learning"
  }'
```

**Response:**
```json
{
  "id": 2,
  "name": "AI & ML",
  "slug": "ai-ml",
  "description": "Artificial Intelligence and Machine Learning"
}
```

---

## 5. Tag Endpoints

### List Tags

**Endpoint:** `GET /api/blogs/tags/`

**Request:**
```bash
curl -X GET http://localhost:8000/api/blogs/tags/
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "python",
    "slug": "python"
  }
]
```

---

### Get Blogs by Tag

**Endpoint:** `GET /api/blogs/tags/{slug}/blogs/`

**Request:**
```bash
curl -X GET http://localhost:8000/api/blogs/tags/python/blogs/
```

**Response:**
```json
[
  {
    "id": 1,
    "title": "Python Tutorial",
    "slug": "python-tutorial",
    ...
  }
]
```

---

## 6. AI Task Endpoints

### List AI Tasks

**Endpoint:** `GET /api/ai/tasks/`

**Request:**
```bash
curl -X GET http://localhost:8000/api/ai/tasks/ \
  -H "Authorization: Bearer $ACCESS_TOKEN"
```

**Response:**
```json
{
  "count": 2,
  "results": [
    {
      "id": 1,
      "blog": 1,
      "task_type": "summarization",
      "status": "completed",
      "result": "AI generated summary...",
      "created_at": "2025-10-19T10:30:00Z",
      "completed_at": "2025-10-19T10:35:00Z"
    }
  ]
}
```

---

### Get Pending Tasks

**Endpoint:** `GET /api/ai/tasks/pending/`

**Request:**
```bash
curl -X GET http://localhost:8000/api/ai/tasks/pending/ \
  -H "Authorization: Bearer $ACCESS_TOKEN"
```

**Response:**
```json
[
  {
    "id": 2,
    "blog": 2,
    "task_type": "sentiment_analysis",
    "status": "pending",
    "created_at": "2025-10-19T12:30:00Z"
  }
]
```

---

## Filtering Examples

### Filter Blogs by Status
```bash
curl -X GET "http://localhost:8000/api/blogs/blogs/?status=published"
```

### Filter Blogs by Category
```bash
curl -X GET "http://localhost:8000/api/blogs/blogs/?category=1"
```

### Search Blogs
```bash
curl -X GET "http://localhost:8000/api/blogs/blogs/?search=python"
```

### Filter by Author
```bash
curl -X GET "http://localhost:8000/api/blogs/blogs/?author=1"
```

### Order Blogs
```bash
curl -X GET "http://localhost:8000/api/blogs/blogs/?ordering=-published_at"
```

### Pagination
```bash
curl -X GET "http://localhost:8000/api/blogs/blogs/?page=1&page_size=5"
```

---

## Postman Collection

You can import this JSON into Postman:

```json
{
  "info": {
    "name": "AI Blog CMS API",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Auth",
      "item": [
        {
          "name": "Register",
          "request": {
            "method": "POST",
            "url": "{{base_url}}/api/users/register/",
            "body": {
              "mode": "raw",
              "raw": "{\"username\":\"test\",\"password\":\"pass123\",\"email\":\"test@test.com\"}"
            }
          }
        },
        {
          "name": "Login",
          "request": {
            "method": "POST",
            "url": "{{base_url}}/api/auth/login/",
            "body": {
              "mode": "raw",
              "raw": "{\"username\":\"test\",\"password\":\"pass123\"}"
            }
          }
        }
      ]
    },
    {
      "name": "Blogs",
      "item": [
        {
          "name": "List Blogs",
          "request": {
            "method": "GET",
            "url": "{{base_url}}/api/blogs/blogs/"
          }
        },
        {
          "name": "Create Blog",
          "request": {
            "method": "POST",
            "url": "{{base_url}}/api/blogs/blogs/",
            "header": [
              {
                "key": "Authorization",
                "value": "Bearer {{access_token}}"
              }
            ]
          }
        }
      ]
    }
  ],
  "variable": [
    {
      "key": "base_url",
      "value": "http://localhost:8000"
    },
    {
      "key": "access_token",
      "value": ""
    }
  ]
}
```

---

## Common Response Codes

| Code | Meaning | Solution |
|------|---------|----------|
| 200 | OK | Request successful |
| 201 | Created | Resource created successfully |
| 400 | Bad Request | Invalid request data - check JSON |
| 401 | Unauthorized | Missing or invalid token |
| 403 | Forbidden | Don't have permission for this action |
| 404 | Not Found | Resource doesn't exist |
| 500 | Server Error | Backend error - check console logs |

---

## Troubleshooting

### Invalid Token Error
- Ensure token format is `Bearer <token>` not `JWT <token>`
- Token might have expired - request new token with refresh

### CORS Error
- Check CORS_ALLOWED_ORIGINS in settings.py
- Frontend URL must be in the list

### Database Errors
- Ensure migrations are applied: `python manage.py migrate`
- Check database connection in .env

---

## Next Steps

1. Test all endpoints with cURL
2. Move to Postman for easier testing
3. Integrate into frontend React components
4. Set up proper error handling in React

