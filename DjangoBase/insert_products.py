import json
import requests


def insert_products(json_url, api_url):
    """
    Calls json_url json response as products iter, 
    sending "upsert" (update or insert) request to the app API for each product

    Parameters:
    json_file: listed products.
    api_url: App PUT Endpoint for Product

    Returns:
    None
    """
    # Fetch the raw JSON data from the GitHub "raw" URL
    response = requests.get(json_url)
    if response.status_code != 200:
        print(f"Failed to fetch JSON data: Status code {response.status_code}")
        return

    try:
        products = response.json()['products']
    except ValueError:
        print("Failed to parse JSON")
        return

    for product in products:
        # Check if the product exists
        check_response = requests.get(f'{api_url}{product["reference"]}/')
        if check_response.status_code == 404:
            # Product does not exist, use POST to create a new product
            post_response = requests.post(api_url, json=product)
            print(f'Created {product["name"]}: Status Code {post_response.status_code}')
        elif check_response.status_code == 200:
            # Product exists, use PUT to update the existing product
            put_response = requests.put(f'{api_url}{product["reference"]}/', json=product)
            print(f'Updated {product["name"]}: Status Code {put_response.status_code}')
        else:
            print(f'Error checking product {product["name"]}: Status Code {check_response.status_code}')

if __name__ == '__main__':
    json_url = 'https://raw.githubusercontent.com/Valerdat-Team/django-exercise/main/products.json?token=GHSAT0AAAAAACKQIHX5JPGCS22R6IKPKHIGZL5VDMA'
    api_url = 'http://localhost:8000/app/valerdat/products/' 
    insert_products(json_url, api_url)
