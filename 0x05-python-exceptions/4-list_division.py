#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for i in range(0, list_length):
        try:
            newlist.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            newlist.append(0)
            print("{}".format("division by 0"))
        except TypeError:
            newlist.append(0)
            print("{}".format("wrong type"))
        except IndexError:
            newlist.append(0)
            print("{}".format("out of range"))
        finally:
            print("".format(), end="")
    return newlist
