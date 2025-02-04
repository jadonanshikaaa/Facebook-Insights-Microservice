import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

def get_from_cache(key):
    data = redis_client.get(key)
    return data.decode("utf-8") if data else None

def set_to_cache(key, value, ttl=300):
    redis_client.setex(key, ttl, str(value))
