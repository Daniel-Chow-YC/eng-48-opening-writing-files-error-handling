def open_print_txt_file(file_name):
    try:
        opened_file = open(file_name, 'r')
        lines = opened_file.readlines()
        for line in lines:
            print(line.strip('\n'))

        opened_file.close() # closes the file so it can be used by other programs

    except FileNotFoundError as errmsg: # the as errmsg captures the original message
        print('Check file name &/or path - File cannot be found')
        print(errmsg) # printing original message
        # raise

def open_print_close(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip('\n'))

    except FileNotFoundError as error:
        print('Check your file')
        print(error)

    finally:
        print('Program closing - execution done!')

def open_write_txt(file, item):
    try:
        with open(file, 'a') as file_to_write:
            file_to_write.write(item + '\n')
    except FileNotFoundError as error:
        print('Check your file and the path')
        print(error)
    finally:
        print('Program closing - execution done!')

# open_print_txt_file('order.txt')
# open_print_txt_file('order.txt')

open_write_txt('order2.txt', 'cupcake')
open_write_txt('order2.txt', 'OJ with carrot')
open_write_txt('order2.txt', 'Eggs Benedict')
open_write_txt('order2.txt', 'Beans on toast')
open_print_close('order2.txt')
