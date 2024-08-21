label afternoon2:
    if romance_points >= 3:
        jump couchhappy
    elif romance_points < 3 and romance_points > -3:
        jump couchneutral
    elif romance_points <= -3:
        jump couchangry

label couchhappy:
    play music "Lazy Afternoon.ogg" loop fadein 1.0

    "I sink into the couch, which is an old gift from my mom."

    "My fur catches onto the old knots and tears from it, having been well-used even before she bought it for me."

    "It's definitely broken under the cushions. It feels like my ass is touching hardwood under the thick layer of cotton and cloth."

    "Still, I'd rather be sitting down on a shitty couch then rolling in my bed right now."

    w "\"Here you go. Drink plenty, okay?\""

    "In my anxiety-ridden stupor, I didn't notice that Walt had gone to the kitchen to fetch me a glass of water."

    "My throat does feel a bit parched. I'm a bit confused by that since I was just in the shower. Maybe it's a side effect?"

    show bg walt couch smile up
    with dis
    "Regardless I take a huge gulp of it as Walt sits down next to me, grinning as he returns to his book."

    "I can't help but wonder why he's so nice to me. We've only known each other for a couple hours by now and it feels like he's my rock."

    "It's too fast. It feels like I'm being pulled into his grasp... even though all he's doing is being a nice guy."

    w "\"\'Water helping?\""

    show bg walt couch grinning up
    with dis
    "His grin is captivating. Helpful, yet inviting."

    "I look down at my glass, but I still feel my ears heat up; probably turning pink."

    show bg walt couch laugh1
    with dis
    "A little chuckle confirms that he notices."

    a hangoverraisedtalkingclothed "\"It's helping a little bit, yeah.\""

    show bg walt couch neutral up
    with dis
    a hangoverupsetclosedclothed "\"Sorry you had to see all of that.\""

    show bg walt couch smile down
    with dis
    w "\"Hey, it's not a problem. No need to apologize.\""

    show bg walt couch smile down reading
    with dis
    "I can feel my shoulders finally relax as Walt says that. I spot his own ears turning red, being perked up high as if he's listening for something."

    show bg walt couch neutral up
    with dis
    w "\"If you don't mind me asking, though...\""

    a hangoverraisedtalkingclothed "\"It's kind of a long story.\""

    show bg walt couch smile down
    with dis
    w "\"Well then, I'll tell you about what I'm reading in return, haha.\""

    show bg walt couch neutral up
    with dis
    w "\"I mean, only if you want to tell me, of course!\""

    "I've never told anyone why the dark terrifies me the way it does. Not even my therapists."

    "I always feel a weight in my stomach, like I've swallowed a rock and can't get it out."

    "...But I don't feel that with Walt. I feel...{w} comfortable.{w} I feel supported."

    "It's a scary feeling that I can't my finger on."

    "I draw in a deep breath, hoping I won't fall into a full-blown anxiety attack."

    a hangoverupsetclosedclothed "\"I wasn't the most... well-behaved kid.{w}{nw}{done}"

    a hangoverponderingopenclothed "\"I wasn't the most... well-behaved kid.{fast} In fact, I was probably the worst of my siblings.\""

    show bg walt couch smile down
    with dis
    w "\"Oooooh, you were a bit of a rascal?{w} A Wily Coyote?\""

    show bg walt couch laugh1
    with vpunch
    "I playfully punch Walt's arm at the remark, holding back laughter myself."

    a hangoverslyclothed "\"Oh, shut up.\""

    show bg walt couch smile up
    with dis
    "The playful air quickly disappears, though I wished it would stay longer."

    show bg walt couch upset up
    with dis
    a hangoverponderingclothed "\"Well, let's just say that my parents shouldn't have been parents.\""

    show bg walt couch upset up reading
    a hangoverupsetclosedclothed "\"One time, I ended up going too far.{w} I accidentally hurt my sister while trying to cut her hair as a prank.\""

    a hangoverraisedtalkingclothed "\"Oh, they were absolutely in the right to punish me. That was fucked up.\""

    "I kind of think Walt's broken gaze is simply because of what I did. It doesn't matter that it's been like... 18, 19 years. I still feel the guilt to this day."

    stop music fadeout 1.0
    a hangoverupsetclosedclothed "\"The next thing I remember...{w}{nw}{done}"

    show bg black
    with dis
    a hangoversurprisedclothed "\"The next thing I remember...{fast} is my dad throwing me by the collar into the hallway closet.\""

    play music "CreepyAmbience.ogg" loop fadein 1.0
    "Oh... I'm here again."

    "It's just another punishment for my past mistakes."

    "A punishment for the people I've hurt."

    "A punishment for existing."

    "I close my eyes as I try to escape the darkness again. I know it's not there, but somehow I always land in nothingness."

    a hangoverupsetclosedclothed "\"Fuck...\""

    a hangoverupsetclosedclothed "\"I remember he taped cardboard over the blinds of the door...{w} and put blankets around the door frame so no light could get in.\""

    a hangoverupsetclosedclothed "\"I couldn't tell how many hours I had been in there.\""

    "{sc=3}It was four.{/sc}"

    a hangoverupsetclosedclothed "\"I couldn't hear anything besides the ringing in my ears.\""

    "{sc=3}I heard their cries as dad yelled at them.{/sc}"

    a hangoverupsetclosedclothed "\"The clothes felt like bugs swarming me.\""

    "{sc=3}What if they were bugs, though?{/sc}"

    a hangoverupsetclosedclothed "\"I just...\""

    a hangoversurprisedclothed "\"It just...\"{nw}"
    window show
    pause 0.15

    window auto show
    w "\"STOP.\""

    $ config.window_hide_transition = None

    window hide
    scene bg walt couch snarl up
    stop music
    pause 2.0

    $ config.window_hide_transition = Dissolve(.2)

    "Walt is staring at me, mouth agape. His face is dressed in horror."

    window auto show
    show bg walt couch upset down reading
    with dis
    "He runs a hand down his muzzle, letting out a deep breath. I can't help but feel like I scared him."

    "It's at this point I noticed my own heavy breathing, and that I'm clutching onto a throw pillow. It's torn, with my claws digging into the fluff inside."

    show bg walt couch snarl down
    with dis
    w "\"I shouldn't have asked you to tell me that.{w}{nw}{done}"

    show bg walt couch upset down
    with dis
    w "\"I shouldn't have asked you to tell me that.{fast} I'm sorry. That was fucking idiotic of me.\""

    "I almost feel like crying.{w} I'm usually told that it's my fault that I get emotional like that.{w} But then there's Walt."

    "What does he have to apologize for? It was me who suddenly fell into a wormhole of memories. It feels too good to be true."

    show bg walt couch snarl up w hand
    with dis
    "A single tear runs down my cheek. The wolf instantly notices, and places his hand on my head; wiping the tear away with his thumb."

    show bg walt couch snarl up
    with dis
    w "\"Fuck, are you okay?\""

    show bg walt couch upset up
    with dis
    "Walt's pawpads feel rough and warm, and I can't help but feel comforted by it. I realize that my tears this time are happy, not sad."

    "Am I this easily moved? Just by someone showing kindness?"

    show bg walt couch snarl up
    with dis
    "I laugh internally at the thought, unsure what to make of it. I smile at the wolf, who looks incredulous."

    w "\"Asher?\""

    menu:
        "Lean on Walt":
            $ romance_points += 1
            show bg walt couch neutral up
            with dis
            play music "Lazy Afternoon.ogg" loop fadein 1.0
            "Drowsy, I fall onto Walt's shoulder. It's firm, but the fur provides enough padding to keep from feeling like I'm lying down on smooth stone."

            "His fur is surprisingly soft, and it smells of mint and alder from the shampoo he used."

            show bg walt couch neutral up reading
            with dis
            "Looking up to the wolf, he quickly averts his gaze; eyes back on his book."

            "His ears are flushed and I can see a bit of pink bursting out from his cheeks."

            "I wonder how he feels about this whole situation. All I've been thinking about this time is my own feelings, but Walt isn't just a hunk of meat to drool over."

            "Is this awkward for him? Does he like it, too? Does he think it's a supernatural kind of love as well?"

            a hangoversmilingclosedclothed "\"I'm doing alright.{w} Sorry for worrying you.\""

            show bg walt couch neutral up
            with dis
            w "\"Do you get these anxiety attacks often?\""

            a hangoverraisedtalkingclothed "\"They aren't rare, but they usually aren't too bad. Having a nightlight helps when I sleep and I take medication, usually.\""

            show bg walt couch upset up
            with dis
            w "\"Usually?\""

            a hangoverupsetclosedclothed "\"I think I forgot with all of the chaos today.\""

            show bg walt couch upset down reading
            with dis
            w "\"Oh...{w} Sorry about th—\"{nw}"
            window show
            pause 0.15

            window auto show

            show bg walt couch neutral up
            a "\"That's both of our faults.{w} We were drunk. Don't pin it just on yourself.\""

            "There's a moment of silence. Walt seems a bit perturbed at that statement, as if I passed my panic baton over to him."

            show bg walt couch upset up reading
            with dis
            w "\"This might sound weird, but...\""

            w "\"Ever since this morning, I've just... felt this need to protect you."

            w "\"And I've felt like I've done a shit job.\""

            "So he has been feeling the same in some capacity."

            show bg walt couch upset down
            with dis
            w "\"I didn't want to say anything at first because it sounds... creepy and weird, but...\""

            w "\"I don't know. I just feel like you're someone worth more than you might think you are.\""

            a hangoverslyclothed "\"Heh, I'm that easy to read?\""

            show bg walt couch smile down reading
            with dis
            w "\"Shut up, I'm serious.\""

            "It's nice to see the wolf crack a smile again, even if it's a bit somber."

            show bg walt couch neutral up
            with dis
            "I lean in closer to him, my muzzle practically rubbing against his arm at this point. I gently push his book down and look up at the ceiling."

            a hangovercuriousclothed "\"You want to know something fucking dumb?\""

            show bg walt couch smile down
            with dis
            w "\"What?\""

            a hangoverneutralclothed "\"Silverstone's signature drink is the \'Silver Bullet.\'\""

            show bg walt couch laugh2
            with dis
            w "\"Why are you bringing this up now?\""

            show bg walt couch smile down
            with dis
            a hangoverponderingopenclothed "\"Well, there's an {i}equally{/i} stupid legend about it.\""

            show bg walt couch smile up
            with dis
            a hangoverslyclothed "\"People say that if two people order a Silver Bullet at the same time, their lives are entwined forever.\""

            show bg walt couch laugh1
            with dis
            w "\"What?!\""

            "I can feel Walt's muscles flex as he bellows.{w} It's a bit uncomfortable, but I can't help but smile as he roars with laughter."

            show bg walt couch smile down
            with dis
            w "\"Okay, there's absolutely {i}no way{/i} that's real.\""

            a hangoversmilingclosedclothed "\"But I got you to laugh, didn't I?\""

            show bg walt couch neutral up
            with dissolve
            pause 1.0
            show bg walt couch smile down
            with dissolve

            w "\"I guess you did.\""

            "I let out a deep breath, Walt's fur spreading out as the air hits his arm.{w} The tenseness I felt in my stomach has finally disappeared."

            "The world is just Walt and I right now.{w} I wish it could it stay that way."

            if romance_points >= 3:
                jump readingbookhappy
            elif romance_points < 3 and romance_points > -3:
                jump readingbookneutral
        "Lean on Sofa":
            $ romance_points -= 1
            show bg walt couch neutral up
            with dis
            play music "Lazy Afternoon.ogg" loop fadein 1.0
            "Drowsy, I decide to fall away from Walt onto the armrest of the sofa, his hand gliding past my fur."

            show bg walt couch neutral down reading
            with dis
            "The expression on his face looks strangely confused, as if he did something wrong."

            show bg walt couch neutral up reading
            with dis
            "He averts his gaze; eyes back on his book. Everything just feels awkward now."

            "I try to get comfortable in my position, but all I'm doing is distracting the wolf from his reading."

            "I wonder how he feels about this whole situation. All I've been thinking about this time is my own feelings, but Walt isn't just a hunk of meat to drool over."

            "Is this awkward for him? Does he like it, too? Does he think it's a supernatural kind of love as well?"

            a hangoverponderingopenclothed "\"I'm doing alright.{w} Sorry for worrying you.\""

            show bg walt couch neutral down
            with dis
            w "\"Do you get these anxiety attacks often?\""

            a hangoverraisedtalkingclothed "\"They aren't rare, but they usually aren't too bad. Having a nightlight helps when I sleep and I take medication, usually.\""

            show bg walt couch upset down
            with dis
            w "\"Usually?\""

            a hangoverupsetclosedclothed "\"I think I forgot with all of the chaos today.\""

            show bg walt couch upset down reading
            with dis
            w "\"Oh...{w} Sorry about that.\""

            show bg walt couch upset down
            with dis
            a "\"I mean, it's both of our faults.{w} We were drunk. Don't pin it just on yourself.\""

            "There's a moment of silence. Walt seems a bit perturbed at that statement, as if I passed my panic baton over to him."

            show bg walt couch upset down reading
            with dis
            w "\"This might sound weird, but...\""

            "I wait for the rest, but Walt's maw just hangs out, like the words are trying to escape but can't."

            w "\"Uh... forget it. Sorry.\""

            show bg walt couch upset down
            with dis
            w "\"It would just sound creepy and weird.\""

            show bg walt couch neutral down reading
            with dis
            "Creepy and weird? Does he feel the same way as I do?"

            show bg walt couch neutral up
            with dis
            "I lean slightly closer to him, and the wolf's eyes light up. It's almost like I hit a light switch inside his brain."

            a hangovercuriousclothed "\"You want to know something fucking dumb?\""

            show bg walt couch neutral down
            with dis
            w "\"What?\""

            a hangoverneutralclothed "\"Silverstone's signature drink is the \'Silver Bullet.\'\""

            show bg walt couch laugh2
            with dis
            w "\"Why are you bringing this up now?\""

            show bg walt couch smile down
            with dis
            a hangoverponderingopenclothed "\"Well, there's an {i}equally{/i} stupid legend about it.\""

            show bg walt couch smile up
            with dis
            a hangoverslyclothed "\"People say that if two people order a Silver Bullet at the same time, their lives are entwined forever.\""

            show bg walt couch neutral down
            with dis
            w "\"Wait, really?\""

            "Not quite the response I expected, but I can't really pin that on him. It is just a hokey legend. Still would've preferred a chuckle at least"

            show bg walt couch upset down
            with dis
            w "\"Yeah, there's absolutely {i}no way{/i} that's real.\""

            a hangoverponderingclothed "\"I mean, yeah, but...\""

            show bg walt couch neutral up
            with dissolve
            pause 1.0
            show bg walt couch neutral down
            with dissolve

            w "\"Sorry.\""

            "I let out a deep breath, and take another swig of my water.{w} The tenseness I felt in my stomach is somewhat lessened."

            "The world is just Walt and I right now.{w} While it isn't perfect, something in me wishes it could it stay that way."

            if romance_points >= 3:
                jump readingbookhappy
            elif romance_points < 3 and romance_points > -3:
                jump readingbookneutral
