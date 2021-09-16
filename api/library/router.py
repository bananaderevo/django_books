from .views import BookList, OrderView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('list', BookList)
router.register('order', OrderView)