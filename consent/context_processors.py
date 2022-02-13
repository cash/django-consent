from django.conf import settings


def consent(request):
    return {
        "CONSENT_TEXT": settings.CONSENT_TEXT,
    }
