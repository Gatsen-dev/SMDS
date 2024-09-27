# The script of gay goes in this     .

# the namesss
# all nametags are attached to nameboxes already, just use the nametag and the textbox will appear in that dialogue
# im pretty sure everyone is here already, but if you need to add one, use this template:
# $ (nametag) = Character(None, window_background = "gui/(textbox image name).png")
init:
    $ m = Character(None, window_background = "gui/miketextbox.png")
    $ smi = Character(None, window_background = "gui/sirtextbox.png", image='sir')
    $ ms = Character(None, window_background = "gui/sprtextbox.png")
    $ r = Character(None, window_background = "gui/rosatextbox.png")
    $ sms = Character(None, window_background = "gui/sprotextbox.png")
    $ bm = Character(None, window_background = "gui/moliotextbox.png")
    $ sh = Character(None, window_background = "gui/shadytextbox.png")
    $ o = Character(None, window_background = "gui/omolitextbox.png")
    $ thrs = Character(None, window_background = "gui/theresetextbox.png")
    $ mrsh = Character(None, window_background = "gui/marshatextbox.png")
    $ hd = Character(None, window_background = "gui/haroldtextbox.png")
    $ c = Character(None, window_background = "gui/cartatextbox.png")
    $ cblood = Character(None, window_background = "gui/cartabloodytextbox.png")
    $ h = Character(None, window_background = "gui/harrytextbox.png")
    $ t = Character(None, window_background = "gui/terrytextbox.png")
    $ tg = Character(None, window_background = "gui/tollgatortextbox.png")
    $ kc = Character(None, window_background = "gui/kingcrawlertextbox.png")
    $ g = Character(None, window_background = "gui/guardtextbox.png")
    $ ao1 = Character(None, window_background = "gui/overlordtextbox.png", image='ao1')
    $ bandit = Character(None, window_background = "gui/bandittextbox.png")
    $ anbandit = Character(None, window_background = "gui/anbandittextbox.png")
    $ sabil = Character(None, window_background = "gui/sabiltextbox.png")
    $ ALERTALERTSHADYHASSTOLENTHETEXTBOX = Character(None, window_background = "gui/shadytextboxstolen.png")
define ghhsthm = Character("Gerald Handy-Hands Smith The Helpful Mole")
#
init python:
    define.move_transitions("move", 0.5)
# MUSIC
define audio.rose = "audio/82. Wandering Rose.mp3"
define audio.chill = "audio/17. Forest Chillin'.mp3"
define audio.time = "audio/41. Such A Time We Had Together.mp3"
define audio.pyrefly = "audio/74. Pyrefly Forest - Cat's Cradle.mp3"
define audio.swirly = "audio/91. Swirly 1000x.mp3"
define audio.name = "audio/34. A Rose By Any Other Name....mp3"
define audio.ohmygod = "audio/33. Oh My God..mp3"
define audio.king = "audio/76. Sweet Paralysis.mp3"
define audio.mole1 = "audio/molenoise_1.mp3"
define audio.mole2 = "audio/molenoise_2.mp3"
define audio.hit = "audio/gen_just_smash.ogg"
define audio.dead = "audio/SYS_you died_2.ogg"
# ANIMATIONS
# RENPY IS STUPID AND CAN'T PLAY ANY GIFS SO DO EM LIKE THIS:
image hadys:
    "SMI_hadys1.png"
    0.5 # this part defines how long to wait before next frame
    "SMI_hadys2.png"
    0.5
    repeat
image sabil:
    "SMI_sabil1.png"
    0.5
    "SMI_sabil2.png"
    0.5
    repeat
image scary:
    "SMI_scary1.png"
    0.5
    "SMI_scary2.png"
    0.5
    repeat

# VARIABLES
default mc_name = "dummy"
default tofudie = False
default fig = False
default hp = 1
default sirtrue = 0  # <--- the amount of gifts given to the mole, in future type something like rosatrue and add one after giving each gift
default smiending = False # <--- if sirtrue is 2 (the player gifted both gifts) then the additional cutscene activates
# ^ don't worry about those yet, prob will just add a cute extra scene in the credits and an achievement for getting them

# FOR WRITING:
# {cps=(speed)} text {/cps} makes text appear in textbots the cool way (letter by letter)
# {w} makes the dialogue stop on that spot, making the player push the button to progress
# ^ put those on all sentences, haven't found an easier way to implement them so i do them manually
# {w=2.0}{nw} at the end of a dialogue makes it skip over without waiting for the player to click
# oh also the quotes (") don't work when pasted over here from google docs
# (shows “ instead of ")
# which doesn't work when scripting dialogue
# so probably just put the text in, it works fine

