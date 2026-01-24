from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('create-property/', views.create_property, name='create_property'),
    path('search/', views.search, name='search'),

    path('property/<uuid:property_id>/', views.property_detail, name='property_detail'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('property/<uuid:property_id>/edit/', views.edit_property, name='edit_property'),
    path('property/<uuid:property_id>/delete/', views.delete_property, name='delete_property'),

    path('property/<uuid:property_id>/images/', views.add_property_images, name='add_property_images'),

    path('property/<uuid:property_id>/inquire/', views.submit_inquiry, name='submit_inquiry'),
    path('inquiries/', views.manage_inquiries, name='manage_inquiries'),
]
