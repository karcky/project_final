from django.contrib import admin
from . models import admin_create,useradd,index_panal,addtax,adding_product,quotation_add,purchase_add,stock_transfer_adding,add_sales,unitadd

# Register your models here.
admin.site.register(admin_create)
admin.site.register(useradd)
admin.site.register(index_panal)
admin.site.register(addtax)
admin.site.register(adding_product)
admin.site.register(quotation_add)
admin.site.register(purchase_add)
admin.site.register(stock_transfer_adding)
admin.site.register(add_sales)
admin.site.register(unitadd)



