from django.contrib import admin
from .models import Advertisement

# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'user', 'price', 'auction', 'created_at', 'created_date', 'updated_date', 'image', 'show_mini_image']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_true', 'make_auction_false']

    @admin.action(description='Перевести auction в True')
    def make_auction_true(self, request, query):
        query.update(auction=True)

    @admin.action(description='Перевести auction в False')
    def make_auction_false(self, request, query):
        query.update(auction=False)

    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'user', 'image'),
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

admin.site.register(Advertisement, AdvertisementAdmin)