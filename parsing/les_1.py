import json
from typing import Optional

from bs4 import BeautifulSoup
import requests

class Quote:
    def __init__(self, text: str, author: Author, tags: list):
        self.text = text
        self.author = author
        self.tags = tags

    def to_dict(self):
        return {
            'text': self.text,
            'author': self.author.to_dict() if self.author else None,
            'tags': [tags.to_dict() for tags in self.tags]
        }


class Author:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url
    def to_dict(self):
        return {'name': self.name, 'url': self.url}

class Tag:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url
    def to_dict(self):
        return {'name': self.name, 'url': self.url}

class QuoteScraper:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.quotes = []
        self.authors = []
        self.tags = []

    def _fetch_page(self, url:str):
        try:
            page = requests.get(url)
            page.raise_for_status()
            return page.text
        except requests.exceptions.RequestException as e:
            print(e)
            return None

    def _parse_quote(self, quote_element) -> Optional[Quote]:
        try:
            text_element = quote_element.find('span', class_='text')

            if text_element is None:
                return None
            text = text_element.text.strip()

            author_element = quote_element.find('small', class_='author')
            author_name = author_element.text.strip() if author_element else "Неизвестный"

            author_link_elem = quote_element.find('a')['href'] if author_element else None
            print(author_link_elem)
            author_url = self.base_url + author_link_elem.lstrip('/')
            author = Author(name=author_name, url=author_url)


            self.authors.append(author)

            tags = []
            tags_div = quote_element.find('div', class_='tags')
            if tags_div:
                tag_links = tags_div.find_all('a', class_='tag')
                for tag in tag_links:
                    tag_name = tag.text.strip()
                    tage_url_link = self.base_url + tag['href'].lstrip('/')

                    tag = Tag(tag_name, tage_url_link)
                    tags.append(tag)
                    self.tags.append(tag)

            return Quote(text=text,author=author, tags=tags)
        except Exception as e:
            print(f"This {e}")
            return None

    def scrape_all_page(self):
        num_page = 1

        while True:
            if num_page == 1:
                url = self.base_url
            else:
                url = f"{self.base_url}page/{num_page}/"

            page = self._fetch_page(url)
            if not page:
                break

            soup = BeautifulSoup(page, 'html.parser')
            quote_elements = soup.find_all('div', class_='quote')

            if not quote_elements:
                break

            for quote_element in quote_elements:
                quote = self._parse_quote(quote_element)
                if quote:
                    self.quotes.append(quote)

            num_page += 1

        return self

    def save_to_json(self, file_name: str):
        data = {
            'quotes': [quote.to_dict() for quote in self.quotes],
            'authors': [author.to_dict() for author in self.authors],
            'tags': [tags.to_dict() for tags in self.tags],
        }
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            print("Файл записался удачно!")


if __name__ == '__main__':
    scraper = QuoteScraper("https://quotes.toscrape.com/")
    scraper.scrape_all_page()
    scraper.save_to_json("quotes.json")