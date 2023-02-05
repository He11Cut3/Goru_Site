from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.shortcuts import render , get_object_or_404 , redirect
from .forms import CommentForm, AddQuantityForm
from .models import Order, Product, Comment, OrderItem
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator



class HomeView(ListView):
    model = Product
    template_name = "index.html"

class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs.get("slug")).select_related()



class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.product_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.product.get_absolute_url()


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about-us.html')


def login_user(request):
    return render(request, 'auth/login.html')

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    return render(request, 'cart.html')


@login_required(login_url=reverse_lazy('login'))
def add_item_to_cart(request, pk):
    if request.method == 'POST':
        quantity_form = AddQuantityForm(request.POST)
        if quantity_form.is_valid():
            quantity = quantity_form.cleaned_data['quantity']
            if quantity:
                cart = Order.get_cart(request.user)
                product = get_object_or_404(Product, pk=pk)
                cart.orderitem_set.create(product=product,
                                          quantity=quantity,
                                          price=product.price)
                cart.save()
                return redirect('cart')
        else:
            pass
    return redirect('index')

@login_required(login_url=reverse_lazy('login'))
def cart(request):
    cart = Order.get_cart(request.user)
    items = cart.orderitem_set.all()
    context = {
        'cart' : cart,
        'items' : items,
    }
    return render(request, 'cart.html', context)



@method_decorator(login_required, name='dispatch')
class CartDeleteItem(DeleteView):
    model = OrderItem
    template_name = 'cart.html'
    success_url = reverse_lazy('cart')

    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(order__user=self.request.user)
        return qs