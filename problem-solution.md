# Problem-Solution project timeline
---

## Explanations

urlpatterns (in rango_app/urls.py)
- This project/urls.py file has three ways of functioning, I picked up the third one.
- I create my own URL file in app/urls.py and then I included here with include().

import area (in rango_app/urls.py)
- Here I associate URLs to Views
- So I need to import django.urls to use func path and views to create the relationship