def rom_num(num):
  roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M': 1000, 'K': 5000}
  num = num[::-1]
  current = num[0]
  running_tot = roman[num[0]]
  prev = ''
  for i in range(1, len(num)):
    current = num[i]
    prev = num[i-1]
    if roman[current] < roman[prev]:
      running_tot -= roman[current]
    else:
      running_tot += roman[current]

  print(running_tot)

rom_num('KMMMXLIV')
