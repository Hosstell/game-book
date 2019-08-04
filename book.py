class Book:
    def __init__(self, book_path):
        book_steps = open(book_path, 'r').read().split('---')
        self.__data = {}
        for book_step in book_steps:
            step_number, data = Book.convert_book_step_to_dict(book_step)
            self.__data[step_number] = data

    @staticmethod
    def convert_book_step_to_dict(book_step):
        text = book_step.split('\n', 1)[1]
        number, text = text.split('\n', 1)
        lines = text.split('\n')
        text = ''
        links = []
        for line in lines[:-1]:
            if line[0] == '?':
                to = line.split('(')[1].split(')')[0]
                name = line.split(')')[1]
                links.append({
                    'to': to,
                    'text': name
                })
            else:
                text += line + '\n'
        return number, {'text': text, 'links': links}

    def __getitem__(self, index):
        return self.__data[str(index)]
