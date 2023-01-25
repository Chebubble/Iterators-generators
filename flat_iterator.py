class FlatIterator:

    def __init__(self, list_of_list):
        self.result_of_list = list_of_list

    def __iter__(self):
        self.cursor_main = 0
        self.cursor_inserted = -1
        return self

    def __next__(self):
        self.cursor_inserted += 1
        if self.cursor_inserted >= len(self.result_of_list[self.cursor_main]):
            self.cursor_main += 1
            self.cursor_inserted = 0
        if self.cursor_main >= len(self.result_of_list):
            raise StopIteration
        return self.result_of_list[self.cursor_main][self.cursor_inserted]
