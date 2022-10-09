from django.contrib import admin

from .models import Flat, Complain, Owner

class OwnerFlatInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ["owner", "flat"]

class FlatAdmin(admin.ModelAdmin):
    inlines = [OwnerFlatInline]
    search_fields = ('town', 'address')
    readonly_fields = ["created_at"]
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ["liked_by"]

class ComplainAdmin(admin.ModelAdmin):
    raw_id_fields = ["complainant", "contested_flat"]

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ["flats"]

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complain, ComplainAdmin)
admin.site.register(Owner, OwnerAdmin)
