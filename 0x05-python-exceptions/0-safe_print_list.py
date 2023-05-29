def safe_print_list(my_list=[], x=0):
    try:
        summ = 0
        for i in my_list:
            if summ < x:
                print(i, end=" ")
                summ += 1
            else:
                break
        print()
        return summ
    except:
        return 0
