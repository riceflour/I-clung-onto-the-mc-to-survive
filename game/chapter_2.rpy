# ============================================================
#  GOT DROPPED INTO A GHOST STORY — STILL GOTTA WORK
#  Chapter 2: Next station
# ============================================================ # appendix station

# props
image notepad = "images/chap2/prop/notepad.png" 

label chapter_2:
    scene bg subway_inside with fade

    show screen ticker("This stop is Resentment, Resentment Station.")

    announcement "This stop is Resentment, Resentment Station."

    announcement "The doors are to your right.."

    inner "If sorrow station was a bust, resentment station sounds even worse."

    new_hires "That station name, Resentment… it sounds like the kind of resentment people feel when they're angry, right?"

    "The people who had panicked after witnessing two live dismemberments were starting to regain their composure and talk."

    new_hires "Ha, no cell service, no data… seriously, what is going on…?"

    show notepad at prop with dissolve

    inner "What is that..."

    inner "Something like a notepad was flying around in front of the employee with the box, also the employee who convinced the others to stay."

    "1st Place : Dark Exploration Records Real Merch Box"

    ": Daydream Inc. identification code - Qterw-D-16"

    hide notepad at prop with dissolve

    inner "Huh..."

    "I could see information about this situation on top of that guy's head."

    "What seemed like exploration records scorlled atop his head."

    exploration_records "Dark Exploration Records / Ghost Story"

    player "A ghost story huh?"

    exploration_records "/ Welcome to Abyss Transpo"

    exploration_records "3.2 Exploration Records (up to 56 entries)"

    "From the text perodically changing it's clear that this text, the employee is reading it on his phone. Somehow I see it atop his head."

    exploration_records "1- Stations named after colors like red, yellow, blue: Two-person escape success (Attempt : Blue Station)"

    exploration_records "2- Stations named after body parts like left arm, cornea, heart: No recorded escape success (Attempt : Cochlea Station)"

    exploration_records "3- Stations named after serial killers like ■■, ■■■■, ■■■: Twelve-person escape success (Attempt : ■■■■ Station)"

    exploration_records "4- Stations named after years like 2008, 2012, 2016: No recorded escape success (Attempt : 2024 Station)"

    exploration_records "5- Stations named after illnesses like asthma, stroke, glaucoma: : Three-person escape success (Attempt : Cold Station)"

    inner "From people getting melted at a station to seeing text atop someone's head, so this is a ghost story!"

    inner "Okay so a station's positivity has no correlation with escape success rate-"

    show kim_soleum neutral at npc_center
    show go_yeongeun neutral at npc_right
    with dissolve

    show kim_soleum neutral at npc_center, speaking
    show go_yeongeun neutral at npc_right, not_speaking

    guy_with_box "You mentioned a ghost story?"

    show kim_soleum neutral at npc_center, not_speaking
    show go_yeongeun neutral at npc_right, speaking

    new_hires "Ha.. like the ones on youtube" #female doc

    show go_yeongeun neutral at npc_right, not_speaking

    show kim_soleum neutral at npc_center, speaking

    guy_with_box "Could you tell me more? This doesn't seem like a normal situation, so it's probably best to share any information we have."

    show kim_soleum neutral at npc_center, not_speaking

    inner "Trying to bring up those exploration records?"

    show go_yeongeun neutral at npc_right, speaking
    new_hires "It's not really information… it just feels like everything is straight out of a ghost story. The lecture hall suddenly turned into a subway, and people… died like that." # female doc

    show go_yeongeun scared at npc_right, speaking
    "Her face turned slightly pale, likely remembering the insane dismemberment that happened just moments before."

    new_hires "Ah, I'm sorry. I didn't mean to suddenly—"

    player "No, I've seen something on online forums too."

    show baek_saheon smile at npc_left, speaking

    new_hires "Um, you were sitting next to me earlier, right?" # baek neutral

    "It seemed new hire wasn't part of any of the other conversations happening around us. He rubbed the back of his neck and glanced between the woman I was talking to and me, and the employee with the box."

    baek_saheon "My name is Baek Saheon."

    hide screen ticker

    show baek_saheon neutral at npc_left, not_speaking
    show go_yeongeun neutral at npc_right, not_speaking
    show kim_soleum neutral at npc_center, speaking

    guy_with_box "..!" #

    exploration_records "Dark Exploration Records / Daydream Inc: : An employee of Daydream Inc. in <Dark Exploration Records>"

    exploration_records "Final rank - Section Chief           Of these, 17 are special cases recorded in the wiki."

    inner "This guy's gonna end up as a section chief? Maybe I should follow him instead."

    show kim_soleum neutral at npc_center, not_speaking
    show go_yeongeun neutral at npc_right, speaking

    go_yeongeun "Given the situation, we might as well introduce ourselves. I'm Go Yeongeun."

    show kim_soleum neutral at npc_center, speaking

    kim_soleum "I'm Kim Soleum."

    player "Lee Ki-Young"

    "While we were talking, it seems others were talking amongst their groups too. One group was trying to communicate with the other car."

    show kim_soleum neutral at npc_center, not_speaking
    show go_yeongeun neutral at npc_right, speaking

    go_yeongeun "Ah, those people.. it looks like they're trying to communicate with the front car?"

    "It seems communication is not allowed, exactly what the exploration records also said."

    new_hires "What should we do? We can't communicate with the front car at all. And it looks like there's a fight breaking out up there…"

    inner "A fight? Hopefully some people get off at the next station. No one got of at resentment station. Tsk"

    "As the tension and anxiety among the passengers grew, another station announcement played."

    "But this time..."
    # TODO add scren scroller
    announcement "This stop is Euphoria, Euphoria Station."

    new_hires "Doesn't 'euphoria' sound kind of… positive? Maybe…"

    "From the sudden slience and comtemplating looks, it seems many were going to get off at euphoria station."

    announcement "The doors are on your left…"