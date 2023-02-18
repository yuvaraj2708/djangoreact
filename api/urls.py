from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import ContactViewSet
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import MeView
router = DefaultRouter()
router.register(r'contacts', ContactViewSet)
urlpatterns = router.urls


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('me/', MeView.as_view(), name='me'),
    ]