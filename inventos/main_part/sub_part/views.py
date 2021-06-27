from django.shortcuts import render,redirect
from django.contrib import messages
from . models import index_panal,useradd,admin_create,unitadd,addtax,add_category,adding_product,quotation_add,purchase_add,stock_transfer_adding,add_sales
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
import os
import easygui
from django.views.generic import ListView
from django.core.paginator import Paginator

multi_var_name = ''
#............Landing.............#

#index_panel
def index(request):
    return render(request,'index.html')
def index_main(request):
    if request.method=="POST":
        landing=index_panal(cand_name=request.POST['cand_name'],
        email=request.POST['email'],
        address=request.POST['address'],
        messages=request.POST['messages'],)
        landing.save()
        easygui.msgbox("massage sended successfully")
        return redirect(index)   
    return render(request,'index.html')   
    
#user_panel
def Signup(request):
    return render(request,'Signup.html')


#admin_panel    
def admin_index(request):
    if request.method=="POST":
        if admin_create.objects.filter(email=request.POST['email'],password=request.POST['password']).exists():
            fetching=admin_create.objects.get(email=request.POST['email'],password=request.POST['password'])
            global multi_var_name
            multi_var_name=fetching.username
            ut_data=admin_create.objects.get(username=multi_var_name)
            
            easygui.msgbox("successfully loggedin!!!")
            return redirect(dashboardindex)
        else:
            context={'msg':'incorrect username or password!'} 
            return render(request,'admin_index.html', context)  
    return render(request,'admin_index.html')
def register(request):
    if request.method=='POST':  
        creating=admin_create(username=request.POST['username'],
        password=request.POST['password'],
        email=request.POST['email'],
        phone_number=request.POST['phone_number'],)
        if admin_create.objects.filter(username=request.POST['username']).exists():
            messages.warning(request,'Warning!!! User Name Already Taken')
        elif admin_create.objects.filter(email=request.POST['email']).exists():
            messages.warning(request,'Warning!!! Email Already Taken') 
        elif admin_create.objects.filter(password=request.POST['password']).exists():
            messages.warning(request,'Warning!!! Password Already Taken')  
        else:  
            creating.save()
            subject = 'Welcome to Inventos'
            message = 'you are  successfully logged in the inventos ! Thank you for login'
            email_from = settings.EMAIL_HOST_USER
            recepient = request.POST.get('email')
            print("check:",recepient)
            send_mail(subject, message, email_from, [recepient], fail_silently = False)
            messages.success(request,'User Information Saved Successfully !!!')
            return redirect(admin_index)         
    return render(request,'register.html')  
#password_forget
def forgetpass(request):
    
    return render(request,'forgetpass.html') 

#......End_Landing_Function.....#

#dashboard

def dashboardindex(request):    
    ut_data=admin_create.objects.get(username=multi_var_name)
    return render(request,'dashboardindex.html',{'ut_data':ut_data})

#..........Category.............#

#listing_category
def categorylist(request):
    products=add_category.objects.all()
    context={'products':products}   
    return render(request,'categorylist.html', context)
#adding_category
def addcategory(request):
    if request.method=='POST':
        adding=add_category()
        adding.category_name=request.POST.get('names')
        if len(request.FILES) != 0:
             adding.image_icon=request.FILES['icon_file']
        adding.category_select=request.POST.get('selectcategory')
        adding.save()
        messages.success(request,'Saved The Information Successfully In DataTable!!!') 
        return redirect(categorylist)       
    return render(request,'categorylist.html')   
#editing_category
def edit_category(request,id):
    editting=add_category.objects.get(id=id)
    if request.method=='POST':
        if len(request.FILES) != 0:
            if len(editting.image_icon) > 0:
                 os.remove(editting.image_icon.path)
        editting.image_icon=request.FILES['icon_file']
        editting.category_name=request.POST.get('names')
        editting.category_select=request.POST.get('selectcategory')
        editting.save()  
        return redirect(categorylist)
    context={'editting':editting}
    return render(request,'edit_category.html', context) 
