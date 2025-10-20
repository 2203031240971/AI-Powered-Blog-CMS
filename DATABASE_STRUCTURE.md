# 📊 Database Structure

## 🗄️ Complete Database Schema

This document provides a detailed overview of the database structure for the AI-Powered Blog CMS.

---

## 📋 Table Overview

| Table | Purpose | Key Relationships |
|-------|---------|------------------|
| **users** | User accounts and authentication | One-to-many with blogs, comments |
| **blogs** | Blog posts and content | Many-to-one with users, categories |
| **categories** | Blog categorization | One-to-many with blogs |
| **tags** | Content tagging | Many-to-many with blogs |
| **comments** | User comments on blogs | Many-to-one with blogs, users |
| **blog_summary** | AI-generated summaries | One-to-one with blogs |
| **blog_tags** | Blog-Tag relationship | Junction table |

---

## 👥 Users Table

**Purpose:** Store user accounts and authentication data

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | Primary Key | Unique user ID |
| username | String(150) | Unique, Required | Username for login |
| email | String(254) | Unique, Required | User email address |
| password | String | Required | Hashed password (bcrypt) |
| first_name | String(150) | Optional | User's first name |
| last_name | String(150) | Optional | User's last name |
| role | String(20) | Default: 'viewer' | User role (admin/editor/author/viewer) |
| bio | Text | Optional | User biography |
| profile_image | ImageField | Optional | Profile picture |
| is_active | Boolean | Default: True | Account active status |
| is_staff | Boolean | Default: False | Staff status |
| is_superuser | Boolean | Default: False | Superuser status |
| is_active_user | Boolean | Default: True | Custom active flag |
| created_at | DateTime | Auto | Account creation time |
| updated_at | DateTime | Auto | Last update time |

**Indexes:**
- Primary key on `id`
- Unique index on `username`
- Unique index on `email`

**Relationships:**
- One-to-many with `blogs` (author)
- One-to-many with `comments` (author)

---

## 📝 Blogs Table

**Purpose:** Store blog posts and content

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | Primary Key | Unique blog ID |
| title | String(200) | Required | Blog post title |
| slug | String | Unique | URL-friendly identifier |
| description | String(300) | Optional | Short description |
| content | Text | Required | Full blog content (Markdown) |
| featured_image | ImageField | Optional | Blog thumbnail |
| author_id | Integer | Foreign Key | Reference to users table |
| category_id | Integer | Foreign Key, Nullable | Reference to categories table |
| status | String(20) | Default: 'draft' | Status (draft/published/archived) |
| views_count | Integer | Default: 0 | Number of views |
| is_featured | Boolean | Default: False | Featured blog flag |
| created_at | DateTime | Auto | Creation time |
| updated_at | DateTime | Auto | Last update time |
| published_at | DateTime | Nullable | Publication time |

**Indexes:**
- Primary key on `id`
- Unique index on `slug`
- Index on `author_id`
- Index on `category_id`
- Composite index on `(status, published_at)`
- Composite index on `(author, status)`

**Relationships:**
- Many-to-one with `users` (author)
- Many-to-one with `categories`
- Many-to-many with `tags` (through blog_tags)
- One-to-one with `blog_summary`
- One-to-many with `comments`

---

## 🏷️ Categories Table

**Purpose:** Organize blogs into categories

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | Primary Key | Unique category ID |
| name | String(100) | Unique, Required | Category name |
| slug | String | Unique | URL-friendly identifier |
| description | Text | Optional | Category description |
| created_at | DateTime | Auto | Creation time |

**Indexes:**
- Primary key on `id`
- Unique index on `name`
- Unique index on `slug`

**Relationships:**
- One-to-many with `blogs`

**Example Categories:**
- Technology
- Programming
- AI & Machine Learning
- Web Development
- DevOps
- Cybersecurity

---

## 🏷️ Tags Table

**Purpose:** Add tags to blogs for better organization

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | Primary Key | Unique tag ID |
| name | String(100) | Unique, Required | Tag name |
| slug | String | Unique | URL-friendly identifier |
| created_at | DateTime | Auto | Creation time |

**Indexes:**
- Primary key on `id`
- Unique index on `name`
- Unique index on `slug`

**Relationships:**
- Many-to-many with `blogs` (through blog_tags)

**Example Tags:**
- Python, Django, React, JavaScript
- AI, Machine Learning, GPT
- Tutorial, Guide, Tips
- Beginner, Advanced

---

## 💬 Comments Table

**Purpose:** Store user comments on blog posts

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | Primary Key | Unique comment ID |
| blog_id | Integer | Foreign Key | Reference to blogs table |
| author_id | Integer | Foreign Key | Reference to users table |
| content | Text | Required | Comment text |
| is_approved | Boolean | Default: False | Approval status |
| created_at | DateTime | Auto | Creation time |
| updated_at | DateTime | Auto | Last update time |

**Indexes:**
- Primary key on `id`
- Index on `blog_id`
- Index on `author_id`
- Composite index on `(blog_id, is_approved)`

**Relationships:**
- Many-to-one with `blogs`
- Many-to-one with `users` (author)

---

## 🤖 Blog Summary Table

