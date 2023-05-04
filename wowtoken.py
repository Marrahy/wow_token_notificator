import requests
from winotify import Notification

url = "https://wowtokenprices.com/current_prices_ajax.php"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()    
    price =  data['eu']['current_price']
    
if price > 250000:
    notification = Notification(app_id='Not today boy',
                                title=':(',
                                msg=price,
                                duration='short')
    notification.show()
else:
    notification = Notification(app_id='Token Price',
                                title="It's the right time"
                                msg="¡GOGOGOGOGOGOGOGO!",
                                duration='long')
    notification.show()
exit()
