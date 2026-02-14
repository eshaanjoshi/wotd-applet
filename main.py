from typing import Any
import requests
from bs4 import BeautifulSoup


def get_webcontent(url:str) -> requests.models.Response:
    try:
        page = requests.get(url)
        page.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred:{http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return page


    

WORD_OF_THE_DAY_URL = "https://www.merriam-webster.com/word-of-the-day"
DEF_API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"
def get_webster_page() -> requests.models.Response:
    page = get_webcontent(WORD_OF_THE_DAY_URL)
    return page

def parse_webster_page(page: requests.models.Response) -> str:
    """Parse webpage using bs4 to get word of the day

    Args:
        page (requests.models.Response): Word of the day webpage

    Returns:
        str: Word of the day
    """
    soup = BeautifulSoup(page.content, "html.parser")
    header_text = soup.find(class_="word-header-txt")
    if header_text:
        word_of_the_day = header_text.get_text().lower()
    else:
        raise AttributeError("Error: The word of the day could not be located!")
    return word_of_the_day

def get_api_info(word:str)-> requests.models.Response:
    return get_webcontent("https://api.dictionaryapi.dev/api/v2/entries/en/"+word)


print(
    parse_webster_page(
        get_webster_page()
    ),
    get_api_info("canoodle")
)