from django.urls import path
from .views import CampaignCalendarView, CampaignDetailView, CampaignPromoDetailView

urlpatterns = [
    path('', CampaignCalendarView.as_view(), name='campaign_calendar'),
    path('schedule/<int:pk>/', CampaignPromoDetailView.as_view(), name='schedule-detail'),
    path('<int:pk>/', CampaignDetailView.as_view(), name='campaign_detail'),
    
]

