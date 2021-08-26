valid_operations = [
    "plain",
    "bold",
    "italic",
    "inline-code",
    "link",
    "header",
    "new-line",
    "unordered-list",
    "ordered-list"
]


def go_option_help():
    message_help_1 = "Available formatters: plain bold italic header link inline-code ordered-list " \
                     "unordered-list new-line "
    message_help_2 = "Special commands: !help !done"
    print(message_help_1)
    print(message_help_2)
    print()


def go_option_done(result):
    file_result = open("output.md", "w", encoding="utf-8")
    file_result.writelines(result)
    file_result.close()
    return


def obtain_option():
    valid_options = [
        "!help",
        "!done"
    ]
    valid_options.extend(valid_operations)

    while True:
        option = input("Choose a formatter: ")
        if option not in valid_options:
            print("Unknown formatting type or command")
        else:
            return option


def do_operation_plain(text):
    return f"{text}"


def do_operation_bold(text):
    return f"**{text}**"


def do_operation_italic(text):
    return f"*{text}*"


def do_operation_inline_code(text):
    return f"`{text}`"


def do_operation_link(label, url):
    return f"[{label}]({url})"


def do_operation_new_line():
    return "\n"


def do_operation_header(level, text):
    header_level = "#" * level
    return f"{header_level} {text}\n"


def do_operation_list(rows, is_ordered=True):
    list_elements = []
    for row in range(1, rows + 1):
        element = input(f"Row #{row}: ")
        position = f"{row}." if is_ordered else "*"
        list_elements.append(f"{position} {element}\n")
    return "".join(list_elements)


def do_operation_unordered_list(rows):
    return do_operation_list(rows, False)


def do_operation_ordered_list(rows):
    return do_operation_list(rows)


def go_option_operation(operation):
    if operation == "plain":
        text = input("Text: ")
        return do_operation_plain(text)
    elif operation == "bold":
        text = input("Text: ")
        return do_operation_bold(text)
    elif operation == "italic":
        text = input("Text: ")
        return do_operation_italic(text)
    elif operation == "inline-code":
        text = input("Text: ")
        return do_operation_inline_code(text)
    elif operation == "link":
        label = input("Label: ")
        url = input("URL: ")
        return do_operation_link(label, url)
    elif operation == "header":
        while True:
            level = int(input("Level: "))
            if level not in range(1, 7):
                print("The level should be within the range of 1 to 6")
            else:
                break
        text = input("Text: ")
        return do_operation_header(level, text)
    elif operation == "new-line":
        return do_operation_new_line()
    elif operation == "unordered-list":
        while True:
            rows = int(input("Number of rows: "))
            if rows <= 0:
                print("The number of rows should be greater than zero")
            else:
                break
        return do_operation_unordered_list(rows)
    elif operation == "ordered-list":
        while True:
            rows = int(input("Number of rows: "))
            if rows <= 0:
                print("The number of rows should be greater than zero")
            else:
                break
        return do_operation_ordered_list(rows)


def print_text(text_list):
    print("".join(text_list))


def create_menu(text_list):
    while True:
        user_option = obtain_option()
        if user_option == "!help":
            go_option_help()
        elif user_option == "!done":
            go_option_done(text_list)
            break
        else:
            text_formatter = go_option_operation(user_option)
            if text_formatter is not None:
                text_list.append(text_formatter)
                print_text(text_list)


def main():
    text_list = []
    create_menu(text_list)


if __name__ == '__main__':
    main()
