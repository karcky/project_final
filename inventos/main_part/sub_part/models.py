from django.db import models
from django.db.models.base import Model


#index
class index_panal(models.Model):
    cand_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=40)
    address=models.CharField(max_length=100)
    messages=models.CharField(max_length=100)

    def __str__(self):
        return self.cand_name

#admin_add
class admin_create(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField(max_length=40)
    phone_number=models.CharField(max_length=100)  

    def __str__(self):
        return self.username   

#UserAdd        
class useradd(models.Model):
    names=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=100)
    profileimage=models.ImageField(upload_to='images', null=True,blank=True)
    password=models.CharField(max_length=100)
    confirmpass=models.CharField(max_length=100)
    selectgroup=models.CharField(max_length=100)

    def __str__(self):
        return self.names

#unit
class unitadd(models.Model):
    unit_name=models.CharField(max_length=50)
    unit_code=models.CharField(max_length=50)

    def __str__(self):
        return self.unit_name

#tax
class addtax(models.Model):
    tax_name=models.CharField(max_length=50)
    tax_rate=models.CharField(max_length=50)

    def __str__(self):
        return self.tax_name

#category
class add_category(models.Model):
    category_name=models.CharField(max_length=50)
    image_icon=models.ImageField(upload_to='category', null=True,blank=True)
    category_select=models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

#product add
class adding_product(models.Model):
    select_category=models.CharField(max_length=50)
    select_brand=models.CharField(max_length=50)
    select_unit=models.CharField(max_length=50)
    product_code=models.CharField(max_length=50)
    product_cost=models.CharField(max_length=50)
    product_sale_price=models.CharField(max_length=50)
    product_alert_quantity=models.CharField(max_length=50)
    product_image=models.ImageField(upload_to='product_images', null=True,blank=True)
    tax_type=models.CharField(max_length=50)
    product_name=models.CharField(max_length=50)
    product_description=models.CharField(max_length=500)


    def __str__(self):
        return self.product_code

#quotation_add
class quotation_add(models.Model):
    names=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100)
    product_list=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    product_quality=models.CharField(max_length=100)
    unit_price=models.CharField(max_length=100)
    sub_price=models.CharField(max_length=100)
    product_describtion=models.CharField(max_length=500)

    def __str__(self):
        return self.product_list


#purchase
class purchase_add(models.Model):
    warehouse=models.CharField(max_length=200)
    supplier=models.CharField(max_length=100)
    purchaselist=models.CharField(max_length=100)
    productname=models.CharField(max_length=100)
    quality=models.CharField(max_length=100)
    unitprice=models.CharField(max_length=100)
    subprice=models.CharField(max_length=100)
    shipping=models.CharField(max_length=100)
    discount=models.CharField(max_length=100)
    paidamount=models.CharField(max_length=100)
    image_file=models.ImageField(upload_to='purchase_image', null=True,blank=True)
    description=models.CharField(max_length=100)

    def __str__(self):
        return self.warehouse


#stock_transfer
class stock_transfer_adding(models.Model):
    fwarehouse=models.CharField(max_length=100)
    twarehouse=models.CharField(max_length=100)
    shipping=models.CharField(max_length=100)
    productlist=models.CharField(max_length=100)
    productname=models.CharField(max_length=100)
    quality=models.CharField(max_length=100)
    unitprice=models.CharField(max_length=100)
    subprice=models.CharField(max_length=100)
    image_file=models.ImageField(upload_to='staock_transfer_image', null=True,blank=True)
    description=models.CharField(max_length=100)

    def __str__(self):
        return self.fwarehouse

class add_sales(models.Model):
    product_name=models.CharField(max_length=100)
    invoice_number=models.CharField(max_length=100)
    total_price=models.CharField(max_length=100)
    quality=models.CharField(max_length=100)
    customer=models.CharField(max_length=100)
    created=models.CharField(max_length=100)

    def __str__(self):
        return self.product_name





    

    
