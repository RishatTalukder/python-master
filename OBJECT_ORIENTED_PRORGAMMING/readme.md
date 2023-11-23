# OBJECT ORIENTED PROGRAMMING or OOP

## What is OOP?

OOP is a programming `paradigm` that uses `objects` and their `interactions` to design applications and computer programs. 

It utilizes several techniques from previously established paradigms, including `modular`, `procedural`, and `prototype-based` programming. 

But `OOP` also introduces entirely new concepts that make programming more `flexible` and `modular` than ever before.

In OOP, `computer programs` are designed by making them out of `objects` that `interact` with one another. 

There is `significant overlap` between `OOP` and `modular programming`, since both approaches focus on `breaking down` `software` into `components`, or `modules`.

More specifically, `OOP` in `Python` is a `programming paradigm` that uses `classes` and `objects` to `design` and `build` `applications`. So it's a way to `structure` and `organize` code.

## What is a class?

A `class` is a `blueprint` for the `object`. We can think of `class` as an `idea` of a `car`. It doesn't exist in the real world, it's just an idea, a concept. 

in python we can create a `class` by using the `class` keyword. 

```python
class Car:
    pass
```

## What is an object?

An `object` is an `instance` of a `class`. When we talk about an `instance`, we talk about a `real car`. But it's not just any car, it's a `specific car`. 

So an `object` is an `instance` of a `class`. 

```python
class Car:
    pass

car_1 = Car() # car_1 is an object of Car class
car_2 = Car() # car_2 is an object of Car class

print(car_1) # <__main__.Car object at 0x7f9f1c1b6d90>
print(car_2) # <__main__.Car object at 0x7f9f1c1b6e50>
```

as you can see, `car_1` and `car_2` are `instances` of `Car` class. But we know that anything before `=` is a `variable`. So `car_1` and `car_2` are `variables` that are `instances` of `Car` class. 

* Basic terminology
    * `class` - a `blueprint` for an `object`
    * `object` - an `instance` of a `class`
    * `instantiate` - create an `instance` of a `class`
    * `method` - a `function` defined in a `class`
    * `attribute` - a `variable` bound to an `instance` of a `class`

## What is a method?

A `method` is a `function` that is `defined` inside a `class`. 

```python
class Car:
    def drive(self):
        print('driving')

car_1 = Car() # object of Car class
car_1.drive() # driving
```

to `call` a `method` we need to `call` it on an `object` of a `class`, in this case `car_1` and we have to use `.` operator to tell python that we want to `call` a `method` on an `object`.

after adding `()` to `drive` we are `calling` the `drive` method.

So if we want to `call` the `drive` method on `car_1` we have to write `car_1.drive()`.

## What is an attribute?

An `attribute` is a `variable` that is `bound` to an `instance` of a `class`. 

```python
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

car_1 = Car('red', 1000)
car_2 = Car('blue', 2000)

print(car_1.color) # red
print(car_2.color) # blue
```

Here we have a `class` called `Car` and it has a `method` called `__init__`. We'll talk about `__init__` later but for now can thing of it as a normal `method` which doesn't require us to `call` it. thats why we don't need the `.` operator to `call` it. But we do need to `call` it when we want to `create` an `object` of a `class`.

So we have `car_1` and `car_2` which are `objects` of `Car` class. And we are `passing` `red` and `1000` to `car_1` and `blue` and `2000` to `car_2`. 

So `car_1` has `red` and `1000` as `attributes` and `car_2` has `blue` and `2000` as `attributes`.

So `color` and `mileage` are `attributes` of `Car` class.

So, by the difinition of `attribute`, `color` and `mileage` are `variables` that are `bound` to an `instance` of a `class`. Everytime we use that object, we can access those `variables` or `attributes`.

## What is self?

`self` is a `reference` to the `current instance` of the `class`. 

```python
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

car_1 = Car('red', 1000)
car_2 = Car('blue', 2000)

print(car_1.color) # red
print(car_2.color) # blue
```

So, in every `method` of a `class` we have to `pass` `self` as the `first argument`. 

So, in `__init__` method, `self` is a `reference` to the `current instance` of the `class`. Meaning in the `object` `car_1`, `self` is a `reference` to `car_1` and in the `object` `car_2`, `self` is a `reference` to `car_2`. Thats why we can `access` `color` and `mileage` `attributes` of `car_1` and `car_2` by using `self.color` and `self.mileage`. This is how we `access` `attributes` of an `object` in a `class`.

