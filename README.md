# Python Playwright QA Automation Framework

## Overview
This project is a QA automation framework built using Python, Playwright, and Pytest.

It demonstrates:
- UI automation with Playwright
- Page Object Model (POM)
- Parameterized test cases
- Environment-based configuration
- Test categorization (smoke, regression)
- Automatic screenshot capture on failure

## Tech Stack
- Python
- Playwright
- Pytest
- Pytest-HTML

## Project Structure
tests/      → test cases
pages/      → page objects
data/       → test data
utils/      → configuration
reports/    → test reports (ignored in Git)

## Running Tests

Run all tests:
pytest

Run smoke tests:
pytest -m smoke

Run smoke tests:
pytest -m regression

Run regression tests:
$env:ENV="staging"; pytest

## Features

- Clean test structure using POM
- Scalable test data management
- Environment switching without code changes
- Automatic failure screenshots
- HTML test reports

## Future Improvements

- CI/CD integration (GitHub Actions)
- API test coverage
- Database validation

## Project Overview

This project demonstrates a complete QA automation framework built using Python, Playwright, and Pytest.

It includes:
- UI automation (Playwright)
- API testing (requests)
- Test architecture using Page Object Model (POM)
- Parametrized test cases and externalized test data
- CI/CD integration with GitHub Actions
- Automated reporting with screenshots on failure
- Structured QA documentation (test strategy, test cases, bug reports)

The framework is designed to simulate real-world QA practices and is fully reusable across different projects.

## Documentation

- Test Strategy: `docs/test-strategy.md`
- Test Cases: `docs/test-cases.md`
- Bug Reports: `docs/bug-report-examples.md`
- Sample Reports: `docs/reports/`