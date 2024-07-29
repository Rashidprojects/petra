# your_app/context_processors.py

from .models import Quote, FindDealers, NewDealers

def unread_counts(request):
    unread_quotes_count = Quote.objects.filter(Is_read=False).count()
    unread_findEnquirys_count = FindDealers.objects.filter(Is_read=False).count()
    unread_newDealers_count = NewDealers.objects.filter(Is_read=False).count()
    
    total_unread_enquirys = unread_quotes_count + unread_findEnquirys_count + unread_newDealers_count
    
    return {
        'total_unread_enquirys': total_unread_enquirys
    }
