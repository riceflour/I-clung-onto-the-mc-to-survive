# ============================================================
#  GOT DROPPED INTO A GHOST STORY — STILL GOTTA WORK
#  Chapter 1: New Employee Initiation
# ============================================================

init python:
    gui.textbox_alpha = 0.5

define mc   = Character("Mok Jeong", color="#ffcbcb")
define sys  = Character("SYSTEM", color="#ff4444")
define employee1 = Character("Employee", color="#585858")
define hr   = Character("HR Manager Shin", color="#335d79")
define yuna = Character("Yuna", color="#ffccaa")       # Overachiever
define dohyun = Character("Do-hyun", color="#cccccc")  # Denier
define somi = Character("Somi", color="#ffaacc")       # Panicker / sweet
define junho = Character("Junho", color="#aaffcc")     # Nervous guy, survives
define rina  = Character("Rina", color="#ddaaff")      # Sharp girl, survives
define voice = Character("???", color="#6666ff")       # Anomaly / train voice

image bg orientation_hall = "images/bg_orientation_hall.png"
image bg subway_inside = "images/bg_subway_inside.png"

image black_box = "black_box.png" 
image field_exploration_text = "field_ex_text.png" 


image mascot = "fox.png"
image mascot happy = "fox_jump.png"
image mascot waving = "fox_wave.png"
image mascot disguised = "fox_disguised.png"

image employee1 = "npc1.png"
image hr excited= "presenter.png"
image hr annoyed= "presenter_annoyed.png"

# Transforms

transform npc_size:
    xalign 0.2
    yalign 1.0
    zoom 0.82

transform higher:
    xalign 0.5
    yalign 0.3

# Stats
default contamination = 0
default sanity        = 100
default trust_score   = 0     # how much kim soleum trusts MC (aka none)
default meanness   = 0     # how mean the player character is (unlocks mean dialogue options)
default chapter       = 1

transform prop:
    xalign 0.5
    yalign 0.35
    zoom 1

# Internal monologue style — no name tag, italicized
define inner = Character(None, what_italic=True, what_color="#999999")


# ============================================================
label start:
# ============================================================
# in chapter1.rpy
    jump chapter_1