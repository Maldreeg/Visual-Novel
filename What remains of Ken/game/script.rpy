
#Ken
define K = Character("Ken",color = "#ff0000")

#Helen
define H = Character("Helen", color = "#FF8B8B")
image helen = im.Scale("Helen.png", 700, 750)
image helen_icon_idle = im.Scale("helen_sitting_idle.png", 300, 300)
image helen_icon_hovered = im.Scale("helen_sitting_hovered.png", 300, 300)

#Coworker
define CW = Character("Billy", color = "#FF8B8B")
image billy = im.Scale("Ugly_bastard.png", 700, 900)
#backgrounds
image intro1_1 = im.Scale("Scene 1 Intro/1.jpg", 1920, 1080)
image intro1_2 = im.Scale("Scene 1 Intro/2.jpg", 1920, 1080)
image intro1_3 = im.Scale("Scene 1 Intro/3.jpg", 1920, 1080)
image intro1_4 = im.Scale("Scene 1 Intro/4.jpg", 1920, 1080)
image intro1_5 = im.Scale("Scene 1 Intro/5.jpg", 1920, 1080)
image intro1_6 = im.Scale("Scene 1 Intro/6.jpg", 1920, 1080)
image intro1_7 = im.Scale("Scene 1 Intro/7.jpg", 1920, 1080)
image room_morning = im.Scale("room_morning_light_on.jpg", 1920, 1080)
image urban_day = im.Scale("urban_day.jpg", 1920, 1080)
image living_room = im.Scale("living_room.jpg", 1920, 1080)
image bathroom = im.Scale("Bathroom.jpg", 1920, 1080)

#transition
define slow_dissolve = Dissolve(1.0)

#character position
transform center:
    xalign 0.5
    yalign 1.0
transform left:
    xalign 0.0
    yalign 1.0
transform right:
    xalign 1.0
    yalign 1.0
transform slightleft:
    xalign 0.25
    yalign 1.0
transform slightright:
    xalign 0.75
    yalign 1.0

#buttons

default button1 = False
default button2 = False
default button3 = False
default button4 = False


screen screen_button1:
        modal True
        imagebutton:
            focus_mask True
            xalign .4
            yalign .6
            idle "helen_icon_idle"
            hover "helen_icon_hovered"
            action Jump("talk_to_helen")
              
        imagebutton:
            xpos 1181
            ypos 407
            idle "kitchen_top_idle"
            hover "kitchen_top_hover"
            action Jump("kitchen_top")

        imagebutton:
            xpos 516
            ypos 160
            idle "backdoor_idle"
            hover "backdoor_hover"
            action Jump("look_neighborhood")
            

        imagebutton:
            xpos 338
            ypos 117
            idle "go_to_room_idle"
            hover "go_to_room_hover"
            action Jump("go_to_room_menu")

label start:

    #Intro scene lmaooo
    scene intro1_1 with slow_dissolve
    pause 1
    scene intro1_2 with slow_dissolve
    pause 1
    scene intro1_3 with slow_dissolve
    pause 2
    scene intro1_4 with slow_dissolve
    pause 2
    scene intro1_5 with slow_dissolve
    pause 2
    scene intro1_6 with slow_dissolve
    pause 2
    scene intro1_7 with slow_dissolve
    pause 3


    scene room_morning with slow_dissolve

    "HEY! It's almost 8 my guy, Wake up. "
    K "hrrgh- huh? W-what?"
    "Get outta bed! Geez, you want me to kick you out of it?"
    K "yes...NO! I’m wide awake now."

    show helen with slow_dissolve
    H "Good. Wouldn’t want you to be late after all. Now c’mon."
    K "{i}*chuckles* \n Never a boring morning with her, huh."
    call button_screens_1

label button_screens_1:
        scene living_room with slow_dissolve
        hide helen with slow_dissolve

        #If all the button is pressed
        if button1 and button2 and button3 and button4:
            jump story_continue
        
        call screen screen_button1 with slow_dissolve



