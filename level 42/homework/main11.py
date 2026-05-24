def get_dict_value(dictonary, key):
    try:
        value = dictonary[key]
    except KeyError:
        print( )