#deleteing_category
def delete_cate(request,id):
    deleting=add_category.objects.get(id=id)
    deleting.delete()
    return redirect(categorylist)    


#......End......#    


#........product_add..........#

#page
def productadd(request):
    return render(request,'productadd.html')
#adding_product
def adding_prod(request):
    if request.method=="POST":
        adding=adding_product()
        adding.select_category=request.POST.get('category_select') 
        adding.select_brand=request.POST.get('brand_name')
        adding.select_unit=request.POST.get('unit_value')
        adding.product_code=request.POST.get('code_gen')   
        adding.product_cost=request.POST.get('cost_of')
        adding.product_sale_price=request.POST.get('sale_price')
        adding.product_alert_quantity=request.POST.get('alert_quality')
        if len(request.FILES) != 0:
            adding.product_image=request.FILES['image_file']
        adding.tax_type=request.POST.get('tax_type')    
        adding.product_name=request.POST.get('product_name')
        adding.product_description=request.POST.get('description_blog')
        adding.save()
        messages.success(request,'Saved The Information Successfully in DataTable!')
        return redirect(productadd)    
    return render(request,'productlist.html')    
#listing_function
def productlist(request):
    products=adding_product.objects.all()
    context={'products': products}
    return render(request,'productlist.html', context)
#editing_fuction
def edit_product(request,id):
    editting=adding_product.objects.get(id=id)
    if request.method=='POST':
        if len(request.FILES) != 0:
            if len(editting.product_image) > 0:
                os.remove(editting.product_image.path)
        editting.product_image=request.FILES['image_file']        
        editting.select_category=request.POST.get('category_select') 
        editting.select_brand=request.POST.get('brand_name')
        editting.select_unit=request.POST.get('unit_value')
        editting.product_code=request.POST.get('code_gen')   
        editting.product_cost=request.POST.get('cost_of')
        editting.product_sale_price=request.POST.get('sale_price')
        editting.product_alert_quantity=request.POST.get('alert_quality')
        editting.tax_type=request.POST.get('tax_type')    
        editting.product_name=request.POST.get('product_name')
        editting.product_description=request.POST.get('description_blog')
        editting.save()     
        return redirect(productlist)  
    context={'editting':editting}
    return render(request,'edit_product.html', context)       
#deleting_function    
def delete_product(request,id):
    deleting=adding_product.objects.get(id=id)
    deleting.delete()
    return redirect(productlist) 

#.......End.......#       

#............purchase..............#

#purchase_page
def purchaseadd(request):
    return render(request,'purchaseadd.html')
#adding_purchase    
def adding_purchase(request):
    if request.method=='POST':
        adding=purchase_add()   
        adding.warehouse=request.POST.get('warehouse')
        adding.supplier=request.POST.get('supplier')
        adding.purchaselist=request.POST.get('purchaselist')
        adding.productname=request.POST.get('product_name')
        adding.quality=request.POST.get('quality_of')
        adding.unitprice=request.POST.get('unit_price')
        adding.subprice=request.POST.get('sub_price')
        adding.shipping=request.POST.get('shipping')
        adding.discount=request.POST.get('discount')
        adding.paidamount=request.POST.get('paidamount')
        adding.description=request.POST.get('description_blog')
        if len(request.FILES) != 0:
            adding.image_file=request.FILES['image_file']
        adding.save()
        messages.success(request,'Saved The Information Successfully In DataTable!')
        return redirect(purchaseadd)      
    return render(request,'purchaselist.html','dashboardindex.html','admin_index.html')     
#edit_purchase
def edit_purchase(request,id):
    editting=purchase_add.objects.get(id=id)
    if request.method=='POST':
        if len(request.FILES) != 0:
            if len(editting.image_file) > 0:
                os.remove(editting.image_file.path)
            editting.image_file=request.FILES['image_file'] 
            editting.warehouse=request.POST.get('warehouse')
            editting.supplier=request.POST.get('supplier')
            editting.purchaselist=request.POST.get('purchaselist')
            editting.productname=request.POST.get('product_name')
            editting.quality=request.POST.get('quality_of')
            editting.unitprice=request.POST.get('unit_price')
            editting.subprice=request.POST.get('sub_price')
            editting.shipping=request.POST.get('shipping')
            editting.discount=request.POST.get('discount')
            editting.paidamount=request.POST.get('paidamount')
            editting.description=request.POST.get('description_blog') 
        editting.save()
        return redirect(purchaselist)      
    context={'editting':editting}
    return render(request,'edit_purchase.html', context)    
