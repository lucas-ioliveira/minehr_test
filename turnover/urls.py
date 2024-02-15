from django.urls import path
from turnover.views import TurnoverTotalView, TurnoverTotalCategoryView

urlpatterns = [
    path('line_chart/', TurnoverTotalView.as_view(), name='line_chart'),
    path('category_charts/', TurnoverTotalCategoryView.as_view(), name='category_charts'),
]