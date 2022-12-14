from cpu_cs104 import CPU

DATA_INPUT = 'data_input.txt'
INSTRUCTION_INPUT = 'instruction_input.txt'

# Functions

def insert_data_into_memory():
  with open(DATA_INPUT) as DI:
    for data in [line.strip() for line in DI.readlines()]:
      cpu.write_to_memory(data[:8], int(data[9:]))

def parse_instructions():
  with open(INSTRUCTION_INPUT) as II:
    for instruction in [line.strip() for line in II.readlines()]:
      splited_instruction = instruction.split(',')
      if splited_instruction[0] == 'HALT':
        cpu.halt_instruction()
        break
      cpu.parse_instruction(instruction)

# --- #

# Program

cpu = CPU()

insert_data_into_memory()
parse_instructions()