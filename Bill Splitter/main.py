import random

dict_length = int(input("Enter the number of friends joining (including you):\n"))
if dict_length <= 0:
    print("\nNo one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = [input("> ") for _ in range(dict_length)]
    bill_value = float(input("Enter the total bill value:\n"))
    lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if lucky.lower() == "yes":
        lucky_friend = random.choice(friends)
        print(f"{lucky_friend} is the lucky one!")


        friends_dict = {friend: 0 for friend in friends}
        remaining_bill = bill_value - friends_dict[lucky_friend]
        split_value = round(remaining_bill / (dict_length - 1), 2)


        for friend in friends_dict:
            if friend != lucky_friend:
                friends_dict[friend] = split_value
    else:

        friends_dict = {friend: round(bill_value / dict_length, 2) for friend in friends}
        print("No one is going to be lucky")

    print(friends_dict)