# The boingyboof starts here.

label start:
    scene mybench
    show hup3
    "{cps=60}heyy welcome to da beta number -0.1 enjoy :){/cps}"
    hide hup3
    show hup1
    "{cps=60}oh also choose a name{/cps}"
    $ mc_name = renpy.input("whats your name buckaroo", length=15)
    hide hup1
    show hup3
    "{cps=60}oh hi [mc_name]{/cps}"
    "{cps=60}smiley face :){/cps}"
    jump sir1
    return
label sir1:
    play music rose volume 0.2
    scene sweetbg
    "{cps=70}You find yourself wandering the famous halls of Sweetheart’s castle.{w} Its beauty astonishes you.{/cps}"
    "{cps=70}Suddenly, you see a knight walking around, trying to hand out leaflets to guests,{w} most of whom recline the kind offer.{w} You decide to approach him and find out what he is trying to do.{/cps}"
    play sound mole1
    show sir hap at truecenter with easeinleft:
        yalign 0.2
    smi hap "{cps=70}Hello, how are you doing?{w} I am the founder of the “D.U.M.” club here at the castle!{w} Do you want to join?{/cps}"
    "{cps=70}Well...{/cps}"
    menu:
        "Yea":
            jump sir2
        "Nah":
            "{cps=70}I don't really want to join anything right now.{/cps}"
            play sound mole2
            smi sad "{cps=70}Come on...{/cps}"
            smi sad "{cps=70}I can offer you free snacks..{/cps}"
            "{cps=70}Oh{/cps}"
            menu:
                "Yes":
                    jump sir2
                "Hell yeah":
                    jump sir2
label sir2:
    "{cps=70}Can't pass that up.{/cps}"
    play sound mole1
    smi hap "{cps=70}Yay!{w} Oh gosh, this is so exciting!{w} Okay, you’re probably wondering what “D.U.M.” is an acronym for, yeah?{/cps}"
    smi neut "{cps=70}Well,{w} it’s an acronym for “D&M UNITED MEMBERS”!{/cps}"
    menu:
        "{cps=70}What's D&M?{/cps}":
            play sound mole2
            smi emb "{cps=70}Oh,{w} well...{/cps}"
            jump sir3
label sir3:
    smi hap "{cps=70}It’s Dungeons and Moles of course!{w} Haven’t you heard of it?{w} It’s an amazing tabletop role-playing game about adventurous mole heroes going on epic journeys!{/cps}"
    smi emb "{cps=70}I know that playing board games is not something a knight like me should be doing...{w} Especially after my great-grandfather,{w} grandfather,{w} and father{w} all were brutally murdered not so long ago...{w} But I can't just sit here and do nothing!{/cps}"
    play sound mole1
    smi angy "{cps=70}And it’s not like these{w=1.0}{nw}{/cps}"
    play sound mole2
    smi angy "{cps=70}{i}{b}{color=#ff0000}twisted,{/color}{/b}{/i}{w=1.0}{nw}{/cps}"
    play sound mole2
    smi angy "{cps=70}{i}{b}{color=#ff0000}soulless,{/color}{/b}{/i}{w=1.0}{nw}{/cps}"
    play sound mole2
    smi angy "{cps=70}{i}{b}{color=#ff0000}cold-blooded maniacs{/color}{/b}{/i} are coming back any time soon...{/cps}"
    smi neut "{cps=70}So why not enjoy a new hobby?"
    smi emb "{cps=70}Oh, I'm sorry for blabbering so much...{w} You’re probably bored out of your mind,{w} I'm so sorry...{/cps}"
    smi neut "{cps=70}Here, take the leaflet and uh...{w} I guess you can come play if you want to!{/cps}"
    play sound mole2
    smi hap "{cps=70}Bye-bye now!{/cps}"
    show black with Dissolve(0.3)
    "{cps=70}As you read the leaflet, you notice it's mostly drawings of sprout moles and... Bushes?{/cps}"
    menu:
        "Jump to Day 2, Sweetheart's garden":
            jump sir4
# END OF SMIV DAY ONE
label sir4:
    play music chill
    scene hideout2
    show newgardendark
    hide black with Dissolve(0.3)
    "{cps=60}From what you understood in the leaflet, you came to the right place. When you come behind the bushes you see a table with Marsha, Therese, Harold, and SIR MAXIMUS IV. They were waiting for you."
    hide newgardendark with Dissolve(0.3)
    smi "{cps=60}I’m so glad you came, [mc_name]!{/cps}"
    if tofudie == True:
        menu:
            "Hey, i found this strange tofu thing, do you want it?":
                "{cps=60}You give SIR MAXIMUS IV the tofu six-sided die. His face froze in shock."
                smi "{cps=60}H-how did you get that?! I-it’s the legendary tofu D6!! Mmm... It even tastes pretty good still! Thank you, [mc_name]!!"
                $ sirtrue += 1
                jump aftertofu
    else:
        jump aftertofu
