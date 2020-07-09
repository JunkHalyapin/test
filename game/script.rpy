# The script of the game goes in this file.

init python:
    renpy.music.register_channel("voices","bgm",False,tight=True)

    def set_voices_volume(value=None):
        if value is None:
            return MixerValue('bgm')
        else:
            return SetMixer('bgm', value)

    import pygame.scrap
    def scrubs(what):
        pygame.scrap.put(pygame.SCRAP_TEXT, what.encode("utf-8"))
        renpy.notify("The text is now on the clipboard.")

#Intro
label splashscreen:

    show parental_advisory
    with Pause(5)

    scene black with dissolve
    with Pause(1)

    return

label start:

    scene day1 ev01-01
    "The early morning light illuminates a young couple lying in bed, both sleeping soundly."
    "The silence of the apartment is interrupted at exactly 6:00 AM."

    scene day1 ev01-02  with dissolve
    play sound alarm_clock loop
    pause 1
    "The alarm only blares for a few seconds before it jolts Jessica O'Neil out of her sleep."

    scene day1 ev01-03
    pause 1
    stop sound
    "She glances at the arm of the man beside her and shuts off the alarm."

    scene day1 ev01-04
    JesT "Nothing wakes Conner up. He once told me he slept through a mortar attack in Afghanistan."
    Con "..."
    JesT "I missed him so much while he was deployed. It feels like a dream that he is finally back with me in one piece."
    Con "ZzzzzzzzZZzz"
    JesT "He's so cute when he's snoring. I want to curl up next to him and spend all day in bed, but I'd better take a shower."

    scene day1 ev01-05
    JesT "Today I start my new job as junior reporter at the New Port Gazette. I could barely sleep I was so excited about my first day."

    scene day1 ev02-01 with fade
    "Jessica slips out of her panties and steps into the shower."

    scene day1 ev02-02
    play sound shower_1 loop
    "The warm water pours over her ample curves as she washes herself with the exfoliating sponge."

    scene day1 ev02-03
    "The bathroom fills with steam as she lathers her breasts and between her toned thighs."

    scene day1 ev02-04
    "Her fingers stroke the delicate folds of her pussy."
    JesT "I'm so wound up about this first day. Maybe I should release a little tension."

    scene day1 ev02-05
    play voices x_moaning_1
    "She plays with her thick, sensitive nipples, gasping softly in the rush of water as her fingers tighten around her tender buds."
    "Her hands trail from the soft mounds of her breasts down her toned tummy."

    scene day1 ev02-06
    "Her nimble fingers massage her aching groove and rub at her clit."
    JesT "Oh god, he touched me like this last night, when he came back home. He kissed me like when we first started dating."
    JesT "His hand slid into my panties as he kissed me. And then he took me up against the wall."
    "She leans back, pressing herself against the steamy shower wall and fucking herself with two fingers."

    if persistent.pov == 2:
        scene day1 ev02-07fpov
    else:
        scene day1 ev02-07
    "Her breasts heave with her lust and her pussy aches with her need to cum."
    Jes "Oh, Conner…"
    "Her soft cries of pleasure echo in the shower. She thrusts her hips and fucks herself faster and faster."
    "Her pleasure builds as she plunges her fingers into her hungry channel, but Jessica stops short of an orgasm."

    scene day1 ev02-08
    stop voices fadeout 1
    JesT "Conner."
    JesT "I need to wake up Conner. I can have a little fun with him before work. I've missed him so much."

    stop sound fadeout 1
    scene day1 ev02-09
    "Jessica lets out an excited breath and steps out of the shower. Her thighs are shaking with desire as she quickly runs the towel over the shapely body, hastily drying her soaking skin.."
    "Eager to be back with Conner, she wipes away herself down but leaves her hair moist, unwilling to wait."

    scene day1 ev02-10
    "Once mostly dry, she slips into her silk robe, hastily returning to the bedroom."

    scene day1 ev03-01 with fade
    "Jessica's body burns with lust for Conner as she crawls into bed next to him."
    Jes "Wake up, sweetie."
    Con "ZZzzzz..."
    Jes "C'mon, sleepyhead. You told me to get you up before I leave for work."
    Con "..."

    show day1 ev03-02
    "Conner rolls onto his back and pulling the blanket off of him Jessica sees his erection sticking up in the front of his shorts."
    JesT "Oh, my… somebody is having a good dream…"

    show day1 ev03-03
    "She runs her hand over Conner's shorts and feels his rigid manhood swelling within."
    JesT "Oh, I've missed having my big boy home."
    "She reaches inside his boxers and takes hold of her boyfriend's hard cock."

    show day1 ev03-04ani-0
    JesT "At least one soldier is standing at attention."
    "Her pulse quickens as she feels his familiar hardness in her grasp."
    JesT "I went so long without him, I can't resist him now."
    "Almost without a conscious thought, Jessica's hand begins to move from Conner's root to his swollen tip."

    show d01ev03-handjob-ani
    JesT "I'm sure he won't mind if I wake him up like this."
    "Jessica's heart swells as her hand works over her boyfriend's rigid manhood, a warmth stirring within her loins."
    JesT "He's so hard I can feel his heart beating in his cock."
    "Conner groans softly in his sleep, but does not wake as she continues to stroke his throbbing manhood. He's still asleep..."
    JesT "He wasn't kidding. A soldier really can sleep through anything."

    hide d01ev03-handjob-ani
    JesT "I'll have to resort to something a little more intense to wake him up."
    JesT "What should I do?"

    menu:
        "Ride his cock":
            $ tempvar = 1
            $ sex += 1
            JesT "Oh, god, I need to have him inside me…"
            jump day01morningsex

        "Suck his cock":
            $ tempvar = 2
            $ blowjob += 1
            JesT "I know just the way to wake him up…"
            jump day01morningblow

