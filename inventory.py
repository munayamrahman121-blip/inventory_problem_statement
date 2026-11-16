LOW_STOCK = 5
UPDATE_FIELDS = {"price", "stock"}

PAYMENT_WAYS = {"bkash", "cash", "card", "nagad"}
ALLOWED_VOUCHER = {"EID10": 10, "NEW5": 5}

# maintain a previous stock
inventory = {
	"Panjabi": {"price": 1000, "stock": 15, "category": "Men"},
	"Scarf": {"price": 400, "stock": 10, "category": "Women"},
	"Cotton Kurti": {"price": 850, "stock": 8, "category": "Women"},
	"Hat": {"price": 500, "stock": 0, "category": "Universal"}
}


while True:
	print("INVENTORY MGMT SYSTEM")
	print("1. Add Item")
	print("2. View all items")
	print("3. Update item")
	print("4. Delete item")
	print("5. Sell") # this is for you guys to complete.
	print("q. Exit")

	choice = input("Choose any one: ").strip().lower()

	if choice == "1":
		name = input("item name: ").strip().title()
		if not name:
			print("Name can not be empty")
		elif name in inventory:
			print("Item already exists, go to [3] to update it.")
		else:
			price_text = input("price (in BDT): ").strip()
			stock_text = input("stock / quantity: ").strip()
			category = input("category: ").strip()

			if not price_text.isdigit() or int(price_text) == 0:
				print("Price must be a number and must be positive")
			elif not stock_text.isdigit():
				print("Stock must be a whole digit")
			elif not category:
				print("Category cannot be empty")
			else:
				inventory[name] = {
					"price": int(price_text),
					"stock": int(stock_text),
					"category": category
				}
				print(f"Added new product {name}, quantity: {stock_text}")

	elif choice == "2":
		if not inventory:
			print("Inventory is empty")
		else:
			print(f"{'Item':<16}{'Category':<14}{'Price':>8}{'Stock':>6}")
			for item, details in inventory.items():
				note = ""
				if details["stock"] == 0:
					note += "  OUT OF STOCK"
				elif details["stock"] <= LOW_STOCK:
					note += "  low"
				print(f"{item:<16}{details["category"]:<14}{details["price"]:<8}{details["stock"]:>6}{note}")
	
	elif choice == "3":
		name = input("Item name to update (exact):").strip().title()

		if name not in inventory:
			print("No such item exists in the inventory")
		else:
			field = input("update which one (price/stock): ").strip().lower()
			if field not in UPDATE_FIELDS:
				print("Only price or stock can be updated")
			else:
				value = input(f"New {field}: ").strip()

				if not value.isdigit() or int(value) == 0:
					print(f"Enter valid {field} - must be a number")
				else:
					inventory[name][field] = int(value)
					
					print(f"{name} item's {field} is now: {inventory[name][field]}")

	elif choice == "4":
		name = input("Which item to delete: ").strip().title()
		if name not in inventory:
			print("Item doesn't exists to remove.")
		else:
			confirmation = input(f"Delete {name} (yes/no): ")
			if confirmation == "yes":
				inventory.pop(name)
				print(f"{name} deleted!")
			else:
				print("Cancelled.")
	elif choice == "q":
		print("Thank you, goodbye.")
		break
	else:
		print("Invalid choice, enter 1-5 or 'q' to exit")