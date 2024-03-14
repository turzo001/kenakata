from django.contrib import admin
from sklearn.tree import DecisionTreeClassifier
import joblib
from .models import(
    Customer,
    Cart,
    Product,
    Cart,
    Orderplaced,
    # data
)

#costomer register
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','locality','city','zipcode','state']
    
# @admin.register(data)
# class PredictionsModelAdmin(admin.ModelAdmin):
#     list_display=['ram','rom','predictions']

# Product resister
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discounted_price','size','colour','description','brand',
                  'quantity','catagory','product_image']

#cart resister
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

#orderplace resister
@admin.register(Orderplaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_date','status']

# @admin.register(predict)
# class CustomerModelAdmin(admin.ModelAdmin):
#     list_display=['id','name','brand','ram','rom','price']

 