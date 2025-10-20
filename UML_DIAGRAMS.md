# 📐 UML Diagrams & System Architecture

## 🏗️ **System Architecture Overview**

This document contains comprehensive UML diagrams and architecture visualizations for the AI-Powered Blog CMS.

---

## 1. **High-Level System Architecture**

```
┌───────────────────────────────────────────────────────────────────────┐
│                           PRESENTATION LAYER                           │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │                      React Frontend (Port 3000)                  │  │
│  │                                                                   │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐       │  │
│  │  │BlogList  │  │BlogEditor│  │Dashboard │  │  Auth    │       │  │
│  │  │Component │  │Component │  │Component │  │Components│       │  │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘       │  │
│  │                                                                   │  │
│  │  ┌───────────────────────────────────────────────────────────┐  │  │
│  │  │              Zustand State Management                      │  │  │
│  │  │  {user, blogs, isAuthenticated, actions}                  │  │  │
│  │  └───────────────────────────────────────────────────────────┘  │  │
│  │                                                                   │  │
│  │  ┌───────────────────────────────────────────────────────────┐  │  │
│  │  │              Axios HTTP Client + Interceptors             │  │  │
│  │  │  - Automatic JWT token attachment                         │  │  │
│  │  │  - Token refresh on 401                                   │  │  │
│  │  └───────────────────────────────────────────────────────────┘  │  │
│  └─────────────────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ HTTP/HTTPS (REST API)
                                    │ JSON Data Exchange
                                    ▼
┌───────────────────────────────────────────────────────────────────────┐
│                           APPLICATION LAYER                            │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │                  Django REST Framework (Port 8000)              │  │
│  │                                                                   │  │
│  │  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌──────────┐    │  │
│  │  │  Users    │  │   Blogs   │  │   Auth    │  │AI Service│    │  │
│  │  │   API     │  │   API     │  │   API     │  │   API    │    │  │
│  │  └───────────┘  └───────────┘  └───────────┘  └──────────┘    │  │
│  │        │              │              │              │            │  │
│  │  ┌─────────────────────────────────────────────────────────┐   │  │
│  │  │              DRF Serializers & Validators               │   │  │
│  │  └─────────────────────────────────────────────────────────┘   │  │
│  │        │              │              │              │            │  │
│  │  ┌─────────────────────────────────────────────────────────┐   │  │
│  │  │              Business Logic Layer                       │   │  │
│  │  │  - Permission checks                                    │   │  │
│  │  │  - Data validation                                      │   │  │
│  │  │  - Workflow orchestration                               │   │  │
│  │  └─────────────────────────────────────────────────────────┘   │  │
│  │                                                                   │  │
│  │  ┌─────────────────────────────────────────────────────────┐   │  │
│  │  │              Middleware Layer                            │   │  │
│  │  │  - CORS handling                                         │   │  │
│  │  │  - JWT authentication                                    │   │  │
│  │  │  - Request logging                                       │   │  │
│  │  └─────────────────────────────────────────────────────────┘   │  │
│  └─────────────────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
┌────────────────────────────────┐   ┌────────────────────────────────┐
│      DATABASE LAYER            │   │      EXTERNAL SERVICES         │
│                                 │   │                                 │
│  ┌──────────────────────────┐  │   │  ┌──────────────────────────┐  │
│  │   PostgreSQL/SQLite      │  │   │  │      OpenAI API          │  │
│  │                          │  │   │  │  - GPT-3.5/4 Models      │  │
│  │  ┌────────┐ ┌────────┐  │  │   │  │  - Text Generation       │  │
│  │  │ Users  │ │ Blogs  │  │  │   │  │  - Summarization         │  │
│  │  └────────┘ └────────┘  │  │   │  └──────────────────────────┘  │
│  │  ┌────────┐ ┌────────┐  │  │   │                                 │
│  │  │Comments│ │  Tags  │  │  │   │  ┌──────────────────────────┐  │
│  │  └────────┘ └────────┘  │  │   │  │   AWS S3 (Optional)      │  │
│  │  ┌────────────────────┐ │  │   │  │  - Image storage         │  │
│  │  │   BlogSummary      │ │  │   │  └──────────────────────────┘  │
│  │  └────────────────────┘ │  │   │                                 │
│  └──────────────────────────┘  │   └────────────────────────────────┘
└────────────────────────────────┘
```

