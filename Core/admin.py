from django.contrib import admin
from .models import HangingPosition,ColorShade,Quote,FindDealers,Material,Size,Product

# Register your models here.
admin.site.register(HangingPosition)
admin.site.register(ColorShade)
admin.site.register(Material)
admin.site.register(Quote)
admin.site.register(FindDealers)
admin.site.register(Size)
admin.site.register(Product)