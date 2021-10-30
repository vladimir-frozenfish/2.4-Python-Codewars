'''
Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

test.describe("Testing function to_camel_case")
test.it("Basic tests")
test.assert_equals(to_camel_case(''), '', "An empty string was provided but not returned")
test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")
'''

def to_camel_case(text):
    if text == '':
        return ''
    camel_list = []

    camel_list.append(text[0])

    i = 1
    while i < len(text):
        if text[i] == '_' or text[i] == '-':
            i += 1
            camel_list.append(text[i].upper())
            i += 1
        else:
            camel_list.append(text[i])
            i += 1

    return ''.join(camel_list)


print(to_camel_case('the_stealth_warrior'))
print(to_camel_case('The-Stealth-Warrior'))
print(to_camel_case(''))
print(to_camel_case("A-B-C"))

