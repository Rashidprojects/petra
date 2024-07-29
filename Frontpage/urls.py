from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('products/',views.products,name='products'),
    path('product/<slug:slug>/',views.product_detail,name='product_detail'),
    path('findDealers/',views.findDealers,name='findDealers'),
    path('becomeDealer/',views.becomeDealer,name='becomeDealer'),
    path('registerWarranty/', views.registerWarranty, name='registerWarranty'),
    path('registerComplaint/', views.registerComplaint, name='registerComplaint'),
    path('testimonials/',views.testimonials,name='testimonials'),
    path('gallery/',views.gallery,name='gallery'),
    path('blogs/',views.blogs,name='blogs'),
    path('<str:category>/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('contact/',views.contact,name='contact'),
    path('submit-quote/', views.submit_quote, name='submit_quote'),
    path('success/', views.success_view, name='success_view'),


]
