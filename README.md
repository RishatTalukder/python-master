# python tips and tricks

Just wanted give my viewers some tips in becomming a python pro

## What should i start with?

Got it..

# LEARN THE BASICS OF PYTHON

Now that you have learned the basics of python, you can start learning the tips and tricks of python.

BTW you can learn the basics of python [here](https://www.youtube.com/watch?v=XKHEtdqhLK8&t=8400s)

now, time for tips and tricks

# TIPS AND TRICKS

Not every code you write has to be long and complicated, you can shorten it and make it easier to read. This is called `pythonic` code. In a `pythonic` code we follow some rules to make our code shorter and easier to read.

## 1. Use the `in` keyword to check if a value is in a list

```python
# Example of basic logic to check if a value is in a list
for i in ["hello", "world"]:
    if i == "hello":
        print("hello is in the list")


# Example of using the in keyword to check if a value is in a list
if "hello" in ["hello", "world"]:
    print("hello is in the list")
```

this shortens the code and makes it easier to read. No need to use a for loop to check if a value is in a list.

## 2. Use the `is` and `is not` keyword to check if a value is equal or not equal to another value

```python
# Example of basic logic to check if a value is equal to another value
name = "ITVAYA"
if name == "ITVAYA":
    print("1 is equal to 1")


# Example of basic logic to check if a value is not equal to another value
name = "ITVAYA"
if name != "ITVAYA":
    print("1 is not equal to 1")




# Example of using the is keyword to check if a value is equal to another value
name = "ITVAYA"
if name is "ITVAYA":
    print("1 is equal to 1")

# Example of using the is not keyword to check if a value is not equal to another value
name = "ITVAYA"
if name is not "ITVAYA":
    print("1 is not equal to 1")
```

## 3. Use the `and` keyword to check if two conditions are true

```python
# Example of basic logic to check if two conditions are true
name = "ITVAYA"
age = 13
if name == "ITVAYA":
    if age == 13:
        print("name is ITVAYA and age is 13")


# Example of using the and keyword to check if two conditions are true
name = "ITVAYA"
age = 13
if name == "ITVAYA" and age == 13:
    print("name is ITVAYA and age is 13")
```

preventing nesting is a good way to make your code shorter and easier to read. No need to use a nested if statement to check if two conditions are true.

so using keywords like `in`, `is`, `is not`, and `and` can make your code shorter and easier to read if you use them correctly and in a smart way.

the are other ways to make your code shorter and easier to read, like using list comprehension, dictionary comprehension, and lambda functions.

## 4. Use list comprehension to create a list

```python
# Example of basic logic to create a list
my_list = []
for i in range(10):
    my_list.append(i)
print(my_list,)


# Example of using list comprehension to create a list
my_list = [i for i in range(10)]
print(my_list)
```


there are some more tips for lists 

## 5. Use the `*` operator to unpack a list

```python
# Example of basic logic to unpack a list
my_list = [1, 2, 3, 4, 5]
print(my_list[0], my_list[1], my_list[2], my_list[3], my_list[4])


# Example of using the * operator to unpack a list
my_list = [1, 2, 3, 4, 5]
print(*my_list)
```

## 6. Use the `zip` function to zip two lists together

```python
# Example of basic logic to zip two lists together
my_list = [1, 2, 3, 4, 5]
my_list2 = ["hello", "world", "python", "is", "cool"]
for i in range(len(my_list)):
    print(my_list[i], my_list2[i])


# Example of using the zip function to zip two lists together
my_list = [1, 2, 3, 4, 5]
my_list2 = ["hello", "world", "python", "is", "cool"]
for i, j in zip(my_list, my_list2):
    print(i, j)
```

## 7. Use the `enumerate` function to get the index of an item in a list

```python
# Example of basic logic to get the index of an item in a list
my_list = ["hello", "world", "python", "is", "cool"]
for i in range(len(my_list)):
    print(i, my_list[i])


# Example of using the enumerate function to get the index of an item in a list
my_list = ["hello", "world", "python", "is", "cool"]
for i, j in enumerate(my_list):
    print(i, j)
```

## 8. Use the `map` function to apply a function to every item in a list

```python
# Example of basic logic to apply a function to every item in a list
my_list = [1, 2, 3, 4, 5]
for i in range(len(my_list)):
    my_list[i] = my_list[i] * 2
print(my_list)


# Example of using the map function to apply a function to every item in a list
my_list = [1, 2, 3, 4, 5]
my_list = list(map(lambda x: x * 2, my_list))
print(my_list)
```

## 9. Use the `filter` function to filter a list

```python
# Example of basic logic to filter a list
my_list = [1, 2, 3, 4, 5]
new_list = []
for i in my_list:
    if i % 2 == 0:
        new_list.append(i)
print(new_list)


# Example of using the filter function to filter a list
my_list = [1, 2, 3, 4, 5]
new_list = list(filter(lambda x: x % 2 == 0, my_list))
print(new_list)
```

## 10. Use the `all` function to check if all items in a list are true

```python
# Example of basic logic to check if all items in a list are true
my_list = [True, True, True, True, True]
for i in my_list:
    if i == False:
        print("not all items are true")
        break
else:
    print("all items are true")


# Example of using the all function to check if all items in a list are true
my_list = [True, True, True, True, True]
if all(my_list):
    print("all items are true")
else:
    print("not all items are true")
```

## 11. Use the `any` function to check if any item in a list is true

```python
# Example of basic logic to check if any item in a list is true
my_list = [False, False, False, False, True]
for i in my_list:
    if i == True:
        print("at least one item is true")
        break
else:
    print("no items are true")


# Example of using the any function to check if any item in a list is true
my_list = [False, False, False, False, True]
if any(my_list):
    print("at least one item is true")
else:
    print("no items are true")
```
