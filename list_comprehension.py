def dont_do_this():
    a_simple_list = []
    for i in range(10):
        a_simple_list.append(i)

    return a_simple_list

def do_this():
    a_simple_list = [i for i in range(10)]
    return a_simple_list


print(dont_do_this(), end='\n\n')
print(*do_this())