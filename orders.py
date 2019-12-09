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

# open_print_txt_file('order.txt')
# open_print_txt_file('order.txt')
open_print_close('order.txt')

