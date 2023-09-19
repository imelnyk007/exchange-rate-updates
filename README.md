# Exchange rate API Service

The Exchange Rate API Service is an API for recording the exchange rate of USD in Google Sheets from the Monobank API. 
To make a request, you need to authenticate with a token.

## Check it out
[Exchange rate API Service deployed to Pythonanywhere](https://irynamelnyk.pythonanywhere.com)

To access the service on PythonAnywhere, use the following credentials:
```
username: admin
password: 123
```

There ara two endpoints:
1. https://irynamelnyk.pythonanywhere.com/api/token/ -  for creating an authentication token (you can use the Chrome extension "ModHeader" to send requests with a token).
2. https://irynamelnyk.pythonanywhere.com/api/update/ -  for recording and updating exchange rates. 
To specify a date range, you can use the "update_from" and "update_to" parameters (the default is today).
For example, https://irynamelnyk.pythonanywhere.com/api/update/?update_from=2023-01-01&updates_to=2023-01-02 - to record exchange rates from 2023-01-01 to 2023-01-02. 
If the operation is successful, you will receive the message "Data updated in Excel"


## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/imelnyk007/exchange-rate-updates.git
```
2. Navigate to the project directory:
```bash
cd exchange-rate-updates
```
3. Create an .env file and define the environment variables using .env.sample.
4. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
```
5. Install requirements:
```bash
pip install -r requirements.txt
```
6. Perform the migration:
```bash
python manage.py migrate
```
7. Create a superuser:
```bash
python manage.py createsuperuser
```
8. Start the server:
```bash
python manage.py runserver
```