label readingbookhappy:
    show bg walt couch smile down reading
    with dis
    "Finally, I peer down at Walt's book. The cover is a deep purple, with golden trims running along it."

    "There also seems to be a half-naked man on it, only covered by a burgundy cape and navy shorts."

    show bg walt couch neutral up
    with dis
    a hangoverslyclothed "\"So you gonna tell me about the book you're reading or...?\""

    show bg walt couch smile up
    with dis
    "I chuckle at seeing Walt smile, obviously excited to talk about it."

    show bg walt couch grinning up reading
    with dis
    w "Well, it's this sort of... political sci-fi romance drama, I guess?"

    show bg walt couch grinning up w hand
    with dis
    w "\"This dude gets abducted by an alien when he's studying in Italy, and they make a pact that he'll be the alien's \'pet\' for political gain until they can find a way to get him back home.\""

    show bg walt couch grinning down reading
    with dis
    w "\"However, they've started to form a genuine bond and it turns out that there's more deceit going on in the kingdom than they thought there was.\""

    show bg walt couch upset down reading
    with dis
    w "\"It's... not for everyone. A lot of people don't care for the main character or political intrigue.{w} In fact, most of my classmates just talk about who they'd bone.\""

    show bg walt couch smile up
    with dis
    w "\"Still, I like it. It's surprisingly emotional and I'm a sucker for political romance type stuff.\""

    menu:
        "Sounds Interesting":
            $ romance_points += 1
            show bg walt couch neutral up
            with dis
            a hangovercuriousclothed "\"That... actually sounds pretty interesting.{w} Maybe I'll give it a try.\""

            show bg walt couch grinning up
            with dis
            w "\"Wait, really?!\""

            "I'm a bit stunned at Walt's surprise, but nevertheless glad to see him happy."

            a hangoversurprisedclothed "\"Y-yeah, it sounds like a cool story. Do your classmates really hate it that much?\""

            show bg walt couch laugh2
            with dis
            w "\"I think it's more that they want something more action-packed, to be honest.\""

            show bg walt couch smile up
            with dis
            w "\"There's a miniseries coming out soon, too, so you should read it if you're gonna watch it!\""

            show bg walt couch laugh1
            with dis
            stop music fadeout 3.0
            "I listen intently as the wolf goes on about the space opera, accidentally spoiling certain plot points before apologizing for his mistake."

            "Despite my genuine interest in the topic, my eyes feel heavy and my body feels sluggish."

            show bg walt couch neutral up
            with dis
            "At some point, I think Walt notices. His voice gets a lot quieter and he tones down the exposition."

            show bg couch
            with dis
            "As I nod between the worlds of the living and dreaming, Walt disappears from my vision."

            play sound "BlanketSound2.ogg"
            "Everything suddenly feels warm. I feel around and my heated blanket is wrapped around me."

            show bg walt couch smile down reading
            with dis
            "Walt returns to my vision one last time before I fall asleep."

            scene bg black
            with dissolvelong
            play music "CreepyAmbience.ogg" loop fadein 10.0
            jump dream
        "Sounds Boring":
            $ romance_points -= 1
            show bg walt couch neutral up
            with dis
            stop music fadeout 3.0
            a hangoverclosedclothed "\"I... sort of agree with your classmates on this one.{w} Romance novels just aren't my thing, unfortunately.\""

            show bg walt couch neutral up reading
            with dis
            w "\"Oh, uh... That's okay.\""

            "The wolf's ears droop as he returns to his book. It looks like he's trying to escape back into his reading after my reaction."

            a hangoversurprisedclothed "\"I mean, that's just a personal preference! For all I know it could be a great book!\""

            show bg walt couch neutral down
            with dis
            w "\"You don't have to try to make me feel better about it, you know.\""

            show bg walt couch neutral down reading
            with dis
            w "\"I like what I like, and you like what you like. That's that.\""

            "\'Fuck,\' I whisper to myself. I should've just pretended to be interested."

            "About half an hour of silence passes, and my eyes feel heavy and my body feels sluggish."

            show bg walt couch neutral down
            with dis
            "At some point, I think Walt notices. He turns the pages of his book more slowly and keeps looking back at me."

            show bg couch
            with dis
            "As I nod between the worlds of the living and dreaming, Walt disappears from my vision."

            play sound "BlanketSound2.ogg"
            "Everything suddenly feels warm. I feel around and my heated blanket is wrapped around me."

            show bg walt couch neutral down reading
            with dis
            "Walt returns to my vision one last time before I fall asleep."

            scene bg black
            with dissolvelong
            play music "CreepyAmbience.ogg" loop fadein 10.0
            pause 3.0
            jump dream
