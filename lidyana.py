# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def get_page_source(product_url):
    """
    a simple function which returns page source as string
    :param product_url:
    :return page_source:
    """
    page_source = requests.get(url=product_url)
    return page_source.text


def get_fund_creds(html_source):
    """
    takes source code of a product page and return it's information as a dictionary

    :param html_source:
    :return product(dict):
    """
    bs = BeautifulSoup(html_source, "html.parser")
    product = dict()

    product_brand = bs.find(itemprop="brand").get_text()
    product_brand = product_brand.encode("utf-8").strip()

    product_name = bs.find(itemprop="name").get_text()
    product_name = product_name.encode("utf-8").strip()

    product_content = bs.find(class_="content first").get_text()
    product_content = product_content.encode("utf-8").strip()

    product['brand'] = product_brand
    product['name'] = product_name
    product['content'] = product_content

    return product
