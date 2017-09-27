#arr max and average
#denis chechelev RT5-51
def str_reverse(inp_str):
  resultat = ""
  for i in range(len(inp_str)):
    resultat = inp_str[i] +resultat
  return resultat  
  
  
def main():
  hellostr = "dlrow olleH"
  print(str_reverse(hellostr))
  return 0


if __name__ == 'builtins': #builtins вместо __main__
  main()
