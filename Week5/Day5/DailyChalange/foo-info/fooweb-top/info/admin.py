from django.contrib import admin
from .models import Person
# from phonenumber_field.modelfields import PhoneNumberField NOT INSALLED
# from phonenumber_field.widgets import PhoneNumberPrefixWidget


# Register your models here.
class PhoneRegion(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'address']
    list_editable = ['phone_number']

    # formfield_overrides = {
    #     PhoneNumberField: {"widget": PhoneNumberPrefixWidget},
    # }

    search_fields = ('name', 'phone_number', 'email')


admin.site.register(Person, PhoneRegion)