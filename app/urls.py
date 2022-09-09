from django.urls import path, include, re_path
from rest_framework import routers
from .views import PersonGet, PersonCreate, PersonRetPutDel, CompanyView, PersonsListOnLocation, PersonsListOnJob, PersonsListOnCompany

router = routers.DefaultRouter()
router.register("company", CompanyView, basename='company')


urlpatterns = [
    # path('', views.test, name='test'),
    path('', include(router.urls)),
    path('persons_get/', PersonGet.as_view()),
    path('persons_create/', PersonCreate.as_view()),
    path('person/<int:pk>/', PersonRetPutDel.as_view()),
    # path('search/', ProductListOnLocation.as_view() ),
    re_path('^search/location/(?P<location>.+)/$', PersonsListOnLocation.as_view()),
    re_path('^search/job/(?P<job>.+)/$', PersonsListOnJob.as_view()),
    re_path('^search/company/(?P<comp>.+)/$', PersonsListOnCompany.as_view()),
]