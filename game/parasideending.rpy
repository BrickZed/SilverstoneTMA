label paradiseending:
    "My feet shift the longer I wait; my hands constantly picking at the back of my fur.{w} What am I doing?"

    "This could very well be the last time I ever see Walt and I'm just... standing in front of my door like an idiot?"

    "No. It's time I take a chance."

    "I skid across the floor as I race to my room, throwing on my coat before I twist the doorknob and head outside."

    window hide
    scene bg black
    with fade
    play sound "Running.ogg" loop
    show bg normalend1
    with dissolve

    window auto show
    "The lights under the carports seem brighter as I make my way towards the bus stop, almost as if they're dancing with hope."

    "My pawpads skate across the ice-cold concrete; I only now realize I forgot my socks and shoes."

    window hide
    show bg goodending1
    with dissolve

    window auto show
    "I feel full of life, as if I'm climbing up a rope on the edge of a cliff hundreds of feet high."

    "{font=HEROLD.otf}{size=-2}You're going to kill yourself, boy.{/size}{/font}"

    "If this is how my life ends, I'm fine with it."

    "{font=HEROLD.otf}{size=-2}So you just want to die?{/size}{/font}"

    "At least if I die, it will be next to Walt.{w} We may not know a lot about each other, but these past 24 hours have felt like a century."

    "{font=HEROLD.otf}{size=-2}Such a fool.{/size}{/font}"

    window hide
    show bg goodending2
    with dissolve

    window auto show
    stop sound fadeout 1.0
    "I stare blankly at the bus sign. There's no one sitting on the bench."

    "I missed him."

    "I cave into my knees, my head in my hands.{w} I was too late."

    "I can feel the eyes on me from the cars driving by, but it doesn't matter.{w} I fucked up, and this is the price I pay."

    w "\"Asher?!\""

    play sound "Paw.ogg"
    "A paw lands on my shoulder, and I whirl around.{w}{nw}{done}"

    show walt staringsideneutralclothed
    with dis
    "A paw lands on my shoulder, and I whirl around.{fast} He's still here, holding a bag from the convenience store down the street."

    "I let out a small laugh, wiping away the tears coating my eyes.{w} I didn't miss him after all."

    w neutraltalkingsideclothed "\"Are you okay? What are you even doing out here?\""

    "His eyes. Those gentle, amber eyes enrapture me as they meet with my dull emerald ones.{w} A bit of fear pangs inside my heart wondering if he would even say yes if I told him how I felt."

    "{font=HEROLD.otf}{size=-2}Just go back already.{/size}{/font}"

    "I take a deep gulp, and sway back and forth trying to find the words.{w} I can't feel them. My throat is empty."

    "{font=HEROLD.otf}{size=-2}I'll help.{/size}{/font}"

    menu:
        "Go Back":
            "{font=HEROLD.otf}{size=-2}I take a few steps backward, towards the apartment you came from.{/size}{/font}"

            "{font=HEROLD.otf}{size=-2}I already have the words locked in for you to reach a final goodbye.{/size}{/font}"

            a hangoverponderingclothed "\"Eh... never mind, it's not that important.{w} Hope you have a safe trip.\""

            "That's not what I want to say. {font=HEROLD.otf}{size=-2}But it's what you have to say.{/size}{/font}"

            w staringtalkingneutralclothed "\"Wait!\""

            "The wolf grabs my arm {font=HEROLD.otf}{size=-2}and I have to fight it.{/size}{/font}"

            w neutraltalkingclothed "\"You didn't come out over here without your shoes just to say goodbye, did you?!\""

            w neutral2clothed "\"What's going on?\""

            "Who the fuck even are you?{w} This is my life and if I fuck it up, I fuck it up."

            window hide
            pause 2.0
            window auto show
            "{font=HEROLD.otf}{size=-2}Is this what you really want, boy?{/size}{/font}"

            window hide
            pause 2.0
            window auto show
            "{font=HEROLD.otf}{size=-2}Then I hope you have a happy fucking life.{/size}{/font}"

            window hide
            pause 1.5
            play sound "Stab.ogg"
            show overlaylight onlayer overlay
            pause 1.0

            window auto show
            "I almost throw up as I feel... {i}something{/i} leave me.{w} I don't know what it is, but... everything is calm."

            "The only disturbance is the burning bile coating my throat.{w} But I least know what I need to say."

            a hangoverupsetclosedclothed "\"Walt, I...{w}{nw}{done}"

            a hangoversurprisedclothed "\"Walt, I...{fast} Bear with me, I've... {i}never{/i} done this before.\""

            play sound "BusArrive.ogg"
            show walt staringneutralclothed
            "It's then when the bus arrives. It finally sinks in that it's now or never."

            d "\"\'Ya gettin\' on or what?\""

            w angrysideclosedclothed "\"H-hang on!\""

            w neutraltalkingsideclothed "\"What were you saying, Asher?\""

            "I look up at the raccoon bus driver, who's giving me those \'evil eyes\' as he taps his foot on the pedal.{w} A deep inhale and then—"

            a hangoverupsetclosedclothed "\"Give me a chance, please...\""
            
            scene cg goodend with dissolvelong
            play music "Connection.ogg" fadein 1.0

            "I stare down at the sidewalk, unaware of Walt's eyes widening; trying to connect to mine. My ears are a hot red, and I can feel my hands getting sweaty as Walt grabs one of them."

            w "\"Did I... Did I hear that right?{w} Asher?\""

            "I turn towards the bus, averting my gaze even more. All I can think of is how much of a teenager I resemble right now."

            "Finally, Walt tilts my muzzle over to meet him and... he's smiling. Did that actually work?"

            a "\"Today has been a whirlwind of emotions and...{w}{nw}{done}"

            a "\"Today has been a whirlwind of emotions and...{fast} somewhere along the line, I think I fell for you.\""

            "I cringe inside at how I must sound. Despite the desperation in my tone, the words that come out are the most cliched I've ever said."

            w "\"So, you've felt it, too?\""

            "Finally I feel the electricity between us. It doesn't feel like this supernatural pull anymore. We both had the same feelings for each other this whole time."

            w "\"Not going to lie, I was hoping you would come out here and stop me.\""

            w "\"It might have been why I went over to the convenience store... to miss the bus on purpose."

            a "Well, you failed at that, asshole."

            scene bg goodending2
            show walt grinningclosedsideclothed
            with dissolvelong
            play sound "BusLeave.ogg"

            "The bus pulls away as we start to laugh at each other; the raccoon hurling an expletive at us as the door closes."

            show walt smilingclothed
            "Walt wraps his fingers along mine, swaying his bag of food and drinks around as he guides me back to my apartment."

            hide walt smilingclothed with dissolve
            "It's where everything started and where everything will end."

            show bg black with dislong
            stop music fadeout 3.0
            "I don't know how long we will last, but all I can hope for are the best days of my life."
            $ persistent.EndingGood = True
            $ quick_menu = False
            window hide
            pause 3.0
            jump credits
