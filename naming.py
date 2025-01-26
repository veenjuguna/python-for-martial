import random

def get_cat_name(color, behavior, activity):
    color_names = {
        'black': ['Shadow', 'Midnight', 'Coal'],
        'white': ['Snowball', 'Pearl', 'Ivory'],
        'orange': ['Tiger', 'Pumpkin', 'Ginger'],
        'gray': ['Smokey', 'Ash', 'Silver'],
        'brown': ['Cocoa', 'Mocha', 'Brownie']
    }

    behavior_names = {
        'playful': ['Whiskers', 'Pounce', 'Zippy'],
        'lazy': ['Sleepy', 'Dozer', 'Chill'],
        'curious': ['Scout', 'Snoop', 'Quest'],
        'aggressive': ['Claw', 'Fury', 'Spike']
    }

    activity_names = {
        'climbing': ['Climber', 'Mounty', 'Summit'],
        'hunting': ['Hunter', 'Stalker', 'Prowler'],
        'sleeping': ['Napster', 'Dreamer', 'Snoozer'],
        'eating': ['Chomper', 'Nibble', 'Snack']
    }

    name = random.choice(color_names.get(color, [])) + " " + \
           random.choice(behavior_names.get(behavior, [])) + " " + \
           random.choice(activity_names.get(activity, []))
    
    return name

# Example usage
color = 'black'
behavior = 'playful'
activity = 'climbing'

cat_name = get_cat_name(color, behavior, activity)
print(f"The cat's name is: {cat_name}")