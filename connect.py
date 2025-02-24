"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='redis-17398.c253.us-central1-1.gce.redns.redis-cloud.com',
    port=17398,
    decode_responses=True,
    username="default",
    password="OCsjQPD3mdo8eKn0iylmrziYkR7tb61r",
)

success = r.set('my_name', 'jessie')
print(success)
# True

result = r.get('my_name')
print(result)
# >>> bar

