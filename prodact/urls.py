from django.urls import path
from . import views





app_name = 'home'

urlpatterns = [
    path('',views.ProductManage.as_view()),
    path('<int:pk>',views.ProductDetail.as_view()),
    path('my', views.MyProduct.as_view()),
    path('chat/<int:id_product>', views.ChatUser.as_view()),
    path('ListChat', views.ListChat.as_view())



]