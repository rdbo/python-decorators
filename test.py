class MyApp:
	def route(self, path, **args):
		def decorator(func):
			print(args)
			return func()
		return decorator

	def deco(self, func):
		return func()

app = MyApp()

@app.route("/", methods=["GET", "POST"])
def my_function():
	print("function called")

"""
Explanation:
app.route is called and returns the function 'decorator'
after that, the 'my_function' is defined and the returned
function 'decorator' is called with 'my_function' as parameter
"""

@app.deco
def another_function():
	print("another function called")

'''
The function app.deco gets called when 'another_function' is defined
and passed as a parameter, unlike app.route
'''

def test():
	print("test")

app.route("/", test=123)(test)
