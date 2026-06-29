# ============================================================
#  GOT DROPPED INTO A GHOST STORY — STILL GOTTA WORK
#  Chapter 1: New Employee Initiation
# ============================================================
label chapter_1:
    scene expression "#ffffff"
    with fade

    show mascot at higher

    "What kind of a company is Daydream Inc.?"

    show mascot happy at higher

    "A company that produces insanely effective hair growth products?"

    show mascot disguised at higher

    "No! I heard they're a pharmaceutical company focused on cosmetics and skin treatments!"

    show mascot happy at higher

    "That's not all!!!"

    "We provide you with every medicine you could ever need!"

    show mascot happy at higher

    "We are a magical pharmaceutical company that makes drugs akin to miracles!"

    show mascot waving at higher

    "Daydream Inc."

    "See you at Daydream!"

    hide mascot with dissolve

    scene bg orientation_hall
    with fade

    scene bg orientation_hall with dissolve

    # play sound "chap1-applause.wav" # TODO: uncomment

    hr "And... you are the chosen candidates!"

    hr "Welcome to Daydream Inc., everyone!"
    hr "Our new employees, who have successfully passed a 145:1 competition, should be proud of themselves! Haha!"

    inner "So only ten thousand applied? Doesn't seem like that great of a ratio.."


    show employee1 at npc_size
    with dissolve

    employee1 "Excuse me, did you get that somewhere? Is the company giving those out?"

    inner "That wasn't towards me but the person next to me."

    hide employee1

    "The other employee in question has a strange black box, with a huge silver symbol embossed on it, looked like it had been carefully crafted."

    show black_box at prop
    with dissolve

    "...it caught the light in a way that felt deliberate."

    hide black_box
    with dissolve

    menu:
        "\"...\"":
            inner "Not worth acknowledging." # OR "Smart looking but this one's a dud."
            inner "How did that guy get his hands on that..."

        "\"Are you dumb? No way the company gave him that.\"":
            $ trust_score -= 5
            inner "No way a capitalistic company like the daydream inc is going to give every rookie something as expensive as that."
            employee1 "Wha-?! Ex-excuse me!"
            inner "Too loud. People are looking."
            inner "...that was mildly entertaining though."

            show hr annoyed at npc_size
            with dissolve

            "As if to cut someone off..."

    show hr excited at npc_size
    with dissolve


    hr "Now, lets begin the new employee orientation!"

    hr "You are the chosen candidates!"

    hr "In fact, only a select few of those who applied through this job posting have been gathered in Orientation Room A for this special session"

    hr "Congratulations! You have passed the aptitude test and have been assigned to the special team, the {b}Field Exploration Team{/b}."

    hide hr 
    with dissolve

    # TODO add murmur sounds

    employee1 "They've already made the assignments?"

    employee1 "Field Exploration Team? Does Daydream Inc. have a department like that?"

    employee1 "Field exploration… for a pharmaceutical company?"

    employee1 "Uh, it sounds like we're being exiled somewhere? Not the headquarters but a branch office? Are they trying to lure us in with fancy words…?"

    inner "Did these people seriously came in without knowing what their jobs will be?"

    inner "Wait what's that on..!"

    "Like a lightning bolt, text appeared on top of the employee holding the intricate black box."

    show field_exploration_text at prop
    with dissolve

    inner "...?"

    inner "Is this guy the mc or something?"

    inner "Suicide squad... that's exactly what Ms Jin said."

    hide field_exploration_text at prop
    with dissolve

    hr "Before official employment, there will be a brief probationary period, but don't worry, it won't be long! We will assess your practical abilities through an absolute evaluation."

    hr "Of course, full participation is necessary for a proper evaluation! Freeloading will not be tolerated!"

    inner "Here we go..."

    # TODO play doors shutting sound

    hr "Now, let's get started!"

    scene expression "#ffffff"
    pause 0.1
    scene bg orientation_hall
    pause 0.1
    scene expression "#ffffff"
    pause 0.1
    scene bg orientation_hall
    pause 0.1
    scene expression "#c8c8c8"
    pause 0.1
    scene bg orientation_hall
    pause 0.1
    scene expression "#888888"
    pause 0.1
    scene bg orientation_hall
    pause 0.1
    scene expression "#6E6E6E"
    pause 0.1
    scene bg subway_inside
    pause 0.1
    scene expression "#444444"
    pause 0.1
    scene bg subway_inside

    # desolate subway station

    question_mark "Passengers, thank you for using Abyss Transpo today… Our train will not halt."

    question_mark "Please pay attention to the announcements for a pleasant journey to your destination."

    "An unfamiliar announcement, with strange station names, started playing."

    employee1 "Is this some kind of VR? Did we really move?" # TODO sprite for him

    show scared_rookies at prop
    with dissolve

    "Many of the people who were in the auditorium seemed to be there still, which offered some comfort, leading to complacent reactions."

    "They wandered around the subway, looking for any sign of the company or someone from the event, or searched for doors that might open."

    "Soon, they began to get a better sense of the situation."

    hide scared_rookies at prop
    with dissolve

    show person_in_next_car at prop
    with dissolve

    "There are people in the next car! But… uh, the doors won't open? Is this some new technology?"

    hide person_in_next_car at prop
    with dissolve

    announcement "Welcome to Abyss Transpo"

    "D-Class Darkness that boasts a ridiculously high difficulty for escaping and one of the most infamous stories. The Field Exploration Team suffers endlessly."

    new_hires "Is this something like an escape room?"

    new_hires "Why would a pharmaceutical company that makes hair loss treatment bother with escape rooms for new sales recruits…?"

    $ ticker_msg = (
        "This stop is Sorrow, Sorrow Station."
        "                           The doors are on your right…"
        "                           The doors are opening."
        "                           The doors will close in 30 seconds. Once closed, they will never open again."
        "                           Passengers whose destination is Sorrow Station should disembark according to the announcement."
    )
    show screen ticker(ticker_msg)
    # show screen ticker("This stop is Sorrow, Sorrow Station.                                The doors are on your right…                          The doors are opening.                                    The doors will close in 30 seconds. Once closed, they will never open again.                                                     Passengers whose destination is Sorrow Station should disembark according to the announcement.")

    announcement "This stop is Sorrow, Sorrow Station."

    announcement "The doors are on your right…"

    announcement "The doors are opening."

    announcement "The doors will close in 30 seconds. Once closed, they will never open again."

    announcement "Passengers whose destination is Sorrow Station should disembark according to the announcement."

    hide screen ticker

    "The familiar voice calmly mixed strange words and phrases into the announcement."

    # pointing outside?

    new_hires "Look outside! It's just a subway station!"

    # outside, people by the door prop
    show doors_opening at prop
    with dissolve
    "Outside the train, the platform was clearly visible. It looked a bit dark and damp, but otherwise, it seemed like an ordinary subway station."

    "Relieved by this, two or three people moved toward the door."
    hide doors_opening at prop
    with dissolve

    inner "Idiots.. We just got teleported, and they think to a normal subway? The more normal it looks, the more alarm bells it should be ringing."

    # kim soleum neutral w briefcase
    guy_with_box "I think it's better if you don't get off."

    guy_with_box "You heard them say 'Sorrow Station'. There's no station like that in Korea. Anyone would think it's strange."

    # baek/viper
    quick_witted "Yeah, I think this guy's right. Maybe we should wait and see how things play out…"

    "The people who had been about to step off hesitated further."

    new_hires "Hey, the doors are closing!"

    # people moving out people_getting_off
    show people_getting_off at prop
    with dissolve
    "But the sound of the doors closing caused a few panicked individuals to impulsively jump out…"
    hide people_getting_off at prop
    with dissolve

    announcement "The doors are closing."

    "A chance to get off..!"
    menu:
        "\"Get me off now!\"":
            $ death_count += 1
            "Some who got off breathed a sigh of relief, some even waving at the ones back on the car."
            "The doors to the car closed with a creek."
            "Then.. just as the subway accelerated, something came dripping down."
            scene bg melting_ending
            with dissolve
            "A silver liquid came dripping down that melted flesh like water to cotton candy."
            pause 2.0
            centered "— ENDING: The Ones Who Left —"
            pause 2.0
            centered "You got off at Sorrow Station."
            centered "It was, in every sense, the last thing you did."
            pause 1.0
            jump bad_end_screen
        
        "\"Let's not do anything rash.\"":
            jump stay_in_car


