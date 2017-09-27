#arr max and average
def arr_min(array):
  if len(array) == 0:
      return -1
  minim = array[0]
  for x in array:
    current = x
    if current < minim:
      minim = current
  return minim


def arr_avg(array):
  if len(array) == 0:
      return -1
  summ = 0
  for x in array:
    summ += x
  return summ / len(array)
  
  
def main():
  array1 = [-63,-62,23,22,58,98]
  array2 = [3,65,1,-5,-98,65]     
  print(array1)
  print('Минимальное значение первого массива: ')
  print(arr_min(array1))  
  print('Среднее значение первого массива: ')
  print(arr_avg(array1),'\n')

  print(array2)
  print('Минимальное значение второго массива: ')
  print(arr_min(array2))  
  print('Среднее значение второго массива: ')
  print(arr_avg(array2))
  return 0


#print (__name__)
if __name__ == 'builtins': #builtins вместо __main__
  main()
  
