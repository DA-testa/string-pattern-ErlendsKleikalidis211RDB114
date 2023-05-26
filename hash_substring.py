def read_input():
  input_type = input().rstrip()
  
  if input_type == 'F':
    fileName = input().rstrip()
    with open(fileName, 'r') as file:
      pattern = file.readline().rstrip()
      text = file.readline().rstrip()
  else:
    pattern = input().rstrip()
    text = input().rstrip()
  
  return pattern, text

def print_occurrences(output):
  print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
  occurrences = []
  p_len = len(pattern)
  t_len = len(text)
  prime = 10 ** 9 + 7
  multiplier = 263

  p_hash = hash_string(pattern, prime, multiplier)
  t_hash = hash_string(text[:p_len], prime, multiplier)

  if p_hash == t_hash and pattern == text[:p_len]:
    occurrences.append(0)

  y = pow(multiplier, p_len, prime)

  for i in range(1, t_len - p_len + 1):
    t_hash = (multiplier * t_hash + ord(text[i + p_len - 1]) - y * ord(text[i - 1])) % prime
    if p_hash == t_hash and pattern == text[i:i + p_len]:
      occurrences.append(i)

  return occurrences


def hash_string(string, prime, multiplier):
  h = 0
  for i in range(len(string)):
    h = (h * multiplier + ord(string[i])) % prime
  return h

if __name__ == '__main__':
  print_occurrences(get_occurrences(*read_input()))
