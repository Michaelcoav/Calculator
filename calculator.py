from tkinter import *

class calculator(Tk):
	def __init__(self):
		super().__init__()
		self.title("Calculator")
		self.geometry("400x500+300+00")
		self.configure(bg="#798485")
		self.calc_Background()
		self.calc_String = ""
		self.first_Number = ""
		self.second_Number = ""
		self.first_Operation = ""
		self.second_Operation = ""
		self.total = 0
		self.calc_Buttons()
		
	def calc_Background(self):

		self.calc_Text = StringVar()
		self.calc_Entry = Entry(self, textvariable=self.calc_Text, width=50, font=("bold", 45))
		self.calc_Entry.place(x=0, y=0, height=100)

	def calc_Buttons(self):

		self.num_7_Button = Button(self, text="7", bg="#99a7a8", font=("bold", 20), command=lambda: self.add_Number(7))
		self.num_7_Button.place(x=0, y=100, width=100, height=100)

		self.num_8_Button = Button(self, text="8", bg="#99a7a8", font=("bold", 20), command=lambda: self.add_Number(8))
		self.num_8_Button.place(x=100, y=100, width=100, height=100)

		self.num_9_Button = Button(self, text="9", bg="#99a7a8", font=("bold", 20), command=lambda: self.add_Number(9))
		self.num_9_Button.place(x=200, y=100, width=100, height=100)

		self.num_4_Button = Button(self, text="4", bg="#99a7a8", font=("bold", 20), command=lambda: self.add_Number(4))
		self.num_4_Button.place(x=0, y=200, width=100, height=100)

		self.num_5_Button = Button(self, text="5", bg="#99a7a8", font=("bold", 20), command=lambda: self.add_Number(5))
		self.num_5_Button.place(x=100, y=200, width=100, height=100)

		self.num_6_Button = Button(self, text="6", bg="#99a7a8", font=("bold", 20), command=lambda: self.add_Number(6))
		self.num_6_Button.place(x=200, y=200, width=100, height=100)

		self.num_1_Button = Button(self, text="3", bg="#99a7a8", font=("bold", 20), command=lambda: self.add_Number(3))
		self.num_1_Button.place(x=200, y=300, width=100, height=100)

		self.num_2_Button = Button(self, text="2", bg="#99a7a8", font=("bold", 20), command=lambda: self.add_Number(2))
		self.num_2_Button.place(x=100, y=300, width=100, height=100)

		self.num_3_Button = Button(self, text="1", bg="#99a7a8", font=("bold", 20), command=lambda: self.add_Number(1))
		self.num_3_Button.place(x=0, y=300, width=100, height=100)
		
		self.sign_Button = Button(self, text="+/-", bg="#99a7a8", font=("bold", 20), command= self.sign_Change)
		self.sign_Button.place(x=0, y=400, width=100, height=100)

		self.num_0_Button = Button(self, text="0", bg="#99a7a8", font=("bold", 20), command=lambda: self.add_Number(0))
		self.num_0_Button.place(x=100, y=400, width=100, height=100)

		self.decimal_Button = Button(self, text=".", bg="#99a7a8", font=("bold", 20), command=lambda: self.add_Number("."))
		self.decimal_Button.place(x=200, y=400, width=100, height=100)

		self.delete_Button = Button(self, text="DEL", bg="#99a7a8", font=("bold", 20), command= self.delete)
		self.delete_Button.place(x=300, y=100, width=100, height=67)

		self.division_Button = Button(self, text="/", bg="#99a7a8", font=("bold", 20), command=lambda: self.add_Operation("/"))
		self.division_Button.place(x=300, y=167, width=100, height=67)

		self.multiplication_Button = Button(self, text="*", bg="#99a7a8", font=("bold", 20), command=lambda: self.add_Operation("*"))
		self.multiplication_Button.place(x=300, y=234, width=100, height=67)

		self.subtraction_Button = Button(self, text="-", bg="#99a7a8", font=("bold", 20), command=lambda: self.add_Operation("-"))
		self.subtraction_Button.place(x=300, y=301, width=100, height=67)

		self.addition_Button = Button(self, text="+", bg="#99a7a8", font=("bold", 20), command=lambda: self.add_Operation("+"))
		self.addition_Button.place(x=300, y=368, width=100, height=67)

		self.equal_Button = Button(self, text="=", bg="#99a7a8", font=("bold", 20), command=lambda: self.equal(self.calc_String))
		self.equal_Button.place(x=300, y=435, width=100, height=67)

	def add_Number(self, number):

		# adds number to the end of entry
		self.calc_Entry.insert(END, number)
		
		# adds number to calc string to keep track of entry
		self.calc_String += str(number)

		# if first Operation is empty
		if (len(self.first_Operation) == 0):

			# append number to the first number
			self.first_Number += str(number)
			return

		# append number to the second number
		self.second_Number += str(number)


	def sign_Change(self):

		# the position where the first negative sign would go
		first_Negative = 0

		# the position where the second negative sign would go
		second_Negative = len(self.calc_String) - len(self.second_Number)

		# perform on the first number
		if (len(self.first_Operation) == 0):

			# if first Number is not empty and the first element in first Number is -
			# remove the - sign from the expression
			if (len(self.first_Number) != 0 and self.first_Number[0] == "-"):

				# removes the first element in the first Number
				self.first_Number = self.first_Number[1:]

				# removes the first element in the calc String
				self.calc_String = self.calc_String[1:]

				# delete the first element in calc Entry
				self.calc_Entry.delete(first_Negative)

			# add the - to the expression
			else:

				# add - to the beginning of first Number
				self.first_Number = "-" + self.first_Number

				# add - to the beginning of calc String
				self.calc_String = "-" + self.calc_String

				# insert - at position first Negative to calc Entry
				self.calc_Entry.insert(first_Negative, "-")

		# perform on the second number
		else:

			# if second Number is not empty and the first element in second Number is -
			# remove the - sign from the expression
			if (len(self.second_Number) != 0 and self.second_Number[0] == "-"):

				# deletes the element at position second Negative
				self.calc_Entry.delete(second_Negative)

				# removes the first element of the second Number
				self.second_Number = self.second_Number[1:]

				# concatentes calc String from before second Negative plus second Number
				self.calc_String = self.calc_String[:second_Negative] + self.second_Number

			# add the - expression
			else:

				# negative sign is inserted at position second Negative into calc Entry
				self.calc_Entry.insert(second_Negative, "-")

				# add - to the beginning of second Number
				self.second_Number = "-" + self.second_Number

				# concatenates calc String from before second Negative plus second Number
				self.calc_String = self.calc_String[:second_Negative] + self.second_Number
	

	def replace_Operation(self, operation):

		# first operation is reset
		self.first_Operation = ""

		# removes the previous operation in the calc String
		self.calc_String = self.calc_String[:len(self.calc_String) - 1]
		
		# removes the previous operation from the calc Entry
		self.calc_Entry.delete(len(self.calc_String))


	def add_Operation(self, operation):

		# if second Number is empty and first Operation is not empty
		if (len(self.second_Number) == 0 and len(self.first_Operation) != 0):

			# calls replace Operation
			self.replace_Operation(operation)

		# inserts the operation onto the Entry box
		self.calc_Entry.insert(END, operation)

		# appends the operation to the calc_String
		self.calc_String += operation

		# if first Operation is empty
		if (len(self.first_Operation) == 0):

			# adds the current operation to the first operation
			self.first_Operation += operation
			return 
		
		# saves the new operation to the second operation
		self.second_Operation += operation

		# uses the equal method on everything before the second operation
		self.equal(self.calc_String[:len(self.calc_String) - 1])

		# sets the first operation to the second operation
		self.first_Operation = self.second_Operation

		# resets the value of the second operation
		self.second_Operation = ""

		# adds the first operation which was the second operation to the calc String
		self.calc_String += self.first_Operation

		# inserts the first operation to the calc Entry
		self.calc_Entry.insert(END, self.first_Operation)


	def delete(self):

		# if calc string is empty exit function
		if (len(self.calc_String) == 0):
			return

		# removes the last element in calc String
		self.calc_String = self.calc_String[:len(self.calc_String) - 1]

		# delete the last element in calc Entry
		self.calc_Entry.delete(len(self.calc_String))

		# if there is no current Operation
		if (len(self.first_Operation) == 0):

			# removes the last element from first Number
			self.first_Number = self.first_Number[:len(self.first_Number) - 1]

		# if first Operation is not empty
		else:

			# removes the last element from second Number
			self.second_Number = self.second_Number[:len(self.second_Number) - 1]


	def equal(self, expression):

		# if there is no second Number
		if (len(self.second_Number) == 0):
			return

		# evaluates the expression and converts to an integer
		self.total = eval(expression)

		# sets the first_Number to total 
		self.first_Number = str(self.total)

		# resets the valule of the second number
		self.second_Number = ""
			
		# deletes everything in the calc_Entry	
		self.calc_Entry.delete(0, len(self.calc_Entry.get()))
		
		# resets the calc_String to only containing the new first number
		self.calc_String = "" + self.first_Number

		# resets the current operation
		self.first_Operation = ""

		# inserts the total to the calc_Entry
		self.calc_Entry.insert(END, str(self.total))

if (__name__ == "__main__"):
	win = calculator()
	win.mainloop()
