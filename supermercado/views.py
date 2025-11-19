from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView
)

from .models import Page, Producto, Proveedor, Cliente, Categoria
from .forms import PageForm, ProductoForm, ProveedorForm, ClienteForm, CategoriaForm


# ===========================
# HOME y ABOUT
# ===========================

class HomeView(TemplateView):
    template_name = "supermercado/home.html"


class AboutView(TemplateView):
    template_name = "supermercado/about.html"


# ===========================
# BLOG / PÁGINAS
# ===========================

class PageListView(ListView):
    model = Page
    template_name = "supermercado/pages_list.html"
    context_object_name = "pages"
    paginate_by = 6

    def get_queryset(self):
        q = self.request.GET.get("q")
        qs = Page.objects.all().order_by("-publicado")
        if q:
            qs = qs.filter(titulo__icontains=q)
        return qs


class PageDetailView(DetailView):
    model = Page
    template_name = "supermercado/page_detail.html"
    context_object_name = "page"


class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = "supermercado/page_form.html"
    success_url = reverse_lazy("supermercado:pages")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = "supermercado/page_form.html"
    success_url = reverse_lazy("supermercado:pages")


class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = "supermercado/page_confirm_delete.html"
    success_url = reverse_lazy("supermercado:pages")


# ===========================
# PRODUCTOS
# ===========================

class ProductoListView(ListView):
    model = Producto
    template_name = "supermercado/productos_list.html"
    context_object_name = "productos"


class ProductoDetailView(DetailView):
    model = Producto
    template_name = "supermercado/producto_detail.html"
    context_object_name = "producto"


class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "supermercado/producto_form.html"
    success_url = reverse_lazy("supermercado:productos")


class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "supermercado/producto_form.html"
    success_url = reverse_lazy("supermercado:productos")


class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = "supermercado/producto_confirm_delete.html"
    success_url = reverse_lazy("supermercado:productos")


# ===========================
# PROVEEDORES (FBV)
# ===========================

@login_required
def proveedores_list(request):
    proveedores = Proveedor.objects.all()
    return render(request, "supermercado/proveedores_list.html", {"proveedores": proveedores})


@login_required
def proveedor_detail(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, "supermercado/proveedor_detail.html", {"proveedor": proveedor})


@login_required
def proveedor_create(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("supermercado:proveedores_list")
    else:
        form = ProveedorForm()
    return render(request, "supermercado/proveedor_form.html", {"form": form})


@login_required
def proveedor_update(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)

    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect("supermercado:proveedor_detail", pk=pk)
    else:
        form = ProveedorForm(instance=proveedor)

    return render(
        request,
        "supermercado/proveedor_form.html",
        {"form": form, "proveedor": proveedor}
    )


@login_required
def proveedor_delete(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)

    if request.method == "POST":
        proveedor.delete()
        return redirect("supermercado:proveedores_list")

    return render(
        request,
        "supermercado/proveedor_confirm_delete.html",
        {"proveedor": proveedor}
    )


# ===========================
# CLIENTES (FBV)
# ===========================

@login_required
def clientes_list(request):
    clientes = Cliente.objects.all()
    return render(request, "supermercado/clientes_list.html", {"clientes": clientes})


@login_required
def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, "supermercado/cliente_detail.html", {"cliente": cliente})


@login_required
def cliente_create(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("supermercado:clientes_list")
    else:
        form = ClienteForm()

    return render(request, "supermercado/cliente_form.html", {"form": form})


@login_required
def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("supermercado:cliente_detail", pk=pk)
    else:
        form = ClienteForm(instance=cliente)

    return render(
        request,
        "supermercado/cliente_form.html",
        {"form": form, "cliente": cliente}
    )


@login_required
def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == "POST__":
        cliente.delete()
        return redirect("supermercado:clientes_list")

    return render(
        request,
        "supermercado/cliente_confirm_delete.html",
        {"cliente": cliente}
    )


# ===========================
# CATEGORÍAS (CRUD – SOLO LOGIN)
# ===========================

class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = "supermercado/categorias_list.html"  # ← CORREGIDO
    context_object_name = "categorias"


class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "supermercado/categoria_form.html"
    success_url = reverse_lazy("supermercado:categorias_list")


class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "supermercado/categoria_form.html"
    success_url = reverse_lazy("supermercado:categorias_list")


class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = "supermercado/categoria_confirm_delete.html"
    success_url = reverse_lazy("supermercado:categorias_list")


# ===========================
# RUTA PROTEGIDA DEMO
# ===========================

@login_required
def protected_example(request):
    return render(request, "supermercado/protected.html")
