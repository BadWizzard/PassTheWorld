from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Value, F, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Cart, CartItem, Product, Customer, Collection, Order, OrderItem

def say_hello(request):
    #this is controller
    x = 1
    y = 2

    try:
        products = Product.objects.all().get()
    except ObjectDoesNotExist:
        pass

    for product in products:
        print(product)
    return render(request, 'hello.html', {'name': 'Valerii'})

def show_customers(request):
    customers = Customer.objects.filter(email__endswith='.com')
    return render(request, 'hello.html', {'name': 'Valerii', 'customers': list(customers)})

def show_collections_with_no_products(request):
    collections = Collection.objects.filter(featured_product_id__isnull=True)
    return render(request, 'hello.html', {'name': 'Valerii', 'collections': list(collections)})

def products_without_order(request):
    # id_in={query_set}
    # prefetch_related 1 to many

    # select_related one to one
    # Product.objects.select_related('order').all()
    products = Product.objects.filter(orderitem__id__isnull=False).order_by('-title')
    return render(request, 'hello.html', {'name': 'Valerii', 'products': list(products)})

def get_aggregates(request):
    order_count = Order.objects.aggregate(count=Count('id'))
    sold_products_count = OrderItem.objects.filter(product_id=1).aggregate(units_sold=Sum('quantity'))
    customer_orders_count = Order.objects.filter(customer_id=1).aggregate(count=Count('id'))
    products_in_collection = Product.objects.filter(collection_id=3).aggregate(count=Count('id'), min_price=Min('unit_price'), max_price=Max('unit_price'), average_price=Avg('unit_price'))
    return render(request, 'hello.html', {
        'name': 'Valerii',
        'order_count': order_count,
        'sold_products_count': sold_products_count,
        'customer_orders_count': customer_orders_count,
        'products_in_collection': products_in_collection,
        })

def get_expressions(request):
    customer_expenses_expression = ExpressionWrapper(F('order__orderitem__unit_price') * F('order__orderitem__quantity'), output_field=DecimalField())
    customer_orders = Customer.objects.annotate(last_order_id=Max('order__id'), expenses=Sum(customer_expenses_expression))

    collection_products_counts = Collection.objects.annotate(products_count=Count('product__id'))

    customers_5_more_orders = Customer.objects.annotate(order_count=Count('order')).filter(order_count__gt=5)

    total_sales_expression = ExpressionWrapper(F('orderitem__unit_price') * F('orderitem__quantity'), output_field=DecimalField())
    top_5_bestsellers = Product.objects.annotate(sell_count=Sum('orderitem__quantity'), total_sales=Sum(total_sales_expression)).order_by('-sell_count')[:5]

    return render(request, 'hello.html', {
        'name': 'Valerii',
        'customer_orders': customer_orders,
        'collection_products_counts': collection_products_counts,
        'customers_5_more_orders': customers_5_more_orders,
        'top_5_bestsellers': top_5_bestsellers,
        })

def create_objects(request):

    shopping_cart = Cart()
    shopping_cart.save()

    cart_item = CartItem()
    cart_item.quantity = 1
    cart_item.cart = shopping_cart
    cart_item.product = Product(pk=1)
    cart_item.save()

    cart_item.quantity = 5
    cart_item.save()

    shopping_cart.delete()

    return render(request, 'hello.html', {
        'name': 'Valerii',
        })