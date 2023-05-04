from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views


urlpatterns = [
    path('', views.endpoints, name="endpoints"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('advocates/', views.advocates_list, name="advocates"),
    path('advocates/<str:username>', views.AdvocateDetail.as_view(), name="advocates-details"),
    path('company/', views.company_list, name="company-list"),
]

