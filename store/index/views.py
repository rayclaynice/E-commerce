from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def home(request):
	all_products = Product.objects.all
	context = {'all_products': all_products}


	return render(request, 'index.html', context)


def categories(request):
	all_categories = Category.objects.all()
	return{'all_categories':all_categories}


def category_details(request, category_slug=None):
	category = get_object_or_404(Category, slug=category_slug)
	products = Product.objects.filter(category = category) #we are filtering all thje product that are under this category
	return render(request, 'Shop.html', {'category':category, 'products':products})



def product_details(request, product_slug):
	product = get_object_or_404(Product, slug=product_slug)
	context = {'product':product}
	return render(request, 'details.html', context)


