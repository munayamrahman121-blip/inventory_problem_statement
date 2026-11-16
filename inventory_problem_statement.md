# Shop Manager: Problem Statement

A console program in Python, built with loops, conditions and the data structures learnt so far (dictionary, set, tuple, list).

---

## 1. Problem Statement

> *"I sell clothes from my shop and my Facebook page. I keep my stock in a notebook, so I often promise customers items that are already sold out, and I forget which items are almost finished. I want a simple program with a menu. I should be able to add new items, view everything in stock, change an item's price or stock, and delete an item I no longer sell. Selling should work like a real counter. I enter the customer's name and add items one at a time. If I add the same item twice, it should become one line on the bill. I should be able to check what is still available, or cancel the whole sale if the customer changes their mind. The customer can use a discount code and pays by cash, bKash, Nagad or card. For cash, the program tells me the change. The moment the sale is finished, I want one clear report of that sale, with a warning for any item that is now low or sold out. Then it should go back to the menu."*

### Problem at a Glance

| Aspect | Description |
|---|---|
| Who uses it | A shop owner or cashier at the counter |
| Current problem | Stock is tracked on paper, so items get oversold and low stock is missed |
| Goal | Manage items and sell them safely, with a clear report after every sale |
| Input | Menu choices, item details, customer name, quantities, discount code, payment details |
| Output | Item table, sale report, warnings and error messages |
| Data kept | Item list with price, stock and category (kept only while the program runs) |
| Out of scope | Saving data to files, daily or monthly reports, refunds after payment |

---

## 2. Menu Items

| Key | Menu item | What it does |
|---|---|---|
| `1` | Add item | Adds a new item with price, stock and category |
| `2` | View all items | Shows every item in a table, with low and out-of-stock notes |
| `3` | Update item | Changes the price or the stock of an existing item |
| `4` | Delete item | Removes an item after a yes or no confirmation |
| `5` | Sell items | Runs a full sale and ends with a sale report |
| `q` | Exit | Closes the program |

Any other key shows: `Invalid choice. Enter 1-5 or q.`

---

## 3. Requirements

### 3.1 Item Data

| Field | Rule |
|---|---|
| Name | Required and unique. Any letter case or extra spaces finds the same item (`" cotton kurti "` is `Cotton Kurti`) |
| Price | Positive whole number (taka) |
| Stock | Whole number, 0 or more |
| Category | Required |

### 3.2 Item Rules (Options 1 to 4)

| # | Option | Requirement |
|---|---|---|
| I1 | Add | Reject an empty name, and reject a name that already exists |
| I2 | Add | Reject a price that is not a positive whole number, a stock that is not a whole number, and an empty category |
| I3 | View | Show item, category, price and stock in a table |
| I4 | View | Show `low` next to items with 5 or fewer in stock, and `OUT OF STOCK` next to items with 0 |
| I5 | View | If there are no items, say `Inventory is empty.` |
| I6 | Update | Only an existing item can be updated, and only `price` or `stock` can be changed |
| I7 | Update | The new value must be a whole number (a price cannot be 0) |
| I8 | Delete | Only an existing item can be deleted, and the program must ask `yes` or `no` first |

### 3.3 General Requirements

| # | Requirement |
|---|---|
| G1 | The menu repeats until the user chooses `q` |
| G2 | The program must not crash on empty or wrong input |
| G3 | Every error message tells the user what to do next |
| G4 | Low stock limit is 5 units |

---

## 4. Selling (Option 5)

### 4.1 Selling Rules

| # | Rule |
|---|---|
| S1 | Ask for the customer's name. If left empty, use `Walk-In` |
| S2 | Items are added one at a time, each with a quantity |
| S3 | Adding the same item again **merges** into one line on the bill |
| S4 | Quantity must be a positive whole number |
| S5 | Quantity cannot be more than what is **available**, which is the stock minus what is already on this bill |
| S6 | An item with nothing available cannot be added, and the user is told it is out of stock |
| S7 | An item name that does not exist is rejected with a hint to type `list` |
| S8 | Typing `cancel` abandons the sale, and stock stays exactly as it was |
| S9 | Typing `done` with nothing on the bill gives `Nothing sold.` |
| S10 | Stock is reduced **only after payment is confirmed** |
| S11 | The sale ends with one sale report, then the program returns straight to the menu |

### 4.2 Commands While Adding Items

| Type this | What happens |
|---|---|
| An item name | Asks for a quantity, then adds it to the bill |
| `list` | Shows every item with its price and how many are still available for this sale |
| `cancel` | Abandons the sale, with no change to stock |
| `done` | Finishes adding items and moves on to the discount and payment |

### 4.3 Sale Flow

| Step | What happens | Stock changed? |
|---|---|---|
| 1 | Enter the customer name | No |
| 2 | Add items to the bill (with `list`, `cancel` and `done` available) | No |
| 3 | Subtotal is calculated from the bill | No |
| 4 | Optional discount code is applied | No |
| 5 | Payment method is chosen. For cash, the amount received must cover the total and the change is calculated | No |
| 6 | Stock is reduced for every item on the bill | **Yes** |
| 7 | Sale report is printed, with warnings for low and out-of-stock items | No |
| 8 | Return to the menu | No |

### 4.4 Discount Codes

| Code | Discount |
|---|---|
| `EID10` | 10% off the subtotal |
| `NEW5` | 5% off the subtotal |
| (empty) | No discount |
| Anything else | `Invalid code, no discount applied.` and the sale continues |

Discount amounts are rounded down to a whole taka.

### 4.5 Payment

| Method | Rule |
|---|---|
| `cash` | Ask for the cash received. It must be a whole number at least equal to the total. Change = received minus total |
| `bkash` | Paid exactly the total, change is 0 |
| `nagad` | Paid exactly the total, change is 0 |
| `card` | Paid exactly the total, change is 0 |
| Anything else | Ask again, showing the allowed methods |

### 4.6 Sale Report Contents

| Section | Content |
|---|---|
| Customer | The customer's name, or `Walk-In` |
| Item lines | Item, quantity, price and amount for each merged line |
| Subtotal | Sum of all line amounts |
| Discount | Shown only if a valid code was used (negative amount, with the code) |
| Total | Subtotal minus discount |
| Paid | Amount paid and the payment method |
| Change | Paid minus total |
| Out of stock | Items whose stock is now 0 (shown only if there are any) |
| Low stock | Items whose stock is now 1 to 5 (shown only if there are any) |

### 4.7 Sample Sale Report

```
SALE REPORT
Customer : Nadia
Item             Qty   Price   Amount
Cotton Kurti       5    1200     6000
Panjabi            1    1800     1800
Subtotal                         7800
Discount (EID10)                 -780
Total                            7020
Paid (bkash)                     7020
Change                              0
Low stock   : Cotton Kurti, Panjabi
```
