# ============================================================
#  GOT DROPPED INTO A GHOST STORY — STILL GOTTA WORK
#  script
# ============================================================

init python:
    gui.textbox_alpha = 0.5

define player   = Character("Lee Kiyoung", color="#ffcbcb")
define sys  = Character("SYSTEM", color="#ff4444")
define employee1 = Character("Employee", color="#585858")
define hr   = Character("HR Manager Shin", color="#335d79")
define new_hires = Character("New hires", color="#465966")
define exploration_records = Character("Exploration records", color="#0252fd")


define guy_with_box = Character("New hire with box", color="#6d6c6c")
define quick_witted = Character("Quick witted new hire", color="#cccccc")
define baek_saheon = Character("Baek Saheon", color="#052914")     # baek_saheon, viper
define kim_soleum = Character("Kim Soleum", color="#1B2457")     # baek_saheon, viper
define go_yeongeun = Character("Go Yeongeun", color="#ffccaa")       # doctor who died early
define dohyun = Character("Do-hyun", color="#cccccc")  # Denier
define somi = Character("Somi", color="#ffaacc")       # Panicker / sweet
define rina  = Character("Rina", color="#ddaaff")      # Sharp girl, survives
define announcement = Character("Annoucement", color="#6666ff",  what_font="fonts/Inconsolata-Regular.ttf")       # Anomaly / train voice what_font="fonts/ShareTechMono-Regular.ttf"
define question_mark = Character("???", color="#cefffb")       # Anomaly / train voice what_font="fonts/ShareTechMono-Regular.ttf"

screen ticker(msg):
    frame:
        xalign 0.0
        yalign 0.0
        xfill True
        background "#000000cc"
        xpadding 20
        ypadding 8
        text msg:
            color "#6666ff"
            font "fonts/Inconsolata-Regular.ttf"
            size 22
            xsize 5000
            textalign 0.0
            layout "nobreak"
            at ticker_scroll

transform ticker_scroll:
    xpos 1280
    linear 20.0 xpos -1280
    repeat

# bg
image bg orientation_hall = "images/chap1/bg/bg_orientation_hall.png"
image bg subway_inside = "images/chap1/bg/bg_subway_car.webp" # bg_subway_inside.png drawn
image bg melting = "images/chap1/bg/melting.png"
image bg sorrow_station_watching_dead = "images/chap1/bg/sorrow_station_watching_dead.png"

# ending
image bg melting_ending = "images/chap1/bg/melting_ending.png"


# props
image black_box = "images/chap1/prop/black_box.png" 
image field_exploration_text = "images/chap1/prop/field_ex_text.png" 
image scared_rookies = "images/chap1/prop/scared_rookies.png" 
image doors_opening = "images/chap1/prop/doors-opening.png" 
image people_getting_off = "images/chap1/prop/people_getting_off.png" 
image person_in_next_car = "images/chap1/prop/ppl_in_next_car.png" 
image people_waving = "images/chap1/prop/people_waving.png" 
image teardrops = "images/chap1/prop/teardrops.png" 
image across = "images/chap1/prop/across.png" 

# characters
image mascot = "images/char/fox.png"
image mascot happy = "images/char/fox_jump.png"
image mascot waving = "images/char/fox_wave.png"
image mascot disguised = "images/char/fox_disguised.png"

image employee1 = "images/char/npc1.png"
image hr excited= "images/char/presenter.png"
image hr annoyed= "images/char/presenter_annoyed.png"

# kim soleum
image kim_soleum neutral = "images/char/kim_soleum.png"

# go yeongeun 
image go_yeongeun neutral = "images/char/go_yeongeun_neutral.png"
image go_yeongeun scared = "images/char/go_yeongeun_scared.png"
image go_yeongeun happy = "images/char/go_yeongeun_happy.png"

# baek saheon 
image baek_saheon netural = "images/char/baek_saheon_neutral.png"
image baek_saheon smile = "images/char/baek_saheon_smile.png"

# Transforms

transform higher:
    xalign 0.5
    yalign 0.3

transform npc_left:
    xalign 0.2
    yalign 1.0
    zoom 0.82

transform npc_center:
    xalign 0.5
    yalign 1.0
    zoom 0.82

transform npc_right:
    xalign 0.8
    yalign 1.0
    zoom 0.82

transform speaking:
    zoom 0.82
    matrixcolor TintMatrix("#ffffff")

transform not_speaking:
    zoom 0.82
    matrixcolor TintMatrix("#888888") * BrightnessMatrix(-0.3)

# Stats
default contamination = 0
default sanity        = 100
default trust_score   = 0     # how much kim soleum trusts MC (aka none)
# start off with 20, if u reach 0, you get to do nice things
default meanness   = 20     # how mean the player character is (unlocks mean dialogue options, or apathetic)
default death_count       = 1
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