label talk_to_helen:
    show helen with slow_dissolve
    H "What? Staring at me again I see."

    menu:
        "Hey, this is part of my morning routine too.":
            H "Sure buddy, you wash your face, you brush your teeth, get your cup of coffee, and-"
            K " And I get to see your pretty profile, that is what makes my mornings complete."
            H "Oh, shut up. don’t start this early. (Use the blushing sprite)"
        "I just can’t believe what I’m seeing.":
            H "Yeah, might be too good for you. Are you sure I’m real?"
            K "Sure as day!"
            H "Yeah?"
            K "Yeah!"
            H "You Sure?"
            K "Yeah!"
            H "*Sigh* \n Why do I even bother…"
        "…You got something on your face":
            H "Oh! Dammit, again? Can you take it off? Please…"
            K "Nah, I was just kidding."
            H "WHY YOU-"
    $ button1 = True
    jump button_screens_1

label look_neighborhood:
    scene urban_day with slow_dissolve
    K "is so cool"
    K "Im so very cool"
    K "I should so back"
    $ button2 = True
    jump button_screens_1

label go_to_room_menu: 
    menu:
        "Go to Bedroom":
         jump go_to_bedroom
        "Go to Bathroom":
         jump go_to_bathroom

label kitchen_top:
    K "You already made some coffee?"
    H "Yeah! It's yours. I already drank my half."
    K "Thanks! …Although I thought you hated this blend."
    H "I just tried it again, plus hate is a strong word anyway."
    K "It’s a bit cold now."
    H "Yeah sorry, I woke up really early."
    $ button3 = True
    jump button_screens_1

label go_to_bedroom:
    scene room_morning with slow_dissolve
    "Well...nothing to do here"
    jump button_screens_1

label go_to_bathroom:
    scene bathroom with slow_dissolve
    H "The heater’s broken again. Found that out the hard way."
    K "Ouch…Guess it's another cold shower for me today."
    H "Yeah, sucks to be us."
    K "Sucks to be me."
    H "I’ll bring over your clothes, just call for me."
    K "Alright, Thank you."
    $ button4 = True
    jump button_screens_1

label story_continue:
        show helen with slow_dissolve
        H "How about some breakfast before you go? "
        menu:
            "Nah, I might just make it before I’m late if I hurry- I have to go.":
                jump with_breakfast

            "Sure, why not? I’m going to be late anyway.":
                jump no_breakfast
        
        
label with_breakfast:
    H "You sure? You’ve been skipping breakfast since-"
    K "I’m sure."
    jump after_menu1

label no_breakfast:
    H "That’s the spirit you deterministic sucker."
    K "What’s for breakfast?"
    H "French Toast."
    K "Nice, you always made them nicely."
    H " …erm, from the convenience store."
    K "And that is fine as well, thanks for getting us some."
    jump after_menu1

label after_menu1:
    H "Okay, take care of yourself, I sure as hell won’t."
    K "You never did stop with that did you?"
    H "Whatever do you mean?"
    K "…I love you."
    H "I love you too."
    scene morningtime with slow_dissolve
    pause 5.0
    jump act2_start

label act2_start:
    scene work with slow_dissolve
    K "{i}The trains were crowded, as usual.\nThe clerk gave me the wrong change, as usual.\nAnd I hate my job, as usual."
    K "{i}*Sighs* Alright enough complaining, on to your cubicle.\nI am the company’s most dispensable soldier, ready to fight their most mundane battles."
    K "{i}Can’t wait to go home."
    scene cubicle with slow_dissolve
    "You work to live, and live to work. A 9 to 5, 5 days a week."
    "Like Clockwork, you hear the other cubicles, silent, save for the clacking of keyboards."
    "You are focused at your job, until…"
    K "{i}It smells like cigarettes… Oh, dammit."
    show billy with slow_dissolve
    CW "Ken, well you’re here early."
    K "No sir, I’m just on time."
    CW "My point being, you haven’t been on time for ages. Take it from me- just take the company allotted leave."
    CW "No one is going to fault you for it. And you need it anyhow, after-"
    menu:
        "I…need it? I’m perfectly fine.":
            CW "…"
            CW "Look, it’s fine to say that you are, but you shouldn’t lie to yourself."
            K "What? I have no idea of where you’re going with this."
            CW "You’re relatively new here. You don’t talk much. You don’t join any of your coworkers."
            CW "You’re a mystery to us, Ken. But even I can tell that something happened to you recently."
        "I would if I could, but a man’s gotta eat.":
            CW "You already took a week off, on a mental health leave. You must know that the company still pays you for that."








































return