label couchneutral:
    play music "Lazy Afternoon.ogg" loop fadein 1.0

    "I sink into the couch, which is an old gift from my mom."

    "My fur catches onto the old knots and tears from it, having been well-used even before she bought it for me."

    "It's definitely broken under the cushions. It feels like my ass is touching hardwood under the thick layer of cotton and cloth."

    "Still, I'd rather be sitting down on a shitty couch then rolling in my bed right now."

    w "\"Here.\""

    "In my anxiety-ridden stupor, I didn't notice that Walt had gone to the kitchen to fetch me a glass of water."

    "My throat does feel a bit parched. I'm a bit confused by that since I was just in the shower. Maybe it's a side effect?"

    show bg walt couch neutral down reading
    with dis
    "Regardless I take a huge gulp of it as Walt sits down next to me, his gaze powerful as he returns to his book."

    "I can't help but wonder why he's been nice to me. We've only known each other for a couple hours by now, and I haven't been a perfect host. Yet it feels like he's my rock."

    "It's too fast. It feels like I'm being pulled into his grasp... even though all he's doing is being a decent guy."

    show bg walt couch neutral up
    with dis
    w "\"\'Water helping?\""

    show bg walt couch neutral down reading
    with dis
    "His eyes are enchanting. Powerful, yet calming."

    "I look down at my glass, but I still feel my ears heat up a little."

    a hangoverponderingclothed "\"It's helping a little bit, yeah.\""

    a hangovercuriousclothed "\"Thanks for getting it, by the way.\""

    show bg walt couch smile up reading
    with dis
    "I can't help but notice how warm his smile is, even if it isn't facing me."

    "Even just a silent \'you're welcome\' causes my chest to tighten a bit."

    show bg walt couch neutral up
    with dis
    a hangoverupsetclosedclothed "\"Sorry you had to see all of that.\""

    show bg walt couch neutral down
    with dis
    w "\"Hey, it's not a problem. No need to apologize.\""

    show bg walt couch neutral down reading
    with dis
    "I can feel my shoulders finally relax as Walt says that. I spot his own ears turning a little pink, being perked up high as if he's listening for something."

    show bg walt couch neutral up
    with dis
    w "\"If you don't mind me asking, though...\""

    a hangoverraisedtalkingclothed "\"It's kind of a long story.\""

    show bg walt couch smile down
    with dis
    w "\"Well then, I'll tell you about what I'm reading in return, haha.\""

    show bg walt couch neutral down
    with dis
    w "\"I mean, only if you want to tell me, though.\""

    "I've never told anyone why the dark terrifies me the way it does. Not even my therapists."

    "I always feel a weight in my stomach, like I've swallowed a rock and can't get it out."

    "...But I don't feel that with Walt. I feel...{w} comfortable.{w} I feel supported."

    "It's a scary feeling that I can't my finger on."

    "I draw in a deep breath, hoping I won't fall into a full-blown anxiety attack."

    a hangoverupsetclosedclothed "\"I wasn't the most... well-behaved kid.{w}{nw}{done}"

    a hangoverponderingopenclothed "\"I wasn't the most... well-behaved kid.{fast} In fact, I was probably the worst of my siblings.\""

    show bg walt couch smile down
    with dis
    w "\"Oooooh, you were a bit of a rascal?{w} A Wily Coyote?\""

    show bg walt couch laugh1
    with vpunch
    "I playfully punch Walt's arm at the remark, holding back laughter myself."

    a hangoverslyclothed "\"Oh, shut up.\""

    show bg walt couch smile up
    with dis
    "The playful air quickly disappears, though I wished it would stay longer."

    show bg walt couch upset up
    with dis
    a hangoverponderingclothed "\"Well, let's just say that my parents shouldn't have been parents.\""

    show bg walt couch upset up reading
    a hangoverupsetclosedclothed "\"One time, I ended up going too far.{w} I accidentally hurt my sister while trying to cut her hair as a prank.\""

    a hangoverraisedtalkingclothed "\"Oh, they were absolutely in the right to punish me. That was fucked up.\""

    "I kind of think Walt's broken gaze is simply because of what I did. It doesn't matter that it's been like... 18, 19 years. I still feel the guilt to this day."

    stop music fadeout 2.0
    a hangoverupsetclosedclothed "\"The next thing I remember is my dad throwing me by the collar into the hallway closet.\""

    show bg walt couch upset up
    with dis
    a hangoverponderingclothed "\"I remember he taped cardboard over the blinds of the door.{w} 'Asshole even put blankets around the door frame so no light could get in.\""

    a hangoverupsetclosedclothed "\"I couldn't tell how many hours I had been in there.\""

    a hangoverupsetclosedclothed "\"I couldn't hear anything besides the ringing in my ears.\""

    a hangoverupsetclosedclothed "\"The clothes felt like bugs swarming me.\""

    a hangoverupsetclosedclothed "\"I just...\""

    a hangoversurprisedclothed "\"It just...\""

    show bg walt couch snarl up
    "I draw in some air, deciding to end the story there before I find I'm sinking deeper into myself."

    "Walt is staring at me, fangs flaring. His face is dressed in horror."

    show bg walt couch upset down reading
    with dis
    "He runs a hand down his muzzle, letting out a deep breath. I can't help but feel like I scared him."

    show bg walt couch snarl down
    with dis
    w "\"I shouldn't have asked you to tell me that.{w}{nw}{done}"

    show bg walt couch upset down
    with dis
    w "\"I shouldn't have asked you to tell me that.{fast} I'm sorry. That was fucking idiotic of me.\""

    "I almost feel like crying.{w} I'm usually told that it's my fault that I get emotional like that.{w} But then there's Walt."

    "What does he have to apologize for? It was me who suddenly fell into a wormhole of memories."

    show bg walt couch snarl up w hand
    with dis
    "A single tear runs down my cheek. The wolf instantly notices, and places his hand on my head; wiping the tear away with his thumb."

    show bg walt couch snarl up
    with dis
    w "\"Fuck, are you okay?\""

    show bg walt couch upset up
    with dis
    "Walt's pawpads feel rough and warm, and I can't help but feel comforted by it. I realize that my tears this time are happy, not sad."

    "Am I this easily moved? Just by someone showing kindness?"

    show bg walt couch snarl up
    with dis
    "I laugh internally at the thought, unsure what to make of it. I smile at the wolf, who looks incredulous."

    w "\"Asher?\""

    menu:
        "Lean on Walt":
            $ romance_points += 1
            show bg walt couch neutral up
            with dis
            play music "Lazy Afternoon.ogg" loop fadein 1.0
            "Drowsy, I fall onto Walt's shoulder. It's firm, but the fur provides enough padding to keep from feeling like I'm lying down on smooth stone."

            "His fur is surprisingly soft, and it smells of mint and alder from the shampoo he used."

            show bg walt couch neutral down reading
            with dis
            "Looking up to the wolf, he quickly averts his gaze; eyes back on his book."

            "His ears are flushed and I can see a bit of pink bursting out from his cheeks."

            "I wonder how he feels about this whole situation. All I've been thinking about this time is my own feelings, but Walt isn't just a hunk of meat to drool over."

            "Is this awkward for him? Does he like it, too? Does he think this has a weird vibe to it as well?"

            a hangoverponderingopenclothed "\"I'm doing alright.{w} Sorry for worrying you.\""

            show bg walt couch neutral down
            with dis
            w "\"Do you get these anxiety attacks often?\""

            a hangoverraisedtalkingclothed "\"They aren't rare, but they usually aren't too bad. Having a nightlight helps when I sleep and I take medication, usually.\""

            show bg walt couch neutral down reading
            with dis
            w "\"Ah.\""

            "It's only now I realize that I forgot to take my meds, probably because of today's chaos."

            "I want to go take them, but the comforting spirit of Walt is lulling me into a tired state."

            show bg walt couch upset down reading
            with dis
            w "\"Once again, I'm sorry about—\"{nw}"
            window show
            pause 0.15

            window auto show

            show bg walt couch neutral up
            a "\"Hey, you didn't know.{w} Sometimes these things happen. Don't pin it just on yourself.\""

            "There's a moment of silence. Walt seems a bit perturbed at that statement, as if I passed my panic baton over to him."

            show bg walt couch upset down reading
            with dis
            w "\"This might sound weird, but...\""

            show bg walt couch upset up reading
            with dis
            w "\"Ever since this morning, I've just... felt this need to protect you."

            show bg walt couch upset down reading
            with dis
            w "\"And I've felt like I've done a shit job.\""

            "So he has been feeling the same in some capacity."

            show bg walt couch upset down
            with dis
            w "\"I didn't want to say anything at first because it sounds... creepy and weird, but...\""

            w "\"I don't know. I just feel like you're someone worth more than you might think you are.\""

            a hangoverslyclothed "\"Am I that easy to read?\""

            show bg walt couch smile down reading
            with dis
            w "\"Hey, I'm serious.\""

            "It's nice to see the wolf crack a smile again, even if it's a bit somber."

            show bg walt couch neutral up
            with dis
            "I lean in closer to him, my muzzle practically rubbing against his arm at this point. I gently poke his book and look up at the ceiling."

            a hangovercuriousclothed "\"You want to know something fucking dumb?\""

            show bg walt couch neutral up reading
            with dis
            w "\"What?\""

            a hangoverneutralclothed "\"Silverstone's signature drink is the \'Silver Bullet.\'\""

            show bg walt couch laugh2
            with dis
            w "\"Why are you bringing this up now?\""

            show bg walt couch smile down
            with dis
            a hangoverponderingopenclothed "\"Well, there's an {i}equally{/i} stupid legend about it.\""

            show bg walt couch smile up
            with dis
            a hangoverslyclothed "\"People say that if two people order a Silver Bullet at the same time, their lives are entwined forever.\""

            show bg walt couch laugh1
            with dis
            w "\"What?!\""

            "I can feel Walt's muscles flex as he bellows.{w} It's a bit uncomfortable, but I can't help but smile as he roars with laughter."

            show bg walt couch smile down
            with dis
            w "\"Yeeeeah, there's absolutely {i}no way{/i} that's real.\""

            a hangoversmilingclosedclothed "\"But I got you to laugh, didn't I?\""

            show bg walt couch neutral up
            with dissolve
            pause 1.0
            show bg walt couch smile down
            with dissolve

            w "\"I guess you did.\""

            "I let out a deep breath, Walt's fur spreading out as the air hits his arm.{w} The tenseness I felt in my stomach has finally disappeared."

            "The world is just Walt and I right now.{w} I wish it could it stay that way."

            if romance_points >= 3:
                jump readingbookhappy
            elif romance_points < 3 and romance_points > -3:
                jump readingbookneutral
            elif romance_points <= -3:
                jump readingbookangry
        "Lean on Sofa":
            $ romance_points -= 1
            show bg walt couch neutral up
            with dis
            play music "Lazy Afternoon.ogg" loop fadein 1.0
            "Drowsy, I decide to fall away from Walt onto the armrest of the sofa, his hand gliding past my fur."

            show bg walt couch neutral down reading
            with dis
            "The expression on his face looks strangely confused, as if he did something wrong."

            show bg walt couch neutral up reading
            with dis
            "He averts his gaze; eyes back on his book. Everything just feels awkward now."

            "I try to get comfortable in my position, but all I'm doing is distracting the wolf from his reading."

            "I wonder how he feels about this whole situation. All I've been thinking about this time is my own feelings, but Walt isn't just a hunk of meat to drool over."

            "Is this awkward for him? Does he like it, too? Does he think this has a weird vibe to it as well?"

            a hangoverponderingopenclothed "\"I'm doing alright.{w} Sorry for worrying you.\""

            show bg walt couch neutral down
            with dis
            w "\"Do you get these anxiety attacks often?\""

            a hangoverraisedtalkingclothed "\"They aren't rare, but they usually aren't too bad. Having a nightlight helps when I sleep and I take medication, usually.\""

            show bg walt couch neutral down reading
            with dis
            w "\"Mmm.\""

            "Walt doesn't look up from his book, and I can't help but wonder if he actually registered my response."

            "It's only now I realize that I forgot to take my meds, probably because of today's chaos."

            "I want to go take them, but I feel exhausted just from shifting around trying to get comfortable."

            show bg walt couch upset down reading
            with dis
            w "\"Sorry again, by the way."

            show bg walt couch neutral down
            with dis
            a "\"I mean, you didn't know.{w} Shit happens. Don't pin it just on yourself.\""

            "There's a moment of silence. Walt seems a bit perturbed at that statement, as if I passed my panic baton over to him."

            show bg walt couch upset down reading
            with dis
            w "\"This might sound weird, but...\""

            "I wait for the rest, but Walt's maw just hangs out, like the words are trying to escape but can't."

            w "\"Uh... forget it. Sorry.\""

            show bg walt couch upset down
            with dis
            w "\"It would just sound creepy and weird.\""

            show bg walt couch upset down reading
            with dis
            "Creepy and weird? Does he feel the same way as I do?"

            show bg walt couch neutral up
            with dis
            "I lean slightly closer to him, and the wolf's eyes light up. It's almost like I hit a light switch inside his brain."

            a hangovercuriousclothed "\"You want to know something fucking dumb?\""

            show bg walt couch neutral down reading
            with dis
            w "\"What?\""

            a hangoverneutralclothed "\"Silverstone's signature drink is the \'Silver Bullet.\'\""

            show bg walt couch laugh2
            with dis
            w "\"Why are you bringing this up now?\""

            show bg walt couch smile down
            with dis
            a hangoverponderingopenclothed "\"Well, there's an {i}equally{/i} stupid legend about it.\""

            show bg walt couch smile up
            with dis
            a hangoverslyclothed "\"People say that if two people order a Silver Bullet at the same time, their lives are entwined forever.\""

            show bg walt couch neutral down
            with dis
            w "\"Wait, really?\""

            "Not quite the response I expected, but I can't really pin that on him. It is just a hokey legend. Still would've preferred a chuckle at least."

            show bg walt couch upset down
            with dis
            w "\"Well, there's absolutely {i}no way{/i} that's real.\""

            a hangoverponderingclothed "\"I mean, yeah, but...\""

            show bg walt couch neutral up
            with dissolve
            pause 1.0
            show bg walt couch neutral down
            with dissolve

            w "\"Sorry.\""

            "I let out a deep breath, and take another swig of my water.{w} The tenseness I felt in my stomach is still there, but feels a bit lighter."

            "The world is just Walt and I right now.{w} While it isn't perfect, something in me wishes it could it stay that way."

            if romance_points >= 3:
                jump readingbookhappy
            elif romance_points < 3 and romance_points > -3:
                jump readingbookneutral
            elif romance_points <= -3:
                jump readingbookangry
