import random
from classes.enemy import Enemy

enemy = Enemy(200, 60)
print("HP:", enemy.get_hp())





'''    
        
        
playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp -= dmg
    if playerhp <= 30:
        playerhp = 30

    print("Enemy strikes for", dmg, "points. Current HP is:", playerhp)

    if playerhp > 30:
        continue

    print("You have low health. Teleporting to hospital")
    break
'''