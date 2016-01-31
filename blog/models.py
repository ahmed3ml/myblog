from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
	author_name = models.CharField(max_length=100)
	author_email = models.EmailField(unique=True)
	author_bio = models.TextField()

	def __str__(self):
		return self.author_name


class Category(models.Model):
	cat_name = models.CharField('category Name',max_length=150)
	cat_description = models.CharField('category Description',max_length=255)

	class Meta:
		verbose_name_plural =  'Categories'

	def __str__(self):
		return self.cat_name



class Tag(models.Model):
	tag_name = models.CharField(max_length=200)

	def __str__(self):
		return self.tag_name
		
		

class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
	author = models.ForeignKey(Author)
	categories = models.ManyToManyField(Category)
	tag = models.ManyToManyField(Tag)

	def __str__(self):
		return self.title

