"""
The rgb function is incomplete. Complete it so that passing in RGB decimal
values will result in a hexadecimal representation being returned.
Valid decimal values for RGB are 0 - 255.
Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""

def int_to_hex(x):
    if x < 0:
        return '00'
    elif x < 16:
        return '0' + f'{x:X}'
    elif x >= 255:
        return 'FF'

    return f'{x:X}'

def rgb(r, g, b):
    rgb_hex = int_to_hex(r) + int_to_hex(g) + int_to_hex(b)
    return rgb_hex

print(rgb(16, 0, 0))
print(rgb(1, 2, 3))
print(rgb(255, 255, 255))
print(rgb(254, 253, 252))
print(rgb(254, 253, 252))
print(rgb(-20, 275, 125))

'''
test.assert_equals(rgb(0,0,0),"000000", "testing zero values")
test.assert_equals(rgb(1,2,3),"010203", "testing near zero values")
test.assert_equals(rgb(255,255,255), "FFFFFF", "testing max values")
test.assert_equals(rgb(254,253,252), "FEFDFC", "testing near max values")
test.assert_equals(rgb(-20,275,125), "00FF7D", "testing out of range values")
'''