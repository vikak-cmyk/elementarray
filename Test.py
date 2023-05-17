# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1

y_company = ["Canvas", "Framed Poster"]
z_company = ["Canvas", "Poster"]


def linear_search(x_company, n, x):
    for i in range(0, n):
        if x_company[i] == x:
            return i
    return -1


# Driver Code
x_company = ["Poster", "Framed Poster", "Whiteboard"]
x = "Canvas"
n = len(x_company)
result = linear_search(x_company, n, x)
if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", result)
