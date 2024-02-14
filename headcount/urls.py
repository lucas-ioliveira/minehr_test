from django.urls import path
from headcount.views import HeadcountTotalview, HeadcountTotalCategoryView
urlpatterns = [
    path('line_chart/', HeadcountTotalview.as_view(), name='line_chart'),
    path('category_charts/', HeadcountTotalCategoryView.as_view(), name='category_charts'),
]