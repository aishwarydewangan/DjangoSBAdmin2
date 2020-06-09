from django.shortcuts import render

def index(request):
	return render(request, 'base/index.html')

def login(request):
	return render(request, 'base/login.html')

def register(request):
	return render(request, 'base/register.html')

def blank(request):
	return render(request, 'base/blank.html')

def buttons(request):
	return render(request, 'base/buttons.html')

def cards(request):
	return render(request, 'base/cards.html')

def charts(request):
	return render(request, 'base/charts.html')

def forgot_password(request):
	return render(request, 'base/forgot-password.html')

def tables(request):
	return render(request, 'base/tables.html')

def not_found(request):
	return render(request, 'base/404.html')

def utilities_animation(request):
	return render(request, 'base/utilities-animation.html')

def utilities_border(request):
	return render(request, 'base/utilities-border.html')

def utilities_color(request):
	return render(request, 'base/utilities-color.html')

def utilities_other(request):
	return render(request, 'base/utilities-other.html')