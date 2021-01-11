from django.urls import path
from . import views
from .views import search,terms
from .orderview import (
    orderproduct, 
    orderfood, 
    bookservice,
    OrderProductDeleteView,
    OrderFoodDeleteView,
    BookServiceDeleteView

) 

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', search, name='search'),
    path('contact/', views.contant, name='contact'),
    path('terms/', terms, name='terms'),
    path('pr/<str:username>/order/', orderproduct, name='order-product'),
    path('rs/<str:username>/order/', orderfood, name='order-food'),
    path('sv/<str:username>/book/', bookservice, name='book-service'),
    path('pr/order/<int:pk>/detele', OrderProductDeleteView.as_view(), name='prorder-delete'),
    path('rs/order/<int:pk>/detele', OrderFoodDeleteView.as_view(), name='foodorder-delete'),
    path('sv/book/<int:pk>/detele', BookServiceDeleteView.as_view(), name='bookservice-delete')

]
