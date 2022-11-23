def show_greetings():
    print('こんにちは。')


def show_program_title():
    print('お昼のニュースの時間です。')


def print_first_message(func1, func2):
    func1()
    func2()


print_first_message(show_greetings, show_program_title)
