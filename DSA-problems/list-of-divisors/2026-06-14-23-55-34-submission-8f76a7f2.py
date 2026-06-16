# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
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
  return divisors
