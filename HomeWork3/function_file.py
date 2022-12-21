from random import sample

def random_list (len_list):
    new_list = sample (range (1, len_list ** 2), k=len_list)
    return new_list

def sum_odd (new_list, sum=0):
    for i in range (len(new_list)):
        if i%2==0:
            sum += new_list[i]
    return sum

def pair_multiplication (new_list, list_pair_multiplication = []):
    if len(new_list)%2==0:
        for i in range (int(len(new_list)/2)):
            list_pair_multiplication.append (new_list[i]*new_list[-1-i])
    else:
        for i in range (int(len(new_list)/2)+1):
            if i == int(len(new_list)/2):
                list_pair_multiplication.append (new_list[i])
            else:
                list_pair_multiplication.append (new_list[i]*new_list[-1-i])
    return list_pair_multiplication

def binary (number, binary_list = []):
    while number>0:
        binary_list.insert(0, int(number%2))
        number = int(number/2)
    return binary_list
    