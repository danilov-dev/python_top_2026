import string
import random
from typing import Optional

import requests

def get_url_image(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get("message") and data.get('status') == "success":
            img_link = data.get('message')
            return img_link
        else:
            return ''
    except Exception as e:
        print(f"Error: {e}")
        return ""


def get_image_by_url(url: str) -> Optional[bytes]:
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        print(type(response.content))
        return response.content
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    base_url = "https://dog.ceo/api/breeds/image/random"
    link = get_url_image(base_url)
    if link:
        image = get_image_by_url(link)
        if image is not None:
            with open("dog.jpg", "wb") as f:
                f.write(image)

# Скачать не менее 20 фото
# Названия фото по породе собаки
# Каждая порода в отдельной директории

def generate_random_string(length: int) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation

    return ''.join(random.choice(alphabet) for i in range(length))

print(generate_random_string(10))
