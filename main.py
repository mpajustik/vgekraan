import requests
from bs4 import BeautifulSoup

# URL veebilehelt
url = 'https://www.vastseliina.edu.ee/'  # Asenda see soovitud veebilehe URL-iga

# Tee HTTP päring
response = requests.get(url)

# Kontrolli, et päring õnnestus
if response.status_code == 200:
    # Parseti HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Leia kõik elemendid, mille class on "well-lg event-box"
    event_boxes = soup.find_all(class_='well-lg event-box')
    # print(event_boxes)

    # Prindi välja iga "event-box" tekst
    for box in event_boxes:
        print(box.get_text(separator='\n', strip=True))
else:
    print(f'Veebilehe laadimine ebaõnnestus, statusi kood: {response.status_code}')