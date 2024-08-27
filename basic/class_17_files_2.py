def demo():
  # read file using read()
  # with open('simple.txt') as f:
  #   contents = f.read(1)
  #   print(contents)

  # read file using readlines()
  # with open('simple.txt') as f:
  #   for index, line in enumerate(f.readlines()):
  #     print(f"{index}. {line}")

  # reade file and strip newline('\n') using readlines()
  # with open('simple.txt') as f:
  #   [print(line.strip()) for line in f.readlines()]

  # read file with 'utf-8' encoding
  with open('quotes.txt', encoding='utf-8') as f:
    for line in f:
      print(line.strip())

  # # write into file with appending mode and utf-8 encoding
  # with open('quotes.txt', encoding='utf-8', mode='a') as f:
  #   f.write("first write")

  # # write file with newline at end of each line
  # lines = ['Readme', 'How to write text files in Python']
  # with open('write.txt', 'w') as f:
  #   # for line in lines:
  #   #     f.write(line)
  #   #     f.write('\n')
  #   f.write('\n'.join(lines))

  # # write chinese into file with utf-8
  # line = "你好，我在学习编程"
  # with open('utf8_write.txt', 'w', encoding='utf-8') as f:
  #   f.write(line)
  '''
  Create a Python function named compress_string that implements a basic string compression using the counts of repeated characters. For example, the string "aabcccccaaa" would become "a2b1c5a3". If the compressed string is not smaller than the original string, your function should return the original string. You can assume the string only has uppercase and lowercase letters (a-z).

  1. The function should take a single string as an argument.
  2. It should return the compressed string if the compressed version is shorter, otherwise, it should return the original string.
  3. You need to count consecutive characters and append the count after the character.

  Sample Input and Output:

  compress_string("aabcccccaaa") should return "a2b1c5a3".
  compress_string("abcdef") should return "abcdef" (since compression does not shorten the string).
  '''

  def compress_string(s):
    compressed = []
    count = 1

    for i in range(1, len(s)):
      if s[i] == s[i - 1]:
        count += 1
      else:
        compressed.append(s[i - 1] + str(count))
        count = 1

    compressed.append(s[-1] + str(count))

    compressed_string = ''.join(compressed)

    return compressed_string if len(compressed_string) < len(s) else s


'''
Work with files
Log File Analysis
You are given a log file named "system.log". Each line in the file represents a log message from a different component of a system, formatted as follows:

[Timestamp] [Component] Message

example:
[2024-05-05 12:00:00] [Database] Connection initialized
[2024-05-05 12:01:00] [Database] Connection closed successfully
[2024-05-05 12:02:00] [Network] Packet received
[2024-05-05 12:03:00] [Network] Packet sent

Your task is to write a Python program that reads the file and print out count of log messages for each component. Each line should be formatted as follows:

[Component]: [Count]

For instance, based on the example above, print should contain:

[Database]: 2
[Network]: 2
'''

def analyze_logs():
  # because we need to count the message per component
  # initialize a dict to store the count of message per component
  message_count = {}

  # 1. read from the system.log file
  with open('system.log', 'r') as f:
    for line in f:
      # each line is expected to be in a format [Timestamp] [Component] Message
      # extract the component of the line
      if ']' in line:
        start = line.find('[') + 1
        end = line.find(']')
        component = line[start:end].strip()

        # increase the count for this component
        if component in message_count:
          message_count[component] += 1
        else:
          message_count[component] = 1

  for component, count in message_count.items():
    print(f'[{component}]: {count}')
