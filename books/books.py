import json
import os


PESCHERA_VREMENI = "peschera_vremeni"
TAINA_ZAMKA = "taina_zamka"
NA_DNO_MORYA = "na_dno_morya"


book_names_map = {
    "PESCHERA_VREMENI": PESCHERA_VREMENI,
    "TAINA_ZAMKA": TAINA_ZAMKA,
    "NA_DNO_MORYA": NA_DNO_MORYA
}


def get_book_dir_name(book_name):
    book_dir_name = book_names_map.get(book_name)
    assert bool(book_dir_name), f"Book with name {book_name} is not found!"
    return book_dir_name


class Book:
    def __init__(self, book_dir_name: str):
        project_dir = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(project_dir, book_dir_name, "book.json")
        self.book_json = json.loads(open(filepath, "r", encoding="cp1251").read())

    def get_page(self, page_id):
        page_id = int(page_id)
        return [x for x in self.book_json if x["id"] == page_id][0]


def create_book(book_name):
    return Book(get_book_dir_name(book_name))
