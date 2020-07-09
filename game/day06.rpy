label day06:

    scene day6 with fade
    "DAY 6"

    scene day6 ev01-01a with fade
    "Pleasant yet strange dreams of churches and coworkers quickly fade away from Jessica's mind at the touch of another."
    Jes "Mmm."
    Con "Hey, sweetie."
    Jes "Hmm? Conner?"
    Con "Yeah. Morning, Jess."

    scene day6 ev01-01b with dissolve
    "Her eyes open as she turns to Conner."
    Jes "Hey, you."
    Con "Hey. How are you feeling?"
    Jes "Good. I'm good."

    if "d05noConner" not in choices:
        "The sight of her lovely boyfriend brings back thoughts of her the previous night."
        Jes "Really good after last night."

    "Jessica notices that Conner is dressed. Her brow furrows in confusion."
    Jes "What's up? You going somewhere?"

    scene day6 ev01-02
    Con "I have to go out for a few hours. I need to take care of a few things."
    Jes "You're heading into work on a Saturday? Why?"
    "He shrugs, a brief flash of annoyance passing through Jessica's chest."
    Con "There's a lot going on, and unfortunately they're understaffed."
    Jes "Baby, you worked so hard all week. We both have. Do you really need to go out today?"
    Con "It really wouldn't look good if I didn't help out after just starting."
    Con "Don't worry, sweetie. Things will die down soon. I promise."

    if "d053some" not in choices and "d05noConner" not in choices:
        Jes "That's too bad. You'll miss lying on the couch with me and doing nothing, recovering from last night."
        "Conner chuckles."
        Con "You're that tired?"
        Jes "Oh yeah. Last night was a lot of fun, but more exhausting than our usual thing."

        if "d05heatherLesson" in choices:
            Jes "So, you're sure you're okay with it? With Heather and I…?"
            "Conner smiles and nods."
            Con "Yeah. I admit, that was a little weirder than I figured having my wife be with another woman would be, but I liked it."

        if "d05heatherPleasure" in choices and "d05noConner" not in choices:
            Jes "That was… wonderful! I don't remember the last time I came so hard."
            "Conner chuckles again."
            Con "So you want me to make love with my tongue from now on?"
            Jes "Just because you're good with your tongue doesn't mean I don't want your dick too!"

            if "d05heatherWatch" in choices:
                Jes "And you didn't mind Heather watching?"
                Con "That… was a lot hotter than I expected it to be. Still a little weird, but hot as hell!"
                Con "I wanted to make sure I wasn't too rough, though. I kinda just went primal there."
                Jes "Baby, it was great. I loved it!"
                Con "I'm just glad I could make you happy, sweetie."

        scene day6 ev01-03
        Con "I really have to head out, though. I promise I'll make it up to you tonight."
        "Conner leans in, planting a soft kiss on her cheek."
        Jes "Okay. Have a good day, baby."
        Con "You too, Jess."

    elif "d053some" in choices:
        Jes "That's too bad. You'll miss lying on the couch with me and doing nothing, recovering from last night."
        "Conner nods, his smile briefly fading."

        scene day6 ev01-04
        Con "Yeah. Yeah, that was fun."
        "He looks down, as if wanting to say more but unable to find the words."
        Jes "Baby? You okay?"
        Con "I'm just tired is all."

        scene day6 ev01-05
        Jes "Hey. You seem… kinda tense. Are you sure you okay?"
        Jes "Did you not… enjoy last night?"
        Con "Of course I did. It was amazing."
        Con "I just… I feel bad for Christian."

        scene day6 ev01-06
        Con "I mean, he's my friend. He's a good guy… and I just fucked his wife."
        Jes "We fucked his wife! I was there, remember?"
        Con "Yeah, but that won't matter. He won't care."
        "Jessica blanches."
        Jes "Um… excuse me?"
        Con "What?"
        Jes "What do you mean it won't matter?"
        Con "Because you're a woman."
        Jes "So it's okay if a woman sleeps around with other women, but a cock is a step too far?"
        Con "You know that's not what I mean! Every guy dreams of his wife screwing another woman."
        "Jessica takes a deep breath and lets out a long groan."
        Jes "I'm going to move on because I'm too tired to argue."
        Jes "I'd already spoken with Heather about this. It's fine. I think they're swingers."

        scene day6 ev01-07
        Con "Wait, really? So he's probably used to Heather sleeping with other men?"
        Jes "And he probably sleeps with other women."
        "Conner becomes visibly relieved."
        Con "Well… I suppose that's not as bad, but still. I don't think it's any better."
        Jes "What do you mean?"
        Con "He might want us to repay the favor."
        "Jessica rolls her eyes."
        Jes "For fuck sake, I think I might have a say in that exchange."

        scene day6 ev01-08
        Con "I know! I know! I'm not about to be swinging with the neighbors!"
        Con "I just meant that Christian might be thinking that way, and then it's gonna be awkward and he'll get upset."
        Jes "If he does, he's an asshole. I think we're fine, though. This wasn't an exchange, it was Heather having some fun with her friends. That's all."

        scene day6 ev01-09
        "Despite her assurances, Conner remains insecure."
        "He gives her one last kiss before standing up."
        Con "I really do need to go. We'll talk more when I get home."
        Con "I love you, babe."
        Jes "I love you too."
        "Jessica watches him go, sighing in frustration."
        JesT "Damnit. Was last night a mistake?"

    else:
        scene day6 ev01-03
        Con "I really have to head out, though. I promise I'll make it up to you tonight."
        Con "MWA!"
        Jes "Okay. Have a good day, baby."
        Con "You too, Jess."

    if "d05wearMine" in choices:
        scene day6 ev01-10b with fade
    else:
        scene day6 ev01-10a with fade
    "Briefly, Jessica tries to get some more sleep, but finds she can't drift off."
    JesT "I guess it's time to get up."
    "Sitting up, Jessica rubs her eyes, letting her body wake up slowly."
    JesT "I really would like to get some more sleep, but I'm absolutely starving."

    if "d05noConner" in choices:
        JesT "I wonder if I should have had Heather stay last night? The three of us could have had some real fun."
        JesT "Then again, it's better to keep my relationship with Heather separate. Whatever that relationship is."
        JesT "I mean, I'm not a lesbian. I like men. Heather's the same way, but flirting with her is so much fun!"

    elif "d05noConner" not in choices and "d05wearMine" in choices:
        scene day6 ev01-11 with dissolve
        "Jessica's eyes drift down, as she suddenly remembers having switched panties with Heather."
        JesT "Oh my god! I forgot about these."
        JesT "Heather's so wild and different than any woman I've ever known. Maybe that's why I like her so much."
        JesT "We have the strangest relationship. Whatever that relationship is."
        JesT "I mean, I'm not a lesbian. I like men. Heather's the same way. I just can't get enough of that woman, though. She's fucking amazing!"
        JesT "I wonder if part of it is the thrill of having a relationship with someone other than Conner. Would this feel the same if I were doing it with another man?"
        JesT "Or is it because I just love the touch of a woman. It feels so different than when Conner touches me."

    if "d05wearMine" in choices:
        scene day6 ev01-12b with dissolve
    else:
        scene day6 ev01-12a with dissolve
    "Thoughts of sex draw Jessica's attention back to her encounter with Victor."
    JesT "Ugh. And then there's that guy."

    if "d05victorHJ" in choices:
        JesT "I can't believe what I did for that guy. I really shouldn't have done it."
        JesT "I can't give in to every man who tries to get sexual favors out of me. I'd never stop fucking, and absolutely no one would take me seriously."

        if slut >= 16:
            JesT "It was oddly fun, though. Why did I enjoy that so much?"
            JesT "Maybe because it was so wrong."
        else:
            JesT "At least I got what I wanted from him. It didn't seem like he was going to give me anything otherwise."

    else:
        JesT "I did the right thing refusing him, though, even if it put me back to square one. I can't let men use me like that."
        JesT "I really hope David can come through. If he has nothing, I'm at a dead end."

    if "d05wearMine" in choices:
        scene day6 ev01-13b
    else:
        scene day6 ev01-13a
    "She steps out of bed, yawning. Her belly grumbles at her."
    JesT "It's food time."
    JesT "I wonder if Laura got back last night."

    scene day6 ev01-14
    "Opening the door to the guest bedroom, Jessica finds Laura asleep within, clothes strewn about."
    JesT "Geez, Laura. You make more of a mess than Conner."
    JesT "She must have come in late. I'll just leave her alone for now."
    "She closes the door quietly, leaving Laura to her sleep."

    if "d05wearMine" in choices:
        scene day6 ev01-15b
    else:
        scene day6 ev01-15a
    "Strolling into the kitchen, Jessica takes a few seconds to realize that a stack of pancakes sits on the table, a good morning gift from Conner."
    JesT "He made… pancakes. Again."
    JesT "I really need to teach him how to cook something else."

    if "d053some" in choices:
        JesT "Did he know I'd get upset and make breakfast for me to apologize in advance?"
        JesT "Probably not. Otherwise, he could have just not put his foot in his mouth."

    scene day6 ev01-16
    "As she eats, Jessica's frustration begins to bleed away."
    Jes "Mmm! Oh my god! So good!"
    JesT "I'm too hard on him. He can only cook pancakes, but they're the best fucking pancakes ever!"
    "Once she's finished, Jessica takes a moment to let her food settle."

    if "d05victorHJ" in choices:
        JesT "I should go take a little bath, relax for a little. I could use a soak since I'm not on a timetable today."
        JesT "Afterward I need to go check out that address I got from Victor. The sooner, the better."

    else:
        JesT "I should go take a bath. It's been a long week, and I could use a soak now that I have a day off."

    if "d05wearMine" in choices:
        scene day6 ev01-18 with fade
        "Jessica heads off to the bathroom, brushing her teeth before beginning to slip out of her sleepwear."
        "As her fingers slip into Heather's black panties, she giggles and recalls the sensation of Heather's wetness against her body."
        JesT "Oh my god, that was so naughty! I can't believe I wore these all night!"
        "Her fingers slide over her sex, gently rubbing her tingling clit. She savors the memory of putting them on, and briefly considers holding onto them."
        JesT "I should probably give them back to the Heather, though. I shouldn't be collecting souvenirs from our little thing."
        JesT "And as naughty as giving them back like this would be, I should probably wash them first."

    else:
        scene day6 ev01-17 with fade
        "Jessica heads off to the bathroom, brushing her teeth before slipping out of her sleepwear."
        "Dropping off her undergarments in the laundry basket, she takes a long stretch, ready to soak."

    scene day6 ev01-19
    "Once she's nude, Jessica slides into the tub, soaking her body from head to toe."
    "She moans happily, letting her body go limp and luxuriating in the moment."
    JesT "Oh, this is nice. Exactly what I needed after this week."

    if "d05victorHJ" in choices:
        scene day6 ev01-21
        "The feeling of the water is so relaxing that she begins to drift away."
        "Her mind wanders, and as it does her hands begin to move of their own accord."
        "She soon finds her fingers rubbing at her sex, slowly massaging her clit."

        scene day6 ev01-22
        JesT "Mmm. It feels nice to relax."
        "Her hands keep moving, slowly rubbing in a circular motion."
        "Small moans fill the small room, Jessica trying to keep quiet so Laura won't hear her… again."
        "The pressure builds within her sex, her need for release growing with each passing second."

        scene day6 ev01-23
        "Swifter movements bring her closer and closer to orgasm. She shuts her lips tightly, ensuring she won't cry out when she cums."
        "Yet she whines and moans as her climax nears, feeling the tremendous pressure building and building until it can be held back no longer."
        "Her body goes rigid and stiff, her back arching as she feels waves of pleasure spilling over her body."
        "The tension of the past few days evaporates in moments, and as she comes down from her climax, Jessica feels truly relaxed for the first time since the week began."
        JesT "Whew. That was good. Alright. I've had enough time to myself in here."

        scene day6 ev01-26
        "After drying off, Jessica begins to get dressed."
        "While putting her hair up, she begins planning out her day."
        JesT "If I leave soon, I can check out this address from Victor before noon."
        JesT "Then I head back here for lunch."
        JesT "That gives me plenty of time to spend with Laura and Conner before Mom gets here."
        JesT "I'll even have some time to unwind before then. Having her around is always… eventful."

        if "d05heatherFinger" in choices:
            "Her thoughts soon turn back to her last moment with Heather from the previous evening, making her smile."
            Jes "I wonder if Heather's home right now."

            if "d053some" in choices:
                JesT "I should drop by later and talk with her."
            else:
                Jes "I think I'm gonna give her a call..."

    else:
        scene day6 ev01-20
        "For a few minutes, Jessica is blissfully relaxed. The world outside has completely vanished."
        "The ringing of the phone might as well be screeching in her ears, and her soft breathing turns into a harsh groan."
        Jes "Oh, come on."
        "She sighs, debating whether or not to answer the phone."
        JesT "Fuck it. Whoever it is, I can call them back."
        "Jessica closes her eyes and tries to ignore it, and it soon goes to voicemail. Unfortunately, they call back immediately, and Jessica sneers as she rises from the tub."
        Jes "Goddamnit. I don't want them to wake Laura."

        scene day6 ev01-30 with fade
        "She quickly throws on a bathrobe and walks out to find that it's David calling. Jessica's annoyance vanishes, a smile moving onto her face."
        JesT "Oh good. I hadn't expected to hear from him so soon."
        JesT "I wonder if he's checked on Victor already."

        scene day6 ev01-31
        Jes "Hey, David. How's it going?"
        Dav "Hey, Jess. I wanted to let you know I visited Victor this morning, and I have some news."
        Jes "David, that's great! Did you get the address?!"
        Dav "Um… Can you meet me? I need to explain what happened."
        "Jessica's excitement quickly dissipates, thinking it's strange he can't just tell her."
        Jes "Um… yeah. Sure. I can meet you in an hour or so."
        Dav "Great. There's a coffee shop near Memorial Park. Why don't we meet up there?"
        Jes "Okay. One hour, then?"
        Dav "Yeah. I'll see you soon, Jess."
        Jes "Bye."
        "Sighing, Jessica stops the call and leans back on the bed."
        JesT "What's he gonna tell me? If he had the address, he could have just given it to me, and if he doesn't he would have just said so."
        JesT "What happened?"

        scene day6 ev01-26
        "Jessica removes her robe, drying herself off and putting on fresh underwear."

        if "d05heatherFinger" in choices and "d053some" not in choices:
            "While she dresses, her thoughts turn back to her last moment with Heather from the previous evening, making her smile."
            Jes "I wonder if Heather's home right now."

            if "d053some" in choices:
                JesT "I should drop by later and talk with her."
            else:
                Jes "I think I'm gonna give her a call..."

    if "d05heatherFinger" in choices and "d053some" not in choices:
        $ choices.append("d06visitHeather")

        scene day6 ev01-27
        "She quickly calls Heather, her heart beginning to beat in her chest."
        Heath "Good morning, Jes!"
        Jes "Hey there, Heather. How's it going?"
        Heath "Better now that I'm hearing your voice."
        "Jessica blushes, and she bashfully shifts on the bed."

        if "d05victorHJ" in choices:
            Jes "Listen, are you home right now? I was gonna head out to check something for work, and I was wondering if I could stop by."
        else:
            Jes "Listen, are you home right now? I was gonna head out to meet someone from work, and I was wondering if I could stop by."

        Heath "Absolutely! Come on over! Just let yourself in when you get here."
        Jes "Okay. I'll see you in a few."
        "After hanging up, Jessica suppresses a smile and gets up to get dressed."

    scene day6 ev01-32 with fade
    "Before she heads out, Jessica stops in to Laura's room."
    Jes "Hey. Laura."
    Lau "Hmm? What?"
    Jes "Hey, it's me."
    Lau "Mmm."
    Jes "I'm gonna head out. I should be back for lunch, but if not there's some food from last night in the fridge."
    "Laura moans, shoving her head back into the pillow and mumbling ‘okay'."
    "Jessica grins as she heads out of the room."
    JesT "I bet she'll still be in bed when I get back."

    if "d06visitHeather" in choices:
        jump day06visitHeather

    elif "d05victorHJ" in choices:
        jump day06checkingAddress

    else:
        jump day06meetingDavid

