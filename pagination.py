

class Page:
    def __init__(self, data, has_next_page, has_previous_page) -> None:
        self.data = data
        self.has_next_page = has_next_page
        self.has_previous_page = has_previous_page

class Pagination:
    def __init__(self, data:list, PAGINATION_RATE:int, start_page = 1) -> None:
        self.data = data
        self.PAGINATION_RATE = PAGINATION_RATE
        self.start_page = start_page
    def get_page(self, page) -> Page:
        page -= self.start_page # we work with indexes
        start_point = page * self.PAGINATION_RATE
        finish_point = start_point + self.PAGINATION_RATE
        data = self.data[start_point:finish_point]

        # -1 because finish point is index
        has_next_page = (len(data) == self.PAGINATION_RATE) and (finish_point != len(self.data))
        has_previous_page = start_point != 0

        return Page(data, has_next_page, has_previous_page)
