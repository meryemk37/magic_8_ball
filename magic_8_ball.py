#magic_8_ball
import random
Magic_8_Ball  = random.randint(1,9)
print("🎱 Magic 8-Ball 🎱")
q = input('\nAsk your question: ')
if Magic_8_Ball == 1:
  print("🎱 Magic 8-Ball 🎱: ")
  print("Yes - definitely.")
elif Magic_8_Ball == 2: 
  print("🎱 Magic 8-Ball 🎱: ")
  print("It is decidedly so.")
elif Magic_8_Ball == 3:
  print("🎱 Magic 8-Ball 🎱: ")
  print("Without a doubt.")
elif Magic_8_Ball == 4:
  print("🎱 Magic 8-Ball 🎱: ")
  print("Reply hazy, try again.")
elif Magic_8_Ball == 5:
  print("🎱 Magic 8-Ball 🎱: ")
  print("Ask again later.")
elif Magic_8_Ball == 6:
  print("🎱 Magic 8-Ball 🎱: ")
  print('Better not tell you now.')
elif Magic_8_Ball == 7:
  print("🎱 Magic 8-Ball 🎱: ")
  print("My sources say no.")
elif Magic_8_Ball == 8:
  print("🎱 Magic 8-Ball 🎱: ")
  print("Outlook not so good.")
elif Magic_8_Ball == 9:
  print("🎱 Magic 8-Ball 🎱: ")
  print('Very doubtful.')

