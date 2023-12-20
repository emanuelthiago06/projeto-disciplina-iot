from django.contrib import admin
from django.urls import path
from api.views import view_graph, add_point, initial_page


urlpatterns = [
    path("graph/", view_graph, name="plot_graph"),
    path("add-point/", add_point, name="add_point"),
    path('initial_page/', initial_page, name='initial_page'),
]
