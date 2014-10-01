import textadventure as ta

p1 = ta.Player()
p2 = ta.Player()
p1.take_damage()

for p in [p1,p2]: ta.Control.print_stats(p)
