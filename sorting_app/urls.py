from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard_view, name='index'),
    path('bubble', bubble_sort_view, name='bubble'),
    path('insertion', insertion_sort_view, name='insertion'),
    path('selection', selection_sort_view, name='selection'),
]