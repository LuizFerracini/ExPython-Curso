words = ('Macaco',
         'Leao',
         'Cachorro',
         'Gato',
         'Porco',
         'Tigre',
         'Papagaio')
print('-='*20)
for x in words:
    print(f"\nNa palavra {x.upper()} temos:", end=" ")
    for letra in x:
        if letra in "aeiouAEIOU":
            print(f"{letra}", end='  ')
