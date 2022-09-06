from django.urls import path, include
from rest_framework import routers
from .views import PersonGet, PersonCreate, PersonRetPutDel, CompanyView

router = routers.DefaultRouter()
router.register("company", CompanyView, basename='company')


urlpatterns = [
    # path('', views.test, name='test'),
    path('', include(router.urls)),
    path('persons_get/', PersonGet.as_view()),
    path('persons_create/', PersonCreate.as_view()),
    path('person/<int:pk>/', PersonRetPutDel.as_view()),
]