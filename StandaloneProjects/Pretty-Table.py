from prettytable import PrettyTable

# Create a table
table = PrettyTable()


# Fill the Table
table.add_column('Pokemon', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])


# Customize Table Elements
table.align = 'l'

# Print Table
print(table.align)
print(table)
