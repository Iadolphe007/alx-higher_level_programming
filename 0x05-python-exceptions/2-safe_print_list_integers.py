def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in my_list[:x]:
            try:
                if isinstance(item, int):
                print("{:d}".format(item), end=' ')
                count += 1
            except ValueError:
                pass
        print()
        return count
    except TypeError:
        raise ValueError("Invalid argument: my_list must be a list")

