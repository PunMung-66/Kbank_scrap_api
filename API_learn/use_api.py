import httpx

# Access the endpoint with parameters (e.g., sum of 3 and 5)
sum_url = "http://127.0.0.1:8000/4/5"
response_sum = httpx.get(sum_url)
print(response_sum.json())
