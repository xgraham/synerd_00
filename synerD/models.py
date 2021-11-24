from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=125, unique=True)
    middlename = models.CharField(max_length=125,default=None, blank=True, null=True)
    firstname= models.CharField(max_length=125,default='None', blank=True, null=True)
    lastname = models.CharField(max_length=125,default='None', blank=True, null=True)
    email = models.CharField(max_length=125,default=None, blank=True, null=True)
    address1 = models.CharField(max_length=125,default=None, blank=True, null=True)
    address2 = models.CharField(max_length=125,default=None, blank=True, null=True)
    city = models.CharField(max_length=125,default=None, blank=True, null=True)
    state  = models.CharField(max_length=125,default=None, blank=True, null=True)
    zipcode  = models.CharField(max_length=125,default=None, blank=True, null=True)
    employername  = models.CharField(max_length=125,default=None, blank=True, null=True)
    staff = models.BooleanField(default=False)
    password = 1


class SubscriptionType(models.Model):
    subscriptiontypename = models.CharField(max_length=125)

class Service(models.Model):
    servicename = models.CharField(max_length=125)
    description = models.CharField(max_length=125)
    premium = models.CharField(max_length=125,default=None, blank=True, null=True)
    allocation = models.CharField(max_length=125,default=None, blank=True, null=True)


class Subscriber(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    subscriptiontypecode = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)
    servicecode = models.ForeignKey(Service, on_delete=models.CASCADE)
    startdate = models.DateField()

class TransferredSubscription(models.Model):
    transferfrom = models.CharField(max_length=125)
    transferto = models.CharField(max_length=125)
    requestdate = models.DateField(default=None, blank=True, null=True)
    transferdate= models.DateField(default=None, blank=True, null=True)
    subscriberid = models.ForeignKey(Subscriber, on_delete=models.CASCADE)


class Office(models.Model):
    id = models.AutoField(primary_key=True)
    officename = models.CharField(max_length=125)
    attribution = models.CharField(max_length=125)

class Officer(models.Model):
    id = models.AutoField(primary_key=True)
    officecode = models.ForeignKey(Office, on_delete=models.CASCADE)
    subscriberid = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    startdate = models.DateField()
    enddate = models.DateField()

class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    organizationname = models.CharField(max_length=125)
    description = models.CharField(max_length=125)
    datejoined = models.DateField(default=None, blank=True, null=True)
    address1 = models.CharField(max_length=125)
    address2 = models.CharField(max_length=125,default=None, blank=True, null=True)
    city = models.CharField(max_length=125,default=None, blank=True, null=True)
    state = models.CharField(max_length=125,default=None, blank=True, null=True)
    zipcode = models.CharField(max_length=125,default=None, blank=True, null=True)
    phonenumber = models.CharField(max_length=125,default=None, blank=True, null=True)


class OrganizationMember(models.Model):
    id = models.AutoField(primary_key=True)
    organizationcode = models.ForeignKey(Organization, on_delete=models.CASCADE)
    subscriberid = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    startdate = models.DateField()
    enddate = models.DateField(default=None, blank=True, null=True)
    nativecountry = models.CharField(max_length=125,default=None, blank=True, null=True)
    citizenship = models.CharField(max_length=125,default=None, blank=True, null=True)
    isdelegate = models.BooleanField()

