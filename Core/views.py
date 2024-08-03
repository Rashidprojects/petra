import re
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Core.models import Product, HangingPosition,ColorShade,Size, Material ,Quote,FindDealers,NewDealers,Complaints,Testimonials,Gallery,Blogs,Contact
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'Dashboard/Core/dashboard.html')


#----------------------------------- Manage Products -----------------------------------#

@login_required
def manage_products(request):
    products = Product.objects.all().order_by('-Date')

    context = {
        'products': products
    }
    return render(request, 'Dashboard/Products/products.html', context)

#----------------------------------- Add Product -----------------------------------#

@login_required
def add_product(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            images = [request.FILES.get(f'image{i}') for i in range(1, 6)]
            desc = request.POST.get('description')
            door_type = request.POST.get('door_type')
            hanging_position = request.POST.getlist('hanging_position')
            color_shade = request.POST.getlist('color_shade')
            material = request.POST.getlist('material')
            custom_sizes = request.POST.getlist('sizes')


            if name and images[0] and desc and door_type :
                product = Product(
                    Name=name,
                    Image=images[0],
                    Image2=images[1],
                    Image3=images[2],
                    Image4=images[3],
                    Image5=images[4],
                    Description=desc,
                    Door_type=door_type
                )
                product.save()

                hanging_objects = HangingPosition.objects.filter(id__in=hanging_position)
                product.Hanging_position.set(hanging_objects)
                
                color_objects = ColorShade.objects.filter(id__in=color_shade)
                product.Color_shade.set(color_objects)
                
                material_objects = Material.objects.filter(id__in=material)
                product.Materials.set(material_objects)
                
                size_ids = []
                for size in custom_sizes:
                    if size.isdigit():
                        size_ids.append(int(size))
                    else:
                        new_size_obj, created = Size.objects.get_or_create(Name=size)
                        size_ids.append(new_size_obj.id)
                
                if size_ids:
                    size_objects = Size.objects.filter(id__in=size_ids)
                    product.Sizes.set(size_objects)
                    
                product.save()

                messages.success(request, 'Product added successfully.')
                return redirect('manage-products')
            else:
                messages.warning(request, 'Please fill in all required fields.')
        except Exception as e:
            messages.warning(request, f"An error occurred: {str(e)}")
            return redirect('add-product')

    door_types = Product.DOOR_TYPES
    hanging_positions = HangingPosition.objects.all().order_by('id')
    color_shades = ColorShade.objects.all().order_by('id')
    materials = Material.objects.all().order_by('id')
    sizes = Size.objects.all().order_by('id')


    return render(request, 'Dashboard/Products/product-add.html', {
        'door_types': door_types,
        'hanging_positions': hanging_positions,
        'color_shades' : color_shades,
        'materials' : materials,
        'sizes' : sizes,
    })

#----------------------------------- Delete Product -----------------------------------#

@login_required
def delete_product(request):
    product_id = request.POST.get('product_id')
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('manage-products')

#----------------------------------- Edit Product -----------------------------------#

@login_required
def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        try:
            if 'image' in request.FILES:
                product.Image = request.FILES.get('image')

            if 'image2' in request.FILES:
                product.Image2 = request.FILES.get('image2')
                
            if 'image3' in request.FILES:
                product.Image3 = request.FILES.get('image3')

            product.Name = request.POST.get('name')
            product.Description = request.POST.get('description')
            product.save()
                
            messages.success(request, 'Product details edited successfully!')
            return redirect('manage-products')
        except Exception as exception:
            messages.warning(request, exception)
            return redirect('edit-product', product_id=product.id)
        
    context = {
        'product': product,
    }
    return render(request, 'Dashboard/Products/product-edit.html', context)


#----------------------------------- Manage Enquirys -----------------------------------#

@login_required
def manage_enquirys(request):
    quotes = Quote.objects.all().order_by('-Date')
    findEnquirys = FindDealers.objects.all().order_by('-Date')
    newDealers = NewDealers.objects.all().order_by('-Date')
    
    unread_quotes = Quote.objects.filter(Is_read=False).count()
    unread_findEnquirys = FindDealers.objects.filter(Is_read=False).count()
    unread_newDealers = NewDealers.objects.filter(Is_read=False).count()

    context = {
        'quotes': quotes,
        'findEnquirys': findEnquirys,
        'newDealers': newDealers,
        
        'unread_quotes': unread_quotes,
        'unread_findEnquirys': unread_findEnquirys,
        'unread_newDealers': unread_newDealers,

    }
    return render(request, 'Dashboard/Enquiry/enquiry.html', context)

#----------------------------------- Manage Quote Enquirys -----------------------------------#

@login_required
def manage_quotes(request):
    quotes = Quote.objects.all().order_by('-Date')

    context = {
        'quotes': quotes,
    }
    return render(request, 'Dashboard/Enquiry/quotes.html', context)

#----------------------------------- Manage Quote counts -----------------------------------#

@login_required
def update_read_status(request, quote_id):
    if request.method == 'POST':
        try:
            quote = Quote.objects.get(id=quote_id)
            quote.Is_read = not quote.Is_read
            quote.save()
            return JsonResponse({'success': True, 'is_read': quote.Is_read})
        except Quote.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Quote not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


@login_required
def mark_all_as_read(request):
    if request.method == 'POST':
        Quote.objects.all().update(Is_read=True)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})



