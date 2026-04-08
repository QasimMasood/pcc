mountains = ['Everest', 'K2', 'Kangchenjunga', 'Lhotse', 'Makalu']

print(mountains)

# Print only the 2nd element in the list above
print(mountains[2])

# Use case methods on the 3rd element in the list above
print(mountains[2].title())
print(mountains[2].upper())
print(mountains[2].lower())

# Print your favorite mountain from the list, assign the statement to a variable and print the variable
message = f"My favorite mountain is Mount {mountains[0]}."
print(message)

# Add a new mountain as the last element in the list
mountains.append('Kilimanjaro')
print(mountains)

# Insert in another mountain at the 1st index in the list of mountains
mountains.insert(1, 'Denali')
print(mountains)

# Remove the mountains at the 3rd index in the current list
del mountains[3]
print(mountains)

# Use the pop() method to shrink the list to 3 items
popped_mountains1 = mountains.pop()
popped_mountains2 = mountains.pop()
popped_mountains3 = mountains.pop()
print(mountains)

# Print the popped items
print (f"The mountains that I want to visit the least are: {popped_mountains1}, {popped_mountains2}, and {popped_mountains3}.")

# Alphabetically sort current list without permanently changing the order of the list
print(f"Alphabetical order: {sorted(mountains)}")

# Reverse the order of the list permanently
mountains.reverse()
print(mountains)

# Remove a mountain by value
mountains.remove('K2')
print(mountains)

# Reverse alphabetical order sort permanently
mountains.sort(reverse=True)
print(mountains)

# Print the size of the current list
print(f"There are {len(mountains)} mountains that I have yet to visit.")