---

## 2. **Class Diagram - Database Models**

```
┌─────────────────────────────────────────────────────────────────────┐
│                            User Model                                │
├─────────────────────────────────────────────────────────────────────┤
│ Fields:                                                              │
│ - id: Integer (PK, Auto)                                            │
│ - username: String (Unique, Max 150)                                │
│ - email: String (Unique, Email format)                              │
│ - password: String (Hashed, bcrypt)                                 │
│ - first_name: String (Optional, Max 150)                            │
│ - last_name: String (Optional, Max 150)                             │
│ - role: String (Choices: admin, author, reader)                     │
│ - is_active: Boolean (Default: True)                                │
│ - is_staff: Boolean (Default: False)                                │
│ - date_joined: DateTime (Auto)                                      │
│ - last_login: DateTime (Nullable)                                   │
├─────────────────────────────────────────────────────────────────────┤
│ Relationships:                                                       │
│ - blogs: One-to-Many → Blog                                         │
│ - comments: One-to-Many → Comment                                   │
├─────────────────────────────────────────────────────────────────────┤
│ Methods:                                                             │
│ + create_user(username, email, password): User                      │
│ + check_password(raw_password): Boolean                             │
│ + set_password(raw_password): void                                  │
│ + get_full_name(): String                                           │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              │ 1:N (author)
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                            Blog Model                                │
├─────────────────────────────────────────────────────────────────────┤
│ Fields:                                                              │
│ - id: Integer (PK, Auto)                                            │
│ - title: String (Max 200)                                           │
│ - slug: String (Unique, Auto-generated from title)                  │
│ - content: Text (Rich text/HTML)                                    │
│ - excerpt: String (Max 300, Optional)                               │
│ - author: ForeignKey → User (CASCADE)                               │
│ - category: ForeignKey → Category (SET_NULL)                        │
│ - tags: ManyToMany → Tag                                            │
│ - status: String (Choices: draft, published, archived)              │
│ - featured_image: ImageField/URL (Optional)                         │
│ - views_count: Integer (Default: 0)                                 │
│ - likes_count: Integer (Default: 0)                                 │
│ - created_at: DateTime (Auto)                                       │
│ - updated_at: DateTime (Auto-update)                                │
│ - published_at: DateTime (Nullable)                                 │
├─────────────────────────────────────────────────────────────────────┤
│ Relationships:                                                       │
│ - author: Many-to-One → User                                        │
│ - category: Many-to-One → Category                                  │
│ - tags: Many-to-Many → Tag                                          │
│ - comments: One-to-Many → Comment                                   │
│ - ai_summary: One-to-One → BlogSummary                              │
├─────────────────────────────────────────────────────────────────────┤
│ Methods:                                                             │
│ + save(): void (auto-generate slug)                                 │
│ + increment_views(): void                                           │
│ + publish(): void (set status & published_at)                       │
│ + get_absolute_url(): String                                        │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              │ 1:1
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         BlogSummary Model                            │
├─────────────────────────────────────────────────────────────────────┤
│ Fields:                                                              │
│ - id: Integer (PK, Auto)                                            │
│ - blog: OneToOne → Blog (CASCADE)                                   │
│ - summary: Text (AI-generated or manual)                            │
│ - word_count: Integer                                               │
│ - generated_by: String (Choices: ai, manual)                        │
│ - model_used: String (e.g., "gpt-3.5-turbo")                        │
│ - created_at: DateTime (Auto)                                       │
│ - updated_at: DateTime (Auto-update)                                │
├─────────────────────────────────────────────────────────────────────┤
│ Methods:                                                             │
│ + generate_from_ai(content): String                                 │
│ + calculate_word_count(): Integer                                   │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                          Category Model                              │
├─────────────────────────────────────────────────────────────────────┤
│ Fields:                                                              │
│ - id: Integer (PK, Auto)                                            │
│ - name: String (Unique, Max 100)                                    │
│ - slug: String (Unique, Auto-generated)                             │
│ - description: Text (Optional)                                      │
│ - icon: String (Optional, FontAwesome class)                        │
│ - created_at: DateTime (Auto)                                       │
├─────────────────────────────────────────────────────────────────────┤
│ Relationships:                                                       │
│ - blogs: One-to-Many → Blog                                         │
├─────────────────────────────────────────────────────────────────────┤
│ Methods:                                                             │
│ + __str__(): String                                                 │
│ + get_blog_count(): Integer                                         │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                             Tag Model                                │
├─────────────────────────────────────────────────────────────────────┤
│ Fields:                                                              │
│ - id: Integer (PK, Auto)                                            │
│ - name: String (Unique, Max 50)                                     │
│ - slug: String (Unique, Auto-generated)                             │
│ - created_at: DateTime (Auto)                                       │
├─────────────────────────────────────────────────────────────────────┤
│ Relationships:                                                       │
│ - blogs: Many-to-Many → Blog                                        │
├─────────────────────────────────────────────────────────────────────┤
│ Methods:                                                             │
│ + __str__(): String                                                 │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                          Comment Model                               │
├─────────────────────────────────────────────────────────────────────┤
│ Fields:                                                              │
│ - id: Integer (PK, Auto)                                            │
│ - blog: ForeignKey → Blog (CASCADE)                                 │
│ - author: ForeignKey → User (CASCADE)                               │
│ - content: Text (Max 1000)                                          │
│ - parent: ForeignKey → Comment (Nullable, for replies)              │
│ - is_approved: Boolean (Default: True)                              │
│ - created_at: DateTime (Auto)                                       │
│ - updated_at: DateTime (Auto-update)                                │
├─────────────────────────────────────────────────────────────────────┤
│ Relationships:                                                       │
│ - blog: Many-to-One → Blog                                          │
│ - author: Many-to-One → User                                        │
│ - parent: Self-referential (for nested comments)                    │
├─────────────────────────────────────────────────────────────────────┤
│ Methods:                                                             │
│ + __str__(): String                                                 │
│ + is_reply(): Boolean                                               │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. **Sequence Diagram - User Registration Flow**

```
┌──────┐         ┌─────────┐         ┌─────────┐         ┌──────────┐
│Client│         │Frontend │         │ Backend │         │ Database │
└──────┘         └─────────┘         └─────────┘         └──────────┘
   │                  │                   │                    │
   │ 1. Navigate to   │                   │                    │
   │    /register     │                   │                    │
   │ ────────────────>│                   │                    │
   │                  │                   │                    │
   │ 2. Display form  │                   │                    │
   │ <────────────────│                   │                    │
   │                  │                   │                    │
   │ 3. Fill & submit │                   │                    │
   │ ────────────────>│                   │                    │
   │                  │                   │                    │
   │                  │ 4. POST /api/auth/register/            │
   │                  │    {username, email, password,         │
   │                  │     password2}                         │
   │                  │ ─────────────────>│                    │
   │                  │                   │                    │
   │                  │                   │ 5. Validate data   │
   │                  │                   │    (required fields,│
   │                  │                   │     password match,│
   │                  │                   │     email format)  │
   │                  │                   │                    │
   │                  │                   │ 6. Check username  │
   │                  │                   │    uniqueness      │
   │                  │                   │ ──────────────────>│
   │                  │                   │                    │
   │                  │                   │ 7. Username exists?│
   │                  │                   │ <──────────────────│
   │                  │                   │                    │
   │                  │                   │ 8. Hash password   │
   │                  │                   │    (bcrypt)        │
   │                  │                   │                    │
   │                  │                   │ 9. Create user     │
   │                  │                   │    record          │
   │                  │                   │ ──────────────────>│
   │                  │                   │                    │
   │                  │                   │ 10. User saved     │
   │                  │                   │ <──────────────────│
   │                  │                   │                    │
   │                  │ 11. 201 Created   │                    │
   │                  │     {id, username,│                    │
   │                  │      email}       │                    │
   │                  │ <─────────────────│                    │
   │                  │                   │                    │
   │ 12. Success msg  │                   │                    │
   │     + redirect   │                   │                    │
   │ <────────────────│                   │                    │
   │                  │                   │                    │
   │ 13. Navigate to  │                   │                    │
   │     /login       │                   │                    │
   │ ────────────────>│                   │                    │
