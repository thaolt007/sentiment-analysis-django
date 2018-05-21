
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.views import generic
from .models import Product, Comment
from .forms import SearchForm
import sys
from operator import itemgetter
# connect db
# Create your views here.

def paging(product_list, page):
	paginator = Paginator(product_list, 24) # hien thi sp/trang
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		products = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		products = paginator.page(paginator.num_pages)
	return products

def index(request):
	# product_list = Product.objects.all()
	product_list = Product.objects.all().order_by('-product_vote_total')
	# categories = Product.objects.values_list('category', flat=True).distinct()
	page = request.GET.get('page')
	products = paging(product_list, page)

	for product in products:
		product.poss = Comment.objects.filter(sku=product.sku, prediction=1).count()
		product.negs = Comment.objects.filter(sku=product.sku, prediction=0).count()

	return render(request, 'lazada/index.html', {'products': products})#, 'categories': categories})

def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	comments = Comment.objects.filter(sku=product.sku)
	poss = Comment.objects.filter(sku=product.sku, prediction=1)
	negs = Comment.objects.filter(sku=product.sku, prediction=0)
	count_pos = poss.count()
	count_neg = negs.count()
	pos_percent = max( 0, int( count_pos / float(count_pos+count_neg) * 100 ) )
	return render(request, 'lazada/detail.html', {
		'product': product, 
		'comments': comments,
		'total_comments': comments.count(),
		'poss': poss,
		'negs': negs,
		'count_pos': count_pos,
		'count_neg': count_neg,
		'pos_percent' : pos_percent,
		})


def results(request):
	# if request.method == 'POST':
	text = request.GET.get('search')
	product_list = Product.objects.filter(name__contains=text)
	page = request.GET.get('page')
	products = paging(product_list, page)

	for product in products:
		product.poss = Comment.objects.filter(sku=product.sku, prediction=1).count()
		product.negs = Comment.objects.filter(sku=product.sku, prediction=0).count()

	total_pos = total_neg = 0
	for product in product_list:
		pos = Comment.objects.filter(sku=product.sku, prediction=1).count()
		neg = Comment.objects.filter(sku=product.sku, prediction=0).count()
		total_pos += pos
		total_neg += neg
	# products = Product.objects.all()[:8]
	# Fusionchart
	# Create an object for the column2d chart using the FusionCharts class constructor
	

	return render(request, 'lazada/results.html', {
		'text': text,
		'products': products,
		'total_pos': total_pos,
		'total_neg': total_neg
	})

def vendor(request, vendor):
	# print >> sys.stderr, 'Goodbye, cruel world!' + vendor
	# vendor = 'Samsung'
	product_list = Product.objects.filter(vendor__contains=vendor)
	page = request.GET.get('page')
	products = paging(product_list, page)

	
	for product in products:
		product.poss = Comment.objects.filter(sku=product.sku, prediction=1).count()
		product.negs = Comment.objects.filter(sku=product.sku, prediction=0).count()
		
	total_pos = total_neg = 0
	for product in product_list:
		pos = Comment.objects.filter(sku=product.sku, prediction=1).count()
		neg = Comment.objects.filter(sku=product.sku, prediction=0).count()
		total_pos += pos
		total_neg += neg


	return render(request, 'lazada/vendor.html', {
		'products': products,
		'vendor': vendor,
		'total_pos': total_pos,
		'total_neg': total_neg
		})

def brand(request, brand):
	product_list = Product.objects.filter(brand__contains=brand)
	page = request.GET.get('page')
	products = paging(product_list, page)

	
	for product in products:
		product.poss = Comment.objects.filter(sku=product.sku, prediction=1).count()
		product.negs = Comment.objects.filter(sku=product.sku, prediction=0).count()
		
	total_pos = total_neg = 0
	for product in product_list:
		pos = Comment.objects.filter(sku=product.sku, prediction=1).count()
		neg = Comment.objects.filter(sku=product.sku, prediction=0).count()
		total_pos += pos
		total_neg += neg


	return render(request, 'lazada/brand.html', {
		'products': products,
		'brand': brand,
		'total_pos': total_pos,
		'total_neg': total_neg
		})

def bxh_vendor(request):
	lists = Product.objects.values('vendor').distinct()
	for obj in lists:
		vendor = obj['vendor']
		products = Product.objects.filter(vendor__contains=vendor)
		total_pos = total_neg = 0
		for product in products:
			poss = Comment.objects.filter(sku=product.sku, prediction=1).count()
			negs = Comment.objects.filter(sku=product.sku, prediction=0).count()
			total_pos += poss
			total_neg += negs
		if (total_pos + total_neg > 30): obj['percent'] = int(total_pos / float(total_pos + total_neg) * 100)
		else: obj['percent'] = 0
		# obj['value'] = obj['percent'] * total_pos

	vendors = sorted(lists, key=itemgetter('percent'), reverse=True)[:20]
	# vendors = lists

	return render(request, 'lazada/bxh_vendor.html', {'vendors': vendors})

def bxh_product(request):
	products = Product.objects.filter(product_vote_total__gte=20)
	# print >> sys.stderr, 'Goodbye, cruel world!' + products
	lists = products.values('sku').distinct()
	for obj in lists:
		sku = obj['sku']
		product = Product.objects.filter(sku__contains=sku)[0]
		obj['name'] = product.name
		obj['id'] = product.id
		poss = Comment.objects.filter(sku=product.sku, prediction=1).count()
		negs = Comment.objects.filter(sku=product.sku, prediction=0).count()
		if (poss + negs > 20): obj['percent'] = int(poss / float(poss + negs) * 100)
		else: obj['percent'] = 0

	# products = products.order_by('-percent')[:30]
	products = sorted(lists, key=itemgetter('percent'), reverse=True)[:20]

	return render(request, 'lazada/bxh_product.html', {'products': products})