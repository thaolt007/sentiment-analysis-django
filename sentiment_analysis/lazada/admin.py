from django.contrib import admin

# Register your models here.
from .models import Product, Comment


class CommentInline(admin.StackedInline):
	model = Comment
	extra = 1

class ProductAdmin(admin.ModelAdmin):
	fieldsets = [
		('Product Infomation', {'fields': 
			['name', 'sku', 'price_final', 'discount', 'image_url', 'link_product', 
			'product_rating', 'product_vote_total', 'vendor', 'brand', 'category']
		})
	]
	# inlines = [CommentInline]
	list_display = ('name', 'sku', 'vendor', 'product_rating', 'category')
	list_filter = ['category']
	search_fields = ['name', 'sku']

class CommentAdmin(admin.ModelAdmin):
	fieldsets = [
		('Comment Infomation', {'fields': 
			['title', 'nickname', 'detail', 'comment_rating', 'votes_up', 'votes_down', 
			'id_rating_review', 'fk_customer', 'prediction', 'created_at']
		})
	]
	list_display = ('detail', 'nickname', 'id_rating_review', 'comment_rating', 'votes_up', 'votes_down', 'prediction', 'created_at')
	list_filter = ['created_at', 'prediction']
	search_fields = ['id_rating_review', 'nickname']

admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)