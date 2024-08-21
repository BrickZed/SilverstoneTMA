label screamending:
    "For a while, I just stare at the door, almost like I expect the thing to just open up with Walt behind it."
    
    "After five minutes, however, it finally sinks in that he isn't coming back.{w} I don't know why I thought he would, though."

    "Considering I haven't eaten since breakfast, I decide to just accept the way things are and move to the kitchen."

    show bg kitchen
    with dissolve

    "The smell immediately hits my nose as I enter. A pungent bouquet of rotten meat and aged milk."

    "I lift the garbage bag out of the bin, nearly vomiting as an old carton of milk nearly spills onto the floor."

    "As much as I wish Walt had told me about this, there wouldn't be much of a fix anyway considering the situation we were in."

    show bg door
    with dissolve

    "I suddenly an overwhelming amount of dread as I approach the apartment door, a singular claw of mine hanging on the doorknob."

    "My destination is supposedly where that dream said my doom would be.{w} I can't shake the stupidity of this paranoia."

    "I tell myself..."

    a hangoverclosedclothed "\"It's just a quick trip to the dumpster.{w} In, then out, and I'll be safe in my apartment.\""

    window hide
    show bg normalend1v2
    with dissolvelong
    
    window auto show
    "Each step down the stairs feels like stepping on a landmine.{w} Each tap of the step imitating the trigger's click."

    "When I reach the carport, I notice the lights are fairly dim. My arms itch as my fear of the dark creeps up on me."

    a hangoverupsetclosedclothed "\"It's just going to take thirty seconds, it's only going to take thirty seconds...\""

    "I keep whispering the mantra to myself until I trudge over to the dumpster."

    show bg dumpster
    with dissolve

    "I push the dumpster lid up with all my might, my mind still catching up with my body."

    "I'm about to chuck my trash into the dumpster when I hear it."

    window hide
    play sound "Walt1.ogg"
    pause 4.0
    
    window auto show
    play music "CreepyAmbience.ogg"
    "The fur on my neck bristles, as I slowly muster up to courage to face the sound from behind me."

    window hide
    show bg jumpscare2 with dissolve
    pause 2.0

    window auto show
    "Whatever it was must have left.{w} That or I'm psyching myself up way too much and am to the point of hearing things."

    "Strangely the entire complex seems dim, as if the only light in the entire area was coming from across the street instead."

    a hangoversurprisedclothed "\"Fuck this shit.\""

    show bg dumpster with dissolve
    "Either way the darkness is getting to me, so I reach into my pocket to use my phone's flashlight."

    window hide
    show PhoneHorror at offscreenbottom
    show PhoneHorror at truecenter with MoveTransition(0.4)
    pause 1.5

    window auto show
    a "You... you've got to be kidding me, right?"

    "I give my hand a laugh of fear, repeatedly clicking the button on the side of my phone.{w} I even check if I turned it off before I showered today."

    "Then it dawns on me."

    "My phone was on low battery at breakfast."

    "I never even charged it."

    window hide
    show PhoneHorror at offscreenbottom with MoveTransition(0.1)

    stop music
    play sound "Running.ogg"
    pause 2.0

    show bg jumpscare2
    pause 2.0

    a hangoverraisedtalking2clothed "\"Hello?{nw}\""
    $ config.window_hide_transition = None
    window hide
    show jumpscare at offscreenbottomright
    show jumpscare at right with MoveTransition(0.1)
    hide jumpscare
    show bg black
    play sound "Dumpster.ogg"
    $ config.window_hide_transition = Dissolve(.2)
    pause 2.0

    "I clutch my head as my ears scream with ringing, my eyelids squeezing together when the pain courses through my veins."

    "Whatever just slammed me into the dumpster threw me so hard that I can feel the bile in my stomach swaying back and forth.{w} The sensation alone makes me nearly vomit onto the pavement."

    "I readjust my right hand so I can try to sit up when I feel something warm and sticky on my hand. Along with it is another twinge of pain jolting down my body."

    "I'm scared to see the monster that just attacked, but I know if I keep my eyes closed, I'll dig shards of glass and coke needles into my palms.{w} So slowly they open."

    window hide
    pause 1.0

    show bg normalend2 with dissolvelong
    show darkwalt with dissolvelong

    window auto show
    "In front of me is the man I met last night, but his eyes are of a different ferocity.{w} They're unflinching, almost like a telescope on display, and in them seems to an underlying madness."

    "It's only now I realize that I can't get up, with Walt sitting on my waist as he stares down at me.{w} I pray that someone will walk by and get him off of me, but no one's here."

    show darkwalt open with dis
    w "\"It's not going away for you, is it?\""

    show darkwalt with dis
    "I stare into the wolf's eyes. That feeling of want and longing is morphing into a twisted abomination of love and despair.{w} I can feel the blood run through my fur to the nape of my neck, wondering how Walt hasn't noticed yet."

    "My petty fear of glass and needles flies away as I flail my arms around, trying to find something to grab onto. Either so I can get up or so I can attempt to overpower him."

    show darkwalt open with dis
    w "\"I thought it would if I just left.\""

    w "\"But it was almost like it got worse the farther I was.\""

    hide darkwalt open with dissolve
    play music "CreepyAmbience.ogg" fadein 2.0
    "He plants his muzzle on mine, tilting his head a bit as our lips meet for a kiss."

    "I expected a kiss between us to be full of life and sensual, but all that's in the air is a miasma of discomfort and passionless thought."

    "A string of spit lingers as he pulls away, my eyes dropping to the ground in astonishment. This isn't the Walt I knew, was it?"

    show darkwalt with dis
    "He stares down at me, a hot deep breath meeting my face. A disappointed sigh as I return my gaze to him."

    "I know my fucking head is bleeding, but it only now registers that something is wrong. Something is dead fucking wrong."

    "Walt sways as I look up, with the world behind countering him. Like they're fighting for control of the plane."

    "I retch, the dizziness getting to me. The vomit spills out, tasting only of pennies and acid."

    show darkwalt open with dis
    w "\"Am I that disgusting to you?\""

    show darkwalt with dis
    "I want to scream 'fuck you' to the high heavens, but my stomach rejects me again. My back heaves and stiffens as murky liquid escapes my guts."

    show darkwalt open with dis
    w "\"No... I suppose that's not it.{w} I suppose I did throw you hard.\""

    window hide
    show darkwalt with dis
    pause 2.0
    show darkwalt open with dis
    window auto show
    w "\"Not like it's going to matter.\""

    w "\"I left because I couldn't tell where we were, I guess.\""

    w "\"Your attitude was... throwing me off?\""

    w "\"So I left, thinking this hunger would stop.\""

    w "\"But it just got worse.{w} And worse.{w} AND WORSE.\""

    w "\"I don't want to be with you.{w} But I can't live without you either.\""

    w "\"There's only one thing I can think of to stop this madness.\""

    window hide
    stop music fadeout 2.0
    show darkwalt
    hide darkwalt with dissolve
    pause 3.0

    play sound "Flesh.ogg"
    window auto show
    "Suddenly, the side of my neck feels eerily cold. Like it's not touching fur or skin, but it's actually going through me."

    "It's followed by the sensation of something wet spilling on the ground, and the bottom of my neck warms up."

    "My breathing quickens. It feels like I'm not getting enough air.{w} I try to move my arm to where the feeling is, but my arm feels heavy and limp."

    window hide
    show darkwalt blood with dissolvelong
    pause 3.0

    "Blood drips down Walt's muzzle onto my chest, the single drop feeling like a fifty-pound weight. It's by now I realize what that sensation is."

    w "\"This way we'll be together, right?\""

    hide darkwalt blood with dissolve

    "The wolf doesn't let me give a response, instead planting another emotionless kiss on me. The fucked-up thing is that I wish he continued it because his lips were warm."

    "The body doesn't experience true cold until it starts to bleed out.{w} I remember learning in health class that blood was around 100 degrees Fahrenheit?"

    "Oh, right... I wanted to be a doctor in high school. Huh."

    "Life's a bitch."

    show bg normalend2v2 with dis
    "The energy I once had to look for something to escape with has left me now. My legs are there, but I can't feel them.{w} And my arms are joining them."
    
    "The next mixture of warm and cold comes from my shoulder, so even if I wanted to escape, it'd be useless.{w} I'd just break my bones."

    "My breathing slows, and it feels as if I can sense my heartbeat fading away. I focus on it to help me accept what's happening."

    "Ba-bum.{w} Ba-bum."

    show bg normalend2v3 with dis
    "The trees and sky wrap into a slew of red and gaussian blur. It's getting to the point that I can't tell what I'm even seeing anymore."

    "Walt could be looking down on me and I wouldn't even know."

    "In my final moments, I remember what Walt and I ordered in that club what feels like centuries ago."

    show bg black
    "It was a Silver Bullet."
    $ EndingNormal = True
    $ quick_menu = False
    window hide
    pause 3.0
    jump credits