label bad_end_screen:
    scene expression "#000000"
    with dissolve
    pause 1.0
    centered "GAME OVER"
    pause 1.0
    menu:
        "Try again.":
            jump start
        "Quit.":
            $ renpy.quit()

label stay_in_car:

    "The people who didn't get off sighed, watching the ones who did wave back at us from the platform."

    show people_waving at prop
    with dissolve

    "Some glanced at the guy who told them to wait, others muttered, suppressing curses."

    hide people_waving at prop
    with dissolve

    inner "..."

    "I- ..."
    menu:
        "\"I understood. In such a strange, unsettling situation, their instinct would be to flee without thinking.\"":
            $ meanness -= 5
            inner "They may have made the right decision."

        "\"I did not understand. In such a strange, unsettling situation, we should be trying to get more information.\"":
            $ meanness += 5
            inner "Pathetic."


    "A grotesque sight unfolded."
    #teardrops prop
    show teardrops at prop with dissolve

    "As soon as the people who got off turned around to move…"

    "Silver droplets suddenly poured from the ceiling and pillars of the platform, cascading down on them."

    # change background
    scene bg melting

    "It looked like giant teardrops."

    "But the countless silver droplets fell onto their bodies like molten metal, producing horrifying tearing sounds."

    "Screams. Convulsions. Silence."

    "Blood mixed with the silver liquid splattered against the windows."

    hide teardrops at prop with dissolve

    show screen ticker("The train is now departing from Sorrow Station")

    announcement "The train is now departing from Sorrow Station"

    scene bg sorrow_station_watching_dead

    "The last thing we saw outside the window."

    "In front of the sliding doors, now soaked in filth and blood, only the crushed remains of the new employees were left behind, twitching slightly."

    "It was the fate of those who chose wrong."

    hide screen ticker

    inner "Idiots."

    show screen ticker("Please pay attention to the announcements for a pleasant journey to your destination.")

    announcement "Please pay attention to the announcements for a pleasant journey to your destination."

    hide screen ticker

    show across at prop with dissolve

    "Finally, fear began to spread among the people as screams and shouts echoed around."

    "I look across from me."

    "8 people left in the carriage."

    show across at prop with dissolve

    jump chapter_2