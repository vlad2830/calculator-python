import sys
import os

# Добавляем путь к родительской директории в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.calculator import Calculator

def main():
    calc = Calculator()
    print("калькулятор")
    
    while True:
        print("\nДоступные операции:")
        print("1. Сложение (+)")
        print("2. Вычитание (-)")
        print("3. Умножение (*)")
        print("4. Деление (/)")
        print("5. Выход")
        
        choice = input("\nВыберите операцию (1-5): ")
        
        if choice == '5':
            print("До свидания!")
            break
            
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            
            if choice == '1':
                result = calc.add(a, b)
                print(f"Результат: {a} + {b} = {result}")
            elif choice == '2':
                result = calc.subtract(a, b)
                print(f"Результат: {a} - {b} = {result}")
            elif choice == '3':
                result = calc.multiply(a, b)
                print(f"Результат: {a} * {b} = {result}")
            elif choice == '4':
                result = calc.divide(a, b)
                print(f"Результат: {a} / {b} = {result}")
            else:
                print("Неверный выбор операции!")
                
        except ValueError as e:
            print(f"Ошибка: {str(e)}")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    main()