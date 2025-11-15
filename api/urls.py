from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('products/', views.ProductAPIView.as_view(), name='product_list_api'),
    path('products/<pk>', views.ProductDetailAPIView.as_view(), name='product_detail_api'),
    path('users/', views.ShopUserListAPIView.as_view(), name='users_by_api'),
    path('register/', views.UerRegistrationAPIView.as_view(), name='user_register_by_api')


]