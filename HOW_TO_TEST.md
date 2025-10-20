# Terminal 1
cd backend
python manage.py runserver

# Terminal 2
cd frontend  
npm start# How to Check If Links Are Working - Complete Testing Guide

## 🧪 Method 1: Browser Testing (Easiest)

### Step 1: Start the Application
```bash
# Terminal 1: Backend
cd backend
python manage.py runserver

# Terminal 2: Frontend (wait 5 seconds for backend to start)
cd frontend
npm start
```

**Wait for:**
- Backend shows: `Starting development server at http://127.0.0.1:8000/`
- Frontend opens automatically in browser

### Step 2: Visual Testing in Browser

#### Test 1: Check Frontend Loads
1. Browser should open http://localhost:3000
2. You should see the home page with **navigation bar**
3. Look for:
   - [ ] Logo/App name visible
   - [ ] Navigation menu visible
   - [ ] No red errors in page

#### Test 2: Register Link Works
1. Click **"Register"** link in navbar
2. Page should change to registration form
3. Check:
   - [ ] Form appears without errors
   - [ ] Has username, email, password fields
   - [ ] "Submit" button visible

#### Test 3: Login Link Works
1. Click **"Login"** link
2. Page should show login form
3. Check:
   - [ ] Login form appears
   - [ ] Username and password fields visible
   - [ ] "Submit" button visible

#### Test 4: Complete Registration
1. Fill registration form:
   - Username: `testuser1`
   - Email: `test@example.com`
   - Password: `TestPass123!`
   - Confirm Password: `TestPass123!`
2. Click Submit
3. Check:
   - [ ] Form submits without error
   - [ ] Redirects to login page
   - [ ] Success message appears

#### Test 5: Complete Login
1. Fill login form:
   - Username: `testuser1`
   - Password: `TestPass123!`
2. Click Submit
3. Check:
   - [ ] Login succeeds
   - [ ] Redirects to home or dashboard
   - [ ] Navbar shows "Logout" instead of "Login"

#### Test 6: Blogs Link Works
1. Click **"Blogs"** or **"View Blogs"** link
2. Page should show list of blogs
3. Check:
   - [ ] Blog list appears
   - [ ] Blog titles visible
   - [ ] Blog cards look correct

#### Test 7: Blog Detail Link Works
1. Click on a blog title or card
2. Blog detail page should open
3. Check:
   - [ ] Blog content visible
   - [ ] Blog title shows
   - [ ] Author information visible
   - [ ] Comments section visible

#### Test 8: Create Blog Link Works
1. Click **"Create Blog"** or **"New Post"** (if authenticated)
2. Should show blog creation form
3. Check:
   - [ ] Form appears
   - [ ] Title, content fields visible
   - [ ] Submit button visible

---

## 🖥️ Method 2: Check Browser Console

### Open DevTools
1. Press **F12** or right-click → **Inspect**
2. Go to **Console** tab

### Check for Errors
- [ ] **No red errors** in console
- [ ] No "404 Not Found" messages
- [ ] No "CORS error" messages
- [ ] No "API connection failed" messages

### Check Console Output
Good signs:
```
✅ No errors
✅ Page loads without warnings
✅ API requests successful
```

Bad signs:
```
❌ Uncaught TypeError
❌ Failed to fetch from http://localhost:8000
❌ CORS policy blocked
```

---

## 🌐 Method 3: Network Testing (DevTools)

### Open Network Tab
1. Press **F12** → **Network** tab
2. Refresh page (Ctrl+R)

### Look for API Requests
You should see requests like:
- `http://localhost:8000/api/blogs/` ✅ (Status 200)
- `http://localhost:8000/api/users/profile/` ✅ (Status 200)
- `http://localhost:8000/api/auth/login/` ✅ (Status 200)

### Check Status Codes
| Status | Meaning | Action |
|--------|---------|--------|
| **200** | ✅ OK | All good! |
| **201** | ✅ Created | Resource created successfully |
| **400** | ❌ Bad Request | Check form data |
| **401** | ❌ Unauthorized | Login required |
| **404** | ❌ Not Found | Endpoint doesn't exist |
| **500** | ❌ Server Error | Backend crashed |

### Example: Login Request
1. Click Login form Submit
2. Network tab should show:
   - `POST /api/auth/login/` → Status **200**
   - Response should have `access` and `refresh` tokens

---

## 🧬 Method 4: API Testing with cURL

### Test 1: Check Backend is Running
```bash
curl http://localhost:8000/api/
```

