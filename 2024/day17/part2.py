class Computer:
   def __init__(self, regA, regB, regC, program, program_string):
      self._regA = regA
      self._regB = regB
      self._regC = regC
      self._program = program
      self._i = 0
      self._has_printed = False
      self._output = ""
      self._program_string = program_string

   def combo_operand(self, operand):
      if 0 <= operand <= 3:
         return operand
      elif operand == 4:
         return self._regA
      elif operand == 5:
         return self._regB
      elif operand == 6:
         return self._regC
      raise Exception("Invalid operand %d" % operand)

   def run(self):
      while True:
         if self._i >= len(self._program):
            return self._output == self._program_string
         opcode, operand = self._program[self._i], self._program[self._i + 1]
         if opcode == 0:  # adv
            self._regA = self._regA // 2**self.combo_operand(operand)
         elif opcode == 1:  # bxl
            self._regB = self._regB ^ operand
         elif opcode == 2:  # bst
            self._regB = self.combo_operand(operand) % 8
         elif opcode == 3:  # jnz
            if self._regA != 0:
               self._i = operand
               continue
         elif opcode == 4:  # bxc
            self._regB = self._regB ^ self._regC
         elif opcode == 5:  # out
            if self._has_printed:
               self._output += ","
            self._output += str(self.combo_operand(operand) % 8)
            self._has_printed = True
            if not self._program_string.startswith(self._output):
               return False
         elif opcode == 6:  # bdv
            self._regB = self._regA // 2**self.combo_operand(operand)
         elif opcode == 7:  # cdv
            self._regC = self._regA // 2**self.combo_operand(operand)
         else:
            raise Exception("Invalid opcode %d" % operand)
         self._i += 2


B, C = 0, 0
prog = []
prog_string = ""
for line in open(0).read().splitlines():
   if line.startswith("Register"):
      _, reg, val = line.split(" ")
      if reg[0] == "B":
         B = int(val)
      elif reg[0] == "C":
         C = int(val)
   elif line:
      prog_string = line.split()[1]
      prog = list(map(int, prog_string.split(',')))

A = 8**(len(prog) - 1)
while True:
   c = Computer(A, B, C, prog, prog_string)
   if c.run():
      print(A)
      break
   A += 1
