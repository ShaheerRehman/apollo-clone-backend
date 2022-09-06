from django.urls import path, include
from . import views
from rest_framework import routers
from .views import PersonView, CompanyView

router = routers.DefaultRouter()
router.register("persons", PersonView, basename='persons')
router.register("company", CompanyView, basename='company')


urlpatterns = [
    # path('', views.test, name='test'),
    path('', include(router.urls)),
]