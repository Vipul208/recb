from django.contrib import admin
from .models import introbanner,noticeboard, event, lslider, faq, gallerie, word

# Register your models here.
admin.site.register(introbanner)
admin.site.register(noticeboard)
admin.site.register(gallerie)
admin.site.register(event)
admin.site.register(lslider)
admin.site.register(faq)
admin.site.register(word)