# Performance Testing with k6

## What I implemented
- Load testing using k6
- Simulated multiple users (VUs)
- Used ramping stages
- Tested GET and POST endpoints

## Metrics analyzed
- Response time (avg, p95)
- Number of requests
- Success rate

## Tools
- k6 (JavaScript-based performance testing tool)

## Example command
k6 run performance/test_posts_ramp.js