from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.http import HttpResponse
from .settings.base import *
from django.core.paginator import Paginator
from .models import BlogSingle


class IndexView(View):

    def get(self, request):
    
        for k, v in request.COOKIES.items():
            print(k, v)
    
        return render(request, 'shop/index.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL, 'promotext': PROMO, 'address': ADDRESS})

class ShopView(View):

    def get(self, request, page_id=1):

        products_list = [{'name': 'Bell Pepper',
                          'image': 'shop/images/product-1.jpg',
                          'price': '$120.00',
                          'discount': '30%',
                          'price_sale': '$80.00'},
                         {'name': 'Strawberry',
                          'image': 'shop/images/product-2.jpg',
                          'price': '$120.00'},
                         {'name': 'Green Beans',
                          'image': 'shop/images/product-3.jpg',
                          'price': '$120.00'},
                         {'name': 'Purple Cabbage',
                          'image': 'shop/images/product-4.jpg',
                          'price': '$120.00'},
                         {'name': 'Tomatoe',
                          'image': 'shop/images/product-5.jpg',
                          'price': '$120.00',
                          'discount': '30%',
                          'price_sale': '$80.00'},
                         {'name': 'Brocolli',
                          'image': 'shop/images/product-6.jpg',
                          'price': '$120.00'},
                         {'name': 'Carrots',
                          'image': 'shop/images/product-7.jpg',
                          'price': '$120.00'},
                         {'name': 'Fruit Juice',
                          'image': 'shop/images/product-8.jpg',
                          'price': '$120.00'},
                         {'name': 'Onion',
                          'image': 'shop/images/product-9.jpg',
                          'price': '$120.00',
                          'discount': '30%',
                          'price_sale': '$80.00'},
                         {'name': 'Apple',
                          'image': 'shop/images/product-10.jpg',
                          'price': '$120.00'},
                         {'name': 'Garlic',
                          'image': 'shop/images/product-11.jpg',
                          'price': '$120.00'},
                         {'name': 'Chilli',
                          'image': 'shop/images/product-12.jpg',
                          'price': '$120.00'}]

        paginator = Paginator(products_list, 4)

        try:
            products = paginator.page(page_id)
            products.num_pages_tuple = tuple(range(paginator.num_pages))
        except:
            return redirect(reverse('shop'))

        return render(request, 'shop/shop.html', {'products': products, 'phone_number': PHONE_NUMBER, 'email': EMAIL, 'promotext': PROMO, 'address': ADDRESS})


class AboutView(View):

    def get(self, request):
        return render(request, 'shop/about.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL, 'promotext': PROMO, 'address': ADDRESS})


class ContactView(View):

    def get(self, request):
        return render(request, 'shop/contact.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL, 'promotext': PROMO, 'address': ADDRESS})


class BlogView(View):

    def get(self, request, page_id=1):

        blog_list = [{'header': 'Hello!',
                      'image': 'shop/images/image_1.jpg',
                      'details': 'Hello, hello!',
                      'date': '3th of July, 2020',
                      'author': 'Admin',
                      'comment_number': '3'},
                     {'header': 'Hello!',
                      'image': 'shop/images/image_2.jpg',
                      'details': 'Hello, hello!',
                      'date': '5th of July, 2020',
                      'author': 'Admin',
                      'comment_number': '3'},
                     {'header': 'Hello!',
                      'image': 'shop/images/image_3.jpg',
                      'details': 'Hello, hello!',
                      'date': '6th of July, 2020',
                      'author': 'Admin',
                      'comment_number': '3'},
                     {'header': 'Hello!',
                      'image': 'shop/images/image_4.jpg',
                      'details': 'Hello, hello!',
                      'date': '12th of July, 2020',
                      'author': 'Admin',
                      'comment_number': '3'},
                     {'header': 'Hello!',
                      'image': 'shop/images/image_5.jpg',
                      'details': 'Hello, hello!',
                      'date': '19th of August, 2020',
                      'author': 'Admin',
                      'comment_number': '3'},
                     {'header': 'Hello!',
                      'image': 'shop/images/image_6.jpg',
                      'details': 'Hello, hello!',
                      'date': '30th of August, 2020',
                      'author': 'Admin',
                      'comment_number': '3'}]

        paginator = Paginator(blog_list, 6)

        try:
            blogs = paginator.page(page_id)
            blogs.num_pages_tuple = tuple(range(paginator.num_pages))
        except:
            return redirect(reverse('blog'))

        return render(request, 'shop/blog.html', {'blog_list': blogs, 'phone_number': PHONE_NUMBER, 'email': EMAIL, 'promotext': PROMO, 'address': ADDRESS})


class BlogSingleView(View):

    def get(self, request):
        return render(request, 'shop/blog-single.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL, 'promotext': PROMO, 'address': ADDRESS})


class WishlistView(View):

    def get(self, request):
        return render(request, 'shop/wishlist.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL, 'promotext': PROMO, 'address': ADDRESS})


class ProductSingleView(View):

    def get(self, request):
        return render(request, 'shop/product-single.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL, 'promotext': PROMO, 'address': ADDRESS})


class CartView(View):

    def get(self, request):
        return render(request, 'shop/cart.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL, 'promotext': PROMO, 'address': ADDRESS})


class CheckoutView(View):

    def get(self, request):
        return render(request, 'shop/checkout.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL, 'promotext': PROMO, 'address': ADDRESS})