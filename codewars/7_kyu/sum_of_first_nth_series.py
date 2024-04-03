# Your task is to write a function which returns the n-th term of the following series, which is the sum of the first n terms of the sequence (n is the input parameter).

# series 1 + 1/4 + 1/7 + 1/10 etc

# You will need to figure out the rule of the series to complete this.

# Rules
# You need to round the answer to 2 decimal places and return it as String.

# If the given value is 0 then it should return "0.00".

# You will only be given Natural Numbers as arguments.

def series_sum(n):
    result = sum(1 / (1 + x * 3) for x in range(n))
    return f'{result:.2f}'

print(series_sum(1) == '1.00')
print(series_sum(2) == '1.25')
print(series_sum(5) == '1.57')
print(series_sum(0) == '0.00')
