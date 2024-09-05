from django import template
from babel.dates import format_date
from django.utils import timezone
import datetime  # Import datetime module

register = template.Library()

@register.filter
def format_arabic_date(value):
    if isinstance(value, datetime.date):  # Check if the value is a date object
        # Convert date to datetime at midnight
        value = datetime.datetime.combine(value, datetime.time.min)
    
    # Ensure datetime is timezone-aware
    if isinstance(value, datetime.datetime):
        if timezone.is_naive(value):
            # Make datetime timezone-aware using the default Django timezone
            value = timezone.make_aware(value, timezone.get_default_timezone())
        # Adjust the datetime to the current timezone
        value = timezone.localtime(value)
        return format_date(value, 'MMMM yyyy', locale='ar_TN')
    
    return value