def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)
values_list = [1, True, [34, 8, 6]]
values_dict = {'a':False, 'b':126, 'c':"SLOVECHKO"}
values_list_2=[[2, 5, 1], "WOW"]

print_params()
print_params(1, 3, 6)
print_params(2, 6)
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)