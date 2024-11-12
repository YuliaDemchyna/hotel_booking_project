from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('hotel/<int:hotel_id>/', views.hotel_detail_view, name='hotel_detail'),
    path('hotel/<int:hotel_id>/room/<int:room_id>/book/', views.booking_page_view, name='book_room'),
    path('confirmation/<int:booking_id>/', views.confirmation_page_view, name='confirmation'),
]