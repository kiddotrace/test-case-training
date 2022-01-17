from django.urls import path

from products.views import ProductCreate, ProductList, ProductUpdate, ProductDelete
from products.api import ListProductAPIView, UpdateProductAPIView, CreateProductAPIView, DeleteProductAPIView

app_name = 'products'

urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('create/', ProductCreate.as_view(), name='create'),
    path('<pk>/', ProductUpdate.as_view(), name='update'),
    path('delete/<pk>/', ProductDelete.as_view(), name='delete'),
    path('api/list', ListProductAPIView.as_view(), name='list_api'),
    path('api/create/', CreateProductAPIView.as_view(), name='create_api'),
    path('api/update/<pk>/', UpdateProductAPIView.as_view(), name='update_api'),
    path('api/delete/<pk>/', DeleteProductAPIView.as_view(), name='delete_api'),
]
