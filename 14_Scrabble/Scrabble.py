letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# print(letters)
# 15.3
letters += [letter.lower() for letter in letters]
points *= 2
# print(letters)

# 1
letter_to_points = {key:value for key,value in zip(letters, points)}
# print(letter_to_points)
# 2
letter_to_points[' '] = 0
# print(letter_to_points)

# 3 to 8
def score_word(word):
  # 4
  point_total = 0
  # 5
  for char in word:
    point_total += letter_to_points.get(char, 0)
    # alternatively
    # point_total += letter_to_points[char]
  # 6
  return point_total

# 7
brownie_points = score_word('BROWNIE')
# 8
print(brownie_points)
# should print 15 (points)

# 9
player_to_words = {
  'player1': ['BLUE', 'TENNIS', 'EXIT'],
  'wordNerd': ['EARTH', 'EYES', 'MACHINE'],
  'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'],
  'Prof Reader': ['ZAP', 'COMA', 'PERIOD']
}

# 10
player_to_points = {}

# 11
for player, words in player_to_words.items():
  player_points = 0
  # 12
  for word in words:
    player_points += score_word(word)
  # 13
  player_to_points[player] = player_points
# 14
print(player_to_points)

# print(player_to_points.keys())
# print(player_to_points.values())
# print(player_to_points.items())

# 15.2
player_to_points = {}
def update_point_totals():
    for player, words in player_to_words.items():
      player_points = 0
      for word in words:
        player_points += score_word(word)
      player_to_points[player] = player_points

update_point_totals()
print(player_to_points)

# 15.1
def play_word(player, word):
  player_to_words[player].append(word)
  update_point_totals()

play_word('player1', 'FURNITURE')
print(player_to_words)
print(player_to_points)




