# Test Cases

## Module: Login

---

### TC-LOGIN-001
**Title:** Valid login with correct credentials  
**Type:** Functional / Positive  
**Priority:** High  
**Preconditions:** User is on the login page and valid credentials are available.

**Test Steps:**
1. Open the login page
2. Enter valid username
3. Enter valid password
4. Click the Login button

**Test Data:**
- Username: `tomsmith`
- Password: `SuperSecretPassword!`

**Expected Result:**
- User is successfully logged in
- Success message is displayed

**Automation Status:** Automated

---

### TC-LOGIN-002
**Title:** Invalid login with incorrect credentials  
**Type:** Functional / Negative  
**Priority:** High  
**Preconditions:** User is on the login page.

**Test Steps:**
1. Open the login page
2. Enter invalid username
3. Enter invalid password
4. Click the Login button

**Test Data:**
- Username: `wronguser`
- Password: `wrongpass`

**Expected Result:**
- User is not logged in
- Error message is displayed

**Automation Status:** Automated

---

### TC-LOGIN-003
**Title:** Login with valid username and trailing space  
**Type:** Edge Case / Negative  
**Priority:** Medium  
**Preconditions:** User is on the login page.

**Test Steps:**
1. Open the login page
2. Enter valid username with trailing space
3. Enter valid password
4. Click the Login button

**Test Data:**
- Username: `tomsmith `
- Password: `SuperSecretPassword!`

**Expected Result:**
- User is not logged in
- Validation or error message is displayed

**Automation Status:** Not Automated Yet

---

## Module: Posts API

---

### TC-API-001
**Title:** Retrieve posts successfully  
**Type:** API / Positive  
**Priority:** High  
**Preconditions:** API endpoint is available.

**Test Steps:**
1. Send GET request to `/posts`

**Expected Result:**
- Response status code is `200`
- Response body is a non-empty list

**Automation Status:** Automated

---

### TC-API-002
**Title:** Create new post successfully  
**Type:** API / Positive  
**Priority:** High  
**Preconditions:** API endpoint is available.

**Test Steps:**
1. Send POST request to `/posts` with valid payload

**Test Data:**
```json
{
  "title": "QA Test Post",
  "body": "This is a test payload",
  "userId": 1
}