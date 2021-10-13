def citire():
    '''
    functia citeste o lista de numere
    :return: numerele citite intr-o lista
    '''
    print('Scrieti numere din lista cu un spatiu intre ele')
    elemente = input('')
    numere_in_lista = list(map(int, elemente.split()))
    return numere_in_lista


def get_longest_product_is_odd(lsta):
    '''
    gaseste cea mai lunga segventa a caruia produsul e un nr impar (adica cea mai lunga segventa de nr impare)
    :param lsta: lista de numere
    :return: segventa cea mai lunga formata doar din nr impare
    '''
    list2 = []
    listmax = []
    x = 0
    for x in lsta:
        if x % 2 == 1:
            list2.append(x)
        else:
            if len(list2) > len(listmax):
                listmax.clear()
                listmax.extend(list2)
            list2.clear()
    if len(list2) > len(listmax):
        listmax.clear()
        listmax.extend(list2)
    return listmax


def test_get_longest_product_is_odd():
    assert (get_longest_product_is_odd([1, 3, 5, 7, 2, 4, 5])) == [1, 3, 5, 7]
    assert (get_longest_product_is_odd([1, 3, 7, 2, 1, 5, 7, 9])) == [1, 5, 7, 9]
    assert (get_longest_product_is_odd([1])) == [1]
    assert (get_longest_product_is_odd([2, 4])) == []
    assert (get_longest_product_is_odd([1, 3, 5, 6, 5, 7, 9])) == [1, 3, 5]


def nr_cifre(nr):
    '''
    returneaza nr de cifre ale unui nr
    :param nr: int , nr care dorim sa il verificam
    :return: nr de cifre ale unui nr
    '''
    cifre = 0
    while nr != 0:
        nr = nr // 10
        cifre = cifre + 1
    return cifre


def get_longest_digit_count_desc(list):
    '''
    gaseste cea mai lunga segventa de numere unde nr de cifre este descrescator
    :param list: lista de nr
    :return: segventa cea mai lunga care indeplineste conditia
    '''
    max_cif = 0
    x = 0
    list2 = []
    listmax = []
    for x in list:
        if nr_cifre(x) <= max_cif:
            max_cif = nr_cifre(x)
            list2.append(x)
        else:
            listmax.clear()
            if len(list2) > len(listmax):
                listmax.clear()
                listmax.extend(list2)
            list2.clear()
            max_cif = nr_cifre(x)
            list2.append(x)
    if len(list) == 1:
        return list
    return listmax
def test_get_longest_digit_count_desc():
    assert get_longest_digit_count_desc([123, 23, 4, 23]) == [123, 23, 4]
    assert get_longest_digit_count_desc([54]) == [54]
    assert get_longest_digit_count_desc([123, 23, 4, 23, 5]) == [123, 23, 4]
    assert get_longest_digit_count_desc([1235, 223, 14, 223]) == [1235, 223, 14]

def media(lsta):
    '''
    gasete media aritmetica a tuturor numerelor dintr-o lista
    :param lsta: toate numerele pt care se face media aritmetica
    :return: media aritmetica (float)
    '''
    x = 0
    suma = 0
    for x in lsta:
        suma = suma + x
    return suma / len(lsta)


def get_longest_average_below(lsta, k):
    '''
    returneaza segventa cea mai lunga in care media aritmetica este sub nr k dat
    :param lsta: lista de numere in care se cauta segventa
    :param k: numarul sub care media aritmetica trebuie sa se afle
    :return: segventa ceruta
    '''
    x = 1
    lst2 = []
    lst3 = []
    lstmax = []
    nr=0
    for x in lsta:
        lst2.append(x)
        if media(lst2) <= k:
            lst3.clear()
            lst3.extend(lst2)
        else:
            lst2.clear()
        if len(lstmax)<len(lst3):
            lstmax.clear()
            lstmax.extend(lst3)
    return lstmax


def test_get_longest_average_below():
    assert get_longest_average_below([1, 2, 3, 4, 5], 2.0) == [1, 2, 3]
    assert get_longest_average_below([5, 15, 20, 10, 70, 2, 4, 6, 1, 3], 14) == [2, 4, 6, 1, 3]
    assert get_longest_average_below([5, 6, 7, 8], 4) == []

def meniu():
    '''
    UI interface
    :return:
    '''
    test_get_longest_product_is_odd()
    test_get_longest_digit_count_desc()
    test_get_longest_average_below()
    print('Acest program poate face mai multe lucruri')
    print('1.Citire numere')
    print('2.Prima segventa de marime maxima care are produsul termenilor un nr impar')
    print('3.Ultima segventa de marime maxima care are numarul de cifre descrescator')
    print('4.Segventa maxima in care media nu depaseste un nr dat')
    print('x.EXIT')


if __name__ == '__main__':
    isruning = True
    while isruning == True:
        meniu()
        obtiune = input('Alegeti comanda : ')
        if obtiune == '1':
            lst = citire()
        if obtiune == '2':
            print(get_longest_product_is_odd(lst))
        if obtiune == '3':
            print(get_longest_digit_count_desc(lst))
        if obtiune == '4':
            print(get_longest_average_below(lst))
        if obtiune == 'x':
            isruning = False
        else:
            print('Doriti sa dati alta comanda?')
            obtiune = input('Y sau N ?')
            if obtiune == 'n':
                isruning = False