## What is __init__?

`__init__` is a `special method` that is `called` when we `create` an `object` of a `class`. 

```python
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

car_1 = Car('red', 1000)
print(car_1.color) # red
```

it is also called a `constructor` method or a `dunder` method. `dunder` means `double underscore`. There are many `dunder` methods in python. 

`__init__` is a `dunder` method that is `called` when we `create` an `object` of a `class`. 

Its like starting a `car`. When we start a `car`, we have to `pass` some `arguments` to it. Like `color` and `mileage`. So when we `create` an `object` of a `class`, we have to `pass` some `arguments` to it. And `__init__` is the `method` that `receives` those `arguments`.

So, when we make the `object` `car_1`, we `pass` `red` and `1000` to it. And `__init__` `receives` those `arguments` and `assigns` them to `self.color` and `self.mileage`. 

We will refer to this `method` as `constructor` method from now on.

Constructor is a `method` that is `called` when we `create` an `object` of a `class` automatically.

# OOP Pillars

## What are the four pillars of OOP?

* `Encapsulation`
* `Abstraction`
* `Inheritance`
* `Polymorphism`

## What is encapsulation?

`Encapsulation` is the `mechanism` of `hiding` `data` and `methods` from `outside` `world`. 

```python
# Enough with the car example, lets use a real world example
class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = max(price, 0) # _price is a private variable
        # we can use _price to hide the price from outside world

    def make_a_call(self, phone_number):
        print(f'calling {phone_number}...')

    def full_name(self):
        return f'{self.brand} {self.model}'
```

Here we have a `class` called `Phone`. It has `attributes` like `brand`, `model` and `_price`.

`brand` and `model` are `public` `attributes` and `_price` is a `private` `attribute`.

> `_price` is a `private` `attribute` because it has a `_` before it. this is the way we tell python that this is a `private` `attribute`.

`public` `attributes` are `accessible` from `outside` `world` and `private` `attributes` are `not accessible` from `outside` `world`.

So, we can `access` `brand` and `model` from `outside` `world` but we can't `access` `_price` from `outside` `world`.

```python
.....
phone_1 = Phone('nokia', '1100', 1000)
print(phone_1.brand) # nokia
print(phone_1.model) # 1100
print(phone_1._price) # error
```

So, we can `access` `brand` and `model` from `outside` `world` but we can't `access` `_price` from `outside` `world`. 

```python
phone_1 = Phone('nokia', '1100', 1000)
phone.brand = 'samsung'
phone.model = 's20'
phone._price = 1000000 # error
```

So, there is no way to `access` `_price` from `outside` `world`, So, we need to figure out a way to `access` `_price` from `outside` `world`.

```python
class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = max(price, 0) # _price is a private variable
        # we can use _price to hide the price from outside world

    def make_a_call(self, phone_number):
        print(f'calling {phone_number}...')

    def full_name(self):
        return f'{self.brand} {self.model}'

    # getter method
    def get_price(self):
        return self._price

    # setter method
    def set_price(self, new_price):
        self._price = max(new_price, 0)
```

Here we have `getter` and `setter` `methods` for `_price`. getter `method` is used to `get` the `value` of `_price` and setter `method` is used to `set` the `value` of `_price`. 

```python
.....
phone_1 = Phone('nokia', '1100', 1000)
print(phone_1.get_price()) # 1000
phone_1.set_price(500)
print(phone_1.get_price()) # 500
```

So now, we can easily `access` `_price` from `outside` `world` by using `getter` `method` and we can `set` `_price` from `outside` `world` by using `setter` `method`.

Getter and setter `methods` are used to `access` `private` `attributes` from `outside` `world`. They are also called `accessor` and `mutator` `methods` and In `Encapsulation` we use `getter` and `setter` `methods` to `access` `private` `attributes` from `outside` `world`.

SO `Encapsulation` is the `mechanism` of `hiding` `data` and `methods` from `outside` `world` and the way we `get` and `set` `private` `attributes` from `outside` `world` is by using `getter` and `setter` `methods`.

## What is abstraction?

`Abstraction` is the `mechanism` of `hiding` `implementation` `details` from `outside` `world`. 

```python