label aftertofu:
    "{cps=60}You see a lot of strange papers and playing cubes on the table.{w} You have no idea what the game is about.{/cps}"
    play sound mole1
    smi "{cps=60}Okay,{w} now that I think about it,{w} I should've probably warned you about the rules...{w} Uhm... Okay, how about you just gloss over the Player’s molebook?{w} It’s,{w} uh,{w} the guide for playing D&M as a player..{/cps}"
    "{cps=60}SIR MAXIMUS IV sets a comically large book in front of you.{w} You don’t even know where to begin.{/cps}"
    smi "{cps=60}O-oh,{w} uhm,{w} o-okay...{w} Uh, how about you just... Learn as we go?{w} Yeah, that.. Sounds good.{/cps}"
    smi "{cps=60}How about you play a fighter mole for your first game?{w} It’s the easiest one to moleplay-{w} I mean roleplay.{/cps}"
    play sound mole2
    smi "{cps=60}Okay, let’s start!!"
    show hideout4
    smi "{cps=60}You are a group of noble heroes, the most powerful adventurers in the world!{w} You’ve been slaying bad guys left and right,{w} until a new monster appeared...{w} ARACHNID OVERLORD.{/cps}"
    play sound mole1
    thrs "{cps=60}I hate arac-...{w} arachno..{w} Uhh..{w} I hate spiders..{/cps}"
    "{cps=60}Therese and Harold gasp in surprise.{/cps}"
    smi "{cps=60}He has been terrorizing your sprout mole village,{w} murdering one friendly mole after the other...{/cps}"
    smi "{cps=60}You decide to stop his villainous reign once and for all.{/cps}"
    play sound mole1
    thrs "{cps=60}I hate villuh-...{w} Violin...{w} I hate evil reigns...{/cps}"
    smi "{cps=60}But to do that, you need to make your way to their castle first,{w} the SCARY PALACE!{/cps}"
    play sound mole2
    thrs "{cps=60}Oh!{w} That sounds kinda scary!!{/cps}"
    show hideout3
    hd "{cps=60}Therese,{w} you should stop interrupting the MDM.{w} (mole dungeon master){/cps}"
    thrs "{cps=60}Ah, yes!{w} (sorry){/cps}"
    show black with Dissolve(0.3)
    smi "{cps=60}...Yeah.{w} Okay.{w} Uhh.{/cps}"
    smi "{cps=60}So you bravely venture forth, holding tight onto your weapons.{/cps}"
    smi "{cps=60}But after some time, you hear a terrified scream of a mother mole nearby.{/cps}"
    play music time
    show hadys
    smi "{cps=60}She screams for help as a group of rude bandits surround her and her innocent child.{/cps}"
    smi "{cps=60}What do you do?{/cps}"
    jump sir5
label sir5:
    menu:
        "I attack the bandit leader with my dagger.":
            mrsh "{cps=60}Heck yeah!{w} That's something i can get behind!{/cps}"
            play sound hit
            smi "{cps=60}As you attack their leader,{w} he gasps in shock.{/cps}"
            bandit "{cps=60}Gah!{w} What the... Is... Is that a dagger!?{/cps}"
            anbandit "{cps=60}Oh shoot...{w} Bro, are you okay?{/cps}"
            anbandit "{cps=60}You’re...{w} You’re hurt...{/cps}"
            bandit "{cps=60}I-i’m fine...{/cps}"
            smi "{cps=60}The other bandits look at you disapprovingly.{/cps}"
            anbandit "{cps=60}Not cool man,{w} not cool.{/cps}"
            anbandit "{cps=60}Yeah!{w} We, the HADYS bandits don’t do violence.{w} We’re chill.{/cps}"
            thrs "{cps=60}Isn’t it HADES?{w} Like uh.. The god of death?{w} King of H-E-Double-Hockey-Sticks?{/cps}"
            anbandit "{cps=60}No.{w} H{w}A{w}D{w}Y{w}S.{/cps}"
            anbandit "{cps=60}C’mon boss, let’s go get you a bandaid..{/cps}"
            play sound mole2
            hd "{cps=60}Good job on that one, [mc_name]!{/cps}"
            play sound mole1
            mrsh "{cps=60}Heck yeah! Justice always wins.{w} You could deal with it more peacefully though!{/cps}"
            smi "{cps=60}The bandit crew walks away, leaving the mother mole alone.{w} She thanks you wholeheartedly and gives all of you a healing potion! You now have 2 Hit Points.{/cps}"
            play sound mole2
            thrs "{cps=60}Yay!{/cps}"
            jump sir6
        "I suggest paying them to let her go.":
            mrsh "{cps=60}Are you delusional?{w} We don’t have any money.{/cps}"
            jump attackbandit
        "We try to sneak past.":
            bandit "{cps=60}Hey boss!!{w} Look, there’s someone sneaking up on us there!{/cps}"
            smi "{cps=60}You've been noticed.{/cps}"
            jump attackbandit
