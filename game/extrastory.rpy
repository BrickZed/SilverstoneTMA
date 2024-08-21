label ExtraStory:
    stop music fadeout 2.0
    scene bg black
    with fadehold
    window auto show
    r "\"The year is 1927…\""
    
    scene bg movies with dissolve
    "I'm staring at {i}that{/i} video once again.{w} The same one I've played over and over for the past two months."
    "A muscular otter, my friend Riley, is reciting the town\'s history into his LAV mic, standing a fair distance away from the subject of the video: Silverstone, Oregon."
    r "\"... A town that once had a population of over 7000 people in the 1920s and is now standing at just under 400 people today…\""
    "I'm going to be moving there in a few days, but none of the legends about this town have deterred me from leaving my hometown.{w} I mean… he's there, after all."
    "I've memorized the exposition about Silverstone by this point. Freak accidents in the '20s and '30s, and a mass exodus of the town's population by 2002."
    "To be honest, I'm surprised that Asher still lives over there given the rumors."
    "As the video's intro drones on, I feel my phone rumble in my pocket."
    "I whip it out, hoping it's him."
    window hide
    show phonetext1 at offscreenbottom
    show phonetext1 at truecenter with MoveTransition(0.2)
    pause 1.0
    window auto
    "Oh... 'Just Clyde."

    window hide
    show PhoneFadeClyde
    show phonetext1_1 behind PhoneFadeClyde
    hide phonetext1
    $ renpy.pause()
    show phonetext1_2
    hide phonetext1_1
    $ renpy.pause()
    show phonetext1_3
    hide phonetext1_2
    $ renpy.pause()
    show phonetext1_4
    hide phonetext1_3
    $ renpy.pause()
    show phonetext1_5
    hide phonetext1_4
    $ renpy.pause()
    show phonetext1_6
    hide phonetext1_5
    $ renpy.pause()
    show phonetext1_7
    hide phonetext1_6
    $ renpy.pause()
    show phonetext1_7 at offscreenbottom with MoveTransition(0.2)
    window auto show

    "I turn my attention back to my laptop as the two's theme song blares in my ears.{w} I can remember the night they made it, just moving notes around in the free trial of their music program."
    "Flashy visuals of Riley and Clyde exploring abandoned malls, towns, and mansions decorate the screen before it finally returns to the otter."
    "He's now by the town's boardwalk; his fur coated with sand from the windy day they shot this on. The audio quality occasionally dips as the wind drums against the microphone."
    r "\"On the surface, Silverstone, Oregon appears to be the perfect spot for tourists to come to and enjoy the sights that the Northwest has to offer.\""
    r "\"Once a bustling town many flocked to for holidays or just a quick summer getaway became marred with tragic history and, eventually, a mass exodus that sealed its fate.\""
    "Riley's words make me chuckle a bit; his melodramatic delivery not helping his case."
    "I wish I could just roll my eyes at it, but the video is unfortunately accurate."
    "Every 15 years seemed to have a new disaster for the town since its founding in 1927.{w} The worst case seemed to have been the last incident in 2002, where over half of the town's population left."
    "I asked the two for more details on it, but even for them it was hard to find much.{w} Asher didn't seem to know much either, having moved to the town long after the incident occurred."
    r "\"Oh god, are you actually watching that video again?\""
    "I jolt up, a bit confused at first by the change in dialogue. However, a paw on my shoulder quickly pulls me to reality."
    show riley embarrassed at offscreenleft
    show riley embarrassedtalking at truecenter with MoveTransition(0.4)
    r "\"Can you please just read a history book for once?{w} Even going and searching up the town would be better.\""
    play music "Lazy Afternoon.ogg" loop fadein 1.0
    show clyde chilltalkingriley at offscreenleft
    pause (0.1)
    show clyde chilltalkingriley at furtherleft
    show riley embarrassedclyde at furtherright
    with MoveTransition(0.3)
    cl "\"Dude, relax. Bro's giving us free views like this.\""
    show clyde chillriley
    r embarrassedtalkingclyde "\"I know, but my delivery in that video is shit and we even got some facts wrong.\""
    show riley embarrassed
    show clyde chill
    ws questioning "\"Don't you... get facts wrong in all of your videos? You {i}are{/i} a paranormal investigation channel after all.\""
    show clyde chillriley
    r embarrassedtalking "\"Kind of hard to feel carefree about it when it's actual history you get wrong.\""
    r excitedtalking "\"Anyway, you ready for the movie? So excited to see it.\""
    show riley excitedclyde
    cl excitedtalkingriley "\"Dude, I was up all night just thinking about it.{w} I marathoned the other movies in the series, too, so I would be prepared.\""
    show clyde excitedconcern
    show riley excitedconcern
    ws grimace "\"Ugh, I wish I could be like you two. I fucking hate horror.\""
    show riley teasing
    cl teasingtalking "\"Relax, we'll see your choice next time, princess.\""
    ws disapproving "\"Wow.{w} Rude.\""
    show clyde shock
    show riley excitedconcern
    ws questioning"\"Also, are you fucking high right now?\""
    show riley shockclyde
    cl shocktalkingriley "\"Ah, fuck, is it that noticeable?\""
    show clyde shockphone
    show riley excitedconcern
    "Clyde pulls out his cell phone, opening the camera app to be met with bright pink, yet dead, eyes."
    show riley shockclyde
    cl upsetphone "\"Shiiiiiiiit, man.\""
    show clyde upsetriley
    r embarrassedtalkingclyde "\"Relax, I doubt the staff here cares about that.\""
    show clyde excitedconcern
    r excitedtalking "\"You ready, Walt?\""
    stop music fadeout 1.0
    window hide
    pause 1.0
    show riley excitedconcern
    play sound "PhoneVibrate1.ogg"
    window auto
    "As if on cue, my phone vibrates, delaying my fate for a bit longer."
    ws apolegtic "\"Uh, just a second, guys.\""
    show clyde shockriley
    r irritatedtalking "\"Oh, God. It's not him again, is it?\""

    window hide
    show phonetext2 at offscreenbottom
    show phonetext2 at truecenter with MoveTransition(0.2)
    window auto show

    "Sure enough, it is."
    
    show phonetext2 at offscreenbottom with MoveTransition(0.2)
    show riley irritated
    "I have no idea why, but Riley always gets super agitated whenever Asher comes up in conversation."
    "I remember when I told them I was moving, he accidentally dug his claws into his arms and had to go to the bathroom to clean himself."
    "I don't think he hates Asher specifically, but more the idea of me being taken away from here.{w} It doesn't help that he knows {i}where{/i} I'm going."
    ws "\"Just lemme answer him super quick.\""
    r "\"Ugh. Fine.\""

    window hide
    show PhoneText2 at offscreenbottom
    show PhoneText2 at truecenter with MoveTransition(0.2)
    show PhoneFadeAsher
    show phonetext2_1 behind PhoneFadeAsher
    $ renpy.pause()
    show phonetext2_2
    hide PhoneText2
    hide phonetext2_1
    $ renpy.pause()
    show phonetext2_3
    hide phonetext2_2
    $ renpy.pause()
    show phonetext2_4
    hide phonetext2_3
    $ renpy.pause()
    show phonetext2_5
    hide phonetext2_4
    $ renpy.pause()
    show phonetext2_5 at offscreenbottom with MoveTransition(0.2)
    window auto show

    "I can't help but giggle as I send Asher texts, though I can feel Riley's eyes shooting at my phone like daggers."

    "Clyde is shuffling his feet, possibly trying to avoid the topic altogether.{w} If this is going to be one of our last days together, though, it needs to be addressed."
    ws "\"Riley, seriously. What is your problem with Asher?\""
    "Riley looks surprised at the statement, almost offended. His reaction shocks me, since I expected a more grounded response."
    r "\"I don't...{w} I don't hate Asher.\""
    cl "\"Not going to lie, it feels like you do.\""
    "Riley's gaze shoots over to Clyde before he pinches the bridge of his nose and returns his focus to me."
    r "\"It's just... Are you seriously moving to that place just for a guy?\""
    ws "\"Oh my god, you can't be serious.\""
    "I can feel my face heating up and I run my hands through my fur. This was the reason he was so pissy about Asher?"
    r "\"No, seriously!{w} I like Asher; he's a good dude, but...\""
    r "\"Why do you have to move to Silverstone of all places?\""
    cl "\"Riley.\""
    "Clyde's usual jovial mood has soured. His tone is stern, trying to end the conversation as soon as possible."
    ws "\"Riley, it's just for rent reasons. It's outrageous here, but Silverstone is manageable for us.\""
    ws "\"Seriously, besides these urban legends, what is wrong with the town?\""
    "Riley begins to speak, but silence lingers in the air. It's as if Riley has the facts, but they're stuck in his throat."
    "After an uncomfortable amount of time passes, Clyde claps his hands together. Riley's fur, as well as mine, spread out as the air from the impact collides against us."
    cl "\"I think I'm going to get some popcorn. Come in when you two are ready, okay?\""
    "Before either of us can get a word in, Clyde bounds to the theater door.{w} The two of us stare at each awkwardly before I start to pack my laptop."
    "The warm summer air is heavy as we stand there. This isn't how I wanted things to go, but I'd rather hear his true feelings than another lie."
    "Still, I can't help but feel like I fucked up there. I zip up my backpack, sling it over my shoulder, and look up at the theater sign.{w} What happens here will be our last memory together for a while."

    menu:
        "Get Snacks With Clyde":
            $ Clyde = True
            "The sun is blistering, and my dark fur isn't helping me beat the heat."
            "I head toward the theater, hoping that Riley will follow me, but he just stands at the sidewalk; arms crossed.{w} His tail points to the ground and our conversation ends in a stalemate."
            "I let out a deep exasperated sigh as I open the doors, hit with a wave of immediate regret and air conditioning."

            "I'll never take modern tech for granted again. The cold air provides some relief from the summer weather, although my fur is still hot to the touch."
            "I head right to my destination: the concessions.{w} I plant my feet behind Clyde and flip through the boxes of candy on display before pulling out some sour gummies and lemon chews."
            "Clyde is staring up at the menu and I wonder how he can pay attention to it with the dad yelling at his kid in front of us."
            da "You said you didn't care about the flavor!"
            k "But this one tastes weird!"
            "Clyde turns to me briefly, his eyes still a faint pink from the weed, and rotates his finger in a circle after his ear."
            "The cashier lets out a stifled chuckle and the dad miraculously doesn't notice."
            "After a minute or two, the dad walks away with his crying child, still holding their half-frozen strawberry ice cream."
            "Quickly returning my attention to the museum of junk food, Clyde gives a hard nod and steps up to give his order."
            cl "\"A large bucket of popcorn, a hot dog, and an extra-large soda, please.\""
            "I can't help but cringe by the order. As impressive as it is, thinking about putting that much food in my stomach causes my stomach to whirl."
            c "\"Would you like better with that?\""
            cl "\"Extra, please!\""
            "Barf."
            "It's like karma is striking me for nearly ruining our last day together. Fair enough, I guess."
            "As the poor cashier gets his order ready, the binturong swivels to face me. Although he's still a bit dazed from the drugs, he notices Riley's absence right away."
            cl "\"He's just upset that you're leavin', man.\""
            "I give him a faint smile. We both know how much of a half-lie it is, but the reassurance strangely helps."
            ws "\"Yeah, I know.{w} I just wish it wouldn't end like this.\""
            cl "\"Want me to talk to him for ya?{w} Get it into his thick skull?\""
            ws "\"Nah. It'd be better if I talked to him after the movie.\""
            "The door loudly squeaks and the otter finally enters, quickly sitting on the lobby bench.{w} Clyde picks up his order and readily shuffles over to him."
            c "\"And for you, sir?\""
            ws "\"Uh, just these and a medium soda.\""
            c "\"Sounds good! Hope you enjoy the movie!\""
            "I can only try."
            jump theatercontinued
        "Talk More With Riley":
            $ Riley = True
            "The sun is blistering, and my dark fur isn't helping me beat the heat."
            "I head toward the theater, hoping that Riley will follow me, but he just stands at the sidewalk; arms crossed.{w} His tail points to the ground and our conversation seems to end in a stalemate."
            "I let out a loud sigh and walk back to him, shielding my eyes from the white sun. I swear I can see the sidewalk cooking with all of the heatwaves."
            ws "\"Can we at least move to the shade so I don't get cooked alive, man?\""
            "I can see Riley's eyes pop out of his skull. It's like he's re-entered reality."
            r "\"Uh, shit. Yeah, let's get you under there.\""

            "The silence drowns us.{w} I figured some of the tension was just from us baking, but neither of us have said a word in five minutes."
            "I wonder if I should just head into the air-conditioned building before a deep sigh blasts into the open."
            r "\"Sorry, I'm just...\""
            "I wait for him to finish before I talk, wanting to let him speak his mind without either of us yelling again."
            r "\"You did find a nice guy, Walt. It's just...{w} It's bad news over there. Something bad is going to happen, I know it.\""
            "I let out an awkward chuckle. I was stupid.{w} Riley raises an eyebrow at me, not realizing my laughter was out of understanding."
            ws "\"If something {i}does{/i} end up happening, you can be the first one to say \'I told you so.\'\""
            "Thankfully, Riley shoots a snicker my way."
            ws "\"If I could afford it, I would bring Asher over here, Riley.{w} Shit's just too expensive now.\""
            r "\"Yeah... Yeah, I know.\""
            "Riley flops back onto his bench and bellows out a loud groan; loud enough that people end up looking at us."
            "He raises his head back to me, struggling to fix his posture as he returns to properly sitting."
            ws "\"Seriously, though. Thanks for worrying about me.\""
            "A rare smile flashes across his face.{w} Maybe things will be fine after all."
            r "\"Dude, you know I wouldn't be a good friend if I didn't.\""
            "I put my hand across my chest and clear my throat."
            ws "\"I solemnly swear to do the same, Sir Deckard.\""
            "The otter raises an eyebrow and crosses his arm.{w} I lower my hand and stand up, brushing leaves and pollen off my shorts."
            ws "\"Let's head inside.\""
            r "\"I'll never let you live that down, you know.\""
            "I try to bury the memory and step inside the theater, nearly panting at the relief from the air conditioning."
            "Clyde is sitting on the indoor bench with his order, and Riley and I hurriedly go to the snacks so we don't miss the previews."
            jump theatercontinued
            
