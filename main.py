#!/usr/bin/python3

import re

wall = "f"
path = "g"
optional = "?"
group_start = "["
group_end = "]"
group_seperator = ","
current_attr = "%"
rule_regex = re.compile(r'^\(...,([^,]*),([^\)]*)\)..\(([^,]*),[^,]*,([^\)]*)\)$')

def rules_for_line(line):
  index = line.find(optional, 1, 4)
  if index > 0:
    return [
      *rules_for_line(line[:index] + wall + line[index+1:]),
      *rules_for_line(line[:index] + path + line[index+1:])
    ]

  index = line.find(group_start)
  if index > 0:
    end_index = line.find(group_end, index+1)
    states = line[index+1:end_index].split(group_seperator)
    rules = []
    for state in states:
      rules.extend(
        rules_for_line(line[:index] + state + line[end_index+1:])
      )
    return rules
  
  match = rule_regex.match(line)
  if match:
    offset = 0
    if match[3] == current_attr:
      line = line[:match.start(3)] + match[2] + line[match.end(3):]
      offset = len(match[2]) - len(current_attr)
    if match[4] == current_attr:
      line = line[:match.start(4)+offset] + match[1] + line[match.end(4)+offset:]
  
  return [line]

def main(file):
  for line in open(file, 'r'):
    for rule in rules_for_line(line.strip()):
      print(rule)

if __name__ == '__main__':
  import sys
  if len(sys.argv) == 2:
    main(sys.argv[1])
  else:
    print(f"Usage: {sys.argv[0]} <file>")