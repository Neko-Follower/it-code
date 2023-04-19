from datetime import datetime
import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    day = datetime.now().strftime('%d')
    month = datetime.now().strftime('%B')
    temperature = BeautifulSoup(requests.get('https://www.google.com/search?q=weatherufa', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}).text, 'html.parser').select('#wob_tm')[0].getText().strip()
    print('Сегодня ' + day + ' ' + month + '. На улице ' + temperature + '° градусов' + '\nХолодно, лучше остаться дома') if int(temperature) < 0 else print('Сегодня ' + day + ' ' + month + '. На улице ' + temperature + '° градусов')