label day06visitHeather:

    if "d05victorHJ" in choices:
        scene day6 ev03-01a with fade
    else:
        scene day6 ev03-01b with fade
    "A nervous twinge fills Jessica as she strolls into Heather's apartment, a sign of how far their illicit relationship has progressed."
    Jes "Hey!"
    Heath "Hey, sweetie! I'm in here!"
    "Heather smiles up from the table, an expression of bemusement on her face."
    Heath "Good morning, Jessica. How are you today?"
    Jes "I'm good."
    "Jessica's gaze lingers on Heather's attire."
    JesT "That shirt's adorable, and definitely shows off her figure."

    if "d05victorHJ" in choices:
        scene day6 ev03-02a
    else:
        scene day6 ev03-02b
    Jes "You look wonderful, Heather."
    Heath "And you look good enough to eat! Loving the outfit, sweetie."
    Jes "Really? You don't think the shirt shows off a bit too much?"
    Heath "I'm not complaining from where I'm sitting."

    scene day6 ev03-03a
    "As they speak, Heather's hand slides onto Jessica's leg. Her fingers gently caress the thigh, sending shivers of delight up Jessica's body."
    Heath "I don't suppose you brought my panties back, did you?"
    "Heather giggles, but Jessica simply lets out a shuddering breath in response."

    scene day6 ev03-03b with dissolve
    "Jessica is silent as Heather's hand begins to push up her skirt. The sensation is wonderful, and is exactly what Jessica had been hoping for."
    Jes "I, um… I left them in the laundry. I figured I'd bring them back clean."
    "Heather's hand stops, a devious smile on her face."
    Heath "I was hoping you'd return them as they were given."

    scene day6 ev03-04
    "Heather rises, pulling them both close together."
    Jes "Oh. Well, I've missed you too."
    "Breathlessly, Jessica waits for Heather to lean in and kiss her. Instead, Heather takes her by the hand."
    Heath "Come on. Come sit with me."

    scene day6 ev03-05
    "The pair take a seat on the couch, Heather scooting in close to Jessica."
    Heath "So what's up with work on a Saturday? You should be relaxing today. Preferably with me."
    "Jessica's head shakes."
    Jes "If only I could, but I have to try and get this story done for work."

    if "d05victorHJ" in choices:
        Jes "I've got an address to check on, and if I find anything I'll need to check that out too."
    else:
        Jes "A friend of mine might have some information for me, so I need to go meet him."

    Heath "Well, no one can say you aren't dedicated to your job."

    scene day6 ev03-06
    "Heather leans in closer, her eyes practically glued to Jessica's chest."
    Heath "My, what a lovely necklace you've got there."
    "Her fingers scoop it up, taking their time to slowly swipe along Jessica's cleavage."
    Heath "It's beautiful. It suits you perfectly."
    Jes "Thanks. It was a gift from Conner when we went to Hawaii."

    scene day6 ev03-07
    "The necklace falls back to Jessica's chest, Heather beginning to trace her finger along her breast."
    Heath "It's nice, but it's not nearly as beautiful as the one wearing it."
    "Jessica sighs, her skin tingling at Heather's touch."
    "Her mind goes blank, letting herself drift away with the moment."

    scene day6 ev03-08
    "Heather slowly slips her fingers into Jessica's top and pulls it down."
    Heath "That's so pretty! I want to get a look underneath, though."
    Heath "May I?"
    "Jessica takes a breath and nods."

    scene day6 ev03-09
    "Heather's fingers move beneath the bra, her fingernails lightly scraping along the tender flesh."
    "Her fingers grope Jessica's breast, gently, not squeezing them as she'd used to men doing."
    Jes "Mmm, that feels nice."
    "Fingers curl around Jessica's neck, pulling their faces closer and sending little shivers down her spine."

    scene day6 ev03-10a
    play voices x_moaning_low_1 fadein 1 loop
    "Heather's hand pushes aside Jessica's bra, revealing her breast in all its beauty."
    "Her fingertips begin softly pulling and pinching Jessica's nipple."
    "Jessica's mouth falls open as she begins to moan."
    Jes "Oh. Yeah, keep doing that."
    Heath "As you wish, sweetie."
    "Jessica's eyes almost close, pleasure filling her body."
    JesT "Goddamn! She's so much better at this than Conner!"

    scene day6 ev03-10b
    "Without warning, Heather pinches the nipple and give it a little pull."
    "Jessica squeals in surprise, but continues her incessant moaning."
    Jes "Oh my god!"
    "Heather giggles, delighted at how Jessica is responding to her touch."

    scene day6 ev03-11
    play voices x_ff_kissing_1 fadein 1 loop
    "The pleasure becomes too much, and Jessica leans in, planting her lips against Heather's. Both moan in delight as they kiss, fingers brushing over each other."
    "Jessica's hand pushes Heather's shoulder strap down, eager to see her beautiful lover's naked bosom."

    scene day6 ev03-12a
    "The sight of it drives Jessica wild, and her hand moves down to grope and squeeze the gorgeous breast."
    "The soft, gentle consideration Heather had shown her is nowhere to be found. Jessica can feel her blood pumping, and her libido raging. Her fingers squeeze, Jessica delighting in soft flesh moving in her hand."
    JesT "I can't believe how different it feels being with her. Conner's so hard and muscular, but Heather's so soft and feminine."
    JesT "Touching her is intoxicating!"

    scene day6 ev03-12b
    "She can even feel Heather's rigid nipple poking into her palm, a fact which causes her to giggle as they kiss."
    Heath "What?"
    "Jessica shakes her head."
    Jes "Nothing. Don't stop."
    "The two resume their kiss, moaning and mewling together in a passionate embrace."
    stop voices fadeout 1

    scene day6 ev03-13
    Heath "Agh. Hold on."
    Jes "What?"
    Heath "Don't be so rough. You're squeezing me like a guy."
    Jes "Sorry. I just got caught up in the moment. Conner and I don't usually do the whole gentle thing."
    Heath "It's okay. I get that way sometimes too."
    Heath "Let me show you how it's done."

    scene day6 ev03-14a
    play voices x_ff_kissing_1 fadein 1 loop
    "Heather begins kissing around Jessica's nipple, small smacks filling the room."
    "Jessica sighs, enjoying the feeling of her sapphic lover's lips on her bosom."
    JesT "This feels incredible! I'm so wet already!"
    JesT "I've never gotten this turned on from having my boob played with. I wonder if someone can cum just from breast play?"

    scene day6 ev03-14b
    "Soon Heather takes the nipple in her mouth, sucking and flicking at it with her tongue."
    Heath "Mmm."
    Jes "That's so good, Heather. Keep doing it, just like that."
    "Heather smiles, her lips continuing to suckle all the while."

    scene day6 ev03-15
    "Jessica closes her eyes, enjoying the naughtiness of having another woman sucking at her breast, first thing in the morning."
    JesT "This is so wrong, but fuck me if I'm not loving it!"
    JesT "And it feels so damn good! If this keeps up, I'm gonna have to go back and change my panties before I head out!"

    scene day6 ev03-16
    JesT "Oh, crap. I have to get going."
    stop voices fadeout 1
    Jes "Hey, we need to stop. I actually have to get going."
    "Her breast pops from Heather's mouth with an audible smack. Their eyes meet, and for a moment she wonders if she can stay after all."
    JesT "I really, really don't want to go, but I have to. Damnit. Why does Heather have this effect on me?"

    scene day6 ev03-17
    Heath "Aw, really? I was hoping we could have some more fun while you were here."
    "Jessica nods while putting her breast away."
    Jes "Sorry. Believe me, I'd love to stay, but I can't put this off."

    if "d05victorHJ" in choices:
        Jes "I really need to check this place out as soon as possible."
    else:
        Jes "My friend's waiting for me. I can't be too late. Or show up smelling of sex."

    "Heather's disappointment is written on her face, making Jessica feel a little guilty."
    Heath "That's too bad. I want to do so many things with you."
    Jes "With me or to me?"
    "Heather nods as she pulls her shirt up."
    Heath "Yes."
    Jes "Why don't we got out sometime soon? Have a date just with us girls?"
    Heath "I'm free tonight."
    Jes "I can't. My mom's coming over tonight and we're gonna have dinner together."
    Jes "I'm free tomorrow, though."
    Heath "Okay. It's a date, then."
    "Both ladies smile, sharing one last goodbye kiss before Jessica heads out."

    if "d05victorHJ" in choices:
        jump day06checkingAddress

