# Add these to your existing settings

INSTALLED_APPS = [
    # ...
    'rest_framework',
    'ckeditor',
    'faq',
]

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

CACHE_TTL = 60 * 15  # 15 minutes

# CKEditor configuration
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 800,
    },
}

