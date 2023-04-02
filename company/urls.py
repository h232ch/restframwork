from django.urls import re_path
from company import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^department$', views.department_api),
    re_path(r'^department/([0-9]+)$', views.department_api),

    re_path(r'^employee$', views.employee_api),
    re_path(r'^employee/([0-9]+)$', views.employee_api),

    re_path(r'^employee/savefile', views.save_file),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)