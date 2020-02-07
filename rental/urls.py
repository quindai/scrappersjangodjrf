from rest_framework import routers
from . import views as myview

router = routers.DefaultRouter()
router.register(r'friends', myview.FriendViewset)
router.register(r'belongings', myview.BelongingViewset)
router.register(r'borrowings', myview.BorrowedViewset)