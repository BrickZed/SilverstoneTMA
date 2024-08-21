label afternoon1:
    play sound "DoorClose.ogg"
    scene bg hallway
    with fadehold

    "Stepping into the hallway is like exiting a city and walking through the countryside; smog dissipating as you take in the fresh air."

    "This experience has made me glad I live alone, since the consequence of two wolves showering forty minutes each fills my bathroom with the smell of wet dog."

    "I take a quick whiff of my fur. The smell of alcohol is gone, but the musky sour smell envelops over the soap I scrubbbed in."

    "I shudder before looking at the time.{w} 1:35 PM.{w} Still a little under ten hours to go—{nw}"

    $ config.window_hide_transition = None

    window hide
    scene bg black
    play music "CreepyAmbience.ogg" loop
    pause 3.0

    $ config.window_hide_transition = Dissolve(.2)

    "{sc=3}No, no, no.{w} No, FUCK NO.{/sc}"

    window auto show
    
    "{sc=3}Why in the fuck is it so dark? It's 1:30... right?{/sc}"

    "I can feel my body start to stiffen as I stare into an impossible abyss.{w} The sweat rolling down my body feels like ants crawling down my arms."

    "My mouth starts to dry from my muzzle hanging open in fear. How long has it been already?{w} 30 seconds?{w} 1 minute?{w} 5 minutes?"

    "I can do nothing but stand alone in fear."

    "...Alone."

    "That's when I remember. How could I forget already?"

    "I call out, my voice meek and shakey as I send it out into the void."

    a hangoverupsetclosedclothed "{sc=3}\"W... Walt? Are you there?\"{/sc}"

    "I doubt he can hear it. The volume of my voice is too small to be thrown across the entire apartment."

    "I shrink into myself and wait."

    "..."

    "..."

    if romance_points >= 2:
        w "\"Asher, did you say something?\""

        "I suddenly feel like I've been hit by a truck. Both fear and relief wash over me as I hear the wolf's response."

        a hangoverupsetclosedclothed "{sc=3}\"C-could you light s-some candles?\"{/sc}" 
        
        a hangoverupsetclosedclothed"{sc=3}\"They should be o-on the bookshelf.\"{/sc}"

        "I force myself to be a bit louder so Walt can hear my instructions. Everything is overwhelming at this point and I just want it to be over."

        w "\"Yeah, I'll try to find them!\""

        play sound "Footsteps1.ogg"

        "The footsteps are strangely comforting to me. I don't know if it's because I know it's Walt or just because I know I'm not alone."

        "Any normal person would've been freaking the fuck out at that, but right now, anything is a security blanket for me."

        w "\"They're these purple ones, right?\""

        "I nod, half-expecting for Walt to see my response."

        play sound "Lighter.ogg"

        "I guess he does, because before I know it—"
    elif romance_points < 2 and romance_points > -2:
        w "\"Asher, was that you?\""

        "I suddenly feel like I've been hit by a truck. Both fear and relief wash over me as I hear the wolf's response."

        "Despite this, my voice is still trapped; caged behind my fangs as I hear my shuddering breath."

        w "\"Asher?\""

        a hangoverupsetclosedclothed "{sc=3}\"C-could you light s-some candles?\"{/sc}" 
        
        a hangoverupsetclosedclothed"{sc=3}\"They should be o-on the bookshelf.\"{/sc}"

        "I force myself to be a bit louder so Walt can hear my instructions. Everything is overwhelming at this point and I just want it to be over."

        "My breathing gets heavier, but it feels like nothing is going in. My chest feels like it's caving in on itself and my fingers curl inward as I wrap my arms around me."

        "I'm having a fucking panic attack."

        w "\"Hey, are you okay? Asher?\""

        "It feels like I'm continuously falling into a deep hole, and Walt's voice is getting farther from me."

        play sound "Footsteps1.ogg"

        "His footsteps ground me a bit, since they make me realize I'm not alone."

        "But the darkness still surrounds me."

        w "\"They're these purple ones, right?\""

        "I try to nod, but any movement feels like it'll snap my limbs off."

        play sound "Lighter.ogg"

        "Walt seems to find them, however, because before I know it—"
    elif romance_points <= -2:
        "Nothing.{w} Is this fucker serious?"

        "I try again, thinking I just wasn't loud enough."

        a hangoverupsetclosedclothed "{sc=3}\"W—Wal...\"{/sc}"

        "My voice trails off before I can finish what I was going to say. Not like it would have worked; my voice ended up quieter than before."

        "I hear my shuddering breath, and my fur bristles as I stand in the deep trenches of the dark."

        "Everything is overwhelming at this point and I just want it to be over."

        "My breathing gets heavier, but it feels like nothing is going in. My chest feels like it's caving in on itself and my fingers curl inward as I wrap my arms around me."

        "I'm having a fucking panic attack."

        w "\"Did Asher fucking leave?\""

        "Walt doesn't even realize I'm here, kneeling in front of the bathroom door. I realize how truly alone both of us are right now."

        w "\"I'll fucking find the candles myself, then.\""

        "It feels like I'm continuously falling into a deep hole, and Walt's voice is getting farther from me."

        play sound "Footsteps1.ogg"

        "His footsteps bring me back, but I don't feel safe at all. My mind pictures outlandish scenarios that end up with one of us dead."

        "\'It's just the dark,\' I try to tell myself. \'It's playing tricks on you.\'"

        "It doesn't help...{w} The darkness still surrounds me."

        play sound "Lighter.ogg"

        "My ears finally perk up at the sound of a lighter, and before I know it—"

    if romance_points >= 2:
        show bg afternoontv
        stop music
        show walt staringtalkingneutralclothed

        w staringtalkingneutralclothed "\"Asher, are you okay?!\""

        show walt staringsideneutralclothed
        "I look around at my surroundings as Walt addresses me."
    elif romance_points < 2 and romance_points > -2:
        show bg afternoontv
        stop music
        show walt neutraltalkingsideclothed
        
        w neutraltalkingsideclothed "\"Hey, are you alright?\""

        show walt neutralsideclothed
        "I look around at my surroundings as Walt addresses me."
    elif romance_points <= -2:
        show bg afternoontv
        stop music
        show walt angrysidetalkingclothed

        w angrysidetalkingclothed "\"Hey, what are you doing?!\""

        show walt angrysideclothed
        "I look around at my surroundings as Walt addresses me."

    "Somehow I've made it to the living room, the candle's glow illuminating everything a distinct orange."

    "I feel like I'm about to collapse from just the sight of a television, nearly laughing at how stupid I must look."

    "Despite only a few minutes passing, the windows outside show an impossible starry night. It's as if we've been sucked into another plane of space and time."

    "I wonder if it's my fear just amplifying things, but I can't help but stare at the windows."

    if romance_points >= 2:
        w neutraltalkingclothed "\"Asher, you seemed upset. Seriously, are you okay?\""

        show walt neutral2clothed
        "Walt is looking straight at me; his eyes distressed at such a little thing."

        a hangoversurprisedclothed "\"I-I'm fine now, Walt.\""

        w neutraltalkingclothed "\"Are you sure? You look like you're about to throw up.\""

        show walt neutral2clothed

        "I'd be lying if I said he was wrong."
    elif romance_points < 2 and romance_points > -2:
        w neutraltalkingside2clothed "\"Asher, hey. 'You okay?\""

        show walt lookingdownsideclothed
        "Walt's looking towards the ground, away from me. I think he's trying to not make me any more anxious than I already am, but his gaze sure would be reassuring right now."

        show walt neutralsideclothed
        a hangoversurprisedclothed "\"I... I could be better, honestly.{w}{nw}{done}"
        show walt staringsideneutralclothed
        a hangoverupsetclosedclothed "\"I... I could be better, honestly.{fast} I sort of had a panic attack.\""

        w staringscaredclothed "\"Wait. Shit, are you serious?\""

        show walt lookingdownsideclothed
        a hangoverupsetclosedclothed "\"No, I... I think I'll be okay for now.\""

        w neutraltalkingside2clothed "\"Well, tell me if you need anything. Okay?\""

        show walt lookingdownsideclothed
    elif romance_points <= -2:
        w angrysidetalkingclothed "\"Hey, why didn't you say anything?!\""

        "I'm honestly a bit frightened at Walt's response. I would have said something if I could, but..."

        show walt angrysideclothed
        a hangoverupsetclosedclothed "\"Jesus Christ, Walt! I was having a panic attack!\""

        "Silence lingers for a bit. The apartment feels like it's air is being vacuumed into the nothingness of space."

        show walt angrysideclosedclothed
        "Finally, Walt speaks up."

        w angrysidetalkingclothed "\"Well, sorry.\""

        "His tone is disingenuine, as if the apology is a requirement."

        w angrysideclosedclothed "\"It wasn't that dark, though.\""

        show walt angrysideclothed
        a hangoversurprisedclothed "\"I—?! That doesn't matter?!\""

        "The two of us awkwardly stand in the living room for a bit, the tension rising."

    "It's only now I realize that tears have stained my fur."

    "I shudder in embarrassment as Walt watches me. It was just the dark. How am I still so scared of it?"

    if romance_points >= 2:
        w smilingclothed "\"Hey, I'm still studying, but... why don't you hang out with me for a bit?\""

        "My eyes widen at the offer. While I would like to spend some time on my own and just let Walt study, I'm not too comfortable staying by myself in my room."

        a hangoverponderingopenclothed "\"It... it really wouldn't be a bother to you?\""

        show walt grinningclosedsideclothed
        "I scream inside at the formality of that phrasing."

        w smilingsideclothed "\"Really, it's not an issue. I'm just reading for an elective right now.\""

        a hangoverponderingclothed "\"Then...{w}{nw}{done}"
        a hangoversmilingclothed "\"Then... Sure! Why not?\""

        w grinningclosedsideclothed "\"Awesome!\""

        "With that, Walt guides me to the couch."
    elif romance_points < 2 and romance_points > -2:
        w neutraltalkingsideclothed "\"Well, I'm still studying, but you can join me if you want to.\""

        show walt neutralsideclothed
        "My eyes widen at the offer. After escaping from that horror and having a panic attack, I'm not too comfortable staying by myself in my room."

        a hangoverraisedtalking2clothed "\"It... it really wouldn't be a bother to you?\""

        show walt staringsideneutralclothed
        "I scream inside at the formality of that phrasing."

        w neutraltalkingside2clothed "\"No, it's not an issue. I'm kind of just reading right now.\""

        a hangoverponderingclothed "\"Then...{w}{nw}{done}"
        a hangovercuriousclothed "\"Then... Yeah. Sure I'll join you.\""

        w smilingsideclothed "\"Cool.\""

        "Walt heads on over to the couch, with me following close behind."
    elif romance_points <= -2:
        w lookingdownsideclothed "\"I'm still studying. You can join me as long as you aren't too disruptive.\""

        show walt angrysideclosedclothed
        "I don't know what's worse right now. Staying alone in my room with the potential for another panic attack, or staying with someone who treats it like it's a cry for attention.."
        show walt angrysideclothed
        a hangoverponderingopenclothed "\"I don't really wanna bother you—\""

        w angrysidetalkingclothed "\"Dude, just take the offer.\""

        show walt angrysideclosedclothed at offscreenright with MoveTransition(0.2)
        "Walt doesn't even wait for my answer before heading on over to the couch."

        "I'm not too fond of staying with him, but... I suppose it's better than staying in the dark in my room."

        w "\"Are you coming?\""

        "And with that, my feet unwillingly propel me to the couch."

    scene bg couch
    with dissolvelong

    jump afternoon2