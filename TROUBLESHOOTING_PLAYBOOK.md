# 🚀 TROUBLESHOOTING & AUTO-FIX PLAYBOOK

**When something breaks in your project, use this guide to get fast fixes!**

---

## Section 1: How to Report Issues for Auto-Fix

### The Perfect Bug Report

**Template:**
```
Issue: [Brief title]
Description: [What's happening]
Steps to reproduce: [1. 2. 3.]
Expected: [What should happen]
Actual: [What's happening instead]
Error message: [Copy from console/page]
Console output: [F12 → Console tab]
```

**Example:**
```
Issue: Login form not submitting
Description: When I enter username and password and click login, nothing happens
Steps: 1. Go to login page 2. Enter credentials 3. Click Sign In
Expected: Should log in and redirect to home
Actual: Button shows "Signing in..." then nothing
Error: Console shows: "Cannot read property isAuthenticated of undefined"
```

---

### Speed Up Fixing

**FASTEST (Best for me):**
```
"Got error: [exact error message]
When: [what action]
Where: [which page]"
```

**SLOW (Takes longer):**
```
"something not working"
```

**Pro Tip:** More details = Faster fix!

---

## Section 2: Common Issues & Instant Fixes

### 🔴 LOGIN ISSUES

**Problem:** Can't log in

**Check Console (F12):**
- Look for red error messages
- Copy exact text

**Tell Me:**
```
"Can't login. Console shows: [error]"
```

**I'll Fix:**
- Login.js validation
- store.js token handling
- API authentication

**Time: 1-2 minutes**

---

**Problem:** Login works but logs out on refresh

**Diagnosis:**
- localStorage not saving
- Authentication not persisting

**Tell Me:**
```
"Get logged out when I refresh the page"
```

**I'll Fix:**
- App.js checkAuth() hook
- store.js localStorage code
- Session persistence

**Time: 1-2 minutes**

---

### 🔴 BLOG CREATION ISSUES

**Problem:** Blog won't save

**Symptoms:**
- Form submit fails
- "Failed to create blog" error
- Form stuck on loading

**Diagnosis Steps:**
1. Open console (F12)
2. Look for error message
3. Note any red errors

**Tell Me:**
```
"Blog creation fails. Console shows: [error message]"
```

**I'll Fix:**
- Form validation in BlogEditor.js
- API request formatting
- Backend serializer parsing
- Tag/Category handling

**Time: 2-3 minutes**

---

**Problem:** Blog created but not showing in profile

**Symptoms:**
- Form submits successfully
- Blog doesn't appear in list
- No errors shown

**Tell Me:**
```
"Blog created but not showing in profile"
OR
"Profile still shows 0 blogs"
```

**I'll Fix:**
- Blog fetching in UserProfile.js
- API filtering by author
- Data refresh timing

**Time: 2-3 minutes**

---

### 🔴 IMAGE UPLOAD ISSUES

**Problem:** Can't upload image

**Symptoms:**
- "Please select an image file" error
- File selector won't open
- Upload button disabled

**Tell Me:**
```
"Image upload failing with error: [message]"
OR
"Can't select image file"
```

**I'll Fix:**
- File input validation in BlogEditor.js
- File type checking
- Size limits
- Backend media configuration

**Time: 1-2 minutes**

---

**Problem:** Image too large

**Tell Me:**
```
"Getting error: file size too large"
OR
"Can't upload photos, file too big"
```

**I'll Fix:**
- Size limit in BlogEditor.js
- Backend file upload config
- Will increase limit if needed

**Time: 1 minute**

---

### 🔴 PROFILE ISSUES

**Problem:** Profile shows no data

**Symptoms:**
- "Welcome back" message but empty dashboard
- No blog list
- Stats show 0

**Tell Me:**
```
"Profile page is empty"
OR
"No blogs showing in dashboard"
OR
"Blog count showing 0"
```