label attackbandit:
    mrsh "{cps=60}It's no use reasoning with them! Dice em up!{/cps}"
    play sound hit
    smi "{cps=60}As you attack their leader,{w} he gasps in shock.{/cps}"
    bandit "{cps=60}Gah!{w} What the... Is... Is that a dagger!?{/cps}"
    anbandit "{cps=60}Oh shoot...{w} Bro, are you okay?{/cps}"
    anbandit "{cps=60}You’re...{w} You’re hurt...{/cps}"
    bandit "{cps=60}I-i’m fine...{/cps}"
    smi "{cps=60}The other bandits look at you disapprovingly.{/cps}"
    anbandit "{cps=60}Not cool man,{w} not cool.{/cps}"
    anbandit "{cps=60}Yeah!{w} We, the HADYS bandits don’t do violence.{w} We’re chill.{/cps}"
    thrs "{cps=60}Isn’t it HADES?{w} Like uh.. The god of death?{w} King of H-E-Double-Hockey-Sticks?{/cps}"
    anbandit "{cps=60}No.{w} H{w}A{w}D{w}Y{w}S.{/cps}"
    anbandit "{cps=60}C’mon boss, let’s go get you a bandaid..{/cps}"
    hide hadys
    hd "{cps=60}Good job on that one, [mc_name]!{/cps}"
    mrsh "{cps=60}Heck yeah! Justice always wins.{w} You could deal with it more peacefully though!{/cps}"
    smi "{cps=60}The bandit crew walks away, leaving the mother mole alone.{w} She thanks you wholeheartedly and gives all of you a healing potion! You now have 2 Hit Points.{/cps}"
    $ hp = 2
    thrs "{cps=60}Yay!{/cps}"
    jump sir6
label sir6:
    show sabil
    smi "{cps=60}After some time, you get tired and thirsty.{w} You look around for a water source and see a lake nearby.{w} You come closer and see a fish in need of help.{/cps}"
    sabil "{cps=60}Hello, fellow adventurers... My name is Sabil... You can see I'm in quite a pickle... A sea pickle...{/cps}"
    smi "{cps=60}He is on the hot and sizzling docks of the pond.{/cps}"
    thrs "{cps=80}do you mean a pond pickle{w=0.5}{nw}{/cps}"
    sabil "{cps=60}Can you just...{w} Kick me back into the pond?{w} I’m going to suffocate here...{/cps}"
    smi "What do you do?"
    menu:
        "I save Sabil.":
            mrsh "{cps=60}*sigh* You dubious doofus.{w} This is such an obvious trap! How would a fish get so far out of the water?{w} A paladin like me would righteously suspect a nasty trick up this fishie’s sleeves.{w} If it had any.{/cps}"
            sabil "{cps=60}Uhm... I’m actually a very trustworthy fish...{w} I travel a lot because it’s a good way to release bottled up stress, anxiety, and guilt!{/cps}"
            mrsh "{cps=60}I want to believe that.{w} But it’s quite unlikely.{/cps}"
            mrsh "{cps=60}I don’t know what you’re thinking, [mc_name], but this is obviously some sort of mimic.{w} He will bite your leg clean off if you try to kick him back into the lake.{/cps}"
            thrs "{cps=60}I mean... I don’t know...{w} He seems like a nice guy.. I would trust him..{w} Or not...{/cps}"
            hd "{cps=60}Yeah, I don't agree with you too, Marsha..{w} I just don’t see how such a tiny innocent fish could be a mimic..{/cps}"
            mrsh "{cps=60}Ugh, it is my responsibility to warn you.{w} You’ve heard me.{/cps}"
            menu:
                "Yes I Absolutely Really Really Want To Save Sabil":
                    jump sabilsave
                "Nah, on second thought, i kinda need this leg.":
                    jump sabildie
        "I don't save Sabil.":
            mrsh "{cps=60}What? Are you serious?{w} How could you be so cruel to this innocent fish?{/cps}"
            mrsh "{cps=60}Hmm... But, now that I think about it, yes, maybe we shouldn’t save him.{w} He might not really need our help.{/cps}"
            sabil "{cps=60}Uhh- No?? I-i really am d-dying right now!!{w} C-can you please save me already??{/cps}"
            hd "{cps=60}Uhm, [mc_name], I think you should save him...{/cps}"
            thrs "{cps=60}Uhm... Yeah, I think so too...{w} I guess... Maybe..{/cps}"
            menu:
                "Yeah we should save this mackerel.":
                    jump sabilsave
                "Yea no he's fine on his own":
                    jump sabildie
