from time import sleep
import emoji

print("\033[32mfalta 10 segundos para os fogos de artifisio\033[m")
for c in range(1,11):
    sleep(1)
    print(c)

print(emoji.emojize(':fogos_de_artifício:', language='pt'))

