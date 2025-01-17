# Lab | Vikings (lab-data-vikings)

## Introduction

The Vikings and the Saxons are at War. Both are Soldiers but they have their own methods to fight. Vikings are ported to Python. YAY!!

In this laboratory you will work with the concept of inheritance in Python.

### Getting Started

You will find the following files in the folder of this laboratory:

- `vikings_clases.py`
- `tests.py`

You are free to use any of the code editors you have to open these files.

### Challenge Question

Modify the file `vikings_clases.py` so that all the tests are correct.

## Submission

- Modify `vikings_clases.py` and save your changes.

```
git add .
git commit -m "done"
git push origin lab-data-vikings
```

- Navigate to your repo and [create a Pull Request](https://help.github.com/articles/creating-a-pull-request/)

## Tests

Best way to know how our code is doing is to work with tests. To test the `vikings_clases.py` file step by step you can comment and uncomment lines of code of `tests.py`.

To run the battery of tests you must enter the following command line through the terminal.

```
% > python3 <FILE-NAME>.py -v
```

To run a single test you must enter the following command line through the terminal.

```
% > python3 <FILE-NAME>.py -v -k <TEST-NAME>
```

### Correct Test

When the tests are all correct you will receive the following message in the terminal.

```
% > python3 tests.py -v

testSaxon (__main__.MyTest) ... ok
testSoldier (__main__.MyTest) ... ok
testViking (__main__.MyTest) ... ok
testWar (__main__.MyTest) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

### Failed Test

When any test is incorrect you will receive the following message in the terminal. It means that you must keep making changes in the `vikings_clases.py` file.

```
$ > python3 tests.py -v

testSaxon (__main__.MyTest) ... FAIL
testSoldier (__main__.MyTest) ... ok
testViking (__main__.MyTest) ... ok
testWar (__main__.MyTest) ... ok

======================================================================
FAIL: testSaxon (__main__.MyTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests.py", line 53, in testSaxon
    self.assertEqual(len(signature(Saxon).parameters), 2)
AssertionError: 3 != 2

----------------------------------------------------------------------
Ran 4 tests in 0.002s

FAILED (failures=1)
```

## Exercise

![](https://i.imgur.com/5TPElt8.jpg)

---

**Write the code**

Now we have to write the correct code in the `vikings_clases.py` file to make the test pass. The starter code you will find in the file is the following:

```
# Soldier
class Soldier:

# Viking
class Viking:

# Saxon
class Saxon:

# War
class War:
```

In this case, the test says that _Soldier constructor function should receive 2 arguments (health & strength)_, so we have to write the correct code that passes this test. Let's make the `Soldier` constructor function receive two arguments:

```
# Soldier
class Soldier:
    def __init__(self, health, strength):
        # add code here

# Viking
class Viking:

# Saxon
class Saxon:

# War
class War:

```

### Soldier

Modify the `Soldier` constructor function and add 2 methods to its prototype: `attack()`, and `receive_damage()`.

#### constructor function

- should receive **2 arguments** (health & strength)
- should receive the **`health` property** as its **1st argument**
- should receive the **`strength` property** as its **2nd argument**

#### `attack()` method

- should be a function
- should receive **0 arguments**
- should return **the `strength` property of the `Soldier`**

#### `receive_damage()` method

- should be a function
- should receive **1 argument** (the damage)
- should remove the received damage from the `health` property
- **shouldn't return** anything

---

### Viking

A `Viking` is a `Soldier` with an additional property, their `name`. They also have a different `receive_damage()` method and new method, `battle_cry()`.

Modify the `Viking` constructor function, have it inherit from `Soldier`, reimplement the `receive_damage()` method for `Viking`, and add a new `battle_cry()` method.

#### inheritance

- `Viking` should inherit from `Soldier`

#### constructor function

- should receive **3 arguments** (name, health & strength)
- should receive the **`name` property** as its **1st argument**
- should receive the **`health` property** as its **2nd argument**
- should receive the **`strength` property** as its **3rd argument**

#### `attack()` method

(This method should be **inherited** from `Soldier`, no need to reimplement it.)

- should be a function
- should receive **0 arguments**
- should return **the `strength` property of the `Viking`**

#### `receive_damage()` method

(This method needs to be **reimplemented** for `Viking` because the `Viking` version needs to have different return values.)

- should be a function
- should receive **1 argument** (the damage)
- should remove the received damage from the `health` property
- **if the `Viking` is still alive**, it should return **"NAME has received DAMAGE points of damage"**
- **if the `Viking` dies**, it should return **"NAME has died in act of combat"**

#### `battle_cry()` method

[Learn more about battle cries](http://www.artofmanliness.com/2015/06/08/battle-cries/).

- should be a function
- should receive **0 arguments**
- should return **"Odin Owns You All!"**

---

### Saxon

A `Saxon` is a weaker kind of `Soldier`. Unlike a `Viking`, a `Saxon` has no name. Their `receive_damage()` method will also be different than the original `Soldier` version.

Modify the `Saxon`, constructor function, have it inherit from `Soldier` and reimplement the `receive_damage()` method for `Saxon`.

#### inheritance

- `Saxon` should inherit from `Soldier`

#### constructor function

- should receive **2 arguments** (health & strength)
- should receive the **`health` property** as its **1st argument**
- should receive the **`strength` property** as its **2nd argument**

#### `attack()` method

(This method should be **inherited** from `Soldier`, no need to reimplement it.)

- should be a function
- should receive **0 arguments**
- should return **the `strength` property of the `Saxon`**

#### `receive_damage()` method

(This method needs to be **reimplemented** for `Saxon` because the `Saxon` version needs to have different return values.)

- should be a function
- should receive **1 argument** (the damage)
- should remove the received damage from the `health` property
- **if the Saxon is still alive**, it should return _**"A Saxon has received DAMAGE points of damage"**_
- **if the Saxon dies**, it should return _**"A Saxon has died in combat"**_

---

### (BONUS) War

Now we get to the good stuff: WAR! Our `War` constructor function will allow us to have a `Viking` army and a `Saxon` army that battle each other.

Modify the `War` constructor and add 5 methods to its prototype:

- `add_viking()`
- `add_saxon()`
- `viking_attack()`
- `saxon_attack()`
- `show_status()`

#### constructor function

When we first create a `War`, the armies should be empty. We will add soldiers to the armies later.

- should receive **0 arguments**
- should assign an empty list to the **`vikingArmy` property**
- should assign an empty list to the **`saxonArmy` property**

#### `add_viking()` method

Adds 1 `Viking` to the `vikingArmy`. If you want a 10 `Viking` army, you need to call this 10 times.

- should be a function
- should receive **1 argument** (a `Viking` object)
- should add the received `Viking` to the army
- **shouldn't return** anything

#### `add_saxon()` method

The `Saxon` version of `addViking()`.

- should be a function
- should receive **1 argument** (a `Saxon` object)
- should add the received `Saxon` to the army
- **shouldn't return** anything

#### `viking_attack()` method

A `Saxon` (chosen at random) has their `receive_damage()` method called with the damage equal to the `strength` of a `Viking` (also chosen at random). This should only perform a single attack and the `Saxon` doesn't get to attack back.

- should be a function
- should receive **0 arguments**
- should make a `Saxon` `receive_damage()` equal to the `strength` of a `Viking`
- should remove dead saxons from the army
- should return **result of calling `receive_damage()` of a `Saxon`** with the `strength` of a `Viking`

#### `saxon_attack()` method

The `Saxon` version of `viking_attack()`. A `Viking` receives the damage equal to the `strength` of a `Saxon`.

- should be a function
- should receive **0 arguments**
- should make a `Viking` `receive_damage()` equal to the `strength` of a `Saxon`
- should remove dead vikings from the army
- should return **result of calling `receive_damage()` of a `Viking`** with the `strength` of a `Saxon`

#### `show_status()` method

Returns the current status of the `War` based on the size of the armies.

- should be a function
- should receive **0 arguments**
- **if the `Saxon` list is empty**, should return _**"Vikings have won the war of the century!"**_
- **if the `Viking` list is empty**, should return _**"Saxons have fought for their lives and survive another day..."**_
- **if there are at least 1 `Viking` and 1 `Saxon`**, should return _**"Vikings and Saxons are still in the thick of battle."**_

## Deliverables

- REQUIRED: `vikings_clases.py` modified with your solution to the challenge question.

## Resources

- https://docs.python.org/3/library/unittest.html
- https://www.python-course.eu/python3_inheritance.php

## Additional Challenge for the Nerds

You can try to make your own tests for your code by creating another test file.