label sabilsave:
    smi "{cps=60}You carefully kick Sabil back into the water, he looks very pleased.{/cps}"
    sabil "{cps=60}Oh thank you, kind travelers!!{w} Have this as a humble reward!{/cps}"
    smi "{cps=60}You now have another Hit Point! You now have 3 HP.{/cps}"
    sabil "{cps=60}I'm kinda broke... That was my last healing potion...{/cps}"
    jump smi7
label sabildie:
    smi "{cps=60}Sabil looks at you, terrified and speechless.{w} You look him in the eyes as he passes away.{/cps}"
    hd "{cps=60}Man, that was... Cruel."
    thrs "{cps=60}Yeah, that was kinda.. Horri-...{w} Hor.. Hori..{w} That was kinda scary.{/cps}"
    jump smi7
label smi7:
    play music pyrefly
    show scary
    smi "{cps=60}You continue walking until you reach the castle...{w} SCARY PALACE!{/cps}"
    smi "{cps=60}It’s pretty dark and cold inside.{w} You can swear you heard some pitter-patter behind you.{/cps}"
    mrsh "{cps=60}We will do whatever it takes, no one will be left behind!!{/cps}"
    hd "{cps=60}Never heard about this place before...{/cps}"
    thrs "{cps=60}he told us not so long ago?{w} even i remembered that...{/cps}"
    hide black with Dissolve(0.3)
    show black with Dissolve(0.3)
    smi "{cps=60}You go further and see an empty throne.{w} But before you could turn around...{/cps}"
    play music swirly
    scene ao1
    hide black with Dissolve(0.3)
    smi "{cps=60}ARACHNID OVERLORD STRIKES RIGHT AT YOU FROM THE CEILING!!!{/cps}"
    smi "{cps=60}He's enraged, screaming:{/cps}"
    ao1 angy "{cps=60}HOW DARE YOU ENTER MY LAIR?!{w} PREPARE TO PERISH, PUNY MOLES!!{/cps}"
    jump fight1
label fight1:
    smi "{cps=60}ARACHNID OVERLORD BECAME FURIOUS!{/cps}"
    hd "{cps=60}Quick, [mc_name], do something!{w} He’s angry so the best you can do is try to stay on guard and try to block the attack!{/cps}"
    menu:
        "ATTACK":
            play sound hit
            $ hp == -1
            if hp < 1:
                jump deathao
            else:
                play sound dead
                smi "{cps=70}You've been badly hurt.{/cps}"
                jump attack2
        "DODGE":
            play sound hit
            $ hp == -1
            if hp < 1:
                jump deathao
            else:
                play sound dead
                smi "{cps=70}You've been badly hurt.{/cps}"
                jump attack2
        "GUARD":
            jump attack2
label attack2:
    ao1 hap "{cps=60}HAHAHA!! YOU THINK YOU CAN TAKE ME ON?{w} THAT LITTLE SHIELD OF YOURS WON’T SAVE YOU NOW!{/cps}"
    ao1 hap "{cps=60}ARACHNID OVERLORD BECAME MANIC!{/cps}"
    thrs "{cps=60}Oh, i know this one!!{w} When enemies are happy, their accuracy goes down!{w} Roll out of the way!{/cps}"
    menu:
        "ATTACK":
            play sound hit
            $ hp == -1
            if hp < 1:
                jump deathao
            else:
                play sound dead
                smi "{cps=70}You've been badly hurt.{/cps}"
                jump attack2
        "DODGE":
            smi "{cps=60}ARACHNID OVERLORD falls to the ground after his attack and hits his head hard.{/cps}"
            jump attack3
        "GUARD":
            play sound hit
            $ hp == -1
            if hp < 1:
                jump deathao
            else:
                play sound dead
                smi "{cps=70}You've been badly hurt.{/cps}"
                jump attack2
