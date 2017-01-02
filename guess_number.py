import random


def guess_number(number):
    while True:
        input_number = int(raw_input('Input your number:\n'))
        if input_number > number:
            print "Your number is bigger"
        elif input_number < number:
            print "Your number is smaller"
        else:
            print "Bingo"
            break


def main():
    print "--------Begin Game--------"
    while True:
        number = random.randint(0, 99)
        guess_number(number)
        ans = ''
        while True:
            ans = raw_input('Do you want to continue? [yes/no]\n')
            if ans in ['yes', 'no']:
                break
            else:
                print 'Invaild input'

        if ans == 'no':
            print '--------Game over--------'
            break

if __name__ == '__main__':
    main()
