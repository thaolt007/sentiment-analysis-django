
from django.conf.urls import url
from . import views

app_name = 'lazada'

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^product/(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^results/', views.results, name='results'),

    # url(r'^vendor/(?P<vendor>[-\w\s]+)/$', views.vendor, name='vendor'),
    
    url(r'^vendor/(?P<vendor>.*)/$', views.vendor, name='vendor'),

    url(r'^brand/(?P<brand>.*)/$', views.brand, name='brand'),

    url(r'^bxh/vendor', views.bxh_vendor, name='bxh_vendor'),

    url(r'^bxh/product', views.bxh_product, name='bxh_product'),

]