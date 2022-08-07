# AirBnB_clone - The Console
![Hbnb-img](./img/hbnb-image.png)

**Creation of a command interpreter to manage the hbnb ojects**

## Aims & Objective🌟
***At the end of this project we have been a able to manage the objects of our project:***
-   Creation of a new **object** (ex: `new User`, `new Place`).
-   Retrieval of an **object** from a file storage.
-   Perform operations on **objects** (ex: `count`, `show`, etc).
-   Update attributes of an **object**.
-   Destroy an **object**.

## Objects To be Created🌟
**The list of the objects that can be created are as follows:**
-   **BaseModel**
-   **User**
-   **City**
-   **Amenity**
-   **State**
-   **Review**
-   **Place**

## Commands Implemented🌟
***These are the commands implemented on the interpreter with their description as follows:***

|   **Command**     |       **Description**     |
|   -----------     |       ---------------     |
|   `quit`          |   This command exits the interpreter when used|
|   `EOF`           |   This command also exits interpreter when `ctrl + d` is pressed  |
|   `help`           |   This command helps to tell more about a command when used (Ex: `help quit`).   |
|   `create`           |   This command creates a new Instance of an Objects from the objects stated above (Ex: `create BaseModel` or `BaseModel.create()`)
|   `show`           |   This command shows string representation of an instance based on the class name and id (Ex: `show BaseModel 1234-1234-1234` or `BaseModel.show("1234-1234-1234")`)   |
|   `destroy`      |   This command Deletes an instance based on the class name and id (Ex: `destroy BaseModel 1234-1234-1234` or `BaseModel.destroy("1234-1234-1234")`).    |
|   `all`           |   This command Prints all string representation of all instances based or not on the class name (Ex: `all BaseModel` or `all` or `User.all()`).   |
|   `update`           |   This command Updates an instance based on the class name and id by adding or updating attribute (Usage: `update <class name> <id> <attribute name> "<attribute value>`). |
|   `count`           |   This command retrieves the number of instances of a class. (Usage: `<class name>.count()`, Example: `User.count()`).  |

## Compilation🌟
***To start up the interpreter, clone this repository to local*** <br>
**Run the `console` file on linux like this: `./console.py`**

## Examples🌟
***Here are some examples to guide you in the interpreter:***

```
tom-val@ubuntu:~/hBnB$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) quit
tom-val@ubuntu:~/hBnB$
```
## Authors
-   **Adebisi Oluwatomiwa**
-   **Valentine Maduagwu**
