from django.contrib import admin
from django.urls import include, path
from api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('api',views.TodoViewSet,basename='todoapi')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    # path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    # path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
    # path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'),
]