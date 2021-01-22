from django.urls import path, include
from leads.views import lead_detail, lead_list,lead_create

app_name = "leads"

urlpatterns = [
path('', lead_list),
path('<int:pk>/', lead_detail),
path('create/', lead_create),
]