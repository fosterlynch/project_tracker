
def _display_supported_options():
    print("1: show projects \n2: create new project \n3: quit")

def main_options():
    print("what would you like to do?")
    _display_supported_options()
    choice = int(input())
    if choice == 1:
        print("printing out projects")
        print("------ \n ")
        main_options()
    if choice == 2:
        main_options()
    if choice == 3:
        print("goodbye")

if __name__ == "__main__":
    print("hi :)")
    main_options()

    