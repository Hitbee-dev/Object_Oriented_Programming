# list2 = list1을 하게 되면 데이터를 복사하는것이 아니라,
# list2가 list1을 가리키고 있는 것이기 때문에 정확히 알아야한다.
list1 = [1, 2, 3, 4]
list2 = list1
list2.pop()
print(list1)

# list4 = list3[:]은 데이터를 꺼내서 복사한 것이기 때문에
# list4의 원소를 변경해도 list3의 원소는 변경되지 않는다.
list3 = [1, 2, 3, 4]
list4 = list3[:]
list4.pop()
print(list3)