label day06meetingDavid:

    scene day6 ev02-01 with fade
    play sound city_street_with_vespa loop
    "Jessica arrives at the coffee shop a short time later."
    "There's an outdoor sitting area, but she doesn't see David waiting just yet."
    stop sound fadeout 1

    scene day6 ev02-02 with fade
    play sound city_ambience_5 loop
    "Heading in, she orders a coffee for herself, then takes a seat. She feels a little giddy, hoping that he has at least something for her."
    JesT "He sounded kind of serious when we talked earlier."
    JesT "I hope nothing went wrong."
    JesT "I don't know why he couldn't have just told me what he found on the phone. Why the need to meet?"

    if slut >= 15:
        JesT "Oh well. I don't mind sitting across from such a good looking guy for a bit."
    else:
        JesT "Oh well. It's a nice day, so I shouldn't complain. It's good excuse to talk to a friend for a bit."

    if "d06visitHeather" in choices:
        scene day6 ev02-03
        "David arrives a few minutes after Jessica sat down. Jessica's face lights up when she sees him."
        Jes "Hey, David!"
        Dav "Hey, Jess. Thanks for coming. Sorry for being late like this."
        Jes "That's okay. I ended up talking to my neighbor for a bit."
        JesT "Among other things."

    else:
        "Jessica spends some time sitting alone with no sign of David."
        "She checks the time on her phone twice, wondering just where he is."
        JesT "Alright. I'll call him. See if he's at least on his way."

        scene day6 ev02-03
        "Just as she's bringing up his number, though, he walks in, smiling at her."
        Dav "Hey Jessica."
        Jes "Oh, David. There you are."
        Dav "Yeah, sorry for being late like this. I appreciate you coming."

    scene day6 ev02-04
    Jes "So, please tell me you got the address for me? I really need this."
    Dav "Well, that's the good news. I did get what you wanted."
    Jes "Oh my god, David! You're amazing!"
    Dav "But… there was a problem."
    Jes "What happened?"

    scene day6 ev02-05
    Dav "I went to see him this morning, and he was royally pissed off."
    Dav "Apparently some guy came by yesterday just after you did, asking for the exact same thing."
    Jes "What? That's… someone else was looking for the bike?"
    Dav "Sounds like, and based on what Victor told me it sounds like it's the biker you're looking for."
    Jes "Any idea who, or how they found out about it?"
    Dav "No idea. But the guy wanted to know if Victor made the modifications, and when he said he did the guy wanted any other info."
    Dav "When Victor refused to give it, the guy took it."
    Jes "How?!"
    Dav "Based on the broken nose and bruises, I'd say the guy beat the shit out of him."
    Jes "Oh my god!"

    scene day6 ev02-06
    Dav "Yeah. Victor says the guy jumped him, and held him down until he told him about his ledger."
    Dav "Then the guy ripped the page out and took off."
    Jes "Fuck! Is Victor okay?"
    Dav "Yeah, he's pretty tough. He's working again already."
    Jes "That's good at least. But goddamnit, I needed that address."
    Jes "Wait. You said you had it, right?"
    Dav "Yeah. I asked Victor about it, and he said he remembered the street. Couldn't remember the building number, but the guy who does the deliveries apparently remembered a big old warehouse."
    Dav "He also remembered a name that was supposed to go with the delivery, though that was probably fake."
    Jes "David, this is wonderful! I can probably find the warehouse on my own. What's the street?!"

    scene day6 ev02-07
    "David sighs, leaning back into his chair."
    Dav "Look, Jess, I think you should drop this whole thing."
    Jes "What? No! We've got the address! Why would I drop it now?!"
    Dav "You have been listening to me, right? Some guy beat the shit out of Victor."
    Dav "You're mixed up in something dangerous here, Jessica. I think you need to back out of it. I don't think you need this info."
    Jes "David, I appreciate your concern, I really do. But I will be fine."
    Dav "I mean…"
    Jes "How about this? I promise that I'll only go in daylight, I won't take any chances. I'll even take Conner with me. Okay?"
    JesT "I absolutely won't bring Conner, but I don't need you protecting me, David."
    "David sighs, but nods and pulls out his phone."
    Dav "I'm texting you the info. Be careful with it."
    Jes "I will, David. I promise. So, did Victor get a look at the guy who beat him?"
    Dav "Not really. Young guy, muscular, hat and glasses. He threw motor oil in Victor's face, and after that he didn't see much of anything."
    Jes "I don't suppose he was a cop."
    Dav "Probably not. They usually flash a badge first."
    Jes "It's just so weird that we get the info on this bike, then this guy suddenly shows up."
    Jes "Maybe someone got it from our server, after I uploaded everything."
    Dav "It could be the guy himself. The biker."
    Jes "That doesn't make sense. Why would he ask about the bike parts if he already knew Victor was the guy who did the modifications?"
    Dav "To throw him off, maybe?"

    scene day6 ev02-07b
    "Jessica shrugs."
    Jes "I guess. When did this guy come by?"
    Dav "A little while after you left."
    Jes "Victor… doesn't think I had anything to do with him, does he?"
    Dav "He did, but I convinced him that was bullshit. You wouldn't have sent me to get the address if you sent the other guy."
    Dav "Hell, I think he gave me the address in the hopes that you'd find the guy that did it."
    Jes "I really don't want to get involved in a vendetta between those two."
    Dav "Yeah, that's probably smart."
    Jes "Thanks, David. For all your help. You've saved my ass."

    scene day6 ev02-08
    Dav "Well, it's too nice an ass not to save."
    "The two share a laugh and sit for a while, drinking their coffee and chatting."
    Jes "How's your sister been? I haven't seen her in a while."
    Dav "She's good. She found a place where she sings a couple nights a week."
    Jes "That's awesome. She talked a lot about singing professionally."
    Dav "Well, it's just a small thing, but she's making money doing what she loves."
    Dav "If you want, I can take you to see her. She's singing tonight…"
    Dav "With Conner, of course… if you want."
    Jes "I'd love to, but I have plans tonight. My mom's visiting."
    Jes "Why don't I give you a call sometime next week though? We can set up something for the next time she performs."
    Dav "Sure thing."

    scene day6 ev02-09
    "After chatting for a little while longer, Jessica stands, telling David she has to go."
    JesT "I need to go and check this address. Given all the attention it's getting, anything that's there might disappear soon."
    Jes "Thanks again for all your help, David. I appreciate it so much."
    Dav "My pleasure, Jess. And be safe out there. Remember your promise."
    Jes "I will, but don't worry. I'll be alright."
    JesT "I'd have been screwed without David. I really owe him for this."
    JesT "Not to mention if he hadn't gone, things could have become rough. I really didn't need a guy like Victor thinking I'd sent a guy to beat him up."

    menu:
        "Thank him friendly":
            $ choices.append("d06DavidFriend")

            scene day6 ev02-10
            "Jessica gives David a hug and an air kiss."
            Jes "Thanks for everything, David. You're amazing."
            Dav "Yeah, I know."
            "The two say their goodbyes before both turn to head out."

        "Kiss him":
            $ choices.append("d06kissDavid")
            $ relDavid += 1
            $ slut += 1

            scene day6 ev02-11
            "Jessica leans in and gives David a hug and a kiss on the side of his lips."
            "He seems surprised at first, but a second later he pulls her closer, pressing her chest into his own."
            JesT "Whoa. That was a little more than I'd expected."

            scene day6 ev02-12
            Jes "Um… thanks David. I'll call you tomorrow."
            Dav "Okay. Talk to you later."
            "His hand holds onto her for a second longer before she pulls away and heads out."


    scene day6 ev02-13 with fade
    stop sound fadeout 1
    "Jumping on her scooter, Jessica finds the street on her phone."
    Jes "Alright. Let's go find this warehouse."
    play sound vespa_start_drive
    Jes "And, with a little luck, find out something about our vigilante."
    stop sound fadeout 1