```

---

## 4. **Sequence Diagram - Login & JWT Authentication**

```
┌──────┐     ┌─────────┐     ┌─────────┐     ┌──────────┐     ┌──────┐
│Client│     │Frontend │     │ Backend │     │ Database │     │localStorage│
└──────┘     └─────────┘     └─────────┘     └──────────┘     └──────┘
   │              │               │                │               │
   │ 1. Submit    │               │                │               │
   │    login form│               │                │               │
   │ ────────────>│               │                │               │
   │              │               │                │               │
   │              │ 2. POST /api/auth/login/       │               │
   │              │    {username, password}        │               │
   │              │ ─────────────>│                │               │
   │              │               │                │               │
   │              │               │ 3. Query user  │               │
   │              │               │    by username │               │
   │              │               │ ──────────────>│               │
   │              │               │                │               │
   │              │               │ 4. User object │               │
   │              │               │ <──────────────│               │
   │              │               │                │               │
   │              │               │ 5. Verify      │               │
   │              │               │    password    │               │
   │              │               │    (bcrypt     │               │
   │              │               │     compare)   │               │
   │              │               │                │               │
   │              │               │ 6. Generate    │               │
   │              │               │    JWT tokens  │               │
   │              │               │    - Access    │               │
   │              │               │      (30 min)  │               │
   │              │               │    - Refresh   │               │
   │              │               │      (24 hrs)  │               │
   │              │               │                │               │
   │              │ 7. 200 OK     │                │               │
   │              │    {access,   │                │               │
   │              │     refresh,  │                │               │
   │              │     user}     │                │               │
   │              │ <─────────────│                │               │
   │              │               │                │               │
   │              │ 8. Store tokens                │               │
   │              │ ──────────────────────────────────────────────>│
   │              │               │                │               │
   │              │ 9. Update state                │               │
   │              │    (isAuthenticated=true)      │               │
   │              │               │                │               │
   │ 10. Redirect │               │                │               │
   │     to       │               │                │               │
   │     dashboard│               │                │               │
   │ <────────────│               │                │               │
   │              │               │                │               │
   │ 11. Request  │               │                │               │
   │     protected│               │                │               │
   │     resource │               │                │               │
   │ ────────────>│               │                │               │
   │              │               │                │               │
   │              │ 12. GET /api/blogs/            │               │
   │              │ 13. Get token │                │               │
   │              │ <─────────────────────────────────────────────>│
   │              │               │                │               │
   │              │ 14. Headers:  │                │               │
   │              │     Authorization:             │               │
   │              │     Bearer {token}             │               │
   │              │ ─────────────>│                │               │
   │              │               │                │               │
   │              │               │ 15. Verify JWT │               │
   │              │               │     signature  │               │
   │              │               │                │               │
   │              │               │ 16. Check      │               │
   │              │               │     expiration │               │
   │              │               │                │               │
   │              │               │ 17. Extract    │               │
   │              │               │     user_id    │               │
   │              │               │                │               │
   │              │               │ 18. Fetch data │               │
   │              │               │ ──────────────>│               │
   │              │               │                │               │
   │              │               │ 19. Return data│               │
   │              │               │ <──────────────│               │
   │              │               │                │               │
   │              │ 20. 200 OK    │                │               │
   │              │     {blogs}   │                │               │
   │              │ <─────────────│                │               │
   │              │               │                │               │
   │ 21. Display  │               │                │               │
   │     blogs    │               │                │               │
   │ <────────────│               │                │               │
