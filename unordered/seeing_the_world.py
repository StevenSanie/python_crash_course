location = ['New York', 'London', 'Sillicon Valley']
print(f""" 
	\t {location} ~ Original Order
	\t {sorted(location)} ~ Sorted Order

	\t {location} ~ Original Order is still unchanged

	\t {sorted(location, reverse=True)} ~ Reversed Sorted List
	\t {sorted(location, reverse=False)} ~ The list is still unchanged
""")

location.sort()
print(f'\t\t {location} ~ Permanently Sorted')

location.sort(reverse=True)
print(f'\t\t {location} - Reversed Sorted')

print(location[5])