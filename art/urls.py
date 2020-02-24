from django.urls import path
from . import views

urlpatterns = [
    path('<str:model_name>/page-<int:page_num>/item-<int:item_per_page>', views.get_instances, name='get_instances'),
    path('<str:model_name>/<slug:slug>', views.get_one_instance, name='get_one_instance'),
]