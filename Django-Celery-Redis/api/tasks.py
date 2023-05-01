from celery import shared_task
import requests
from bs4 import BeautifulSoup

@shared_task
def my_async_task(x, y):
    # code to run asynchronously
    return x + y


@shared_task
def scrape_webpage_async(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the title of the page
    title = soup.head.title.string
    # Return the title
    return title