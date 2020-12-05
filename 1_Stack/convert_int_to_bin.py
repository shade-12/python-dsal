from stack import Stack

def convert_int_to_bin(dec_num):
    bin_stack = Stack()

    while dec_num > 0:
        r = dec_num % 2
        bin_stack.push(r)

        dec_num = dec_num // 2

    bin_num = 0
    while not bin_stack.is_empty():
        bin_num *= 10
        bin_num += bin_stack.pop()

    return bin_num