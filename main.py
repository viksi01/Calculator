import functions
import settings

def main():
    memory = 0
    history = []

    while True:
        print('Main Menu')
        print('1. Calculator')
        print('2. Settings')
        print('3. Exit')
        choice = input('Enter your choice (1-3): ').strip()

        if choice == '1':
            while True:
                print('Calculator')
                operator = input('Enter operator (+, -, *, /, ^, sqrt, %): ').strip()

                if operator in ['+', '-', '*', '/', '^', 'sqrt', '%']:
                    
                    num1_input = input('Enter the first number or MR (Memory recall): ').strip()
                    if num1_input == 'MR':
                        num1 = memory
                        print(f'Recalled memory: {num1}')
                    else:
                        num1 = float(num1_input)
                    
                    if operator != 'sqrt':
                        num2_input = input('Enter the second number or MR (Memory recall): ').strip()
                        if num2_input == 'MR':
                            num2 = memory
                            print(f'Recalled memory: {num2}')
                        else:
                            num2 = float(num2_input)     
                    else:
                        num2 = None  
                    
                    try:
                        if operator == '+':
                            result = functions.addition(num1, num2)
                        elif operator == '-':
                            result = functions.substraction(num1, num2)
                        elif operator == '*':
                            result = functions.multiplication(num1, num2)
                        elif operator == '/':
                            result = functions.division(num1, num2)
                        elif operator == '^':
                            result = functions.power(num1, num2)
                        elif operator == 'sqrt':
                            result = functions.square_root(num1)
                        elif operator == '%':
                            result = functions.modulus(num1, num2)
                        else:
                            print('Invalid operator!')
                            continue

                        print(f"Result: {round(result, settings.decimal_places)}")
                        history.append(f'{num1} {operator} {num2 if operator != 'sqrt' else ''} = {round(result, settings.decimal_places)}')

                        
                        memory_choice = input('Do you want to perform any memory operations ("MS" to store in memory, "M+" to add to memory, "MC" to clean memory)?').strip().upper()
                        if memory_choice == 'MS':
                            memory = result
                            print(f'Stored {result} in memory.')
                        elif memory_choice == 'M+':
                            memory += result
                            print(f'Added {result} to memory. New memory: {memory}')
                        elif memory_choice == 'MC':
                            memory = 0.0
                            print('Memory cleared.')
                        else:
                            print('No changes to memory.')

                    except ValueError as e:
                        print(f"Input error: {e}")

                    
                    show_history = input('Do you want to see the history of operations? (y/n): ').strip().lower()
                    if show_history == 'y':
                        print('History')
                        for record in history:
                            print(record)

                    repeat_choice = input('Do you want to perform another calculation? (y/n): ').strip().lower()
                    if repeat_choice == 'n':
                        break

                else:
                    print('Invalid operator!')

        elif choice == '2':
            settings.set_decimal_places() 

        elif choice == '3':
            break

        else:
            print("Invalid choice, please select a number between 1 and 3.")

main()
