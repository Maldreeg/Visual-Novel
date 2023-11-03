
#Ken
define K = Character("Ken",color = "#ff0000")

#Helen
define H = Character("Helen", color = "#FF8B8B")
image helen = im.Scale("Helen.png", 700, 750)
image helen_icon_idle = im.Scale("helen_sitting_idle.png", 300, 300)
image helen_icon_hovered = im.Scale("helen_sitting_hovered.png", 300, 300)

#Coworker
define CW = Character("Billy", color = "#006ca5")
image billy = im.Scale("Ugly_bastard.png", 700, 900)

#Barista
define F = Character("Felix", color = "#77DD77")
image felix = im.Scale("kanzaki.png", 700, 900)

#NPC's
define booger_aids = Character("Intercom", color = "#ADD8E6")

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
image coffee = im.Scale("coffee.png", 1920, 1080)
image office_entrance = im.Scale("Office_Entrance.png", 1920, 1080)
image office_cubicle = im.Scale("Office_Cubicles.png", 1920, 1080)
image hallway1 = im.Scale("hallway1.png", 1920, 1080)
image hallway2 = im.Scale("hallway2.png", 1920, 1080)
image hallway3 = im.Scale("hallway3.png", 1920, 1080)
image cafe = im.Scale("Cafe.png", 1920, 1080)
image cafe_outside = im.Scale("cafe_outside.png", 1920, 1080)
image street_night = im.Scale("street_night.png", 1920, 1080)
image grocery_store_outside = im.Scale("grocery_store_outside.png", 1920, 1080)
image grocery_store_inside = im.Scale("grocery_store_inside.png", 1920, 1080)
image i_wish_this_was_manila_bay = im.Scale("i_wish_this_was_manila_bay.png", 1920, 1080)


#transition
define slow_dissolve = Dissolve(.8)
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define fade = Fade(0.5, 0.0, 0.5)

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
default story_continue_played = False

screen screen_button1:
        modal True   
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

        imagebutton:
            focus_mask True
            xalign .4
            yalign .6
            idle "helen_icon_idle"
            hover "helen_icon_hovered"
            action Jump("talk_to_helen")

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
    show room_morning with slow_dissolve:
        blur 6
    show helen with slow_dissolve
    H "Good. Wouldn’t want you to be late after all. Now c’mon."
    K "{i}*chuckles* \n Never a boring morning with her, huh."
    call button_screens_1

label button_screens_1:
    scene living_room with slow_dissolve
    hide helen with slow_dissolve

    # If all the button is pressed
    if button1 and button2 and button3 and button4 and not story_continue_played:
        jump story_continue
        

    else: 
        call screen screen_button1 with slow_dissolve




label talk_to_helen:
    show living_room with slow_dissolve:
        blur 6
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
    scene coffee with slow_dissolve
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
    show living_room with slow_dissolve:
        blur 6
    show helen with slow_dissolve
    H "How about some breakfast before you go? "
    menu:
        "Nah, I might just make it before I’m late if I hurry- I have to go.":
            jump with_breakfast

        "Sure, why not? I’m going to be late anyway.":
            jump no_breakfast
    $ story_continue_played = True
    jump after_menu1
        
        
label with_breakfast:
    H "You sure? You’ve been skipping breakfast since-"
    K "I’m sure."
    

label no_breakfast:
    H "That’s the spirit you deterministic sucker."
    K "What’s for breakfast?"
    H "French Toast."
    K "Nice, you always made them nicely."
    H " …erm, from the convenience store."
    K "And that is fine as well, thanks for getting us some."
    

label after_menu1:
    H "Okay, take care of yourself, I sure as hell won’t."
    K "You never did stop with that did you?"
    H "Whatever do you mean?"
    K "…I love you."
    H "I love you too."
    scene add_transition_here with slow_dissolve
    pause 5.0
    jump act2_start

