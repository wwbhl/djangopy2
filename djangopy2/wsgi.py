import os,sys

sys.path.append("/Users/baohailong/PycharmProjects/djangopy2/venv/lib/python2.7/site-packages")
sys.path.append("/Users/baohailong/PycharmProjects/djangopy2/djangopy2")
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE","djangopy2.settings")
application = get_wsgi_application()
