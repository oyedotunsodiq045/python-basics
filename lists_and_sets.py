available_apples = ['cox', 'royal blue', 'pink lady']

available_apples.append('red stallion')

available_apples.remove('royal blue')

new_apples = ['grey hound', 'royal blue', 'cox', 'pink lady']

available_apples.extend(new_apples)

unique_apples = set(available_apples)

available_apples = list(unique_apples)

print(available_apples)