label act2_start:
    scene office_entrance with slow_dissolve
    K "{i}The trains were crowded, as usual.\nThe clerk gave me the wrong change, as usual.\nAnd I hate my job, as usual."
    K "{i}*Sighs* Alright enough complaining, on to your cubicle.\nI am the company’s most dispensable soldier, ready to fight their most mundane battles."
    K "{i}Can’t wait to go home."
    scene office_cubicle with slow_dissolve
    "You work to live, and live to work. A 9 to 5, 5 days a week."
    "Like Clockwork, you hear the other cubicles, silent, save for the clacking of keyboards."
    "You are focused at your job, until…"
    K "{i}It smells like cigarettes… Oh, dammit."
    show office_cubicle with slow_dissolve:
        blur 12
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
            jump dialogue_work_1a
        "I would if I could, but a man’s gotta eat.":
            CW "You already took a week off, on a mental health leave. You must know that the company still pays you for that."
            K "I know. I was making a joke."
            CW "Is it a joking matter?"
            K "No, it isn’t. That's why I’d rather keep it to myself."
            CW "So there is something behind your recent behavior."
            K "Back off. It’s not your business."
            CW "For any other person I would agree. But not you."
            jump dialogue_work_2

label dialogue_work_1a:
    menu:
        "You. You think that there is something that happened to me, How so?":
            CW "You’ve never spoken to anyone here this week before this."
            CW "You’re erratic, your work output has gone to hell. And now you’re aggressive at the slightest provocation."
            CW "Not to mention your appearance, have you ever slept in the past week?"
            K "You’ve got quite a list. I’m impressed. How noble of you to take your time to worry about little old me."
            K "You don’t need to do this. I don’t need you."
            CW "Why are you really like this?"
            K "...why? ...WHY? You ask me why?"
        "I know you mean no harm but…I like to keep my personal and work life separate.":
            jump dialogue_work_2

label dialogue_work_2:
    CW "Your behavior the past week has been very concerning."
    CW "You’re closed off. You come in late and you speak to no one."
    CW "You can’t hide it, Hiding it makes it more obvious. You have problems and I want to help."
    K "I-.."
    K "Look are you really risking our comfortable coworker relationship because you think you can help."
    K "I say that because I don’t appreciate it. Not at all. I can’t stop you from pushing but I really don’t think you’ll get the results you want."
    CW "What has gotten you like this? I can’t even begin to imagine, it must have been very bad. You must know tha-"
    menu:
        "IT WAS!":
            jump dialogue_work_3
        "You’re pushing it. Don’t go further with your questioning. I’m warning you.":
            CW "Now…I’m not looking for new gossip, or to hurt you in any way. I’m asking you what happened so that you can begin to heal."
            K "You’re not my therapist. …Sure, I’ll admit that I have my problems, but how can you help me?"
            K "{b}You’re nobody to me, just my senior at work."
            CW "I’m guessing you don’t have many friends here. I’m guessing you're not the type to seek professional help."
            CW "That’s why I’m risking it, Ken. You need a stranger."
            K "I’m pathetic to you, is that it? I’m just this loner you just can’t help but feel sorry for."
            CW "No, you’re a man who’s down on hard times. You need a lot to get back from this, and a lot more people to care, and I’m the first."
            CW "I don’t need to be the one to truly help you, the next one doesn’t either, or the next."
            CW "As long as we get through to you in the end, no matter how long the line may be."
            K "A savior complex? Heh, should have expected as much. Fine, have the truth."

label dialogue_work_3:
    K "…I just really despise you. Ever since I walked in through that door, 3 months ago, you’ve been on my case." with vpunch
    K "You're quite the dedicated nuisance, aren't you."
    K "{b}{i}You just can't leave me alone."
    K "The office dad, is that how you see yourself? heh yeah, that's pretty accurate. Middle-aged know-it-all who mistakes gray hairs for wisdom"
    K "{b}{i}What makes you think you can help?"
    K "You don't know me… or what happened to me… {b}{i}Why would yo-"
    CW "I know what it's like to lose someone?... {i}God!...do I know."
    K " {b}{i}...Lose...someone?"
    K "I- I don't-"
    CW "I've...heard the news. It’s...not something a man would talk about, no."
    CW "But it’s not something you can forget either. Ken, listen to me…you are not currently yourself."
    K "Wh-what are you talking about?"
    CW "Can you even tell me what has gotten you so down? Even a vague recollection of the events?"
    K "...."
    CW "Ken?...." with hpunch
    CW "KEN! Hey wait!" with hpunch
    scene hallway1 with hpunch
    pause .2
    scene hallway2 with hpunch
    pause .2
    scene hallway3 with hpunch
    "{b}Running away is the only thing you can do. Running away is the only thing you have done."

