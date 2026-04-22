def get_details(any):
    all_keys = any.keys()
    all_values = any.values()

    return all_keys, all_values

simple = {"a": 1, "b": 2, "c": 3}
keys, values = get_details(simple)

print(f"key: {keys}")
print(f"value: {values}")