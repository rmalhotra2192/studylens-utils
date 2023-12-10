# studylens-utils
Internal Utils for Studylens Project, defined as seperately installable python package for re-use between web backend and data ingestion pipelines, includes reusable data models, search core related to qdrant and openai integrations.

## Usage:

If using from a non-django application and need to use the data models then initialize django setup with the following code - 

```import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "studylens_models.settings")
django.setup()
```