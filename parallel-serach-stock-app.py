#serach and modify a parallel array
#this will be a product inventory app
#we will have a list of product ids, names, prices, and stock quantity
product_ids = ["P001","P002","P003"]
product_names = ["Laptop","Mouse","Keyboard"]
product_prices = [1200.00,22.99,15.00]
product_stock = [10,50,25]

search_id = input("Please enter the product ID you wish to lookup ")

#we will use a loop and the break statement for this to keep going until your are done
while True:
    if search_id in product_ids:
        #is the product id in the list
        #this will serach the list for the value and grabs it index
        index = product_ids.index(search_id)
        print("Here is your product deatils:")
        print("**********************")
        print("Name -", product_names[index])
        print("Price -", product_prices[index])
        print("Stock -", product_stock[index])
        print("***********************")

        buying_qty = int(input("Please enter the amount of the product you wish to buy "))
        #change the stock amount of the item they searched by using the index
        product_stock[index] = product_stock[index] - buying_qty
        print("Your new stock amount is", product_stock[index])

        break

    else:
        print("Product Not Found")
        search_id = input("Please enter a valid product ID again to find a match ")

print("Here is an updated list of names, prices, and stock quantity")

for i in range(len(product_ids)):
    print(product_names[i], product_prices[i], product_stock[i])