from django.conf.urls import url, include
from rest_framework import routers
from core.views import UserList

router = routers.DefaultRouter()
#router.register(r'students', StudentViewSet)
router.register(r'^users/(?P<pk>[0-9]+)/$', UserList.as_view())
urlpatterns = router.urls