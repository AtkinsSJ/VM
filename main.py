#!/usr/bin/env python

# AtkinsSJ's Virtual Machine
# --------------------------

import sys

class Main():
	def __init__(self):
		if len(sys.argv) == 2:
			try:
				self.file = open( sys.argv[1] ).readlines()
			except IOError:
				print 'ERROR: Cannot open', sys.argv[1]
				sys.exit()
		else:
			print 'Usage:', sys.argv[0], 'FILE'
			sys.exit()
		
		self.memory = dict()
	
	def run(self):
		i = 0
		while i < len(self.file):
			command = self.file[i].strip()
			jump, goto = self.handle(command)
			i += 1 + jump
			if goto:
				i = jump
	
	def handle(self, command):
		"""Handles the command. Returns a tuple of how many steps to skip,
			and whether this number is a line to jump to.
			Usually returns 0, False"""
		command = command.split(' ')
		instruction = command[0]
		try:
			if instruction == 'ADD':
				#Add address value to accumulator
				address = int(command[1])
				self.accumulator += self.memory[address]
			elif instruction == 'ADDVAL':
				#Add specified value to accumulator
				self.accumulator += int(command[1])
			elif instruction == 'AND':
				#AND bitwise operation with accumulator and address value
				address = int(command[1])
				self.accumulator = self.accumulator & self.memory[address]
			elif instruction == 'DEBUG':
				#Output all memory, and accumulator
				print '=== DEBUG ==='
				for key, val in self.memory.items():
					try:
						print key, ':', val, '(', chr(val), ')'
					except ValueError:
						print 'N/A )'
				try:
					print 'Accumulator:', self.accumulator, '(', chr(self.accumulator), ')'
				except ValueError:
					print 'N/A )'
				print '============='
			elif instruction == 'END':
				#Done
				print 'Program terminated successfully.'
				sys.exit()
			elif instruction == 'GET':
				#Get a number from the user and store it in address
				input = 'False'
				while input == 'False':
					try:
						input = int(raw_input())
					except ValueError:
						print 'Please enter a valid integer'
				address = int(command[1])
				self.memory[address] = input
			elif instruction == 'GETC':
				#Get a character from the user and store it in address
				input = False
				while input == False:
					try:
						input = ord(raw_input())
					except TypeError:
						print 'Please enter a single character'
				address = int(command[1])
				self.memory[address] = input
			elif instruction == 'GOTO':
				#Jump to a specific line
				return int(command[1])-1, True
			elif instruction == 'IFNEG':
				#If the accumulator is not -ve, skip next instruction
				if self.accumulator < 0:
					return 0, False
				else:
					return 1, False
			elif instruction == 'IFPOS':
				#If the accumulator is not +ve, skip next instruction
				if self.accumulator > 0:
					return 0, False
				else:
					return 1, False
			elif instruction == 'LOAD':
				#Load address value to accumulator
				address = int(command[1])
				self.accumulator = self.memory[address]
			elif instruction == 'LOADVAL':
				#Load to accumulator
				self.accumulator = int(command[1])
			elif instruction == 'NOT':
				#Invert the accumulator
				self.accumulator = ~self.accumulator
			elif instruction == 'OR':
				#OR bitwise operation with accumulator and address value
				address = int(command[1])
				self.accumulator = self.accumulator | self.memory[address]
			elif instruction == 'PRINT':
				#Output the value at address
				address = int(command[1])
				print self.memory[address]
			elif instruction == 'PRINTC':
				#Output the value at address, as a character
				address = int(command[1])
				print chr(self.memory[address])
			elif instruction == 'PRINTSTRING':
				#Output the rest of the line
				print ' '.join(command[1:])
			elif instruction == 'REM':
				#Comment - do nothing
				pass
			elif instruction == 'SKIP':
				#Miss-out the given number of lines
				return int(command[1]), False
			elif instruction == 'STORE':
				#Store accumulator's value in address
				address = int(command[1])
				self.memory[address] = self.accumulator
			elif instruction == 'XOR':
				#XOR bitwise operation with accumulator and address value
				address = int(command[1])
				self.accumulator = self.accumulator ^ self.memory[address]
			else:
				print 'ERROR: Instruction', command[0], 'not recognised!'
				sys.exit()
				
		except IndexError:
			print 'ERROR: No parameter given for command', command[0]
			sys.exit()
		except KeyError:
			print 'ERROR:', command[1], 'is not a valid memory address!'
			sys.exit()
		return 0, False
			
if __name__=="__main__":
	# call the main function
	main = Main()
	main.run()
