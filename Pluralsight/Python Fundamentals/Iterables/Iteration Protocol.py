def get_first_item(itble):
    iterator = iter(itble)
    try:
        return next(iterator)
    except StopIteration as e:
        print("Iterable is empty")
        raise


print(get_first_item(["abc","xyz"]))

print(get_first_item({"a":"abnc","b":"bfss"}))

print(get_first_item(dict()))       