FILEPATH = 'todos.txt'
def get_todos(file_path = FILEPATH):
	"""Read a text file and return a list of to-do items."""
	with open(file_path, 'r') as file:
		local_todos = file.readlines()
	return local_todos

def write_todos(todo_arg, filepath = FILEPATH):
	"""Write the to-do items list in a text file. """
	with open(filepath, 'w') as file:
		file.writelines(todo_arg)

