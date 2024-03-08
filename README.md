# Console Application

This is a command interpreter to manage your application objects.

## Project Journey

This project was quite a challenge. Here's a fun representation of the journey:

![Hard Working Programmer](https://images.app.goo.gl/BcQNTwiqoV9e1t6h7)

And the feeling when it finally worked:

![Celebration GIF](https://images.app.goo.gl/R1jAkmrD8vRf46fW7)

## How to Use

1. Run the console.py file in your terminal: `python3 console.py`
2. You will be greeted with a prompt `(hbnb)`

## Commands

The console supports the following commands:

- `create <class>`: Creates a new instance of `<class>`, saves it to the JSON file, and prints the `id`.
- `show <class> <id>`: Prints the string representation of an instance based on the class name and `id`.
- `destroy <class> <id>`: Deletes an instance based on the class name and `id`.
- `all <class>` or `all`: Prints all string representation of all instances based on the class name. If no class name is provided, it prints all instances of all classes.
- `update <class> <id> <attribute name> "<attribute value>"`: Updates an instance based on the class name and `id` by adding or updating attribute.

## Example

```bash
$ python3 console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2022, 2, 23, 21, 30, 55, 987259), 'updated_at': datetime.datetime(2022, 2, 23, 21, 30, 55, 987259)}
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2022, 2, 23, 21, 30, 55, 987259), 'updated_at': datetime.datetime(2022, 2, 23, 21, 30, 55, 987259)}"]
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 name "John"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2022, 2, 23, 21, 30, 55, 987259), 'updated_at': datetime.datetime(2022, 2, 23, 21, 30, 55, 987259), 'name': 'John'}
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
[]
(hbnb) quit

## License

Copyright (c) [2024] [Yahia mostafa (satamony)]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## References

This project was built using the following resources:

- [Python Documentation](https://docs.python.org/3/)
- [PEP 8 -- Style Guide for Python Code](https://pep8.org/)
- [Markdown Guide](https://www.markdownguide.org/)

