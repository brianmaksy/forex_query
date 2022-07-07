This programme specifies 16 currencies and returns all combinations of their exchange rates for a given date in the form of a csv named 'currency_data.csv'.

The csv is outputted under a folder named after the query date.

The currencies are:  
AUD  
CAD  
CHF  
DKK  
EUR  
GBP  
HKD  
IDR  
INR  
JPY  
MXN  
SEK  
SGD  
THB  
USD  
VND  

Packages required: pandas, tqdm

run

pip install pandas

and

pip install tqdm

in your Python environment if not already installed


To run the programme:

First add a utils.py file in the root directory specifying your API_KEY for https://exchangeratesapi.io/

Then run

python3 main.py

Sample output for querying four currencies (e.g. currencies = ["AUD", "CAD", "CHF", "DKK"]):
{your_system_path}>python3 main.py  
Query progress: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████| 12/12 [00:07<00:00,  1.52it/s]
