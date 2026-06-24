# The script of the game goes in this file.

# # Declare characters used by this game. The color argument colorizes the
# # name of the character.

# define e = Character("Eileen")


# # The game starts here.

# label start:

#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.

#     scene bg room

#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.

#     show eileen happy

#     # These display lines of dialogue.

#     e "You've created a new Ren'Py game."

#     e "Once you add a story, pictures, and music, you can release it to the world!"

#     # This ends the game.

#     return

# ============================================================
#  GOT DROPPED INTO A GHOST STORY — STILL GOTTA WORK
#  Chapter 1: New Employee Initiation
# ============================================================

define mc   = Character("Mok Jeong", color="#ffcbcb")
define sys  = Character("SYSTEM", color="#ff4444")
define hr   = Character("HR Manager Shin", color="#aaddff")
define yuna = Character("Yuna", color="#ffccaa")       # Overachiever
define dohyun = Character("Do-hyun", color="#cccccc")  # Denier
define somi = Character("Somi", color="#ffaacc")       # Panicker / sweet
define junho = Character("Junho", color="#aaffcc")     # Nervous guy, survives
define rina  = Character("Rina", color="#ddaaff")      # Sharp girl, survives
define voice = Character("???", color="#6666ff")       # Anomaly / train voice

image mascot = "fox.png"
image mascot happy = "fox-jump.png"
image mascot waving = "fox-wave.png"
image mascot disguised = "fox-disguised.png"

transform higher:
    xalign 0.5
    yalign 0.3

# Stats
default contamination = 0
default sanity        = 100
default trust_score   = 0     # how much survivors trust MC (they shouldn't)
default chapter       = 1

# Internal monologue style — no name tag, italicized
define inner = Character(None, what_italic=True, what_color="#bbbbbb")


# ============================================================
label start:
# ============================================================

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

    # add applause
    play sound "chap1-applause.wav"

    hr "And... you are the chosen candidates!"

    hr "Welcome to Daydream Inc., everyone!"
    hr "Our new employees, who have successfully passed a 145:1 competition, should be proud of themselves! Haha! Now, lets begin the new employee orientation!"

    inner "So only ten thousand applied? Doesn't seem like that great of a ratio.."

    yuna "Excuse me, did you get that somewhere? Is the company giving those out?"

    inner "That wasn't towards me but the person next to me."
    inner "Front row. Blazer ironed sharp enough to cut glass. Already talking."
    inner "Overachiever. High energy. Poor threat assessment. Will be a problem."

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