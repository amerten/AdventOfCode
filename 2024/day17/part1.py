import math


class Computer:
   def __init__(self, regA, regB, regC, program):
      self._regA = regA
      self._regB = regB
      self._regC = regC
      self._program = program
      self._i = 0
      self._has_printed = False

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
            return
         opcode, operand = self._program[self._i], self._program[self._i + 1]
         if opcode == 0:  # adv
            self._regA = int(self._regA / math.pow(2, self.combo_operand(operand)))
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
               print(end=',')
            print(end=str(self.combo_operand(operand) % 8))
            self._has_printed = True
         elif opcode == 6:  # bdv
            self._regB = int(self._regA / math.pow(2, self.combo_operand(operand)))
         elif opcode == 7:  # cdv
            self._regC = int(self._regA // math.pow(2, self.combo_operand(operand)))
         else:
            raise Exception("Invalid opcode %d" % operand)
         self._i += 2


A, B, C = 0, 0, 0
prog = []
for line in open(0).read().splitlines():
   if line.startswith("Register"):
      _, reg, val = line.split(" ")
      if reg[0] == "A":
         A = int(val)
      elif reg[0] == "B":
         B = int(val)
      else:
         C = int(val)
   elif line:
      prog = list(map(int, line.split()[1].split(',')))
c = Computer(A, B, C, prog)
c.run()