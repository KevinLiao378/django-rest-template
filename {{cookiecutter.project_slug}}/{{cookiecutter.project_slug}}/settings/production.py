# flake8: noqa
{%- if cookiecutter.use_sentry == "y" %}
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

{%- endif %}

import {{ cookiecutter.project_slug }}

from .base import *

# ==================================================
# SECURITY SETTINGS
# ==================================================
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SESSION_COOKIE_SECURE = True


# ==================================================
# THIRD-PARTY APPS SETTINGS
# ==================================================
{%- if cookiecutter.use_sentry == "y" %}
# Sentry
# --------------------------------------------------
SENTRY_DSN = config("SENTRY_DSN", default="")
SENTRY_ENVIRONMENT = config("SENTRY_ENVIRONMENT", default="production")
SENTRY_TRACES_SAMPLE_RATE = config("SENTRY_TRACES_SAMPLE_RATE", default=0.0, cast=float)
sentry_sdk.init(
    dsn=SENTRY_DSN,
    environment=SENTRY_ENVIRONMENT,
    release="{{ cookiecutter.project_slug }}@%s" % {{ cookiecutter.project_slug }}.__version__,
    integrations=[DjangoIntegration()],
    traces_sample_rate=SENTRY_TRACES_SAMPLE_RATE,
)
{%- endif %}
