from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    path('', views.home, name='home'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('registration/', views.register),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='checkout'),
    path('<slug:val>/', views.category, name='category'),
    path('cart/order_placed/', views.thx, name='order_placed')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)