label readingbookneutral:
    show bg walt couch neutral down reading
    with dis
    "Finally, I peer down at Walt's book. The cover is a gradient of pink and purple, with faux scars mapping it."

    "There also seems to be two men on it; one in a hoodie and jeans, and the other in what looks like combat gear."

    show bg walt couch neutral up
    with dis
    a hangovercuriousclothed "\"So you gonna tell me about the book you're reading?\""

    show bg walt couch smile up
    with dis
    "I chuckle at seeing Walt smile, obviously excited to talk about it."

    show bg walt couch grinning up reading
    with dis
    w "\"Well, it's this sort of... sci-fi romance, I guess?\""

    show bg walt couch grinning up w hand
    with dis
    w "\"This dude who has a perfect life, even has a boyfriend, gets his life uppended and wakes up in what looks like a new city and his memories gone.\""

    show bg walt couch grinning down reading
    with dis
    w "\"He's found by this wolf, who ends up helping this guy finding his way home. But things don't end up as they seem to be.\""

    show bg walt couch upset down reading
    with dis
    w "\"It's... not for everyone. A lot of people don't understand the complexity of some of the characters.{w} In fact, most of my classmates just bitch about who they don't like.\""

    show bg walt couch smile up
    with dis
    w "\"Still, I enjoy it. It's surprisingly emotional and I'm a sucker for sci-fi genre smashed type stuff.\""

    menu:
        "Sounds Interesting":
            $ romance_points += 1
            show bg walt couch neutral up
            with dis
            a hangovercuriousclothed "\"That... actually sounds pretty interesting.{w} Maybe I'll give it a try.\""

            show bg walt couch grinning up
            with dis
            w "\"Wait, really?!\""

            "I'm a bit stunned at Walt's surprise, but nevertheless glad to see him happy."

            a hangoversurprisedclothed "\"Y-yeah, it sounds like a cool story. Do your classmates really hate it that much?\""

            show bg walt couch laugh2
            with dis
            w "\"I think it's more that they want something that's less of a slow burn, to be honest.\""

            show bg walt couch smile up
            with dis
            w "\"There's a miniseries coming out soon, too, so you should read it if you're gonna watch it!\""

            show bg walt couch laugh1
            with dis
            stop music fadeout 3.0
            "I listen intently as the wolf goes on about the cyberpunk love story, accidentally spoiling certain plot points before apologizing for his mistake."

            "Despite my genuine interest in the topic, my eyes feel heavy and my body feels sluggish."

            show bg walt couch neutral up
            with dis
            "At some point, I think Walt notices. His voice gets a lot quieter and he tones down the exposition."

            show bg couch
            with dis
            "As I nod between the worlds of the living and dreaming, Walt disappears from my vision."

            play sound "BlanketSound2.ogg"
            "Everything suddenly feels warm. I feel around and my heated blanket is wrapped around me."

            show bg walt couch smile down reading
            with dis
            "Walt returns to my vision one last time before I fall asleep."

            scene bg black
            with dissolvelong
            play music "CreepyAmbience.ogg" loop fadein 10.0
            jump dream
        "Sounds Boring":
            $ romance_points -= 1
            show bg walt couch neutral up
            with dis
            stop music fadeout 3.0
            a hangoverclosedclothed "\"I... sort of agree with your classmates on this one.{w} I just kind of like to turn my brain off, unfortunately.\""

            show bg walt couch neutral up reading
            with dis
            w "\"Oh, uh... That's okay.\""

            "The wolf's ears droop as he returns to his book. It looks like he's trying to escape back into his reading after my reaction."

            a hangoversurprisedclothed "\"I mean, that's just a personal preference! For all I know it could be a great book!\""

            show bg walt couch neutral down
            with dis
            w "\"You don't have to try to make me feel better about it, you know.\""

            show bg walt couch neutral down reading
            with dis
            w "\"I like what I like, and you like what you like. That's that.\""

            "\'Fuck,\' I whisper to myself. I should've just pretended to be interested."

            "About half an hour of silence passes, and my eyes feel heavy and my body feels sluggish."

            show bg walt couch neutral down
            with dis
            "At some point, I think Walt notices. He turns the pages of his book more slowly and keeps looking back at me."

            show bg couch
            with dis
            "As I nod between the worlds of the living and dreaming, Walt disappears from my vision."

            play sound "BlanketSound2.ogg"
            "Everything suddenly feels warm. I feel around and my heated blanket is wrapped around me."

            show bg walt couch neutral down reading
            with dis
            "Walt returns to my vision one last time before I fall asleep."

            scene bg black
            with dissolvelong
            play music "CreepyAmbience.ogg" loop fadein 10.0
            pause 3.0
            jump dream