#list_purchase        
def purchaselist(request):
    products=purchase_add.objects.all().order_by('id')
    paginator = Paginator(products,6) 
    page_number = request.GET.get('page',6)
    products = paginator.get_page(page_number)
    return render(request,'purchaselist.html', {'products':products})
#deleting_purchase
def delete_purchase(request,id):
    deleting=purchase_add.objects.get(id=id)
    deleting.delete()
    return redirect(purchaselist)

#.........End.......#


#........Quotation...........#

#page
def quotationsadd(request):
    return render(request,'quotationsadd.html')
#adding_quotation    
def quotation_adding(request):
    if request.method=='POST':
        quotation=quotation_add()
        quotation.names=request.POST.get('names') 
        quotation.phone_number=request.POST.get('phone_number')   
        quotation.product_list=request.POST.get('state_of')
        quotation.product_name=request.POST.get('product_name')
        quotation.product_quality=request.POST.get('quality_of')
        quotation.unit_price=request.POST.get('unit_price')
        quotation.sub_price=request.POST.get('sub_price')
        quotation.product_describtion=request.POST.get('description_blog')
        quotation.save()
        messages.success(request,'Saved The Information Successfully In DataTable!')
        return redirect(quotationsadd)     
    return render(request,'quotationsadd.htm')
#listing_quotation
def quotationlist(request):
    product=quotation_add.objects.all().order_by('id')
    paginator = Paginator(product,6) 
    page_number = request.GET.get('page',6)
    product = paginator.get_page(page_number)
    return render(request,'quotationlist.html', {'product':product})
#edit_quotation
def edit_quotation(request,id):
    editting=quotation_add.objects.get(id=id)
    if request.method=='POST':
        editting.names=request.POST.get('names') 
        editting.phone_number=request.POST.get('phone_number')   
        editting.product_list=request.POST.get('state_of')
        editting.product_name=request.POST.get('product_name')
        editting.product_quality=request.POST.get('quality_of')
        editting.unit_price=request.POST.get('unit_price')
        editting.sub_price=request.POST.get('sub_price')
        editting.product_describtion=request.POST.get('description_blog')
        editting.save()  
        return redirect(quotationlist)
    context={'editting':editting}
    return render(request,'edit_quotation.html', context)
#deleting_quotation
def delete_quotation(request,id):
    deleting=quotation_add.objects.get(id=id)
    deleting.delete()
    return redirect(quotationlist)

#........End..........#


#.......Stock........#

#page
def stock_tranfer_add(request):
    return render(request,'stock_tranfer_add.html')
#adding_stock
def stock_add(request):
    if request.method=='POST':
        adding=stock_transfer_adding()
        adding.fwarehouse=request.POST.get('fwarehouse')
        adding.twarehouse=request.POST.get('twarehouse')
        adding.shipping=request.POST.get('shipping')
        adding.productlist=request.POST.get('productlist')
        adding.productname=request.POST.get('product_name')
        adding.quality=request.POST.get('quality_of')
        adding.unitprice=request.POST.get('unit_price')
        adding.subprice=request.POST.get('sub_price')
        if len(request.FILES) != 0:
            adding.image_file=request.FILES['image_file']
        adding.save()
        messages.success(request,'Saved The Information Successfully In DataTable!')
        return redirect(stock_tranfer_add)  
    return render(request,'stock_transfer_list.html','dashboardindex.html')  
