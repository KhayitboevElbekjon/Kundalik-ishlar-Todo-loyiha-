
from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home),
    path('HomeEdit/<int:son>',HomeEdit),
    path('qushish/',qushish),
    path('edit/<int:son>',TodoEdit)
]
