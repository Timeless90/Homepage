# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    addressid = models.IntegerField(db_column='AddressID')  # Field name made lowercase.
    addressline1 = models.CharField(db_column='AddressLine1', max_length=60)  # Field name made lowercase.
    addressline2 = models.CharField(db_column='AddressLine2', max_length=60, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30)  # Field name made lowercase.
    stateprovince = models.CharField(db_column='StateProvince', max_length=50)  # Field name made lowercase.
    countryregion = models.CharField(db_column='CountryRegion', max_length=50)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=15)  # Field name made lowercase.
    rowguid = models.CharField(max_length=36)
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Address'


class Customer(models.Model):
    customerid = models.IntegerField(db_column='CustomerID')  # Field name made lowercase.
    namestyle = models.BooleanField(db_column='NameStyle')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=8, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50)  # Field name made lowercase.
    suffix = models.CharField(db_column='Suffix', max_length=10, blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    salesperson = models.CharField(db_column='SalesPerson', max_length=256, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    passwordhash = models.CharField(db_column='PasswordHash', max_length=128)  # Field name made lowercase.
    passwordsalt = models.CharField(db_column='PasswordSalt', max_length=10)  # Field name made lowercase.
    rowguid = models.CharField(max_length=36)
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customer'


class Customeraddress(models.Model):
    customerid = models.IntegerField(db_column='CustomerID')  # Field name made lowercase.
    addressid = models.IntegerField(db_column='AddressID')  # Field name made lowercase.
    addresstype = models.CharField(db_column='AddressType', max_length=50)  # Field name made lowercase.
    rowguid = models.CharField(max_length=36)
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomerAddress'


class Product(models.Model):
    productid = models.IntegerField(db_column='ProductID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    productnumber = models.CharField(db_column='ProductNumber', max_length=25)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=15, blank=True, null=True)  # Field name made lowercase.
    standardcost = models.DecimalField(db_column='StandardCost', max_digits=19, decimal_places=4)  # Field name made lowercase.
    listprice = models.DecimalField(db_column='ListPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=5, blank=True, null=True)  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    productcategoryid = models.IntegerField(db_column='ProductCategoryID', blank=True, null=True)  # Field name made lowercase.
    productmodelid = models.IntegerField(db_column='ProductModelID', blank=True, null=True)  # Field name made lowercase.
    sellstartdate = models.DateTimeField(db_column='SellStartDate')  # Field name made lowercase.
    sellenddate = models.DateTimeField(db_column='SellEndDate', blank=True, null=True)  # Field name made lowercase.
    discontinueddate = models.DateTimeField(db_column='DiscontinuedDate', blank=True, null=True)  # Field name made lowercase.
    thumbnailphoto = models.BinaryField(db_column='ThumbNailPhoto', blank=True, null=True)  # Field name made lowercase.
    thumbnailphotofilename = models.CharField(db_column='ThumbnailPhotoFileName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rowguid = models.CharField(max_length=36)
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product'


class Productcategory(models.Model):
    productcategoryid = models.IntegerField(db_column='ProductCategoryID')  # Field name made lowercase.
    parentproductcategoryid = models.IntegerField(db_column='ParentProductCategoryID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    rowguid = models.CharField(max_length=36)
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductCategory'


class Productdescription(models.Model):
    productdescriptionid = models.IntegerField(db_column='ProductDescriptionID')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=400)  # Field name made lowercase.
    rowguid = models.CharField(max_length=36)
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductDescription'


class Productmodel(models.Model):
    productmodelid = models.IntegerField(db_column='ProductModelID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    catalogdescription = models.TextField(db_column='CatalogDescription', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rowguid = models.CharField(max_length=36)
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductModel'
# Unable to inspect table 'ProductModelDescription'
# The error was: Table ProductModelDescription does not exist.


class Salesorderdetail(models.Model):
    salesorderid = models.IntegerField(db_column='SalesOrderID')  # Field name made lowercase.
    salesorderdetailid = models.IntegerField(db_column='SalesOrderDetailID')  # Field name made lowercase.
    orderqty = models.SmallIntegerField(db_column='OrderQty')  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductID')  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    unitpricediscount = models.DecimalField(db_column='UnitPriceDiscount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    linetotal = models.DecimalField(db_column='LineTotal', max_digits=38, decimal_places=6)  # Field name made lowercase.
    rowguid = models.CharField(max_length=36)
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SalesOrderDetail'


class Salesorderheader(models.Model):
    salesorderid = models.IntegerField(db_column='SalesOrderID')  # Field name made lowercase.
    revisionnumber = models.SmallIntegerField(db_column='RevisionNumber')  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate')  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate')  # Field name made lowercase.
    shipdate = models.DateTimeField(db_column='ShipDate', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    onlineorderflag = models.BooleanField(db_column='OnlineOrderFlag')  # Field name made lowercase.
    salesordernumber = models.CharField(db_column='SalesOrderNumber', max_length=25)  # Field name made lowercase.
    purchaseordernumber = models.CharField(db_column='PurchaseOrderNumber', max_length=25, blank=True, null=True)  # Field name made lowercase.
    accountnumber = models.CharField(db_column='AccountNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID')  # Field name made lowercase.
    shiptoaddressid = models.IntegerField(db_column='ShipToAddressID', blank=True, null=True)  # Field name made lowercase.
    billtoaddressid = models.IntegerField(db_column='BillToAddressID', blank=True, null=True)  # Field name made lowercase.
    shipmethod = models.CharField(db_column='ShipMethod', max_length=50)  # Field name made lowercase.
    creditcardapprovalcode = models.CharField(db_column='CreditCardApprovalCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    taxamt = models.DecimalField(db_column='TaxAmt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    freight = models.DecimalField(db_column='Freight', max_digits=19, decimal_places=4)  # Field name made lowercase.
    totaldue = models.DecimalField(db_column='TotalDue', max_digits=19, decimal_places=4)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    rowguid = models.CharField(max_length=36)
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SalesOrderHeader'
