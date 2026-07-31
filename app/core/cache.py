from time import time


cache: dict = {}


def get_cache(
    key: str
):
    item = cache.get(key)

    if item is None:
        return None

    if item["expires_at"] < time():
        del cache[key]
        return None

    return item["value"]


def set_cache(
    key: str,
    value,
    ttl: int = 60
):
    cache[key] = {
        "value": value,
        "expires_at": time() + ttl
    }


def delete_cache(
    key: str
):
    cache.pop(key, None)

def delete_user_task_cache(
    user_id: int
):
    prefix = f"tasks:{user_id}:"

    keys = list(cache.keys())

    for key in keys:
        if key.startswith(prefix):
            del cache[key]