```

---

## 5. **Sequence Diagram - AI Summary Generation**

```
┌──────┐    ┌─────────┐    ┌─────────┐    ┌──────────┐    ┌─────────┐
│Client│    │Frontend │    │ Backend │    │ Database │    │OpenAI   │
│      │    │         │    │         │    │          │    │API      │
└──────┘    └─────────┘    └─────────┘    └──────────┘    └─────────┘
   │             │              │               │               │
   │ 1. Click    │              │               │               │
   │   "Generate │              │               │               │
   │    Summary" │              │               │               │
   │ ───────────>│              │               │               │
   │             │              │               │               │
   │             │ 2. POST /api/ai/generate-summary/            │
   │             │    {blog_id: 15}                             │
   │             │ ────────────>│               │               │
   │             │              │               │               │
   │             │              │ 3. Fetch blog │               │
   │             │              │    content    │               │
   │             │              │ ─────────────>│               │
   │             │              │               │               │
   │             │              │ 4. Blog data  │               │
   │             │              │ <─────────────│               │
   │             │              │               │               │
   │             │              │ 5. Prepare prompt:            │
   │             │              │    "Summarize in 150 words:   │
   │             │              │     {content}"                │
   │             │              │               │               │
   │             │              │ 6. Call OpenAI API            │
   │             │              │    model: gpt-3.5-turbo       │
   │             │              │ ─────────────────────────────>│
   │             │              │               │               │
   │             │              │               │     7. Process│
   │             │              │               │        with   │
   │             │              │               │        GPT    │
   │             │              │               │               │
   │             │              │ 8. AI-generated summary       │
   │             │              │ <─────────────────────────────│
   │             │              │               │               │
   │             │              │ 9. Create     │               │
   │             │              │    BlogSummary│               │
   │             │              │    record     │               │
   │             │              │ ─────────────>│               │
   │             │              │               │               │
   │             │              │ 10. Saved     │               │
   │             │              │ <─────────────│               │
   │             │              │               │               │
   │             │ 11. 200 OK   │               │               │
   │             │     {summary}│               │               │
   │             │ <────────────│               │               │
   │             │              │               │               │
   │ 12. Display │              │               │               │
   │     summary │              │               │               │
   │     in      │              │               │               │
   │     editor  │              │               │               │
   │ <───────────│              │               │               │
