#!/usr/bin/env python
# coding: utf-8

# In[ ]:
def get_formatted_name(first,last):
    full_name = first + ' ' + last
    return full_name.title()
print("entet 'q' any time to quit")
while True:
        first=input("\nplease  give a first name:")
        if first== 'q':
            break
        last = input("\nplease give a last name:")
        if last == 'q':
            break
        formatted_name = get_formatted_name(first,last)
        print("\t Neatly formatted name: " + formatted_name + "!")