#----------------------------------- Delete Quote -----------------------------------#

@login_required
def delete_quote(request):
    quote_id = request.POST.get('quote_id')
    quote = Quote.objects.get(id=quote_id)
    quote.delete()
    return redirect('manage-enquirys')

#----------------------------------- Manage Find Dealer Enquirys -----------------------------------#

@login_required
def manage_findDealers(request):
    enquirys = FindDealers.objects.all().order_by('-Date')

    context = {
        'enquiries': enquirys
    }
    return render(request, 'Dashboard/Enquiry/findDealers.html', context)

#----------------------------------- Manage FindDealers counts -----------------------------------#

@login_required
def update_read_find_dealer_status(request, findDealer_id):
    if request.method == 'POST':
        try:
            findDealer = FindDealers.objects.get(id=findDealer_id)
            findDealer.Is_read = not findDealer.Is_read
            findDealer.save()
            return JsonResponse({'success': True, 'is_read': findDealer.Is_read})
        except FindDealers.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Find Dealer not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})



@login_required
def mark_all_find_dealer_as_read(request):
    if request.method == 'POST':
        FindDealers.objects.all().update(Is_read=True)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

#----------------------------------- Delete Find Dealer Enquirys -----------------------------------#

@login_required
def delete_findDealer(request):
    findDealer_id = request.POST.get('findDealer_id')
    findDealer = FindDealers.objects.get(id=findDealer_id)
    findDealer.delete()
    return redirect('manage-enquirys')

#----------------------------------- Manage New Dealer Enquirys -----------------------------------#

@login_required
def manage_newDealers(request):
    enquirys = NewDealers.objects.all().order_by('-Date')

    context = {
        'enquiries': enquirys
    }
    return render(request, 'Dashboard/Enquiry/newDealers.html', context)

#----------------------------------- Manage NewDealers counts -----------------------------------#

@login_required
def update_read_new_dealer_status(request, newDealer_id):
    if request.method == 'POST':
        try:
            newDealer = NewDealers.objects.get(id=newDealer_id)
            newDealer.Is_read = not newDealer.Is_read
            newDealer.save()
            return JsonResponse({'success': True, 'is_read': newDealer.Is_read})
        except NewDealers.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'New Dealer not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})



@login_required
def mark_all_new_dealer_as_read(request):
    if request.method == 'POST':
        NewDealers.objects.all().update(Is_read=True)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

#----------------------------------- Delete New Dealer Enquirys -----------------------------------#

@login_required
def delete_newDealer(request):
    newDealer_id = request.POST.get('newDealer_id')
    newDealer = NewDealers.objects.get(id=newDealer_id)
    newDealer.delete()
    return redirect('manage-enquirys')

#----------------------------------- Manage Complaints -----------------------------------#

@login_required
def manage_complaints(request):
    complaints = Complaints.objects.all().order_by('-Date')

    context = {
        'complaints': complaints
    }
    return render(request, 'Dashboard/Services/complaints.html', context)

#----------------------------------- Delete Complaints -----------------------------------#

@login_required
def delete_complaint(request):
    complaint_id = request.POST.get('complaint_id')
    complaint = Complaints.objects.get(id=complaint_id)
    complaint.delete()
    return redirect('manage-complaints')

#----------------------------------- Manage Testimonials -----------------------------------#

@login_required
def manage_testimonials(request):
    testimonials = Testimonials.objects.all().order_by('-Date')

    context = {
        'testimonials': testimonials
    }
    return render(request, 'Dashboard/Media/testimonials.html', context)

#----------------------------------- Add Testimonials -----------------------------------#

