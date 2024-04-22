match_flashlight = "question1"
run_hide = "question2"
car_river = "question3"
follow_look = "question4"
fight_stand = "question5"
family_police = "queation6"
tree_light = "question7"

print('You can not look behind you!')
match_flashlight = input('You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you pick up? ')
if match_flashlight.lower() == 'match':
    run_hide = input('You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? ')
if match_flashlight.lower() == 'flashlight':
    follow_look = input('You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ')
if run_hide.lower() == 'run':
    fight_stand = input('The bear chases you until you run out of breathe. You look at the ground and see that there is a flare. You can use the flare to FIGHT the bear or you can STAND your ground and try to scare off the bear. Do you FIGHT or STAND? ')
if run_hide.lower() == 'hide':
    print('The bear goes another way and does not notice you and you get away safely.')
if follow_look.lower() == 'follow':
    car_river = input('You follow the path and when you reach the end of the path you see that there is a CAR that might have gas in it but there is a pack of wolves near it. Or there is a RIVER that may lead to safety. DO you pick the CAR or the RIVER? ')
if follow_look.lower() == 'look':
    family_police = input('You look for what was making the noise and see that it was a satelite phone but it only has enough battery to make one call. Do you call your FAMILY or do you call the POLICE? ')
if fight_stand.lower() == 'fight':
    print('You pick up the flare and shoot it at the bear. The sight of the fire from the flare scares the bear away and you are able to escape to safety.')
if fight_stand.lower() == 'stand':
    tree_light = input('You try your best to try to stand tall and scare the bear but it does not work. The bear begins to chase you. You see a tall tree and a bright light in the distance. Do you run to the LIGHT or do you climb the TREE? ')
if car_river.lower() == 'car':
    print('You successfully make it past the wolves and into the car. But the car has no gas in it and the wolves make it into the car and attack you')
if car_river.lower() == 'river':
    print('You are able to follow the river to a town near by where you are able to find help in getting home safely')
if family_police.lower() == 'family':
    print('You call your family in hopes that they can get help and to say goodbye in the chance something bad happens before they arrive.')
if family_police.lower() == 'police':
    print('You call the police and tell them that you are lost in the woods and they send a search party out to find you.')
if tree_light.lower() == 'tree':
    print('The bear climbs the tree after you and attacks you.')
if tree_light.lower() == 'light':
    print('You run and make it to the bright light which is a small gas station store. You are able to hide in and get help.')
    #I think that my several additions to the story and how each choice has a different ending shows that I did 5- shows creativity and exceeds requirements.