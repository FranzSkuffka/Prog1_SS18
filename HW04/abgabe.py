"""
1.1 Der code gibt nicht immer boolean zurück. z.B. bei einer leeren liste
1.2 Bei einer liste der Länge 1 sollte die Liste sortiert sein, aber es ist dennoch scheinbar 'keine aussaeg möglich'
"""
from worst_code import ListIsSorted
from good_code import is_sorted, is_sorted_one, is_sorted_two

print(ListIsSorted([]))
print(ListIsSorted([1]))

"""
2.1 CamelCase is bad for function names
2.2 Encoding ist futsch
2.3 Signatur entspricht nicht den tatsächlichen Rückgabewerten
2.4 Einiges an unreachable code
"""
print(is_sorted([1,2,3]))
print(is_sorted([1,3,2]))
print(is_sorted_one([1,2,3]))
print(is_sorted_one([1,3,2]))
print(is_sorted_two([1,2,3]))
print(is_sorted_two([1,3,2]))
