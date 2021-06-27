from django.urls import path
from . import views


urlpatterns = [
    #landing
    path('',views.index,name='index'),
    path('index_main',views.index_main,name='index_main'),
    #signup_for_users
    path('Signup',views.Signup,name='Signup'),
    #admin
    path('admin_index',views.admin_index,name='admin_index'),
    #admin_reg
    path('register',views.register,name='register'),
    #forgot_password
    path('forgetpass',views.forgetpass,name='forgetpass'),
    #category
    path('categorylist',views.categorylist,name='categorylist'),
    path('edit_category/<int:id>',views.edit_category,name='edit_category'),
    path('delete_cate/<int:id>',views.delete_cate,name="delete_cate"),
    #add_category
    path('addcategory',views.addcategory,name='addcategory'),
    #admin_dashboard
    path('dashboardindex',views.dashboardindex,name='dashboardindex'),
    #product_adding
    path('productadd',views.productadd,name='productadd'),
    path('adding_prod',views.adding_prod,name='adding_prod'),
    path('productlist',views.productlist,name='productlist'),
    path('edit_product/<int:id>',views.edit_product,name='edit_product'),
    path('delete_product/<int:id>',views.delete_product,name="delete_product"),
    #purchaseing
    path('purchaseadd',views.purchaseadd,name='purchaseadd'),
    path('adding_purchase',views.adding_purchase,name='adding_purchase'),
    path('edit_purchase/<int:id>',views.edit_purchase,name='edit_purchase'),
    path('purchaselist',views.purchaselist,name='purchaselist'),
    path('delete_purchase/<int:id>',views.delete_purchase,name='delete_purchase'),
    #quotation
    path('quotationsadd',views.quotationsadd,name='quotationsadd'),
    path('quotation_adding',views.quotation_adding,name='quotation_adding'),
    path('edit_quotation/<int:id>',views.edit_quotation,name='edit_quotation'),
    path('quotationlist',views.quotationlist,name='quotationlist'),
    path('delete_quotation/<int:id>',views.delete_quotation,name='delete_quotation'),
    #return
    path('return_product',views.return_product,name='return_product'),
    #sales
    path('sales_list',views.sales_list,name='sales_list'),
    path('sales_add',views.sales_add,name='sales_add'),
    path('adding_sales',views.adding_sales,name='adding_sales'),
    path('edit_sales/<int:id>',views.edit_sales,name='edit_sales'),
    path('delete_sales/<int:id>',views.delete_sales,name='delete_sales'),
    path('return_product',views.return_product,name='return_product'),
    #stock
    path('stock_tranfer_add',views.stock_tranfer_add,name='stock_tranfer_add'),
    path('stock_add',views.stock_add,name='stock_add'),
    path('stock_transfer_list',views.stock_transfer_list,name='stock_transfer_list'),
    path('edit_stock/<int:id>',views.edit_stock,name='edit_stock'),
    path('delete_stock/<int:id>',views.delete_stock,name='delete_stock'),
    #tax
    path('taxlist',views.taxlist,name='taxlist'),
    #tax_add
    path('tax_add',views.tax_add,name='tax_add'),
    path('edit_tax/<int:id>',views.edit_tax,name='edit_tax'),
    path('tax_update/<int:id>',views.tax_update,name='tax_update'),
    path('deletetax/<int:id>',views.deletetax,name='deletetax'),
    #unit
    path('unitlist',views.unitlist,name='unitlist'),
    #unit_add
    path('addunit',views.addunit,name='addunit'),
    path('updateunit/<int:id>',views.updateunit,name='updateunit'),
    path('unit_update/<int:id>',views.unit_update,name='unit_update'),
    path('deleteunit/<int:id>',views.deleteunit,name='deleteunit'),
    #create_user
    path('UserManagementAdd',views.UserManagementAdd,name='UserManagementAdd'),
    path('added',views.added,name="added"),
    path('edit_user/<int:id>',views.edit_user,name='edit_user'),
    # path('user_update/<int:id>',views.user_update,name='user_update'),
    path('delete/<int:id>',views.delete,name='delete'),
    #view_user
    path('UserManagementView',views.UserManagementView,name='UserManagementView'),
    path('showing/<int:id>',views.showing,name="showing"),

    #logout
    path('logout',views.logout,name='logout'),

    #........Dummy.........#

    #Group
    path('group',views.group,name='group'),
    #Brand
    path('brand',views.brand,name='brand'),
    #Customer
    path('customer',views.customer,name='customer'),
    #POS
    path('pos',views.pos,name='pos'),
    #Sales list(POS)
    path('saleslistpos',views.saleslistpos,name='saleslistpos'),
    #Expenses
    path('expenses',views.expenses,name='expenses'),
    #Stock Adjustment
    path('stockadjustment',views.stockadjustment,name='stockadjustment'),
    #Add Stock Adjustment
    path('addstockadjustment',views.addstockadjustment,name='addstockadjustment'),
    #Report
    path('report',views.report,name='report'),

]
