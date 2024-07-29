from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import datetime

class HangingPosition(models.Model):
    Name = models.CharField(max_length=50)  # Left, Right
    
    def __str__(self):
        return self.Name

class ColorShade(models.Model):
    Name = models.CharField(max_length=50)  # Wooden, Dark
    
    def __str__(self):
        return self.Name

class Size(models.Model):
    Name = models.CharField(max_length=50)  # 2050x1200x90 mm, etc.
    
    def __str__(self):
        return self.Name
    
class Product(models.Model):
    DOOR_TYPES = [
        ('luxury', 'Luxury'),
        ('single', 'Single'),
        ('double', 'Double'),
    ]
    
    
    Date = models.DateField(auto_now_add=True )
    Name = models.CharField(max_length=100)
    Slug = models.SlugField(unique=True, blank=True, null=True)
    Image = models.ImageField(null=True, upload_to='Premiums')
    Image2 = models.ImageField(null=True, upload_to='Premiums', blank=True)
    Image3 = models.ImageField(null=True, upload_to='Premiums', blank=True)
    Image4 = models.ImageField(null=True, upload_to='Premiums', blank=True)
    Image5 = models.ImageField(null=True, upload_to='Premiums', blank=True)
    Description = models.TextField(null=True, blank=True) 
    Door_type = models.CharField(max_length=10, choices=DOOR_TYPES)
    Hanging_position = models.ManyToManyField('HangingPosition', blank=True)
    Color_shade = models.ManyToManyField('ColorShade', blank=True)
    Sizes = models.ManyToManyField('Size', blank=True)
    
    def save(self, *args, **kwargs):
        if not self.Slug:
            base_slug = slugify(self.Name)
            slug = base_slug
            counter = 1
            while Product.objects.filter(Slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.Slug = slug
        super().save(*args, **kwargs)
        
         # Debugging print statements
        print(f"Product Name: {self.Name}")
        print(f"Generated Slug: {self.Slug}")
    
    def __str__(self):
        return self.Name
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.Slug])
    
class QuoteRequest(models.Model):
    Date = models.DateField(auto_now_add=True )
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    hanging_position = models.CharField(max_length=50, null=True, blank=True)
    material = models.CharField(max_length=50, null=True, blank=True)
    color_shade = models.CharField(max_length=50, null=True, blank=True)
    size = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"Quote request from {self.name}"
    
class Quote(models.Model):
    Date = models.DateField(auto_now_add=True )
    Name = models.CharField(max_length=100)
    Contact = models.CharField(max_length=15)
    Hanging_position = models.CharField(max_length=50, null=True, blank=True)
    Color_shade = models.CharField(max_length=50, null=True, blank=True)
    Size = models.CharField(max_length=50, null=True, blank=True)
    Is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Quote request from {self.Name}"

class FindDealers(models.Model):
    Date = models.DateField(auto_now_add=True )
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    State = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    Place = models.CharField(max_length=50)
    Is_read = models.BooleanField(default=False)

    
    def __str__(self):
        return self.Name
    
class NewDealers(models.Model):
    Date = models.DateField(auto_now_add=True )
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=15)
    Business = models.CharField(max_length=30)
    Address = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    Is_read = models.BooleanField(default=False)

    
    def __str__(self):
        return self.Name
    
class Complaints(models.Model):
    Date = models.DateField(auto_now_add=True )
    Name = models.CharField(max_length=30)
    Address = models.CharField(max_length=100)
    Contact = models.CharField(max_length=15)
    WarrantyCode = models.CharField(max_length=15)
    Dealer = models.CharField(max_length=30)
    Description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name
    
class Testimonials(models.Model):
    Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=30, blank=True, null=True)
    Link = models.CharField(max_length=250)
    
    def __str__(self):
        return self.Name
    
class Gallery(models.Model):
    Date = models.DateTimeField(auto_now_add=True)
    Image = models.ImageField(null=True, upload_to='Gallery')
    
class Blogs(models.Model):
    Date = models.DateTimeField(auto_now_add=True)
    Title = models.CharField(max_length=100)
    Image = models.ImageField(null=True,upload_to='Blogs')
    BannerImg = models.ImageField(null=True,upload_to='Blogs')
    Description = models.TextField(null=True, blank=True)
    Content = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    
    class Meta:
        ordering = ['Title']
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.Title)
            slug = base_slug
            counter = 1
            while Blogs.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('blog_detail', args=['blog', self.slug])
    
class Contact(models.Model):
    Date = models.DateField(auto_now_add=True)
    Email = models.EmailField(max_length=100)
    Name = models.CharField(max_length=100)
    Place = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=20,null=True)
    Message = models.TextField()

    