label dialogue_work_4:
    scene office_entrance with flash
    K "{i}I don’t veer into the deep end this often. He just really got on my nerves."
    K "{i}Wait, is that..."
    show office_entrance with slow_dissolve:
        blur 6
    show helen with slow_dissolve
    K "Ah, …Hey."
    H "You look worse for wear. What happened?"
    K " I- *ahem. Just a little workplace drama, nothing special. Why...Why are you here?"
    H "I’m always there where you need me..."
    H "So, have you had lunch yet?"
    K "No, I haven’t but that sounds like a great idea."
    H "Hehe, that always made you feel better. C’mon take us to Julie’s, I’m feeling for some Italian."
    jump act3_start

label act3_start:
    scene add_transition_here with slow_dissolve
    "{b}Try as hard as you want, as soon as you slip once, you’ll never get back up again."
    "{b}You are haggling with your mind, taking reality and unreality on the same plate."
    "{b}No comfort is enough. You are only delaying it."
    
    scene cafe with slow_dissolve
    K "{i}Ahhh…Nothing like the classic coffee aroma to make myself feel better."
    show cafe with slow_dissolve:
        blur 6
    show helen at slightright with slow_dissolve
    H " And yet, you’re still wearing that frown. What really happened, Ken?"
    K "Aww no…Not you too. Can’t a man feel his bad days by being sad these days?"
    H "I’m seriously asking, Ken."
    K "I’m sorry, maybe I am a bit more bothered than I seem. Helen..."
    menu:
        "You know I’ll always be honest to you.":
            show helen at center
            H "Then face me, and tell it to me straight."
            K "I will tell you, but I just can’t seem to do it now."
            H "Why not? Why can’t you face me?"
            H "Why can’t you..."
            hide helen with slow_dissolve
            jump dialogue_cafe_2
        "Maybe I’ll tell you later, once we get home…please?":
            show helen at center
            H "Always with the delays..."
            H "Can’t you be more punctual with your emotions this time?"
            K "I’m sorry...I just don’t think this is the best time or setting."
            H " I- right. Sorry, I agree with that."
            H "But once it is appropriate…Don’t delay it any longer."
            H "Please…don’t delay it any longer."
            hide helen with slow_dissolve
            jump dialogue_cafe_2

label dialogue_cafe_2:
    K "..."
    "*Ahem!Erm..mister? You’re standing in front of the door-… Oh! It’s you Ken! Welcome!"
    show felix at center with slow_dissolve
    K "What? Oh, I’m sorry for that. Umm…yeah, hi again. Can I have a table for one please?"
    F "Wait, Lemme do the thing first!"
    K "Right. Sure, go ahead."
    F "Welcome to Julie’s! Have a seat and enjoy your respite, I’ll be your server for today, Felix!"
    K "Ever the hyper one, aren’t you Felix? So, can I have that table for one?"
    F "Just one? Where’s your girlfriend? Aren’t you two inseparable?"
    K "Hahaha…No? I guess? Where did you hear that?"
    F "From the woman herself! Heh, she admitted as much about a month ago."
    K "Right. She does come here often."
    F "Only everyday! She always made my shifts a bit better. I do like to serve a beauty like her!"
    F "Plus she always gives me advice..."
    F "Although…She hasn’t been around lately, for about a few weeks now."
    F "{i}*gasp!{/i} Does she not like the-"
    K "Relax…She is just busy with…things. Too busy for even lunch."
    F "Ohhhh...But I miss her..."
    K "I miss her too..."
    F "Don’t you guys live together? Hehe, what a clingy couple."
    K "...yeah"
    K "I mean…Yeah! Hahaha we’re just a couple of sillies that can’t get enough of each other."
    K "...."
    F "Hmm? Are you two…alright?"
    menu:
        "Yes, I’d say so. Why? Does anything seem wrong?":
            F "No, I just thought it’s sad seeing you alone here."
            K "I get it, we do look good together..."
            F "You bet. You are a picturesque couple, if only you’ve seen yourselves."
            K "If only...I didn’t look too sad, did I? I just don’t want people to think I am."
            F "Are you not though? You looked genuinely sad, like a lost puppy."
            K "I just really miss her, that's all."
            F "What's keeping you from her? Did you two have a fight?...Just kidding! That's impossible."
            F "There, there..What really happened?"
            jump dialogue_cafe_3
        "Well…I think she is a bit too busy at work, but we’re alright.":
            F "That’s good to hear, you two are just so cute together!"
            F "That’s why I’m a bit sad to hear that you came in here alone today. Like there's something missing about you."
            K "I agree, although I really shouldn’t...I am my own person but..."
            F "-The two of you together is more than your sum. Ha! See, I can be sweet too!"
            F "So lover boy, how are you holding up with your missus being too busy for you, and even me!"
            K "{i}*Sigh*{/i} Not well to be honest. I haven’t seen her for..."
            K "..."
            K "Since...when did I last see her..."
            F "Hey...Long shifts at work wouldn’t make you miss her that much...What really happened?"
            jump dialogue_cafe_3
        "YES! Never been better!":
            F "Oh, please…didn’t your momma ever tell you to never lie to a cute barista?"
            K "No? Who even says that? Your just making up sayings to-"
            F "Ken....Ken, honey-"
            K "Don’t call me honey."
            F "Sorry. Ken, sweetie? Are you hiding something about you and Helen?"
            F "You can’t deny it now, it’s written straight in your face."
            F "So what gives? What happened?"
            K "She...isn’t around that much anymore."
            F "And that’s not just because she’s busy at work"
            F "{i}*gasp{/i} Did you two break up?"
            F "No...that's not quite right either you guys would never…the only would separate you two is..."
            K "Hahaha, what would that be?"
            F "{b}Death!"
            F "Just kidding! But seriously what is it? Is she sick?"
            K "...When exactly did you last see her?"
            F "About...two weeks ago, why?"
            K "Was I with her?"
            F "Nope. She came here alone..."
            F "Ken, you look unwell."
            jump dialogue_cafe_4

