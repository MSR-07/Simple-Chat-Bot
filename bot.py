def greet(bot_name, birth_year):
    print("Hello! My name is {0}.".format(bot_name))
    print("I was born in {0}.".format(birth_year))


def remind_name():
    print('Please jot down your name for me.....')
    name = input()
    print("What a great name you have, {0}!".format(name))


def guess_age():
    print('Your age, please......')
    print('Divide your age by 3, 5 and 7 and enter the remainder.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is {0}; It's good time to start quiz part.".format(age))


def count():
    print("Now, I'll show you that I'm able to count up to any number you want.")
    num = int(input())

    counter = 0
    while counter <= num:
        print("{0} !".format(counter))
        counter += 1


def test():
    print("Let's put your programming skills to the test.")
    print("#include <iostream>")
    print("int main() {")
    print("int x = 5;")
    print("int y = ++x * 5 / x--;")
    print("std::cout << x << " " << y << std::endl;")
    print("return 0;")
    print('}')

    answer = '4 6'
    guess = str(input())
    while guess != answer:
        print("Please, try again.")
        guess = int(input())

    print('🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉')
    print('Well Done!, Buddy...')
    print('🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊')


def end():
    print('.................................')
    print('Brilliant, Good Work Buddy....')
    print('.......BEST OF LUCK........')
    input()


greet('MSR', '2023')
remind_name()
guess_age()
count()
test()
end()
