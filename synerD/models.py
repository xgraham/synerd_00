from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=125, unique=True)
    middlename = models.CharField(max_length=125)
    firstname= models.CharField(max_length=125)
    lastname = models.CharField(max_length=125)
    email = models.CharField(max_length=125)
    address1 = models.CharField(max_length=125)
    address2 = models.CharField(max_length=125)
    city = models.CharField(max_length=125)
    state  = models.CharField(max_length=125)
    zipcode  = models.CharField(max_length=125)
    employername  = models.CharField(max_length=125)


class SubscriptionType(models.Model):
    subscriptiontypename = models.CharField(max_length=125)

class Service(models.Model):
    servicename = models.CharField(max_length=125)
    description = models.CharField(max_length=125)
    premium = models.CharField(max_length=125)
    allocation = models.CharField(max_length=125)


class Subscriber(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    subscriptiontypecode = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)
    servicecode = models.ForeignKey(Service, on_delete=models.CASCADE)


class TransferredSubscription(models.Model):
    transferfrom = models.CharField(max_length=125)
    transferto = models.CharField(max_length=125)
    requestdate = models.DateField()
    transferdate= models.DateField()
    subscriberid = models.ForeignKey(Subscriber, on_delete=models.CASCADE)


class Office(models.Model):
    officename = models.CharField(max_length=125)
    attribution = models.CharField(max_length=125)

class Officer(models.Model):
    officecode = models.ForeignKey(Office, on_delete=models.CASCADE)
    subscriberid = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    startdate = models.DateField()
    enddate = models.DateField()

class Organization(models.Model):
    organizationname = models.CharField(max_length=125)
    description = models.CharField(max_length=125)
    datejoined = models.DateField()
    address1 = models.CharField(max_length=125)
    address2 = models.CharField(max_length=125)
    city = models.CharField(max_length=125)
    state = models.CharField(max_length=125)
    zipcode = models.CharField(max_length=125)
    phonenumber = models.CharField(max_length=125)


class OrganizationMember(models.Model):
    organizationcode = models.ForeignKey(Organization, on_delete=models.CASCADE)
    subscriberid = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    startdate = models.DateField()
    enddate = models.DateField()
    nativecountry = models.CharField(max_length=125)
    citizenship = models.CharField(max_length=125)
    isdelegate = models.BooleanField()

