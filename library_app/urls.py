from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('books/',views.books,name='books'),
    path('member/', views.member, name='member'),
    path('issue/',views.issue,name='issue'),
    path("searchpage/",views.search_page,name="searchpage"),
    path('login/',views.login_user, name = 'login'),
    path('registration/',views.register_user, name = 'registration'),
    path('logout/',views.logout_user, name='logout'),
]