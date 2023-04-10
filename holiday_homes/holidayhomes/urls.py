from rest_framework import routers

from .views import OwnerViewSet, RoomViewSet, HolidayHomeViewSet, HomeDetailViewSet

router = routers.DefaultRouter()
router.register(r'owner', OwnerViewSet, basename='owner')
router.register(r'room', RoomViewSet, basename='room')
router.register(r'holiday_home', HolidayHomeViewSet, basename='holiday_home')
router.register(r'home_detail', HomeDetailViewSet, basename='home_detail')

urlpatterns = router.urls