label day01morningblow:

    "Jessica rarely performs oral sex on her boyfriend, but she knows he likes it."

    scene day1 ev03-21 with fade
    "As she strokes his hardness, she leans her head down to his cock and begins licking the fat tip."
    "She knows the spot that drives him crazy just underneath his cockhead."
    Con "Zzzz..."

    scene day1 ev03-22
    JesT "Hmmm, still sleeping?"

    scene day1 ev03-23
    JesT "Guess I will have to try a little harder."

    scene day1 ev03-25ani-0
    play voices x_bj_1 loop
    "She takes his stiff cock into her mouth, sliding her full lips over his cockhead as her tongue cradles the underside of his length."
    JesT "Oh god, yes! Having his cock in my mouth is making me so hot."
    play sound x_bj_2
    "She gags a bit on her first try."
    JesT "I'm not used to this… but I'm not giving up."

    show d01ev03-blowjob_ani01
    "She can't take all of his hard cock, so she uses her hand at the base as she begins to bob and slurp on her boyfriend's hot meat."
    Con "Mmmm?"
    hide d01ev03-blowjob_ani01
    show day1 ev03-25ani-9
    "Her spit soaks his shaft and drips from his balls as she works her hot mouth up and down Conner's fat cock."
    JesT "I feel like such a dirty slut! I love it!"
    Jes "Mmmmmm…"
    "Her moan of pleasure vibrates around his shaft."

    if persistent.pov == 1:
        scene day1 ev03-26mpov with fade
    else:
        scene day1 ev03-26 with fade
    Con "Wha…??"
    "He finally stirs, groggily lifting his head to find his beautiful girlfriend eagerly blowing his hard cock."
    Con "Baby… ohhh god… that's so good."
    stop voices fadeout 2

    if persistent.pov == 1:
        scene day1 ev03-27mpov
    else:
        scene day1 ev03-27
    Con "What are you… what are you doing?"
    Jes "What does it look like I'm doing, silly?"
    Jes "Giving you a blowjob! Good morning!"

    scene day1 ev03-28b
    play voices x_bj_3
    Con "Ohhh fuck..."

    scene day1 ev03-28ani-0
    "Jessica's mouth descends wantonly on his hard dick."

    show d01ev03-blowjob_ani02
    "She bobs up and down on the thick piston of his cock, her spit soaking down his shaft as her fist pumps his root."
    "Conner thrusts gently into her grasp, fucking her mouth as much as Jessica will permit."
    JesT "I love blowing someone who actually responds. His dick is so much better than the dildos that kept me company while he was gone."
    "Jessica revels in the eroticism of the moment, overjoyed to have Conner ready to fill her with his love."
    hide d01ev03-blowjob_ani02

    scene day1 ev03-28
    JesT "Mmmmmm! I can taste his precum!"

    scene day1 ev03-29a
    "Her pleasure grows with Conner's and she begins to play with her clit as she sucks his cock."

    scene day1 ev03-30
    Con "That's so good. You’re going to make me cum if you don't stop."
    JesT "I usually don't let him cum in my mouth… but I can't stop myself."

    scene day1 ev03-31
    Con "Baby, did you hear me?"

    if persistent.pov == 1:
        scene day1 ev03-32mpov
    else:
        scene day1 ev03-32
    "She looks up at him, begging with her moans and lusty eyes to cum into her mouth."

    scene day1 ev03-33
    Con "Aahhhhhhhh fuck!"
    JesT "Oh god, I'm going to cum too!"
    "Conner's cock throbs and spurts out hot, salty gushes of cum into Jessica's mouth."

    scene day1 ev03-34b
    "The hot spurting of his cum into her mouth drives Jessica over the edge."
    JesT "Oh my god! Yesss!"
    "As she sucks out his load, she swallows and cums against her fingers, her hips bucking and her fingers pumping lewdly in and out of her soaking pussy."
    stop voices fadeout 3

    scene day1 ev03-34c
    Con "Oh, sweetie, you are amazing!"

    scene day1 ev03-35
    JesT "I can't believe I swallowed it all…"

    scene day1 ev03-36
    "Gasping, she releases his cock from the heat of her mouth, dragging her body over his before collapsing beside him on the bed."

    jump day01dressup

label day01morningsex:

    scene day1 ev03-51 with fade
    "Jessica straddles her boyfriend, stroking his hardness against the slick furrow of her cunt."

    scene day1 ev03-52 with fade
    Jes "Yessss…"

    scene day1 ev03-53ani-0 with fade

    show d01ev03-sex_ani01
    "Conner is still asleep as his beautiful girlfriend grinds her velvet lips against his cock."
    Jes "Ohhhh..."
    Jes "Baby, you feel so good. I've really missed this dick."
    "She rubs her clit against the underside of his cock, spreading her slick nectar along his shaft."
    JesT "He's so hard. I have to feel that big dick now!"
    hide d01ev03-sex_ani01

    if persistent.pov == 1:
        scene day1 ev03-54mpov with fade
        "He awakens to the sensation of her hot channel engulfing his upright cock."
        Con "Oh, Jessica, what are you…"

        scene day1 ev03-55mpov with fade
        Jes "Baby, I couldn't resist."

        scene day1 ev03-56animpov-0 with fade
        show d01ev03-sex_ani02mpov
        "Jessica cannot control herself. She slides down onto him, his hard cock spreading her delicate folds and stretching the tight channel of her pussy."
        Jes "MMmmmm! Oh, it's so good!"
        scene day1 ev03-56animpov-9
        hide d01ev03-sex_ani02mpov

    else:
        scene day1 ev03-54 with fade
        "He awakens to the sensation of her hot channel engulfing his upright cock."
        Con "Oh, Jessica, what are you…"

        scene day1 ev03-55 with fade
        Jes "Baby, I couldn't resist."

        scene day1 ev03-56ani-0 with fade
        show d01ev03-sex_ani02
        "Jessica cannot control herself. She slides down onto him, his hard cock spreading her delicate folds and stretching the tight channel of her pussy."
        Jes "MMmmmm! Oh, it's so good!"
        scene day1 ev03-56ani-9
        hide d01ev03-sex_ani02

    scene day1 ev03-57a with fade
    "Jessica slips her robe off her shoulders, fully revealing her luscious body to him."

    scene day1 ev03-58 with fade
    Con "So sexy..."
    JesT "I can feel his cock twitching inside me."

    scene day1 ev03-59 with fade
    play voices x_sex_1 fadein 2 loop
    "She begins to ride atop him, her hands exploring his muscular chest and her soft mounds heaving."
    Con "Oh, fuck, now this is a nice wakeup call."

    scene day1 ev03-60 with fade
    "Conner takes hold of Jessica's shapely hips and kneads her round ass."
    "He watches her body move atop him and soaks in the warmth of her velvet cunt swallowing his cock."
    Jes "I had to have this big cock!"
    Con "Oh, yeah? You like my big dick?"
    stop voices fadeout 1

    scene day1 ev03-61ani-00 with fade
    play voices x_sex_2 fadein 1 loop
    show d01ev03-sex_ani03
    "She throws back her head and rides urgently atop him. Her clutching channel sliding over every inch of his steely cock."
    "All their time apart melts away in her mind, Jessica feeling as he never left."
    Jes "Yesss! Fuck me! Don't hold back!"
    "Conner silently nods, his eyes glued to his beautiful girlfriend's body rising and falling."
    scene day1 ev03-61ani-19
    hide d01ev03-sex_ani03
    stop voices fadeout 1
    show d01ev03-sex_ani03b
    play voices x_sex_3 fadein 1 loop
    "He lets himself loose, slamming his cock upwards, impaling her tight pussy on his manhood and making her bounce atop him."
    "Their pleasure rises together. Jessica's shapely body responds to each of Conner's thrusts."
    "Jessica’s cries of pleasure fill the room, Conner groaning as he feels his own orgasm approaching."
    hide d01ev03-sex_ani03b

    if persistent.pov == 1:
        scene day1 ev03-62mpov with fade
    else:
        scene day1 ev03-62 with fade
    "Her hips twitch and she bucks atop him, her breasts shaking with the movement of her body."
    "Pleasure blossoms within the buxom woman, the joy of her boyfriend filling her swelling inside."
    stop voices fadeout 1

    scene day1 ev03-63 with fade
    play voices x_sex_4 fadein 1 loop
    Jes "I'm cumming! Oh, Conner, I’m cumming!"

    scene day1 ev03-64 with fade
    "He can feel her pussy squeezing him tightly and he cannot resist."
    Con "Oh, baby, I can't hold out any longer!"
    Jes "Cum inside me! Yesss!"
    stop voices fadeout 1
    play voices x_sex_5 fadein 1 loop
    "With a last roar, Conner explodes deep inside her!"
    JesT "I can feel it shooting his load inside me!"
    "Jessica rides atop him, draining every drop from his throbbing cock as her orgasm ripples through her creamy pussy."
    stop voices fadeout 1

    scene day1 ev03-65a with fade
    "Her cum-filled pussy makes soft, lewd sounds sliding over Conner's spent manhood."
    Jes "Oh, Conner, that was so hot…"

    scene day1 ev03-65b with fade
    "Jessica leans her soft body against him and kisses him, their tongues meeting in a moaning embrace."
    Con "You're telling me, baby."

    scene day1 ev03-66 with fade
    "Their pleasure spent, they collapse together on the bed."
    "Jessica can feel Conner's silky cum trickling out of her freshly-fucked folds."

    jump day01dressup

