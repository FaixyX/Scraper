from django.core.management.base import BaseCommand

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

from scrapper.models import SubCategories, Product

# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def scrape_category(url, store):
    products = []
    # Write code to extract the data.
    # We have four different store, so we will write scraper logic for each store
    # If store == 'Telemart'
    #   image = this this this
    #   title = this this this
    #   url = this this this
    #   price = this this this
    # elif store == 'Daraz'
    #   image = this this this
    #   title = this this this
    #   url = this this this
    #   price = this this this
    
    return products

class Command(BaseCommand):
    help = 'Scrape the data and dump it in the Products table'

    def handle(self, *args, **kwargs):
        # Iterate through each sub-category
        for sub_category in SubCategories.objects.all():
            self.stdout.write(f"Scraping data for sub-category: {sub_category.name}")
            products = scrape_category(sub_category.url, sub_category.store)
            for product_data in products:
                # Check if the product already exists
                product, created = Product.objects.get_or_create(
                    name=product_data['title'],
                    defaults={
                        'image': product_data.get('image'),
                        'price': product_data.get('price'),
                        'url': product_data.get('url'),
                        'store': sub_category.store,
                        'category': sub_category.category,
                        'sub_category': sub_category,
                    }
                )
                if created:
                    self.stdout.write(f"Added new product: {product.name}")
                else:
                    self.stdout.write(f"Updated existing product: {product.name}")
