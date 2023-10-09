# Project 011: Organizing Poet Information (implementing string methods)

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# Task 1
print(highlighted_poems)

# Task 2
highlighted_poems_list = highlighted_poems.split(',')

# Task 3
print(highlighted_poems_list)

# Task 4
highlighted_poems_stripped = [i.strip() for i in highlighted_poems_list]

# Task 5
print(highlighted_poems_stripped)

# Task 6
highlighted_poems_details = []
# Task 7
for i in highlighted_poems_stripped:
  highlighted_poems_details.append(i.split(':'))

print(highlighted_poems_details)

# Task 8
titles = []
poets = []
dates = []

# Task 9
for t, p, d in highlighted_poems_details:
  titles.append(t)
  poets.append(p)
  dates.append(d)

for i in range(len(titles)):
  print('The poem {} was published by {} in {}.'.format(titles[i], poets[i], dates[i]))

# # Altern Task 9 solution
# for poem in highlighted_poems_details:
#     titles.append(poem[0])
#     poets.append(poem[1])
#     dates.append(poem[2])
#
# for i in range(0, len(highlighted_poems_details)):
#     print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))