```

---

## 6. **Component Diagram - React Frontend**

```
┌─────────────────────────────────────────────────────────────────────┐
│                         App Component                                │
│                         (App.js)                                     │
└─────────────────────────────────────────────────────────────────────┘
                                │
                ┌───────────────┴───────────────┐
                │                               │
                ▼                               ▼
┌────────────────────────────┐    ┌────────────────────────────┐
│      Navbar Component      │    │     Router Component       │
│      (Navbar.js)           │    │    (BrowserRouter)         │
│                            │    │                            │
│  - Logo                    │    └────────────────────────────┘
│  - Navigation links        │                 │
│  - User menu               │                 │
│  - Logout button           │    ┌────────────┴────────────┐
└────────────────────────────┘    │                         │
                                  ▼                         ▼
                    ┌──────────────────────┐   ┌──────────────────────┐
                    │   Public Routes      │   │  Protected Routes    │
                    │                      │   │  (RequireAuth HOC)   │
                    └──────────────────────┘   └──────────────────────┘
                              │                           │
        ┌─────────────────────┼─────────┐        ┌───────┴───────┐
        │                     │         │        │               │
        ▼                     ▼         ▼        ▼               ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Register.js  │  │  Login.js    │  │BlogList.js   │  │BlogEditor.js │
│              │  │              │  │              │  │              │
│ - Form       │  │ - Form       │  │ - Blog cards │  │ - Rich editor│
│ - Validation │  │ - Auth logic │  │ - Pagination │  │ - AI button  │
│              │  │              │  │ - Filters    │  │ - Preview    │
└──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘
        │                     │         │                      │
        │                     │         │                      │
        └─────────────────────┴─────────┴──────────────────────┘
                              │
                              ▼
                ┌──────────────────────────────┐
                │   Zustand Store (store.js)   │
                │                              │
                │  State:                      │
                │  - user                      │
                │  - blogs                     │
                │  - isAuthenticated           │
                │  - isLoading                 │
                │  - errors                    │
                │                              │
                │  Actions:                    │
                │  - login()                   │
                │  - logout()                  │
                │  - fetchBlogs()              │
                │  - createBlog()              │
                │  - updateBlog()              │
                │  - deleteBlog()              │
                │  - generateSummary()         │
                └──────────────────────────────┘
                              │
                              ▼
                ┌──────────────────────────────┐
                │   Axios Client (api.js)      │
                │                              │
                │  - Base URL config           │
                │  - Request interceptor:      │
                │    → Add JWT token           │
                │  - Response interceptor:     │
                │    → Handle 401 errors       │
                │    → Refresh token           │
                │    → Retry request           │
                └──────────────────────────────┘