label dialogue_cafe_3:
    K "I’m...I don’t know what is happening to me."
    K "I feel like I’ve haven’t seen her for days but she had breakfast with me today, I’m sure of it. "
    F "Woah...Buddy you might be little too-"
    K "No, it's not like that, it's more than that. I...when is the last time you’ve seen her?"
    F "Let’s see, I remember it’s when we had that autumn sale...So yeah, about two weeks ago and actually a bit more."
    K "That’s around the same time where it started."
    F "What? What started?"
    K "The gaps in my memories, I always feeling disoriented..."
    K "And the feeling of missing Helen..."
    K "I..."
    F " Hey...relax a bit. Take small breaths if you can’t do big ones."
    F "Alright…Now what is it that you are about to say?"
    jump dialogue_cafe_4

label dialogue_cafe_4:
    K "I don’t think Helen is around anymore..."
    F "She...left?"
    K "I don’t know where, my mind is...was convinced that she's here, but she isn’t. She just isn’t."
    F "What’s the last thing you remember about her?"
    K "Well...as I said, it was 2 weeks ago and- God, we were fighting. My last memory of us was us fighting."
    F "Was it a bad fight? Bad enough for her to leave?"
    K "No…it was…heck it was about the groceries."
    K "I forgot to go on my way home. She was looking forward to cooking for us and- it was trivial."
    K "Just the fight that happens between anyone."
    F "Then…why did she leave you?"
    K "I don’t know, I don’t know where she is!"
    F "Ken, sweetie, I’ll need you to calm down…my manager is looking this way. Look…how about I get you something to go- and you-"
    F "Go sit in that comfy outdoor chair, and get your mind in order. What would you like for lunch, it’s my treat."
    menu:
        "Small pan pizza.":
            jump dialogue_cafe_4a
        "Risotto.":
            jump dialogue_cafe_4a
        "Carbonara.":
            jump dialogue_cafe_4a

label dialogue_cafe_4a:
    F "All right. Good choice, just- {i}*ahem*{/i} wait for our signature long-but-not-too-long fancy cafe serving time."
    scene cafe_outside with slow_dissolve
    "{b}The barista left you alone with your thoughts, for a while."
    "{b}The air kept you cool, and the sun hid behind the clouds, darkening the street by shades."
    "{b}The passing cars kept your ears occupied and the shuffling pedestrians, your eyes, but within, your mind was occupied. Thoughts"
    show cafe_outside with slow_dissolve:
        blur 6
    show felix with slow_dissolve
    "{b}Your mid-day lunch arrived, alongside Felix."
    "{b}He is on his lunch break as well. The two of you sat and ate in silence, though an unspoken agreement was felt. You will talk after you both have finished."

