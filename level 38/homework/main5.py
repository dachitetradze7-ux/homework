def manage_dict(my_manage):
    my_manage.update({"age": 14})

    last_item = my_manage.popitem()

    print(f"removed last item: {last_item}")
    print(f"last dictionary: {my_manage}")


simple = {"name": "dachi"}
manage_dict(simple)