label attack3:
    ao1 sad "{cps=60}OUCH... THAT WAS QUITE- OW.{w} THAT WAS QUITE CLUMSY OF ME.{w} I FEEL DISAPPOINTED BECAUSE OF MY INCOMPETENCE.{/cps}"
    smi "{cps=60}ARACHNID OVERLORD BECAME MISERABLE!{/cps}"
    mrsh "{cps=60}He won't be hitting for some time now, how about an attack?{/cps}"
    menu:
        "ATTACK":
            smi "{cps=60}OVERLORD screeches, hurt deeply.{/cps}" with hpunch
            ao1 dead "{cps=70}F-FU..."
            ao1 dead "{cps=60}Fudge... You have bested me,{w} the ARACHNID OVERLORD...{/cps}"
            ao1 dead "{cps=60}I SALUTE YOU, HERO.{/cps}"
            menu:
                "FINISH HIM OFF":
                    jump daytwoend
        "DODGE":
            play sound hit
            $ hp == -1
            if hp < 1:
                jump deathao
            else:
                play sound dead
                smi "{cps=70}You've been badly hurt.{/cps}"
                jump attack3
        "GUARD":
            play sound hit
            $ hp == -1
            if hp < 1:
                jump deathao
            else:
                play sound dead
                smi "{cps=70}You've been badly hurt.{/cps}"
                jump attack3
label daytwoend:
    smi "{cps=60}You hold your dagger, preparing for the final attack, and then you-{/cps}"
    hide ao1
    show hideout
    stop music
    play sound mole2
    "{cps=60}You hear rustling from the bushes nearby,{w} when suddenly some guards appear.{/cps}"
    g "{cps=60}SIR MAXIMUS IV!{w} Are you seriously playing these stupid board games again, even though we SAID NOT TO?!{/cps}"
    play sound mole1
    smi "{cps=60}O-oh, u-uhm...{w} I can explain!!{/cps}"
    g "{cps=60}This is it, pal.{w} I’m sorry, but SWEETHEART ordered us to demote you to “PYREFLY PATROLLER” if we catch you slacking off again.{w} You’re no longer an esteemed guard.{/cps}"
    mrsh "{cps=60}P-pyrefly p-patroller?!{w} You can’t do that! No one came back from their shifts at pyrefly forest!{/cps}"
    thrs "{cps=60}I-i h-heard there’s a monster there...{/cps}"
    hd "{cps=60}This simply isn’t fair! You can’t send him on a suici-...{w} I mean, on a no-return mission!!{/cps}"
    scene black
    "{cps=60}But the guards don’t care.{w} It’s nothing personal, only a job.{w} They grab SIR MAXIMUS IV and take him away. MARSHA goes after them, screaming at them to let SIR MAXIMUS go. Two others stay at the table though, HAROLD comforts THERESE, who is sobbing.{/cps}"
    hd "{cps=60}I-it’s okay, SIR MAXIMUS will be alright...{w} He always finds a way out... Everything is going to be okay...{/cps}"
    play sound mole1
    thrs "{cps=10}...{/cps}"
    menu:
        "Jump to Day 3, Pyrefly forest":
            jump sirdaythree
# END OF SMIV DAY TWO
label sirdaythree:
    play music pyrefly
    "{cps=60}As you approach the forest, you see three familiar moles in the distance.{w} You quickly recognise each other.{/cps}"
    scene smiwhere
    if fig == True:
        mc "{cps=60}Hey, i wanted to give this figurine to SIR MAXIMUS, but, well, you know..{w} Can you keep it safe for now?{/cps}"
        hd "{cps=60}My god, such a fabulous creation. I believe it’s homemade, yes?{w} How handsome this hero looks, I hope I can play as him in the next session...{/cps}"
        hd "{cps=60}A-anyways...{/cps}"
        $ sirtrue += 1
        if sirtrue == 2:
            $ smiending = True
            jump afterfig
        else:
            jump afterfig
    else:
        jump afterfig
label afterfig:
    hd "{cps=60}W-we’ve been looking for SIR MAXIMUS IV, but...{w} He’s nowhere to be found.. I hope we’re not too late..{/cps}"
    thrs "{cps=60}We sneaked out of our apartments in the castle to save him, but we haven’t seen him yet..{/cps}"
    mrsh "{cps=60}We need to go deeper into the forest.{w} I am NOT leaving our esteemed “MM” to die here!{/cps}"
    hd "{cps=60}Yeah... The times we had with our “MM” were the best..{w} He's a good friend of mine, a true BFF..{/cps}"
    thrs "{cps=60}I didn’t mind spending a whole shift at this dead-end stupid job,{w} because I could spend my nights just chatting with you all and playing games...{/cps}"
    mrsh "{cps=60}Let’s go already!! I didn’t bring my battle axe for nothing!{w} We will take this monster on, whatever it is!{/cps}"
    show black with Dissolve(0.3)
    "{cps=60}You venture deep into the forest, strange plants stopping you occasionally.{w} Spiders crawl here and there, you can hear screams from further into the forest, the voice familiar to you. It must be SIR MAXIMUS IV.{/cps}"
    "{cps=60}As you go deeper, you finally see the monster.{w} Its sharp claws are latched onto SIR MAXIMUS IV.{/cps}"
    hd "{cps=60}You foul beast! Release our friend at once!{/cps}"
    mrsh "{cps=60}Or we’ll smash you into bits and pieces, by the rules of law!!{/cps}"
    thrs "{cps=60}Y-yeah!..{/cps}"
    jump attack11
