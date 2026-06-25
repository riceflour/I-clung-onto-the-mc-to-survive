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
            emp "Wha-?! Ex-excuse me!"
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

    show black_box at prop
    with dissolve

    inner "...?"

    inner "Is this guy the mc or something?"

    inner "Suicide squad... that's exactly what Ms Jin said."

    hide black_box at prop
    with dissolve

    inner "Here we go..."

    hr "Before official employment, there will be a brief probationary period, but don’t worry, it won’t be long! We will assess your practical abilities through an absolute evaluation."

    hr ""

    hr "Great question! That's actually on slide forty-two—"

    dohyun "Is this going to go much longer? I have a 2PM call."

    inner "Guy two seats to my left. He said '2PM call' like it's a shield."
    inner "It isn't."

    hr "We'll try to keep things moving! Now, if everyone could please check that your lanyards are—"

    "The lights went out."

    "Not a flicker. Not a stutter."
    "One moment: fluorescent brightness, motivational posters, HR Manager Shin mid-sentence."
    "The next: nothing."

    somi "W— what happened?"
    dohyun "Power outage. Obviously. Someone call facilities."
    yuna "I'll handle it—"

    inner "Nobody handle it."
    inner "Something is wrong with the air."

    sys "[ NOTIFICATION ]"
    sys "[ You have been selected to participate in a Ghost Story. ]"
    sys "[ Survival is not guaranteed. Clocking out is the objective. ]"
    sys "[ Good luck, employee #0047. ]"

    mc "..."

    inner "Hm."

    "The floor disappeared."