label dialogue_cafe_5:
    K "Now is a good time to talk. I- well, I’ll let you go first."
    F "It’s not everyday someone “forgets” weeks of their lives like yours so…"
    F "Are you sure nothing traumatic or unusual happened to you around the time Helen left?"
    K "I can’t say, I don’t even know what the missing parts are."
    F "Then how about let’s start with the pieces that aren’t! In the two weeks that followed, how did your mind fill in for the lack of Helen?"
    K "I imagined she was there, like, actually there, we talk, we banter, and the things I do alone"
    K "I try to contrive that it was her who did it for me."
    F "All because you didn’t have Helen at your side in reality…"
    K "Of course, it’s only ever when I’m alone or when in a public space with strangers."
    F "Where is she now, Ken? C’mon I don’t think any of your fights can get {b}THAT{/b} bad."
    F "Maybe she just vacationed in a place without the internet and now your mind’s going insane from the separation, Hahaha."
    K "Yeah…when she returns, I have nothing to worry about right?"
    F "Yep! That would fix you right up! All you have to do is sit tight and wait."
    F "Though…how long would that be…hmm…Did she ever take a long vacation before?"
    K "Sure. Overseas, with her family or me…the longest has been 8 days in Japan…"
    F "Oooh, no wonder you miss her, it’s been 2 weeks!" with vpunch
    F "A journey like that would have taken months to prepare. So wrack your head, c’mon where did she go?"
    K "She never mentioned anything like that? And I find it hard to believe that she would go on a vacation without me…"
    F "Then that theory is a bust huh…so she just up and vanished one, without a goodbye, and with no indication that she ever planned to leave…"
    F "And your parting is traumatic enough to do wonders on your brain…"
    show cafe_outside:
        blur 6
        xalign 0.5
        ease 2 zoom 1.1
    F "That leads me to believe that…"
    F "Helen…Oh no…Helen"
    pause 3
    show cafe_outside:
        blur 6
        xalign 0.5
        ease 2 zoom 1
    K "What? What did you think happened to her?"
    F "Why did I ever forget…two weeks ago was it? I…"
    K "No…"
    F "I..."
    pause 2
    F "I’ve…Got nothing! I really shouldn’t be a detective, which is why I’m not."
    F "I’m sorry I couldn’t be more of a help. But hey, as long as she’s out there somewhere, I know that she’ll come around, you two are perfect for each other!"
    F "Hmm?"
    F "Hey, Ken? You alright, buddy?" with hpunch
    F "Ken?" with hpunch
    K "I…I’ll pay you back for the lunch, okay? Many thanks, for the food, and the company."
    F "Oh…alright…wait you’re going already?"
    K "I’ve figured it out…about Helen"
    K "Again…Thank you, Felix."
    jump act4_start

label act4_start:
    scene act4introhere
    "{b}Your steps are uniform upon the ground. Walking. Your legs carry you back to your office."
    "{b}The sun was shining on your back, you wished it burned out already."
    scene office_entrance with slow_dissolve
    "{b}Beyond the glass door of the offices, you see a silhouette. Billy reclining on the metal benches. He is waiting for you."
    scene office_entrance with slow_dissolve:
        blur 6
    show billy with slow_dissolve
    CW " {i}*ahem*{/i} I- I think I should apologize to you."
    K "Well, I’m here. So go ahead."
    CW "I had the best of intentions earlier, but the way I handled myself was not the best…"
    CW "I did the equivalent of throwing you a lifesaver, yet not checking to see if you hang on."
    K "Hmm…"
    CW "Though it seems I helped, at least somewhat."
    CW "Your demeanor has changed now. You’re not trying to fool anyone now, especially yourself."
    CW "You’re letting your emotions run their natural course."
    K "Although…I do understand why I didn’t for so long."
    K "Billy. It hurts so bad."
    CW " I know, as it should. For what happened, it’s only the only thing a person can do."
    K "So I should just sit here and let it?"
    CW "Yeah…but not passively, no. You’re not a wounded man just drawing out his inevitable death."
    CW "You’re a fighter that's patiently waiting to heal, with every intention of going out again."
    K "Go out to what?"
    CW "Take on the world…I would say so?"
    K "…You’re just saying what comes to your mind, aren’t you?"
    CW "Am I that blatant? {i}*Heh*{/i} These wrinkles and gray hair are nothing but a sign for old age. You never really figure it out, even at my age."
    K "Still…you tried, I was unfair to you too, earlier."
    CW "Will you be okay though?"
    K "We’ll just have to see for ourselves."
    CW "I’m confident you will, you got it in you."
    CW "…Wanna a smoke?"
    K "{i}*chuckles*{/i} You know I don’t smoke. I got close to considering it today though."
    CW "I wouldn’t have given you one anyway."
    CW "I took the time to fill in your leave by the way. All you need to do is send it in."
    K "For tomorrow?"
    CW "For the next seven days. You’ll need it."
    K "Thank you. I’ll file this in and then I’ll leave early."
    CW "Where will you go? Straight to home?"
    K "No…There’s somewhere I’ll need to go first."
    CW "Then I wish you luck, my friend."
    jump act5_start

