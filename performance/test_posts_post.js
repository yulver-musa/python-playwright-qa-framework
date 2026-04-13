import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '10s', target: 5 },
    { duration: '10s', target: 10 },
    { duration: '10s', target: 0 },
  ],
  thresholds: {
    http_req_duration: ['p(95)<800'],
    checks: ['rate>0.95'],
  },
};

export default function () {
  const payload = JSON.stringify({
    title: 'Performance Test Post',
    body: 'Testing POST under load',
    userId: 1,
  });

  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  const res = http.post(
    'https://jsonplaceholder.typicode.com/posts',
    payload,
    params
  );

  check(res, {
    'status is 201': (r) => r.status === 201,
  });

  sleep(1);
}