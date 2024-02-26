def find_palindrome(s):
    s = s.replace(" ", "").lower()
    if s == s[::-1]:
        return s
    else:
        return None


# Test the function
string = input("Enter a string to find its palindrome: ")
palindrome = find_palindrome(string)

print(palindrome)
if palindrome:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