label day01dressup:

    if tempvar == 1:
        scene day1 ev03-67 with dissolve
    else:
        scene day1 ev03-37 with dissolve
    "They share a long kiss, bodies pressed together and hot with the flush of sex, languid in the afterglow of their pleasure."
    "Conner strokes a lock of Jessica's hair from her face and gazes deeply into her eyes."
    Con "What prompted that?"
    Jes "A little bit of good luck fun, I guess."
    Con "You don't need luck, baby, the paper is lucky to have you."
    Jes "I guess I just can't get enough of you now that you’re home. Sometimes I want to pinch you to be sure you're real."

    if tempvar == 1:
        scene day1 ev03-68
    else:
        scene day1 ev03-38
    Con "It feels like a dream sometimes."
    Con "Like I'm still there in Afghanistan."
    Jes "I know it's hard, honey, but the work you’re doing here is good."
    Con "Yeah, I know. If only Wounded Warriors United paid a little better…"
    Jes "We'll get by and I’ll break some big story and get a promotion."
    Jes "Until then… I'm happy with ramen and dates where we walk in the park."
    Con "Yeah?"
    Jes "Yeah, as long as I have you with me."
    Con "You keep waking me up like that and you'll have me forever!"

    if tempvar == 1:
        scene day1 ev03-69
    else:
        scene day1 ev03-39
    Jes "Haha, no promises, stud!"
    Jes "Now enough cuddling, I need to get ready for work."
    Con "Got your outfit all picked out?"
    Jes "You know I like to plan ahead."
    Jes "I've got something understated in mind, but that’ll still catch the eye. Classy, but pretty."
    if tempvar == 2:
        scene day1 ev03-80
        "She lifts herself from the bed and lets her robe slide down her shoulders."
    Con "Hey, you should wear that lucky necklace I got you when we went to Hawaii."
    Jes "Good idea, honey! It'll be like you’re right there with me all day."

    $ tempvar = 0

    scene day1 ev03-81a
    "Jessica climbs out of bed and crosses to the dresser where she left her necklace."

    scene day1 ev03-82
    "The beautiful gold heart hangs against the soft swell of her cleavage."

    scene day1 ev03-83
    "She models it nude for Conner."
    Con "So sexy. But you'd better get ready to go, babe."

    scene day1 ev03-84
    "Jessica realizes she barely has enough time to get to the office."
    Jes "Shit! You're right!"
    JesT "I still feel dirty from what we just did, but there's no time to for another shower."

    scene day1 ev03-85 with fade
    "She cleans up and put on her makeup as quickly as she can. She slips into her panties and buckles her bra as Conner watches from the bed."
    "Her hair is another story. It's still damp from the shower and she has to blow dry it while she is doing her lipstick."
    "Conner is amused by his beautiful girlfriend's ambidextrous rush to make herself ready."
    Con "I don't know how you girls manage that."
    Jes "We {b}women{/b} get used to it."
    Con "Well practice makes perfect. You look smoking hot."

    scene day1 ev03-86 with fade
    "Jessica slips her feet into her heels."
    Jes "Not the way I was planning to start my day."
    Con "Knock ‘em dead, baby."

    scene day1 ev03-87
    "Conner, still unashamedly naked, stands and embraces Jessica."

    scene day1 ev03-88
    "She shoves him playfully away before he makes a mess of her office attire."
    Jes "No, you've had enough of me this morning."
    Con "I’ll never have enough of you, baby."

    scene day1 ev03-89
    Jes "See you tonight!"
    Con "Right. We have to celebrate your first day!"
    Jes "No getting drunk though."
    Con "A little bit drunk."
    "They share a kiss and he sees her out the door."
    "A last glance at the time on her phone and she is jolted with adrenaline."
    JesT "I am going to have to drive like hell to get there on time."

    scene day1 ev04-01 with fade
    "Jessica rushes out of the apartment. As she is heading outside, she almost literally bumps into an attractive couple exiting the apartment next door to hers."
    "She greets HEATHER STEEL and CHRISTIAN STEEL with a hurried smile."
    Heath "Oh, Jessica! You look so beautiful today!"
    Chris "Very nice."
    Jes "Thanks! First day on the job and I'm trying to make a good impression."
    Heath "If they have eyes, they're going to love you."
    JesT "Heather and Christian are sweet, but they both give me funny looks every time I talk to them."

    scene day1 ev04-02
    "It's no different today. Heather is looking Jessica over and Christian is doing some outright ogling."
    Chris "Would you like to join us for breakfast?"
    Heath "Invite the beau! The war hero!"
    Jes "I'll have to take a raincheck on that. I'm in a rush."
    Heath "We'll hold you to that!"
    Heath "Have a nice day, Jess. See you tomorrow for the jog."
    Jes "Thanks. Bye!"
    "Jessica brushes past them and hurries to her scooter."

    scene day1 ev04-03a with fade
    Jes "Okay, little fireball. Let's do this."
    play sound vespa_start_drive
    pause 3

    scene day1 ev04-03b with fade
    "She speeds off into the downtown traffic, weaving through tight spots and doing everything she can not to be late."
    stop sound fadeout 1

    scene day1 ev04-04a with fade
    play sound city_street_with_vespa fadein 1 loop
    "Jessica drives past a familiar newsstand. The elderly man behind the counter is MR. PARKER, an old acquaintance and ex-reporter Jessica respects deeply."
    "He sees Jessica on her scooter and waves to her."
    Jes "Hey, Mr. Parker!"
    JesT "He has been in this part of the neighborhood for as long as I can remember."

    scene day1 ev04-04b
    JesT "Sometimes I think he lives inside that little stand when the shutters it for the night."
    Parker "Lookin' forward to your first byline, Little Miss Reporter!"
    Jes "Probably not on my first day!"
    Parker "Do your best and it may as well happen!"
    "Jessica smiles back at him and continues her ride."
    stop sound fadeout 1

    scene day1 ev04-05 with fade
    play sound city_ambience_1 fadein 1 loop
    "She rides past the newsstand and continues downtown to the towering edifice of the New Port Gazette."
    JesT "Well, girl, let's climb this mountain."
    "Without wasting any more time she rushes into the lobby and the elevators."
    stop sound fadeout 1

    scene day1 ev04-06 with fade
    "A young, attractive woman with dark hair sits behind the reception desk of the 14th floor."
    Jes "Hi, um, Jessica O'Neil."
    Rec "I know, Miss O’Neil. Head on through to the offices."
    Jes "I'm not late, am I?"
    Rec "..."
    JesT "Oh, no! She just made a face when I asked that."
    JesT "I am late! On my first day!"
    Rec "Mr. Birch likes to start the Monday meetings early."
    Rec "You can go on back to the conference room, the last door on the left."

    scene day1 ev05-01a with fade
    "Jessica opens the door and sees the executive editor of the New Port Gazette, Mr. Birch, speaking to few journalists."
    "She nervously enters the conference room, trying not to disturb them too much."
    "A voluptuous middle-aged Latina (ROSA JIMENEZ), a handsome early middle-aged black man (DUNCAN ADAMS),"
    "a beautiful young woman who looks to be about the same age as Jessica (EVE BEAULIEU), and a pudgy young man wearing glasses (JERRY KRUGER) are all listening to MR. BIRCH speak."

    scene day1 ev05-01b
    "Mr. Birch gives Jessica the gimlet eye as she takes a seat at the table."
    "A few of the other reporters glance in her direction."
    JesT "Oh god! This is not how I wanted to make my entrance."

    scene day1 ev05-02a
    "Before she can apologize, Mr. Birch continues with what he was saying."
    Birch "I'm not interested in the criminal aspect, Duncan."
    Birch "That's second page, below the fold stuff."

    scene day1 ev05-02b
    Birch "I am more interested in the vigilante aspect."
    Birch "There is mystery there - \"Who is behind the mask?\""

    scene day1 ev05-03
    Dun "A lunatic, who is going to get himself killed."
    Dun "That's who. Isn't it obvious?"
    JesT "They're taking about that guy going around beating up criminals. He showed up a month ago, stopping a warehouse heist. The police found the robbers tied and bloodied inside the place."
    JesT "He's been seen a couple more times preventing small crime and helping people. Ever since then he has become the talk of the city and the media are all too happy to embrace the story."
    JesT "It does sound kind of dangerous. Even if this guy is doing good things, he's putting his life on the line."

    scene day1 ev05-04
    Rosa "I think he's cute."
    Birch "Cute?"
    Birch "How can you tell? We have blurry pictures from security cameras and one screen grab from a cell phone video."
    "Jessica's eyes turn to the older woman on the other side of the table, taking in the lady's relaxed demeanor and attentive eyes."

    scene day1 ev05-05
    Rosa "Well, this town needs a guy like that - one who can bust heads."
    Birch "An armed vigilante beating people up is great..."
    Birch "For us. For the news business."
    Birch "For New Port City? I don't think so."

    scene day1 ev05-06a
    Dun "I can follow the crime in the city, I can't follow one masked vigilante."
    Dun "If he shows up, I can try to tell the story you want me to tell."
    Dun "But this tabloid crap, I don't like it."

    scene day1 ev05-06b
    Birch "You’re not paid to like it, Duncan."
    JesT "Do these two usually go at it like this? Are most meetings going to go this way?"
    Dun "This crimewave is the worst in 20 years. Someone or something is behind this. The vigilante is just a by-product."
    Birch "You're not going all chemtrails on me, are you Duncan?"
    Dun "Whatever it is, we'll get to the bottom of it by digging into the crime in the city. Not by following this guy's \"heroic\" adventures."

    scene day1 ev05-07
    Birch "Huh. What about you, young lady?"
    "Mr. Birch seems to be looking at Jessica."
    "Before she can answer, the other young woman in the room leans forward and speaks with a pronounced French accent."

    scene day1 ev05-08a
    Eve "If the police addresses the crime, there is no need for a vigilante."

    scene day1 ev05-08b with dissolve
    Eve "I think there is corruption, inside the police force. They do not do their jobs."
    JesT "Wow. That... is one sexy accent."
    Dun "That's the sort of accusation that is going to burn a lot of my sources."
    Birch "Right. Well, the cops are dirty as mud wrestlin' pigs, but I can’t put that on the front page with this maniac running around."
    JesT "She's right, though. If things are so bad that we need a masked nut running around doing the police's job for them, something is definitely wrong with our law enforcement."

    scene day1 ev05-09a
    "Mr. Birch looks directly at Jessica."
    Birch "How about you, miss O'Neil?"
    Birch "Dazzle me with your insight. Who do you side with on this one?"

    scene day1 ev05-09b
    JesT "Great! My first words and I'm gonna piss someone off."
    JesT "Who should I agree with?"

    menu:
        "Mr. Birch (The vigilante is the story)":
            $ relBirch += 1
            $ relDuncan -= 1
            $ choices.append("d01agreeBirch")
            scene day1 ev05-09c with dissolve
            Jes "Well, every city has crime, right? Even crimewaves. But a masked vigilante is something new."
            Dun "It's called Batman. Or Daredevil. People see it on the screen and then go out and imitate it."
            Jes "I've heard of it happening before, but those people are usually disturbed, living out fantasies. This guy… he's actually stopping criminals."
            Jes "People want to know him. Who is he? How long has he been here? What motivates him to risk his life?"
            Jes "If we can tell his story and inspire people to be better, then that's what we should do."
            scene day1 ev05-09f
            Birch "Watch yourself, Duncan. I may give her your office soon."

        "Duncan (The crimewave is unusual)":
            $ relDuncan += 1
            $ relBirch -= 1
            $ choices.append("d01agreeDuncan")
            scene day1 ev05-09c with dissolve
            Jes "Um, there is something unusual about the crime in the city."
            Dun "See?"
            Birch "What do you mean, Miss O'Neil?"
            Jes "A mix of violent street level crime and these big heists. But domestic crime is unchanged."
            scene day1 ev05-09e
            Dun "Yeah, I saw the pattern too."
            Birch "You're wrong. Both of you. Part of my job is knowing when to tell my reporters they're wrong. And part of their job is listening to me."
            "Mr. Birch is angry, but Duncan favors Jessica with the slightest nod of acknowledgement."

        "Eve (The police is dirty)":
            $ relEve += 1
            $ choices.append("d01agreeEve")
            scene day1 ev05-09c with dissolve
            Jes "A crimewave like this doesn't just start in a vacuum."
            Jes "A lack of police attention and political willpower to confront this problem is what allowed it to happen. And there are some reports of the police acting unusually slow."
            Dun "Maybe you and Eve are right, but it's a story that is difficult to follow."
            Birch "And one we don't have the resources to pursue at this time."
            scene day1 ev05-09d with dissolve
            Jes "Sure. It's my first day. You just asked my opinion."
            Birch "Right. And now I have it."
            "Jessica smiles nervously and glances around the table."
            "Eve meets her gaze and mouths the words \"Thank you.\""

    scene day1 ev05-10a with fade
    "The meeting continues and Mr. Birch moves on to assigning various stories to the reporters."
    "Jessica notices that Rosa seems to work the City Hall beat and Eve is helping her."
    "Duncan reluctantly agrees to pursue the vigilante story among several other stories he is working on."
    JesT "What about my assignment?"
    Birch "Anything else? Rosa?"
    Rosa "We had that job shadow kid from the high school coming Wednesday through Friday."
    Birch "Ugh. Three days of him?"
    Rosa "You agreed to it."
    Birch "I blame you for not stopping me."
    Dun "Don't look at me! I don’t have time for a kid!"
    Birch "You handle it, Rosa."
    Rosa "Got it."

    scene day1 ev05-10b
    Jes "Um, Mr. Birch…"
    Birch "Oh, right. You need an assignment."
    Jes "Yes, thank you."
    Birch "Rosa will show you around the office and figure out something for you to do today. Once you're settled in, come see me."
    Jes "Yes, of course, thank you for this opportunity."
    Birch "I appreciate the positive attitude. I'll try not to crush it out of you too quickly."

    scene day1 ev05-11 with fade
    "The meeting ends and Jessica follows Rosa to the offices for a tour."
    Rosa "Don't let Mr. Birch intimidate you. Deep down, he’s a softy."
    Jes "He reminds me of my grandfather."
    Rosa "Is that good?"
    Jes "No. He was the \"go get my belt\" type of grandpa."
    Rosa "Well, he hasn't hit anyone. Although he has come close to blows with Duncan before."
    Jes "Yeah, I noticed some tension during the briefing."
    Rosa "You'll get used to it, don’t worry."

    scene day1 ev05-12
    Rosa "Duncan will want to talk to you when we get you settled. His office is right over there."
    "Rosa points to Duncan's closed office door and enters the work area."

    scene day1 ev05-13
    Rosa "Eve is sitting here, I'm across the way right there."
    Rosa "As you can see, we have plenty of spare room here."
    Rosa "Few colleagues got axed due to budget cuts and the rest were transferred to national."
    Rosa "Local investigations are not in high demand, what with all the material coming from DC lately."
    Rosa "Thankfully, the new owners decided to get us some manpower. Hence, you and Eve."

    scene day1 ev05-14a
    "They approach a small cubicle, identical to the others. There isn't much room and the desk is already piled with papers."
    Rosa "And here is your desk. What do you think? Wonderful, right?"
    Jes "It's… good."
    Rosa "I’m just messing with you. I know it’s a little small."
    Jes "No, it really is fine. And I'll work hard to get an upgrade. Maybe two cubicles!"
    "Rosa gave a chuckle, nodding."

    scene day1 ev05-14b
    Rosa "Hmmmm. You're not set up on the computer, right?"
    Jes "No, I just arrived. Late, on my first day..."
    Rosa "Don't worry about it. Let me see if Jerry is still here, he’ll give us a hand."
    Jes "Is he the IT guy?"
    Rosa "Oh, I wish. We outsource all that to some company in India. There are barely any tech guys left in the whole building."
    Rosa "Jerry is from the new administration. That's why he is upstairs on the management level. But he is good with computers and helps out with stuff."

    scene day1 ev05-15
    "Rosa departs. While she is gone, Eve approaches confidently."

    if "d01agreeEve" in choices:
        Eve "Thank you for agreeing with me in there."
        Jes "Ah, you seemed right about it."
        Eve "Oui, but you stuck your neck out for me. So I appreciate it."

    Eve "Jessica O'Neil, right?"
    Jes "All me."

    scene day1 ev05-16
    "Eve offers Jessica her hand."
    Eve "Eve Beaulieu."
    Jes "A pleasure to meet you, Eve."

    scene day1 ev05-16b
    Eve "I would welcome you here, only… it seems odd for me. I am new also."
    Jes "How new?"
    Eve "This is my second week."
    Jes "Ah."
    JesT "They told me during the interviewing process they had narrowed it down to two people. They must have hired us both."
    JesT "What does that mean for my job here?"

    scene day1 ev05-17
    Eve "We must be on our toes. I am thinking we maybe compete for the same job."
    JesT "That's great."
    Jes "Thanks for the heads up, Eve."
    Eve "Is only fair. I will win and keep this job."

    scene day1 ev05-18
    "Eve turns and struts back to her desk. She has all the confidence of a runway model."
    JesT "Why couldn't she at least be dumpy looking?"

    scene day1 ev05-19 with fade
    "As if on cue, Rosa returns with the dumpiest-looking man in the office."
    "Jerry fidgets nervously and tries to smile."
    Jes "You must be Jerry."
    Jer "Yeah, uh, pleased to meet you, uh, Miss O'Neil."
    Jes "Just Jessica, please. Can you help me get on the computer?"
    Jer "Y-yeah, sure. As long as you're in the system, I can figure it out."

    scene day1 ev05-20
    "Jerry sits down at Jessica's desk and begins opening windows and clicking through settings faster than she can understand."
    Rosa "I'll leave you two to it. When you’re set up, go knock on Duncan’s door. He’ll want to give you the new reporter talk."
    Jes "Thanks for showing me around."

    scene day1 ev05-21
    "Rosa departs. Jessica watches Jerry working on the computer for a few minutes, but quickly grows bored."
    Jes "Hey, Jerry, how long do you think this is going to take?"
    Jer "Um, no more than fifteen minutes."
    "Jessica glances at Eve, already diligently at work on something."
    Jes "You can handle this without me, right?"
    Jer "Sure thing, Jessica. I'll leave a note on your desk with the info."
    Jes "Thanks, you’re a peach."

    scene day1 ev05-22
    "Jerry goes a bit red in the face at the compliment. He smiles and watches Jessica's shapely bottom as she walks away."

    scene day1 ev05-23 with fade
    "Jessica heads over to Duncan's office and knocks on the door."
    Dun "Come on in."

    scene day1 ev06-01
    "Duncan has the look of someone who is always in the middle of something and can only be interrupted."
    "He motions to a chair as he continues reading his computer."
    JesT "This guy scared the crap out of me during the interviews."
    JesT "He seems like the sort of journalist I idolized when I was in journalism school."
    JesT "Am I up to his level?"

    scene day1 ev06-02a
    if "d01agreeDuncan" in choices:
        Dun "It was nice to see someone else standing up to Birch."
        Dun "I hope you weren't trying to butter me up."
        Jes "Your argument was the most persuasive. Crime is the story."
        Dun "Someone is behind what is happening in this city."
        Dun "I am convinced that there is an agenda here to create disruptions with street level crimes to allow for high-end theft."
        Dun "The pattern is there in the numbers and our job needs to be to figure out who the person is and why they are doing it."
        Dun "Not get bogged down in Birch's vigilante story."
        "He remained silent for a few moments before changing the subject."

    Dun "As you know, I'm Duncan Adams. Senior reporter, responsible for the local investigative branch of New Port Gazette. And you'll be working under my direct supervision."
    Jes "It’s a privilege, sir."

    scene day1 ev06-02b
    Dun "As you can see, the team is small. But we're focused, New Port and the immediate surroundings."
    Dun "If you get your hands on something beyond that area it'll most probably be taken from you and assigned to national."
    Dun "Not because they are better than you, but because we want you concentrated on the issues of the city."
    Jes "I understand."
    Dun "..."

    scene day1 ev06-02a
    Dun "You did well for a couple of years in the newsroom at channel 9."
    Dun "I asked around. I know you worked on that story on Councilman Harding."
    Jes "I did some legwork, knocked on doors, I wasn’t managing the story."
    Dun "So why print? You were on a TV track, you have the looks for it. Why move to print?"
    Jes "I felt like print is where the real stories were being told."
    Dun "Huh."
    JesT "Uh oh, I said something wrong."

    scene day1 ev06-03
    Dun "We’re not in the business of storytelling, Miss O'Neil."
    Dun "If that’s what you want to do, you should start a blog or something. Or make a documentary."
    Dun "We’re in the truth business."
    Jes "Right, I know, I just--"
    Dun "Journalism programs are drilling multimedia and storytelling into the heads of all you journalism students."
    Dun "It’s bullshit. Leave that to the production team."
    Dun "We get the truth. We tell the truth."
    Jes "Got it."
    Dun "And sometimes the truth is not as entertaining as the fiction and we have to work around the editor to do it, do you understand that?"
    Jes "I-I think so. You have to get the truth out there even if he wants to make it about something else."
    Dun "Exactly."
    Jes "So it’s about the crime, even if you write the piece about the vigilante."
    Dun "But leave people wondering about the crime."
    Jes "Smart."
    Dun "Don’t try to flatter me."

    scene day1 ev06-02a
    Dun "You’ve got a long way to go, but maybe we can make it work."
    Jes "I would love to dig in."
    Dun "Today you are going to dig into this."

    scene day1 ev06-04
    "Duncan hands Jessica a thumb drive."
    Jes "Whatever you need."
    Dun "That’s for Rosa. You are going to be transcribing interviews for a story she is doing on the new stadium project."
    JesT "Bullshit! That’s intern work."
    Jes "I, um, sure."

    scene day1 ev06-05 with fade
    "Jessica returns to her desk to find a note from Jerry. Her login is JONEIL and her password is FOXY0N3."
    Jes "Real cute."
    JesT "I’ll let it slide since he was helping me out."

    scene day1 ev06-06
    "She puts on her earbuds, plugs the thumb drive into the computer, and gets to work transcribing audio interviews conducted by Rosa."
    play sound keyboard_typing_1 loop
    pause 1

    scene day1 ev06-07 with fade
    "It’s boring, tedious work. She’s relieved when Rosa stops by her cubicle."
    stop sound
    Rosa "Hey, Mr. Birch is ready to see you."
    Jes "Should I be afraid?"
    Rosa "Nah. Don’t let him scare you."

    scene day1 ev06-08
    "Rosa surprises Jessica with a pat on the ass as Jessica walks past."
    Rosa "You’ll knock him out."
    Jes "Thanks..."

    scene day1 ev06-09 with fade
    "Jessica walks upstairs to the management floor of the office. She is surprised to see Jerry working in a big office next to Mr. Birch. He waves to her and she waves back."
    "She hurries past, avoiding any conversation as she makes a beeline for Mr. Birch’s office."

    scene day1 ev06-10 with fade
    "He’s waiting for her."
    Birch "Miss O’Neil, come on in. Close the door and have a seat."

    scene day1 ev06-11
    Birch "I hope Rosa showed you the ropes and Duncan wasn’t too hard on you."
    Jes "They were both very accommodating, Sir. I can’t wait to start working with them."
    if "d01agreeBirch" in choices:
        Birch "You’re off to a good start, Jessica."
        Birch "You saw things my way back there in that meeting."
        Birch "And I can use more voices on my side in meetings like that."
        Jes "I think you were right, sir. I just spoke my mind."
        Birch "Let’s stay focused on that first part. The \"I think you were right\" part."
        Jes "Okay..."
        Birch "Speaking your mind is overrated."

    scene day1 ev06-12
    "Mr. Birch stands up from his desk and walks around to her side."
    if persistent.pov == 1:
        scene day1 ev06-12mpov
    "Jessica can feel his eyes on her body."
    JesT "He’s old enough to be my father. Maybe even my grandfather. And he’s looking at me like a piece of meat."
    if persistent.pov == 1:
        scene day1 ev06-12
    Birch "Young lady, I’m sure those professors and Duncan and whatever you were doing at Channel 9 put a lot of nonsense into your head about how important journalism is."
    Birch "But you’re at a newspaper now."
    Birch "This is a business and we’re barely clinging to relevance."
    Jes "I know the Internet has been hard on the newspapers."
    Birch "Yes. So my job as the editor here is to balance Duncan’s needs to win another Pulitzer with the owner’s need to make money."
    Birch "And that has gotten very difficult over the years."

    scene day1 ev06-13
    Birch "In fact, you and Miss Beaulieu are the first new hires we’ve had in over a year."
    JesT "Here it comes…"
    Birch "And it’s going to be hard to justify two new reporters in the budget."
    Birch "I want to, mind you. Eve is very… well, she’s a talent. As are you."
    Jes "Thank you, sir."
    Birch "So I will give you the same advice I gave her: when I tell you something as the editor-in-chief, treat it like the word of god, because it comes from the owner as well."
    Jes "I will bend over backwards for you, sir."

    scene day1 ev06-14
    Birch "Oh?"
    "A smirk spreads across Mr. Birch’s face."
    JesT "Oh, no! What I just said sounded dirty."
    Birch "Bending over forward is good enough, Miss O’Neil."
    JesT "Did he just…?"
    JesT "The way he’s staring at me, he definitely did."
    JesT "I need to think very carefully about how to react to this."

    menu:
        "Laugh at the innuendo":
            scene day1 ev06-16
            Jes "Ha ha ha!"
            Birch "It’s good to have someone around with a sense of humor."
            Birch "Rosa and Duncan never laugh at my jokes anymore."
            Jes "I try not to take anything too seriously."
            Birch "Anything?"
            Jes "Uh, other than the job."

        "Make your own dirty joke":
            $ relBirch += 1
            $ slut += 1
            scene day1 ev06-15
            Jes "Actually, I prefer to do my work from on top."
            Birch "Oh! Ha ha ha!"
            Birch "I like that!"
            Birch "Well, with that sort of attitude you may well go to the very top."

    scene day1 ev06-13
    Birch "The main thing I want you to know today, Miss O’Neil, is that you have my confidence and the hope that you will prove yourself a capable reporter."
    Jes "Thank you, Mr. Birch. This is a great opportunity and I will not let you down."
    Birch "Good. I’ll let you get back to work, Miss O’Neil. I’m sure Duncan and Rosa had already found something for you to do."

    scene day1 ev06-17a with fade
    "Jessica returns to her cubicle, her heart still pounding from her meeting with Mr. Birch."
    play sound keyboard_typing_1 loop
    "She tries to put it out of her mind as she returns to transcribing Rosa’s interviews."
    "On the audio, Rosa seems to be prying into a deal for a new baseball stadium in New Port City."
    "Her questions lead Jessica to believe that some people on the council are receiving kickbacks from an unknown company for approving the stadium deal."
    JesT "*sigh* I can’t believe this is what they have me doing on my first day. I guess I shouldn’t be surprised, but it’s still kind of frustrating."

    scene day1 ev06-17b
    JesT "Still, I have to admit, I do kind of like listening to Rosa. She’s a little fiery, and seems pretty good at drawing the truth from the people she’s talking to."
    JesT "Maybe this will be good for me. A little boring, but definitely good material if I want to interview people the way this woman does."
    JesT "I wonder if that was the point of giving me this assignment. Or was it just to give the new girl the crap work? Probably the latter."
    JesT "Oh well. I should just concentrate and keep going. I’ve got quite a few of these to finish."
    "She still has hours more of transcription to complete by the time 5 o’clock rolls around."
    stop sound

    scene day1 ev06-18 with fade
    Rosa "Hey, Jessica."
    Jes "Oh. Hey, Rosa. How’s it going?"
    Rosa "You’re not staying here all night and working on that."
    Rosa "Come get a drink."
    Jes "Oh, thank you, but I can’t."
    Jes "I have to go home to my boyfriend."
    Rosa "I understand. You'll tell me about him tomorrow. At lunch."
    Jes "It’s a date!"
    JesT "It’s a date. What am I? Twelve?"

    scene day1 ev07-01 with fade
    "Jessica rides her scooter home and returns to her apartment. She isn’t surprised that Conner isn’t home from work yet."
    JesT "Ah, Conner, where are you? I could use your magic fingers on my shoulders right now."

    scene day1 ev07-02 with fade
    "She changes into a more comfortable outfit and pours a glass of wine."
    JesT "I guess I’ll relax until he gets home. See if anything good is on."

    scene day1 ev07-03 with fade
    "She sits down to watch some TV, but nothing’s capturing her attention. Her mind too busy with the day’s events."

    scene day1 ev07-04 with fade
    "Some time passes and she receives a call from her sister, Laura."
    Lau "Hey, sis, how did the first day go?"
    Jes "Rough. Boring. Good? I’m not sure."
    Lau "You’re a bad reporter if that’s the best you can do."
    Jes "Don’t say that. I feel like a bad reporter."
    Jes "I spent most of my day transcribing interviews and occasionally looking over at the girl who is going to get my job."
    Lau "Is she good looking?"
    Jes "Uhh, yes, she is."
    Lau "I hate her already."
    Jes "Thanks…"
    Lau "Cheer up, it’s your first day. It’ll get better."
    Lau "Listen, mom and I are going to be in town for the weekend. We should hang out and you can tell me all about it."

    scene day1 ev07-05
    Jes "A family therapy... I cannot wait."
    Jes "Tell me, how is our lovely mother?"
    Lau "She’s good, you know mom, lots of work and no fun."
    Jes "Ahh…"
    Lau "Actually, I think she’s dating someone."
    Jes "You think?"
    Lau "You know how she is - she never tells. I think we were too harsh last time."
    Jes "With Lurch? Yeah, right! If anything, we weren’t harsh enough. She dated that asshole for a year before opening her eyes."
    Lau "You know what? If this guy is not decent, I’ll find her someone myself."
    Jes "Hah, because you’re so good at finding men…"
    Lau "Hey, don’t be rude! I’m waiting for the right guy."
    Lau "I’ll find her someone good to take make her happy. And he’s gonna be cute too, not like Lurch."
    Lau "And speaking of cute, how does it feel to have your boyfriend back?"
    Jes "Good. Not that we’ve seen much of each other. He came late last night and now I’m waiting for him to come back from work."
    Lau "The work you told me will pay him like crap?"
    Jes "It’s a charity. He’s doing good things for the veterans."
    Jes "And don’t you dare tell him we talked about this sort of thing while he was deployed."
    Lau "Our secret. See you this weekend!"
    Jes "Bye."

    scene day1 ev07-06 with fade
    "Jessica hangs up and looks at the time on her phone."
    JesT "Almost eight. Where is he? And why hasn't he called?"
    JesT "Well, I'm not calling him either! I should grab something to eat."

    scene day1 ev07-07 with fade
    "Jessica makes herself a quick dinner, heaving a sigh as the time passes by. Conner nowhere to be found."
    JesT "And here I thought I'm done eating alone..."

    scene day1 ev07-08 with fade
    "As the day comes to a close, Jessica waits patiently for her boyfriend to arrive."
    "The wine helps to dull both the frustration and the hurt she feels at having Conner standing her up."

    scene day1 ev07-09
    "Eventually, her eyes close and her hand slips between her legs, the wine drawing out the young woman’s need for sexual release."
    JesT "Drinking always makes me horny. Where are you, Conner?"
    "She is reminded of the long months she spent without the man she loves, satisfying her own urges whenever they struck, no matter how much she desired to feel her boyfriend’s caress."
    JesT "*sigh* Well, I have another busy day tomorrow, so I guess I’ll turn in, since it’s looking like you’re not getting home any time soon."

    scene day1 ev07-10 with fade
    "Unwilling to wait any longer for Conner, Jessica heads off to bed."
    "She strips down to her panties before climbing under the covers."

    scene day1 ev07-11 with fade
    "She is restless, tossing and turning and watching the clock creep from nine to ten. Her body burning with desire."

    scene day1 ev07-12
    "Jessica’s hand slips between her legs and inside her panties once more, her fingers attempting to give her the satisfaction she craves."
    Jes "Ooooh."
    "Her fingers rub swiftly over her sensitive clit, pulling soft moans of bliss from the stressed and eager young woman."
    "The pleasure is wonderful, but not quite what she’d hoped for. All day she’d been anxiously hoping she’d have a long, rigid phallus thrusting between her legs."
    JesT "Well, if Conner’s dick won’t fuck me, I know someone who will."

    scene day1 ev07-13
    "Jessica reaches into her nightstand and takes out her vibrator."
    "It’s well-worn from Conner’s time deployed in Afghanistan."

    scene day1 ev07-14
    Jes "I’d hoped to retire you. But looks like you need to put me to sleep tonight."

    if persistent.pov == 2:
        scene day1 ev07-15fpov
    else:
        scene day1 ev07-15
    play voices x_moaning_1 loop
    "Jessica slides her panties down her shapely thighs and strokes herself with her fingers."
    "She tries to picture Conner’s hand there."
    "Her fingers move against the warm softness of her sex as she imagines Conner exploring her hot flower with his touch."
    if persistent.pov == 2:
        scene day1 ev07-16fpov
    else:
        scene day1 ev07-16
    "She switches on the vibrator and presses it against her clit."
    Jes "Ohhhhh… yes… Conner."
    "She bucks her hips and presses the buzzing vibe to her hard clit."
    "Her breasts quiver with tremors of her building ecstasy."
    Jes "Mmmmmmm!"
    "Jessica craves more stimulation."
    "Her body aches to be touched, so she touches herself, her hands playing with her soft breasts."
    if persistent.pov == 2:
        scene day1 ev07-17fpov with dissolve
    else:
        scene day1 ev07-17 with dissolve
    "Her fingers plucking at her sensitive nipple."
    "She pinches it so hard it hurts, sending hot jolts to her clit."
    "She keeps the vibrator pressed against her throbbing bud."
    "But she needs more…"
    stop voices fadeout 1

    menu:
        "Fuck yourself with the vibrator":
            $ choices.append("d01casualVibe")
            "Playing with her clit isn’t enough to satisfy her tonight."
            "Jessica needs to be fucked. And without a man around she is going to have to take matters into her own hand."
            jump day01eveningvibe

        "Fuck yourself and play with your ass":
            $ choices.append("d01naughtyVibe")
            $ kink += 1
            "Jessica craves much more than a vibrator against her clit."
            jump day01eveningvibekinky

