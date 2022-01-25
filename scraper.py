from requests_html import HTMLSession
import csv

s = HTMLSession()

def get_product_links(page):
    url = f'https://themes.woocommerce.com/storefront/product-category/clothing/page/{page}/'
    links = []
    r = s.get(url)

    products = r.html.find('ul.products li')

    for item in products:
        links.append(item.find('a', first=True).attrs['href']) # an 'a' tag refers to a link to the products.
    return links

def parse_product(url):

    r = s.get(url)
    # if you are saving to csv use a dictionary and if you are saving to a database it's best to use a tuple.

    title = r.html.find('h1.product_title.entry-title', first=True).text.strip() # h1 is the title of the product.
    price = r.html.find('p.price', first=True).text.strip().replace('\n', ' ') # p is the class and price is the tag. '\n' is a new line in the text. We are going to remove it to prevent errors when we are saving to a csv.
    category = r.html.find('span.posted_in', first=True).text.strip() # span is the class and posted_in is the tag
    try:
        sku = r.html.find('span.sku', first=True).text.strip() # span is the class and sku is the tag
    except AttributeError as err:
        sku = 'None'
        # print (err)

    product = {
        'title': title,
        'price': price,
        'sku': sku,
        'category': category,
    }
    return product

def save_csv(results):
    keys = results[0].keys() # we are going to use the keys of the dictionary to create our headers.

    with open('products.csv', 'w', newline='', encoding='utf-8') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)


results = []
for x in range(1, 5):
    print('Getting page: ', x)
    urls = get_product_links(x) # this will get all the product links from pages in range x
    for url in urls:
        results.append(parse_product(url))
    print('Total results: ', len(results))
    save_csv(results)