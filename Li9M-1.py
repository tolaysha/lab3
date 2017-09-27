#arr max and average

  
def check_age(inp_data):
  for i in inp_data:
    if i['age'] > 18:
      return True
  return False    


def print_workers_with_child_more18(workers):
  for x in workers:
      if check_age(x.get('children', [])):
         print(x['name'])
        
         
def main():
  ivan = {
  "name" : "Работяга№1" ,
  "age" : 34 ,
  "children" : [{
  "name" : "Первый ребенок первого работяги" ,
  "age" : 20 ,
  }, {
  "name" : "Второй ребенок второго работяги" ,
  "age" : 10 ,
  }],
  }
  dasha = {
  "name" : "Работяга№2" ,
  "age" : 41 ,
  "" : [{
  "name" : "Первый ребенок второго работяги " ,
  "age" : 11 ,
  }, {
  "name" : "Первый ребенок второго работяги " ,
  "age" : 15 ,
  }],
  }
  workers = [ ivan , dasha]
  print_workers_with_child_more18(workers)
  return 0
  

if __name__ == 'builtins': #builtins вместо __main__
  main()
