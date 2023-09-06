from django.urls import path
from .import views


urlpatterns=[ 
    path('',views.uploadresume,name='home'),
    path('search',views.search,name='search'),
    path('pdf',views.pdf_view,name='pdf')
]