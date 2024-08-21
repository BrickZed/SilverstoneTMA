label epilogue:
    $ quick_menu = True
    scene bg store
    with fadeholdlong

    window auto show
    c "\"Okaaaaay, and that's going to be 6.28.\""

    t "\"Wait, that's all?\""

    c "\"Yeah, no sales tax in Oregon, dude!\""

    t "\"Damn, maybe I should move here.\""

    c "\"Haha, good luck. Rent here is fucking expensive.\""

    c "\"Besides, I don't think you would want to live in Silverstone anyway.\""

    t "\"Excuse me?\""

    play sound "StoreDoor.ogg"
    window hide
    pause 2.0
    play sound "GrabBag.ogg"
    pause 2.0
    play sound "Footsteps1.ogg"
    pause 3.0
    stop sound

    window auto show

    c "\"\'The usual good?\""

    $ walt_name = "????"

    w "\"Yeah, that's fine.\""

    play sound "CashRegister.ogg"

    c "\"Alright, that's going to be—\""

    w "\"Keep the change.\""

    c "\"Dude, if you keep giving me twenties like this, you're gonna go broke—"

    window hide
    play sound "Footsteps1.ogg"
    pause 3.0
    play sound "StoreDoor.ogg"

    window auto show
    t "\"Damn, what's his issue?\""

    c "\"Dude's grieving.{w} His partner died a couple months ago due to an enlarged heart.\""

    t "\"Shit, are you serious?\""

    c "\"I wish I wasn't.\""

    t "\"...\""

    c "\"Well, my shift is just about over so I'm going to head off.{w} Have a nice day!\""

    scene bg church
    with dissolvelong
    pause 1.0

    "I can feel my lungs burn as I take a drag, my feet crawling through the grass as I make my way to the graveyard."

    play sound "Leaves1.ogg"
    "I'm still trying to work through everything in my head. The snow, the blanket of shadows, and of course, him."

    "The autumn leaves crunch as I traverse the graves, finally landing in front of the reason I'm here."

    "I let the smoke blow out of my nostrils as I put on a fake smile. The one you always see in graveyards."

    "Trying to put on a brave face for those who've departed."

    w "\"Hey, it's me.{w} I know this is... the third time this week, but I like coming here and being with you.\""

    "I place the shoddily-collected bouquet of flowers on the grave before sitting down on the grass, my tail thumping to the side."

    w "\"It's starting to get a bit chilly here.{w} I wonder what it's like where you are.\""

    "I take another puff my cigarette and notice a woman looking at me with judging eyes, pulling her kid towards the front entrance to the church."

    "Can't even grieve in peace."

    w "\"I, uh...{w} I had the job interview today. I think it went well."

    w "\"They liked my attitude, ha. Made me think \'God, I'm a fraud.\'\""

    w "\"It does pay well, though, so I'll be able to afford rent now.{w} I know you said to get out of here, but I can't stand leaving you.\""

    "Tears start to roll down my eyes and I can't hold it back any longer."

    $ walt_name = "Walt"

    play music "Connection.ogg" fadein 2.0
    w "\"I miss you, Asher.{w} I fucking miss you.\""

    w "\"Even if I wanted to leave, I don't think I'd be able to.\""

    w "\"I'd feel like I was abandoning you.{w} We... we didn't date long, but...\""

    w "\"Strangely it's feels as if you were the love of my life.\""

    window hide
    pause 5.0

    window auto show
    w "\"Hey, you know how on your last day we tried to figure out what we got at the club?\""

    w "\"I figured it out last night.\""

    w "\"We both ordered Silver Bullets.\""

    "I laugh, both with irony and pain. I wish I could have told him face-to-face about it so we could laugh at how some dumb legend was \'true\' all along."

    w "\"I'm not going to stop living, Asher.{w} I'll stay in this town and live each day with the thought that one day I'll see you again.\""

    w "\"Through life and death, we're tied together.{w} I love you, babe.\""

    window hide
    pause 5.0

    menu:
        "Let It Out":
            "I don't care how I look in this stupid graveyard anymore. My tears are hot, almost as if it was flowing magma instead of waterfalls."

            "I feel the snot drip out my nose, and guttural screams escape as all I can feel is just how much I miss him."

            "I wonder if it's because of the Silver Bullets for a minute, like it's a fabricated fucked-up love."

            "And the thought of that fills we pain, sadness, and anger at myself for even thinking of it."

            "I remember how soft his fur was.{w} I remember how lulling his heartbeat would be.{w} And I remember the kiss he would give me before each shower...{w} each meal...{w} and each dream."

            "My cries turn into laughter eventually as the good memories flood in. I pick myself up off of the ground and pat the dirt and leaves off of my pants."

            "I take one last puff of my cigarette... and say goodbye to my love."

    scene bg black
    stop music fadeout 5.0
    with fadeholdlong
    pause 3.0

return