from django.urls import path
from mainapp import views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='products'),
    path('category/<int:pk>/', mainapp.products, name='category'),
    path('category/<int:pk>/<int:page>/', mainapp.products, name='category_page'),
    path('product/<int:pk>/', mainapp.products, name='product'),

]
