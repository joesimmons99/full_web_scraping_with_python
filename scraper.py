from requests_html import HTMLSession

s = HTMLSession()

url = 'https://themes.woocommerce.com/storefront/product-category/clothing/page/1/'

r = s.get(url)

# print(r.status_code) # we want to make sure we got a 200 response to establish that the page is working. 300 is a redirect, 400 is a bad request and 500 is a forbidden.
# print(r.text) # confirm that we're actually getting the page text back.

