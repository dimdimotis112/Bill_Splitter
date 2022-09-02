import random

print("Enter the number of friends joining (including you): ")
people = int(input())
print()

friends = {}

if people <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(people):
        friend = input()
        friends[friend] = 0
    print()
    print("Enter the total bill value:")
    bill_amount = int(input())

    print()

    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No: ")
    answer = input()
    lucky_one = None
    print()

    if answer == 'Yes':
        lucky_one = random.choice(list(friends.keys()))
        print(f"{lucky_one} is the lucky one!")
        divided_bill = round(bill_amount / (people - 1), 2)
    else:
        print("No one is going to be lucky")
        divided_bill = round(bill_amount / people, 2)

    for k in friends.keys():
        if k == lucky_one:
            friends[k] = 0
        else:
            friends[k] = divided_bill

    print(friends)
