import unittest

class TestFizzBuzz(unittest.TestCase):
  
  def test_0(self):
    self.assertEqual(fizzBuzz(0), "0")
    
  def test_1(self):
    self.assertEqual(fizzBuzz(1), "1")

  def test_2(self):
    self.assertEqual(fizzBuzz(2), "2")

  def test_3(self):
    self.assertEqual(fizzBuzz(3), "FIZZ")

  def test_4(self):
    self.assertEqual(fizzBuzz(4), "POP")

  def test_5(self):
    self.assertEqual(fizzBuzz(5), "BUZZ")

  def test_6(self):
    self.assertEqual(fizzBuzz(6), "FIZZ")
  
  def test_8(self):
    self.assertEqual(fizzBuzz(8), "POP")
  
  def test_10(self):
    self.assertEqual(fizzBuzz(10), "BUZZ")

  def test_12(self):
    self.assertEqual(fizzBuzz(12), "POPFIZZ")

  def test_15(self):
    self.assertEqual(fizzBuzz(15), "FIZZBUZZ")
  
  def test_15(self):
    self.assertEqual(fizzBuzz(16), "POP")

  def test_15(self):
    self.assertEqual(fizzBuzz(20), "BUZZPOP")
###############################
def fizzBuzz1(number):
  if number == 0:
    number = "0"
  elif number % 3 == 0 and number % 5 == 0 and number % 4 == 0:
    number = "FIZZBUZZPOP"
  elif number % 3 == 0 and number % 5 == 0:
    number = "FIZZBUZZ"
  elif number % 4 == 0 and number % 3 == 0:
    number = "POPFIZZ"
  elif number % 5 == 0 and number % 4 == 0:
    number = "BUZZPOP"
  elif number % 3 == 0:
    number = "FIZZ"
  elif number % 5 == 0:
    number = "BUZZ"
  elif number % 4 == 0:
    number = "POP"
    
  return str(number)

def fizzBuzz2(number):
  if number == 0:
    return "0"

  result = ""
  if number % 3 == 0:
    result += "FIZZ"
  if number % 5 == 0:
    result += "BUZZ"
  if result == "":
    result = str(number)
  
  return result;

def fizzBuzz3(number):
  if number == 0:
    return "0"
  elif number % 3 == 0 and number % 5 == 0:
    return "FIZZBUZZ"
  elif number % 3 == 0:
    return "FIZZ"
  elif number % 5 == 0:
    return "BUZZ"
  else:
    return str(number)
  
############################

if __name__ == '__main__':
    fizzBuzz = fizzBuzz1
    
    #unittest.main()
    
    #for x in range(50000):
      #for y in range(0, 20):
	#fizzBuzz(y)

    for number in range(0, 101):
      print(fizzBuzz(number))
      
    #james = "James"
    #split = 2+1;
    #print(james[0:split] + "." + james[split:len(james)])
    
    #split = 2;
    #print(james[0:split] + "." + james[split+1:len(james)-1])
