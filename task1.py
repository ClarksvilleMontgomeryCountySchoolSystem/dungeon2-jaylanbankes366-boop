good = r"""
           /|
        /\/ |/\
        \  ^   | /\  /\
  (\/\  / ^   /\/  )/^ )
   \  \/^ /\       ^  /
    )^       ^ \     (
   (   ^   ^      ^\  )
    \___\/____/______/
    [________________]
     |              |
     |     //\\     |
     |    <<()>>    |
     |     \\//     |
      \____________/
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
Zot
"""
bad = r"""
             __   
           .-'  '-.       [nabis]
          /        )                                 
          |  C   o( 
           \       >      
            )  \  /      ..`'
         .-._ / `'      /////     
        / _    \       ( | /
        |/ )    \\     / _,
        / /      |\   / /
       / /       | \ / /
      (  )       /\ ' /
       \ \      (  `-'
        \ \      Y 
        /\ `-.   |
        |(   ^'  |
        \ \\\\  /
         `-    f|
           |   ||
           |   f/
           j   /
           |   )
           |  |
           /  |
           f  |
           \  |
            | |&
           (   `-._,
            -^-----'"""
torch_lit = True
if torch_lit:
    outcome = "Flicker: Thank goodness The torch is lit. We can see!"
    print(good)
else:
    outcome = "Doom: We can't see! The torch is not lit"
    print(bad)
print(outcome)



