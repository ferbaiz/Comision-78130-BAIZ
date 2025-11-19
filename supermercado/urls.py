from django.urls import path
from . import views

app_name = "supermercado"

urlpatterns = [

    # ======================
    # HOME
    # ======================
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),


    # ======================
    # BLOG / PÁGINAS
    # ======================
    path("pages/", views.PageListView.as_view(), name="pages"),
    path("pages/nueva/", views.PageCreateView.as_view(), name="page_create"),
    path("pages/<int:pk>/", views.PageDetailView.as_view(), name="page_detail"),
    path("pages/<int:pk>/editar/", views.PageUpdateView.as_view(), name="page_update"),
    path("pages/<int:pk>/eliminar/", views.PageDeleteView.as_view(), name="page_delete"),


    # ======================
    # PRODUCTOS (CRUD)
    # ======================
    path("productos/", views.ProductoListView.as_view(), name="productos"),
    path("productos/nuevo/", views.ProductoCreateView.as_view(), name="producto_create"),
    path("productos/<int:pk>/", views.ProductoDetailView.as_view(), name="producto_detail"),
    path("productos/<int:pk>/editar/", views.ProductoUpdateView.as_view(), name="producto_update"),
    path("productos/<int:pk>/eliminar/", views.ProductoDeleteView.as_view(), name="producto_delete"),


    # ======================
    # PROVEEDORES (CRUD)
    # ======================
    path("proveedores/", views.proveedores_list, name="proveedores_list"),
    path("proveedores/nuevo/", views.proveedor_create, name="proveedor_create"),
    path("proveedores/<int:pk>/", views.proveedor_detail, name="proveedor_detail"),
    path("proveedores/<int:pk>/editar/", views.proveedor_update, name="proveedor_update"),
    path("proveedores/<int:pk>/eliminar/", views.proveedor_delete, name="proveedor_delete"),


    # ======================
    # CLIENTES (CRUD)
    # ======================
    path("clientes/", views.clientes_list, name="clientes_list"),
    path("clientes/nuevo/", views.cliente_create, name="cliente_create"),
    path("clientes/<int:pk>/", views.cliente_detail, name="cliente_detail"),
    path("clientes/<int:pk>/editar/", views.cliente_update, name="cliente_update"),
    path("clientes/<int:pk>/eliminar/", views.cliente_delete, name="cliente_delete"),


    # ======================
    # CATEGORÍAS (CRUD)
    # ======================
    path("categorias/", views.CategoriaListView.as_view(), name="categorias_list"),
    path("categorias/nueva/", views.CategoriaCreateView.as_view(), name="categoria_create"),
    path("categorias/<int:pk>/editar/", views.CategoriaUpdateView.as_view(), name="categoria_update"),
    path("categorias/<int:pk>/eliminar/", views.CategoriaDeleteView.as_view(), name="categoria_delete"),


    # ======================
    # RUTA PROTEGIDA EJEMPLO
    # ======================
    path("protegida/", views.protected_example, name="protected_example"),

]
