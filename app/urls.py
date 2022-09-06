from django.urls import path, include
from rest_framework import routers
from .views import PersonGet, Person, CompanyView

router = routers.DefaultRouter()
router.register("company", CompanyView, basename='company')


urlpatterns = [
    # path('', views.test, name='test'),
    path('', include(router.urls)),
    path('persons_get/', PersonGet.as_view()),
    path('persons/', Person.as_view()),
]