**Expected Response:**
```json
{
  "users": "http://localhost:8000/api/users/",
  "blogs": "http://localhost:8000/api/blogs/",
  "ai": "http://localhost:8000/api/ai/"
}
```

✅ **Working if:** You get JSON response with API endpoints

❌ **Not Working if:** 
- "Connection refused"
- Timeout
- Error message

### Test 2: Register User via cURL
```bash
curl -X POST http://localhost:8000/api/users/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "curluser",
    "email": "curl@test.com",
    "password": "CurlPass123!",
    "password2": "CurlPass123!"
  }'
```

**Expected Response:**
```json
{
  "id": 2,
  "username": "curluser",
  "email": "curl@test.com",
  "message": "User registered successfully"
}
```

✅ **Working if:** Status 201 with user data

### Test 3: Login via cURL
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "curluser",
    "password": "CurlPass123!"
  }'
```

**Expected Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

✅ **Working if:** Status 200 with tokens

### Test 4: View Blogs (Public - No Auth Needed)
```bash
curl http://localhost:8000/api/blogs/blogs/
```

**Expected Response:**
```json
{
  "count": 0,
  "next": null,
  "previous": null,
  "results": []
}
```

✅ **Working if:** Status 200 with blog list (empty is OK if no blogs yet)

### Test 5: Authenticated Request
```bash
# Replace TOKEN with access token from login
curl -X GET http://localhost:8000/api/users/profile/ \
  -H "Authorization: Bearer TOKEN"
```

**Expected Response:**
```json
{
  "id": 2,
  "username": "curluser",
  "email": "curl@test.com",
  "first_name": "",
  "last_name": ""
}
```

✅ **Working if:** Status 200 with user data

❌ **Not Working if:** Status 401 Unauthorized

---

## ✅ Complete Verification Checklist

Print this checklist and mark as you test:

### Frontend Links
- [ ] Home page loads
- [ ] Register link works
- [ ] Login link works
- [ ] Blogs link works
- [ ] User menu appears when logged in
- [ ] Logout link works
- [ ] Navigation is responsive

### Authentication
- [ ] Registration form submits
- [ ] Can register new user
- [ ] Login form submits
- [ ] Can login successfully
- [ ] Token is stored in localStorage
- [ ] Token refresh works
- [ ] Logout clears token

### Blog Operations
- [ ] View blogs list (public)
- [ ] Click blog to view details
- [ ] See blog author
- [ ] See blog comments
- [ ] Create blog button visible (authenticated)
- [ ] Can create new blog
- [ ] Can edit own blog
- [ ] Can delete own blog

### API Endpoints
- [ ] `/api/` returns endpoint list
- [ ] `/api/users/register/` POST works (201)
- [ ] `/api/auth/login/` POST works (200)
- [ ] `/api/users/profile/` GET works (200 with auth)
- [ ] `/api/blogs/blogs/` GET works (200)
- [ ] `/api/blogs/blogs/` POST works (201 with auth)

### Error Handling
- [ ] Invalid login shows error message
- [ ] Form validation works
- [ ] Network errors handled gracefully
- [ ] 404 pages show properly
- [ ] 401 redirects to login

---

## 🔍 Method 5: Check Backend Console

### Look for Errors in Django Terminal

**Good output:**
```
[19/Oct/2025 14:30:00] "POST /api/auth/login/ HTTP/1.1" 200 156
[19/Oct/2025 14:30:05] "GET /api/blogs/blogs/ HTTP/1.1" 200 142
[19/Oct/2025 14:30:10] "GET /api/users/profile/ HTTP/1.1" 200 89
```

✅ Status 200-201 = Working

**Bad output:**
```
[19/Oct/2025 14:30:00] "POST /api/auth/login/ HTTP/1.1" 401 23
ERROR: CORS error
[19/Oct/2025 14:30:05] "GET /api/blogs/blogs/ HTTP/1.1" 500 0
Internal Server Error: /api/blogs/blogs/
```

❌ Status 4xx/5xx = Not working

---

## 📊 Method 6: Automated Test Script

### Create Test Script (test_links.sh)

```bash
#!/bin/bash

echo "🧪 Testing AI-Powered Blog CMS Links..."
echo ""

