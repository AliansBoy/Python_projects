def main():
    val = 20

    def change():
        global val #Переменная становится глобальной и по завершении метода уходит за пределы main
        val = 25
        print(f'Function val: {val}')

    print(f'Now val: {val}')  #Using lockal variable
    print('changing_________')
    change()
    print(f'After changing val: {val}')  #Using lockal variable

main()
print(f'value out: {val}')


