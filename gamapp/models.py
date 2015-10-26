from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	tags = models.CharField(max_length=300)

class Book(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	tags = models.CharField(max_length=300,default="#books")
	
class Fashion(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	tags = models.CharField(max_length=300,default="#fashion")
	
class Travel(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	tags = models.CharField(max_length=300,default="#travel")
	
class Food(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	tags = models.CharField(max_length=300,default="#food")
	
class Technology(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	tags = models.CharField(max_length=300,default="#technology")

	
def publish(self):
	self.publish_date = timezone.now()
	self.save()

def __str__(self):
	return self.title