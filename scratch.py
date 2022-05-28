with open(inventory_commands.txt) as file:
    inventorycommands = file.readlines()
    inventorycommands = [line.rstrip() for line in lines]
