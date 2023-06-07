#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list is None:
        return
    sum = 0
    uniq_num = []

    for nb in my_list:
        if nb not in uniq_num:
            sum += nb
            uniq_num.append(nb)

    return sum
