label night1:
    stop music
    show bg couch
    "My eyes burst open, catching the fading glow of the candles."

    "My fur is stained with sweat, my mind whirling from what I just dreamt up."

    "I pat my cheeks to wake myself up fully and sit properly on the couch.{w} I seemed to have fallen over while I was sleeping."

    w "\"Hey, Asher?\""

    "It's only now I notice that Walt is by the TV, putting his shoes on and carrying his backpack."
    show bg afternoontv
    show walt neutral2clothed
    with dissolve

    w neutraltalkingclothed "\"The snow has cleared up, so I'm gonna head out now.\""

    show walt neutral2clothed
    "My eyes shoot over to the clock. Sure enough, it's past eleven already."

    w neutraltalkingsideclothed "\"I think you were just really exhausted from everything that happened earlier.\""

    show walt neutralsideclothed
    "He says as if he can read my mind.{w} Still, I was so tired that I almost slept for ten hours?"

    "I follow Walt over to the door, and I can feel something in my heart pulling at me."

    "Almost like I'm toeing the line between life and death."

    scene bg black
    with fadehold
    show eveninganimation at show_fade
    pause 5.0
    show eveninganimation at show_fadeout

    jump night2
label night2:
    if romance_points >= 5:
        scene bg door
        show walt smilingsideclothed
        with fadehold

        "My ears droop as we appear before the door, and I think I realize what the feeling is."

        "I don't really want Walt to leave."

        "I can't just spring a confession on him, though. That would be unfair to him, especially since he's here on a trip."

        w neutraltalkingsideclothed "\"Hey, you alright?\""

        show walt neutralsideclothed
        "I jump at the question, quickly sucking up my self-pitying and throwing my arm behind my head."

        a hangoversmilingclothed "\"Oh, yeah! I'm doing good!\""

        w smilingsideclothed "\"Ah, okay.{w}{nw}{done}"

        w grinningclosedsideclothed "\"Ah, okay.{fast} Was a bit worried you were going to miss me.\""

        "I mean, I am."

        w smilingsideclothed "\"Kidding, of course.\""

        w neutraltalkingside2clothed "\"But if I ever do come back to Silverstone...\""

        w smilingsideclothed "\"I'll be sure to come back here.\""

        play sound "DoorOpen.ogg"
        "Why do I feel tears welling up in my eyes? He's practically a stranger..."

        w grinningclosedsideclothed "\"Thanks for letting me stay here, Asher!\""

        show walt grinningclosedsideclothed at show_fadeout
        play sound "DoorClose.ogg"
        window hide
        pause 5.0

        menu:
            "Go After Him":
                jump paradiseending
    elif romance_points < 5 and romance_points > -5:
        scene bg door
        show walt neutralsideclothed
        with fadehold

        "I scratch the top of my head as we appear before the door, and I think I realize what the feeling is."

        "I don't really want Walt to leave."

        "I can't just tell him about it, though. That would be unfair to him, especially since he's here on a trip."

        w neutraltalkingsideclothed "\"Hey, you alright?\""

        show walt neutralsideclothed
        "I jump at the question, quickly sucking up my self-pitying and throwing my arm behind my head."

        a hangovercuriousclothed "\"Oh, yeah! I'm doing good!\""

        w neutralsideclothed "\"Ah, okay.{w}{nw}{done}"

        w smilingsideclothed "\"Ah, okay.{fast} Was a bit worried you were going to miss me.\""

        w smilingsideclothed "\"Kidding, of course.\""

        w neutraltalkingsideclothed "\"But if I ever do come back to Silverstone...\""

        w smilingsideclothed "\"Let's meet up again. You're a nice guy.\""

        play sound "DoorOpen.ogg"
        "I want to reach out to stop him, but something freezes me in place.{w} All I do is watch as Walt exits my apartment."

        w grinningclosedsideclothed "\"See ya, Asher!\""

        show walt grinningclosedsideclothed at show_fadeout
        play sound "DoorClose.ogg"
        window hide
        pause 5.0

        menu:
            "Wait For Him":
                jump screamending
    elif romance_points <= -5:
        scene bg door
        show walt angrysideclothed
        with fadehold

        "My ears flicker about as we approach the door, and I think I realize what the feeling is."

        "I don't really want Walt to leave."

        "I can't just spring a confession on him, though. That would be unfair to both of us, since we've been so toxic to each other this entire time."

        w angrysidetalkingclothed "\"Well, I'm off.\""

        show walt angrysideclothed
        "I awkwardly shuffle about in place, trying to think of a better way to end things off if this is the last time we'll see each other."

        a hangoverneutralclothed "\"Hope you have a safe trip.\""

        w neutraltalkingside2clothed "\"I'll try.\""

        show walt neutralsideclothed
        "I secretly wish he'd just open the door already. I can feel the air pushing down on me and my heart rate is skyrocketing."

        play sound "DoorOpen.ogg"
        w angrysidetalkingclothed "\"See ya..\""

        play sound "DoorClose.ogg"
        show walt angrysideclosedclothed at show_fadeout
        "And with those last two words, I'm all by myself again."

        window hide
        pause 5.0

        menu:
            "Get Something To Eat":
                jump houseending