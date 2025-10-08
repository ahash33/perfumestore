from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [
    path('', views.basic, name='basic'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('collection/', views.collection, name='collection'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact_view, name='contact'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('order/', views.order_perfume, name='order'),
    path('order/success/', views.order_success, name='order_success'),
]