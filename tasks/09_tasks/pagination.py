class Pagination:
    def __init__(self, items: list, page_size=10):
        self.page_size = page_size
        self.items = items
        self.page_index = 1
        self.list_of_pages = {}

        pages = []

        for x in range(0, len(self.items), self.page_size):
            page = self.items[x: self.page_size + x]
            pages.append(page)

        for index, item in enumerate(range(len(pages)), start=1):
            self.list_of_pages.update({index: pages[item]})

    def get_visible_items(self):
        return self.list_of_pages[self.page_index]

    def prev_page(self):
        if self.page_index != 1:
            self.page_index -= 1
        return self

    def next_page(self):
        if self.page_index != len(self.list_of_pages):
            self.page_index += 1
        return self

    def first_page(self):
        self.page_index = 1
        return self

    def last_page(self):
        self.page_index = len(self.list_of_pages)
        return self

    def go_to_page(self, page: int):
        if page > len(self.list_of_pages):
            page = len(self.list_of_pages)
        elif page < 1:
            page = 1

        self.page_index = page
        return self

    def get_current_page(self):
        return self.page_index

    def get_page_size(self):
        return self.page_size

    def get_items(self):
        return self.items


alphabetList = list('abcdefghijklmnopqrstuvwxyz')
a = Pagination(alphabetList)
a.get_visible_items()
a.next_page()


