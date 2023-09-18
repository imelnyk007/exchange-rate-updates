import datetime
import os
import gspread
import requests
from dotenv import load_dotenv

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


load_dotenv()
URL = "https://bank.gov.ua/NBU_Exchange/exchange_site"
SHEET_ID = os.environ.get("SHEET_ID")


def format_date(date_str):
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.strftime("%Y%m%d")


def get_rate(update_to, update_from):
    formatted_from = format_date(update_from)
    formatted_to = format_date(update_to)

    response = requests.get(
        f"{URL}?start={formatted_from}&end={formatted_to}&valcode=usd&json"
    )
    data = response.json()
    rates = []

    for entry in data:
        rate_sell = entry["rate"]
        date_sell = entry["exchangedate"]
        rates.append([date_sell, rate_sell])

    return rates


@api_view(["GET"])
@authentication_classes([TokenAuthentication, ])
@permission_classes((IsAuthenticated,))
def record_exchange_rate_to_excel(request):
    current_date = datetime.datetime.today().strftime("%Y-%m-%d")
    update_from = request.GET.get("update_from", current_date)
    update_to = request.GET.get("update_to", current_date)

    gc = gspread.service_account(filename="credentials.json")
    sh = gc.open_by_key(SHEET_ID)
    worksheet = sh.worksheet("exchange_rate")

    rates = get_rate(update_to, update_from)

    for rate_data in rates:
        date_to_check = rate_data[0]
        existing_records = worksheet.findall(date_to_check)

        if existing_records:
            for record in existing_records:
                worksheet.delete_row(record.row)

    for rate_data in rates:
        next_empty_row = len(worksheet.col_values(1)) + 1
        cell_range = f"A{next_empty_row}:B{next_empty_row}"
        worksheet.update(cell_range, [rate_data])

    return Response({"message": "Data updated in Excel"})


class TokenCreateView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