**Purpose:** Store AI-generated summaries for blogs

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | Primary Key | Unique summary ID |
| blog_id | Integer | Foreign Key, Unique | Reference to blogs table |
| summary | Text | Required | AI-generated summary |
| key_points | JSONField | Default: [] | Array of key points |
| sentiment | String(20) | Optional | Sentiment (positive/negative/neutral) |
| generated_at | DateTime | Auto | Generation time |
| updated_at | DateTime | Auto | Last update time |

**Indexes:**
- Primary key on `id`
- Unique index on `blog_id`

**Relationships:**
- One-to-one with `blogs`

**Example Data:**
```json
{
  "summary": "This article explores how artificial intelligence is transforming healthcare...",
  "key_points": [
    "AI improves diagnostic accuracy",
    "Automation reduces administrative burden",
    "Predictive analytics enhance patient care"
  ],
  "sentiment": "positive"
}
```

---

## 🔗 Blog Tags Junction Table

**Purpose:** Many-to-many relationship between blogs and tags

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | Primary Key | Unique relationship ID |
| blog_id | Integer | Foreign Key | Reference to blogs table |
| tag_id | Integer | Foreign Key | Reference to tags table |

**Indexes:**
- Primary key on `id`
- Index on `blog_id`
- Index on `tag_id`
- Unique constraint on `(blog_id, tag_id)`

**Relationships:**
- Many-to-one with `blogs`
- Many-to-one with `tags`

---

## 📊 Entity Relationship Diagram (ERD)

```
┌─────────────┐
│    users    │
│─────────────│
│ id (PK)     │
│ username    │◄─────┐
│ email       │      │
│ password    │      │
│ role        │      │
│ ...         │      │
└─────────────┘      │
                     │
                     │ author_id (FK)
                     │
┌─────────────┐      │
│    blogs    │      │
│─────────────│      │
│ id (PK)     │      │
│ title       │      │
│ content     │      │
│ author_id   │──────┘
│ category_id │──────┐
│ status      │      │
│ ...         │      │
└─────────────┘      │
                     │
                     │ category_id (FK)
                     │
┌─────────────┐      │
│ categories  │      │
│─────────────│      │
│ id (PK)     │      │
│ name        │      │
│ slug        │      │
│ ...         │      │
└─────────────┘      │
                     │
                     │
┌─────────────┐      │
│    tags     │      │
│─────────────│      │
│ id (PK)     │      │
│ name        │      │
│ slug        │      │
└─────────────┘      │
                     │
                     │
┌─────────────┐      │
│ blog_tags   │──────┘
│─────────────│
│ id (PK)     │
│ blog_id (FK)│
│ tag_id (FK) │
└─────────────┘

┌─────────────┐
│  comments   │
│─────────────│
│ id (PK)     │
│ blog_id (FK)│──────┐
│ author_id   │──────┼──┐
│ content     │      │  │
│ is_approved │      │  │
└─────────────┘      │  │
                     │  │
┌─────────────┐      │  │
│blog_summary │      │  │
│─────────────│      │  │
│ id (PK)     │      │  │
│ blog_id (FK)│──────┘  │
│ summary     │         │
│ key_points  │         │
│ sentiment   │         │
└─────────────┘         │
                        │
                        │
                        │
                        └──► author_id (FK)
```

---

## 🔍 Common Queries

### **Get All Published Blogs**
```sql
SELECT * FROM blogs 
WHERE status = 'published' 
ORDER BY published_at DESC;
```

### **Get Blogs by Author**
```sql
SELECT b.*, u.username 
FROM blogs b 
JOIN users u ON b.author_id = u.id 
WHERE u.id = ?;
```

### **Get Blogs with Categories**
```sql
SELECT b.*, c.name as category_name 
FROM blogs b 
LEFT JOIN categories c ON b.category_id = c.id 
WHERE b.status = 'published';
```

### **Get Blogs with Tags**
```sql
SELECT b.*, t.name as tag_name 
FROM blogs b 
JOIN blog_tags bt ON b.id = bt.blog_id 
JOIN tags t ON bt.tag_id = t.id;
```

### **Get Blog with AI Summary**
```sql
SELECT b.*, bs.summary, bs.key_points 
FROM blogs b 
LEFT JOIN blog_summary bs ON b.id = bs.blog_id 
WHERE b.id = ?;
```

---

## 📈 Database Statistics

| Metric | Value |
|--------|-------|
| **Total Tables** | 7 |
| **Total Relationships** | 10+ |
| **Total Indexes** | 20+ |
| **Storage Engine** | PostgreSQL / SQLite |
| **Character Set** | UTF-8 |

---

## 🔧 Database Maintenance

### **Regular Tasks**
- ✅ Backup database daily
- ✅ Monitor query performance
- ✅ Optimize indexes
- ✅ Clean up old data
- ✅ Update statistics

### **Backup Commands**
```bash
# PostgreSQL
pg_dump -U postgres blog_cms_db > backup.sql

# SQLite
cp db.sqlite3 db_backup_$(date +%Y%m%d).sqlite3
```

---

## 🚀 Future Enhancements

- [ ] Add full-text search
- [ ] Implement caching layer
- [ ] Add database replication
- [ ] Implement soft deletes
- [ ] Add audit logging
- [ ] Implement versioning

---

*Generated: October 19, 2025*  
*Version: 1.0.0*

