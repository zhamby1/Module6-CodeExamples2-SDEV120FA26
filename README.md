# Parallel Arrays
Often times what we want to do with data is create an association or relationship between data sets.  So far we have looked at arrays/lists to create data under one characterstic or umbrella with a single array (i.e a list of groceries, people, scores, etc...)

But what happens if you want to associate multiple items together that may be in separate lists or arrays.

For example, you have a list of names and a list of bank account balances.  Maybe I want to associate the balances with the names of individuals that own account.

Enter the parallel array/list

## How It Works
Parallel arrays/lists work by making sure that two or more lists/arrays are related by putting the related data at the same index

Example

```python
customers = ["Zach","Aly","Jimmy"]
bank_balances = [100.00,500.00,1000.00]
```
Basically this would allow me to loop or call the related data by the same position or index, which would allow me to keep the data related

Downside of parallel lists/arrays is that you must be sure not to get the indexes out of order, and that they contain the same number of elements.

## Searching Arrays Lists
Python has a built in feature for searching through lists.  It works by using the in keyword to find if something is in a list

Example

```python
find_name = "Zach"
party_people = ["Aly", "Sam", "Zach", "Jenny"]

if find_name in party_people:
    print("Found")

else:
    print("not found")
```

We use an if statement to see if some value in inside a list.  If it isn't in a list, the in keyword will return a false

## Serach and Replace
Maybe we to search and replace/update a value.  If we use the .index function we can find where that values index is so we can change it

```python
find_name = "Zach"
party_people = ["Aly", "Sam", "Zach", "Jenny"]

if find_name in party_people:
    print("Found")
    found_name_index = party_people.index(find_name)

    party_people[found_name_index] = input("Please update the list with a new name ")

else:
    print("not found")
```