label theatercontinued:
    "We struggle to make it past the crowded row of people as we try to get to our seats."

    if Clyde == True:
        "Riley eventually sits down on the left seat, with Clyde following suit in the middle."
        "I end up whacking Clyde in the face with my tail as I seat myself, accidentally brushing it against his bucket of popcorn."
        ws "\"Sorry, sorry...\""
        "Clyde waves his hand in acknowledgement, while Riley silences his cell phone."
    elif Riley == True:
        "Clyde moves himself to the furthest seat we got, and I seat myself in the middle."
        "Riley accidentally bats his tail against my nose as he sits down, and I almost drop my half-opened bag of candy."
        r "\"Shit, sorry about that.\""
        "I wave my hand at Riley, laughing a bit even though my nose stings a little."
        "Who knew otter tails were so... forceful?"
        "Clyde is already digging into his popcorn, and it's only now I remember to silence my cell phone."

    "It seems like we made it just in time, as the lights dim around us.{w} The screen turns bright as the trailers begin to play."
    "I want to pay attention, but everything from today has got my head spinning.{w} I know I'll see Clyde and Riley again someday, but..."
    "I wish things could have ended here a bit better."

    "It's that feeling again. I can feel the nails tapping and crawling across the side of my neck."
    "I'm frozen, as stiff as a statue.{w} I look over next to me, hoping to see Clyde next to me."
    "The seat that had once been occupied by the binturong is now empty."
    "One by one, everyone in the theater starts to vanish."
    "The previews turn to static once again, before that photo shows."
    "It's me, wearily sitting at a graveyard.{w} I look disheveled, like I haven't eaten or showered in weeks."
    "I don't know why I'm there or who's buried in front of me, but just looking at the screen makes me feel depressed and nauseous."
    "The gaunt claw is now curled around my neck, squeezing it tight as I try to move any part of my body."
    "Even my fingers are locked in place, and I can feel my consciousness start to fade as the air escapes me."
    cr "\"This is just a glimpse of your future, young wolf.\""
    "I ignore the creature, trying to return to the last day I have here."
    "Fuck, why is this shit happening again?!{w} I try to throw myself out of my seat, hoping that if I do everything will go back to normal."
    "Instead, I feel myself sinking...{w} and sinking...{w} and sink-{nw}"
    jump wakingup

