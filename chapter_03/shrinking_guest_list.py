guest_list = ['Micheal Phelps', 'Serena Williams', 'Cristiano Ronaldo']
guest_list.insert(0, 'Muhammad Ali')
guest_list.insert(2, 'Tom Brady')
guest_list.append('Usain Bolt')
for guest in guest_list:
    print(f"{guest}, you are invited to my dinner party!")
print('Oh no, I only have space for 2 people.')

popped_guest_list = guest_list.pop()
print(f"Sorry {popped_guest_list}, your ivitation has been revoked.")

popped_guest_list = guest_list.pop()
print(f"Sorry {popped_guest_list}, your ivitation has been revoked.")

popped_guest_list = guest_list.pop()
print(f"Sorry {popped_guest_list}, your ivitation has been revoked.")

popped_guest_list = guest_list.pop()
print(f"Sorry {popped_guest_list}, your ivitation has been revoked.")

for guest in guest_list:
    print(f"{guest}, you are still invited to dinner!")

del guest_list[0]
del guest_list[0]
print(guest_list)