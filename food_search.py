import requests
from bs4 import BeautifulSoup

def search_food(request):
     url = 'https://platform.fatsecret.com/rest/server.api'
     search_expression=request.args.get('search_expression')
     auth_token=request.args.get('auth_token')
     params = { 'method':'foods.search', 'search_expression':search_expression, 'format':'json', 'max_results':20, 'page_number':0 }
     header = { 'Authorization': 'Bearer ' + auth_token }
     response = requests.post(url, params=params, headers=header).json()
     
     for food in response['foods']['food']:
         food['food_url'] = get_image(f"{food['food_url']}/photos")
    
     return response


def get_image(url):
    soup = BeautifulSoup(requests.get(url).text)
    images = soup.find_all('img')
    
    for image in images:
        if "https://m.ftscrt.com/food" in image['src']:
            return image['src']
    return ''