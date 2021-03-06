import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

try:
    dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
    load_dotenv(dotenv_path)
except:
    pass


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coloquio.settings")

application = get_wsgi_application()