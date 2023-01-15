from django.urls import path
from pages.views import ExcelView

urlpatterns = [
    # path('', home, name='home'),
    path('', ExcelView.as_view(), name='home'),
    # path('download/<int:id>', download, name='download'),
]
