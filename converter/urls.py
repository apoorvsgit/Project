
# converter/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('convert/', views.convert_pdf_to_word, name='convert_pdf_to_word'),
]