**I'll Fix:**
- Blog fetching in UserProfile.js
- Author filtering in backend
- Data loading logic
- Diagnostic logging already in place

**Time: 2-3 minutes**

---

**Problem:** Profile page won't load

**Tell Me:**
```
"Profile page crashes"
OR
"Console error on profile page: [error]"
```

**I'll Fix:**
- Component rendering
- Data fetching
- Error handling
- API calls

**Time: 2-3 minutes**

---

### 🔴 DELETE ISSUES

**Problem:** Can't delete blog

**Symptoms:**
- Delete button does nothing
- "Permission denied" error
- Delete fails silently

**Tell Me:**
```
"Can't delete my blog. Error: [message]"
OR
"Delete button gives: [error]"
```

**I'll Fix:**
- Permission checks
- User/author verification
- API endpoint
- Response handling

**Time: 1-2 minutes**

---

### 🔴 CONSOLE ERRORS

**Problem:** Red error in browser console

**Steps to Report:**
1. Open DevTools (F12)
2. Go to Console tab
3. Find the RED error
4. Copy it exactly
5. Tell me

**Tell Me:**
```
"Console error: [exact error message]"
OR
"Getting: [error] - cannot find source"
```

**I'll Fix:**
- Find file causing error
- Fix the bug
- Error will disappear

**Time: 1-3 minutes**

---

### 🔴 API/BACKEND ISSUES

**Problem:** CORS error

**Symptoms:**
- Console shows "Access to XMLHttpRequest blocked by CORS policy"
- API calls failing
- Backend not responding

**Tell Me:**
```
"Getting CORS error in console"
```

**I'll Fix:**
- CORS configuration in settings.py
- Allowed origins
- Headers

**Time: 1 minute**

---

**Problem:** Backend not responding

**Symptoms:**
- Console shows "Failed to fetch"
- Network tab shows failed requests
- Backend seems down

**Check:**
1. Is backend running? (Should see output in terminal)
2. Check http://localhost:8000 in browser

**Tell Me:**
```
"Backend not responding"
OR
"Get 'Failed to fetch' errors"
```

**I'll Check:**
- Is server running?
- Port 8000 open?
- Database connected?
- Migrations applied?

**Time: 2-5 minutes**

---

## Section 3: Diagnostic Commands

### Check Backend Status

**Run this:**
```powershell
curl http://localhost:8000/api/blogs/blogs/
```

**Good response:** Shows JSON list of blogs  
**Bad response:** Connection refused or error

---

### Check Frontend Connection

Open browser console (F12) and run:
```javascript
fetch('http://localhost:8000/api/blogs/blogs/').then(r => r.json()).then(d => console.log(d))
```

**Good:** Shows blogs list  
**Bad:** Shows error  

---

### Check localStorage

Open console (F12) and run:
```javascript
console.log(localStorage)
```

**Should see:**
- access_token
- refresh_token
- user (JSON data)

---

## Section 4: Emergency Recovery

### If Everything Breaks

**Tell Me:**
```
"Everything broken!
Last thing I did: [action]
Error: [any messages]
What's not working: [features]"
```

**I Can:**
1. Revert problematic changes
2. Fix multiple issues
3. Restore database if needed
4. Get you back online

**Time: 5-15 minutes**

---

## Section 5: Issue Checklist

Before telling me about an issue, check:

### Frontend Issues:
- [ ] Refresh browser (Ctrl+R)
- [ ] Clear cache (Ctrl+Shift+Delete)
- [ ] Open console (F12)
- [ ] Check for red errors
- [ ] Copy exact error message
- [ ] Try in different browser?

### Backend Issues:
- [ ] Backend running? (Check terminal)
- [ ] Port 8000 open? (Check task manager)
- [ ] Database connected? (Try migration)
- [ ] Check backend terminal for errors
- [ ] Try restarting backend

