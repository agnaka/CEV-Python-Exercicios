import emoji
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
sleep(2)
print(emoji.emojize('\033[1;31mBOOOMMM!!!\033[m ' + '\033[1;33m:fireworks:\033[m ' * 3, use_aliases = True))
# print(emoji.emojize('BOOOMMM!!!' + ':fireworks: ' * 3, use_aliases = True))