label day06checkingAddress:

    scene day6 ev04-01 with fade
    play sound city_street_with_vespa loop

    if "d05victorHJ" in choices:
        "Jessica finds the building without any problems. She pulls up next to the warehouse, an old industrial building that looks to have been abandoned for quite some time."
    else:
        "It takes Jessica a little while to find the building she's searching for, having to drive along the street until she spots a warehouse. Eventually, though, she finds the only building that seems to fit the description: an old industrial building that looks to have been abandoned for some time."

    JesT "It doesn't look like anyone's been here in a while."
    JesT "Let's see if I can get a look inside."
    stop sound fadeout 1

    scene day6 ev04-02
    play sound city_ambience_4 loop
    "She heads over to the door, taking a look at the mailbox to the side. The nameplate has been removed, likely due to the building no longer being in use."
    JesT "Damn. If it really is abandoned, that'll make getting in harder."
    "There's the button for a buzzer next to the door as well, which Jessica presses. She waits a little while before pressing it again, yet no one ever appears to answer."
    JesT "Well, fuck."
    "Hoping for a bit of luck, she tries to open the door, but it's locked tight."
    JesT "Nope. I should take a peek inside. Let's see if I can find a window."

    scene day6 ev04-03 with fade
    play sound city_ambience_5 loop
    "Heading around the back, she finds a large line of windows, just out of reach."
    JesT "That's useful. Let's see if I can get up there."

    scene day6 ev04-04
    "A nearby garbage bin provides a bit of height, though Jessica finds herself suddenly feeling frustrated."
    JesT "I did not dress for this."
    JesT "Note to self: when investigating old buildings, wear flexible pants."
    JesT "And I'm going to hate myself if I end up falling and breaking my neck just to get a peek in some stupid old building."
    "Despite hating her wardrobe choice for the day, Jessica boosts herself up onto the bin to get a peek inside."

    scene day6 ev04-05a
    "The windows are filthy, but Jessica manages to peer through to see… nothing."
    "The entire building is empty from end to end. She sees discoloration on the floor, likely from where heavy machinery used to sit. A few piles of useless garbage lie strewn about as well."
    "At the moment, though, there's nothing and no one to see inside."
    JesT "Damn. That sucks."
    JesT "Not sure what I expected to see. Maybe the vigilante's secret lair."
    JesT "But of course he'd use an empty building for his delivery. Why would he send someone to his home?"

    scene day6 ev04-05b with dissolve
    JesT "But… he did have his stuff delivered here, so maybe there's something inside that can tell me more. I have to get in."
    JesT "I don't want to break inside in broad daylight, though. I'd prefer not to be arrested today."
    JesT "Maybe I can find out who owns the place. Maybe they can tell me how the vigilante got access, if he isn't just breaking and entering."

    if "d05victorHJ" in choices:
        scene day6 ev04-06a
        play sound city_street_with_vespa fadein 3 loop
        "Hopping on her scooter once again, Jessica gets ready to leave."
        Jes "I don't think I'm going to find anything else at the moment."
        "She looks around, but the street is pretty much empty."
        Jes "Well, for the moment I'll try and find the owner. If I can't, I'll come back and ask around later. Maybe someone in the area knows something."

        jump day06visitParker

    else:
        scene day6 ev04-06b
        play sound city_street_with_vespa fadein 3 loop
        "Hopping on her scooter once again, Jessica gets ready to leave."
        Jes "I don't think I'm going to find anything else at the moment."
        "Before she drives away, though, she looks around and notices an old man sitting at an empty table next to a bar across the street."
        Jes "That place looks closed. He might be a local, who might just have seen something."

        scene day6 ev04-07 with fade
        play sound city_ambience_4 fadein 1 loop
        "She drives the scooter over to the other side of the street, hopping off and strolling over to speak with him."
        Jes "Excuse me, sir? Do you live around here?"

        scene day6 ev04-08
        "He nods, thumbing to the building he's sitting next to."
        Art "I sure do. I'm Art. I live in this condo."
        Jes "My name's Jessica O'Neil. I'm a journalist with the New Port Gazette."
        if persistent.pov == 1:
            scene day6 ev04-08mpov
        Jes "I'm doing a piece on small businesses around town. Could you tell me anything about the building across the street?"
        Art "A small company was using it a while back, but they closed up shop a couple of years ago."
        Art "They were making components for those clever new phones."
        "A thin voice picks up from the side of the building."
        VV "They're smartphones, Art."

        scene day6 ev04-09
        "A small boy with a basketball stands nearby, chuckling to himself."
        Art "Get lost, Kevin. No one asked you for your opinion."

        scene day6 ev04-10
        "Kevin looks down to his feet, mumbling something as if embarrassed."
        JesT "That was harsh. The kid was just being helpful."
        Art "Anyway, yeah. The company made smartphone parts."
        Art "But they went bankrupt and a dozen or so people lost their jobs."
        Jes "Do you happen to remember the name of the company?"

        scene day6 ev04-11
        Art "Umm… yeah. I think so. It was… uh… Cellco! I think."
        Art "I'm pretty sure that was it."
        Jes "Was the building used for anything after they closed up shop?"
        Art "No. I haven't seen anyone using it for a while."
        "Jessica turns, addressing Kevin this time."
        Jes "What about you? Have you seen anyone using the place?"
        Kev "No. My friends and I snuck in once when there was an open window, but we didn't see anybody."
        Art "You didn't find an open window! You and your little friends broke one!"
        Art "I remember now! Some guys came by to fix it afterward!"
        Art "With all your little juvenile delinquents in the neighborhood, they should have installed spy cams to keep an eye on you."
        Kev "Ha! They're called security cameras, Art!"

        scene day6 ev04-12
        Art "You shut your mouth, you little brat! I swear, kids like you have no respect for your elders!"
        "The boy's eyes move back to his feet, embarrassed once more."
        JesT "Wow. This got hostile quick. This kid's just trying to help, in his own childish way."
        JesT "Maybe I should stay out of it, though. I've only been speaking to this guy for a few minutes."

        menu:
            "Stay out of it":
                $ choices.append("d06ignoringKevin")

                Art "Go play with your ball, Kevin. I'm gonna have a talk with your mom later."

                scene day6 ev04-13
                "Despondent, the boy turns around and leaves, Jessica watching with pity."
                Art "I swear, kids these days are beyond saving."
                JesT "Still, that was way too harsh. He didn't deserve that kind of scolding."
                Jes "So, you haven't seen anything over at the building after that accident with the window?"
                Art "Nope. Nothin'."
                Jes "Okay. One more question. If I left you my phone number, would mind calling me if anyone comes by, goes in the building, anything like that?"
                Art "Sure. Why not?"

                scene day6 ev04-14
                "Jessica grabs a notepad from her scooter and writes down her work number, handing the slip over to Art."
                Jes "Feel free to call me any time of day if you see anything happening around the building. Anything at all."
                Art "Will do."
                "Jessica and Art say goodbye before she hops on her scooter and takes off."
                JesT "There's gotta be something that can help me out in there. This can't be a dead end."

            "Defend the boy":
                $ choices.append("d06defendingKevin")

                JesT "I think I should try to defuse this situation. Kevin's just being a kid."

                scene day6 ev04-15
                Jes "I'm sure he didn't mean any disrespect. He's just trying to help out."
                Jes "He knows he should be respectful of his elders, don't you?"
                "Jessica's smile draws Kevin's attention, and he nods vigorously."

                scene day6 ev04-16
                Jes "It's just tempting for us, young people, to correct our elders on those rare occasions when they make some small mistake."
                "She winks at Kevin, and he gives her a smile in return."
                Kev "Yeah, I- I'm sorry. I didn't mean anything by it. I just wanted to help out, you know?"
                JesT "He's smarter than some kids this age. Good on him."
                "Art nods and grumbles something under his breath."
                Art "I appreciate that, Kevin. Apology accepted."
                "Kevin backs off a little bit, seemingly relieved."
                Art "Anyway, that's all I can really tell you about the building. Sorry I can't do more to help."
                Jes "If I left you my phone number, would mind calling me if anyone comes by, goes in the building, anything like that?"
                Art "Sure. Why not?"

                scene day6 ev04-17
                "Jessica grabs a notepad from her scooter and writes down her work number, handing the slip over to Art."
                Jes "Feel free to call me any time of day if you see anything happening around the building. Anything at all."
                Art "Will do."
                Kev "I can keep an eye out, too, if you want. Me and my friends are usually hanging around here."
                Jes "That would great, Kevin! Thank you!"
                "She writes down her number again, handing the slip to Kevin this time."
                "His eyes light up as he accepts the paper, holding it close to his chest like a precious possession."
                "Art chuckles, but says nothing."
                Jes "Thank you both for your help. Like I said, anything at all, call me anytime."
                "Jessica says goodbye to Kevin and Art before she hops on her scooter and takes off."
                JesT "There's gotta be something that can help me out in there. This can't be a dead end."

label day06visitParker:

    scene day6 ev05-01 with fade
    play sound city_street_with_vespa fadein 1 loop
    "On her way back, Jessica finds that she's going to pass close to Mr. Parker's newsstand."
    Jes "I should pop in and say hi. I bet he'd be happy to see me."

    if "d04parkerNoApology" in choices:
        Jes "Of course, last time it went too far. Still, it's pretty amazing he can get an erection at his age."
        Jes "I can't really blame him for having a little fun where he can."

    scene day6 ev05-02 with fade
    play sound city_ambience_2 fadein 2 loop
    "Parking her scooter, Jessica heads to the front, waving as she approaches."
    Jes "Hey there, Mr. Parker!"
    "Mr. Parker's eyes light up when he sees Jessica strolling over."
    Parker "Jessica! What a nice surprise!"
    Parker "Come on inside. Have a seat."

    scene day6 ev05-03
    play sound city_ambience_2 fadein 1 loop
    "Jessica heads in the side, Parker getting up to offer her his seat."
    Jes "Thank you very much."

    if "d04parkerNoApology" in choices:
        "She notices his eyes roaming up and down her body, eventually coming to rest on her chest."
        JesT "I guess things are a little different now. He's more bold with his gawking."

    Parker "You're quite welcome. What brings you by today?"
    Jes "I was just on my way home. I thought I'd stop by."
    Jes "I'm coming back from checking a lead for a story."
    Parker "Oh, anything interesting?"

    scene day6 ev05-04
    "Jessica turns the vacated seat to the side before taking her seat."
    Jes "It's the stuff Birch was on me about. The story I told you about before."
    Jes "I'm trying to get info on the vigilante."
    Parker "That's an incredibly high-profile story to get your first week on the job."
    Jes "Well, Duncan wasn't crazy about the story, and Rosa was busy, so it just kind of fell into my lap."
    Jes "Besides, I'm just doing the leg work. If something turns up, someone else will probably take over."
    "Jessica sighs, but Parker immediately speaks up, his tone firm."
    Parker "Maybe, but you're the new office blood. You shouldn't take it personally."
    Parker "A story like the vigilante is so high-profie that they'd want their senior people on it."

    scene day6 ev05-04b
    Jes "Damnit. I was hoping you'd tell me I was wrong, not confirm my fears."
    Parker "Sorry, sweetie. Look, just forget about all that and focus on the work at hand."
    Parker "Worry about that sort of stuff later."
    Jes "Yeah, you're right."
    Parker "What were you out checking, anyway?"
    Jes "An old warehouse off of Mystic Dr. It looks like the vigilante might have used it."
    Jes "It doesn't looks like he's been there in a while, though. I'd like to find out who owns it."
    Jes "I doubt the vigilante does, but it might help me find another lead."
    Jes "Plus… I could always take a quick look inside… after hours."
    "Parker grunts."
    Parker "Just, uh, be careful. Breaking into someone's warehouse isn't a trivial thing. You can get in deep shit."
    Jes "I know, but if breaking the law is the only way to find out more, I'm not sure what else to do. I'm not a cop."
    Parker "No, but you can work with them. Your job is to get a story, not solve the damn case."
    Parker "If anything, having the police on your side will give your story more credibility."

    scene day6 ev05-04c
    Jes "Are you telling me to go find an cop and tell them what I know?"
    Parker "Well, don't just go gabbing to anybody, but if there's someone you trust that's willing to work with you, then yeah."
    Jes "Hmm. No, I don't know any cops like that."
    Parker "I'll tell you what. I have a friend. He's retired, but he might be willing to help."
    Parker "He can point you to someone in the department to talk to."
    Jes "It's worth a try, if he can point me to the right person."

    if "d05victorHJ" in choices:
        Jes "If nothing comes from trying to find the owner, I'll head back and see if there's anyone in the area I can speak to who might know something."
        Jes "Maybe someone could keep an eye on the building for me."
    else:
        Jes "I spoke to a few locals: an old man and a young kid. They agreed to keep an eye on the place for me."

    "Parker nods."
    Parker "Just be careful who you talk to and how much you ask of them."

    if persistent.pov == 1:
        scene day6 ev05-05mpov
    else:
        scene day6 ev05-05
    Parker "I had this colleague who paid a few boys to keep an eye on somebody."
    Parker "He really made them feel like they were helping to catch a bad guy."
    Parker "Well, they got a little overzealous and decided to follow him one day instead of just observing."
    Parker "The whole thing ended in a car chase, a bad accident, and a bunch of those boys in the hospital."
    Jes "Jesus."
    Parker "You can imagine how my colleague felt, and young men would go well out of their way to help a pretty young woman like yourself."

    if "d04parkerNoApology" not in choices:

        scene day6 ev05-16
        "The two chat for a little, Jessica eventually standing up to leave."
        Jes "Okay, I'm gonna take off."
        Parker "Thanks for coming by, Jessica. Have a great weekend!"
        Jes "I'll do my best. Take care!"
        stop sound fadeout 1

        jump day06lunchTime

    else:
        jump day06playParker

