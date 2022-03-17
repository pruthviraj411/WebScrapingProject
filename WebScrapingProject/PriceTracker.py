import requests
from bs4 import BeautifulSoup



products_to_track = [
    {
        "product_URL":"https://www.flipkart.com/realme-9i-prism-blue-128-gb/p/itm3e9987219f652?pid=MOBG9VGV2Q9PDXHN&lid=LSTMOBG9VGV2Q9PDXHNEJSSOX&marketplace=FLIPKART&q=realme+9i&store=tyy%2F4io&srno=s_1_2&otracker=AS_Query_OrganicAutoSuggest_6_3_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_6_3_na_na_na&fm=search-autosuggest&iid=e82ba547-4273-4057-b60d-7bbf97b1f640.MOBG9VGV2Q9PDXHN.SEARCH&ppt=sp&ppn=sp&ssid=945gzvsg280000001647406919091&qH=fb8e16ac00c01589",
        "name":"Realme 9i",
        "target_price": 20000
    },
    {
        "product_URL": "https://www.flipkart.com/motorola-g60-dynamic-gray-128-gb/p/itmf1d5d2978289e?pid=MOBFWSF8U37QFQGK&lid=LSTMOBFWSF8U37QFQGKBPO1B1&marketplace=FLIPKART&q=moto+g60+mobile+phone&store=tyy%2F4io&srno=s_1_3&otracker=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_na&iid=9487166f-514d-4aad-b799-6cd8045c0e32.MOBFWSF8U37QFQGK.SEARCH&ssid=g07nkgii5s0000001647406875872&qH=798e13c6dd66d3fe",
        "name":"Moto G60",
        "target_price": 20000
    },
    {
        "product_URL": "https://www.flipkart.com/motorola-edge-30-pro-cosmos-blue-128-gb/p/itm98bcbdae6fe78?pid=MOBG9CKYHGJGWCXX&lid=LSTMOBG9CKYHGJGWCXXU848SO&marketplace=FLIPKART&q=moto+g60+mobile+phone&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_na&iid=9487166f-514d-4aad-b799-6cd8045c0e32.MOBG9CKYHGJGWCXX.SEARCH&ssid=g07nkgii5s0000001647406875872&qH=798e13c6dd66d3fe",
        "name":"Moto Edge30",
        "target_price": 50000
    },
    {
        "product_URL": "https://www.flipkart.com/hp-ryzen-7-quad-core-3rd-gen-16-gb-512-gb-ssd-windows-10-home-13-ay0046au-2-1-laptop/p/itm956b1526409fa?pid=COMG9WKZNDHUYZ4R&lid=LSTCOMG9WKZNDHUYZ4R75HRIN&marketplace=FLIPKART&q=laptop&store=6bo%2Fb5g&srno=s_1_3&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&fm=search-autosuggest&iid=10abcaf5-4ecb-4f40-8d43-003b56762d84.COMG9WKZNDHUYZ4R.SEARCH&ppt=sp&ppn=sp&ssid=hf0dx2v0c00000001647474145065&qH=312f91285e048e09",
        "name":"HP Ryzen 7 Quad Core 3rd Gen",
        "target_price": 110000
    },
    {
        "product_URL": "https://www.flipkart.com/lenovo-ideapad-gaming-3-core-i5-11th-gen-8-gb-512-gb-ssd-windows-10-home-4-graphics-nvidia-geforce-gtx-1650-15ihu6-laptop/p/itme9af20e47eba2?pid=COMG6EZ2RZKMAPX9&lid=LSTCOMG6EZ2RZKMAPX99DDSBQ&marketplace=FLIPKART&q=laptops&store=6bo%2Fb5g&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=en_MBkWFEcbsastCn6frYVMg84q%2B1lM72fg9XxKIxyVYgoZbONPof%2BglFMCoVLoOeooEB33c22MrcuQvFNyNBsgVg%3D%3D&ppt=sp&ppn=sp&ssid=74iku4dx740000001647474492039&qH=c06ea84a1e3dc3c6",
        "name":"Lenovo IdeaPad Gaming 3 Core i5",
        "target_price": 60500
    }

]

def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    }

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price3 = soup.find("div", {'class': '_30jeq3 _16Jk6d'})

    return price3.string

result_file = open('my_result_file.txt','w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_URL"))
        print(product_price_returned + "-" + every_product.get("name"))

        my_product_price = product_price_returned[1:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(my_product_price)

        print(my_product_price)
        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get(
                'name') + '-' + 'Available at your target price' + '\t,current price-' + str(my_product_price)+ '\n')

        else:
            print("Still at same price")


finally:
    result_file.close()











