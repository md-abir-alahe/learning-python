msg = "\"Hi\""
print(msg)

# if you don't want characters prefaced by \ to be interpreted ass special characters, you need to use raw string by adding an r before the first quote

print('c:\some\name')

# sting literals can span multiple lines. One way is using triple-quotes """"...""" or '''...''' . End of the lines are automatically included in the string, but it's possible to prevent this by adding a \ at the end of the line. The following example


print("""\
      Usage: thingy [OPTIONS]
        -h              Display this usage message
        -H hostname     Hostname to connect to\
""")

# string can concatenated(glued together) with the + operator and repeated with *

print(3 * 'un' + 'ium')


# user_input = int(input('Enter something: '))
# print(type(user_input));