#!/usr/bin/env python

# AtkinsSJ's Virtual Machine
# --------------------------

import sys

class Main():
	
	verbose = False
	
	def __init__(self):
		if len(sys.argv) == 2:
			self.load_file(sys.argv[1])
		elif len(sys.argv) > 2:
			self.load_file(sys.argv[1])
			for arg in sys.argv[2:]:
				if arg == '-d':
					self.verbose = True
					print 'DEBUG MODE'
				else:
					print 'Unrecognised argument:', arg
					sys.exit()
		else:
			print 'Usage:', sys.argv[0], 'FILE [-d]'
			sys.exit()
		
		self.memory = dict()
	
	def load_file(self, filename):
		try:
			self.file = open( filename ).readlines()
		except IOError:
			print 'ERROR: Cannot open', filename
			sys.exit()
	
	def run(self):
		i = 0
		while i < len(self.file):
			if self.verbose:
				print 'Line', i
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
				self.accumulator += self.get_memory(command[1])
			elif instruction == 'ADDVAL':
				#Add specified value to accumulator
				self.accumulator += int(command[1])
			elif instruction == 'AND':
				#AND bitwise operation with accumulator and address value
				self.accumulator = self.accumulator & self.get_memory(command[1])
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
				self.memory[self.get_address(command[1])] = input
			elif instruction == 'GETC':
				#Get a character from the user and store it in address
				input = False
				while input == False:
					try:
						input = ord(raw_input())
					except TypeError:
						print 'Please enter a single character'
				self.memory[self.get_address(command[1])] = input
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
				self.accumulator = self.get_memory(command[1])
			elif instruction == 'LOADVAL':
				#Load to accumulator
				self.accumulator = int(command[1])
			elif instruction == 'NOT':
				#Invert the accumulator
				self.accumulator = ~self.accumulator
			elif instruction == 'OR':
				#OR bitwise operation with accumulator and address value
				self.accumulator = self.accumulator | self.get_memory(command[1])
			elif instruction == 'PRINT':
				#Output the value at address
				print self.get_memory(command[1])
			elif instruction == 'PRINTC':
				#Output the value at address, as a character
				print chr(self.get_memory(command[1]))
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
				self.memory[self.get_address(command[1])] = self.accumulator
			elif instruction == 'XOR':
				#XOR bitwise operation with accumulator and address value
				self.accumulator = self.accumulator ^ self.get_memory(command[1])
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
	
	def get_address(self, address):
		"""Returns a real address, decoding it if a pointer is passed"""
		if address.startswith('P'):
			# It's a pointer
			paddress = address[1:]
			try:
				return self.memory[int(paddress)]
			except KeyError:
				print 'ERROR: Accessing uninitialised memory at', paddress
				self.print_mem()
				sys.exit()
			except ValueError:
				print 'ERROR: Pointer address', paddress, 'is not a valid integer'
				sys.exit()
		else:
			# It's a regular address
			return int(address)
		
	def get_memory(self, address):
		"""Returns a value from an address or pointer address"""
		pos = self.get_address(address)
			
		try:
			return self.memory[pos]
		except IndexError:
			print 'ERROR: Accessing uninitialised memory at', pos
			sys.exit()
	
	def print_mem(self):
		"""Outputs all used memory locations and their values"""
		for key, val in self.memory.items():
			print key, ':', val
			
if __name__=="__main__":
	# call the main function
	main = Main()
	main.run()
