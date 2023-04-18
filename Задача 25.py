def print_given(*args, **kwargs):
    for arg in args:
        print(arg, type(arg))
    fognames = sorted(kwargs.keys())
    for fog in fognames:
        print(f'{fog} {kwargs[fog]} {type(kwargs[fog])}')

print_given(1, [1, 2, 3], 'three', two=2)
print()
print_given(b=2, d=4, c=3, a=1)
        