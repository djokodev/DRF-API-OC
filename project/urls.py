from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from shop.view import CategoryViewset
from shop.view import ProductViewset

#creons notre router
router = routers.SimpleRouter()

router.register('category', CategoryViewset, basename='category')
router.register('product', ProductViewset, basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