```

---

## 7. **Deployment Architecture Diagram**

```
                         ┌─────────────────┐
                         │   GitHub Repo   │
                         │  (Source Code)  │
                         └────────┬────────┘
                                  │
                     git push     │
                                  ▼
                         ┌─────────────────┐
                         │ GitHub Actions  │
                         │   CI/CD Pipeline│
                         └────────┬────────┘
                                  │
                    ┌─────────────┼─────────────┐
                    │             │             │
                    ▼             ▼             ▼
            ┌──────────┐  ┌──────────┐  ┌──────────┐
            │Run Tests │  │  Build   │  │  Deploy  │
            │          │  │  Docker  │  │  to AWS  │
            └──────────┘  │  Images  │  └──────────┘
                          └──────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │   Docker Hub    │
                         │  Image Registry │
                         └────────┬────────┘
                                  │
                        docker pull
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                          AWS EC2 Instance                            │
│                      (Ubuntu 22.04 LTS)                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │               Docker Compose                                    │ │
│  │                                                                  │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │ │
│  │  │   Nginx      │  │   Backend    │  │  PostgreSQL  │         │ │
│  │  │  (Port 80)   │  │  Container   │  │  Container   │         │ │
│  │  │              │  │  (Port 8000) │  │  (Port 5432) │         │ │
│  │  │ - Reverse    │  │              │  │              │         │ │
│  │  │   proxy      │  │ - Django     │  │ - Database   │         │ │
│  │  │ - Static     │  │ - Gunicorn   │  │ - Volumes    │         │ │
│  │  │   files      │  │              │  │              │         │ │
│  │  └──────────────┘  └──────────────┘  └──────────────┘         │ │
│  │         │                  │                  │                 │ │
│  │         └──────────────────┴──────────────────┘                 │ │
│  │                            │                                     │ │
│  │                    Internal Network                             │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                                                       │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │                  React Build (Static Files)                     │ │
│  │              Served by Nginx at /var/www/html                  │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  │ HTTPS (SSL/TLS)
                                  │ via Let's Encrypt
                                  ▼
                         ┌─────────────────┐
                         │   End Users     │
                         │  (Browsers)     │
                         └─────────────────┘
