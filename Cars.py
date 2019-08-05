def make_car(make, module, **car_info):
    dictionary = {}
    dictionary['Cary Type'] = make.title()
    dictionary['Module'] = module.title()
    for key, value in car_info.items():
        dictionary[key.title()] = value.title()
    return dictionary

x = make_car('honda', 'civic', year = '2010')

for a, b in x.items():
    print(a + ": " + b)
    
