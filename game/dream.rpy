label dream:
    if romance_points >= 4:
        jump steps
    elif romance_points <= -4:
        jump inside
    elif romance_points < 4 and romance_points > -4:
        jump outside

label steps:
    pause 2.5
    scene bg steps
    with dissolvelong
    "As I open my eyes, I notice that I'm outside of my apartment."

    "I don't feel awake, however. My body still feels heavy and my mind can't fully bring itself together."

    "I try to go to my door, back inside, but that's when I realize."

    "There's no snow... and it's bright out."

    "The sunlight isn't a piercing white like it usually is, though.{w} It's a strange deep red."

    "{sc=3}{font=HEROLD.otf}You've finally noticed?{/font}{/sc}"

    "I feel my throat dry as I hear the voice in my head.{w} It sounds like my own, just deep and scratchy."

    "{sc=3}{font=HEROLD.otf}You like that wolf, don't you?{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}Denying you do is useless, you know.{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}I can hear everything you're thinking right \nnow.{/font}{sc}"
    window hide
    pause 3.0

    window auto show
    "{sc=3}{font=HEROLD.otf}Yet this... isn't what I expected to see in \nhere.{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}Compared to the other possibilities you could \nhave conjured up...{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}This is... BORING.{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}This is all I will tell you.{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}Your life will end if you go down these steps.{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}You got that?{/font}{sc}"
    window hide
    pause 3.0

    window auto show
    "{sc=3}{font=HEROLD.otf}Good.{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}Now... it's time to wake up.{/font}{sc}"

    jump night1

label inside:
    pause 2.5
    scene bg blinds
    with dissolvelong
    "As I open my eyes, I notice that I'm staring out my bedroom window."

    "I don't feel awake, however. My body still feels heavy and my mind can't fully bring itself together."

    "While trying to remember how I even got into bed, I realize something."

    "There's no snow... and it's bright out."

    "The sunlight isn't a piercing white like it usually is, though.{w} It's a strange deep red."

    "{sc=3}{font=HEROLD.otf}You've finally noticed?{/font}{/sc}"

    "I feel my throat dry as I hear the voice in my head.{w} It sounds like my own, just deep and scratchy."

    "{sc=3}{font=HEROLD.otf}You like that wolf, don't you?{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}Or, you're trying to convince yourself you do.{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}Arguing about it with me is useless.{/font}{/sc}"

    "{sc=3}{font=HEROLD.otf}I can hear everything you're thinking right \nnow.{/font}{sc}"
    window hide
    pause 3.0

    window auto show
    "{sc=3}{font=HEROLD.otf}This is comfortable for you, isn't it?{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}You fit into the stereotypical archetype.{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}You're the lone FUCKING wolf.{/font}{sc}"
    window hide
    pause 3.0

    window auto show
    "{sc=3}{font=HEROLD.otf}But sometimes, normality is dangerous.{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}This is all I will tell you.{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}Your life will end if you go to sleep here \ntonight.{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}You got that?{/font}{sc}"
    window hide
    pause 3.0

    window auto show
    "{sc=3}{font=HEROLD.otf}\"Good.\"{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}\"Now... it's time to wake up.\"{/font}{sc}"

    jump night1

label outside:
    pause 2.5
    scene bg dreamdumpster
    with dissolvelong
    "As I open my eyes, I feel a rush of cold air as I stare at the apartment dumpsters."

    "I don't feel awake, however. My body still feels heavy and my mind can't fully bring itself together."

    "While trying to remember how I even got out here, I realize something."

    "There's no snow... and it's bright out."

    "The sunlight isn't a piercing white like it usually is, though.{w} It's a strange deep red."

    "{sc=3}{font=HEROLD.otf}You've finally noticed?{/font}{/sc}"

    "I feel my throat dry as I hear the voice in my head.{w} It sounds like my own, just deep and scratchy."

    "{sc=3}{font=HEROLD.otf}You like that wolf, don't you?{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}You're at least somewhat smitten with him.{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}I'm truly taking in your equivocation.{/font}{/sc}"

    "{sc=3}{font=HEROLD.otf}I can hear everything you're thinking right \nnow.{/font}{sc}"
    window hide
    pause 3.0

    window auto show
    "{sc=3}{font=HEROLD.otf}This is uncomfortable for you, isn't it?{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}You want to be with him, but you're fucked \nin the brains.{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}You don't want to think for yourself.{/font}{sc}"
    window hide
    pause 3.0

    window auto show
    "{sc=3}{font=HEROLD.otf}But sometimes, you need to grow a pair and make \ndecisions.{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}This is all I will tell you.{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}Your life will end if you go out to this dumpster \ntonight.{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}You got that?{/font}{sc}"
    window hide
    pause 3.0

    window auto show
    "{sc=3}{font=HEROLD.otf}Good.{/font}{sc}"

    "{sc=3}{font=HEROLD.otf}Now... it's time to wake up.{/font}{sc}"

    jump night1