# Django consent app
This app provides a configurable notice of consent banner for Django.
It uses Bootstrap CSS classes including container, alert, and alert-secondary.

## Installation
1. `pip install django-consent`
2. Add `consent` to `INSTALLED_APPS`
3. Add `consent.context_processors.context` to your `TEMPLATES['OPTIONS']`:
  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.contrib.auth.context_processors.auth',
                  'django.template.context_processors.debug',
                  'django.template.context_processors.i18n',
                  'django.template.context_processors.media',
                  'django.template.context_processors.static',
                  'django.template.context_processors.tz',
                  'django.contrib.messages.context_processors.messages',
                  'consent.context_processors.consent'
              ],
          },
      },
  ]
  ```
4. Set `CONSENT_TEXT` in your settings:
  ```python
  CONSENT_TEXT = "This computer system is provided only for authorized use..."
  ```
5. Include the banner template in your login page:
  ```
  {% include "consent/banner.html" %}
  ```
