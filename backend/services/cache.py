import os
import json
import logging
from typing import Optional
from datetime import timedelta

logger = logging.getLogger(__name__)

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")

_cache_store: dict = {}

try:
    import redis.asyncio as aioredis
    _redis_available = True
except ImportError:
    _redis_available = False

_redis_client = None


async def get_redis():
    global _redis_client
    if not _redis_available:
        return None
    if _redis_client is None:
        try:
            _redis_client = aioredis.from_url(REDIS_URL, decode_responses=True)
            await _redis_client.ping()
            logger.info("Connected to Redis successfully.")
        except Exception as e:
            logger.warning(f"Redis connection failed, using in-memory cache: {e}")
            _redis_client = None
    return _redis_client


async def cache_get(key: str) -> Optional[str]:
    client = await get_redis()
    if client:
        try:
            return await client.get(key)
        except Exception:
            pass
    return _cache_store.get(key)


async def cache_set(key: str, value: str, ttl: int = 300):
    client = await get_redis()
    if client:
        try:
            await client.setex(key, timedelta(seconds=ttl), value)
            return
        except Exception:
            pass
    _cache_store[key] = value


async def cache_json_get(key: str) -> Optional[dict]:
    data = await cache_get(key)
    if data:
        return json.loads(data)
    return None


async def cache_json_set(key: str, value: dict, ttl: int = 300):
    await cache_set(key, json.dumps(value), ttl)
