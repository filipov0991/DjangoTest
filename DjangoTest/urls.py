
from django.contrib import admin
from django.urls import path
from Human import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('person/<int:person_id>/', views.person_info, name='person_info'),
    path('married-unemployed-in-city-n/', views.married_unemployed_in_city_n, name='married_unemployed_in_city_n')
]
