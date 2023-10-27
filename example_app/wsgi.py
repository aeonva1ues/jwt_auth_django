import os
import sys
import platform

from django.core.wsgi import get_wsgi_application


sys.path.insert(0, "/home/c/ct84784/apitest/public_html")
sys.path.insert(0, "/home/c/ct84784/apitest/public_html/example_app")
sys.path.insert(
    0, "/home/c/ct84784/venv/lib/python{0}/site-packages"
    .format(platform.python_version()[0:3])
)
os.environ["DJANGO_SETTINGS_MODULE"] = "example_app.settings"

application = get_wsgi_application()
