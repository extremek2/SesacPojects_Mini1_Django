from itertools import product

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from .models import SeasonalProducts, Products, Category, CartItem
from .forms import CartItemForm
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def products_index(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    seasonal_products = SeasonalProducts.objects.all()
    return render(request, 'products/foody2_product.html',
                  context={'products': products,
                           'seasonal_products': seasonal_products,
                           'categories': categories,

                           })

def category(request, slug):
    categories = Category.objects.all()
    # for category in categories:

    if slug == "no_category":
        products = Products.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        products = Products.objects.filter(category=category)
    return render(request,
                  template_name='products/foody2_product.html',
                  context={'products': products, 'categories': categories})


def detail(request, pk):
    product = Products.objects.get(pk=pk)
    categories = Category.objects.all()

    return render(request,
                  template_name='products/product_detail.html',
                  context={'product': product,
                           'categories': categories})

@csrf_exempt
def create_cart(request):


    cartform = CartItemForm()
    if request.method == "POST":
        import json
        data = json.loads(request.body.decode('utf-8'))
        product_id = data.get("product_id")
        product_name = data.get("product_name")
        product_quantity = data.get("quantity")
        print(request.user, product_id, product_name, product_quantity)


        cartform.user_id = request.user
        cartform.product_id = product_id

        if cartform.is_valid():
            cartform.save()
            print("DB 반영 완료")
        else:
            print("폼 에러")
        return redirect('/products/')
        # form = CartItemForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return JsonResponse({'message': '성공적으로 처리되었습니다.'})
        # else:
        #     # 폼 데이터 유효성 검사 실패
        #     return JsonResponse({'errors': form.errors}, status=400)

    # if request.method == "POST":
    #     try:
    #         data = json.loads(request.body.decode('utf-8'))
    #         return JsonResponse(data)
            # print(data)
            #
            # cartform.user = request.user
            # cartform.product = data.get("product")
            # cartform.quantity = data.get("quantity")
            #
            # if cartform.is_valid():
            #     cartform.save()
            #     return redirect('/products/')
        # except json.decoder.JSONDecodeError:
        #     return JsonResponse({'error': 'Invalid JSON'})
    else:
        return redirect('/products/')







# class OrderItemCreateView(CreateView):
#     model = OrderItem
#     fields = ['order', 'product', 'quantity'] # Specify the fields to be included in the form
#     template_name = 'your_app/orderitem_form.html' # Path to your template
#     success_url = reverse_lazy('order_detail') # URL to redirect after successful creation (e.g., order detail page)
#
#     # Optional: Override form_valid to handle additional logic, like setting the order
#     def form_valid(self, form):
#         # Example: If the Order is determined by the URL or session
#         # form.instance.order = Order.objects.get(pk=self.kwargs['order_pk'])
#         return super().form_valid(form)


# def manage_order_items(request, order_id):
#     order = Order.objects.get(pk=order_id)
#     OrderItemFormSet = modelformset_factory(OrderItem, fields=('product', 'quantity'))
#
#     # Filter OrderItems belonging to the specific order
#     formset = OrderItemFormSet(queryset=OrderItem.objects.filter(order=order))
