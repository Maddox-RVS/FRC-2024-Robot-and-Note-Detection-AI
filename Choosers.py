def optionChooser(prompt: str, options: dict) -> int:
    while True:
        print(f'\n{prompt}')
        for option in options:
            print(f'[{options[option]}] {option}')
        choice: any = input('\nEnter the number that corrisponds with a respective option: ')
        try:
            if int(choice) in options.values():
                return int(choice)
            else: 
                print('\n[ERROR] Please enter an integer that corresponds with a respective option!\n')
                continue
        except ValueError:
            print('\n[VALUE ERROR] Please enter an integer that corresponds with a respective option!\n')
def floatChooser(prompt: str) -> float:
    while True:
        choice: any = input(f'\n{prompt}')
        try:
            return float(choice)
        except ValueError:
            print('\n[VALUE ERROR] Please enter a floating decimal point value!\n')
def intChooser(prompt: str) -> int:
    while True:
        choice: any = input(f'\n{prompt}')
        try:
            return int(choice)
        except ValueError:
            print('\n[VALUE ERROR] Please enter an integer value!\n')