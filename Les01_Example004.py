# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма.
#  Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки. 
# Это отношение прибыли к выручке. 
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.




print ("Введите выручку фирмы: ")
v = float(input())

print ("Введите издержки фирмы: ")
i = float(input())

if v>i:
    print ('ПРИБЫЛЬ — выручка больше издержек')
    print ((v-i)/v*100,'%')
    print ("Введите количество сотрудников: ")
    piple = float(input())
    print ("Рентабельность фирмы на одного человека равняется ", v/piple, 'р.')

else:
    print ('УБЫТОК — издержки больше выручки.')