#edit_stock
def edit_stock(request,id):
    editting=stock_transfer_adding.objects.get(id=id)
    if request.method=='POST':
        if len(request.FILES) != 0:
            if len(editting.image_file) > 0:
                os.remove(editting.image_file.path) 
            editting.image_file=request.FILES['image_file']    
            editting.fwarehouse=request.POST.get('fwarehouse')
            editting.twarehouse=request.POST.get('twarehouse')
            editting.shipping=request.POST.get('shipping')
            editting.productlist=request.POST.get('productlist')
            editting.productname=request.POST.get('product_name')
            editting.quality=request.POST.get('quality_of')
            editting.unitprice=request.POST.get('unit_price')
            editting.subprice=request.POST.get('sub_price')  
        editting.save()
        return redirect(stock_transfer_list)
    context={'editting':editting}
    return render(request,'edit_stock.html', context)    
#listing_stock   
def stock_transfer_list(request):
    products=stock_transfer_adding.objects.all().order_by('id')
    paginator = Paginator(products,6) 
    page_number = request.GET.get('page',6)
    products = paginator.get_page(page_number)
    return render(request,'stock_transfer_list.html',{'products':products})
#deleting_stock
def delete_stock(request,id):
    deleting=stock_transfer_adding.objects.get(id=id)
    deleting.delete()
    return redirect(stock_transfer_list)  

#..........End.........#


#...........Tax........# 

#listing_tax
def taxlist(request):
    products=addtax.objects.all()
    context={'products':products}
    return render(request,'taxlist.html', context)
#edit_tax
def edit_tax(request,id):
    taxes=addtax.objects.get(id=id)
    context={'taxes':taxes}
    return render(request,'edit_tax.html',context) 
#update_function
def tax_update(request,id):
    update_tax=addtax(id=id)
    update_tax.tax_name=request.POST.get('tax_name')
    update_tax.tax_rate=request.POST.get('tax_rate')
    update_tax.save()
    return redirect(taxlist)   
#deleting_tax
def deletetax(request,id):
    deleting=addtax.objects.get(id=id)
    deleting.delete()
    return redirect(taxlist)     
#adding_tax
def tax_add(request):
    if request.method=="POST":
        add_tax=addtax(tax_name=request.POST['tax_name'],
        tax_rate=request.POST['tax_rate'])
        add_tax.save()
        messages.success(request,'Saved The Tax Information Successfully In DataTable!')
        return redirect(taxlist) 
    return render(request,'taxlist.html')


#........End.........#


#.......Unit........#

#listing_unit
def unitlist(request):
    products=unitadd.objects.all().order_by('id')
    paginator = Paginator(products,6) 
    page_number = request.GET.get('page',6)
    products = paginator.get_page(page_number)
    return render(request,'unitlist.html', {'products':products})
#adding_unit
def addunit(request):
    if request.method=="POST":
        adding_unit=unitadd(unit_name=request.POST['unit_name'],
        unit_code=request.POST['unit_code'])
        adding_unit.save()
        messages.success(request,'Saved The Unit Information Successfully In DatabaseTable!')
        return redirect(unitlist)   
    return render(request,'unitlist.html')    
#update_function
def updateunit(request,id):
    units=unitadd.objects.get(id=id)
    context={'units':units}
    return render(request,'updateunit.html', context)
#edit_unit
def unit_update(request,id):
    update_unit=unitadd(id=id)
    update_unit.unit_code=request.POST.get('unit_code')
    update_unit.unit_name=request.POST.get('unit_name')
    update_unit.save()
    return redirect(unitlist)
#deleting_unit
def deleteunit(request,id):
    deleting=unitadd.objects.get(id=id)
    deleting.delete()
    return redirect(unitlist)

#............End..........#

#.............Sales.......#

#page
def sales_add(request):
    return render(request,'sales_add.html')
#adding_sales
def adding_sales(request):
    if request.method=='POST':
        adding=add_sales()
        adding.product_name=request.POST.get('names')
        adding.invoice_number=request.POST.get('invoice_number')
        adding.total_price=request.POST.get('total_price')
        adding.quality=request.POST.get('total_quality')
        adding.customer=request.POST.get('customer')
        adding.created=request.POST.get('created')
        adding.save()
        messages.success(request,'Saved The Sales Product Information Successfully In DataTable!')
        return redirect(sales_add)    
    return render(request,'sales_list.html','return_product.html')    

