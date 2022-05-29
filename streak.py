import time
import random
import numpy
from datetime import datetime

    
def find_nearest(array, value):
    array = numpy.asarray([x for x in array if x > value])
    idx = (numpy.abs(array - value)).argmin()
    return array[idx]


start_time = 0 # unix time
now = int(time.time())

total_hours_passed = (now - start_time) / 60 / 60
days_passed = int(total_hours_passed / 24)
day_hours_passed = int(total_hours_passed - days_passed * 24)

if days_passed > 0 and int(datetime.fromtimestamp(start_time).strftime("%d")) == int(datetime.fromtimestamp(now).strftime("%d")):
    print("Special Day: NoFap mensiversary")

goal = find_nearest([30, 90, 180, 365], days_passed)
toGoal = goal - days_passed

print(
    "NoFap for life!"
    if toGoal < 0
    else (
        f"Reached Goal: {goal} days"
        if toGoal == 0
        else f"To Goal: {toGoal} days to {goal} days"
    )
)

print(f"Streak: {int(days_passed)} days and {day_hours_passed} hours")

enable_quoates = False;
if enable_quoates:
    quoate = random.choice(
        [
            "Work hard for what you want because it won't come to you without a fight. You have to be strong and courageous and know that you can do anything you put your mind to. If somebody puts you down or criticizes you, just keep on believing in yourself and turn it into something positive.\n\n- Leah LaBelle",
            "Remember your dreams and fight for them. You must know what you want from life. There is just one thing that makes your dream become impossible: the fear of failure.\n\n- Paulo Coehelo",
            "I never give up, even when people tell me that I can't do anything. But if I believe I can, I really fight for it.\n\n- Leila Lopes",
            "A warrior is not a person that carries something destructive. The biggest war you ever go through is right between your own ears. It’s in your mind. We’re all going through a war in our mind, and we have to callus our mind to fight that war and to win that war.\n\n- David Goggins",
            "If you want to get a life that is worth living, a life that expresses your deepest feelings and emotions and cares and dreams, you have to fight for it.\n\n- Alice Walker",
            "Life is full of harmony. Notice it, Notice the bumble bee, the small child, and the smiling faces, Breathe the rain, and feel the wind. Live your life to the fullest potential, and fight for your dreams.\n\n- Ashley Smith",
            "Like success, failure is many things to many people. With a confident mental attitude, failure is a learning experience, a rung on the ladder, and a plateau at which to get your thoughts in order to prepare to try again.\n\n- Clement Stone",
            "If you accomplish something good with hard work, the labor passes quickly, but the good endures; if you do something shameful in pursuit of pleasure, the pleasure passes quickly, but the shame endures.\n\n- Musonius Rufus",
            "It's all for a much larger purpose than any samplance of happiness that immediate gratification provides.\n\n- YUGEN",
            "NoFap gives you energy, courage, motivation and much more. Feel free to use them in your path.\n\n- Sensei",
        ]
    )
    
    print(f"\n{quoate}")