```

---

## 8. **State Diagram - Blog Post Lifecycle**

```
                    ┌────────────┐
                    │   START    │
                    └─────┬──────┘
                          │
                  Author creates blog
                          │
                          ▼
                    ┌────────────┐
              ┌────>│   DRAFT    │<────┐
              │     └─────┬──────┘     │
              │           │            │
              │     Save changes       │
              │           │            │
        Unpublish         ▼            │
              │     ┌────────────┐     │
              │     │  EDITING   │─────┘
              │     └─────┬──────┘
              │           │
              │    Click "Publish"
              │           │
              │           ▼
              │     ┌────────────┐
              └─────│ PUBLISHED  │
                    └─────┬──────┘
                          │
                ┌─────────┼─────────┐
                │         │         │
          Admin action    │    Author edits
          (Archive)       │         │
                │         │         ▼
                │         │   ┌────────────┐
                │         │   │  UPDATING  │
                │         │   └─────┬──────┘
                │         │         │
                │         │    Save changes
                │         │         │
                │         │         ▼
                │         │   ┌────────────┐
                │         │   │ PUBLISHED  │
                │         │   └────────────┘
                │         │
                │    Delete action
                │         │
                ▼         ▼
          ┌────────────┐┌────────────┐
          │  ARCHIVED  ││  DELETED   │
          └────────────┘└────────────┘
                │             │
           Restore?           │
                │        Permanent
                ▼             │
          ┌────────────┐      ▼
          │   DRAFT    │  ┌────────────┐
          └────────────┘  │    END     │
                          └────────────┘
```

---

## 9. **Data Flow Diagram - Creating a Blog with AI Summary**

```
┌──────────────────────────────────────────────────────────────────────┐
│                        Level 0: Context Diagram                       │
└──────────────────────────────────────────────────────────────────────┘

     ┌────────┐                                      ┌────────────┐
     │ Author │                                      │  OpenAI    │
     │        │                                      │    API     │
     └───┬────┘                                      └─────┬──────┘
         │                                                 │
         │  Blog content,                                  │
         │  title, category                           AI summary
         │                                                 │
         ▼                                                 ▼
    ┌─────────────────────────────────────────────────────────┐
    │                                                          │
    │            AI-Powered Blog CMS System                   │
    │                                                          │
    │  Processes blog creation, stores data,                  │
    │  generates AI summaries, publishes content              │
    │                                                          │
    └────────────────────┬────────────────────────────────────┘
                         │
                         │  Published blog with summary
                         │
                         ▼
                    ┌────────┐
                    │Readers │
                    └────────┘

┌──────────────────────────────────────────────────────────────────────┐
│                        Level 1: Detailed Flow                         │
└──────────────────────────────────────────────────────────────────────┘

┌────────┐
│ Author │
└───┬────┘
    │
    │ 1. Blog data (title, content, category, tags)
    │
    ▼
┌─────────────────────┐
│   Process 1.0       │
│  Validate & Store   │
│   Blog Content      │
└──────┬──────────────┘
       │
       │ 2. Validated blog data
       │
       ▼
┌───────────────┐
│   Data Store  │◄──── Read blog content ────┐
│   D1: Blogs   │                             │
└───────────────┘                             │
       │                                      │
       │ 3. Blog ID                           │
       │                                      │
       ▼                                      │
┌─────────────────────┐                      │
│   Process 2.0       │                      │
│   Trigger AI        │                      │
│   Summary Request   │                      │
└──────┬──────────────┘                      │
       │                                      │
       │ 4. Blog content                     │
       │                                      │
       ▼                                      │
┌─────────────────────┐                      │
│   Process 3.0       │                      │
│  Prepare Prompt &   │──────────────────────┘
│  Call OpenAI API    │
└──────┬──────────────┘
       │
       │ 5. Prompt: "Summarize in 150 words: {content}"
       │
       ▼
┌────────────────┐
│  External      │
│  OpenAI API    │
└────┬───────────┘
     │
     │ 6. AI-generated summary
     │
     ▼
