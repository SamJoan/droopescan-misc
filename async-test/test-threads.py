from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

with ThreadPoolExecutor(max_workers=20) as executor:
    futures = []
    for a in range(1000):
        future = executor.submit(requests.get, 'http://crp.droope.org/?a')

    for future in as_completed(futures):
        future.result()
