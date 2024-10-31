from django.urls import path
from .views import CampaignCalendarView, CampaignDetailView

urlpatterns = [
    path('', CampaignCalendarView.as_view(), name='campaign_calendar'),
    path('<int:pk>/', CampaignDetailView.as_view(), name='campaign_detail'),
]
