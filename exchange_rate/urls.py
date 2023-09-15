from django.urls import path

from exchange_rate.views import record_exchange_rate_to_excel, UserCreateView, TokenCreateView

urlpatterns = [
    path("", record_exchange_rate_to_excel,  name="exchange_rate"),
    path("register/", UserCreateView.as_view(), name="create"),
    path('token/', TokenCreateView.as_view(), name="token"),
]

app_name = "exchange_rate"
