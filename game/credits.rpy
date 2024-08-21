label credits:
    if EndingGood == True:
        $ credits_speed = 80
        scene bg black
        play music "Credits.ogg"
        show bg theend with fade
        pause 5.0
        show bg black with dissolvelong
        pause 1.0
        show Credits at Move((0.5, 1.0), (0.5, -3.27), credits_speed, xanchor=0.5, yanchor=0) with Pause(credits_speed+2)
        stop music fadeout 3.0
        pause 2.0
        jump epilogue
    elif EndingNormal == True or EndingBad == True:
        $ credits_speed = 80
        scene bg black
        play music "Remembrance.ogg"
        show bg theend with fade
        pause 5.0
        show bg black with dissolvelong
        pause 1.0
        show Credits at Move((0.5, 1.0), (0.5, -3.27), credits_speed, xanchor=0.5, yanchor=0) with Pause(credits_speed+2)
        stop music fadeout 3.0
        pause 2.0
    elif EndingExtra == True:
        $ credits_speed = 80
        scene bg black
        play music "Credits.ogg"
        show bg theend with fade
        pause 5.0
        show bg black with dissolvelong
        pause 1.0
        show Credits at Move((0.5, 1.0), (0.5, -3.27), credits_speed, xanchor=0.5, yanchor=0) with Pause(credits_speed+2)
        stop music fadeout 3.0
        pause 2.0
        
        return