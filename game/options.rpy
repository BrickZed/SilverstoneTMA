## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Silverstone: The Morning After")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "1.02"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
SPOILERS AHEAD! PLEASE DON'T READ BEFORE FINISHING THE GAME!

-----------------------------------------------------------

Hello, and welcome to "Silverstone: The Morning After." This is a visual novel made for the May Wolf 2024 Jam and an indirect prequel to "Silverstone," the main FVN I'm planning. I (BrickZed) figured I would use the about section to detail the process developing this game as it's my first visual novel. Think of this as a post-mortem of sorts.

The creation of S:TMA was somewhat turbulent due to many factors. I had just started living on my own, was having severe health issues, and I wasn't fully comfortable with being out as a furry yet; to my friends or family. Ironically, my friends are what helped me fully embrace being a furry and I might have constantly sent videos to them. My work on the game started a little later than most, on the 3rd of May instead of the 1st. The initial designs were, for lack of a better word, fucking shit. I quickly was able to create a better design for Walt on the 4th, however, and then Asher's design came to me almost instantly. The backgrounds were created along the way, with a lot of photography and Photoshop sessions happening when they were needed. Very few photos were borrowed from other sources since I wanted the majority of the game to be made by me. The UI was probably the biggest pain, simply due to hours of arguing with Ren'py's programming. It was eventually solved, however!

Music was created bit by bit since it wasn't a primary focus compared to other parts. There are only six songs in the entire game, plus an ambient track created from free sound effects (it's literally called "CreepyAmbience.ogg" lol). I like the arrangements of the tracks, but I feel like they would have been a lot better with an actual producer. "The Morning After" suffered especially since FL Studio has no good guitar presets. The unfortunate side effects of being a sole dev during a game jam.

My favorite part was probably the writing and programming. I already knew a bit of Python and Ruby, so coding issues were mainly from learning more complex algorithms and my own stupidity (something that happened often was putting the incorrect file name in), but coding was for the most part smooth sailing. The story changed quite a bit over development, mainly due to a lack of planning compared to other projects I've done. The initial idea was just a straight-forward romantic visual novel with little deviation, but this quickly changed as I wrote. As early as the breakfast decision, I added in a romance points system and multiple endings (initially there were two, but I extended this to three after having trouble deciding what "bad" ending to use). Later on, I added horror elements to tie it more into the Silverstone universe I conjured up a couple years ago. I decided to keep it separate from Silverstone's main story though so it could enjoyed on it's own.

Honestly, the hardest part was probably keeping a consistent tone when switching between different options. I didn't want Walt to suddenly divebomb into being an asshole after being an incredibly charming person. For the judges, I chose to present the theme of "expanding" as developing a relationship, which is another reason the multiple endings happened. Would the player cause the relationship to grow or completely turn to dust? In the "good" end, I took this literally by having Asher die of an enlarged heart. Is it kind of mean? Maybe. I wanted to subvert having the "earn your happy ending" thing most visual novels do, though, to drive home the fact that Silverstone is a place full of loss and pain. Even if there's brief moments of happiness, sometimes shit hits you when you least expect it. Then again, I was also kind of in a "I wanna kill my OCs" mood due to my mental and physical state at the time, haha.

For those wondering what books I had Walt read, they're all based on other furry visual novels: "Adastra" by The Echo Project, "Remember The Flowers" by Jericho, and "Socially Awkward" by monchimutt. All great visual novels you should read.

What's next for me? I'll be taking a month-long break so I can catch up on other projects and play games made by the other devs from the jam. If there are any bugs or typos, however, there will be some updates. After that the break ends, I'm going to start working on the main game for Silverstone. If you want to follow development, you can find me on Twitter (@BrickZed) or follow me on itch.io. Hope to see you all in the future, and take care!

-BrickZed
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "SilverstoneTheMorningAfter"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "Main Menu.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = Fade(0.5, 0.5, 0.5)


## Used when entering the main menu after the game has ended.

define config.end_game_transition = Dissolve(2.0)

## Used after splash

define config.end_splash_transition = Dissolve(2.0)

## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 50


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "SilverBullets-1714779328"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
