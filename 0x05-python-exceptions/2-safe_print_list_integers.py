#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        for element in my_list:
            try:
                if isinstance(element, int):
                    if isinstance(element, int):
                        count += 1
            except:
                pass
            if count == x:
                break
        except:
            pass
        finally:
            print()
            return count
