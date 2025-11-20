from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *


# Create your views here.
def index(request):
    return render(request, 'shop/index.html')


def product_list(request, category_slug=None):
    products = Product.objects.select_related('category').all()

    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    #search logic

    manufacturer_filter = request.GET.get('manufacturer')
    memory_filter = request.GET.get('memory')
    resolution_filter = request.GET.get('resolution')
    pcie_filter = request.GET.get('pcie')

    # فیلتر بر اساس سازنده
    if manufacturer_filter:
        # فیلتر کردن بر اساس سازنده که در مدل ProductFeature قرار دارد
        products = products.filter(features__manufacturer=manufacturer_filter)
        # 💡 features__manufacturer: از related_name='features' برای دسترسی به فیلد manufacturer استفاده شده است

    # فیلتر بر اساس رم
    if memory_filter:
        try:
            # رم (memory) یک PositiveIntegerField است
            memory_filter = int(memory_filter)
            products = products.filter(features__memory=memory_filter)
        except:
            ValueError('مقدار معتبری وارد کنید.')

    if resolution_filter:
        products = products.filter(features__suggested_resolution=resolution_filter)

    if pcie_filter:
        products.filter(features__interface=pcie_filter)
    # ----------------------------------------------------

    # 4. آماده‌سازی Context برای فرم جستجو در HTML

    # الف) لیست سازنده‌ها (از فیلد choices مدل ProductFeature می‌آید)
    manufacturer_choices = ProductFeature.MANUFACTURER
    resolution_choices = ProductFeature.SUGGESTED_RESOLUTION
    interface_choices = ProductFeature.PCIE_INTERFACES
    available_memory = ProductFeature.objects.values_list('memory', flat=True).distinct().order_by('memory')

    paginator = Paginator(products,1)
    page_number = request.GET.get('page', 1)
    try:
        products = paginator.page(page_number)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        products = paginator.page(1)
    context = {
        'category': category,
        'products': products,
        'available_memory': available_memory,
        'selected_memory': memory_filter,
        'manufacturer_choices': manufacturer_choices,
        'selected_manufacturer': manufacturer_filter,
        'resolution_choices': resolution_choices,
        'selected_resolution':resolution_filter,
        'interface_choices': interface_choices,
        'selected_interface': pcie_filter

    }

    return render(request, 'shop/list.html', context)
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    context = {'product': product}
    return render(request, 'shop/detail.html', context)


from django.shortcuts import render, get_object_or_404
from .models import Product, Category, ProductFeature  # 💡 ProductFeature را ایمپورت کنید


