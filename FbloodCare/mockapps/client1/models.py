from django.db import models

# Create your models here.
class requestmodel(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    def __str__(self):
    	return self.city

class post_requestmodel(models.Model):
	username = models.CharField(max_length=100)
	blood_group = models.CharField(max_length=100)
	Age = models.IntegerField()
	phone_number = models.CharField(max_length=20)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	def __str__(self):
		return self.username

class getbyidrequestmodel(models.Model):
    username = models.CharField(max_length=100)
    def __str__(self):
    	return self.username