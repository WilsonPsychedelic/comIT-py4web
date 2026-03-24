#cli_utils/separators.py

def print_custom_separator(char, length):
    print(char[0] * length)

print_custom_separator("*", 30)
print_custom_separator("-", 10)
print_custom_separator("#", 50)

def print_labeled_separator(label, char="*", width=30):

    print_labeled_separator("START".center(20, "*"))

    print_labeled_separator("DONE", char="*", width=40)

def print_box(message, char="*"):
    width = len(message) + 4

    print(char * width)
    print(char + " " + message + " " + char)
    print(char * width)
    
print_box("Hello, World!")