# Test 1: Backend API Root
echo "1️⃣ Testing Backend API Root..."
RESPONSE=$(curl -s http://localhost:8000/api/)
if echo "$RESPONSE" | grep -q "users"; then
    echo "   ✅ PASS: API is responding"
else
    echo "   ❌ FAIL: API not responding"
fi
echo ""

# Test 2: Register Endpoint
echo "2️⃣ Testing Register Endpoint..."
RESPONSE=$(curl -s -X POST http://localhost:8000/api/users/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"test'$RANDOM'","email":"test'$RANDOM'@test.com","password":"Test123!","password2":"Test123!"}')
if echo "$RESPONSE" | grep -q "message"; then
    echo "   ✅ PASS: Registration working"
else
    echo "   ❌ FAIL: Registration not working"
fi
echo ""

# Test 3: Blogs Endpoint
echo "3️⃣ Testing Blogs Endpoint..."
RESPONSE=$(curl -s http://localhost:8000/api/blogs/blogs/)
if echo "$RESPONSE" | grep -q "results"; then
    echo "   ✅ PASS: Blogs endpoint working"
else
    echo "   ❌ FAIL: Blogs endpoint not working"
fi
echo ""

# Test 4: Frontend
echo "4️⃣ Testing Frontend..."
RESPONSE=$(curl -s http://localhost:3000)
if echo "$RESPONSE" | grep -q "React"; then
    echo "   ✅ PASS: Frontend is running"
else
    echo "   ❌ FAIL: Frontend not responding"
fi
echo ""

echo "✨ Testing complete!"
```

### Run Test Script
```bash
# Save as test_links.sh
chmod +x test_links.sh
./test_links.sh
```

---

## 🐛 Troubleshooting During Testing

### If Backend Not Responding
```bash
# Check if port 8000 is in use
netstat -ano | findstr :8000  # Windows
lsof -i :8000  # Mac/Linux

# Try different port
python manage.py runserver 8001
```

### If Frontend Not Loading
```bash
# Check if port 3000 is in use
netstat -ano | findstr :3000  # Windows
lsof -i :3000  # Mac/Linux

# Try different port
npm start -- --port 3001
```

### If API Returns 401
1. Make sure you're logged in
2. Check token is in localStorage (F12 → Application → localStorage)
3. Check token format is `Bearer <token>` not `JWT <token>`

### If Database Error
```bash
# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

---

## 📋 Quick Summary - How to Know It's Working

### ✅ All Links Working Indicators
1. **Browser:** Smooth navigation between pages
2. **Console:** No red errors
3. **Network:** All requests return 200 status
4. **Forms:** Registration and login work
5. **Data:** Blogs display correctly
6. **Authentication:** Can login/logout
7. **Backend:** Django shows 200 status codes

### ❌ Links NOT Working Indicators
1. **Page blank:** Likely API not responding
2. **Red console errors:** JavaScript errors
3. **Network errors:** 404, 500, CORS errors
4. **Forms don't submit:** Validation or API error
5. **No data displays:** Database or API issue
6. **Logout doesn't work:** Token not cleared

---

## 🎯 Final Verification Steps

### 1. Quick Visual Check (2 min)
```
✅ Start backend
✅ Start frontend
✅ Open http://localhost:3000
✅ Click 2-3 navigation links
✅ Check no red errors in F12
```

### 2. Complete Test (10 min)
Follow all steps in **Method 1: Browser Testing** above

### 3. API Test (5 min)
Run the **cURL tests** from **Method 4**

### 4. Console Check (2 min)
Open F12 and verify **Method 2: Check Browser Console**

**Total Time:** ~15-20 minutes for complete verification

---

## 📞 What to Do If Something Fails

| Issue | Check This |
|-------|-----------|
| Browser shows blank | Backend running? Check terminal |
| Red console errors | Check DevTools Console tab (F12) |
| 404 errors | Database migrations applied? |
| 401 unauthorized | Are you logged in? Token valid? |
| CORS error | Backend CORS settings correct? |
| Port in use | Different process on that port? |
| Connection refused | Is backend server running? |

---

## ✨ Expected Success Signs

When everything is working:

```
Frontend (http://localhost:3000)
✅ Page loads smoothly
✅ Navigation between pages instant
✅ Forms respond to input
✅ No loading delays
✅ No error messages

Backend (http://localhost:8000)
✅ API responds to requests
✅ All status codes are 200/201
✅ Data returns correctly
✅ Tokens work properly

Browser Console
✅ No red errors
✅ No warnings
✅ Network requests successful

Database
✅ Users created successfully
✅ Blogs stored and retrieved
✅ Comments saved properly
```

---

**Once you complete the tests above, reply with your results and I can help if anything isn't working! 🎉**
