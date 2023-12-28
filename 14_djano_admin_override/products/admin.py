from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Review



class ReviewInline(admin.TabularInline):
    model = Review
    extra = 2
    classes = ('collapse',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "update_date", "is_in_stock", "bring_img_to_list")
    list_editable = ("is_in_stock",)
    # list_display_links = ("create_date",)
    list_filter = ("is_in_stock","create_date")
    ordering = ("-name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    list_per_page = 25
    date_hierarchy = "update_date"

    inlines = [ReviewInline]
    readonly_fields = ("bring_image",)

    # fields = (("name", "slug"), "is_in_stock", "description")
    fieldsets =(
        (None, {
        "fields" : (
            ("name", "slug"), "is_in_stock", "bring_image", "product_img"
        )}),
        ("Optioanl Settings", {
            "classes":("collapse",),
            "fields": ("description",),
            "description":"You can this section for optional settings."

        })
    )

    actions = ("is_in_stock",)
    def is_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f"{count} stoğa eklendi")

    is_in_stock.short_description="İşaretlenen ürünleri stoğa ekle" 

    def bring_image(self, obj):
        if obj.product_img:
            return mark_safe(f"<img src={obj.product_img.url} width=400 height=400></img>")
        return mark_safe(f"<h3>{obj.name} has not image </h3>")
    
    def bring_img_to_list(self, obj):
        if obj.product_img:
            return mark_safe(f"<img src={obj.product_img.url} width=50 height=50></img>")
        return mark_safe("******")
    
    bring_img_to_list.short_description = "product_image"


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'create_date', "is_released")
    list_per_page = 50
    raw_id_fields = ('product',)



admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)


admin.site.site_title = "Cosmios Product"
admin.site.site_header = "Cosmios Product Admin Portal"
admin.site.index_title = "Welcome To Cosmios Product Admin Portal"