label attack11:
    play music king volume 0.4
    scene kingcrawler
    show goobers with easeinbottom
    kc "{cps=60}KING CRAWLER hisses at you predatorily.{w} It’s time to fight!{/cps}"
    kc "{cps=60}It’s impatient.{w} It is ready to rip you apart, offended by your blind optimism.{/cps}"
    menu:
        "ATTACK":
            play sound hit
            "{cps=60}You command MARSHA to attack!{w} MARSHA’s attack gets blocked by KING CRAWLER’s sharp claws and he attacks you.{/cps}"
            jump deathkc
        "DODGE":
            "{cps=60}THERESE panics out and commands everyone to dodge.{w} That was useless..{/cps}"
            jump deathkc
        "GUARD":
            "{cps=60}You ask HAROLD to guard KING CRAWLER’s furious attack.{w} Surprisingly enough, his iron armor fully blocks it!{/cps}"
            jump attack22
label attack22:
    kc "{cps=60}King crawler takes a moment to enjoy how stupid you look.{/cps}"
    menu:
        "ATTACK":
            "{cps=60}You command MARSHA to attack!{w} MARSHA’s attack gets blocked by KING CRAWLER’s sharp claws and he attacks you.{/cps}"
            jump deathkc
        "DODGE":
            "{cps=60}THERESE commands everyone to roll away.{w} You successfully dodge KING CRAWLER’s massive attack!{/cps}"
            jump attack33
        "GUARD":
            "{cps=60}You ask HAROLD to guard KING CRAWLER’s attack.{w} He didn’t hear you.{/cps}"
            jump deathkc
label attack33:
    kc "{cps=60}King crawler looks at SIR MAXIMUS IV trying to escape the claws' painful clutch.{w} King Crawler rethinks his actions for a moment.{w} Just for a moment.{/cps}"
    menu:
        "ATTACK":
            "{cps=60}You command MARSHA to attack!{w} It didn't do much...{/cps}" with hpunch
            jump attack44
        "DODGE":
            "{cps=60}THERESE panics out and commands everyone to dodge.{w} That was useless..{/cps}"
            jump attack33
        "GUARD":
            "{cps=60}You ask HAROLD to guard KING CRAWLER’s attack.{w} He didn’t hear you.{/cps}"
            jump attack33
label attack44:
    kc "{cps=60}King crawler screeches.{w} He didn’t expect that sudden attack, now he’s ready to charge again.{/cps}"
    menu:
        "ATTACK":
            "{cps=60}You command MARSHA to attack!{w} MARSHA’s attack gets blocked by KING CRAWLER’s sharp claws and he attacks you.{/cps}"
            jump deathkc
        "DODGE":
            "{cps=60}THERESE panics out and commands everyone to dodge.{w} That was useless..{/cps}"
            jump deathkc
        "GUARD":
            "{cps=60}You ask HAROLD to guard KING CRAWLER’s furious attack.{w} Surprisingly enough, his iron armor fully blocks it!{/cps}"
            jump attack55
label attack55:
    kc "{cps=60}King crawler tries to keep up his positive mood.{/cps}"
    menu:
        "ATTACK":
            "{cps=60}You command MARSHA to attack!{w} MARSHA’s attack gets blocked by KING CRAWLER’s sharp claws and he attacks you.{/cps}"
            jump deathkc
        "DODGE":
            "{cps=60}THERESE commands everyone to roll away.{w} You successfully dodge KING CRAWLER’s massive attack!{/cps}"
            jump attack666
        "GUARD":
            "{cps=60}You ask HAROLD to guard KING CRAWLER’s attack.{w} He didn’t hear you.{/cps}"
            jump deathkc
label attack666:
    kc "{cps=60}King crawler rethinks his actions again and lowers his guard.{/cps}"
    menu:
        "ATTACK":
            "{cps=60}You command MARSHA to attack!{w} It still isn't enough..{/cps}" with hpunch
            jump finale
        "DODGE":
            "{cps=60}THERESE panics out and commands everyone to dodge.{w} That was useless..{/cps}"
            jump attack666
        "GUARD":
            "{cps=60}You ask HAROLD to guard KING CRAWLER’s attack.{w} He didn’t hear you.{/cps}"
            jump attack666
