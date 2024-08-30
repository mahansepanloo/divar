from django.urls import path
from . import views





app_name = 'home'

urlpatterns = [
    path('',views.ProdactShome.as_view()),
    path('<int:pk>', views.propk.as_view()),




]