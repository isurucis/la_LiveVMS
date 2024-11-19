from django.urls import path
from .views import ShipmentCalendarView, ShipmentDetailView

urlpatterns = [
    path('', ShipmentCalendarView.as_view(), name='shipment_calendar'),
    path('<int:pk>/', ShipmentDetailView.as_view(), name='shipment_detail'),
]
