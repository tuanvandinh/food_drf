import sys
import os
import django


# if __name__ == "__main__":
BASE_DIR = os.getcwd() + "/"
sys.path.append(BASE_DIR)
if os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ["DJANGO_SETTINGS_MODULE"] = os.environ.get("DJANGO_SETTINGS_MODULE")
    django.setup()
