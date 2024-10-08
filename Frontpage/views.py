import ast #The ast module (Abstract Syntax Trees)
from django.shortcuts import render, get_object_or_404, redirect
from Core.models import Product,FindDealers,NewDealers,Complaints,Testimonials,Gallery,Blogs,Contact
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from Core.models import Quote  # Assuming you have a QuoteRequest model
from django.contrib import messages
from django.db.models import Q


def index(request):
    all_products = Product.objects.all()
    context = {
        'all_products': all_products,
    }
    return render(request, 'Frontpage/index.html', context)

def about(request):
    return render(request, 'Frontpage/about.html')

def products(request):
    all_products = Product.objects.all()
    luxury_products = Product.objects.filter(Q(Door_type_1='Luxury') | Q(Door_type_2='Luxury'))
    signature_products = Product.objects.filter(Q(Door_type_2='Signature') | Q(Door_type_1='Signature') )

    context = {
        'all_products': all_products,
        'luxury_products': luxury_products,
        'signature_products': signature_products,
    }

    return render(request, 'Frontpage/products.html', context)
    
def product_detail(request, slug):
    all_products = Product.objects.all()
    product = get_object_or_404(Product, Slug=slug)
    luxury_products = Product.objects.filter(Q(Door_type_1='Luxury') | Q(Door_type_2='Luxury'))
    
    # Assuming product.FixedSize is a string like "['value1', 'value2']"
    
    # Check if FixedSize is not None and is a valid string
    if product.FixedSize is not None:
        try:
            fixed_sizes = ast.literal_eval(product.FixedSize) # now fixed_sizes = ['value1', 'value2']
        except (ValueError, SyntaxError):
            fixed_sizes = []  # or handle it in another appropriate way
    else:
        fixed_sizes = []    
    
    context = {
        'product' : product,
        'all_products': all_products,
        'fixed_sizes': fixed_sizes,
        'luxury_products': luxury_products,
    }
    return render(request, 'Frontpage/product-detail.html', context)

@csrf_exempt
def findDealers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        district = request.POST.get('district')
        place = request.POST.get('place')
        
        try:
            FindDealers.objects.create(Name=name,Phone=phone,State=state,District=district,Place=place)
            messages.success(request,'Our team connect you soon ... !')
            return redirect('findDealers')
        except:
            return JsonResponse({'status':'failed'})
    return render(request, 'Frontpage/findNearDealers.html')

def becomeDealer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact_number')
        business = request.POST.get('business')
        address = request.POST.get('address')
        state = request.POST.get('state')
        district = request.POST.get('district')
        
        try:
            NewDealers.objects.create(Name=name,Email=email,Contact=contact,Business=business,Address=address,State=state,District=district)
            messages.success(request,'Our team connect you soon ... !')
            return redirect('becomeDealer')
        except:
            return JsonResponse({'status':'failed'})
    return render(request, 'Frontpage/becomeAdealers.html')

def registerWarranty(request):
    return render(request, 'Frontpage/registerWarranty.html')

@csrf_exempt
def registerComplaint(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        number = request.POST.get('number')
        warranty = request.POST.get('warranty')
        dealer = request.POST.get('dealer')
        description = request.POST.get('description')
        
        try:
            Complaints.objects.create(Name=name,Address=address,Contact=number,WarrantyCode=warranty,Dealer=dealer,Description=description)
            messages.success(request,'Our team connect you soon ... !')
            return redirect('registerComplaint')
        except:
            return JsonResponse({'status':'failed'})
    return render(request, 'Frontpage/registerComplaint.html')

def testimonials(request):
    videos = Testimonials.objects.all()
    
    context = {
        'videos' : videos
    }
    return render(request, 'Frontpage/testimonials.html', context)

def gallery(request):
    images = Gallery.objects.all().order_by('id')
    
    context = {
        'images' : images
    }
    return render(request, 'Frontpage/gallery.html', context)

def blogs(request):
    blogs = Blogs.objects.all().order_by('id')
    
    context = {
        'blogs' : blogs
    }
    return render(request, 'Frontpage/blogs.html', context)

def blog_detail(request, category, slug):
    if category == 'blog':
        blog = get_object_or_404(Blogs, slug=slug)
    else:
        blog = None


    return render(request, 'Frontpage/blog_detail.html', {'blog': blog})

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        place = request.POST.get('place')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')

        try:
            Contact.objects.create(Name=name,Email=email,Place=place,Mobile=mobile,Message=message)
            messages.success(request, 'Your enquiry submitted successfully.')
            return redirect('contact')
        except:
            return JsonResponse({'status':'failed'})
    return render(request,'Frontpage/contact.html')

def success_view(request):
    return render(request, 'Frontpage/success.html')

def submit_quote(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        door_hanging_position = request.POST.get('door_hanging_position')
        available_size = request.POST.get('available_size')
        available_color = request.POST.get('available_color')
        material = request.POST.get('available_material')


        selection = Quote(
            Name=username,
            Contact=phone_number,
            Hanging_position=door_hanging_position,
            Size=available_size,
            Color_shade =available_color,
            Material = material,
        )
        selection.save()
        messages.success(request, 'Our team connect you soon !')
        return redirect('products')  # Redirect to a success page after saving
    return redirect('product_detail')