label act5_start:
    scene add_transition_here with slow_dissolve
    pause 5
    scene street_night with slow_dissolve
    K "{i}That day…The last time I saw her, she left the apartment early in the night. Just as we both got home from work."
    K "{i}Grocery shopping. Such a mundane task, I didn’t even look at her face when I said goodbye."
    K "{i}I was sure that I’ll see her again within the hour…"
    scene grocery_store_outside with slow_dissolve
    "{b}You walked here with a certain determination between each step."
    "{b}You did not wander in here, you are exactly where you put yourself."
    scene grocery_store_inside with fade
    booger_aids "*Catchy Jingle* There’s only so much time left!"
    booger_aids "So catch up on your groceries on the last day of our 3 day sale! *Catchy Outro*"
    K "Heh. I probably should buy some…"
    scene grocery_store_fridge with fade
    K "Now what am I missing? Chicken meat, pork, maybe some ice cream…and oh yeah…"
    K "You. I am missing you."
    show grocery_store_fridge with slow_dissolve:
        blur 6
    show helen with slow_dissolve
    H "Umm, hey…"
    K "Where have you been, Helen?"
    H "I’ve been {i}*ahem*{/i} I have been…"
    K "Dead"
    H "I have been dead."
    H "I passed away 2 weeks ago, the same day you last saw me."
    scene grocery_store_inside with slow_dissolve:
        blur 6
    show helen at left with slow_dissolve
    K "It wasn’t the last time I saw you, at least not alive."
    H "Ken…"
    hide helen
    scene dead_helen_lmao with flash
    K "Your face was…irreparable when they had me confirm the body. But it was you."
    K "It was you. And that was me, standing 3 feet away, as they pulled down the sheets over you."
    show grocery_store_outside with slow_dissolve:
        blur 6
    show helen with slow_dissolve
    H "I’m so sorry…I can’t even imagine."
    K "You can’t. I felt like I died right there with you."
    K "I wanted to."
    H "But you didn’t…The worst that you thought about doing to yourself, you never entertained any of them."
    K "I never had the chance to even think about it."
    K "You…I…whatever made me forget, it took over me quickly."
    H "But it's gone now? You remembered the whole story?"
    hide helen
    scene car_leaving with flash
    K "I remembered everything. You, saying goodbye. Me, oblivious to what’s gonna happen, watching TV. And then suddenly an hour or less later."
    K "The call. It was a police officer I think, he was stern and professional, he probably said similar things in similar situations."
    K "He made me come to the location, the U-turn on the 5th, with that pretty view of the bay."
    H "It didn’t hurt. It’s true, what they told you. The impact killed me long before the water did."
    scene isekai_moment with flash
    K "A truck was careening off the side, and your…our car was caught between it and the bay."
    H "I reacted as best I could, it wasn’t enough to survive…"
    scene car_crash with flash
    K "There was no surviving that."
    show grocery_store_outside with slow_dissolve:
        blur 6
    show helen with slow_dissolve
    H "I’m sorry…I’m sorry..If I hadn’t gone that night, I would be alive and I would be with you still."
    K "Don’t make me blame you…please, don’t."
    H "It was my fault, I killed Helen."
    K "What are you saying…stop it. Stop."
    H "I’m only saying what you deserve to hear. The things you didn’t get to."
    K "No one killed you, not even that truck driver, or the truck’s engine that failed. It was…It just happened."
    H "’m glad you see it that way, it’s for the best. There’s nothing I can do for you now…All I ever was, was just there to delay the inevitable."
    K "…What even are you?"
    H "I’m Helen, the one that is within you."
    H "When people…make a connection as much as we did, they give a part of themselves over to the other."
    H "We, apparently, gave up half of ourselves. I’m the half of Helen that's still in you…"
    H "Call me a ghost, a hallucination, well…both are fitting."
    K "You were quite the convincing illusion. Even now, I see you, I hear you, I feel you."
    K "What happens when I touch you?"
    H "You’ll go right through me. I’m just an illusion, Ken, something your mind came up with to soften the blow of losing me."
    K "But you talk, you can talk, right? Ask about my day. Be there for me. Have our usual banter on lazy days…you’re real enough for me, I don’t care if you’re-"
    H "KEN. Don’t. Don’t please…" with hpunch
    K "I promised you once, that if there’s still a chance, I’ll chase after you. That’s what brought me to this city in the first place."
    H "You know this isn’t even in the same ballpark. Ken…I’m nothing."
    H "I’m not anything anymore, I’m dead."
    H "Nothing is a replacement for me, not even me."
    K "I’ll be the judge of that…"
    H "KEN!" with hpunch
    H "Don’t! Do think about what you’re doing FOR ONCE!"
    K "WHY! Why did it happen to me…why did it happen to you!" with vpunch
    K "Traffic accident…It’s just unfair, life was good with you. And it was looking even better for the future."
    K "And now it’s gone…you’ll never live in this world again. And I feel it."
    K "My heart feels missing. So even if I can just have a sliver of you left..."
    H "It won’t do, Ken. It’s not a fair replacement."
    K "But it’s {i}{b}something{/b}{/i}. I’ll take that over nothing, over just…letting you go."
    H "You have to let me go. Move on. It’s the only way to go about this."
    K "I can’t. You said half of you was in me, that meant half of me was in you too."
    K "Half of me is dead. And I feel it, it's too much."
    K "And now, what will happen to my half of Helen? You’re telling me to move on, yet you’re a part of me now…"
    K "Should I just ignore it? Shut it off like it was never there? {i}{b}How can I forget you?"
    H "That part is dying too…slowly. You’re forcing it to stay, and it’s only hurting you and me."
    H " It will die off on its own, Ken. I’m not asking you to forget me, or to kill me a second time."
    H "All I’m asking for is for you to take it head on."
    H "Don’t be unfair to me, Not only did I die…"
    H "But I’m killing you too by dying. I want you to have the strength to smile again, to enjoy the moment…"
    H "...even without me."
    H "…Can you do it?"
    K "I…I can’t…"
    H "It would hurt me the most to find out that, by loving me, you’ll have it worse!"
    K " ……"
    pause 3
    K " …….."
    K "…We said to each other once that “Love is a curse, and so I will curse you-”"
    H " “-Curse you for eternity.” "
    K "Did that mean nothing after all?"
    H "Then let it be my mistake. Let it be my failure, my broken vow. I can’t curse you for life after all…not when it hurts you."
    K "So you’re setting me free?"
    H "You’ve been free the second I was dead. I’m just here to inform you."
    H "…"
    H "Heh-"
    H "Heh-HAHAHAHA"
    H "You were always the sappy one…"
    K "And you were always there to hold me back. Hahaha, even now, as a ghost you still have my well being as your primary concern."
    H "How could I not? After all, it’s our last day together. I better stay consistent till the end."
    K "The last day, huh? ...Okay."
    K "Okay."
    show helen with slow_dissolve:
        blur 3
    H "My image is already getting fainter, that means you’re doing it, you’re letting yourself live again"
    show helen with slow_dissolve:
        blur 5
    H "…I guess this is it. I will alw-"
    K "Now hold on. I’m NOT saying goodbye to the love of my life in a grocery store."
    hide helen
    show helen with slow_dissolve
    H "Okay…Good point."
    K "I have somewhere in mind…Come on."
    jump act6_start
    
