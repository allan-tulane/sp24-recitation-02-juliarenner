from main import *
import math


def test_simple_work():
  """ done. """
  for n in [10, 20, 50, 100, 1000, 5000, 10000]:
    result = simple_work_calc(n, a=2, b=2)
    print(result)
  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650
  assert simple_work_calc(40, 5, 2) == 5390
  assert simple_work_calc(50, 6, 2) == 13592
  assert simple_work_calc(60, 7, 2) == 27416


def test_work():
  assert work_calc(10, 2, 2, lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n * n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300
  assert work_calc(30, 3, 2, lambda n: n * n) == 2340
  assert work_calc(30, 3, 2, lambda n: n * n * n) == 41022
  assert work_calc(30, 2, 2, lambda n: n) == 128


n = 200
print(work_calc(n, 2, 2, lambda n: 1))
print(work_calc(n, 2, 2, lambda n: math.log(n)))
print(work_calc(n, 2, 2, lambda n: n))


def test_compare_work():
  # curry work_calc to create multiple work
  # functions that can be passed to compare_work

  # create work_fn1
  def work_fn1(n):
    return work_calc(n, 4, 2, lambda n: n)

  # create work_fn2
  def work_fn2(n):
    return work_calc(n, 4, 2, lambda n: n * n * n)

  res = compare_work(work_fn1, work_fn2)
  print_results(res)


def test_compare_span():
  # curry work_calc to create multiple work
  # functions taht can be passed to compare_work
  # create work_fn1
  def span_fn1(n):
    return span_calc(n, 4, 2, lambda n: n)

  # create work_fn2
  def span_fn2(n):
    return span_calc(n, 4, 2, lambda n: n * n * n)

  res = compare_span(span_fn1, span_fn2)
  print_results(res)
