import my_func

help(my_func.print_stars)
for _ in range(5):
    my_func.print_stars()

from my_func import print_stars

for i in range(5):
    print_stars()
