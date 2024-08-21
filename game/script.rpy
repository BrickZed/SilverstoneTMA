define fadehold = Fade(0.5, 1.0, 0.5)
define fadeholdlong = Fade(0.5, 5.0, 0.5)
define dissolvelong = Dissolve(2.0)
define dis = { "master" : Dissolve(0.5) }
define dislong = { "master" : Dissolve(3.0) }

transform offscreenbottom:
    xpos 0.5 xanchor 0.5 ypos 2.0 yanchor 1.0

transform offscreenbottomright:
    xpos 2.0 xanchor 1.0 ypos 2.0 yanchor 1.0

transform furtherleft:
    xpos 0.57 xanchor 1.0 ypos 1.0 yanchor 1.0

transform furtherright:
    xpos 1.1 xanchor 1.0 ypos 1.0 yanchor 1.0

transform show_fade:
    alpha 0.0
    xcenter 0.5 yoffset 0
    easein 1.0 alpha 1.0

transform show_fadeout:
    alpha 1.0
    xcenter 0.5 yoffset 0
    easein 1.0 alpha 0.0

define windowhidecut = _window_hide(trans=None, auto=False)

default Veggie = False
default Bacon = False
default Coffee = False
default Clyde = False
default Riley = False

default romance_points = 0

default persistent.EndingGood = False
default EndingNormal = False
default EndingBad = False
default EndingExtra = False

define config.menu_include_disabled = True

# SEPARATING SCRIPT AND DEFINITIONS

label splashscreen:
    scene bg black
    pause 1.0
    show splashscreen with dissolvelong
    pause 4.0
    hide splashscreen with dissolvelong
    return

label start:

    jump morning1

    # This ends the game.

    return
