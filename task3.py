good = r"""
        ||
        ||                   ||
     ||/||___                ||
     || /`   )____________||_/|
     ||/___ //_/_/_/_/_/_/||/ |
     ||(___)/_/_/_/_/_/_/_||  |
     ||     |_|_|_|_|_|_|_|| /|
     ||     | | | | | | | ||/||
     ||~~~~~~~~~~~~~~~~~~~||
jgs  ||                   ||

"""
bad = r"""

                                     _
                                    //
                       ___         //
                      /   \       //
                     :   ==\   <\//
                      \____/_.-'_}>
                     /  `-`\  .//`'
                    :__<_   :/ "
                    /.--.\  |
                   { \>
    -. i|       `. |._|         .
       Y||        \ ' '          `.
   -., ||     ,    ,)'| .__,_\
  b'ger ' .,-.+- ,'_._\  "'-=-i"" ----
 .,'.            _,. -'''
"""

guard_awake = False
if not guard_awake:
    outcome = "Shadow: Run away while he is asleep!!"
    print(good)
else:
    outcome = "Doom: He's awake!! Don't let him find you"
    print(bad)
print(outcome)
