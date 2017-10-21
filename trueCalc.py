import sys, re, itertools

class TrueCalc:
	def __init__(self):
			self.enteredText = raw_input("Enter the boolean expression: ")
			self.variables = self.getVariables(self.enteredText)

			if not self.validateText(self.enteredText):
				# The entered text checks out, let's move on.
				self.numVariables = self.countVariables(self.variables)

				# Table Generation
				self.generateTable(2**(self.numVariables))
			else:
				print("The input was invalid.")

	def countVariables(self, var):
			return len(var)

	def validateText(self, text):
			regex = re.compile(r"([A-Z]){1}")
			# Is empty?
			if not text:
				return False

	def generateTable(self, rows):
			true = "T"
			false = "F"

			# Set up top row of truth table
			for i in range(0,self.numVariables):
				sys.stdout.write(self.variables[i] + "|")

			print(self.enteredText)

			# Draw a divider line in between the variables and truth values.
			numOfLines = self.numVariables*2 + len(self.enteredText)
			for j in range(0,numOfLines):
				sys.stdout.write("-")

			print("")

			table = list(itertools.product([True,False], repeat=self.numVariables))
			regex = re.compile(r"(True|False)",re.UNICODE)

			for x in table:
				for y in x:
					if y:
						sys.stdout.write(true + "|")
					else:
						sys.stdout.write(false + "|")
				print("")


	def getVariables(self, text):
			regex = re.compile(r"(\w+)",re.UNICODE)
			return regex.findall(text)

					

booleanCalculator = TrueCalc()