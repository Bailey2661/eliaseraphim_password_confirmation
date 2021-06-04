# author: elia deppe
# date 6/4/21
#
# simple password confirmation program that confirms a password of size 12 to 48, with at least: one lower-case letter
#   one upper-case letter, one number, and one special character.

# constants
MIN_LENGTH, MAX_LENGTH = 12, 48  # min and max length of password

#   dictionaries
LOWER_CASE, UPPER_CASE = 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS, SPECIAL_CHARS = '0123456789', '!@#$%^&*()-_+=[{]}|:;<,>.?/'
FULL_DICTIONARY = LOWER_CASE + UPPER_CASE + NUMBERS + SPECIAL_CHARS


# function
# get_password
#
#   parameter(s)
#       none
#   return value(s)
#       password              | string | the password desired by the user
#       password_confirmation | string | the password desired by the user, entered a second time for confirmation
#
# description: gets the password from the user, and confirms that is the desired password by retrieving it twice.
def get_password():
    password = input('>> password\n>> ')
    password_confirmation = input('>> confirm password\n>> ')

    return password, password_confirmation


# function
# check_char
#
#   parameter(s)
#       char  | string                    | the current character being inspected
#       flags | dictionary {string: bool} | the flags for the password's validity
#   return value(s)
#       none
#
# description: checks the current character to see if it is valid. if so, checks to see if it fulfills the requirement
#   of being a lower-case letter, upper-case letter, number, or special character (unless already fulfilled). if so,
#   then the respective flag is set to true.
#
#   if the character is not within the dictionary, then the invalid character flag is set.
def check_char(char, flags):
    if char in FULL_DICTIONARY:
        if not flags.get('lower') and char in LOWER_CASE:
            flags.update({'lower': True})

        elif not flags.get('upper') and char in UPPER_CASE:
            flags.update({'upper': True})

        elif not flags.get('num') and char in NUMBERS:
            flags.update({'num': True})

        elif not flags.get('special') and char in SPECIAL_CHARS:
            flags.update({'special': True})
    else:
        flags.update({'invalid': True})


# function
# valid
#
#   parameter(s)
#       flags | dictionary {string: bool} | the flags for the password's validity
#   return value(s)
#       none
#
# description: returns whether or not the password is valid based on the current flags
def valid(flags):
    return (
            not flags.get('invalid') and flags.get('lower') and flags.get('upper')
            and flags.get('num') and flags.get('special')
    )


# --------------- Error Functions


# function
# general_error
#
#   parameter(s)
#       flags | dictionary {string: bool} | the flags for the password's validity
#   return value(s)
#       none
#
# description: informs the user of which error they encountered when entering their password based on the flags.
def general_error(flags):
    if flags.get('invalid'):
        print('>> invalid characters used')
        print('>> the characters ~`\\| may not be used within a password')

    if not flags.get('lower'):
        print('>> password requires at least one lower-case letter')

    if not flags.get('upper'):
        print('>> password requires at least one upper-case letter')

    if not flags.get('num'):
        print('>> password requires at least one number')

    if not flags.get('special'):
        print('>> password requires at least one special character')
        print(f'     valid special characters | {SPECIAL_CHARS}')


# function
# length_error
#
#   parameter(s)
#       password | string | the password entered by the user
#       length   | int    | the length of the password
#   return value(s)
#       none
#
# description: outputs an error where the length of the password is too small, or too large
def length_error(password, length):
    print('>> incorrect length, password should be 12 to 48 characters long')
    print(f'    password | {password} | {length} characters long')


# function
# password_mismatch_error
#
#   parameter(s)
#       password              | string | the password entered by the user
#       password_confirmation | string | the confirmation password entered by the user
#   return value(s)
#       none
#
# description: outputs an error where the password and the password confirmation do not match
def password_mismatch_error(password, password_confirmation):
    print('>> passwords do not match, please check your spelling')
    print(f'    password              | {password}')
    print(f'    password confirmation | {password_confirmation}')


# function
# main
#
#   parameter(s)
#       none
#   return value(s)
#       none
#
# description: the main function of the program, initiates retrieving a password from the user and then confirms if it
#   is valid. the user is informed if the password is valid, or invalid and why it was invalid
def main():
    i = 0
    password, password_confirmation = get_password()
    flags = {
        'invalid': False,
        'lower'  : False,
        'upper'  : False,
        'num'    : False,
        'special': False
    }

    # check that the passwords match
    if password == password_confirmation:
        length = len(password)

        # check the length of the password
        if MIN_LENGTH <= length <= MAX_LENGTH:
            # loop through the password, and while there has been no invalid char
            while i < length and not flags.get('invalid'):
                check_char(password[i], flags)
                i += 1

            # if loop is finished and flags are proper, then the password is good
            if valid(flags):
                print('>> password set')

            # otherwise a general error
            else:
                general_error(flags)
        # error with length of password
        else:
            length_error(password, length)
    # password and confirmation mismatch
    else:
        password_mismatch_error(password, password_confirmation)


if __name__ == '__main__':
    main()
