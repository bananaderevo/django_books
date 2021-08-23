from .views import BookList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', BookList)