label wakingup:
    "I let out a loud yelp as my head hits the floor of our bedroom.{w} That's right. It's been months since that day."
    "I groggily sit myself up, rubbing the back of my head which is aching like hell."
    "I turn to see if I woke up Asher...{w} but he isn't in our bed again."
    "I suppose I should have been used to this by now, but it feels strange to live with my boyfriend and never see him next to me when I wake up."
    "I almost fall back down as I prop myself onto the bed, finally realizing how wet my fur is.{w} The fall air sneaking in through the window gives me chills."
    "With that, I stand up and head to the hallway."

    "It's hard to see through the dark apartment, even with my eyes adjusting to the little light there is."
    "Nevertheless, my paw manages to stroke itself from the bumpy wall to the hallway closet.{w} I pull out a towel, at least I think it's a towel, and wipe the sweat off of my body."
    "As I close the door, I nearly jump from what I see in the mirror."
    ws "\"WHO'S-\""
    "I immediately stop as I realize who it is."
    "The dim glow from the dying kitchen light bathes Asher, asleep on the counter where we first talked to each other."
    "His laptop next to his shoulder is dark, asleep like him, and I can see two bottles next to his other arm."
    "One is an orange bottle I remember getting a month ago. The label on it says \'Benazepril.\'{w} I guess he forgot to take his night dosage again and decided to do some work while it kicked in."
    "The other bottle is white, obviously a generic store brand. I pick it up, it's label facing Asher."
    "My brow furrows as I read it, and I let out a deep sigh."
    ws "\"Asher, you can't take this...\""
    "His headaches have been getting worse, but that still doesn't mean he can take Ibuprofen."
    "I wish the doctors would just figure out what's wrong already. We've gotten \"high blood pressure\" but it feels like more than that."
    "I can't help but feel like the Benazepril isn't helping either.{w} Even walks are hard for Asher now."
    "..."
    "I feel helpless."

    menu:
        "Cover Him Up":
            "With how cold I am, I can't imagine how cold Asher feels."
            "Digging through his fur, I can feel the goosebumps on his skin, and I wonder how he's still able to sleep like that."
            "I hurry back to our room and grab the blanket we share, covering him up.{w} He lets out a small moan as I do so, probably adjusting to the weight and temperature."
            "I would wake him up, but... he needs all the sleep he can get."
            "Not wanting to sleep alone again, I go to our couch.{w} It's not nearly as comfortable as our bed, but I'd rather be next to him than alone in a cold, dark room."
            "I stare at the ceiling, hoping we'll be able to go out to breakfast tomorrow, and finally drift back into a deep sleep."
    jump leavingapartment