label day01eveningvibe:

    if persistent.pov == 2:
        scene day1 ev07-18fpov with fade
    else:
        scene day1 ev07-18 with fade
    play voices x_moaning_1 loop
    "She switches off the vibrator and teases open her slick folds with the tapered tip."
    Jes "Oh god, yes. Put it inside me…"

    scene day1 ev07-19ani-0
    "She thrusts the toy into her aching channel, picturing Conner kneeling between her legs."
    Jes "Conner, baby, fuck me. Fuck me, sweetie."

    show d01ev07-vibe_ani01
    "She plunges the vibrator in and out of her tight pussy."
    "Her eyes close, the sound of her heavy breathing filling the room along with her growing moans of ecstasy."
    "The joys she’d hoped Conner would bring her begin to fill her soaking womanhood, but she hardly thinks about it. The pleasure is too great."
    Jes "Oh god, that’s good. Oh, so good."
    "Soon, the bedroom fills with her cries of joy, the pleasure quickly building within her cunt."
    Jes "Ahhhh! Yesss! Conner, fuck me! Fuck me harder!"
    "She presses the vibrator into her clutching cunt to the hilt and switches it on."
    Jes "Ahhhhhhhhhhhh!"
    Jes "I’m cumming! Fuck me, Conner! Fuck me!"
    "In her mind’s eye, she sees Conner’s body as it thrusts against her own. She hears his own grunts of pleasure, and feels him pushing his chest into hers."
    scene day1 ev07-19ani-9
    hide d01ev07-vibe_ani01
    stop voices fadeout 1

    scene day1 ev07-20
    play voices x_moaning_2
    "The vibrator buzzing deep inside her sends rippling shockwaves of ecstasy through her body."
    "Jessica arches on the bed, fucking herself with forceful strokes of the vibrator."
    "Each time, the whirr is muffled by the spasming depths of her pussy."
    "Orgasmic bliss fills the young woman, her sex convulsing as ecstasy flows up her body, washing over every inch of her flesh."
    "Jessica’s mouth hangs open in a wordless cry of pleasure as she cums against the buzzing toy."
    "Her mind goes blank, nothing remaining for her but the blissful world of sexual nirvana."
    "Soon enough though, it fades. The young lady collapsing back to the bed."
    stop voices fadeout 1

    scene day1 ev07-21
    "Spent at last, Jessica switches off the vibrator and places it on her tummy, enjoying the warmth coming from it."

    scene day1 ev07-27
    "Finally feeling satisfied, she wearily pulls the blanket over her naked body and quickly falls asleep."

    jump day02

