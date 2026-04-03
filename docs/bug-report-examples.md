# Bug Report Examples

## Example 1: UI Bug Report

**Bug ID:** BUG-LOGIN-001  
**Title:** Error message remains visible after successful login attempt  
**Module:** Login  
**Severity:** Medium  
**Priority:** Medium  
**Environment:** Staging / Chrome / Windows 11  
**Reporter:** Yulver Musa  

### Description
After entering invalid credentials and receiving an error message, performing a valid login does not fully clear the previous error state.

### Preconditions
- User is on the login page
- Application is accessible
- Valid credentials are available

### Steps to Reproduce
1. Open the login page
2. Enter invalid username and password
3. Click the Login button
4. Confirm the error message is displayed
5. Enter valid username and valid password
6. Click the Login button again

### Expected Result
- User is logged in successfully
- Previous error message is cleared
- Only success message is visible

### Actual Result
- User is logged in successfully
- Previous error state remains visible or overlaps with success feedback

### Evidence
- Screenshot attached
- HTML report reference available from automated run

### Notes
This issue may confuse users by displaying inconsistent feedback after successful authentication.

---

## Example 2: API Bug Report

**Bug ID:** BUG-API-001  
**Title:** POST /posts accepts empty title without validation  
**Module:** Posts API  
**Severity:** Medium  
**Priority:** High  
**Environment:** Test API / JSONPlaceholder simulation  
**Reporter:** Yulver Musa  

### Description
The API accepts creation of a post with an empty `title` field and still returns a successful `201 Created` response.

### Preconditions
- API endpoint `/posts` is available
- Valid request format is used

### Steps to Reproduce
1. Send POST request to `/posts`
2. Use payload with empty `title` value:
   ```json
   {
     "title": "",
     "body": "Test body",
     "userId": 1
   }