#edit_sales
def edit_sales(request,id):
    editting=add_sales.objects.get(id=id) 
    if request.method=='POST':
        editting.product_name=request.POST.get('names')
        editting.invoice_number=request.POST.get('invoice_number')
        editting.total_price=request.POST.get('total_price')
        editting.quality=request.POST.get('total_quality')
        editting.customer=request.POST.get('customer')
        editting.created=request.POST.get('created')
        editting.save()
        return redirect(sales_list)
    context={'editting':editting}
    return render(request,'edit_sales.html',context)  
#deleting_sales
def delete_sales(request,id):
    deleting=add_sales.objects.get(id=id)
    deleting.delete()
    return redirect(sales_list)    
#listing_sales
def sales_list(request):
    products=add_sales.objects.all()
    context={'products':products}
    return render(request,'sales_list.html',context)


#........End.........#


#...........Return.........#

#Returning_Products    
def return_product(request):
    return render(request,'return_product.html')

#listing_products
def return_product(request):
    editting=add_sales.objects.all()
    context={'editting':editting}
    return render(request,'return_product.html',context)  

#.........End........#



#........UserManagement.......#

#page
def UserManagementAdd(request):
    return render(request,'UserManagementAdd.html')
#adding_user    
def added(request):
    if request.method=="POST":
        adding=useradd()
        adding.names=request.POST.get('names')
        adding.email=request.POST.get('user_email')
        adding.phone=request.POST.get('phone_number')
        if len(request.FILES) != 0:
            adding.profileimage = request.FILES['image_file']
        adding.password=request.POST.get('user_password')
        adding.confirmpass=request.POST.get('confirmpass')
        adding.selectgroup=request.POST.get('selectgroup')
        if adding.password == adding.confirmpass :
            adding.save()
            messages.success(request,'Profile Added In Table, Successfully !')
            return redirect(UserManagementAdd)         
        else:
            messages.warning(request,'Password not match with "Comfirm Password" !!')
            return redirect(UserManagementAdd)            
    return render(request,'UserManagementView.html','show.html')    
#edit_user
def edit_user(request,id):
    editting=useradd.objects.get(id=id)
    if request.method=='POST':
        if len(request.FILES) != 0:
            if len(editting.profileimage) > 0:
                os.remove(editting.profileimage.path)
            editting.profileimage = request.FILES['image_file']
            editting.names=request.POST.get('names')
            editting.email=request.POST.get('user_email')
            editting.phone=request.POST.get('phone_number')
            editting.password=request.POST.get('user_password') 
            editting.confirmpass=request.POST.get('confirmpass')
            editting.selectgroup=request.POST.get('selectgroup')
        editting.save()
        return redirect(UserManagementView)
    context={'editting':editting}
    return render(request,'edit_user.html', context)   
#show
def showing(request,id):
    items=useradd.objects.get(id=id)
    context={'items':items}
    return render(request,'show.html', context)
#listing_user
def UserManagementView(request):
    products=useradd.objects.all()
    context={'products': products}
    return render(request,'UserManagementView.html',context)
#delewting_user
def delete(request,id):
    deleting=useradd.objects.get(id=id)
    deleting.delete()
    return redirect(UserManagementView)   

#.......End........#


#LogOut
def logout(request):
    log(request)
    return render(request,'admin_index.html')      

#...............Blank Page................#

#Group
def group(request):
    return render(request,'group.html')   
#Customer
def customer(request):
    return render(request,'customer.html')
#Brand
def brand(request):
    return render(request,'brand.html')  
#POS
def pos(request):
    return render(request,'pos.html')  
#Sales list(POS)
def saleslistpos(request):
    return render(request,'saleslistpos.html')  
#Expenses
def expenses(request):
    return render(request,'expenses.html')  
#Stock Adjustment
def stockadjustment(request):
    return render(request,'stockadjustment.html') 
#Add Stock Adjustment
def addstockadjustment(request):
    return render(request,'addstockadjustment.html')  
#Report
def report(request):
    return render(request,'report.html')       

#....................End...........................#
