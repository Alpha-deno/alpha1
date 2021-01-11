from django import forms
from .models import Contant,OrderProduct,OrderFood,BookService

class ContantForm(forms.ModelForm):
    class Meta:
        model = Contant
        fields = ['Your_Name', 'Phone_Number', 'Subject', 'message']

class OrderProductForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = ['Phone_Number', 'location', 'product_1', 'product_2', 'product_3', 'product_4', 'product_5', 'product_6']

class OrderFoodForm(forms.ModelForm):
    class Meta:
        model = OrderFood
        fields = ['table_number', 'location', 'Phone_Number', 'meal_1', 'meal_2', 'meal_3', 'meal_4', 'meal_5', 'meal_6']

class BookServiceForm(forms.ModelForm):
    class Meta:
        model = BookService
        fields = ['Phone_Number', 'checkin_date', 'service_1', 'service_2', 'service_3', 'service_4']