label morning2:
    if romance_points >= 1:
        show walt smiling at show_fade
        w "\"Oh, yeah, I'm from Birkenfeld!\""
    elif romance_points <= -1:
        show walt neutraltalking at show_fade
        w "\"Yeah, I'm from out of town.\""

        show walt neutral2
        "I can sense the irritation coming from Walt, even if he isn't trying to be outwardly upset."

        "It feels off-putting considering how friendly and outgoing he was just five minutes ago."

        a hangoverraisedtalking "\"Uh... from where?\""

        show walt lookingdownside
        "I don't mean to sound like a dick, but even I can hear the pitch and volume rise as I finish my sentence."

        "It does seem to snap Walt out of his funk, though, even if it's just a bit."

        w smilingside "\"Uh, my bad.{w} I'm from Birkenfeld.\""

    a hangovercurious "\"Wait, Birkenfeld?{w}{nw}{done}"

    a hangoverneutral "\"Wait, Birkenfeld?{fast} No offense, but why would you vacation here? It's only an hour by car.\""

    show walt grinningclosedside
    "Despite being a genuine question, Walt seems to find some humor in it."

    if romance_points >= 1:
        "I can't really figure out why, but I at least get to hear his laugh for the first time."

        "Although I expected it, his laugh is full and deep, easily echoing across the apartment.{w} It's cute, if I'm being honest with myself."
    elif romance_points <= -1:
        "His laugh at least lets me know he's back down to a jovial level."

        "It's expectedly full and deep, easily echoing across the apartment.{w} It's cute, but I hope it doesn't bother the neighbors."

    w smiling "\"Eh, it was actually my friends' idea.{w} They're huge urban legend nerds.\""

    "\'Well, they came to the right place if they chose Silverstone,\' I keep to myself, not wanting to sound like a sarcastic asshole."

    "Then it strikes me."

    a hangoversurprised "\"Wait, you came here with friends?!\""

    a hangoversurprised "\"Aren't they worried about you?!\""

    w grinningclosedside "\"I doubt it, to be honest!\""

    "The wolf lets out some laughs in between his words, as if he doesn't understand the gravity of the situation."

    w smilingside "\"I separated from them pretty early on.{w}{nw}{done}"

    w smiling "\"I separated from them pretty early on.{fast} As interesting as ghost stories are, it's not really my thing.\""

    "One of the few people who doesn't come to Silverstone because of those trashy paranormal shows on TV?"

    a hangoverneutral "\"So, why did you come here, then?\""

    w neutraltalkingside2 "\"I'm actually a photographer. I figured there would be some nice shots of the beach here.\""

    w neutraltalkingside "\"Unfortunately, the weather was overcast yesterday—\""

    a hangoverupsetclosed "\"And now we're stuck in a spontaneous snowstorm...\""

    w grinningclosedside "\"Unfortunately!\""

    "Despite the situation, Walt seems to be taking everything in stride.{w} I wish I had his energy, because I'm really not looking forward to being stuck in the house all day."

    "It's normally pretty warm in Silverstone, even in lower temperatures. I ended up throwing my jacket away because it was just collecting dust in my closet."

    stop music fadeout 1.0
    window hide
    pause 1.0
    show walt staringsideneutral
    play sound "PhoneVibrate1.ogg"
    window auto

    "All of a sudden, I hear a buzz in my bedroom."

    a hangoverraisedtalking2 "\"Sorry, I'll be right back.\""

    if romance_points >= 1:
        w smilingside "\"It's no worry, take your time!\""

        "Damn, this wolf is easy to please. I feel a bit guilty for just leaving him, but he seems content with his meal, at least."
    elif romance_points <= -1:
        w lookingdownside "\"Mm.\""

        "Walt just turns back to his meal, and I feel a bit of guilt in my stomach since I thought things had been patched up by now."

    "I scamper back to my room and pull my phone out from under the covers, quickly returning to Walt."

    "I almost fall out of my chair as I sit down, but Walt catches me by grabbing my shoulder. His grip is firm, but comforting. Maybe that feeling is just from my quick panic, though."

    w grinningclosedside "\"Damn, you run marathons or something?\""

    "His laugh booms once again;{w}{nw}{done}"
    
    play sound "PhoneVibrate2.ogg"
    "His laugh booms once again;{fast} my phone's vibration joining in with the cacophony of chaos."

    window hide
    show phone at offscreenbottom
    show phone at truecenter with MoveTransition(0.2)
    pause 1.0
    window auto

    "{sc=3}I was kidding when I said I'd be stuck inside all day!!{/sc}"

    show phone at offscreenbottom with MoveTransition(0.2)
    show walt neutralside
    "Walt already can read the frustration running across my face; his own plastered with curiosity."

    w neutraltalking "\"Is something up?\""

    "Damn it, how do I break the news to him...?"

    menu:
        "I Hate To Break It To You...":
            $ romance_points += 1
            a hangoverupsetclosed "\"Uh, so...{w}{nw}{done}"

            show walt staringneutral
            a hangoverpondering "\"Uh, so...{fast} I hate to break it to you, but the weather is going to be really bad for the rest of the day...\""

            a hangoverclosed "\"You're probably going to have to stay here for a little bit...\""

            show walt smiling
            "I expect to see Walt upset, but to my surprise, he's actually smiling."

            w smilingside "\"Is that all?\""

            a hangoverraisedtalking2 "\"Huh?\""

            play music "The Morning After.ogg" loop fadein 1.0
            w grinningclosedside "\"I mean, you already said that it's too long of a walk to that diner, right?\""

            a hangoversquinting "\"Uh...{w} I guess I did?\""

            "I can't help but feel suspicious. Walt is accepting this a bit {i}too{/i} quickly."

            "I mean, I'm not upset he's staying. Something just feels... a bit off."

            w smilingside "\"Seriously, it isn't an issue. I have an extra pair of clothes in my backpack and some homework to do.\""

            w grinningclosedside "\"Better here than a freezing diner, in my opinion!\""

            a hangoverraisedtalking2 "\"...\""

            a hangoversquinting "\"Who brings a backpack with homework to a club?\""

            w staringtalkingneutral "\"GUH!\""

            w staringsidesmiling "\"This doofus...?\""

            play sound "Silverware.ogg"
            "I snort at his reply before returning to finishing my breakfast, which has been sitting on the island for about five minutes due to our conversation."
            stop music fadeout 1.0
        "You're Gonna Have To Stay Here":
            $ romance_points -= 1
            show walt staringneutral
            a hangoverpondering "\"Yeah, so you're going to have to stay here.\""

            "I don't notice Walt's expression as I check through my phone; his face masked with both puzzlement and worry."

            w angrysidetalking "\"Uuuuuh, want to elaborate on that?\""

            show walt angryside
            "I finally look up from my phone. The anger on Walt's face is intense, even if it doesn't fit him."

            "Then again, I suppose I did just dump that and leave him in the dark."

            a hangoverraisedtalking "\"Oh, the forecast said it's going to be freezing for the rest of the day.\""

            "Walt only looks more irritated at the explanation.{w} It's not my fault that the weather is such bullshit, though."

            w angrysidetalking "\"It's fine. I have some spare clothes and homework to do in my backpack.\""

            show walt angryside
            a hangoverneutral "\"You brought a backpack to the club?\""

            play sound "Silverware.ogg"
            "Walt doesn't answer, instead picking at his breakfast. Eventually I join him in that, my hunger dissipating from the awkward air pressing down on me."

            show walt angrysideclosed
            "Eventually I hear a deep sigh, Walt's irritation swimming out of him as we return to our conversation, albeit hesitantly."

    if romance_points >= 0:
        w smilingside "\"Hey, uh... this might be an awkward question...{w}{nw}{done}"

        w grinningclosedside "\"Hey, uh... this might be an awkward question...{fast} Did we do it last night?"

        play sound "Slam.ogg"
        show walt staringscared
        with vpunch
        "I nearly spit my fucking food out, before accidentally inhaling it and choking."

        w staringtalkingneutral "\"SHIT! Sorry, sorry!!\""

        "I can tell from the trembling in his voice he's remorseful, but it wasn't really his fault."

        "I wave my hand in acknowledgement before successfully getting my breakfast down my throat."

        a hangoversurprised "\"You're fine, you're fine!\""

        "My voice is a bit raspy, so I go to the kitchen to get some fresh water."
    elif romance_points <= -1:
        w lookingdownside "\"Hey, uh... this might be an awkward question...{w}{nw}{done}"

        w neutraltalkingside "\"Hey, uh... this might be an awkward question...{fast} Did we do it last night?"

        play sound "Slam.ogg"
        show walt staringsideneutral
        with vpunch
        "I nearly spit my fucking food out, before accidentally inhaling it and choking."

        "I can see Walt's eyes widen as I try to dislodge the food, clearly not expecting this scenario."

        "Eventually I hack it out onto the counter; drawing in deep breathes as I try to catch my air."

        a hangoversurprised "{sc=3}\"Jesus!\"{/sc}"

        w staringtalkingneutral "Shit, sorry about that."

        show walt staringneutral
        "I nearly glare at him due to his dismissiveness, but think better of it as I clean up the mess."

        a hangoverpondering "\"It's fine.\""

        "My voice is a bit raspy, so I go to the kitchen to get some fresh water."

    scene bg kitchen
    with dissolve
    play sound "Sink.ogg"

    "To be honest, though, even I'm not sure if we did it last night.{w} There's an empty slot in my memory bank, and it's been doused in alcohol and regret."

    "Still, I don't think I would've minded having sex with Walt. He's handsome, his fur is soft, and—"

    "..."

    "..."

    "..."

    "I need to get my mind out of the gutter."

    "I take a huge gulp of water, and it feels like I've swallowed the arctic. Soon, I can feel everything return to normal."

    w "\"So? What do you think?\""

    "Well, mostly normal.{w} Walt waits patiently for my answer, his tail wagging in anticipation."

    "Lord, fucking help me."

    menu:
        "Yes":
            $ romance_points -= 1
            "Considering both of us are in our underwear right, I wouldn't be surprised if we did have sex."

            "I mean, who sleeps together in the same bed with a stranger in their underwear without doing it?"

            a hangoverraisedtalking2 "\"I'm pretty sure we did have sex.\""

            "My tone involuntarily jumps up at the end of my sentence, as if I was questioning myself."

            "I hope Walt doesn't catch it, but I see his brow furrow."

            w "\"\'You sure about that?\""

            "I almost shrug; just wanting to get out of the conversation at this point.{w} However, I feel the words escape my tongue before I even think of them."

            a hangoverraisedtalking "\"I mean, why else would we be in our briefs?\""

            "Walt seems a little unconvinced, but he lets out a deep sigh."

            w "\"Well, you got me there.\""

            "Now I'm wondering if I was just fucking bad in bed.{w} With that awkward exchange, I return to my spot at the counter."
        "I Don't Know":
            $ romance_points += 1
            "Despite my inner thoughts wanting to have slept with Walt, it'd be scummy to lie and say yes."

            "It'd also be awful to deny it, since there could be potential health risks neither of us know about."

            "I take a deep breath to collect my thoughts before finally answering..."

            a hangoverupsetclosed "\"If I'm being quite honest, Walt, I don't actually know.\""

            a hangoverpondering "\"I really wish I did so that I could give you a concrete answer, but I honestly don't remember anything from last night.\""

            a hangoverupsetclosed "\"Sorry about that...\""

            "Silence hangs in the air for a bit, and it also feels like when you're in the southeast for the summer.{w} Muggy, sticky, and uncomfortable."

            play sound "ChairScraping.ogg"
            "It feels like an eternity, but soon I hear a chair at the counter screech against my floor."

            show walt neutralside at show_fade
            "I'm face-to-face with Walt now. His face isn't happy, but it's not really upset, either."

            show walt smilingside
            "He cracks a bit of a smile, as if he can sense my anxiety about the situation."

            w neutraltalkingside2 "\"Well, I'm not exactly happy that neither of us know...\""

            w neutraltalkingside "\"But I would rather you tell me the truth than lie and said we did do it.\""

            w smiling "\"So thanks for telling that, at least.\""

            show walt grinningclosedside at show_fadeout
            "Finally, the wolf lets out a gigantic grin before returning to his seat.{w} I'm a little baffled, to be honest, but I also feel a wave of relief wash over me."

            "After staring confusedly at the wall for probably too long, I return to my seat next to Walt as well."
        "No":
            $ romance_points -= 1
            "Despite both of us being in our underwear, I don't think that's enough evidence to say we had sex."

            "As well as that, my body doesn't feel very sore and I'm pretty sure my exhaustion is from this goddamn hangover."

            a hangoverneutral "\"I don't think we did.\""

            "My tone involuntarily jumps up at the end of my sentence, as if I was questioning myself."

            "I hope Walt doesn't catch it, but I see his brow furrow."

            w "\"\'You sure about that?\""

            "I almost shrug; just wanting to get out of the conversation at this point.{w} However, I feel the words escape my tongue before I even think of them."

            a hangoverraisedtalking "\"I mean, just being in our underwear isn't really proof, is it?\""

            w "\"Well, I guess, but—\""

            "I raise a paw in front of Walt, wanting to get out of this fucking conversation. I feel a bit bad as I see his ears droop, but I'm not going to last another minute in this hell."

            "Now I'm wondering if the wolf is a bit disappointed by this outcome.{w} With that awkward exchange, I return to my spot at the counter."
    scene bg counter
    show walt neutral2
    play music "The Morning After.ogg" loop fadein 1.0
    with dissolve

    "Both of us seem a bit awkward after that exchange. I feel my ears burning a bright red, and Walt's posture is less relaxed and incredibly stiff."

    "Well, if we're playing \'20 Questions,\' I suppose it's my turn."

    a hangoverpondering "\"So, uh...{w}{nw}{done}"

    show walt staringneutral
    a hangovercurious "\"So, uh...{fast} You're a photographer?\""

    if romance_points >= 2:
        w grinningclosedside "\"Well, uh... I'm more like a photographer in training?\""

        w smiling "\"I'm going to college for journalism, technically, but I fell in love with the school's darkroom.\""

        w smilingside "\"Next thing I knew, I'd spent thousands on camera equipment, film, editing software...\""

        w neutraltalkingside2 "\"Uh, sorry. I suppose you get the idea by now.\""

        "If I'm being honest, seeing Walt gush about his love for photography is adorable. It's always brightens my day to see people talk about their hobbies unfiltered like that."

        a hangoversmiling "\"Do you have any pictures I could look at?\""

        show walt staringsideneutral
        "Walt's face goes wide-eyed, with a touch of pink peeking through the fur on his cheeks. It's almost at if he's embarrassed by his profession."

        w neutraltalkingside2 "\"I mean, I do, but...{w}{nw}{done}"

        w angrysideclosed "\"I mean, I do, but...{fast} they aren't very good.\""

        a hangoversly "\"Aaaaah, c'mon! I'm sure they're fine!\""

        show walt lookingdownside
        "Maybe fine was a bad word to use.{w}{nw}{done}"

        show walt neutral2
        play sound "TouchScreen.ogg"

        "Maybe fine was a bad word to use.{fast} Nevertheless, he pulls out his phone and shows me his social media."

        a hangoversurprised "\"Wait, you took these?!\""

        w angrysidetalking "\"Yeah, I know they're amateur...\""

        "Before I can even give my opinion, Walt's already accepted defeat. Who's been putting him down?"

        a hangoverraisedtalking2 "\"Dude, these are awesome! You should sell prints of these.\""

        show walt grinningclosedside
        "Walt snickers, even though my suggestion is serious. He plucks his phone out of my hands and finishes his meal."

        w smiling "\"Thanks, but I don't really have the audience for that—\""

        a hangoversly "\"Yet.\""

        w grinningclosedside "\"Sure. \'Yet.\'\""
        
        show walt smiling
        "Walt wipes his face with a paper towel before standing up and shaking his fur. I don't see anything fly out, so maybe he's just pumped up?"

        w smilingside "I'm going to go change and start on some homework. Does you have a shower I can use?"

        "I point to the hallway where my bathroom is and Walt disappears into my bedroom, clutching his backpack as he races to shower."

        show walt smilingside at offscreenleft with MoveTransition(0.2)
    elif romance_points < 2 and romance_points > -2:
        w smilingside "\"I dabble a bit.\""

        a hangoverneutral "\"...A bit?\""

        show walt grinningclosedside
        "Walt lets out another of those booming laughs, though he muffles it a bit. It's as if he's realized how loud his laughs actually are."

        w smiling "\"Okay, maybe {i}more{/i} than a bit.\""

        "Walt pulls out his phone before handing it to me. It looks like one of his social media profiles."

        "A lot of the pictures are landscapes; some from risky places and some in the most mundane places possible."

        a hangoverponderingopen "Hey, these are actually pretty good."

        show walt neutraltalkingside2
        "Walt actually looks a bit embarrassed, as if he hadn't expected the compliment. His mouth hangs open, as if he's trying to find the words to say."

        w smilingside "\"Eh, you don't have to be so nice about it. I know I'm an amateur at it.\""

        show walt lookingdownside
        "Before I can respond, Walt snatches his phone out of my hand. I notice the sadness in his expression he does so, almost as if he didn't mean to reject the compliment and it only came out of instinct."

        w smiling "\"Hey, do you have a shower I can use? I wanna change and get started on my homework.\""

        "I point to the hallway where my bathroom is and Walt disappears into my bedroom, clutching his backpack as he races to shower."

        show walt lookingdownside at offscreenleft with MoveTransition(0.2)
    elif romance_points <= -2:
        w lookingdownside "\"Mhmm...\""

        "Despite him talking about it earlier, Walt doesn't seem to have any interest in talking about it."

        "A few seconds go by, filled with silence that's occasionally interrupted by slurps from Walt finishing his breakfast."

        show walt neutralside
        "Eventually I let out a loud cough, finally bringing the wolf's attention back to me."

        a hangoverneutral "\"Can I see some of your photos?\""

        show walt angryside
        "Walt lets out a deep sigh; it's warmth brushing against my fur as he ponders what to do."

        w neutraltalkingside2 "\"Maybe later.\""

        show walt lookingdownside
        "I'm just gonna guess that's a big fat \'no.\'{w} Whatever, I'll stalk his social media later...{w} if I can find it."

        w neutraltalkingside2 "\"Do you have a shower, actually? I kind of what to change and get started on my homework.\""

        "I point to the hallway where my bathroom is and Walt disappears into my bedroom, clutching his backpack as he races to shower."

        show walt angrysideclosed at offscreenleft with MoveTransition(0.2)
    play sound "DoorClose.ogg"
    "As soon as I hear the door close, I sniff my own fur, uselessly praying that the smell of alcohol has dispelled."

    "My effort is futile as I'm welcomed by the smell of vodka. I nearly gag as it enters my nose.{w} Christ, is this what Walt has been smelling for the past half hour?!"

    "Well, until Walt is done hogging my bathroom, I suppose all I can do is eat and relax by the TV."

    "I wonder what shows Walt likes..."

    stop music fadeout 1.0
    "..."

    "Why am I thinking that? I just met him."

    if romance_points >= 2:
        "Still, I do feel... some sort of security around him? Like some kind of warmth; like a blanket your mom wrapped around you after a nightmare."
    elif romance_points < 2 and romance_points > -2:
        "There is some sort of security around him, though. I can't quite describe it, but I feel safe around him."
    elif romance_points <= -2:
        "I sense some security around him despite our first impressions... Or is it danger?"

    "...{w}{nw}"

    "...{fast}What the hell happened last night?"

    scene bg black
    with fadehold
    play sound "Shower.ogg"
    show afternoonanimation at show_fade
    pause 5.0
    show afternoonanimation at show_fadeout

    play sound "DoorOpen.ogg"
    jump afternoon1
