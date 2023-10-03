
#Ken
define K = Character("Ken",color = "#ff0000")

#Helen
define H = Character("Helen", color = "#FF8B8B")
image helen = im.Scale("Helen.png", 700, 750)
image helen_icon_idle = im.Scale("helen_sitting_idle.png", 500, 500)
image helen_icon_hovered = im.Scale("helen_sitting_hovered.png", 500, 500)

#backgrounds
image morningtime = im.Scale("630 AM.jpg", 1920, 1080)
image room_morning = im.Scale("room_morning_light_on.jpg", 1920, 1080)
image urban_day = im.Scale("urban_day.jpg", 1920, 1080)

#transition
define slow_dissolve = Dissolve(1.0)


#buttons

default button1 = False
default button2 = False

screen screen_button1:
        modal True
        imagebutton:
            xalign 3
            yalign .8
            idle "helen_icon_idle"
            hover "helen_icon_hovered"
            focus_mask True
            action Jump("talk_to_helen")

        imagebutton:
            xpos 610
            ypos 199
            idle "door_idle"
            hover "door_hover"
            action Jump("look_neighborhood")

label start:

    scene morningtime with slow_dissolve
    pause 5.0
    scene room_morning with slow_dissolve

    "HEY! It's almost 7 my guy, Wake up. "
    K "hrrgh- huh? W-what?"
    "Get outta bed! Geez, you want me to kick you out of it?"
    K "yes...NO! I’m wide awake now."

    show helen with slow_dissolve
    H "Good. Wouldn’t want you to be late after all. Now c’mon."
    K "*chuckles* \n Never a boring morning with her, huh."
    call button_screens_1

label button_screens_1:
        scene room_morning with slow_dissolve
        hide helen with slow_dissolve

        if button1 and button2:
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
    return









































return