label couchangry:
    "I sink into the couch, which is an old gift from my mom."

    "My fur catches onto the old knots and tears from it, having been well-used even before she bought it for me."

    "It's definitely broken under the cushions. It feels like my ass is touching hardwood under the thick layer of cotton and cloth."

    "Still, I guess I'd rather be sitting down on a shitty couch then rolling in my bed right now."

    show bg walt couch upset down reading
    with dis
    "My body leans a bit as Walt sitting down causes the cushions to slump down. I try to say something, but I realize how dry my throat is."

    "I'm a bit confused by that since I was just in the shower. Maybe it's a side effect?"

    "I can't help but wonder what Walt thinks of me. We've only known each other for a couple hours by now, and our relationship has been pretty turbulent. Yet it feels like he's my rock."

    "It's too fast. It feels like I'm being pulled into his grasp... and it scares me since I don't know if he's actually a nice guy."

    show bg walt couch upset down
    with dis
    w "\"Can I help you?\""

    "Only now do I realize I've been staring at him. His eyes are enchanting. Powerful and menacing."

    "I look down at my legs, wondering why I feel my ears heat up a little."

    a hangoverponderingclothed "\"No, sorry.\""

    w "\"Mmm.\""

    show bg walt couch upset down reading
    with dis
    "The silence hangs for a minute, with the only sound coming from me shifting my legs around in discomfort."

    "After an agonizing amount of time, I finally spit the words out."

    a hangoverupsetclosedclothed "\"Sorry you had to see all of that.\""

    w "\"It's fine.\""

    "Walt's indifference kind of unsettles me. I feel some sort of connection between us, and I see his ears turning pink, but..."

    "I don't even know if I want this connection now."

    # SKIP ANXIETY EXPLANATION

    "All I feel now is exhaustion from my panic attack and the emotional toll of today. I can feel my body swaying a bit as I pick my destination."

    show bg walt upset up
    with dis
    "I see Walt's eyes dart over as I start to fall, wondering if he's worried or just confused at my behavior.
    "
    show bg walt couch snarl up
    with dis
    w "\"Asher?\""

    menu:
        "Lean on Walt":
            $ romance_points += 1
            show bg walt couch neutral up
            with dis
            play music "Lazy Afternoon.ogg" loop fadein 1.0
            "To the wolf's surprise, I place my head on his shoulder. It's firm, but the fur provides enough padding to keep from feeling like I'm lying down on smooth stone."

            "His fur is surprisingly soft, and it smells of mint and alder from the shampoo he used."

            show bg walt couch upset down reading
            with dis
            "Looking up to the wolf, he quickly averts his gaze; eyes back on his book."

            "His ears are flushed and I can see a bit of pink bursting out from his cheeks."

            "I wonder how he feels about this whole situation. All I've been thinking about this time is my own feelings, but Walt isn't just a hunk of meat to drool over."

            "Is this awkward for him? Does he even like it? Does he think this has a weird vibe to it as well?"

            a hangoverclosedclothed "\"I'm doing alright.{w} Sorry for worrying you.\""

            "It's a good minute before I get a response from Walt."

            show bg walt couch neutral down reading
            with dis
            w "\"Do you get anxiety attacks often?\""

            "So he does care. At least a little, that is."

            a hangoverclosedclothed "\"They aren't rare, but they usually aren't too bad. Having a nightlight helps when I sleep and I take medication, usually.\""

            show bg walt couch upset down reading
            with dis
            w "\"Ah.\""

            "It's only now I realize that I forgot to take my meds, probably because of today's chaos."

            "I want to go take them, but the warmth of Walt's fur is lulling me into a tired state."

            show bg walt couch upset down
            with dis
            w "\"I'm sorry I was a bit of an asshole about it.{w} That was uncalled for.\""

            a "\"You didn't know.{w} Sometimes these things happen. Just be a bit more considerate next time.\""

            "There's a moment of silence. Walt seems a bit perturbed at that statement, maybe because I ended up saying \'next time.\' It's as if I passed my panic baton over to him."

            show bg walt couch upset down reading
            with dis
            w "\"This might sound weird, but...\""

            show bg walt couch upset up reading
            with dis
            w "\"Ever since this morning, I've just... felt this need to protect you."

            show bg walt couch upset down reading
            with dis
            w "\"And I've definitely done a shit job at that.\""

            "So he has been feeling the same in some capacity."

            show bg walt couch upset down
            with dis
            w "\"I didn't want to say anything at first because it sounds... creepy and weird, but...\""

            w "\"I don't know. I just feel like you're someone worth more than you might think you are.\""

            a hangoverraisedtalkingclothed "\"Am I that easy to read?\""

            show bg walt couch neutral down
            with dis
            w "\"Hey, I'm serious.\""

            "It's nice to see the wolf care about me like this, even if his tone is a bit somber."

            show bg walt couch neutral up
            with dis
            "I lean in closer to him, my muzzle practically rubbing against his arm at this point. I sneak a peek over at his book and look up at the ceiling."

            a hangovercuriousclothed "\"You want to know something fucking dumb?\""

            show bg walt couch neutral up reading
            with dis
            w "\"What?\""

            a hangoverneutralclothed "\"Silverstone's signature drink is the \'Silver Bullet.\'\""

            show bg walt couch neutral down
            with dis
            w "\"Oh, yeah?\""

            show bg walt couch neutral down reading
            with dis
            a hangoverponderingclothed "\"Well, there's an {i}equally{/i} stupid legend about it.\""

            show bg walt couch neutral down
            with dis
            a hangoverneutralclothed "\"People say that if two people order a Silver Bullet at the same time, their lives are entwined forever.\""

            show bg walt couch snarl down
            with dis
            w "\"Uh...\""

            "I can feel Walt's muscles flex as he lets his disappointment out.{w} It's a bit uncomfortable, and I end up looking away as his eyes meet mine."

            show bg walt couch upset down
            with dis
            a hangoverponderingclothed "\"Never mind. Forget I said anything.\""

            a hangoverponderingclothed "\"It's stupid anyway.\""

            show bg walt couch upset down reading
            with dis
            "I let out a deep breath, Walt's fur spreading out as the air hits his arm.{w} The tenseness I felt in my stomach has finally disappeared."

            "The world is just Walt and I right now.{w} I wish it could it stay that way."

            if romance_points < 3 and romance_points > -3:
                jump readingbookneutral
            elif romance_points <= -3:
                jump readingbookangry
        "Lean on Sofa":
            $ romance_points -= 1
            show bg walt couch upset up
            with dis
            play music "Lazy Afternoon.ogg" loop fadein 1.0
            "I ultimately decide to swing away from Walt, my head hitting the hard armrest as I let gravity do the rest of the work."

            show bg walt couch snarl down reading
            with dis
            "The expression on his face looks strangely confused, as if he did something wrong."

            show bg walt couch upset down reading
            with dis
            "He averts his gaze; eyes back on his book. Everything just feels awkward now."

            "I try to get comfortable in my position, but all I'm doing is distracting the wolf from his reading."

            "I wonder how he feels about this whole situation. All I've been thinking about this time is my own feelings, but Walt isn't just a hunk of meat to drool over."

            "Is this awkward for him? Does he even like me? Does he think this has a weird vibe to it as well?"

            a hangoverclosedclothed "\"I'm doing alright.{w} Sorry for worrying you.\""

            "No response.{w} Walt doesn't look up from his book, and I can't help but wonder if he actually registered my response."

            "Maybe he just chose to ignore me."

            "It's only now I realize that I forgot to take my meds, probably because of today's chaos."

            "I want to go take them, but I feel exhausted just from... well, everything."

            show bg walt couch snarl up reading
            "There's a moment of silence before I suddenly hear the wolf take a deep breath."

            show bg walt couch snarl down reading
            with dis
            w "\"This might sound weird, but...\""

            "I wait for the rest, but Walt's maw just hangs out, like the words are trying to escape but can't."

            show bg walt couch upset down reading
            with dis
            w "\"Uh... forget it. Sorry.\""

            show bg walt couch upset down
            with dis
            w "\"It would just sound creepy and weird.\""

            show bg walt couch upset down reading
            with dis
            "Creepy and weird? Does he feel the same way as I do?"

            show bg walt couch upset up
            with dis
            "I lean slightly closer to him, and the wolf's eyes light up. It's almost like I hit a light switch inside his brain."

            a hangovercuriousclothed "\"You want to know something fucking dumb?\""

            show bg walt couch upset up reading
            with dis
            w "\"What?\""

            a hangoverneutralclothed "\"Silverstone's signature drink is the \'Silver Bullet.\'\""

            show bg walt couch upset down
            with dis
            w "\"Oh, yeah?\""

            show bg walt couch upset down reading
            with dis
            a hangoverponderingclothed "\"Well, there's an {i}equally{/i} stupid legend about it.\""

            show bg walt couch upset down
            with dis
            a hangoverneutralclothed "\"People say that if two people order a Silver Bullet at the same time, their lives are entwined forever.\""

            show bg walt couch upset down reading
            with dis
            w "\"And people actually believe that?\""

            "Not quite what I expected from Walt, but I can't really pin that on him. It is just a hokey legend. Still would've preferred a chuckle at least."

            show bg walt couch snarl down reading
            with dis
            w "\"Well, there's absolutely {i}no way{/i} that's real.\""

            show bg walt couch upset down reading
            with dis
            a hangoverponderingclothed "\"I mean, yeah, but...\""

            "I wish I could find the words to say, but Walt is right. It's a dumb hokey legend that was probably made to be a tourist trap."

            "A deep sigh escapes my mouth, and my brows furrow."

            show bg walt couch upset down
            with dis
            a hangoverupsetclosedclothed "\"You know what? Just forget it.\""

            "I turn back away from the wolf, my teeth grinding against each other.{w} The tenseness I feel in my stomach exasperates, and I don't even know what to think of Walt anymore."

            "The world is just him and I right now.{w} What scares me is that despite me hating it, something in me wishes it could it stay that way."

            if romance_points < 3 and romance_points > -3:
                jump readingbookneutral
            elif romance_points <= -3:
                jump readingbookangry
