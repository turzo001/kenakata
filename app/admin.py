from django.contrib import admin
from .models import(
    Customer,
    Cart,
    Product,
    Cart,
    Orderplaced
)

#costomer register
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','locality','city','zipcode','state']

# Product resister
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discounted_price','size','colour','description','brand',
                  'catagory','product_image']

#cart resister
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

#orderplace resister
@admin.register(Orderplaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_date','status']

 