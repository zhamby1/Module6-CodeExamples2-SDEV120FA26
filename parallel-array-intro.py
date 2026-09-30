#this example will use bank balances and names to relate data

#parallel lists

people = ["Aly","Zach","Tim"]
bank_balance = [1000.00,500.00,800.00]

#if you are displaying parallel lists, we usually have to use a more traditional for loop for this
#this is because we need the index piece to keep up with the poistioning of our multiple lists
#we will use a loop to grab each item in our multiple lists are their matching index and print them

#no which list we use to loop through doesn't matter.  Because they all should be the same length and the same positions

#we will create a loop_variable using for i in range (you can name i whatever you want to)
for i in range(len(people)):
    print(people[i], "has a balance of", bank_balance[i])