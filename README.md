
---

# Draw Application

## Overview

The Draw Application is a simple program written in Python that allows users to:
- Add user names to a list.
- View the list of added users.
- Randomly shuffle the user list.
- Pick a random selection of users from the list.

The application continues running in a loop, allowing users to perform various actions until terminated manually.

## Features

1. **Add User**: Allows users to add a name to the list of participants.
2. **Show Users**: Displays all the users currently in the list.
3. **Shuffle Users**: Randomly shuffles the user list.
4. **Pick Random Users**: Selects a specified number of users randomly from the list.

## Functions

### `add_user(x)`
This function lets the user add a new participant by entering a name, which is then appended to the list of users.

**Parameters**: 
- `x`: The list of users where the name will be added.

### `show_user(x)`
This function displays the current list of users with an index number for each user.

**Parameters**: 
- `x`: The list of users to display.

### `pic(x)`
This function randomly selects a specified number of users from the list. The users are selected one at a time, with a delay between selections to simulate a drawing process.

**Parameters**: 
- `x`: The list of users from which random selections will be made.

### `shake(x)`
This function randomly shuffles the order of users in the list.

**Parameters**: 
- `x`: The list of users to be shuffled.

## Usage

1. Run the script.
2. The program will greet you with the following menu:
   ```
   1-Add User
   2-Show User
   3-Shake User
   4-Pic Random User
   ```
3. Choose an option:
   - `1`: Add a new user to the list.
   - `2`: View the list of users.
   - `3`: Shuffle the list of users randomly.
   - `4`: Randomly pick a certain number of users from the list.

4. After each action, the program will prompt you to press a button to continue.

## Example

```
***Welcome to Draw Application***
1-Add User
2-Show User
3-Shake User
4-Pic Random User
```

If you choose `1` (Add User):

```
------------------------------
Welcome to add user screen
Please enter a user name: John
İf you want to continiue press a button
------------------------------
```

If you choose `4` (Pick Random User):

```
------------------------------
Calculating how many person you want to pick
How man people do you want to pick: 2

1-User name: Sarah
Other user picking from the system...
(waiting for 3 seconds)
2-User name: Mike
------------------------------
```

## Requirements

- Python 3.x

## Notes

- The `pic()` function uses `random.sample()` to pick a number of users without duplicates.
- The `shake()` function shuffles the list of users using `random.shuffle()`.

---

