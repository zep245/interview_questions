def duplicates(lst):
    s = set(lst)
    if len(s) == len(lst):
        return False
    else:
        return True


print(duplicates([1,2,3]))