def show_greetings(message):
    print(message)


def show_program_title(title):
    print(title)


def print_first_message(func1, func2, message, title):
    func1(message)
    func2(title)


print_first_message(
    show_greetings,
    show_program_title,
    'こんばんは。',
    '夜のニュースの時間です。'
)
