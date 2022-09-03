import time

from libs.openexchange import OpenExchangeClient

APP_ID = "8d20594f2b1f4562a66b0e9e0df22303"

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()
print(f"{usd_amount}USD is {gbp_amount:.2f}GBP")
print(f'{end - start}')

start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()
print(f"{usd_amount}USD is {gbp_amount:.2f}GBP")
print(f'{end - start}')

start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()
print(f"{usd_amount}USD is {gbp_amount:.2f}GBP")
print(f'{end - start}')

