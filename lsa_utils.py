#TODO write logics for these

def zero():
    return 0

def one():
    return 1

def two():
    return 2

def three():
    return 3

def four():
    return 4

def five():
    return 5

def six():
    return 6

def seven():
    return 7

def eight():
    return 8

def nine():
    return 9

def ten():
    return 10

def eleven():
    return 11

def twelve():
    return 12

def thirteen():
    return 13

def fourteen():
    return 14

def fifteen():
    return 15

def get_int_from_hex(hex_byte):
    options = {'0' : zero,
               '1' : one,
               '2' : two,
               '3' : three,
               '4' : four,
               '5' : five,
               '6' : six,
               '7' : seven,
               '8' : eight,
               '9' : nine,
               'A' : ten,
               'B' : eleven,
               'C' : twelve,
               'D' : thirteen,
               'E' : fourteen,
               'F' : fifteen,
               }
    first_digit = options[hex_byte[2]]()
    second_digit = options[hex_byte[3]]()
    return first_digit*16 + second_digit

def get_lsa_age(first_byte, second_byte):
    first_int = get_int_from_hex(first_byte)
    second_int = get_int_from_hex(second_byte)
    return first_int*256 + second_int

def get_lsid(first_byte, second_byte, third_byte, fourth_byte):
    first_octet = str(get_int_from_hex(first_byte))
    second_octet = str(get_int_from_hex(second_byte))
    third_octet = str(get_int_from_hex(third_byte))
    fourth_octet = str(get_int_from_hex(fourth_byte))
    return first_octet + '.' + second_octet + '.' + third_octet + '.' + fourth_octet

def get_rtr(first_byte, second_byte, third_byte, fourth_byte):
    first_octet = str(get_int_from_hex(first_byte))
    second_octet = str(get_int_from_hex(second_byte))
    third_octet = str(get_int_from_hex(third_byte))
    fourth_octet = str(get_int_from_hex(fourth_byte))
    return first_octet + '.' + second_octet + '.' + third_octet + '.' + fourth_octet

def get_seq(first_byte, second_byte, third_byte, fourth_byte):
    first_int = get_int_from_hex(first_byte)
    second_int = get_int_from_hex(second_byte)
    third_int = get_int_from_hex(third_byte)
    fourth_int = get_int_from_hex(fourth_byte)
    return first_int*16777216 + second_int*65536 + third_int*256 + fourth_int