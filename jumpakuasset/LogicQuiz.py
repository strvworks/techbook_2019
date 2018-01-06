# -*- coding: utf-8 -*-
import itertools as it

def implies(p, q):
    return (not p) or q

# 容疑者集合
suspects = ("美衣", "出井", "永一", "愛")

# 前提条件
conditions = (
    lambda cs, vs: implies("美衣" in cs, "永一" in cs),
    lambda cs, vs: implies("美衣" in vs, "永一" in vs),
    lambda cs, vs: "愛" not in cs and "愛" not in vs,
    lambda cs, vs: len([s for s in suspects if s in cs and s in vs]) == 0,
    lambda cs, vs: len([s for s in suspects if s in cs or s in vs]) == 3,
    lambda cs, vs: "出井" not in cs,
    lambda cs, vs: implies("美衣" in cs, "出井" not in vs),
)

for (criminalsIndex, victimsIndex) in it.product(
        it.product(range(2), repeat=len(suspects)),
        it.product(range(2), repeat=len(suspects))):
    criminals = list(it.compress(suspects, criminalsIndex))
    victims = list(it.compress(suspects, victimsIndex))
    isConsistent = all([c(criminals, victims) for c in conditions])
    if isConsistent:
        print("犯人", list(criminals))
        print("被害者", list(victims))
