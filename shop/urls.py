from django.urls import path

from . import views

urlpatterns = [
    path('shop/greetings/', views.greetings, name='greetings'),
    path('shop/', views.list_item, name='item_list'),
    path('<int:item_id>', views.detail_item, name='detail_item'),
]