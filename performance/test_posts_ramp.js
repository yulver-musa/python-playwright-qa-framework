import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '10s', target: 5 },   // ramp up to 5 users
    { duration: '15s', target: 10 },  // ramp up to 10 users
    { duration: '10s', target: 10 },  // stay at 10 users
    { duration: '5s', target: 0 },    // ramp down to 0
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.95'],
  },
};

export default function () {
  const res = http.get('https://jsonplaceholder.typicode.com/posts');

  check(res, {
    'status is 200': (r) => r.status === 200,
  });

  sleep(1);
}