label leavingapartment:
    ws "\"Babe, are you ready?\""
    "I shout across the hall as I look into the mirror. My clothes look fine but the rest of me... looks like shit."
    "Even after a shower, there's horrendous bags under my eyes, which are bloodshot.{w} I need more goddamn sleep."
    "I hear a loud gulp as Asher takes his morning dose of benazepril, finishing his tea after doing so."
    "It's not nearly as cold as it was last night, but I made sure to put on some sweatpants and I have an old jacket wrapped around my waist in case I need it."
    "Asher, however, is decked out in full winter gear.{w} He's wearing the winter coat I brought when I moved, as well as an old scarf we found at a thrift store."
    "Even under that, he has on a sweatshirt. The cold must really be getting to him."
    "The wolf unexpectedly gives me a deep kiss as I turn to him, and I can feel my cheeks heating up."
    "The taste of peppermint tea enters my mouth as he goes deep in there, mixing it with the cinnamon from my toothpaste."
    "I want to grab him and pull him in more, maybe even skip our breakfast, but he pulls away, smiling like the goofy dork he is."
    ac "\"Ready!\""
    "He lets out a dumb giggle, which I can't help but join in with.{w} I playfully give him a light slap on the ass and he jumps in surprise, a squeaky yelp echoing in the hallway."
    ac "\"Ah-h-hey!\""
    "Now his cheeks are red, and he scurries out towards the door. I can't tell if it's out of embarrassment or if he just wants to hide his laughter from me."
    "Either way, I'm happy he's here with me."

    "It's once we're out the door I realize why he kissed me like that. Two teenagers at the bottom of the stairs are handing out fliers."
    "Asher's face has turned from mischievous lust to a dour expression. His eyes look vacant, darker than usual, and his smile has turned into a frown."
    "As much as I want to hold my boyfriend's hand, we both shove them in our pockets."
    "Moving to Silverstone from Birkenfeld was a culture shock.{w} While there had been plenty of homophobes in Birkenfeld it felt like Silverstone was still living in the past."
    "It wasn't uncommon for us to be called \"faggots\" just for being near each other."
    "I go ahead of Asher, politely declining the folders the two are handing out, hoping that the distance we create is even for us to be safe."
    "Nothing happens, but I try to keep my eye on Asher and hope they won't bombard him with the handouts."
    "Thankfully, we make it to the car, both of us letting out a sigh of relief as the boys divert their attention to a poor old woman just trying to get to her apartment."
    "I turn on the ignition and pull out of the carport, hoping we can have our date in peace."

    jump breakfast

