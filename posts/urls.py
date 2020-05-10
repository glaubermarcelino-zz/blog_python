from django.urls import path
from .views import *

app_name = "posts"

urlpatterns = [
    path("", ListarPosts.as_view(), name="index"),
    path("Adicionar/", AdicionarPost.as_view(), name="add_post"),
    path("Adicionar/drafts/", PostDraftsList.as_view(), name="list_drafts"),
    path("buscar/", BuscarPosts.as_view(), name="search"),
    # post archives
    path("<int:year>/", PostYearArchive.as_view(), name="y_archive"),
    path(
        "<int:year>/<int:month>/",
        PostYearMonthArchive.as_view(month_format="%m"),
        name="ym_archive",
    ),
    path("tag/<str:tag>/", ListarPorTag.as_view(), name="tag"),
    path("categoria/<str:name>/", ListarPorCategoria.as_view(), name="Categoria"),
    path("autor/<str:autor>/", ListarPorAutor.as_view(), name="author"),
    path("<slug:slug>/", DetailsPost.as_view(), name="details_post"),
    path("<slug:slug>/delete/", DeletarPost.as_view(), name="delete_post"),
    path("<slug:slug>/update/", AtualizarPost.as_view(), name="update_post"),
]
