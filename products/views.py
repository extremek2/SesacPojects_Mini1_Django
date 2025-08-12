from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from .models import SeasonalProducts, Products, Category, Order, OrderItem
from .forms import OrderItemForm


def products_index(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    seasonal_products = SeasonalProducts.objects.all()
    return render(request, 'products/foody2_product.html',
                  context={'products': products,
                           'seasonal_products': seasonal_products,
                           'categories': categories
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

class OrderItemCreateView(CreateView):
    model = OrderItem
    fields = ['order', 'product', 'quantity'] # Specify the fields to be included in the form
    template_name = 'your_app/orderitem_form.html' # Path to your template
    success_url = reverse_lazy('order_detail') # URL to redirect after successful creation (e.g., order detail page)

    # Optional: Override form_valid to handle additional logic, like setting the order
    def form_valid(self, form):
        # Example: If the Order is determined by the URL or session
        # form.instance.order = Order.objects.get(pk=self.kwargs['order_pk'])
        return super().form_valid(form)


# def manage_order_items(request, order_id):
#     order = Order.objects.get(pk=order_id)
#     OrderItemFormSet = modelformset_factory(OrderItem, fields=('product', 'quantity'))
#
#     # Filter OrderItems belonging to the specific order
#     formset = OrderItemFormSet(queryset=OrderItem.objects.filter(order=order))