label finale:
    mrsh "{cps=60}What in the name of Sweetheart is that thing?!{w} Why isn’t it dying?!{/cps}"
    hd "{cps=60}We’re not going to make it... *sigh*...{w} Too bad no superhero will ascend from the sky and help us... We’re on our own...{/cps}"
    stop music
    thrs "{cps=60}Guys! Look!{w} What is that in the sky?{/cps}"
    "{cps=60}Everyone looks up. Even KING CRAWLER.{w} You see a magnificent figure slowly descend from the skies, spinning gracefully, a light of hope in the sea of despair.{w} You can smell fruits and a pretty nice perfume.{/cps}"
    show bigmolio hap with easeintop
    play music ohmygod volume 0.5
    bm "{cps=60}{b}HELLO, MY FELLOW MOLES!{w} IT IS I, YOUR SAVIOR, BIG MOLIO.{/b}{/cps}"
    bm "{cps=60}{b}I am here to slay this foul beast and help you.{/b}{/cps}"
    show black with Dissolve(0.3)
    "{cps=60}All 5 of you scramble away as you hear the sounds of an amazing battle fade in the distance.{w} You’re finally safe.{/cps}"
    "{cps=10}...{/cps}"
    scene pyreflybg
    show sir sad at truecenter:
        yalign 0.2
    smi sad "{cps=60}My friends... I can’t believe you tried to save me!{w} Oh, how noble of you... But also quite foolish.{w} What if Big Molio wasn’t there to save us? We would all die!{/cps}"
    smi neut "{cps=60}Nevertheless, I will be eternally grateful... {w}Especially to you, [mc_name]! You were so heroic back there, way more than I...{/cps}"
    thrs "{cps=60}Phew... I’m glad all of this is resolved now but...{w} How will we come back now? You’re still not allowed there anymore...{/cps}"
    hd "{cps=60}Yeah, and we’ll probably get in trouble after what happened...{/cps}"
    mrsh "{cps=60}I don’t actually know.{/cps}"
    smi hap "{cps=60}My friends, I have the perfect plan!...{/cps}"
    show black with Dissolve(0.3)
    play music time
    "{cps=10}...{/cps}"
    scene dotty
    with irisout
    hide black with Dissolve(0.3)
    show smi0 with easeinleft
    "{cps=60}A guard stands at the entrance of the castle.{w} He stops SIR MAXIMUS IV.{/cps}"
    g "{cps=60}Hey, aren’t you SIR MAXIMUS IV?{w} I think you’re not allowed here, pal.{/cps}"
    show smi1 with easeintop
    smi "{cps=60}Oh, but you are mistaken, my friend.{w} I am SIR MAXIMUS V!{/cps}"
    show smi2 with easeinbottom
    "{cps=60}And I am SIR MAXIMUS VI!{/cps}"
    show smi3 with easeintop
    thrs "{cps=60}And I am SIR MAXIMUS VII!{w} I-i guess!...{/cps}"
    show smi4 with easeinbottom
    mrsh "{cps=60}I am SIR MAXIMUS VIII! I just.{w} Uh.{w} Forgot my armor at home.{w} Yes.{/cps}"
    show smi5 with easeintop
    hd "{cps=60}Haha, pleasure to meet you!{w} I am SIR MAXIMUS IX, of course!{/cps}"
    show smi6 with easeinbottom
    g "{cps=60}Hmm... Okay, I will let you through, let me just..{w} Do this real quick...{/cps}"
    $ renpy.movie_cutscene('dicethrow.webm')
    g "{cps=60}Ah yes, you can go through, dear guards.{w} Have fun!{/cps}"
    scene black
    stop music
    "{cps=10}...{/cps}"
    "{cps=10}le fin{/cps}"
    # END OF SMIV DAY THREE
    play music name volume 0.4
    scene mybench
    show hup1
    with blinds
    "{cps=60}Wow! That was so cool! Right? Right??{/cps}"
    hide hup1
    show hup2
    "{cps=60}not much but ehh :){/cps}"
    hide hup2
    show hup3
    "{cps=60}now i banish you to the desktop muahahaha{/cps}"
    hide hup3
    show hup1
    "{cps=60}- huperk :3{/cps}"
    $ renpy.quit()
label deathao:
    show black
    "{cps=60}You fall to the ground, sharp clothes dig into your skin and rip you apart. It's over.{/cps}"
    menu:
        "Hey, Sir Maximus IV, can we redo that fight..? Pretty please?":
            jump fight1
label deathkc:
    show black
    play sound dead
    "{cps=60}You fall to the ground, sharp clothes dig into your skin and rip you apart. It's over.{/cps}"
    menu:
        "It's okay to try again.":
            jump attack11