label day06playParker:

    scene day6 ev05-06
    "Jessica giggles."
    Jes "I wonder if only young boys would do something like that for me."
    Parker "Oh, I imagine not. I'm sure you could get men of all ages to do just about anything for you. A pretty woman makes some men easily lose their composure."
    "She grins and licks her lips, her eyes glancing down toward Mr. Parker's crotch."
    Jes "Yeah, I got a feel for your… \"composure\" last time."
    "Parker suddenly looks nervous."
    Parker "I was just as surprised as you."
    Jes "Do you mean you haven't been able to… you know… before last time?"
    Parker "I mean, it's not like I couldn't, but more like I don't bother to check anymore."
    Parker "You don't wonder if you can swim if there's no water around."

    scene day6 ev05-07
    "Jessica leans forward, a mischievous smile on her face."
    Jes "In that case, what does it take for you to start \"swimming\" again?"
    Jes "Is it about how a woman looks, or what she does?"

    scene day6 ev05-08
    "Mr. Parker moves towards Jessica, placing his hand on the back of her head."
    JesT "Wait, what's he doing?"
    "To her relief, he simply tilts her head up to look into his face."
    Parker "Well, what we did last time was a very good start."
    "She chuckles, but shakes her head slightly."
    Jes "Last time was a bit too far."
    Jes "Maybe we should \"swim\" in shallow waters before going too deep."

    if "d04parkerHandsOff" in choices:
        scene day6 ev05-08b
        Parker "Well, I'm a bigger fan of jumping in the deep end, but I don't mind taking my time."
        "Jessica chuckles."
        Jes "Well, good things come to those who wait."
        Parker "In my experience, it's better to go for what you want."
        Jes "Based on that bulge, I think I can tell what you want."
        Jes "And we don't always get what we want."

    else:
        scene day6 ev05-09
        "As Jessica's speaking, Mr. Parker's eyes remain glued to her breasts."
        "Apparently unable to contain himself, he leans in and gropes her bosom."
        Jes "That's not… Mr. Parker, you really shouldn't do that."
        Parker "Uh-huh."
        "His eyes are almost glazed over, his attention entirely on her breasts. Jessica isn't even sure he heard her."
        "She sighs, as his fingers gently caressing her breast do feel rather nice."
        JesT "Goddamnit it. Why do I enjoy getting felt up by him so much?"
        JesT "Well, I suppose I can have a little fun with him this time, so long as I control how far we go."

    scene day6 ev05-10
    "Leaning back, Jessica lifts her leg and pushes Mr. Parker away."
    "He begins to protest, only to fall silent when he realizes just where she placed her foot."
    "She keeps her shoe where it is, after he's gone back as far as he can. She can't quite feel his erection through the sole, but she can see he's enjoying the attention."
    if persistent.pov == 1:
        scene day6 ev05-10mpov
    Jes "I'm sorry. These shoes are a little dirty. Should I stop?"
    "Her mockingly innocent tone draws a swift shake of the head from the older man."
    Parker "No. Keep going."
    "His words are barely a whisper, all his attention on the pleasure filling his manhood."

    scene day6 ev05-11
    "Gently, so she doesn't hurt him, Jessica begins rubbing her foot up and down, putting just enough pressure on his cock to make it feel nice."
    "Even through the shoe, she can feel he's starting to get harder."
    "She's keeping her legs together but she knows that, given her position, Parker has a view right up her skirt."
    JesT "It feels so naughty letting him look at my panties, but given what I'm doing I suppose it's perfectly fine."

    scene day6 ev05-12a
    "Jessica continues to play with him, moving her shoe between his legs and rubbing back and forth."
    "Her shoes keeps moving up and over his dick, lightly sliding along the rigid erection, before moving back between his legs."
    "She smiles and moans happily, rolling the edge of her shoe around his outline of his manhood."

    scene day6 ev05-12b with dissolve
    "His reactions are intense, and quite pleasing to Jessica."
    JesT "This is ridiculously hot! I can't believe how much I'm enjoying this!"
    JesT "I can't believe how much he's loving this! I bet I could get him to cum if I just keep doing this."

    scene day6 ev05-13
    "Mr. Parker's hands suddenly move forward, gripping her ankle."
    "He begins to roll her foot along his dick, guiding it where he wants it to go."
    JesT "Oh wow. I… think this is probably far enough."
    JesT "It's gone farther than it should have already… even if it was a lot of fun."

    scene day6 ev05-14
    "Jessica puts her foot down and stands up."
    Jes "I think that's enough for our first swimming lesson. You shouldn't push yourself too hard."
    Jes "I'm gonna head out now. Thanks for the talk, Mr. Parker."
    "Before he can respond, she turns to leave, intentionally brushing her hips against his crotch as she goes."
    Parker "Uh- uh- o- okay."

    scene day6 ev05-15
    "She can feel his eyes on her as she walks toward her scooter."
    Jes "I'll see you soon. I hope you'll be ready for our next lesson."
    Parker "Definitely, Jessica."
    "Hopping on, she gives him a smile and a little wave as she drives off."
    JesT "Okay, time to go home and cool off Jess."
    JesT "God, I'm starving. \"Swimming\" always leaves me famished!"
    stop sound fadeout 1

label day06lunchTime:

    scene day6 ev06-01 with fade
    "Arriving back home, Jessica finds Conner and Laura busy on the couch playing Mario Kart."
    Lau "Haha! You can't even beat me with a blue shell!"
    Con "How the hell do you always get the super horn when you're in first?!"
    JesT "Oh goody. They're playing Mario Kart. Ugh."

    scene day6 ev06-02
    Jes "Hey guys. How's it going?"
    Lau "Good. Kicking your boyfriend's ass."
    Con "Hey."
    "Conner says nothing else, and Jessica rolls her eyes."
    Jes "Sorry for getting home a bit late."
    Con "No worries. There's lunch in the oven, babe."
    "When neither says anything else, Jessica sighs quietly and heads to the kitchen."

    scene day6 ev06-03
    "She pulls out the meal Conner kept heated; leftovers from their dinner with Heather."
    "As famished as she is, she digs in quickly, devouring her meal and thinking about Heather all the while."
    JesT "I wonder what she's up to at the moment."

    if "d053some" in choices:
        JesT "I should see how she's doing. I wonder if she had just as much fun as we did last night."
        JesT "I'm not sure we can do it again, though, given how Conner reacted this morning."
        JesT "If he thinks this is going to come between him and Christian, maybe it's for the best."

    elif "d02friendlyRun" in choices or "d05heatherStop" in choices:
        JesT "Probably something fun. Or something naughty, this woman is wild."

    else:
        "Jessica's heart begins to beat thinking about their date. A smile comes over her face, which Jessica quickly smooths away."
        JesT "I wonder what she'll be wearing. She's always so incredibly glamorous."
        JesT "If Conner asks where I'm going, I can just tell him we're going out for girl's night. It's the truth, after all."

    scene day6 ev06-04
    Lau "You're never gonna catch me, Conner. We've done a full circuit, and you're still in sixth!"
    Con "This track sucks! I'll kick your butt on the next one!"
    Lau "Sure. Jessica, your boyfriend sucks at Mario Kart!"
    "Jessica chuckles, but feels a quick flash of envy."
    JesT "I really wish I could have as much fun with that as they do."
    JesT "They always seem to bond over those games, but I just can't enjoy them."
    JesT "And I don't have anything like that with Conner. Nothing we both love doing."
    JesT "Hmm… I should find something we can enjoy doing together… besides fucking."

    if "d053some" in choices:
        scene day6 ev06-05a with fade
        "As she finishes her meal, Conner comes over and plants a kiss on her cheek."
        "She gives him a polite smile, still a little uneasy from their earlier argument."
        Con "Hey, babe."
        Jes "Hey, sweetie. Done with your game?"
        Con "For now. Your sister's a cheat."
        Lau "You just suck!"
        Con "Ugh. Anyway, how's your day been?"
        "Jessica shrugs."
        Jes "Okay. Pretty uneventful."
        Con "Yeah. Me too. I've mostly just been playing with Laura."
        Con "I remember being better at video games. Maybe she just got better."
        "Jessica doesn't say anything. She just nods."

        scene day6 ev06-06a
        "Conner sits down, taking Jessica's hand in his own."
        Con "You okay? You seem upset."
        "He speaks softly, trying to keep the conversation between the two of them."
        Jes "Well, I'm still unhappy about our conversation this morning."
        Con "I'm sorry, Jess. I didn't mean it to sound that way."

        scene day6 ev06-07a
        Con "Last night really was great. Like I said, I just feel bad for Christian."
        "Jessica sighs inwardly."
        Jes "I told you, it's fine. Heather assured me they've done this before. It's not a problem."
        Con "I get it. I just… I think I need to talk to Christian. Just to make sure we're all good."

        scene day6 ev06-09
        Jes "Oh my god. Sweetie, you cannot talk to Christian about this. This is between him and Heather. We don't have any business getting involved."
        "His shoulders sag, his frustration clear."
        Con "What am I supposed to do? Just pretend it didn't happen the next time I talk to him?"
        Jes "Look. I'll talk to Heather. I'll see what she has to say about the whole thing, okay?"
        "For a moment, Conner doesn't say anything, but he reluctantly nods."
        Con "Alright. That seems fair."

        scene day6 ev06-08a
        "He smiles, and leans in to give her a gentle kiss."
        "Jessica, though, isn't in the mood for romance. Her face remains set in a pout."
        Jes "Good. Would you take care of the dishes? I'm gonna go say hi to Laura."
        Con "Yeah. Sure."
        "She gets up without another word and strolls over to the couch."

        scene day6 ev06-10a
        "Jessica plops down heavily onto the couch, sighing heavily."
        Lau "Hey. Trouble in paradise?"
        "Laura flicks her head over toward Conner."
        Jes "Oh, we had an argument, and now Conner's being stubborn."

        scene day6 ev06-11
        Lau "What happened?"
        "Jessica mulls the question in her mind."
        JesT "How do I tell my sister we screwed another woman and now Conner's feeling guilty?"
        Jes "I'll tell you later."
        "Laura smacks her lips, her eyes narrowing."
        Lau "Ooh. Okay. Sounds intense."
        "Jessica shrugs."
        Lau "Well, wanna play for a bit? Take your mind off whatever it is? I promise I'll let you win."

        scene day6 ev06-12
        "Jessica agrees, and the pair sit playing for a little while."
        "True to her word, Laura holds back, mainly driving just behind Jessica and running interference."
        "The gesture is appreciated, but Jessica is finding no joy in the game."
        Jes "Hey, I think I'm gonna go get some chores finished."
        Lau "Oh. Okay."
        "Laura sucks in her lips, which Jessica recognizes as Laura holding back what she wants to say."
        "She doesn't inquire further, which Jessica appreciates."
        JesT "Right now, I really just want to fume for a bit."

    else:
        scene day6 ev06-05b with fade
        "As she finishes her meal, Conner comes over and plants a kiss on her cheek."
        "She smiles, glad to have him paying her a little attention."
        Con "Hey, babe."
        Jes "Hey, sweetie. Done with your game?"
        Con "For now. Your sister's a cheat."
        Lau "You just suck!"
        Con "Ugh. Anyway, how's your day been?"
        Jes "Pretty good, actually. Uneventful, but kind of relaxing."
        Jes "It looks like Laura's kicking your butt."
        Con "Yeah, she's evil."
        Con "I remember being better at video games. Maybe Laura just got better."

        scene day6 ev06-06b
        "Conner sits down, taking Jessica hand in his own."
        Con "So, what else did you have planned for today?"
        Jes "Well, Mom's going to be by later, so for now I'm just going to hang out, relax… maybe get wasted before she gets here."
        "Conner laughs."
        Con "Come on. Your mom's not that bad."
        Jes "I know. I'm just joking. Kind of."

        scene day6 ev06-07b
        Con "I'm looking forward to seeing Sara again. It's been way too long."
        Con "Of course, that does mean we'll need to be silent again, just like the other night."
        "Jessica laughs and shakes her head."
        Jes "These walls are thinner than we thought."
        Con "Huh? Wh… what do you mean?"
        "Jessica smiles slyly and nods her head toward Laura."
        Con "Oh."
        Jes "We'll just save it for another night, okay, sweetie?"

        scene day6 ev06-08a
        Con "Well, that's a shame, but yeah. It's probably best."
        "He leans in, planting a soft kiss on her mouth."
        "She smiles against his lips, and gives him a quiet moan."

        scene day6 ev06-08b
        Con "But we should do something special once we have time to ourselves."
        Jes "Hmm. I'll think of something special we can do. Something fun."
        Jes "For now, though, there's something you can do to please me."
        "Conner smiles and leans in."
        Con "What's that, babe?"
        Jes "Do the dishes."
        Con "Ooh! That's just mean."
        "Jessica laughs and kisses his forehead before rising to go to the couch."

        scene day6 ev06-10b
        "She tussles Laura's hair as she passes by and plops down onto the sofa, giving her sister a warm smile."
        Lau "Hey Jess. Did you come to lose in Conner's place."
        Jes "Oh please. You can kick Conner's ass, and he's way better at this than me."
        Lau "Come on! Give it a try. I'll even play with a handicap. I won't use items. That's fair!"
        Jes "No, that's not fair! You're still gonna run circles around me. But what the hell. I'll give it a try."

        scene day6 ev06-13
        "After a few minutes of gameplay, Conner comes up behind Jessica and gives her a hug."
        Con "Hey babe. Doing well?"
        Jes "No. My sister's lack of a life means she has time to practice this game."
        Lau "And learn how to kick your a-a-a-a-a-ss."
        Jes "Why am I in this box?"
        Con "That's the mode, Jess. You try and put the other team in jail."
        Jes "Why is there a jail in the first place? Isn't this a go-kart game?"
        Lau "Yeah. A go-kart game with a jail for bad playaaaaaas!"
        Jes "Okay. You know what? I'm done."
        "Jessica stands up, putting the controller down and walking away."
        Lau "Oh come on. I was just messing around, Jess."
        Jes "I have things to do anyway. Feel free to keep embarrassing Conner, though."
        Lau "Good idea. Conner, sit your ass down so you can lose!"


    scene day6 ev06-14 with fade
    "Jessica does a few chores around the apartment, listening to the sounds of the game all the while."
    "Neither Conner nor Laura seem particularly interested in helping out, but Jessica hardly finds that surprising."

    if "d053some" in choices:
        "While putting away her laundry, the sight of her own panties sends her mind goes back to the sight of Christian and Heather together. It puts a smile on her face."
        JesT "I should go see how she's doing, and I guess I should talk to her about Conner's problem."
        JesT "Plus, it's an excuse to get out for a bit. I can only take the sounds of Mario Kart for so long before they become grating."

        jump day06visitHeatherAfternoon

    else:
        scene day6 ev08-01 with fade
        "After finishing her chores, she gets back to the living room. Conner and Laura are still going at it. Jessica is hardly surprised."

        jump day06hiMum

