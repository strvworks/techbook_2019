s = Seq(1, 2, 3, 4, 5).map(lambda x: x + 1)\
                      .flat_map(lambda x: [x, x])
print(s)  # => [2, 2, 3, 3, 4, 4, 5, 5, 6, 6]