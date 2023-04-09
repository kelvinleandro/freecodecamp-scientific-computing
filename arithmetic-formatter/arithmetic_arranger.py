def has_invalid_operators(problems):
  ''' 
  saves each operator in an array and 
  returns True if there's a multiply or 
  divide operator in the array
  '''
  arr = [p.split()[1] for p in problems]
  if '*' in arr or '/' in arr:
    return True

  return False


def has_invalid_operands(problems):
  '''
  saves all operands in an array and
  returns True if it finds one that
  doesn't contains only digits
  '''
  arr = []
  for problem in problems:
    arr.append(problem.split()[0])
    arr.append(problem.split()[2])

  for operand in arr:
    if not operand.isdigit():
      return True

  return False


def has_more_digits(problems):
  '''
  saves all operands in an array and
  returns True if it finds one that
  has more than 4 digits
  '''
  arr = []
  for problem in problems:
    arr.append(problem.split()[0])
    arr.append(problem.split()[2])

  for operand in arr:
    if len(operand) > 4:
      return True

  return False


def arithmetic_arranger(problems, showAnswer=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  if has_invalid_operators(problems):
    return "Error: Operator must be '+' or '-'."

  if has_invalid_operands(problems):
    return "Error: Numbers must only contain digits."

  if has_more_digits(problems):
    return "Error: Numbers cannot be more than four digits."

  arranged_problems = ''
  # formatted_string = f"{string:>{maxlen+2}}"
  operands_tuples = [(p.split()[0], p.split()[2]) for p in problems]
  operators_arr = [p.split()[1] for p in problems]
  max_lengths = [max(len(word) for word in p.split()) for p in problems]

  # adds the first operand of each operation in the string
  for i in range(len(operands_tuples)):
    arranged_problems += f"{operands_tuples[i][0]:>{max_lengths[i]+2}}"
    if i == (len(operands_tuples) - 1):
      arranged_problems += '\n'
    else:
      arranged_problems += '    '

  # adds the second operand plus the operator of each operation in the string
  for i in range(len(operands_tuples)):
    arranged_problems += f"{operators_arr[i]} {operands_tuples[i][1]:>{max_lengths[i]}}"
    if i == (len(operands_tuples) - 1):
      arranged_problems += '\n'
    else:
      arranged_problems += '    '

  # adds the horizontal line below each operation
  for i in range(len(max_lengths)):
    arranged_problems += '-' * (max_lengths[i] + 2)
    if i < len(max_lengths) - 1:
      arranged_problems += '    '

  if showAnswer:
    arranged_problems += '\n'
    for i in range(len(problems)):
      # calculate each problem and adds to the string
      result = eval(problems[i])
      arranged_problems += f"{result:>{max_lengths[i]+2}}"
      if i < (len(problems) - 1):
        arranged_problems += '    '

  return arranged_problems
