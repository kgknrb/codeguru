def non_conformant_variable_initialized_within_loop():
    mylist = ['first', 'second', 'third', 'other']
    s = ""
    for item in mylist:
        s += "Hello World" + item
        print(s)

#############unnecessary-iteration
def nonconformant_list2():
    input_list = set([10, "USA", 20, "RSA"])
    x = 0
    while x < len(input_list):
        y = input_list[x]
        if y == 20:
            print("found country code")
        x += 1

def nonconformant_list3():
    input_list = set([10, "USA", 20, "RSA"])
    for x in range(len(input_list)):
        y = input_list[x]
        if y == 10:
            print("item found")

##avoid_complex_comprehension_non_compliant_1
def avoid_complex_comprehension_non_compliant_2():
    text = [['bar','foo','fooba'],['Rome','Madrid','Houston'], ['aa','bb','cc','dd']]
    text_3 = [z.upper() for x in text if len(x) == 3 for y in x for z in y]

def avoid_complex_comprehension_non_compliant_3():
    text = [['bar','foo','fooba'],['Rome','Madrid','Houston'], ['aa','bb','cc','dd']]
    text_3 = [z.upper() for x in text if len(x) == 3 for y in x for z in y]
    text_4 = [y.upper() for x in text if len(x) == 3 for y in x if y.startswith('f')]

def avoid_complex_comprehension_non_compliant_4():
    text = [['bar','foo','fooba'],['Rome','Madrid','Houston'], ['aa','bb','cc','dd']]
    text_3 = {z.upper() for x in text if len(x) == 3 for y in x for z in y}