label breakfast:
    "The restaurant is more crowded than usual. I can't help but feel like something doesn't want the two of us to have some peace and quiet."
    "The couple next to us is vomiting out the words they heard on the news, none of them pleasant to process."
    "Asher seems incredibly out of it, just poking his scrambled eggs as the echoes of silverware ring throughout the restaurant.{w} This was unfortunately not unusual for him."
    "My eyes are heavy from last night, and I struggle to lift the mug of coffee I ordered.{w} Anyone could tell that it's cheap, and the bitter tones outweigh the acidic components."
    "My boyfriend seems to notice my weariness; his own eyes lighting up a bit."
    ac "\"You alright, dude?{w} You look kind of out of it.\""
    "It takes all of my strength not to snicker at Asher saying \'dude.\'{w} Just hearing the surfer slang coming from him is so unnatural."
    ws "\"I guess I am... I just had another nightmare last night is all.\""
    ac "\"Oh...\""
    "Asher looks down, taking a bite of a sausage link. He doesn't wait to finish chewing before continuing."
    ac "\"Did you talk with your therapist about them?\""
    ws "\"A while ago, yeah. She just said it was because I was getting used to a new place or something.\""
    ac "\"Maybe you should make another appointment?\""
    "I don't really know how to respond.{w} Asher is right, but the closest hospital is an hour out of Silverstone. It bleeds me dry just to get there."
    "There's an awkward silence for a bit, both of us waiting for the other to speak. The irritating chatter from next door eventually comes back, but that's just worse."
    "Asher lets out a deep sigh, and his chair lets out a loud screech as he gets up.{w} The noise is anxiety-inducing, and I hope no one sees us together."
    ac "\"I'm gonna head to the restroom real quick, okay.\""
    "He's giving me a cheery smile, but he looks sickly as all hell.{w} I want to go with and help, but..."
    ws "\"Okay, text me if you need anything.\""
    "I keep my tone hushed, praying that the two next to us aren't eavesdropping."
    "I hate this. I just want to hold hands with him, hug him, and kiss him like any \'normal\' couple can."
    "He wobbles to the restroom, giving me a half-hearted wave. His tail drags across the floor, and it's only now that the others in the restaurant notice him."
    bf "\"Holy shit, is he okay?{w} He didn't look too hot.\""
    gf "\"I don't know. It's not really our business, though, is it?\""
    bf "\"I... I guess you're right...\""
    "I want to scream."
    "I nearly jump out of my seat, flinging a bite of hash browns in the air, as I feel my phone vibrate in my pocket."
    "Once I regain my composure, I pull it out."

    if Clyde == True:
        "I double-take when I see who it is.{w} Clyde and I had talked since I moved, sure, but only over text."
        "Getting a call from him so soon after that nightmare feels fucking eerie."
        cl "\"Yo, took you long enough!\""
        "I can tell Clyde hasn't smoked yet today. For good reason, too."
        ws "\"How's the new job, man?\""
        cl "\"We'll see. I just pulled up to the office.{w} This suit fucking sucks, man.\""
        "Imagining Clyde in a suit with a combover almost kills me, but I'm too exhausted to laugh right now."
        cl "\"Just wanted to check up on you and Asher since this job will probably start eating my time up.\""
        ws "\"We're doing alright. Out on a breakfast date right now.\""
        cl "\"Oh shit, put it on speaker so I can talk to ya both!\""
        ws "\"He's not at the table right now, actually. He went to the restroom.\""
        cl "\"Ah.{w} Is everything okay with him... ya know...?\""
        "I let out a sigh, trying to point the phone away from me as I do so.{w} It's great that Clyde cares about Asher's health, but the both of us are so tired of the constant reminders."
        ws "\"I did find him asleep on the island last night. Other than that, we're just waiting to hear from the doctors about his next appointment.\""
        cl "\"You okay, man? You don't sound too hot, either.\""
        ws "\"I-I'm good, just... ya know... More nightmares...\""
        "I say it hushed, hoping it slips through the traffic I hear from Clyde's end. It doesn't escape him."
        cl "\"Dude, neither of you are doing well. I think Riley might have been right.\""
        ws "\"Clyde, I don't-\""
        cl "\"Just... think about the two of you moving back to Birkenfeld if things don't get better.{w} I'll even pitch in for rent and everything.\""
        "Just as Clyde says that, Asher returns to the table. I didn't want us to have this talk during breakfast."
        ws "\"Listen, I gotta go. I'll text you later?\""
        cl "\"Uh... Yeah, sure.{w} Seriously, though. Think about it, man.\""
        "Before I can respond, the phone hangs up. My only guess is that he was about to get to his desk anyway, but it was unusual for Clyde not to give a cheerful goodbye."
    if Riley == True:
        "I double-take when I see who it is.{w} Riley and I had talked since I moved, sure, but only over text."
        "Getting a call from him so soon after that nightmare feels fucking eerie."
        r "\"Hey, what's up, dude?!\""
        "From the sound of running water, I'm guessing he just finished working out."
        ws "\"How's the new workout routine?\""
        r "\"It's fucking killing me, man.{w} Barely been on it a week and my muscles ache like hell.\""
        "Imagining Riley just sitting limp in a chair with heat compresses almost kills me, but I'm too exhausted to laugh right now."
        r "\"Just wanted to see how you and Asher were doing before my next deep dive into the paranormal.\""
        ws "\"We're doing alright. Out on a breakfast date right now.\""
        r "\"Oh hey, you should put it on speaker, then!\""
        ws "\"He's not at the table right now, actually. He went to the restroom.\""
        r "\"Ah, alright.{w} Is everything okay with him... health-wise?\""
        "I let out a sigh, trying to point the phone away from me as I do so.{w} It's great that Riley cares about Asher's health, but the both of us are so tired of the constant reminders."
        ws "\"I did find him asleep on the island last night. Other than that, we're just waiting to hear from the doctors about his next appointment.\""
        r "\"And what about you, man? You sound pretty tired.\""
        ws "\"I-I'm good, just... ya know... More nightmares...\""
        "I say it hushed, hoping it slips through the locker slams I hear from Riley's end. It doesn't escape him."
        r "\"Dude, this isn't an \'I told you so,\' but I don't know if you'll get the best care in Silverstone. There's not even a therapist there.\""
        ws "\"Riley, I don't-\""
        r "\"Just... think about moving back here to Birkenfeld if things don't get better.{w} I'll help with finding doctors and all that shit.\""
        "Just as Riley says that, Asher returns to the table. I didn't want us to have this talk during breakfast."
        ws "\"Listen, I gotta go. I'll text you later?\""
        r "\"Uh... Yeah, okay.{w} Seriously, though. I care about you guys, man.\""
        "Before I can respond, the phone hangs up. My only guess is that he was about to get into the showers, but it was unusual for Riley not to give a snarky goodbye."

    ac "\"Who were you talking to?\""
    "Asher takes a bite of his oatmeal as he asks, a blueberry falling back into the bowl. He looks strangely chipper, which catches me off-guard."

    ws "\"Oh, Clyde called me. His job starts today.\""
    ws "\"Oh, Riley called me. Sounds like he's gonna do more research soon.\""

    ac "\"Oh, you should have put him on speaker! I would have loved to talk to him.\""
    "My eyes narrow and drift towards my boyfriend's jacket pocket. A suspicious lump protrudes from the side."
    ws "\"You seem a bit better.\""
    ac "\"Hmm?!\""
    ac "\"Oh, it was nothing. I had a headache, so I splashed some water on my face is all...\""
    "I want to believe him, but..."

    menu:
        "Question Him":
            ws "\"I can see the bottle in your jacket, Asher.\""
            "There's a brief pause between the two of us, as if the others in the restaurant are gone."
            "A wave of guilt washes over Asher's face. He sighs, before reaching into the pocket and handing me the ibuprofen."
            ws "\"Asher, please...{w} You {i}know{\i} this messes with the Benazepril...\""
            ac "\"I know... That's why I didn't take any in there.\""
            "Now I'm just confused."
            ac "\"I know you found the bottle last night since I did take some then. My head really fucking hurts, but...\""
            ac "\"I know you just want to see me get better. I swear I just splashed some water on my face.\""
            "He guides my hand to his fur. Sure enough, his face is wet."
            "He lets me go and the world resumes, my boyfriend returning to his breakfast."
            "Now the guilt hits me. I can't help but stare at the bottle of pills I took."
            "Without thinking, my hand grabs the bottle and slides it over to him."
            ws "\"I'm sorry... I just don't want you to hurt anymore.\""
            "Asher, almost in confusion, picks up the bottle before returning it to his pocket."
            "One of his hands slides under the table, and I can feel his claws poking through my jeans a little."
            "The squeeze he gives is comforting, but I don't think I deserve it."
            ac "\"We'll get through it, Walt.\""
            "He gives me a quick, tight squeeze, as if to mimic a kiss. I smile as much as I can at him, but the guilt still lingers."
            "I take a forkful of hash browns, and we eat the rest of our meal in silence."

            jump afternoonex
        "Don't Bring It Up":
            "As much as I want to bring up the meds that I suspect are in the pocket, it's been rough for both of us."
            "I pray it's just my paranoia kicking in, and I look up at him."
            "Now that I get a good look, some areas of his fur are a bit darker than the rest. Like he had messily took a cup of water and flung it on himself."
            "I guess I was staring for a while, since I feel Asher's hand grab my thigh."
            "He gives it a small, playful squeeze, like he's giving me a peck on the snout."
            ac "\"Whatcha lookin' at over there?\""
            "I clear my throat, putting my own hand on Asher's, caressing it as much as I can before the waiter comes back to us."
            ws "\"Just tired. Thought I saw a fly buzzing around.\""
            "Asher gives a small grin, before returning to his breakfast.{w} Another blueberry falls from his spoon to the bowl of oatmeal and I can't help but chuckle a bit."
            "We pull our hands away, but I swear I'll give his man a huge kiss when we get home."
            "I take a forkful of hash browns, and we eat the rest of our meal in silence."

            jump afternoonex

