from django.urls import path,include
from .views import BookList,BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Book', BookViewSet, basename='Book')
urlpatterns = [
    path('book/', BookList.as_view(), name= 'book-list'),
    path('', include(router.urls)),
]