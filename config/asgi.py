"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_asgi_application()

#앱서버 로직을 처리 어플리케이션 서버 파이썬이라는 어플리케이션 의 인터페이스가 필요
# 파이썬은 웹서버로 통신이 불가능해서 asgi  
# 자바는 웹서버 일체형
# 프레임워크로 세팅