import requests, json, traceback
import itertools
import pandas as pd
from tqdm import tqdm
from utils import API_KEY # relative import syntax enabled by content in __init__.py

def get_currency_pair_rate(from_currency, to_currency):
  # For url: the date parameter is optional. Default is today.
  # The amount parameter is taken at random. It does not affect the rate returned fomr the response
  url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount=10"
  headers= {
    "apikey": API_KEY
  }
  try:
    response = requests.request("GET", url, headers=headers)
  except requests.exceptions.RequestException as e:
    with open ('errors.txt', 'a') as file:
      file.write(traceback.format_exc())

  result = json.loads(response.text)
  rate = result['info']['rate']

  return rate

def get_all_currency_data_list(currencies):
  pair_permutations_iterable = itertools.permutations(currencies, r=2)
  pair_permutations = list(pair_permutations_iterable)

  all_currency_pair_data = []
  for pair in tqdm(pair_permutations, desc="Query progress", total=len(pair_permutations)):
    from_currency, to_currency = pair
    rate = get_currency_pair_rate(from_currency, to_currency)
    pair_data = {"currency_from": from_currency, "currency_to": to_currency, "exchange_rate": rate}
    all_currency_pair_data.append(pair_data)

  return all_currency_pair_data

def generate_csv_from_list_via_pandas(all_currency_pair_data):
  df = pd.DataFrame(all_currency_pair_data)
  df.to_csv('currency_data.csv', encoding='utf-8', index=False)

# %%
currencies = ["AUD", "CAD", "CHF", "DKK", "EUR", "GBP", "HKD", "IDR", "INR", "JPY", "MXN", "SEK", "SGD", "THB", "VND", "USD"]
all_currency_pair_data = get_all_currency_data_list(currencies)
generate_csv_from_list_via_pandas(all_currency_pair_data)
