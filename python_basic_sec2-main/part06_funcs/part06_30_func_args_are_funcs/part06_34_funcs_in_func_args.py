def print_first_message(message, title):
    def show_greetings(_message):
        print(_message)

    def show_program_title(_title):
        print(_title)

    show_greetings(message)
    show_program_title(title)


print_first_message('こんばんは。', '夜のニュースの時間です。')
