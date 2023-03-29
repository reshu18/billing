from django.urls import path
from .views import login_view,dashboard,logout_view,index,billing

urlpatterns = [
    path('login/',login_view, name='login'),
    path('dashboard/',dashboard, name='dashboard'),
    path('logout/',logout_view, name='logout'),
    
    path('index/',index,name='index'),
    path('billing/',billing,name='billing')
    
]
