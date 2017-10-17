import sys

class TrueCalc:
	def __init__(self):
			self.numVariables = 0
			self.tableSize = 0

			enteredText = raw_input("Enter the boolean expression: ")

			self.validateText(enteredText)

			# The entered text checks out, let's move on.
			numVariables = self.countVariables(enteredText)
			tableSize = 2**(numVariables)

			print(numVariables)

	def countVariables(self, text):
			i = 0
			for c in text:
				if c.isupper():
					i += 1
			return i

	def validateText(self, text):
			# Is empty?
			if not text:
				return False


booleanCalculator = TrueCalc()