from loguru import logger

from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, CreateView, ListView, DeleteView

from products.forms import ProductCreateForm, ProductFilter, ProductUpdateForm
from products.models import Product


class ProductCreate(CreateView):
    models = Product
    success_url = reverse_lazy('products:list')
    template_name = 'products/create.html'
    form_class = ProductCreateForm


class ProductList(ListView):
    model = Product
    template_name = 'products/list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['obj_filter'] = ProductFilter(data=self.request.GET, queryset=self.model.objects.all())
        return context


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductUpdateForm
    success_url = reverse_lazy('products:list')
    template_name = 'products/update.html'


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products:list')
    template_name = 'products/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.get_object()
        return context

    def delete(self, request, *args, **kwargs):
        """
        on deletion removes the old image from images
        """

        self.object = self.get_object()
        success_url = self.get_success_url()
        if self.object.logo != 'default.png':
            self.object.logo = ''
        self.object.delete()
        logger.info(f'Product {self.object.uuid} deleted')
        return HttpResponseRedirect(success_url)



