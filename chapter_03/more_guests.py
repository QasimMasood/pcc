guest_list = ['Micheal Phelps', 'Serena Williams', 'Cristiano Ronaldo']
for guest in guest_list:
    print(f"{guest}, you're invited to dinner!")
print("Great news, found a bigger table!")
guest_list.insert(0, 'Tom Brady')
guest_list.insert(2, 'Muhammad Ali')
guest_list.append('Usain Bolt')
# Print a new set of invitations
for guest in guest_list:
    print(f"Hello {guest}! I would like to invite you to my dinner party.")