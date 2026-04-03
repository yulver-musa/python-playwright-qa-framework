# Test Strategy

## 1. Overview

This project implements an automated QA framework designed to validate both UI and API functionality of a web application.

The framework is built using Python, Playwright, and Pytest, with integration into a CI pipeline using GitHub Actions.

The goal of this strategy is to ensure:
- Reliable validation of critical user flows
- Fast feedback during development
- Scalable and maintainable test coverage

---

## 2. Scope

### In Scope
- UI testing of login functionality
- API testing of public endpoints (GET and POST)
- Validation of response data and UI messages
- Execution in local and CI environments

### Out of Scope
- Performance testing
- Security testing
- Database validation (future improvement)

---

## 3. Test Types

### UI Testing
- End-to-end validation using Playwright
- Covers user interactions and visual flows

### API Testing
- Backend validation using Python requests
- Verifies status codes and response payloads

---

## 4. Test Design Approach

### Positive Testing
- Valid login scenarios
- Successful API responses

### Negative Testing
- Invalid login credentials
- Incorrect inputs

### Edge Cases
- Input variations (e.g. incorrect formatting, unexpected values)

---

## 5. Test Architecture

The framework follows a modular structure:

- Page Object Model (POM) for UI interaction
- Separate test data layer for scalability
- Fixtures for setup and reuse
- Parameterized tests for multiple scenarios

---

## 6. Test Data Management

Test data is externalized in dedicated modules to:
- Improve maintainability
- Enable easy addition of new test scenarios
- Separate logic from data

---

## 7. Test Execution

### Local Execution
Tests can be executed using:
