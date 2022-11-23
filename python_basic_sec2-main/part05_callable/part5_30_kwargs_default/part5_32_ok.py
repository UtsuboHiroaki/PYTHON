from datetime import datetime


def write_all_list_strings(list_strings=None):
    if list_strings is None:
        list_strings = []

    print(len(list_strings))
    last_str = '出力日時: ' + datetime.now().strftime('%Y/%m/%d %H:%M:%S.%f')
    list_strings.append(last_str)
    for list_string in list_strings:
        print(list_string)
    print('出力を終了しました\n')


write_all_list_strings()
write_all_list_strings()
write_all_list_strings()
write_all_list_strings()
