from django.contrib import admin
from .models import (
    BusinessActivator, 
    Contant, 
    OrderProduct, 
    OrderFood, 
    BookService, 
    Restaurant, 
    Service,
    Product,
    NonUserBookService,
    NonUserOrderFood,
    NonUserOrderProduct
)
admin.site.register(BusinessActivator)
admin.site.register(Contant)
admin.site.register(OrderProduct)
admin.site.register(OrderFood)
admin.site.register(BookService)
admin.site.register(Restaurant)
admin.site.register(Service)
admin.site.register(Product)
admin.site.register(NonUserBookService)
admin.site.register(NonUserOrderFood)
admin.site.register(NonUserOrderProduct)