┌─────────────────────┐
│   Process 4.0       │
│   Store Summary &   │
│   Link to Blog      │
└──────┬──────────────┘
       │
       │ 7. Summary data
       │
       ▼
┌───────────────────┐
│   Data Store      │
│   D2: Summaries   │
└───────────────────┘
       │
       │ 8. Complete blog with summary
       │
       ▼
┌─────────────────────┐
│   Process 5.0       │
│   Publish Blog      │
│   (Set status)      │
└──────┬──────────────┘
       │
       │ 9. Published blog
       │
       ▼
┌────────┐
│Readers │
└────────┘
```

---

## 10. **API Architecture Diagram**

```
┌─────────────────────────────────────────────────────────────────────┐
│                         API ENDPOINTS                                │
└─────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│  AUTHENTICATION APIs                                              │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│  POST   /api/auth/register/                                      │
│         Request: {username, email, password, password2}          │
│         Response: {id, username, email}                          │
│         Auth: None                                               │
│                                                                   │
│  POST   /api/auth/login/                                         │
│         Request: {username, password}                            │
│         Response: {access, refresh, user}                        │
│         Auth: None                                               │
│                                                                   │
│  POST   /api/auth/token/refresh/                                 │
│         Request: {refresh}                                       │
│         Response: {access}                                       │
│         Auth: Refresh Token                                      │
│                                                                   │
│  POST   /api/auth/logout/                                        │
│         Request: {refresh}                                       │
│         Response: {message}                                      │
│         Auth: JWT Required                                       │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│  BLOG APIs                                                        │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│  GET    /api/blogs/                                              │
│         Query: ?page=1&category=tech&search=django               │
│         Response: {count, next, previous, results: [blogs]}      │
│         Auth: Optional (public blogs visible to all)             │
│                                                                   │
│  POST   /api/blogs/                                              │
│         Request: {title, content, category, tags, status}        │
│         Response: {id, title, slug, author, created_at, ...}     │
│         Auth: JWT Required (Author/Admin)                        │
│                                                                   │
│  GET    /api/blogs/{id}/                                         │
│         Response: {id, title, content, author, summary, ...}     │
│         Auth: Optional                                           │
│                                                                   │
│  PUT    /api/blogs/{id}/                                         │
│         Request: {title, content, ...}                           │
│         Response: {updated blog object}                          │
│         Auth: JWT Required (Owner/Admin)                         │
│                                                                   │
│  DELETE /api/blogs/{id}/                                         │
│         Response: {message: "Deleted successfully"}              │
│         Auth: JWT Required (Owner/Admin)                         │
│                                                                   │
│  GET    /api/blogs/my-blogs/                                     │
│         Response: [user's blogs]                                 │
│         Auth: JWT Required                                       │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│  AI SERVICE APIs                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│  POST   /api/ai/generate-summary/                                │
│         Request: {blog_id}                                       │
│         Response: {summary, word_count, model_used}              │
│         Auth: JWT Required (Author/Admin)                        │
│                                                                   │
│  POST   /api/ai/rephrase/                                        │
│         Request: {text, tone}                                    │
│         Response: {rephrased_text}                               │
│         Auth: JWT Required                                       │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│  CATEGORY & TAG APIs                                             │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│  GET    /api/categories/                                         │
│         Response: [{id, name, slug, blog_count}]                 │
│         Auth: None                                               │
│                                                                   │
│  GET    /api/tags/                                               │
│         Response: [{id, name, slug}]                             │
│         Auth: None                                               │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│  COMMENT APIs                                                     │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│  GET    /api/blogs/{id}/comments/                                │
│         Response: [comments with nested replies]                 │
│         Auth: Optional                                           │
│                                                                   │
│  POST   /api/blogs/{id}/comments/                                │
│         Request: {content, parent_id?}                           │
│         Response: {comment object}                               │
│         Auth: JWT Required                                       │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘
```

---

This comprehensive UML documentation provides a complete technical blueprint of the AI-Powered Blog CMS system! 🚀