label act6_start:
    scene black with slow_dissolve
    pause 5
    H "This place you're taking us…Is it far?"
    K "No. But I think you’ll like it."
    H "Hehe, well…lead the way, lover"
    pause 5
    K "We’re walking together again…"
    H "With me by your side, looking up at you."
    K "I’ll miss this."
    H "And for me, I’ll miss everything…but you most of all."
    pause 5
    K "I can’t call it sadness, but it’s not happiness either. I just feel like a great weight has been lifted off me, yet too much has been taken off, and now I feel weightless."
    H "Hmmm…Just call it bittersweet, and go on your day."
    K "Bittersweet huh? …Yeah, I guess that’s accurate."
    scene i_wish_this_was_manila_bay with slow_dissolve
    pause 5
    show i_wish_this_was_manila_bay with slow_dissolve:
        blur 6
    show helen with slow_dissolve
    H "Oh…It’s beautiful! And so cool too!"
    K "Not as cool and beautiful as you though"
    H "Oh, you shush. Hahaha"
    K " I’m glad you liked it though. I really was planning to take you here, before…yeah…"
    H "Well, I’m glad you took the chance to do it, regardless of the short time that we have left."
    K "Short time…yeah…even I can see it. You’re getting…fainter?"
    H "Yep, My appearance is finally fitting for what I am, a half-ghost, half-hallucination…or something between those. I’m still not sure."
    H "I don’t really care though. I’m just glad I was able to even exist for you even for just a couple of weeks more."
    H "Doing so prevented you from…following me. And I even saved you from the brink there."
    H "You were this close to going all psycho lover on me, and trying to keep a relationship with me, your dead fiance."
    K "Yeah…It was close. I’m not proud of what I could have become, It’s not what I considered possible for me…and that disturbs me so much."
    H "Hey, at least you listened to me in the end, that’s what matters."
    K "I was willing to chase after you, what I was not willing to do, is to hurt you and your soul."
    K "I love you only so far as that love doesn’t hurt."
    H "And I love you for that. Even with me as a ghost…you still can never betray me huh."
    K "I’d never disrespect your memory, never."
    H "Memory? I’m still right here you know."
    K "Um…yeah. But as a ghost."
    H "{i}*chuckles*{/i} I know I was testing you…I’m glad you took it too heart this quickly."
    K "Yeah…It's really the only thing I can do."
    H "Mhm."
    "{b}The two of you let silence comfort the scene. It’s somberness is not lost on both of you." 
    "{b}The soft sounds of the waves hitting the breakwater quickly overtook it however, yet not breaking its effect."
    "{b}You stayed like that for minutes, each one of you letting the moment pass without any event, and the next, and the next…"
    "{b}You however, felt her presence slowly, but noticeably, get fainter each time. This is your cue. Time to say-"
    K "Goodbye, Helen."
    H "Good…wait, not yet! I got something I wanna do first!"
    K "What? Okay…"
    H "Okay. I’m a ghost right?"
    K "Or my hallucination, but yeah I guess so. Why?"
    H "Ghosts. Can float."
    K "Yeah, they do that."
    H "Let me just…"
    K "Woah, HEY HELEN!"
    "{b}You watched as her image disappeared under the baywalk walls. You wondered why you screamed so loudly out of concern for a woman who is already a ghost."
    "{b}Then…you see her! A few feet away, her feet on no surface but the air."
    K "HAHAHAHA, you look like a water spirit!"
    H "Oh dear mortal…what has deemed you worthy of my countenance…{i}*pfft."
    H "Oh shut up, this is probably my only chance of doing this…"
    K "Alright, I’ll stop, you go have your fun. While I- Urhg- watch you from here."
    "{b}You climbed the top of the walls, putting you at eye level with the floating beauty…Her etherealness is already visible, the moonlight is passing through her."
    H "…You’ll be fine, I think. At this moment, I know you would love nothing else but to have me back. And thank you for that."
    K "And I’m glad you understand that. My efforts do pay off."
    H "Except for this one…"
    H "Seven years since…I let you in my walls. For a quarter of my life, you were my everything."
    H "And I was yours. I’m sorry I died. I know, I know it's not my fault, but still…"
    H "To ease my soul…I’m sorry."
    K "And you are forgiven…"
    H "Well…as I was saying. You’ll be fine. It’s you after all. You…get hot-headed, you’re pessimistic, you’re awkward as hell sometimes…but deep down, you are just the kindest person ever."
    H "You’re kind to everyone…even to yourself, I hope you never forget that."
    K "I’ll…be kind to myself, even without you, I’ll try to live again truly."
    H "Good…"
    K "But I’ll never forget you. You…made me who I am today. Half of what I am was once you. It may be filled by me again, or by another person, but the shape…the hollow mold, is of you."
    K "You will always have a place in my heart."
    H "I…Thank you…"
    H "And you made me the happiest during my life. No one can compare to you"
    H "So hold your head up high, because you made this girl’s life a good one. And I hope you have a better one, even with this setback."
    H "Live for me, alright? That’s the last thing I can say, I have nothing more."
    K "…I guess, I’ll see you whenever, in the next life."
    K "Goodbye, Helen."
    H "Goodbye, Ken. You are the love of my life. I loved you…"
    H "I love you."
    menu:
        "I love you too.":
            hide helen with slow_dissolve
            jump ew

label ew:
    hide helen with slow_dissolve
    menu:
        "And I always will.":
            jump ew2

label ew2:
    scene black with slow_dissolve
    jump act7_start

label act7_start:
    "START NA NG 7 boiiiiii"









    



label game_over:
    $ renpy.full_restart()