label afternoonex:
    scene bg counter with dissolvelong
    "My eyes burn as I continue to stare at my laptop screen.{w} I've been staring at this photo editing software all afternoon."
    "I'm on my third cup of coffee by now, but I can barely feel the buzz from the caffeine."
    "Asher is behind me on the couch with a blanket draped over him as he snores away."
    "He practically passed out when we got back, his headache being too much for him by the time we arrived."
    "I'm trying my best to focus, but my eyesight is getting blurry, and Asher's snores only make me want to join in."
    ws "\"Fuck this stupid deadline.\""
    "I continue to adjust the color balance of the photo, going back and forth as I try to make things out."
    "My attention drifts, however, as I see what's next to me."
    "It's the medical bills we were looking at last night.{w} The memory of the outrageous costs angers me."
    "Thousands of dollars just to be told it's high blood pressure when it's clearly not."
    "I sent out so many e-mails to people asking for photo work, hoping to hear a response.{w} I asked forums about Asher's symptoms, but no one's given an answer."
    "It hasn't even been 24 hours, but the anticipation is killing me.{w} I want him to get better."
    "Suddenly, I feel a hand on my shoulder. There's need to question who it is."
    "Asher slips under my arm, swinging his leg over mine. He sits on top of me, nuzzling his nose into my neck as he holds me tightly."
    ws "\"You still sleepy?\""
    ac "\"Mmm.\""
    "I cuddle into my boyfriend's cheek as he gives a slight nod into me. His grasp weakens a bit as his tail wags a bit, batting the other chairs and the island behind him."
    ws "\"You want me to take you to the bedroom?\""
    ac "\"Mm-mmm.\""
    "This time he shakes his head, and his tail droops a little. He tightens his grip, and my attention is fully taken away from the laptop."
    "I wrap my own arms around him, caressing his back. His fur is soft, and he smells of wood from the cologne he put on earlier."
    "I bury my nose into his neck and give a light kiss. He responds by burying deeper into my own neck, and his grip turns from hugging to clutching onto me.."
    ws "\"Hey, what's up?\""
    ac "\"Nothing, I'm just... I'm tired and want to cuddle you.\""

    scene cg cuddle with dissolvelong
    "A silence lingers for a bit before he moves his head a little, his snout resting on my shoulder."
    ac "\"Everything will be okay, Walt.\""
    ws "\"I... I know, I just don't want you to feel like this anymore...\""
    ac "\"I mean, I'll probably still be tired as hell when I do get better.\""
    "He lets out a nervous chuckle, which calms when I don't respond."
    ac "\"As long as you're with me, I'm happy.\""
    "I try not to cry, but the stress and emotions finally get to me. My grip tightens to the point where I'm worried that I'll break his spine in two."
    "He gently kisses me. Once, then twice, and then three times.{w} The tears flow out of my fur and into his, but neither of us mind."
    "We're together and that's what matters in the end...{w} That's all that matters..."
    scene bg counter with dissolvelong
    "It's then that I finally seeing the monster haunting my dreams in the reflection of my empty laptop screen."
    "His claw is about to reach for me once again, and I already feel my body start to stiffen."
    "I see my boyfriend's body begin to fade as the claw gets closer to my neck."
    "There's only one word that comes to mind."

    menu:
        "Don't.":
            "As if the creature has learned some empathy, I see him walk away from the two of us. My body returns to normal."
            "Asher pulls away from me, his body once again fully there. He doesn't seem to notice the monster, and I can't help but wonder if it's by own mind or not."
            ac "\"Want to order some Chinese tonight?\""
            "I know what happens this night, but if it means some more time with him, I'll play along with this cursed town."
            ws "\"Sure. Can you get me the number?\""
            "I know I have to wake up and let go eventually, but for now, I want to hold onto him for just a bit longer."
            "Once it's morning, though, I promise to order the same thing we did that night."
            "One year without him. One year without letting go. One year trapped in this hellhole."
            "There's nothing I want more right now than to be with him."
            "The apartment brightens as my boyfriends smiles at me, the windows bathing us in white."
            "It's time to wake up."

    $ EndingExtra = True
    $ quick_menu = False
    window hide
    pause 3.0

    jump credits