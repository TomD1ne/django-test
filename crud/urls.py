from django.urls import include, path
from crud import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"software", views.SoftwareViewSet)

urlpatterns = [
    path("error/", views.exampleError),
    path("companies/<int:company_id>/", views.CompanyByIdView.as_view()),
    path("companies/", views.CompanyView.as_view()),
    path("", include(router.urls)),
]
