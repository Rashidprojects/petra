from django.contrib import admin
from .models import HangingPosition,ColorShade,Quote,FindDealers

# Register your models here.
admin.site.register(HangingPosition)
admin.site.register(ColorShade)
admin.site.register(Quote)
admin.site.register(FindDealers)