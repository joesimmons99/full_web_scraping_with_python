from requests_html import HTMLSession

s = HTMLSession()

# def get_product_links(page):
#     url = f'https://themes.woocommerce.com/storefront/product-category/clothing/page/{page}/'
#     links = []
#     r = s.get(url)

#     products = r.html.find('ul.products li')

#     for item in products:
#         links.append(item.find('a', first=True).attrs['href']) # an 'a' tag refers to a link to the products.
#     return links

test_link = 'https://themes.woocommerce.com/storefront/product/lowepro-slingshot-edge-250-aw/'

r = s.get(test_link)

print(r.html.find('h1.product_title.entry-title', first=True).text)