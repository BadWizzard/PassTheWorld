from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('rooms/', views.get_rooms),
    path('rooms/create/', views.create_room),
    path('room/', views.get_room),

    
    #path('hello/', views.say_hello),
    #path('customers/', views.show_customers),
    #path('collections/', views.show_collections_with_no_products),
    #path('products_without_order/', views.products_without_order),
    #path('aggregates/', views.get_aggregates),
    #path('expressions/', views.get_expressions),
    #path('create_objects/', views.create_objects),
]