label readingbookangry:
    show bg walt couch upset down reading
    with dis
    "Finally, I peer down at Walt's book. The cover is a sky blue, with white spots decorating it like paw prints."

    "There also seems to be a young man on it; a cat wearing an orange beanie and a dirt-brown shirt."

    show bg walt couch upset up
    with dis
    a hangovercuriousclothed "\"So what'cha reading?\""

    show bg walt couch neutral up reading
    with dis
    "Walt seems like he wants to tell me what it is, but is a bit hesitant."

    show bg walt couch neutral up
    with dis
    "Eventually he relents, letting out a small whistle as he begins to explain it."

    show bg walt couch neutral down reading
    with dis
    w "\"Well, it's a romantic comedy with...{w}{nw}{done}"

    show bg walt couch snarl up reading
    with dis
    w "\"Well, it's a romantic comedy with...{fast} I guess it would be a touch of supernatural horror?\""

    show bg walt couch snarl up w hand
    with dis
    w "\"Basically, this guy with social anxiety goes to college and ends up reconnecting with an old friend.\""

    show bg walt couch neutral down reading
    with dis
    w "\"They end up connecting through exercise and revelations about their past, and even start a relationship together.\""

    show bg walt couch upset down reading
    with dis
    w "\"It's... not for everyone. While there's a lot of heart, the jokes can be pretty dark or risque.{w} In fact, most of my classmates just repeat the jokes and complain about how fast the relationship moves.\""

    show bg walt couch neutral up
    with dis
    w "\"Still, I enjoy it. It's actually pretty relatable and I love the mystery behind the supernatural stuff.\""

    menu:
        "Sounds Interesting":
            $ romance_points += 1
            show bg walt couch neutral up
            with dis
            a hangovercuriousclothed "\"That... actually sounds pretty interesting.{w} Maybe I'll give it a try.\""

            show bg walt couch snarl up
            with dis
            w "\"Wait, really?!\""

            "I'm a bit stunned at Walt's surprise, but nevertheless glad to see him happy."

            a hangoverraisedtalking2clothed "\"Y-yeah, it sounds like a cool story. Do your classmates really hate it that much?\""

            show bg walt couch laugh2
            with dis
            w "\"I think it's more that they want something that's \'realistic,\' to be honest.\""

            show bg walt couch smile up
            with dis
            w "\"There's a miniseries coming out soon, too, so you should read it if you're gonna watch it!\""

            show bg walt couch grinning down reading
            with dis
            stop music fadeout 3.0
            "I listen intently as the wolf goes on about the unique genre mash, accidentally spoiling certain plot points before apologizing for his mistake."

            "Despite my genuine interest in the topic, my eyes feel heavy and my body feels sluggish."

            show bg walt couch neutral up
            with dis
            "At some point, I think Walt notices. His voice gets a lot quieter and he tones down the exposition."

            show bg couch
            with dis
            "As I nod between the worlds of the living and dreaming, Walt disappears from my vision."

            play sound "BlanketSound2.ogg"
            "Everything suddenly feels warm. I feel around and my heated blanket is wrapped around me."

            show bg walt couch neutral down reading
            with dis
            "Walt returns to my vision one last time before I fall asleep."

            scene bg black
            with dissolvelong
            play music "CreepyAmbience.ogg" loop fadein 10.0
            jump dream
        "Sounds Boring":
            $ romance_points -= 1
            show bg walt couch neutral up
            with dis
            stop music fadeout 3.0
            a hangoverclosedclothed "\"I... sort of agree with your classmates on this one.{w} I like my romances to build up, ya know?\""

            show bg walt couch upset down reading
            with dis
            w "\"Oh, uh... That's okay.\""

            "The wolf's ears droop as he returns to his book. It looks like he's trying to escape back into his reading after my reaction."

            a hangoverneutralclothed "\"I mean, that's just a personal preference. For all I know it could be a great book.\""

            "Walt just ignores me, putting his full attention into the book. Whatever goodwill I had with him feels like it's disappeared."

            "\'Fuck,\' I whisper to myself. I should've just pretended to be interested."

            "About half an hour of silence passes, and my eyes feel heavy and my body feels sluggish."

            show bg walt couch upset down
            with dis
            "At some point, I think Walt notices. He turns the pages of his book more slowly and keeps looking back at me."

            show bg couch
            with dis
            "As I nod between the worlds of the living and dreaming, Walt disappears from my vision."

            "I wait for him to come back, my eyes fighting me. However, he doesn't return."

            "Emotionally defeated, I let my eyes close and I fall asleep."

            scene bg black
            with dissolvelong
            play music "CreepyAmbience.ogg" loop fadein 10.0
            pause 3.0
            jump dream