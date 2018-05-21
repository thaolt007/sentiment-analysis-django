from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=200)
	price_final = models.IntegerField()
	discount = models.IntegerField()
	image_url = models.CharField(max_length=200)
	link_product = models.CharField(max_length=200)
	product_rating = models.IntegerField()
	product_vote_total = models.IntegerField()
	sku = models.CharField(max_length=20, unique=True)
	vendor = models.CharField(max_length=200)
	brand	 = models.CharField(max_length=200)
	category = models.CharField(max_length=200)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return smart_unicode(self.name,self.brand, self.category, self.vendor)


class Comment(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	sku = models.CharField(max_length=20)
	comment_rating = models.FloatField()
	detail = models.CharField(max_length=500)
	nickname = models.CharField(max_length=200)
	id_rating_review = models.IntegerField()
	fk_customer = models.IntegerField()
	created_at = models.DateTimeField()
	title = models.CharField(max_length=300)
	votes_up = models.IntegerField()
	votes_down = models.IntegerField()
	prediction = models.IntegerField()

	def __str__(self):
		return self.title

	def __unicode__(self):
		return smart_unicode(self.title, self.nickname)