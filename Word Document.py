def func():
    set01 = set()
    set10 = set()
    while True:
        try:
            n1= int(input("Количество элементов: "))
            if n1 < 0:
                raise ValueError("Количество элементов должно быть неотрицательным целым числом.")
            break
        except ValueError:
            print("Некорректный ввод. Введите целое неотрицательное число.")
    for i in range(n1):
        while True:  
            bn = input("Введите двоичное число: ")
            if not bn:  
                print("Ввод не может быть пустым.Введите двоичное число.")
                continue
            a = True
            b = bn.startswith('-')
            if b:
                if len(bn) == 1:  
                    print("Некорректный ввод")
                    continue
                bn = bn[1:]
            if not bn:  
                print("Ввод не может быть пустым.Введите двоичное число.")
                continue
            if '.' in bn:
                ip, fp = bn.split('.')
            else:
                ip, fp = bn, ''
            for i in ip:
                if i not in ('0', '1'):
                    a = False
                    print("Некорректный ввод. Введите двоичное число.")
                    break  
            for i in fp:
                if i not in ('0', '1'):
                    a = False
                    print("Некорректный ввод. Введите двоичное число.")
                    break  
            if a:
                if b:
                    set01.add('-' + bn)  
                    dn = -int(ip, 2) - int(fp or '0', 2) / (2 ** len(fp))
                else:
                    set01.add(bn)
                    dn = int(ip, 2) + int(fp or '0', 2) / (2 ** len(fp))
                set10.add(dn) 
                break  
    return set10, set01  
set10, set01 = func()
print("Множество двоичных чисел:", set01)
print("Множество десятичных чисел:", set10)
