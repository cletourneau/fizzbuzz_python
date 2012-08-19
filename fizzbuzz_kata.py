import unittest

class FizzBuzz(object):
  convert_list = [(15, 'fizzbuzz'), (5, 'buzz'), (3, 'fizz')]

  def convert(self, n):
    for m, v in FizzBuzz.convert_list:
      if n % m == 0: return v
    return str(n)


class FizzBuzzTestCase(unittest.TestCase):
  def setUp(self):
    self.fb = FizzBuzz()

  def test_numbers(self):
    self.assertEqual('1', self.fb.convert(1))
    self.assertEqual('2', self.fb.convert(2))
    self.assertEqual('4', self.fb.convert(4))
    self.assertEqual('7', self.fb.convert(7))

  def test_fizz(self):
    self.assertEqual('fizz', self.fb.convert(3))
    self.assertEqual('fizz', self.fb.convert(6))

  def test_buzz(self):
    self.assertEqual('buzz', self.fb.convert(5))
    self.assertEqual('buzz', self.fb.convert(10))
    self.assertEqual('buzz', self.fb.convert(100))

  def test_fizzbuzz(self):
    self.assertEqual('fizzbuzz', self.fb.convert(15))
    self.assertEqual('fizzbuzz', self.fb.convert(30))

if __name__ == '__main__':
  unittest.main()
