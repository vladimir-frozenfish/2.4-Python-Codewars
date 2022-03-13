def slices_to_name(n):
    if isinstance(n, str) or n < 2:
        return None
    if n % 2:
        return f'bread {"sandwich " * (n // 2)}'.rstrip()
    return ('sandwich ' * (n // 2)).rstrip()

def name_to_slices(name):
    if isinstance(name, int) or name == '' or name == 'bread' or name == None:
        return None

    name = name.split()

    name_set = set(name)
    name_set.discard('bread')
    name_set.discard('sandwich')
    if len(name_set) != 0:
        return None

    if 'bread' in name and name.index('bread') != 0:
        return None

    return name.count('bread') + name.count('sandwich') * 2


print('test slices_to_name')
print(slices_to_name(0) == None)
print(slices_to_name(1) == None)
print(slices_to_name(-2) == None)
print(slices_to_name('bread') == None)
print(slices_to_name(2) == 'sandwich')
print(slices_to_name(3) == 'bread sandwich')
print(slices_to_name(11) == 'bread sandwich sandwich sandwich sandwich sandwich')
print(slices_to_name(8) == 'sandwich sandwich sandwich sandwich')

print('test name_to_slices')
print(name_to_slices(12) == None)
print(name_to_slices('') == None)
print(name_to_slices('sandwich bread sandwich') == None)
print(name_to_slices('sand wich') == None)
print(name_to_slices('bread sandwich') == 3)
print(name_to_slices('sandwich sandwich sandwich sandwich') == 8)
print(name_to_slices('bread') == None)
print(name_to_slices('bread sandwich sandwich sandwich') == 7)