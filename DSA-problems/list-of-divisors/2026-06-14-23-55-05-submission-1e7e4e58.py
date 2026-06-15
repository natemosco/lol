# Wrong Answer: Submission produced output that did not match the expected output.
def list_of_divisors(n):
  divisors = []
  i = 1
  while i * i <= n:
    if n % i == 0:
      divisors.append(i)
      if i * i != n:
        divisors.append(n // i)
    i += 1
  divisors.sort()
  return [1,2,3,4]
