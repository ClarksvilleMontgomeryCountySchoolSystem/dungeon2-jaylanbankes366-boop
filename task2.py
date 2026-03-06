good = r"""

     8 8 8 8                     ,ooo.
     8a8 8a8                    oP   ?b
    d888a888zzzzzzzzzzzzzzzzzzzz8     8b
     `""^""'                    ?o___oP'
     """

bad = r"""

            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
ejm        |__________|
"""
has_key = False
if has_key:
    outcome = "Click: Let's unlock the door"
    print(good)
else:
    outcome = "Doom: We need to get they key!"
    print(bad)
print(outcome)

