from django.urls import path, include

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('login/', views.login, name='login'),
	path('register/', views.register, name='register'),
	path('blank/', views.blank, name='blank'),
	path('buttons/', views.buttons, name='buttons'),
	path('cards/', views.cards, name='cards'),
	path('charts/', views.charts, name='charts'),
	path('forgot_password/', views.forgot_password, name='forgot_password'),
	path('tables/', views.tables, name='tables'),
	path('404/', views.not_found, name='404'),
	path('utilities_animation/', views.utilities_animation, name='utilities_animation'),
	path('utilities_border/', views.utilities_border, name='utilities_border'),
	path('utilities_color/', views.utilities_color, name='utilities_color'),
	path('utilities_other/', views.utilities_other, name='utilities_other'),
]