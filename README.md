# studylens-models
Internal Backend Models for Studylens Project, defined as seperately installable python package for re-use between web backend and data ingestion pipelines.

## Usage:

If using from a non-django application, initialize django setup with the following code - 

```import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "studylens_models.settings")
django.setup()
```