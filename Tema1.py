        ##Ex1
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

        ##Ex2

ascending_list = sorted(my_list)
print(ascending_list)

        ##Ex3

descending_list = sorted(my_list ,reverse = True)
print(descending_list)

        ##Ex4

my_sliced_list = my_list[1:5:2] + my_list[6:8] + my_list[-1:]
print(my_sliced_list)

        ##Ex 5

my_sliced_list2 = my_list[0:5:2] + my_list[5::3]
print(my_sliced_list2)

        ##Ex6
multiple_of_3_list = my_list[2::7]
print(multiple_of_3_list)