@login_required
def add_testimonials(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            link = request.POST.get('link')

            if name and link:
                # Extract the video ID from the provided YouTube link
                youtube_id = extract_youtube_id(link)
                if youtube_id:
                    embed_link = f"https://www.youtube.com/embed/{youtube_id}"
                    testimonial = Testimonials(Name=name, Link=embed_link)
                    testimonial.save()

                    messages.success(request, 'Testimonial added successfully.')
                    return redirect('manage-testimonials')
                else:
                    messages.warning(request, 'Invalid YouTube link. Please provide a valid link.')
            else:
                messages.warning(request, 'Please fill in all required fields.')
        except Exception as e:
            messages.warning(request, f"An error occurred: {str(e)}")
            return redirect('add-testimonials')

    return render(request, 'Dashboard/Media/testimonials-add.html')

def extract_youtube_id(url):
    # This function extracts the YouTube video ID from various URL formats
    regex = (r'(https?://)?(www\.)?'
             '(youtube|youtu|youtube-nocookie)\.(com|be)/'
             '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    match = re.match(regex, url)
    return match.group(6) if match else None

#----------------------------------- Delete testimonials -----------------------------------#

@login_required
def delete_testimonials(request):
    testimonials_id = request.POST.get('testimonials_id')
    testimonials = Testimonials.objects.get(id=testimonials_id)
    testimonials.delete()
    return redirect('manage-testimonials')

#----------------------------------- Gallery -----------------------------------#

@login_required
def manage_gallery(request):
    gallery = Gallery.objects.all().order_by('-id')

    context = {
        'gallery' : gallery
    }
    return render(request,'Dashboard/Media/gallery.html',context)

#----------------------------------- Add Images -----------------------------------#

@login_required
def add_gallery(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images')

        for image in images:
            # resized = resize(image,800)
            try:
                Gallery.objects.create(Image=image)
            except Exception as exception:
                messages.warning(request,exception)
                return redirect('add-gallery')
        messages.success(request,'New images added successfully ... !')
        return redirect('manage-gallery')
    
#----------------------------------- Delete Image -----------------------------------#

@login_required
def delete_gallery(request):
    gallery_id = request.POST.get('gallery_id')
    gallery = Gallery.objects.get(id=gallery_id)
    gallery.delete()
    messages.warning(request,'Image Deleted ... !')
    return redirect('manage-gallery')


#----------------------------------- Manage Blogs -----------------------------------#

@login_required
def manage_blogs(request):
    blogs = Blogs.objects.all().order_by('-Date')

    context = {
        'blogs': blogs
    }
    return render(request,'Dashboard/Blogs/blogs.html',context)

#----------------------------------- Add Blogs -----------------------------------#

@login_required
def add_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        bannerImg = request.FILES.get('banner')
        desc = request.POST.get('desc')
        content = request.POST.get('content')
        

        try:
            # resized = resize(image,800)
            blog = Blogs.objects.create(Title=title, Image=image,BannerImg=bannerImg, Description=desc,Content=content)

            messages.success(request, 'New blog added successfully ...!')
            return redirect('manage-blogs')
        except Exception as exception:
            messages.warning(request, f'Error: {exception}')
            return redirect('add-blog')

    return render(request, 'Dashboard/Blogs/blog-add.html')

#----------------------------------- Delete Blog -----------------------------------#

@login_required
def delete_blog(request):
    blog_id = request.POST.get('blog_id')
    blog = Blogs.objects.get(id=blog_id)
    blog.delete()
    return redirect('manage-blogs')


#----------------------------------- Edit Blogs -----------------------------------#

@login_required
def edit_blog(request, blog_id):
    blog = Blogs.objects.get(id=blog_id)

    if request.method == 'POST':
        try:
            if 'image' in request.FILES:
                blog.Image = request.FILES.get('image')
            
            if 'bannerImg' in request.FILES:
                blog.BannerImg = request.FILES.get('bannerImg')

            blog.Title = request.POST.get('title')
            blog.Description = request.POST.get('desc')
            blog.Content = request.POST.get('content')
            blog.save()
                
            messages.success(request, 'Blog details edited successfully!')
            return redirect('manage-blogs')
        except Exception as exception:
            messages.warning(request, exception)
            return redirect('edit-blog', blog_id=blog.id)
        
    context = {
        'blog': blog,
    }
    return render(request, 'Dashboard/Blogs/blog-edit.html', context)

#----------------------------------- Contact Enquiries -----------------------------------#

@login_required
def enquiries(request):
    enquiries = Contact.objects.all().order_by('-id')

    context = {
        'enquiries' : enquiries
    }
    return render(request,'Dashboard/Core/enquiries.html',context)

#----------------------------------- Delete Contact Enquiry -----------------------------------#

@login_required
def delete_enquiry(request):
    if request.method == 'POST':
        enquiry_id = request.POST.get('enquiry_id')
        enquiry = Contact.objects.get(id=enquiry_id)
        enquiry.delete()
        return redirect('enquiries')