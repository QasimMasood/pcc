guest_list = ['Micheal Phelps', 'Serena Williams', 'Cristiano Ronaldo']

for guest in guest_list:
    print(f"Hello, {guest}, I would like to invite you to dinner.")

print(f"{guest_list[2]} has a match tonight and won't be able to make it.")
guest_list.remove('Cristiano Ronaldo')
guest_list.append('LeBron James')

for guest in guest_list:
    print(f"Hello, {guest}, I would like to invite you to dinner.")