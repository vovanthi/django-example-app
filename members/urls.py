from rest_framework import routers
from .views import MemberViewSet, MemberListViewSet

router = routers.DefaultRouter()
router.register(r'members', MemberViewSet, base_name='members')
router.register(r'memberslist', MemberListViewSet, base_name='memberslist')