label day06visitHeatherAfternoon:

    scene day6 ev07-01 with fade
    "Jessica arrives at Heather's a minute later, her neighbour answering the knock by shouting for her to come in."
    "Inside, Heather is lounging on her couch, reading, and she gives Jessica a smile as she enters."
    Heath "Hey, Jess. How's it going?"
    "Jessica shrugs."
    Jes "Not bad, could be better. I thought I'd come over and see how you're doing."
    Heath "I am wonderful! Thanks for asking."
    "She pats the cushion next to her."

    scene day6 ev07-02
    "Jessica takes a seat, though she's hesitant to broach the subject Conner had brought up earlier."
    Jes "So, last night was… a hell of a lot of fun."
    Heath "It was. I'm so glad you were both okay with it."
    Jes "Well, speaking of that, there was something I wanted to talk to you about."
    Heath "What's up? What'd you want to talk about?"
    Jes "Okay, it's not something I really want to talk about at all, but I don't really have a choice."
    Jes "So… Conner's a little worried. About Christian. He feels bad, and worries that Christian's going to take it the wrong way. He'd like to talk to him about it."
    Heath "Trust me, there's no problem. He already knows, and he's fine with it."
    Jes "He knows already?"
    Heath "Yeah. He called me a few hours ago, and asked how dinner went. And I told him."
    Jes "I see. So, if Conner wanted to talk with him..."
    Heath "I see no harm in it. I'm sure Christian would set his mind at ease."

    scene day6 ev07-03
    Jes "Okay. So... I mean… how does that system work? You both just sleep with whoever you want to?"
    Heath "Pretty much. We give each other the freedom to have fun when we want to, but we're always honest about it."
    Heath "I actually haven't slept with anyone other than Christian in a while. I guess I'm getting older."
    "Jessica laughs."
    Jes "You sure as hell looked pretty damn young the other night."

    scene day6 ev07-04
    "The two chat for a while longer about nothing in particular. After a while, Jessica nods to the book."
    Jes "What are you reading?"
    Heath "Oh, just a romance novel. Here. Take a look."
    Jes "Sure. \"Nathaniel's calloused hands spread Julia's thighs apart. His rough fingertips sent a jolt of ecstasy up her spine as they slid along her sensitive skin. She resisted, just a bit, but soon relinquished herself to him, revealing her glistening treasure…\""
    Jes "Oh my."
    "Heather laughs."
    Heath "Hey, a girl has to keep herself entertained when she's alone, right?"
    Jes "I thought that's what we did last night."
    Heath "Yeah. Last night. What have you done for me today?"
    "Both of them laugh, Jessica doing so hard enough that her eyes tear up."

    scene day6 ev07-05
    Heath "Although, if you did want to keep me company, we could go out tonight."
    Heath "Have ourselves a girls' night out!"
    Jes "I can't. My mom's coming over soon, and she'll be staying the night."
    Heath "Oh poo."
    Jes "Would you like to come over? We'd be happy to have you."
    Heath "That's okay. I'm fine here. I have Nathaniel, after all."
    Heath "Besides, I'm guessing your mother isn't ready to meet your bisexual friend you shared with your boyfriend the other night."
    Jes "Yeah, you're probably right about that."

    scene day6 ev07-06
    Jes "I am free tomorrow, though."
    Heath "Fantastic! We'll get out and have some fun together, just the two of us."
    Jes "I can't wait. I'd better get back and get ready for my mom. I'll call you tomorrow."
    Heath "Have a wonderful night, sweetie."
    "The pair exchange a quick kiss before Jessica rises and heads back to her own apartment."

    scene day6 ev08-01 with fade
    "Back at home, Conner and Laura are still going at it. Jessica is hardly surprised."

