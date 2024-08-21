label morning1:
    stop music fadeout 2.0
    scene bg warning
    with fadehold
    $ renpy.pause()
    
    scene bg black
    with fadehold

    "It's an all too familiar feeling."

    "It's as if the jackhammers residing outside my apartment a week ago migrated to my head."

    play sound "BlanketSound1.ogg"
    a hangoverclosed "\"Mmmmf...\""

    "I struggle to open my eyes.{w} The sun's light piercing through the blinds exasperates my headache, hammers dancing around my frontal cortex."
    show bg ceilingmorning
    with dissolve

    play sound "BlanketSound2.ogg"
    "As I sit up, I feel the cold sweat running down my arms and chest, my fur soaked with the smell of alcohol."

    "I know exactly what this feeling is..."

    a hangoversquinting "{sc=3}\"Fucking hangover...\"{/sc}"

    scene bg black
    with fadehold
    show morninganimation at show_fade
    pause 5.0
    show morninganimation at show_fadeout

    play sound "DoorOpen.ogg"
    jump morning

label morning:

    # WEEEEEEEEEEEEEE TIME TO START

    play sound "DoorClose.ogg"
    scene bg hallway
    with fadehold

    # DIALOGUE STARTS HERE

    "I stumble my way to the kitchen, my stomach growling up a storm.{w} I make a note to myself that I should start eating before I go partying on a Friday.{w} Whether I'll follow through on that mental note or not is yet to be seen."

    scene bg kitchen
    with dissolve
    play sound "LightSwitch1.ogg"
    "The lights from the kitchen's fixtures burn my retinas, and I can feel the construction crew in my head swing harder and harder as they invade my nervous system."

    a hangoverbright "\"Jesus fuck, that's bright...\""

    "As I'm swarmed with the rays of a thousand suns, it finally comes to me.{w} I don't remember SHIT about last night."

    "How fucking drunk did I get? The last thing I can recall is pulling up to the club and then..."

    "Wait, is my car here? Did I drive back to my apartment drunk?! I sure hope not."

    window hide
    play sound "StomachGrowling1.ogg"
    pause 2.0
    window auto

    "...I guess I can't accomplish anything on an empty stomach."

    play sound "RefrigeratorOpen.ogg"
    "I make my way to the fridge, hoping to find some leftover pizza or Chinese from my drunken escapades."

    "Of course, I'm let down as my refrigerator is barely stocked.{w} All that resides are some wilting vegetables, a couple eggs, and some bacon I opened yesterday...{w} I think."

    "Looking over to the counter, my coffee machine sits begging to be used. My mocha latte pods have barely been touched, partially because I normally order coffee, but also because I just don't like the flavor."

    a hangoverpondering "\"What should I make for breakfast...?\""

    menu:
        "Veggie Smoothie":
            $ Veggie = True
            "While I would prefer something more palatable, I come to the conclusion that making a vegetable smoothie is probably the best option for a hangover."

            "The eggs would be great to treat this never-ending migraine due to their amino acids, but the fat from the bacon would completely throw that off-balance."

            "Ugh, and the coffee would probably make everything worse with all of that caffeine..."

            "I dust off the blender and bring out the sad vegetables from my fridge."

            show bg blender
            with fade

            play sound "Sink.ogg"
            "I throughly rinse the spinach in my hands, making sure to pull off the leaves that look disgusting and rotten. My trash bin resembles the inside of a lawnmower."

            "Stained green with grass and muck."

            "I put in the good spinach first before rummaging through my cupboards for some canned fruits.{w} It's high in sugar, but it'll balance the flavor."

            "Luckily I have some canned pineapple and mango. Sweet, sour, and slightly bitter. Just the way I like it."

            "I sniff the almond milk in my fridge to make sure it hasn't gone bad yet, my nose twitching as I bring it all in."

            play sound "RefrigeratorClose.ogg"
            "Finally, it's time to blend."

            play sound "Blender.ogg"
            "The blender makes a loud grinding sound.{w} I don't know if it's from the lack of use or whatever, but I really should look into getting a new one."

            w "\"Jesus, that's loud!\""
        "Bacon and Eggs":
            $ Bacon = True
            "I know everyone says that fatty foods are terrible if you have a hangover, but right now I'm craving both a cure AND flavor."

            "The vegetable smoothie would just taste like I'm drinking grass and the coffee would be too bitter for my poor tongue.{w} Not to mention all of the caffeine in there."

            "Guess it's a classic American breakfast for me, then."

            show bg egg
            with fade

            "As usual, I turn up the heat to medium on my stove before breaking out my trusty, and uh... somewhat dusty, non-stick pan."

            "As I let the pan heat up, I make my way to the fridge. Immediately, my hands snipe the eggs before cracking them onto the hot metal."

            play sound "PanSizzling.ogg"
            "It brings back memories of cooking an egg on the sidewalk before my mom wrestled me and my brother back in."

            "I sniff the bacon, making sure my mind isn't playing tricks on me.{w} The scent of salt, smoke, and ham perks my ears up."

            "My tail bats against the trash can and counter before I finally make my way over to the bubbling eggs."

            play sound "RefrigeratorClose.ogg"
            "I put two slabs of bacon onto the pan to soak up the juices left by the eggs. I prefer oven-baked, but sometimes you gotta make do."

            w "\"Something smells really good.\""
        "Mocha Latte":
            $ Coffee = True
            "It probably isn't a good idea due to all of the caffeine, but I can feel my eyelids imitating the Titanic right now."

            "I don't really trust myself around a hot pan or a blender with this hangover. Who knows what gorey mess I'd conjure up if I used those in this state."

            "I go over to the under-used coffee machine and plug it in. Time to actually put those 300 bucks to use."

            show bg coffee
            with fade

            play sound "RefrigeratorClose.ogg"
            "A thin layer of dust coats the machine due to the days I spent walking by and ignoring it.{w} God, I'm gross."

            play sound "Sink.ogg"
            "After wiping my regrets away, I fill the water reservoir and press the power button, letting it heat up for a few minutes."

            "This is somehow both the laziest and most boring way to have breakfast."

            "After the water is as hot as can be, I put in my K9-Cup. Picking out my favorite mug, I sit back as my mocha latte brews."

            play sound "CoffeeMachine.ogg"
            a "\"One cup of coffee, then I'll go...{w} Though I just dropped by to let you know...\""

            "Once it's done, I immediately take the mug and have a quick swig, burning my tongue in the process.{w} I guess that's one way to wake up."

            w "\"\'Thought I smelled coffee in here.\""

    show bg closeup
    play sound "Dishes.ogg"
    with vpunch

    a hangoversurprised "{sc=3}{size=*2}\"FUCKING CHRIST!!\"{/size}{/sc}{fast}"

    show bg kitchen
    show walt staringscared

    "I grasp my head as my own voice sends a missile into my brain.{w} I can't imagine what it was like for the wolf standing in front of me..."

    "...Wait. There's a fucking wolf in front of me?!"

    w staringtalkingneutral "\"Are you okay, dude?\""

    w "\"Sorry, I...{w} I didn't mean to scare ya.\""

    # I LOVE IF ELSE STATEMENTS :')

    if Veggie == True:
        "He doesn't seem to mean any harm, though I would have bludgeoned him with my blender if I was more awake..."
    elif Bacon == True:
        "He doesn't seem to mean any harm, though I would have assaulted him with my frying pan if my food wasn't cooking in it..."
    elif Coffee == True:
        "He doesn't seem to mean any harm, though I almost scalded him by breaking my mug over his head..."

    a hangoverupsetclosed "\"Uh... no, you're fine. I'm just a bit hungover at the moment.\""

    w staringneutral "\"Oh...{w} Well, I guess that makes two of us, then...\""

    "Two of us?"

    w lookingdownside "\"I, uh...{w} I have a bit of a hangover.\""

    "Now I feel even worse about my yelling.{w} I think I'm starting to get the picture, though."

    "Two half-nude canines talking in the kitchen at 11 AM? Did my drunken ass bring him over here last night?"

    "I must have.{w} Despite my fugue state, something about him does seem familiar to me."

    "Compared to my snow-white fur, his is two shades of burnt ash. If I wrestled with him for longer than a minute, I'd have to take a shower to erase the evidence."

    "Strangely, the singular hairs sticking out of him look brittle; as if they would crumble by a simple prod."

    "But together, the hairs form into a wavy, silky coat. If you buried yourself in it, it would warm you up in no time flat."

    show walt neutralside
    "His eyes follow the Arizonian desert scheme, the amber color accented by a piercing bronze."

    "If he hadn't been so friendly, I would've sworn he was shooting daggers at my dumb ass."

    w neutraltalkingside "\"Um...\""

    a hangovercurious "\"Hmm? Something up?\""

    w neutraltalkingside2 "\"Eh, nothing much...\""

    w neutraltalkingside "\"You've just been staring at me for a long time?\""

    with vpunch
    "IDIOT!!"

    a hangoversurprised "\"Sorry, sorry!!\""

    show walt grinningclosedside
    "I guess my blunder amuses the wolf, who just stands there laughing at my awkward misfortune."

    $ walt_name = "Walt"

    w "\"The name's Walt.\""

    "I guess names were out of the question while we were piss-drunk."

    a hangoverneutral "\"I'm Asher.\""

    play music "The Morning After.ogg" loop fadein 1.0
    w smilingside "\"Sorry I haven't left yet, it's just... a bit icy right now.\""

    "Walt brushes it off, but this is news to me.{w} Sure enough, I look out the window and am blinded by the sun bouncing out of the snow."

    w neutraltalkingside2 "\"I'll be out of your hair soon, just felt it was common courtesy to let you know I was here first.\""

    show walt lookingdownside
    "More courteous than the other people I've slept with at least."

    a hangoverneutral "\"Where are you going to go though?{w} There's not much to do around here.\""

    show walt neutralside
    "I'm not exaggerating when I tell him that.{w} Despite being a coastal town, Silverstone has pretty much been a ghost town since 2002."

    "The only interesting places around here that are still open are an understaffed arcade and some psuedo-science crystal museum."

    w grinningclosedside "\"I was actually gonna head south a bit to that diner I saw on the way here!\""

    "I have come to the conclusion this guy is a moron.{w} A hot moron, but a moron."

    "Even though his coat is thicker than mine, I can tell it still wouldn't be enough to withstand the barrage of snow coming our way."

    a hangoversurprised "\"Are... are you sure about that?{w} That's a thirty minute walk.\""

    a hangoverneutral "\"If you walk there and it's closed, you're going to get sick.\""

    w smilingside "\"It's nothing I can't stand, chief!\""

    "I grimace as he calls me that. Chief is a nickname you give your dad, not someone around your age...{w} Or someone you possibly slept with."

    stop music fadeout 1.0
    pause 1.0
    show walt staringsideneutral
    play sound "StomachGrowling2.ogg"

    "I hold back my laughter as the wolf's stomach rumbles louder than mine did."

    play music "The Morning After.ogg" loop fadein 1.0
    "I can see his ears flush red in embarrassment, and even a pinch of pink under that dark brown fur of his."

    "But still, like hell I was going to let him leave without eating first at least."

    show walt staringsidesmiling
    a hangoverraisedtalking "\"You know, you could have woken me up.\""

    a hangoverraisedtalking2 "\"I would have made you breakfast.\""

    w neutraltalkingside "\"Uh... I kind of did try to wake you up.\""

    "Well now I feel like even more of a bastard. I yell at him, oggle at his chest, and now I'm a bad host, too.{w} Jesus Christ, I'm a fucking mess."

    w grinningclosedside "\"I stopped trying eventually, though. You just looked too cute resting like that!\""

    "...{w}Where did that level of confidence come from?{w} I'm pretty sure I had drool crusted against my chin."

    "Still I guess I should get him something to eat..."

    if Veggie == True:
        menu:
            "Give Smoothie to Walt":
                $ romance_points += 1
                show walt staringsideneutral
                "I have no problem offering Walt my smoothie, craving something of actual substance in my stomach by now.{w} I guess that's a bit selfish, but at least we both get something."

                w staringtalkingneutral "\"Wait, no. Didn't you make that for yourself?\""

                w neutraltalking "\"Dude, I can't take that.\""

                show walt neutral2

                a hangoverupsetclosed "\"It's fine. I have more here I can make.\""

                a hangoverneutral "\"Go sit at the island and eat already.\""

                show walt lookingdownside
                "Despite his initial reluctance to take the glass of grass, Walt eventually accepts it."

                show walt grinningclosedside
                "I swear I see him flash a grin before he heads on over to the isle to indulge in the blessing of mediocrity."

                show walt grinningclosedside at offscreenright with MoveTransition(0.2)
                "While he starts to eat, I make my own breakfast. Landing on bacon and eggs, I take in the smell before sitting right beside him."

                scene bg counter
                with dissolvelong
                pause 0.5

                play sound "Silverware.ogg"
                a hangovercurious "\"So, where are you from?\""

                a hangoverraisedtalking "\"I'm just guessing you're from out of town since you mentioned that old diner our few tourists find.\""

                jump morning2
            "Keep Smoothie":
                $ romance_points -= 1
                show walt neutralside
                "As much as I want to give Walt breakfast right away, I need to get rid of this hangover if I'm going to survive today."

                "Sorry, Walt, but this smoothie is mine."

                show walt staringsideneutral
                a hangovercurious "\"There's some bacon and eggs in the fridge if you want that.\""

                show walt lookingdownside
                "I can already tell by the look on the wolf's face that he's a bit disappointed. As much as he tries to hide it, his ears slightly droop and his nose twitches as if he's agitated."

                show walt smilingside
                "His expression eventually turns back to his cheerful self, but I can't help feeling like I messed up."

                w grinningclosedside "\"I'll go cook that, then!{w}{nw}{done}"

                w smiling "\"I'll go cook that, then!{fast} Why don't you go ahead and drink your smoothie before it gets gross and clumpy?\""

                a hangoverraisedtalking2 "\"You sure?\""

                w neutraltalking "\"Yeah, I'll be fine.\""

                show walt neutraltalking at show_fadeout
                "Although I try to argue back at him, the ashy wolf has already made his way to the fridge.{w} With that shut down, I decide it's best to just go and eat."

                scene bg counter
                with dissolve
                pause 0.5

                play sound "Silverware.ogg"
                "Walt stumbles through cooking his meal as I gulp down my smoothie, anxiety rising as he almost scrapes my non-stick pan."

                "Soon enough, he joins me at the counter, although his meal somehow looks both burnt and somewhat raw... which I didn't think was possible."

                "The air's still a tad heavy, so I attempt to break the silence."

                a hangovercurious "\"So you're from out of town?\""

                a hangoverraisedtalking "\"Most locals don't really care about that diner since it's a bit too far.\""

                jump morning2
    elif Bacon == True:
        menu:
            "Give Bacon and Eggs to Walt":
                $ romance_points += 1
                show walt staringsideneutral
                "While I would like to eat some bacon and eggs, they would just get cold if I tried to cook Walt something.{w} Better someone actually eats it than let it go lukewarm."

                w staringtalkingneutral "\"Wait, no. Didn't you make that for yourself?\""

                w neutraltalking "\"Dude, I can't take that.\""

                show walt neutral2

                a hangoverupsetclosed "\"It's fine. I have more here I can make.\""

                a hangoverneutral "\"Go sit at the island and eat already.\""

                show walt lookingdownside
                "Despite his initial reluctance to take the Grand Slam sans pancakes, Walt eventually accepts it."

                show walt grinningclosedside
                "I swear I see him flash a grin before he heads on over to the isle to indulge in the heart of 'Murica."

                show walt grinningclosedside at offscreenright with MoveTransition(0.2)
                "While he starts to eat, I make my own breakfast. I settle for coffee, not wanting to risk the health hazards of molten spinach, before sitting right beside him."

                scene bg counter
                with dissolvelong
                pause 0.5

                play sound "Silverware.ogg"
                a hangovercurious "\"So, where are you from?\""

                a hangoverraisedtalking "\"I'm just guessing you're from out of town since you mentioned that old diner our few tourists find.\""
                
                jump morning2
            "Keep Bacon and Eggs":
                $ romance_points -= 1
                show walt neutralside
                "As much as I want to give Walt breakfast right away, I'm almost drooling over my breakfast at this point."

                "Sorry, Walt, but this farmed-raised meal is mine."

                show walt staringsideneutral
                a hangovercurious "\"If you want to, you can use my coffee machine.\""

                show walt lookingdownside
                "I can already tell by the look on the wolf's face that he's a bit disappointed. As much as he tries to hide it, his ears slightly droop and his nose twitches as if he's agitated."

                show walt smilingside
                "His expression eventually turns back to his cheerful self, but I can't help feeling like I messed up."

                w grinningclosedside "\"I'll go make that, then!{w}{nw}{done}"

                w smiling "\"I'll go make that, then!{fast} Why don't you go ahead and eat your breakfast before it gets cold and greasy?\""

                a hangoverraisedtalking2 "\"You sure?\""

                w neutraltalking "\"Yeah, I'll be fine.\""

                show walt neutraltalking at show_fadeout
                "Although I try to argue back at him, the ashy wolf has already made his way to the fridge.{w} With that shut down, I decide it's best to just go and eat."

                scene bg counter
                with dissolve
                pause 0.5

                play sound "Silverware.ogg"
                "Walt stumbles through cooking his meal as I snarf down my eggs, anxiety rising as he slams down the K9-Pod cover."

                "Soon enough, he joins me at the counter, although his coffee looks cold and a bit unfinished... probably because of the strength he unloaded onto the machine."

                "The air's still a tad heavy, so I attempt to break the silence."

                a hangovercurious "\"So you're from out of town?\""

                a hangoverraisedtalking "\"Most locals don't really care about that diner since it's a bit too far.\""

                jump morning2
    elif Coffee == True:
        menu:
            "Give Latte to Walt":
                $ romance_points += 1
                show walt staringsideneutral
                "I have no problem offering Walt my coffee, being well enough awake to finally operate a motor vehicle.{w} Well, maybe not that, but I can at least use a blender."

                w staringtalkingneutral "\"Wait, no. Didn't you make that for yourself?\""

                w neutraltalking "\"Dude, I can't take that.\""

                show walt neutral2

                a hangoverupsetclosed "\"It's fine. I have more here I can make.\""

                a hangoverneutral "\"Go sit at the island and eat already.\""

                show walt lookingdownside
                "Despite his initial reluctance to take the bitter taste of death, Walt eventually accepts it."

                show walt grinningclosedside
                "I swear I see him flash a grin before he heads on over to the isle to indulge in Café au Asher."

                show walt grinningclosedside at offscreenright with MoveTransition(0.2)
                "While he sips the painfully expensive brew, I make my own breakfast. I figure it's probably best to use the spinach now, so I blend a smoothie before sitting right beside him."

                scene bg counter
                with dissolvelong
                pause 0.5

                play sound "Silverware.ogg"
                a hangovercurious "\"So, where are you from?\""

                a hangoverraisedtalking "\"I'm just guessing you're from out of town since you mentioned that old diner our few tourists find.\""
                
                jump morning2
            "Keep Latte":
                $ romance_points -= 1
                show walt neutralside
                "As much as I want to give Walt breakfast right away, I won't even be able to host if I don't get caffeine in my system."

                "Sorry, Walt, but this latte is mine."

                show walt staringsideneutral
                a hangovercurious "\"There's some vegetables in the fridge and canned fruit if you want to make a smoothie.\""

                show walt lookingdownside
                "I can already tell by the look on the wolf's face that he's a bit disappointed. As much as he tries to hide it, his ears slightly droop and his nose twitches as if he's agitated."

                show walt smilingside
                "His expression eventually turns back to his cheerful self, but I can't help feeling like I messed up."

                w grinningclosedside "\"I'll go make that, then!{w}{nw}{done}"

                w smiling "\"I'll go make that, then!{fast} Why don't you go ahead and drink your coffee before it gets cold and disgusting?\""

                a hangoverraisedtalking2 "\"You sure?\""

                w neutraltalking "\"Yeah, I'll be fine.\""

                show walt neutraltalking at show_fadeout
                "Although I try to argue back at him, the ashy wolf has already made his way to the fridge.{w} With that shut down, I decide it's best to just go and eat."

                scene bg counter
                with dissolve
                pause 0.5

                play sound "Silverware.ogg"
                "Walt stumbles through picking off the rotten spinach leaves as I sip on my coffee, anxiety rising as he almost drops my blender."

                "Soon enough, he joins me at the counter, although his coffee looks chunky and barely like liquid... proably because he forgot to add a base."

                "The air's still a tad heavy, so I attempt to break the silence."

                a hangovercurious "\"So you're from out of town?\""

                a hangoverraisedtalking "\"Most locals don't really care about that diner since it's a bit too far.\""

                jump morning2