label day01eveningvibekinky:

    scene day1 ev07-22
    "She turns onto her hands and knees, her plump ass lifted into the air behind her."
    "As she shifts, her fantasies become increasingly kinky."
    "Oh, Conner, fuck me…"
    play voices x_moaning_1 loop
    "She switches off the vibrator and plays the tip against her delicate folds."
    "She pictures Conner kneeling behind her and teasing his cock at her pussy."

    scene day1 ev07-23a
    "As she does, she buries her face in the pillows and reaches back to run the fingers of her other hand down her crack."
    Jes "Mmmmmmmm!"

    scene day1 ev07-23b
    "She pictures her neighbor, Heather Steel, kneeling beside Conner."
    "In this steamy fantasy, the beautiful woman is kissing Conner as her fingers tease the clenched rim of Jessica’s asshole."
    Jes "Ohhhhh, Heather! What are you doing?"
    "Jessica pushes the dildo into her aching cunt and gently pushes a fingertip from her other hand into her asshole."
    Jes "Oh god, Heather! You’re playing with my ass!"
    Jes "Yessss, fuck me while she fingers my ass, Conner!"

    scene day1 ev07-25ani-0
    show d01ev07-vibe_ani02
    "Jessica’s thrusting finger becomes Heather’s and the vibrator is Conner’s cock."
    "She thrusts back against this fantasy of her boyfriend and switches the vibrator back on."
    "The pleasure is instantaneous."
    Jes "Ohhhh my god!"
    "It pounds through her fluttering pussy."
    stop voices fadeout 1
    play voices x_moaning_2
    "She can feel her orgasmic ecstasy clenching against the finger she is thrusting into her ass."
    Jes "Ohhhh my god, I’m cumming!"
    "Jessica imagines the beautiful neighbor moaning in reply and begins to urgently fuck her own ass with her finger."
    Jes "Yes! Yes! Cum for me, Conner! Cum inside me!"
    scene day1 ev07-25ani-9
    hide d01ev07-vibe_ani02
    "She imagines Conner unleashing his cum deep inside her."

    scene day1 ev07-26
    "Unfortunately, the vibrator can’t unload, but in her fantasy, she pictures Conner grabbing her ass with both hands and slamming his hardness deep into her pussy."
    Jes "Ohhhh, I can feel it!"
    "She almost can in the kinky depths of her imagination."
    stop voices fadeout 1

    scene day1 ev07-27 with fade
    "Spent at last, Jessica switches off the vibrator and places it on the nightstand."
    "Finally feeling satisfied, she wearily pulls the blanket over her naked body and quickly falls asleep."

    jump day02
