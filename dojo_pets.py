import ninja
import pets

turtle = pets.Pet('Linus', 'turtle', 'hides')
ninja1 = ninja.Ninja('Bob', 'Bobson', 'lettuce', 'pellets', turtle)

ninja1.feed().walk().bathe()

dog = pets.Dog('Bruno', 'dog', 'hoops')
ninja2 = ninja.Ninja('Bartholomew', 'Bartson', 'bone', 'kibble', dog)
ninja2.feed().walk().bathe()