label day06hiMum:

    "She just takes a seat, ignoring the game noises and the taunting."
    JesT "I'll see if I can get some work done before Mom gets here."
    "She turns her attention back to the building she visited earlier."

    if "d05victorHJ" in choices:
        JesT "Let's see what I can find."
        JesT "It was built for a tire company decades ago. Most recently it belonged to a company called CellCo."
        "She spends a few minutes searching until she finds some info on the company."
        JesT "Let's see. They made cell-phone parts, it looks like they went bankrupt."
        "She keeps digging, but can't come up with anything that helps."
        JesT "Damn. I'll need to make some calls tomorrow. See if I can find anything else."

    else:
        JesT "What was the name of that company? CellCo."
        JesT "Let's see what I can find."
        "She spends a few minutes searching until she finds some info on the company."
        JesT "They made cell-phone parts, it looks like they went bankrupt."
        "She keeps digging, but can't come up with anything that helps."
        JesT "Damn. I'll need to make some calls tomorrow. See if I can find anything else."

    if "d05heatherFinger" not in choices and "d053some" not in choices:
        scene day6 ev08-02
        "A short while later, Jessica's phone rings. A picture of Heather comes up on the screen."
        Jes "Hi, Heather. What's up?"
        Heath "Hi, Jess. I'm bored, and I was wondering if you want to head out tonight? Have ourselves a girls' night out?"
        Jes "I can't. My mom's coming over soon, and she'll be staying the night."
        Heath "Oh poo."
        Jes "I am free tomorrow, though."
        Heath "Fantastic! We'll get out and have some fun together, just the two of us."
        Jes "Alright. See you tomorrow."
        Heath "Bye."
        "Just as Jessica is about to put her phone down another call arrives, this time it's her mother."

    else:
        scene day6 ev08-02
        "A short while later, her phone rings. A picture of her mother comes up on the screen."

    Jes "Hey, Mom. How's it going?"
    Sara "Hey, Jessica. I'm on my way. I should be there in about ten minutes."
    Jes "Okay. We'll see you soon."

    scene day6 ev08-03
    Jes "Okay. Mom's almost here."
    Jes "Conner, would you mind going down and helping Mom with her luggage?"
    Con "Really? How much luggage does she have?"
    Jes "Not much, but I'm sure she'd appreciate the gesture."
    Jes "Besides, she hasn't seen you in so long. She'd love if you were there to greet her."
    Con "Alright. I'll head on down."
    Jes "Great. I'll put some coffee on for Mom. You know how she gets without her caffeine."

    scene day6 ev08-04
    "Laura shuts off the game, putting the controller back beneath the table."
    Jes "You're still trying to hide those from Mom?"
    "Laura nods and sighs."
    Lau "Yeah. Mom still likes to complain that I play video games too much."
    Jes "Well, maybe you do."
    "After making a rude gesture, Laura blows her tongue at Jessica."

    scene day6 ev08-05 with fade
    "A short while later, the door opens and Jessica's mother Sara comes through the door, Conner close behind."
    Jes "Mom! It's so great to see you!"
    Sara "Hello, sweetie. You're looking wonderful, as always."
    Jes "Thanks, Mom."
    Sara "Hello, Laura."
    Lau "Hey, Mom."
    Jes "Can I get you some coffee?"
    Sara "I'd love some, sweetie."

    scene day6 ev08-06
    "Sara takes a seat at the table, Jessica fixing her mother's drink and bringing it over."
    Jes "Here you go, Mom."
    Sara "Thanks, Jessica."
    "She takes a sip."
    Sara "Mmm, perfect. I really needed this."
    Jes "Was your trip here okay?"
    Sara "Oh goodness, no. First Class was filled, and I had to fly coach. No wonder people are always complaining about flying."
    Sara "I haven't been so cramped in years, and I'm pretty sure someone grabbed my ass as I walked by."
    Sara "What a nightmare experience. I'd like to own an airline just so I could close it down."

    scene day6 ev08-07
    Sara "Regardless, I'm here now, so at least that's over."
    Jes "Well, it's good to have you. How's the business goin'?"
    Sara "Very well, though it would be far better if I had my daughter there to help run it."
    "Jessica just sighs, used to Sara's complaints about not working in the family business."
    Sara "Our profits this year have been incredible. I'm even thinking about expanding."
    Sara "Maybe even open up another office here."
    Jes "That's fantastic."

    scene day6 ev08-08
    "Laura comes over and takes a seat."
    Lau "Tell her about the naked guy?"
    Jes "The what now?!"
    "Sara rolls her eyes and sighs."
    Sara "We had a party last Christmas, and one of our potential partners got drunk and stripped."
    Lau "Right in front of everybody!"
    Sara "It was pretty embarrassing, but at least it got the party going."
    Sara "Anyway, pictures were taken, and now he's one of our primary investors."
    Jes "You're blackmailing him?"
    Sara "Oh no. The pictures are already out there. I think he just wants to maintain a good relationship, lest I sue him or something like that."
    Sara "He's a good man. Just needs to keep his pants on, is all."

    scene day6 ev08-09
    Lau "A good man with a huge dick. I've seen the pictures. I keep telling Mom she should date him."
    Sara "And I keep telling you that such talk is entirely inappropriate. You shouldn't say such things to your mother."
    Lau "What? I just want you to be happy… and the big dick is just a bonus."
    Sara "Oh my god. Jessica, your sister listens to you. Please silence her."
    Jes "Pfft. She never listens to me. Like that one time in high school when I told her not to sneak..."
    Lau "Hey!"
    Jes "There. That should do it."
    Lau "Traitor."

    scene day6 ev08-10
    "After a few more minutes of small talk, Conner joins the ladies."
    Sara "So Conner, what are your plans now that you're back?"
    Con "Well, my job keeps me pretty busy right now. I have a position helping out other veterans."
    Con "I have some other things in mind, but for now I'm happy reacclimating there and helping out people whenever I can."
    Sara "You're so sweet, Conner. You and Jessica go well together."
    Sara "I'm so happy to have you back. Maybe now I can see one of my daughters married."
    "Snickering, Laura hides her smile behind her fist, holding back laughter."

    scene day6 ev08-11
    "Conner and Jessica share an awkward look. Conner blushes, and lowers his gaze to his drink."
    "Laura continues to giggle while looking over at him."
    Jes "Anyway, I should get the sleeping arrangements ready."
    Sara "Oh, no worries, sweetie. I had plans to check into a hotel."
    Jes "Oh, come on, Mom. You can stay here with us."
    Jes "You can have the guest bedroom. Laura can take the couch for tonight."
    Lau "Wait, what?"

    scene day6 ev08-12
    "Sara fixes her daughter with a stern gaze, and Laura seems to wilt."
    Lau "Oh yeah, the couch! That's exactly what I was going to say."
    "Exasperated, Sara shakes her head."
    Sara "If it were up to you, I'd already be in a nursing home."

    scene day6 ev08-13
    Lau "Oh, come on, Mom. That's not true."
    Lau "You know I love you. I would sleep on the floor for you, like a cat. A cute little kitty-cat."
    Sara "You're not bringing a cat home, Laura."
    Lau "But they're so cuuuuute!"
    "A small shake of the head and a sip of coffee from Sara tells Laura that her pleas fall on deaf ears."
    Lau "Anyway, Let's go get the room ready for you."
    Sara "Yes, I think I'll get changed. I've had a long day, and my feet are killing me. I need to get out of these shoes."

    if "d053some" in choices:
        scene day6 ev08-14
        "With the other two away, Jessica turns to speak quietly to Conner."
        Jes "So, I talked to Heather. Christian already knows, and she says it would be fine if you wanted to talk to him."
        Con "Wait, he already knows?"
        Jes "Yeah, she told him."
        Con "What? I mean…"
        Jes "Apparently, that's how they work. They fuck other people, and make sure to be honest about it. No secrets."
        Con "That's… really freaking weird."

        scene day6 ev08-15
        Jes "You didn't seem to think it was weird last night."
        Con "Fair point. Still, I have no idea how a relationship survives under those sort of conditions."
        Con "And speaking of that, I'm really sorry about… you know, kind of freaking out earlier."
        "Jessica smiles and puts her hand over his."
        Jes "Well, I probably overreacted. This isn't a normal situation for us."
        Con "No kidding. Maybe we should talk about these things in the future before trying anything like that again."
        Jes "That's probably smart."
        "Pulling him closer, she plants a kiss on his forehead."

    else:
        scene day6 ev08-16
        Jes "So, sweetie. Shall we run out right now and get married? Fly to Vegas and just get it done."
        Con "Don't encourage your mother, or she won't give it up."
        Jes "I know. She just wants us to be happy, is all. It's been worse since Dad died."
        Con "You're happy, right?"
        Jes "I'm so happy with you, but if you get down on one knee and propose right now, we're done."

        scene day6 ev08-17
        "Conner laughs."
        Con "Right, cause what we need right now, in addition to both our busy schedules, is wedding planning. That never caused anyone any stress."
        Con "Or you can tell me you're pregnant and give me a heart attack."
        Jes "Well…"
        Con "N- wh- no…"
        "It's Jessica's turn to laugh."
        Jes "Don't worry baby. I'd like to be young and have a life for a little while longer too."
        Con "Please don't do that to me again."
        Jes "I won't, sweetie. I love you."
        Con "I love you, too."
        "The pair share a passionate kiss, Jessica happy that she's with a man that makes her feel so wonderful."

    scene day6 ev08-18 with fade
    "Jessica returns to her desk to do a little more work. A little while later, her mother comes back out, now changed."
    Sara "So, tell me about your work, sweetie. How's the new job?"
    Jes "It's going really well, actually. I saw my first byline."
    Sara "Already? Wow."

    if "d02cutAngus" in choices:
        Jes "Yeah. I helped a colleague uncover some shady dealings between the city and a local construction company. On top of that, I interviewed the mayor the other day."
    else:
        Jes "Yeah. I interviewed the mayor the other day. Not quite the man I thought he was, actually."

    Sara "That's wonderful news. The kind of news that one would normally call her mother to talk about."

    scene day6 ev08-19
    Jes "Well, it wasn't much, Mom."

    if "d02cutAngus" in choices:
        Jes "Just a gesture from a colleague and a casual interview."
    else:
        Jes "Just a casual interview."

    Jes "I promise that as soon as something real happens for me, I'll call you immediately."
    Sara "Alright. I understand. Still, you shouldn't sell yourself short. What you've done is impressive for one week of work."

    scene day6 ev08-20
    Sara "So, sweetie, what did you have planned for this evening?"
    Jes "I figured we'd stay in and have a nice family dinner. It's not like we get together that often."
    Sara "Oh, you don't need to stay in on my account, Jessica."
    Jes "Of course I'm gonna spend time with you, Mom! You're not in town that often!"
    Jes "I can always go out some other time."
    Sara "You're sweet, Jessica."
    Jes "I miss all our dinners together, especially when you made lasagna."
    Lau "Nom nom nom. It is really good."
    Sara "I'd love to make it for you. Hell, why don't we make it together while I'm here?"
    Jes "I'd love to!"
    Sara "Plus, we can finally teach Laura how to make it, so she damn well doesn't end up alone."
    "Laura scoffs."
    Lau "Geez, Mom! I'm right here!"

    scene day6 ev08-21
    Sara "I'll see if you have all the ingredients, and start getting things ready."
    Jes "Okay. I'll finish up here and head in to help out."
    "Sara starts toward the kitchen, turning to Laura as she passes."
    Sara "And you should join us too, Laura."
    "Laura rolls her eyes, then nods."
    Lau "Okay, fine."

    scene day6 ev08-22
    "With Sara having moved into the other room, Laura twists her face and quietly mocks her mother."
    Lau "You should join us too. Meh meh meh."
    Lau "I don't know why she's so worried about my cooking skills."
    Jes "Haha. What cooking skills?"
    Lau "Shut up."
    Lau "Besides, there's lots of ways to catch a man. Wearing something as revealing as your top should do the trick, Jess."
    "Jessica blushes, waving away the comment."
    Jes "True enough. It's not hard to attract a man, especially for someone as pretty as you."
    Lau "Oh, now you're just patronizing me."
    "The ladies share a laugh and chat for a little while, until Sara calls to them from the kitchen."
    Lau "The chef is calling."

    scene day6 ev08-23
    "Laura heads into the kitchen to help her mother, while Jessica tries to wrap up her work."
    "Conner heads over and gives her a hug from behind."
    Con "Happy to have your mom around?"
    Jes "I really am. And I know you're happy, since Mom's cooking."
    Con "Yeah, her food is amazing. I'm just worried since your sister's helping."
    Jes "I'll make sure she doesn't ruin everything. You'll be able to stuff your face soon."
    Con "You know, your mother's cooking is why I started dating you. I wanted a woman who could cook like she does."
    Con "It's a good thing I fell in love before I found out kitchen skills aren't hereditary."
    "Jessica gives a hearty laugh and smacks him with the back of her hand."
    Jes "You're such an asshole."
    "She starts to stand."
    Jes "I'm gonna go help them out. Care to join us?"
    Con "Nah, you guys have your family time. I have a few calls to make anyway."

    scene day6 ev08-24
    "Jessica heads into the kitchen, pulling her sister into a hug."
    Jes "How's it going? You haven't burned everything yet, have you?"
    Lau "Jess, I'm holding a knife."

    scene day6 ev08-25
    Sara "Come on you two. Do I really need to remind you that you're grown women."
    Jes "Oh, Laura will always be my baby sister. MWA!"
    Lau "I love you too, Jess. Now let me go."

    scene day6 ev08-26
    "The three of them spend some time cooking and chatting."
    "Sara mostly questions Jessica about her job, trying to draw as many details out of her as possible."
    "Jessica, exhausted, tries to turn the conversation away from work."

    scene day6 ev08-27
    "Once the lasagna is in the oven, the group takes a seat at the table."
    Jes "Enough about my work. Mom, how are things going with your work?"
    Jes "What's up with this meeting you have tomorrow?"
    Sara "I'm meeting a potential partner for our office here in the city."
    Jes "Really? That's great!"
    Lau "I bet it's a date. Mom's going out!"
    Sara "No, it is not a date."
    Jes "Mom! Are you dating again?! You should tell us if you are!"
    Lau "Yeah, Mom! No need to hide it! What's he like?!"
    Sara "You're both being silly. My dating days are long behind me."
    Jes "That's not true, Mom!"
    Lau "Mom, have you seen your ass lately? Every guy who walks by you has to check it out."
    Sara "No, sweetie. When we're together, it's not me the men stare at."
    Sara "Speaking of, though, I have to get something ready for tomorrow. Keep an eye on the food."

    scene day6 ev08-28
    "With Sara gone, Jessica leans in closer to Laura."
    Jes "You mentioned something on the phone about Mom dating someone, right?"
    Lau "I just kinda suspected."
    Lau "She's always talking on the phone with someone, and it doesn't sound like work talk."
    Lau "Plus she always leaves the room when they speak. Tell me she's not banging someone."

    scene day6 ev08-29
    Jes "First off, eww. Second, is she going out in the evenings?"
    Lau "Not that I've seen, at least when I'm home."
    Jes "I mean, it doesn't seem like she would just go on dates in the daytime."
    Lau "Unless she's trying to throw me off the trail!"
    Jes "Oh, Jesus."
    Lau "I'm serious. Besides, how do you know how old people date?"
    Jes "Mom isn't that old."
    Lau "I know. That's not what I meant. She's still hot. Even Conner checks her ass out sometimes."
    Jes "He… does not."
    "Despite her protest, Jessica still briefly casts a glance his way. She feels foolish when she hears Laura snorting."
    Lau "Gotcha!"
    Lau "The point is, she doesn't do the whole nightclub thing, or stuff like that. Late night stuff."
    Jes "I'm really curious now. If she is seeing someone, I want it to go well. She should be happy, but she's practically working herself raw."
    Jes "She has been ever since Dad died."
    Jes "Keep an eye on her. See if you can find out anything else."
    Lau "\"Mission: Spy On Mom\" is a go!"

    scene day6 ev08-30 with fade
    "Eventually, when the food is ready, Jessica calls her mother over."
    Jes "Grub's up, Mom."
    Sara "Be right there."

    scene day6 ev08-31
    "All four of them take a seat and dig into the meal."
    Sara "So Jess, what's this story you're working on?"
    Jes "Well, it might not be going anywhere, but I'm looking into that vigilante."

    scene day6 ev08-32
    Sara "Really? Found anything interesting?"
    Jes "Lots of dead ends. We had a picture of him on his motorcycle, and I even found the guy who modded it. Found where he delivered it, too."
    Jes "It looks like a dead end, though. Empty warehouse. No one's been there for a long time."
    Con "Babe, please be careful. This doesn't sound safe."
    Jes "Don't worry. I'm not taking any big risks."

    if "d05victorHJ" in choices:
        if slut >= 15:
            JesT "Though I did get to give a guy a handjob."
        else:
            JesT "Though I did have to give a guy a handjob. Ugh."

    Sara "I'm not sure I like this either."
    Jes "Mom, this is what my work is. It's perfectly safe. Most of the time I'm sitting in a cubicle doing paperwork."

    scene day6 ev08-33
    "The conversation goes on for a bit, eventually turning to Sara."
    Con "Did I hear something earlier about you opening an office in New Port?"
    Sara "You did indeed."
    Con "Are you going to be coming over more often? Cause I'll be a very happy man if you'll be cooking for us more often."
    Sara "I'd love to! And maybe I can teach my daughters a thing or two while I'm here."
    "Both Jessica and Laura share a look, but say nothing and just keep eating."

    scene day6 ev08-35
    "They keep happily chatting, pleased not only to have the whole family together, but also with Sara's fantastic meal."

    scene day6 ev08-36 with fade
    "After dinner, while Jessica and Conner clean the dishes, Sara and Laura take a seat on the couch."
    Lau "I'm just saying, Mom, pot is like the official plant of college. I've literally seen a pot plant growing over someone's bed."
    Lau "You can't walk down the hall without someone blowing it in your face."
    Sara "I'm sure you're exaggerating, but given that I paid thirty-thousand dollars for tuition, you better not get kicked out for smoking, Laura."
    Lau "I'll be fine, Mom."

    scene day6 ev08-37 with fade
    "Jessica and Conner soon finish cleaning and join the others."
    Con "So, shall we relax and watch a movie?"
    Lau "Alien!"
    Jes "God no, Laura. We are not watching Alien for the tenth time!"
    Sara "Why do you always want to watch such violent movies?"
    Con "It's not her fault her taste in movies is AWESOME!"
    Lau "Thank you!"
    "Laura puts her hand up, Conner giving her a high-five."

    scene day6 ev09-01
    "Deciding to be both stubborn and silly, Laura insists on a movie with an alien."
    "Eventually, the group settles on \"The Day The Earth Stood Still\"."

    scene day6 ev09-02 with fade
    "Once it's over, Sara rises and stretches."
    Sara "Okay, I need to get some sleep. Have a good night everyone."
    Lau "Night, Mom."
    Jes "See you in the morning."
    Jes "Come on, Laura. I'll help you set up the couch."
    Con "Alright, I'm gonna go finish my book. You two have fun."

    scene day6 ev09-03 with fade
    "The ladies change and lay out the bedding. Laura groans when she sees the result."
    Jes "What? It looks cozy."
    Lau "Tell that to my back in the morning."

    scene day6 ev09-04

    if "d053some" in choices:
        "Jessica, eager to talk to someone about what's been going on in her life, takes a seat next to Laura."
        Lau "So… you gonna tell me what's going on with you and Conner?"

        scene day6 ev09-05
        JesT "This is a weird thing to talk about with my sister, but I really need to talk to SOMEONE."
        JesT "At least, someone who wasn't involved in last night."
        JesT "And we've always shared everything."
        Jes "Conner and I… we kind of had a thing last night. With Heather."
        Lau "What is ‘thing'? What does that mean?"
        Jes "A… sex… thing."
        Lau "A sex thing!"
        "Laura gasps."
        Lau "You two had a threesome with Heather?"

        scene day6 ev09-06
        Jes "Shh! Keep it down."
        Jes "Yes, we did."
        Lau "Oh my god. How did it happen? Did you plan it? Isn't she married? Was she a good kisser?"
        Jes "Okay, calm down. Heather and Christian have an open marriage. There was no cheating."
        Jes "And we didn't plan it. It kind of just happened."

        scene day6 ev09-07
        "Laura grins."
        Lau "Did you like it? Did you have fun with another woman?"
        Jes "You are so bad… and yes. It was fantastic."
        Lau "Oh my god! Details! I need details!"
        Jes "It was a threesome. You know? Conner fucked her, I fucked her. And yes, she's a very good kisser."
        Lau "You gonna do it again? Maybe with a different woman?"
        Jes "I don't know. Maybe."
        "Jessica can't help but grinning like an idiot and blushing crimson."

        scene day6 ev09-08
        Lau "But wait. Why did that make you two argue?"
        "Jessica sighs."
        Jes "Conner felt guilty afterward, and wanted to square things with Christian. I kind of felt like he was basically excluding both me and Heather from the equation."
        Jes "Like swapping partners is just a deal between bros."
        Lau "Oh, that's just how guys talk. I'm sure he didn't mean anything by it."
        Jes "It doesn't matter now. I talked to Heather, and everything's fine."
        "Laura giggles."
        Lau "Wow. I can't believe my sister is such a sllllllut."
        Jes "I am not a slut."
        Lau "Do I need to remind you that you just fucked your hot neighbor? You little bisexual slut."
        Jes "Okay. Maybe I'm a little slutty."

        scene day6 ev09-10
        Jes "Enough about my problems, though. What happened to that guy you were seeing?"
        Lau "Ugh. He was good and all, but he was moving WAY too quick."
        Lau "He wanted the whole family, white-picket fence, all that."
        Lau "Some girls may be looking for that, but I'm not. I'm too young and have too much to experience to chain myself to that kind of life. Yech!"

        if slut >= 15:
            Jes "Oh yeah. I get it."
            Jes "You're young and pretty. Don't waste that by doing the Betty Crocker thing."
            Jes "Have some fun while you can."
            Lau "Exactly. Like have a threesome with your cute neighbor."
            "Jessica grins."

        else:
            Jes "Are you sure you're not missing a great guy just because you want to have some fun?"
            Lau "He is a great guy, but he's not MY great guy, and I don't think I need one just yet."
            Jes "Okay. I hope you see him when he comes along."
            Lau "Eh. I'm sure I can find a great guy when the time comes. If Mom's any indication, I'll be hot for a long time, so I should have my pick."

    else:
        "Jessica sits down next to Laura, wanting to get a few minutes alone with her sister."
        "They chat for a bit about nothing in particular."
        Jes "Oh, I wanted to ask, what happened to that guy you were seeing?"
        Jes "I thought you liked him."

        scene day6 ev09-10
        Lau "Ugh. We just… we did not click."
        Jes "He seemed like a good guy."
        Lau "I guess. That's kind of the problem."
        Lau "He was the whole family, white-picket fence, dog in the yard sort of dude. Scared the shit out of me."
        Lau "I mean, I liked it, but not that much. He started talking about our future, and I was pretty much done."
        Jes "Wow. That was quick. You weren't even together that long."

        scene day6 ev09-11
        Lau "I'm sure he can find some other girl who wants that life, but fuck that. I'm way too young for that bullshit."
        Lau "And with school, I've barely been able to have any fun. I'm not settling down already."
        Lau "There's too much life to be had, you know?"

        if slut >= 15:
            Jes "Oh yeah. I get it."
            Jes "You're young and pretty. Don't waste that by doing the Betty Crocker thing."
            Jes "Have some fun while you can."
            Lau "Exactly."

        else:
            Jes "Are you sure you're not missing a great guy just because you want to have some fun?"
            Lau "He is a great guy, but he's not MY great guy, and I don't think I need one just yet."
            Jes "Okay. I hope you see him when he comes along."
            Lau "Eh. I'm sure I can find a great guy when the time comes. If Mom's any indication, I'll be hot for a long time, so I should have my pick."

    scene day6 ev09-12
    "Jessica laughs, planting a kiss on Laura's forehead before she stands."
    Jes "I should get to bed, too. Sleep well, Laura."
    Lau "Sure. I mean, Mom could easily afford a hotel, but I'll sleep on the couch instead. That's fair."
    "Jessica rolls her eyes and shakes her head as she turns away, heading to her bedroom."

    scene day6 ev09-13
    "She climbs into bed with Conner, who's still awake and reading his book."
    Con "Hey. What took you so long?"
    Jes "I just had a chat with Laura. A little sister time."
    "Conner smiles, closes his book and gives Jessica a smile."
    Con "So, thin walls, eh?"
    Jes "Very thin."
    "Conner stays silent for a bit, a silly smile on his face."
    Jes "What?"
    Con "You're saying Laura heard us having sex the other night?"
    Jes "She did."
    Con "That's kind of naughty…"
    "Jessica snorts and slaps his chest."
    Jes "Maybe Mom's right. Our entire family acts like children."
    "Conner just smiles and gives her a kiss."
    Con "Good night, babe."
    Jes "Good night."

    jump day07
