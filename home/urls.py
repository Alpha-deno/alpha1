from django.urls import path
from . import views
from .views import search
from .orderview import (
    orderproduct, 
    orderfood, 
    bookservice,
    OrderProductDeleteView,
    OrderFoodDeleteView,
    BookServiceDeleteView,
    OrderproductDeleteView,
    OrderfoodDeleteView,
    BookserviceDeleteView

) 
from business.views import terms

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', search, name='search'),
    path('contact/', views.contant, name='contact'),
    path('location/<str:location>/', views.mylocation, name='mylocation'),
    path('pr/<str:username>/order/', orderproduct, name='order-product'),
    path('rs/<str:username>/order/', orderfood, name='order-food'),
    path('sv/<str:username>/book/', bookservice, name='book-service'),
    path('pr/order/<int:pk>/detele', OrderProductDeleteView.as_view(), name='prorder-delete'),
    path('rs/order/<int:pk>/detele', OrderFoodDeleteView.as_view(), name='foodorder-delete'),
    path('sv/book/<int:pk>/detele', BookServiceDeleteView.as_view(), name='bookservice-delete'),
    path('pro/order/<int:pk>/detele', OrderproductDeleteView.as_view(), name='proorder-delete'),
    path('rse/order/<int:pk>/detele', OrderfoodDeleteView.as_view(), name='fdorder-delete'),
    path('svi/book/<int:pk>/detele', BookserviceDeleteView.as_view(), name='bkservice-delete'),
    path('terms',terms, name='terms') 

]
