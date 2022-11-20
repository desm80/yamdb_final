from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TokenObtainPairView, UserSignUpView, UserViewSet

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
urlpatterns = [
    path('', include(router.urls)),
    path(
        'auth/token/', TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'auth/signup/', UserSignUpView.as_view(),
        name='sign_up'
    ),
]
