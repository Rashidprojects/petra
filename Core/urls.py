from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    path('product/list/',views.manage_products,name='manage-products'),
    path('product/add/',views.add_product,name='add-product'),
    path('product/delete/',views.delete_product,name='delete-product'),
    path('product/edit/<int:product_id>/', views.edit_product, name='edit-product'),
    path('size/delete/',views.delete_size,name='delete-size'),

    path('enquirys/list/',views.manage_enquirys,name='manage-enquirys'),
    
    path('quotes/list/',views.manage_quotes,name='manage-quotes'),
    path('quote/delete/',views.delete_quote,name='delete-quote'),
    path('quotes/update-read-status/<int:quote_id>/', views.update_read_status, name='update_read_status'),
    path('mark_all_as_read/', views.mark_all_as_read, name='mark_all_as_read'),
    
    path('findDealers/list/',views.manage_findDealers,name='manage-findDealers'),
    path('findDealers/delete/',views.delete_findDealer,name='delete-findDealer'),
    path('findDealers/update-read-status/<int:findDealer_id>/', views.update_read_find_dealer_status, name='update_read_find_dealer_status'),
    path('mark_all_find_dealer_as_read/', views.mark_all_find_dealer_as_read, name='mark_all_find_dealer_as_read'),
    
    path('newDealers/list/',views.manage_newDealers,name='manage-newDealers'),
    path('newDealers/delete/',views.delete_newDealer,name='delete-newDealer'),
    path('newDealers/update-read-status/<int:newDealer_id>/', views.update_read_new_dealer_status, name='update_read_new_dealer_status'),
    path('mark_all_new_dealer_as_read/', views.mark_all_new_dealer_as_read, name='mark_all_new_dealer_as_read'),
    
    path('complaints/list/',views.manage_complaints,name='manage-complaints'),
    path('complaints/delete/',views.delete_complaint,name='delete-complaint'),
    
    path('testimonial/list/',views.manage_testimonials,name='manage-testimonials'),
    path('testimonials/add/',views.add_testimonials,name='add-testimonials'),
    path('testimonials/delete/',views.delete_testimonials,name='delete-testimonials'),
    
    path('gallery/list/',views.manage_gallery,name='manage-gallery'),
    path('gallery/add/',views.add_gallery,name='add-gallery'),
    path('gallery/delete/',views.delete_gallery,name='delete-gallery'),
    
    path('blog/list/',views.manage_blogs,name='manage-blogs'),
    path('blog/add/',views.add_blog,name='add-blog'),
    path('blog/delete/',views.delete_blog,name='delete-blog'),
    path('blog/edit/<int:blog_id>/',views.edit_blog,name='edit-blog'),
    
    # Contact Enquirys
    path('enquiries/',views.enquiries,name='enquiries'),
    path('enquiry/delete/',views.delete_enquiry,name='delete-enquiry'),


]
