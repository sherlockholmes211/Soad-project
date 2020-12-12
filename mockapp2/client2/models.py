from django.db import models

# Create your models here.
class requestmodel(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    blood_group=models.CharField(max_length=100)
    def __str__(self):
    	return self.city

class post_requestmodel(models.Model):
	Customer = models.CharField(max_length=100)
	Blood_Bank = models.CharField(max_length=100)
	blood_type = models.CharField(max_length=100)
	quantity = models.IntegerField()
	def __str__(self):
		return self.Customer

class getbyidrequestmodel(models.Model):
    username = models.CharField(max_length=100)
    def __str__(self):
    	return self.username