### API Issues:
- [ ] Try curl to test endpoint
- [ ] Check network tab in console
- [ ] See what status code returned
- [ ] What's the error message?

---

## Section 6: Report Templates

### For Login Issues:
```
Issue: Login [working/not working]
Browser console shows: [copy here]
When I click login: [what happens]
Expected: [should log in]
Actual: [what happened instead]
```

### For Blog Issues:
```
Issue: [create/edit/delete/view] blog
Action: [what I did]
Expected: [should work]
Actual: [what happened]
Error: [console shows]
```

### For Profile Issues:
```
Issue: Profile [empty/broken/slow]
When I go to profile: [what I see]
Should show: [blogs/stats/etc]
Actually shows: [nothing/error/etc]
Console: [any errors?]
```

### For General Issues:
```
Issue: [brief title]
Reproduction: [steps 1-2-3]
Expected: [correct behavior]
Actual: [what's wrong]
Error: [any messages]
```

---

## Section 7: After I Fix It

### Test Steps:
1. Refresh browser (F12 or Ctrl+R)
2. Try the action that was failing
3. Check console for new errors
4. Try creating/editing/deleting content
5. Tell me if it works

### If Still Broken:
- Don't worry!
- Tell me what's still wrong
- I'll dig deeper and fix again
- Keep reporting until perfect

---

## Section 8: Quick Fix Guide

| Issue | Quick Tell | Fix Time |
|-------|-----------|----------|
| Login failing | "Can't login, error: [msg]" | 1-2 min |
| Blog won't save | "Create blog fails: [error]" | 2-3 min |
| Profile empty | "No blogs in profile" | 2-3 min |
| Image won't upload | "Upload fails: [error]" | 1-2 min |
| Delete not working | "Can't delete: [error]" | 1-2 min |
| Console error | "Red error: [message]" | 1-3 min |
| CORS error | "CORS blocked in console" | 1 min |
| Backend down | "Backend not responding" | 2-5 min |

---

## Section 9: Communication Template

**Save this and use when reporting:**

```
ISSUE: [What's broken]

WHEN: [What page/action]

ERROR: [Exact error message]

CONSOLE: [What F12 shows]

STEPS:
1. [First thing you do]
2. [Second thing]
3. [When error occurs]

EXPECTED: [What should happen]

ACTUAL: [What actually happened]
```

---

## Section 10: Support Flow

```
YOU submit report
   ↓ (me reading code)
   ↓ 30 seconds
ME identify problem
   ↓ (me fixing code)
   ↓ 1-2 minutes
ME show you fix
   ↓ (you testing)
   ↓ 1 minute
YOU confirm working
   ↓
✅ ISSUE SOLVED
```

---

## Emergency Support Phrases

Use these for fast help:

**"I'm getting [specific error]"** ← Fastest  
**"[Feature] is broken"** ← Fast  
**"Something's not working"** ← Slower  
**"Help"** ← Slowest  

**The more details, the faster the fix!**

---

## Key Points

✅ **Include exact error messages**  
✅ **Tell me what you were doing**  
✅ **Open console (F12) for errors**  
✅ **Copy-paste full error text**  
✅ **Describe expected vs actual**  
✅ **Be patient - I work fast!**  

---

## Final Notes

### I Can Fix:
✅ Code bugs  
✅ Configuration issues  
✅ API problems  
✅ Database issues  
✅ Logic errors  
✅ Styling problems  
✅ Performance issues  

### I Cannot Fix:
❌ Internet connectivity  
❌ Computer hardware  
❌ Third-party services down  
❌ Node/Python not installed  

---

## Ready to Report?

Just tell me what's wrong and I'll fix it!

**Format:**
```
"[Issue]. 
When I [action], 
[what happens].
Error: [message]"
```

**And I'll handle the rest automatically!** ✅

---

**Your project has automatic error detection & fixing enabled!** 🛡️

No problem is too big or small - I'll fix it!

