from django.urls import path

from exchange_rate.views import record_exchange_rate_to_excel, TokenCreateView

urlpatterns = [
    path("update/", record_exchange_rate_to_excel, name="update"),
    path("token/", TokenCreateView.as_view(), name="token"),
]

app_name = "exchange_rate"
