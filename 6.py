#Напишите программу,создающую список из чисел, которые при делении на 5 дают в остатке 3. Отобразить в прямом и обратном порядке
gap=int(input('Введите число'))  #пользователь вводит с клавиатуры масштабы бедствия
i=0  #завела счетчик с нуля.
while i<gap:     #до тех пор, пока i меньше числа пользователя
    k=i%5   #i делится по модулю на 5
    i+=1 #шаг увеличивается на 1
    if k==3: #если результат равен 3
        print(i)   #мы выводим его на экран
    else:   #если нет - шлем к черту
        ('Нет таких чисел')


