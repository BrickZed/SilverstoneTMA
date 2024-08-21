label houseending:
    "I breathe a sigh of relief as I put my ear to the door, waiting until Walt has reached the final step."
    
    "Despite a good beginning, the only thing I could feel by the end of our meeting was overwhelming tension."

    "The knot in my stomach unwinds and I finally realize that I haven't eaten since breakfast this morning."

    "Alone once again, I head to the kitchen to pick through the scraps that are left in my pantry."

    show bg kitchen
    with dissolvelong

    "The morsels left in my kitchen sit in their respective places, sad and alone."

    "I'm tempted to try and call my local pizza place, but it's way too late for them to realistically still be open.{w} I manage to find an old breakfast pastry in my cupboard that I missed this morning and pop it in the toaster."

    "As I wait the minute and a half it takes to cook, Walt crosses my mind again.{w} I grimace.{w} I still want him with me in the apartment, but our compatibility is just nonexistent."

    "My mouth burns with dry pastry and gooey jam as I ponder.{w} Could things have been any different?"

    "Despite my overindulged nap, I can't help but feel tired."

    "Staying up this late will fuck with my sleep schedule, so I resign to my fate.{w} A wolf's gotta sleep when a wolf's gotta sleep."

    show bg ceilingnight
    with dissolvelong
    pause 0.5

    "I stare up my ceiling, letting the moonlight shine in through the windows.{w} The dream I had returns to me."

    "\'I will die here tonight.\'"

    "I give a sarcastic laugh before rolling onto my stomach, letting my muzzle dress the pillow."

    "Despite how much sleep I got today, I'm quickly lulled back into a deep slumber."

    window hide
    show bg black
    with dissolvelong
    pause 3.0

    play sound "Glass.ogg"
    $ config.window_hide_transition = None
    "My eyes shoot open as I hear shards of glass fall on the floor.{w}{nw}{done}"
    
    play music "CreepyAmbience.ogg" fadein 2.0
    $ config.window_hide_transition = Dissolve(.2)
    "My eyes shoot open as I hear shards of glass fall on the floor.{fast} I feel a chill as wind blows onto my back; my shoulders curling in as I shiver from the cold."

    "I'm afraid to open my eyes, fearing who I'll see if I look around."

    "But would it be worse just to let whoever it is stalk around my home?"

    pause 2.0
    menu:
        "Open Your Eyes":
            $ config.window_hide_transition = None
            window hide
            show bg ceilingnight
            pause 2.0

            $ config.window_hide_transition = Dissolve(.2)
            "Turning onto my back, I scan the room.{w} Glass decorates the floor, and even some of my sheets.{w} Whoever decided to break in had intent."

            "Despite this, there's no one here.{w} I grab an old hiking cane from my closet and venture out into the hallway."

    play sound "Footsteps1.ogg"
    window hide
    show bg hallway with dissolve
    pause 1.0
    show bg kitchen with dissolve
    pause 1.0
    show bg afternoontv with dissolve
    stop sound fadeout 1.0
    pause 2.0

    window auto show
    "I lower my guard once I reach the living room.{w} If anyone's here, they're doing a good job of hiding."

    "The one positive outlook on this is that it signaled me about my lights. I pick up a candle and blow it out, drenching the room in darkness."

    "The kitchen light shines through, giving me a glimmer of hope in the abyss. I decide to return to my room, realizing my cell phone is there and I should call the police."

    play sound "Footsteps1.ogg"
    window hide
    show bg kitchen with dissolve
    pause 0.5
    show bg hallway with dissolve
    pause 0.5
    show bg ceilingnight with dissolve
    stop sound fadeout 0.5
    pause 1.0

    window auto show
    "I pounce back onto my bed, grabbing my cell phone from my nightstand.{w} I press the home button and..."

    window hide
    show PhoneHorror at offscreenbottom
    show PhoneHorror at truecenter with MoveTransition(0.4)
    pause 1.5

    window auto show
    "\'Fuck,\' I whisper to myself.{w} The memory of Walt and I chatting at breakfast crawls back into my mind.{w} My battery was low when I checked the weather."

    show PhoneHorror at offscreenbottom with MoveTransition(0.1)

    a hangoversurprised "\"It'll be fine.{w} I can just plug it in and turn it back on when it's at five percent.\""

    show bg black with dissolvelong
    "I turn on my belly, reaching for the charging wire.{w}{nw}{done}"

    stop music fadeout 2.0
    "I turn on my belly, reaching for the charging wire.{fast} As my thumb brushes across it, my stomach sinks into a pit of horror."

    "The charger's been frayed."

    play sound "BlanketSound2.ogg"
    "I suddenly feel something warm and heavy get on my back, with its appendages intertwining themselves around my legs."

    "A paw grabs the phone from my hand, placing it gently back onto the nightstand."

    "I can feel my eyes bug out, but I bury my face into my pillow.{w} I don't want to look at what's on top of me."

    play sound "Walt1.ogg"
    "A hot breath brushes along my neck, and soon a muzzle is rubbing against my shoulder.{w} Whoever it is, it's both stiff and sensual."

    $ walt_name = "????"

    w "\"Shhhhh...{w} It's just me.\""

    "I recognize the voice immediately. Deep, husky, and warm."

    $ walt_name = "Walt"

    w "\"I know we got off on the wrong foot, but...{w} we can work something out.\""

    "All I can repeat in my head is \'what the fuck\' over and over again.{w} Is this asshole serious?"

    "I feel soft nibbles on my neck, and my limbs contort in discomfort.{w} It's like there's no control over my body.{w} Paralyzed, yet reactionary."

    w "\"My mind was focusing on you ever since I left.{w} I couldn't stop thinking about cuddling you.\""

    "As my thoughts fill with fear, my fur becomes stained with tears. Please, someone.{w} A robber, the landlord, I don't fucking know..."

    w "\"I'm not going to do anything, babe.\""

    w "\"Let's just sit here...{w} and cuddle until we can't anymore.\""

    "That's when I feel something warm and sticky on the sheets."

    "I open my eyes for my split second, turning to see what—{nw}"
    pause 0.15

    $ config.window_hide_transition = None
    window hide
    play sound "BlanketSound1.ogg"
    show bg ceilingnight
    show jumpscare
    pause 3.0

    show bg black
    hide jumpscare
    play sound "BlanketSound2.ogg"
    window auto show
    "I turn back to my pillow, my stomach churning at the sight of Walt.{w} His eyes were emotionless, just staring at me like I was a possession."

    $ config.window_hide_transition = Dissolve(.2)
    "But I figured out what's on the sheets.{w} There's a shard of glass stuck in my hip."

    "It must have happened when I returned to the bed.{w} How I didn't notice it is beyond me."

    "It can't be shock, can it? Perhaps it's adrenaline from having a giant wolf break in and wrap his arms around me."

    "A loud rumble echoes into my ears. The man who I once loved and is now my greatest fear... has fallen asleep on top of me."

    "I'm too scared to move. What if my struggling causes the glass to break and spill even more blood?"

    "My phone is useless right now, and I'm pretty sure Walt could overpower me even if I try to move him."

    "I start to feel cold. Not from the wind... It feels like when medicine is injected through an IV, but constant."

    "I shoulder Walt, trying to move him.{w} But he's too heavy...{w} and that's when I realize."

    "Some of the blood is his.{w} His eyes weren't emotionless...{w} They were dead."

    show bg ceilingnight with dislong
    "I let out some soft whimpers, tears flowing down my eyes...{w} I don't want to die like this."

    "Everything feels colder and heavier; my muscles feel atrophied.{w} Soon, my energy depletes and I just let my head sink into the pillow."

    "I think back to the night at the club. Things are coming back right as I die."

    "I even remember the drinks we ordered."

    show bg black
    "It was a Silver Bullet."
    $ EndingBad = True
    $ quick_menu = False
    window hide
    pause 3.0
    jump credits