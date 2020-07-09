label day05:

    scene day5 with fade
    "DAY 5"

    scene day5 ev01-01a with fade
    "Sleep fades. The day returns. Briefly, Jessica's dream holds her in its hands, and her mind wonders that the days are all the same, yet always so very different."
    "Then it's gone, and she wakes to the comforting feeling of Conner's warm body at her side."

    scene day5 ev01-01b
    JesT "Hey, baby. I hope you slept well too."
    JesT "I really should have cleaned up after sex last night. I feel kind of icky."

    if slut >= 10:
        JesT "Although it's a good kind of icky. Really dirty. I've been a dirty girl a lot lately."
        if "d04parkerNoApology" in choices:
            JesT "And after flirting with Mr. Parker yesterday, I should feel positively filthy."

    JesT "Hopefully today will give me a chance to relax. With all that happened yesterday, I'm really exhausted."
    JesT "Things have been so damn hectic."

    scene day5 ev01-02
    JesT "I still can't believe I got to interview the mayor, and that it went so well."
    JesT "Even with his eyes on my legs. It's kind of amazing what just a hint of thigh can do to a man, even an experienced politician like him."

    if "d04mayorTease" in choices:
        JesT "It's even more amazing how much you can get if you show off a little more. I'm glad I did. Getting another interview so soon is almost too good to be true."

    JesT "I need to check and see if David got back to me with that guy's number. If so, I'll have to go see him. This day could be just as hectic as yesterday."
    JesT "But I should get going if I'm gonna go jogging with Heather."

    scene day5 ev01-03 with fade
    play sound sink_water_1
    "Still fighting off sleep, Jessica begins to get ready for her day."
    "Her stomach is already rumbling, and she's eager to get some food before her run."
    stop sound

    scene day5 ev01-04 with fade
    "While fixing pancakes, Jessica hears Laura come in."
    Jes "Hey, Laura."
    Lau "Hey, Jess. Gotta pee!"
    "Jessica just nods and turns her mind back to her growling stomach while her sister rushes off to the bathroom."

    scene day5 ev01-05a with fade
    "Sitting down to breakfast, Jessica digs in, while her sister's mind seems to drift off."
    Jes "Still tired?"
    Lau "A little. Where's Conner?"
    Jes "He's tired. I tried to get him up, but he wouldn't budge."
    Jes "I'll let him sleep. His job can be exhausting."
    Lau "Ah."
    "Laura says nothing else for a moment, her mind wandering while her cheeks turn red."
    JesT "Seriously? I say anything about my boyfriend, and she gets all bashful."
    Jes "Really? With the blushing?"
    Lau "Sorry, I just, um..."
    Jes "What?"
    Lau "You two weren't as quiet as you thought last night."

    scene day5 ev01-05b with dissolve
    "Suddenly embarrassed, Jessica turns away and shields her face, hoping in vain that Laura doesn't see that she's blushing."
    Lau "Wow. I guess it runs in the family."
    Jes "What, shame?"
    Lau "You have no shame, Jessica."

    scene day5 ev01-05c with dissolve
    Jes "I'm sorry. We'll try to keep it down in the future."
    Lau "Well, I mean, it's your place, and it's not really a problem."
    Lau "It's just... weird to hear my sister having sex."
    Lau "I mean, remember when you heard Mom and Da-"
    Jes "DON'T remind me."

    if persistent.pov == 2:
        scene day5 ev01-06fpov
    else:
        scene day5 ev01-06
    "The two chat a bit as they eat, about nothing in particular."
    "Jessica ravenously devours her meal, as usual, her mind already turning to the rest of her day."
    Lau "So I probably won't be coming back tonight, after all. My friend Kara's gonna meet up with us, so I'll crash at her place."
    Jes "Okay. Oh, hey, I'm gonna go out running with Heather before I head to work."
    Lau "Cool. You mind if I tag along?"
    Jes "Sure. You brought something to run in, I take it? You're not gonna show up in your undies again?"
    Lau "And why not? Are you embarrassed of your sister running around half-naked?"

    scene day5 ev01-07
    "The conversation about Laura in her underwear abruptly ceases as the pair hear Conner strolling in from the bedroom."
    Con "Morning, ladies."
    Jes "Morning, babe."
    Lau "Hey, Conner. Sleep well?"
    Con "Like a baby."
    "Sitting down, Conner immediately grabs the remaining stack of pancakes and wolfs them down."
    Jes "Geez. Hungry, Conner?"
    "Conner speaks with his mouth open, little flecks of food flying out."
    Con "I gotta get going or I'm gonna be late."
    Jes "Okay. Well, we're going for a run with Heather in a few."
    Con "I should be gone by the time y'all get back. Have a great day, sweetie."
    Jes "You too, babe."
    "Before the words are even out of her mouth, Conner's up from his seat, swallowing the last of the meal as he heads back to the bedroom."

    scene day5 ev01-08 with fade
    "The pair quickly dress, meeting back out in the living room."
    Jes "Ready to go?"
    Lau "Yep. Let's go kill some evil calories."

    scene day5 ev02-01 with fade
    "A minute later, the pair knock at Heather's door."

    if "d02hotRun" in choices:
        JesT "God, she's beautiful."
        "Jessica and Heather's eyes meet ever so briefly in a moment of shared emotion."
        Heath "Hey, Jessica. You're looking nice, as always."
        Jes "Thanks, Heather. So are you."

    else:
        Heath "Morning, Jess."
        Jes "Good morning."

    Heath "Hey! Laura, it's good to see you again."
    Lau "You too, Heather. It's been a while."
    Jes "Shall we get going?"
    Heath "Let's."
    play sound neighborhood_1 loop

    if "d02hotRun" in choices:
        scene day5 ev02-02a
        "Heather's arm pulls Jessica close as they descend the steps, a twinkle in her eye."
    else:
        scene day5 ev02-02b

    Heath "So, did you and Conner have fun the other night?"
    Lau "Seriously, can we not talk about my sister's sex life right now? I'm right here."
    "A devious smile comes over Heather's face, along with a quick glance to Jessica, the pair silently agreeing to talk later."

    scene day5 ev02-03
    Heath "So Laura, how have things been with you?"
    Lau "Pretty good. Lots of studying. I'm pretty sure my calculus teacher is trying to fail me. Asshole."
    Heath "What's your major?"
    Lau "Business Finance. It wasn't my first choice, but Mom thought it was a good idea."
    Jes "She wanted to study fine arts, but I talked her out of wasting tens of thousands of dollars."
    Lau "Hey, I would have been a great artist."
    stop sound

    scene day5 ev02-04
    play sound park_1 fadein 2 loop
    Lau "Mom won't get off my back about my grades, though. God forbid I don't get a perfect 4.0."
    Jes "Yeah, I remember. Mom did the same thing with me when I was in college."
    Lau "Oh please, you can do no wrong with Mom. Laura, Jessica just graduated Cum Laude. Laura, Jessica just got a job at a prestigious newspaper. Laura, why don't you have a nice boyfriend like Jessica?"
    Lau "That's every time I talk to Mom, by the way. All we talk about is you."
    Jes "Come on. You're her baby. She dotes on you."

    scene day5 ev02-05
    "Laura shrugs as they as they jog on, none of them more than slightly winded."
    Lau "I'd rather she respect me the way she does you. Wanna trade?"
    Jes "Are you kidding? I don't want Mom to dote on me. I'd have to talk to her every day, and she's just..."
    Lau "Exhausting."
    Heath "I'd like to point out that my mom and I get along wonderfully!"
    Jes "Go ahead, bitch. Rub it in."

    scene day5 ev02-06
    Heath "Is your dad a little less intrusive?"
    Lau "No. He passed away a few years back."
    Heath "Oh, I'm so sorry. I shouldn't have said anything."
    Jes "It's okay. We've had a while to come to terms."
    Lau "We miss him, though, especially around Christmas."
    Jes "And Thanksgiving. Remember his ham?"
    Lau "Oh, it was so good! And now I'm hungry again."
    stop sound

    scene day5 ev02-07
    play sound neighborhood_1 loop
    "Back near their building, Laura's phone buzzes in her pocket."
    Lau "Aw, shit yeah!"
    Jes "What's up?"
    Lau "My friend Kara wants to meet up early to go see her brother. He always has the best weed!"
    Jes "Laura!"
    Lau "Sorry, I meant fashion advice, grandma."

    scene day5 ev02-08
    Lau "I'ma head home and get changed. Later, guys!"
    Jes "Hey, wait, hold on..."
    Heath "Bye, Laura! Good to see you again!"
    Jes "Laura, wait! Oh, damnit."
    Heath "She's so spunky!"
    Jes "I'd call it flighty."

    scene day5 ev02-10
    Jes "Well, great. Now my bathroom's gonna be occupied for the next half hour."
    Heath "Back a day, and already she's hogging the place, is she?"
    Jes "Not really, though I do wish she'd think a little before she acts."
    Heath "Well, if you like we can pass the time at my place? Can I make you some tea or coffee before you head off to work."
    Jes "I'd love some tea. I think coffee might be overkill. Laura always winds me up."
    stop sound

    scene day5 ev03-01 with fade
    "Back inside, Heather heads toward the kitchen."
    Heath "Go ahead and take a seat on the couch. How do you take your tea?"
    Jes "One sugar, please."
    Heath "Sure thing."
    Jes "Is Christian home?"
    Heath "Nope. He'll be out working the whole weekend."

    if "d02hotRun" in choices:
        Jes "So… we're all alone, then?"
        Heath "Yep. You've got me all to yourself."
        "Without turning back, Jessica blushes and smiles."

        jump day05HeatherLesbian
    else:
        jump day05HeatherFriendly

label day05HeatherFriendly:

    scene day5 ev03-02 with fade
    Heath "So, how did things go with Conner after you two left?"

    if "d03dinnerLick" in choices:
        Jes "Well, we tried something new. Conner went down on me."
        "An eager smile comes over Heather's face."
        Heath "And?"
        Jes "And it... wasn't great."
        Heath "Ah. He's not great with his tongue, then?"
        Jes "Definitely not."
        Heath "I wouldn't be too down on him. It was his first time."
        Heath "My advice would be to keep trying, give him tips on how to improve."
        Heath "Who knows? Maybe one day he'll be able to make you scream with his tongue."
        Jes "That does sound wonderful."

    elif "d03spySex" in choices:
        Jes "Pretty good. We went home and had sex."
        "An eager smile comes over Heather's face."
        Heath "Good sex?"
        Jes "It's always good with Conner."
        Heath "You didn't have him go down on you?"
        Jes "Nah. Maybe another time."

    else:
        Jes "We were pretty tired, so we just went home and climbed into bed."
        Heath "That's it? Well, that's no fun."
        "Jessica shrugs."
        Jes "It's no big deal. We had sex last night instead. Poor Laura heard us."
        Heath "If I had a man like Conner, I'd fuck him every night."
        Heath "Oh wait. I do."
        "The ladies share a laugh."

    "Heather looks away for a moment and rubs the back of her neck, as if trying to broach an awkward subject."
    Heath "Hey, can I ask you a question?"
    Jes "Shoot."
    Heath "Did you come back for your phone that night?"

    scene day5 ev03-03
    "Jessica blushes, suddenly reliving memories of Heather moaning as Christian licked her to completion."
    "She's momentarily speechless, and realizes her reaction gave her away."
    Jes "Uh, yeah, I did."
    "Silence pervades for a moment, neither saying a word."
    Heath "So, you just came on in?"
    Jes "Well, I knocked, and I heard music. I figured you two were cleaning dishes, and just couldn't hear me."

    scene day5 ev03-04
    Heath "Shit. You saw us on the couch."

    if "d03dinnerSpy" in choices:
        JesT "Oh, I saw a lot more than that."

    Jes "I'm really, really sorry. I shouldn't have come in."
    "Much to Jessica's surprise, Heather just shakes her head and chuckles."
    Heath "Well, I hope we put on a good show, at least."
    Jes "You're not mad?"
    Heath "Well, I'm a little miffed. You could have just asked. I'd have let you watch. We like having an audience."
    Jes "Wait? Have you had other people watch you two before?"
    "Heather's answer is a mischievous smile."

    scene day5 ev03-05a
    Jes "Oh my god, you're so bad!"
    Heath "So are you, little miss 'spies on her neighbor getting head'. But that's why I love you."
    "Jessica takes another sip of her tea, unsure of what to say."
    Heath "So? What did you think?"
    Jes "Huh?"
    Heath "What did you think? Did you enjoy the show?"
    "Jessica's chuckles, unsure of how to respond."
    Jes "It was... interesting."

    scene day5 ev03-05b with dissolve
    Heath "Interesting? That's all?"
    Jes "It was really hot."

    scene day5 ev03-05a with dissolve
    Heath "Did you touch yourself while you watched?"
    Jes "Heather!"
    Heath "Well? Did you?"

    scene day5 ev03-06
    "Jessica decides to dodge the question by changing the subject."

    if "d03dinnerSpy" in choices:
        Jes "I want to try it with Conner more than ever, now."
        Heath "You should. It's incredible. There's something about seeing a man's eyes gazing up at you from between your legs that's just so incredibly erotic."
        Heath "It's romantic and filthy at the same time, and it makes you just want to scream for joy!"
        Jes "That good?"
        Heath "Better. Seriously, get him to try. You'll love it!"

    elif "d03lickLie" in choices:
        Jes "I just wish Conner had been as good as Christian was. Although... I kind of told him he was."
        Heath "You told Conner he was as good as Christian?"
        Jes "No, no, I mean that I told him I liked it."
        Heath "Even though you hated it?"
        Jes "Yeah."
        Heath "I've been there. Not with Christian. He's a gift from the gods in bed. I meant I've been there with other men."
        Heath "They're not good, and if you tell them the truth they either get mad or get all tryhard when you just want to go to sleep."
        Jes "I almost always cum when Conner fucks me, but this just wasn't any fun, you know?"

    elif "d03lickTrue" in choices:
        Jes "I just wish Conner had been as good as Christian was."
        Heath "What did you tell him after?"
        Jes "The truth."
        Heath "You told him he wasn't good?"
        Heath "Huh. I wouldn't have pegged you for the kind of woman to tell your boyfriend he sucks in bed."
        Jes "He doesn't! I almost always cum when Conner fucks me, but this just wasn't any fun, you know?"

    scene day5 ev03-07
    Jes "What do you think I should do?"
    Heath "I'll tell you what. Why don't I come over tonight?"

    if "d03dinnerSpy" in choices:
        Heath "I can maybe talk it up with Conner, get it in his head that it's his idea to try, and maybe give him a few helpful pointers."
        "Jessica feels herself becoming a little light in the head, both nervous and a little aroused at the idea of another woman talking to her boyfriend about sex."

    elif "d03lickTrue" in choices:
        Heath "I can maybe give him a few pointers, tell him what a woman likes. Maybe that will help him improve."
        "Jessica feels herself becoming a little light in the head, both nervous and a little aroused at the idea of another woman talking to her boyfriend about sex."
        "Proposing it to Conner was one thing. Going through with it feels so very strange."

    else:
        Heath "I can maybe give him a few pointers, tell him what a woman likes. Maybe that will help him improve."
        "Jessica feels herself becoming a little light in the head, both nervous and a little aroused at the idea of another woman talking to her boyfriend about sex."

    Jes "Yeah. Yeah, I think that could be fine."
    Heath "If everything goes well, after I leave Conner will make like Aladdin and take you to a whole new world."

    scene day5 ev03-08
    Jes "You're sure you're comfortable with that? Talking to Conner about our sex life?"
    Jes "Wait, what am I saying? This is you."
    "Heather chuckles."
    Heath "I promise to get your boyfriend licking you like a pro, sweetie."
    Heath "Then we go ahead with the threesome."
    Jes "Wh- what!?"
    "Heather bursts into laughter before giving Jessica's shoulder a squeeze."
    Heath "I'm kidding, sweetie. No worries."
    "Jessica smiles and nods, unsure if Heather is being truthful or not."

    scene day5 ev03-09
    Jes "Thanks, Heather. You're wonderful."
    Heath "I know, and you're welcome."
    Jes "Alright, I should get ready and get to work. I'll see you tonight, then?"
    Heath "I'm looking forward to it."

    jump day05beforeWork

label day05HeatherLesbian:

    scene day5 ev03-10 with fade
    Heath "It's nice to see your sister again. She's such a cutie."
    Jes "Sure, spelled P-A-I-N. She can't stop blushing around the mere mention of Conner."
    "Heather smiles."
    Heath "You two have fun the other night after you left?"
    "Jessica chuckles."
    Jes "Yeah."
    Heath "After you came back for your phone."
    Jes "Um... what? I'm- I'm not sure what you mean."

    scene day5 ev03-11
    Heath "Sweetie, did you come in and see me and Christian together?"
    Jes "Uh... yeah. Sorry. I knocked, and I heard music, so..."
    Heath "What did you think?"
    Jes "What?"
    Heath "Did you like what you saw?"
    Jes "It was... it was beautiful."
    Heath "Yeah?"

    scene day5 ev03-12
    "Heather reaches up, her fingers gently brushing along Jessica's cheek. A shiver of delight passes up Jessica's spine."
    Jes "Yeah. You were beautiful. The look on your face, was... sublime. You looked like you were in heaven."
    Heath "I was. When you're with someone who can make your toes curl, you can't help but show it."
    Heath "How long were you here for? Did you see me cum?"
    "Jessica nods."
    Heath "Any longer?"

    if "d03dinnerSpy" in choices:
        Jes "Um... well..."
        Heath "So you stayed and watched. You saw Christian and I make love."
        "Jessica just gives a small nod."
        Heath "What did you think?"
        Jes "It was incredible. You're both so gorgeous."
        Heath "Did you like the sight of his beautiful cock sliding inside my sopping pussy?"
        "Heather's finger begins brushing across Jessica's lips."
        Heath "Did you like seeing my naked body?"
        Jes "Yes."
        "Jessica's voice is barely a whisper, her eyes now locked with Heather's own."

    else:
        Jes "No. I grabbed my phone and left before you noticed me."
        Heath "So you didn't stay to watch Christian and I make love?"
        "Jessica's lips part, her breath coming quickly as her heart beats harder and harder in her chest."
        Jes "Uh, no. No, I went back and spent some time with Conner."
        Heath "It's a pity you didn't stay. It's a beautiful sight, the two of us having sex."
        Jes "I'll bet."
        "Jessica's voice is barely a whisper, her eyes now locked with Heather's own."

    scene day5 ev03-13
    "Heather is moving closer, her breath beginning to blow across Jessica's cheek."
    Heath "I wish I knew you were here. I would have invited you to join us."
    Heath "Or just me. Oh, Jessica you have no idea how much I've wanted to have some time alone with you ever since we met."
    "Jessica's body feels tingly and heavy. She sits stock still, her only movement that of her chest as it rises and falls with her breath, and her eyes moving to keep Heather's gaze."
    Heath "Here, let's put the tea aside."
    Jes "Okay."
    "Her voice is robotic, her mind speaking without intention. Heather is so close, and her presence has hypnotized Jessica into a state of paralysis."

    scene day5 ev03-14
    "Heather climbs over Jessica, her lips moving closer, her body so close Jessica can feel her body heat."
    JesT "I can't believe this is happening! What the hell am I doing?!"
    "Her mind races, unable to comprehend what was about to take place. This isn't flirting, or groping, or spying on someone fucking. This is so much more."
    "Heather wants to have sex, that was made clear at dinner, and she's making her move."
    JesT "Oh my god, she's so beautiful. So incredible. I want her so badly."

    scene day5 ev03-15
    "The feeling of Heather's hand on her side draws a shiver from Jessica, and the sensation of Heather's lips on her neck draws a gasp of shock."
    "Her body begins to sweat, their slick skin sliding against one another as Heather begins gently grinding into her."
    "She says nothing. She doesn't know what she could say. Heather wants her, and she wants Heather."
    JesT "This isn't something new, Jessica. You've been with a girl before."
    "She knows she's lying to herself. Making out with drunken sorority girls at college is nothing like what's happening."

    if "d03kissBlake" in choices:
        "Nor is the little kiss she'd shared with Blake. Despite the passion both she and Blake had put into it, it was merely playful."

    "This, though, is an honest to god lesbian encounter."
    Jes "Heather..."
    Heath "Hmm?"
    Jes "I..."

    scene day5 ev03-16a
    "Her thought remains unspoken as Heather's lips met her own."
    "She doesn't know what to do, how to react. She'd known it was coming, yet it's shocking to finally have Heather pressing down upon her."
    JesT "She's kissing me. Oh my god, she's actually kissing me!"

    scene day5 ev03-16b with dissolve
    "The pressure on Jessica's lips is far more gentle than she was used to, the touch more ginger and careful."
    "Her previous experiences in college with kissing women had been nothing of the sort, more like drunken idiots slobbering roughly over one another."
    "Heather's kiss, though, is warm and welcoming, a delicate touch from a caring woman."

    if "d03kissBlake" in choices:
        JesT "She's so tender and considerate. I wonder if this is how Blake felt when I kissed her."

    "Jessica can't help being drawn into the embrace, and desperately yearns for their touch to go further."

    scene day5 ev03-16c with dissolve
    JesT "Can I do this? This is... this is cheating."
    JesT "I really want Heather, but... I don't know if I can do this to Conner."

    menu:
        "Stop her":
            $ choices.append("d05heatherStop")
            $ relHeather -= 1
            JesT "No. I can't do this. This is going too far."

            scene day5 ev03-17
            Jes "Wait."
            Heath "What's wrong?"
            Jes "I'm sorry. I can't do this. I can't cheat on Conner."

            scene day5 ev03-18
            "Heather, clearly disappointed, gets off of Jessica."
            Jes "I can't believe I let this go this far. I, um, I have to go."
            Heath "Right. I understand."
            Jes "Look, I don't... I don't want this to hurt our friendship. You're wonderful, and I was flirting too."
            Jes "Why don't you come over tonight? For dinner? We'll... just pretend this didn't happen, okay?"
            Heath "Yeah. That sounds good."
            Jes "Okay. I'm gonna head to work. I'll see you tonight."
            "Without another word, Jessica heads home, still shaking from her brush with infidelity."

            jump day05beforeWork

        "Continue":
            $ choices.append("d05heatherFinger")
            $ relHeather += 2
            $ slut += 1
            JesT "Fuck it. A few kisses won't hurt."

            scene day5 ev03-19 with dissolve
            play voices x_ff_kissing_1 loop
            "Jessica squeezes Heather's hand, savoring the feeling of the other woman's fingers on her face."
            "Small moans begin to slip from her lips as she returns Heather's affectionate embrace, silently telling Heather how desperately she wanted her."

    scene day5 ev03-20
    "As Heather straddles her, Jessica draws in a deep, shuddering breath."
    Jes "Wait? What about Christian?"
    "Heather smiles."
    Heath "Oh, don't worry, I'm sure he'd be fine with it."
    "Jessica relaxes slightly, still unsure, though Heather's touch quickly drives away her doubts."
    "The feeling of Heather's lips brushing against her own, of the woman's hands on her body, is overwhelming yet entirely welcome."
    Heath "You're so beautiful, Jessica."
    Jes "So are you, Heather."
    Heath "I want you, Jessica. I want you so badly."

    scene day5 ev03-21
    "It's what Jessica wants as well. Their lips come together in a passionate kiss, tongues thrusting together as the pair share their mutual affection."
    "The embrace is warm and loving in a way Jessica had never imagined, and already the idea of going further with Heather was swirling about in her mind."
    JesT "She's amazing! I can't believe it took me this long to realize how incredible Heather is!"
    "Her heart beat itself like a drum in her chest. A warmth fills her body and a tingling spreads through her nethers."

    scene day5 ev03-22
    "Heather's hand descends in one smooth motion, gently caressing Jessica's breast."
    "The difference between she and Conner is night and day. Heather's touch seems less about squeezing a part of Jessica's body that she desires and more about making Jessica feel nice."
    "It feels like a touch entirely meant to please her."
    JesT "God, I want to feel her hands all over me. If this keeps going, it's going to be more than a few kisses and some groping."
    JesT "Would that be so bad? God knows I want her, too."

    scene day5 ev03-23
    "The kiss continues as Heather's hand goes further down, fingers slipping into Jessica's pants."
    "Fingertips begin to stroke her sensitive clit, driving her wild with desire and drawing small squeals of delight from her lips."
    JesT "Oh my god, that feels good! She knows exactly how to touch me! Ah, I want her so bad."
    JesT "But this is getting serious. This... this is going to be sex very soon."

    if "d03lickTrue" in choices:
        $ choices.append("d05heatherLesson")
        scene day5 ev03-24
        stop voices
        Jes "Hey, wait a minute."
        Heath "What's wrong?"
        Jes "Nothing. I just... I, uh, I wanted to ask you something."
        Heath "What is it?"

        scene day5 ev03-25
        Jes "Listen, this is, uh... wonderful. You're... fucking incredible."
        Heath "Thank you. But..."
        "Jessica takes a breath, forming her thoughts before she speaks."
        Jes "I have to get to work, but Conner and I are alone tonight. Laura's gonna be out at a friend's."
        Jes "Last night, Conner went down on me, and it… wasn't great."
        Jes "We had discussed getting someone to teach him how to please a woman. Would you like to come over, and, uh, give him a little show?"
        Jes "Show him how it's done?"
        "Heather licks her lips, nodding slowly."
        Heath "Sure. I think that sounds great."

        scene day5 ev03-26
        "Jessica stands, her legs shaky, her face still red."
        Jes "Okay. I'll, um... I'll see you tonight."
        Heath "I'm looking forward to it."
        "Jessica turns away from Heather's grin, her legs wobbling as she strolls out of the apartment, feeling Heather's gaze on her all the way out."

        jump day05beforeWork

    scene day5 ev03-27
    $ choices.append("d05heatherPleasure")
    $ cheat += 1
    $ slut += 1
    "The sensation flooding her nethers is too great. The voice in her head telling her she's about to cheat is quickly quieted."
    JesT "Holy shit. This woman's hands are magic. I wanna feel everything she can do."
    "Jessica's moans grow louder as Heather's hands rub faster and her lips begin to devour Jessica's neck once more."

    scene day5 ev03-28
    "Heather pulls her back into a passionate embrace as she rolls her body off Jessica."
    "The feeling of her sweaty body sliding against Jessica's own is euphoric. Jessica gasps quietly into Heather's lips."
    "Her hand briefly slips out as she moves, but quickly moves back, gently rubbing just over Jessica's eager and throbbing sex."
    "Jessica continues to moan as they kiss, the teasing of Heather's fingers, brushing closer and closer to her clit, driving her insane."
    JesT "Oh, you teasing bitch. Just touch me!"

    scene day5 ev03-29
    stop voices
    play voices x_ff_kissing_2 loop
    "The teasing soon comes to an end, Heather's fingers slipping further inside and once again rubbing Jessica's clit."
    "Their embrace deepens, Jessica's moans increasing in volume even as their kiss becomes ever more passionate."
    "Heather's middle finger circles slowly over her clitoris, causing Jessica to gently pump her hips up and down in time with the rubbing."
    JesT "Fuuuuuck, this is great! She's not gonna have to do much to get me to cum!"

    scene day5 ev03-30
    "Heather's hands pull out once again, this time to push Jessica's pants down her legs."
    "Jessica helps, eager to give her new lover as much access as she desires."

    scene day5 ev03-31
    "With Jessica's eager and sopping sex fully exposed, Heather's fingers once again run over her lover's beautiful womanhood."
    Heath "Lovely."
    "Heather's voice is a whisper in Jessica's ear, one which she delights in hearing. Her eyes close, savoring the feeling of Heather's hand."
    "Fingers run over her clit and her labia, gently rubbing her most sacred of temples."
    "Already, Jessica can feel her orgasm building."

    scene day5 ev03-32
    Heath "Does that feel good, sweetie?"
    Jes "Yes. Oh, it's so good."
    Heath "And this?"
    "Heather flicks her finger from the tip of Jessica's labia up to her clit, drawing a gasp from Jessica's lips."
    Jes "Oh yeah, that's good!"

    scene day5 ev03-33
    "Heather's fingers begin moving faster, more rapidly rubbing Jessica's sex, and bringing her closer and closer to her climax."
    Jes "Heather, you're gonna make me cum."
    "Heather giggles, planting a quick kiss on Jessica's cheek."

    scene day5 ev03-34ani-00
    Heath "That's the idea, sweetie."

    show d05ev03-34ani1
    "Their lips join once more, Heather gently kissing Jessica as her climax approaches."
    Heath "I want you to cum for me, sweetie. Let yourself feel good."
    "Jessica says nothing, simply moaning in pleasure, her joyous orgasm almost there."
    "Heather's fingers are magic, as skilled at bringing her to climax as Conner's cock ever was, and the fact that she was sitting in her neighbor's home, in her new lover's arms, about to cum for another woman is enough to push her over the edge."
    hide d05ev03-34ani1
    stop voices fadeout 1
    play voices x_moaning_2
    Jes "Ah! I'm cumming!"

    scene day5 ev03-35
    "Jessica arches her back, her mouth opening in a cry of ecstasy as she begins to cum."
    "Heather's fingers continue to rapidly stroke her clit, rubbing vigorously back and forth while Heather herself watches the beautiful woman in her arms screaming in joy."
    "Their bodies press together, Heather rubbing her leg along Jessica's thigh, while Jessica's fingers dig into her backside."
    "Jessica's hips buck and thrust into Heather's fingers, pleasure filling her sex as her warm juices flow onto them."
    "It's one of the most intense orgasms she's had in some time, and she can feel herself squirting with incredible force, drenching the cushion beneath her body."
    stop voices

    scene day5 ev03-36
    "Once she's finished, Jessica lifts her head, eyes still closed while she savors the sweet tingling in her body."
    Jes "Oh my god. Oh my god, that was wonderful."
    Heath "I'm glad I made you feel good, baby."
    Jes "I can't believe I never tried that with a girl before. I kissed some other girls in college, but..."
    Heath "No drunken college chick can make you feel as good as I can, Jess."

    scene day5 ev03-37
    "Heather draws her fingers to her lips, tasting Jessica's juices inches from her face."
    Heath "You even taste sweet, baby."
    JesT "Oh, that's a bad line."
    "Despite how corny it was, Jessica had to admit that it was erotic as hell."

    scene day5 ev03-38
    "As she comes down from her orgasmic high, however, emotions begin warring within her chest."
    "She decides it's time to go. Pulling her pants back up, she realizes just how wet she is, as she can feel the sticky juices mixing with the sweat in the fabric."
    "Her eyes close momentarily. Unlike with Conner, she feels icky having spread her cum all over Heather's couch, and into her pants."
    "She soon manages to push it out of her mind, along with the guilt building inside. There will be time for reflection later."
    Jes "I've, uh, I've got to go. Gotta get work."
    Heath "Sure thing."
    "Jessica turns back, flashing Heather a quick smile."
    Jes "This was great. Listen, um… do you want to come over for dinner tonight?"
    Heath "I'd love to."
    "Jessica bids Heather farewell, trying to hide just how awkward she feels as she walks out the door."

label day05beforeWork:

    if "d02hotRun" in choices:
        scene day5 ev03-40 with fade
        play sound shower_1 loop
        "Coming home and finding the shower empty, Jessica quickly strips away the sweaty clothes clinging to her body and climbs inside."
        "She takes a moment to savor the feeling of the hot water cascading over her body."
        "She's trying, and failing, to ignore the myriad feelings swirling about in her stomach."

        scene day5 ev03-40b
        if "d03lickTrue" in choices:
            JesT "I just kissed another woman, passionately… and I invited her over for more!"
            JesT "God help me, I'm gonna have another woman eating me out tonight!"
            JesT "I can't believe what's been happening. It's so, so hot! I can't wait to see her again."

        else:
            JesT "What did I just do? I just cheated on Conner… with another woman!"
            JesT "And I invited her over for dinner!"
            JesT "I can't believe what's been happening. It's so, so hot! I can't wait to see her again tonight."
            JesT "I know this is wrong, but it's not like I'm leaving Conner. I'm not a full-blown lesbian."
            JesT "It's just some fun with my friend, right?"

        scene day5 ev03-41b
        Lau "Jess!?"
        "Laura knocks on the door, just a little too loudly, making Jessica jump."
        Jes "Yeah?"
        Lau "I'm taking off. I'll see you and Conner tonight, 'kay?"
        Jes "Okay. Have a good day, Laura."
        Lau "You too."
        "Jessica soon hears the sound of the front door closing. After another few moments, she steps out and begins to dry herself off."
        stop sound

    else:
        scene day5 ev03-39 with fade
        play sound shower_1 loop
        "Coming home and finding the shower empty, Jessica quickly strips away the sweaty clothes clinging to her body and climbs inside."
        "She takes a moment to savor the feeling of the hot water cascading over her body. Her mind wanders, considering the coming day."
        JesT "Hopefully, there's nothing major going on at work. Afterward, I'll go check out this Victor Smith and see what he can tell me."

        scene day5 ev03-41
        Lau "Jess!?"
        "Laura knocks on the door, just a little too loudly."
        Jes "Yeah?"
        Lau "I'm taking off. I'll see you and Conner tomorrow, 'kay?"
        Jes "Okay. Have a good day, Laura."
        Lau "You too."
        "Jessica soon hears the sound of the front door closing. After another few moments, she steps out and begins to dry herself off."
        stop sound

    scene day5 ev04-01 with fade
    "After her shower, Jessica begins getting dressed for her day."

    if "d02hotRun" in choices:
        JesT "Get Heather out of your head, Jessica. There will be time later to think about what happened."

    "Despite their refusal to leave her head, she tries to push any thoughts of her conversation with Heather aside. She has to focus on her day."

    scene day5 ev04-02 with fade
    play sound vespa_start_drive
    "Jessica hops on her bike, savoring the feeling of the fresh air as she drives away."

    if "d04parkerNoApology" in choices:
        "Jessica's thoughts turn to Mr. Parker."
        JesT "I can't believe what happened between us yesterday."
        JesT "I'm not sure what's gotten into me lately."
        JesT "He and I should talk about it, but not today. I'm already late."

    elif "d04parkerNoApology" in choices and "d05heatherFinger" in choices:
        JesT "What's happening with me lately?"
        JesT "Between Mr. Parker yesterday and Heather today, I've just turned into this horny little slut."
        JesT "Fuck it. I'll talk with Mr. Parker about what happened, but not today. I'm already late."

    else:
        JesT "I have to hurry. I'm gonna be late."

    stop sound fadeout 1

    scene day5 ev04-03 with fade
    "Jessica strolls into the Gazette a little late, groaning inwardly when Eve spots her coming in."
    Eve "Bonjour, Jessica. Late again?"
    Jes "Yeah, my run went a little long."

    if "d05heatherFinger" in choices:
        JesT "And I was getting felt up by my hot neighbor."

    Eve "Best not let Mr. Birch find out. He seems to be in a foul mood today."
    Jes "Got it. Thanks."

    scene day5 ev04-04
    "Heading to her desk, Jessica finds Tommy waiting."
    Jes "Good morning, Tommy!"
    Tom "Hey! Check it out! Your interview with the mayor is in here!"
    Jes "Oh, cool."

    if persistent.pov == 1:
        scene day5 ev04-05mpov
    else:
        scene day5 ev04-05
    "Jessica takes the newspaper and opens it to the interview, briefly glancing through it."
    Tom "Isn't it awesome!?"
    "She doesn't spend any time reading the article, as she was the one who wrote it, but is amused by Tommy's reaction."
    JesT "He's so cute when he's excited, and he definitely seems more relaxed."

    scene day5 ev04-06
    Rosa "Hey, Jessica. Congratulations on the article. You're already making a name for yourself."
    Jes "Thanks, Rosa."

    if "d02cutAngus" in choices:
        Jes "You helped me get started with that, after all."
        Rosa "True, but this is your first solo article, and you deserve the recognition."

    scene day5 ev04-06b
    Rosa "But I came over to enlist your help for something."
    Jes "Sure. What have you got?"
    Rosa "Eve is already helping me with some names and numbers I need to go through, but we have a lot of them."

    scene day5 ev04-07
    Eve "Quite a lot. I could definitely use the help whittling them down."
    Jes "What are they for?"
    Rosa "That construction company I've been investigating, the one that got the contract for the stadium? Well, I've been investigating other companies with connections to them."
    Rosa "Unfortunately, I'm not making much progress. Most of my leads have come up dry."
    Rosa "So I've put together a list of ex-employees from some of these companies. I need help calling them to see if they have any information they're willing to share."
    Jes "Sure. Give me a list, and I'll get started."
    Rosa "Thanks, Jessica. I'll go get you the list now, and I'll get the rest of the numbers to you, Eve."

    scene day5 ev04-08  with fade
    "Jessica takes a seat at her desk, glancing over the list Rosa gave her."
    JesT "I'll get to that in a second. First, let's see if David got me that guy's address."
    "Jessica is pleased to see that David has already sent her the info she'd asked for, including the man's name and address."
    JesT "Fantastic. I'll have to check this guy out after work. For now, let's make some calls."
    "Taking out her phone, she starts working through the phone numbers, identifying herself and her employer before asking if they could tell her anything about the construction companies in question."
    "For the most part, no one has anything to say. A few are rather rude and hang up quickly. Three of them hang up the moment she identifies her employer."
    "One of them even screams at her and tells her to fuck off, but Jessica just sighs and dials the next number."

    scene day5 ev04-09
    Jes "No, sir, I'm looking for information on..."
    MV "You sound really hot, you know that?"
    Jes "Um, sir, I just..."
    MV "You want some information, I bet I could dig something up."
    Jes "Really?"
    JesT "Please don't say dig it out of your pants."
    MV "I'm digging it up right now. I'm getting my hand on it, and pulling it out."
    MV "So, you want to get your hands on what I've got? I want you to get your hands on it."
    "With a sneer and a groan, Jessica hangs up."
    JesT "I feel like I'm at a fucking call center. This sucks."

    scene day5 ev04-10
    "And then, a stroke of luck."
    Jes "You did?"
    FV "Definitely. I worked for Gavin Wright Incorporated, but my paychecks were coming from one of the companies you mentioned, Shell Beach Construction."
    Jes "You're sure?"
    FV "Positive. Even had a little shell for their logo."

    scene day5 ev04-11
    Jes "Just a sec."
    "Jessica starts frantically waving for Rosa, trying to get her attention."
    Jes "Rosa! Rosa!"

    scene day5 ev04-12
    Rosa "What's up? Did you get something?"
    Jes "Yeah. This lady, Adanya Abimbola, said she was getting paid by Shell Beach Construction."
    Rosa "Does she have anything on the company? Any old paperwork or anything?"
    Jes "Here. Take one of the earbuds and listen in."

    scene day5 ev04-13
    Jes "Ms. Abimbola? Still there?"
    FV "Yes."
    Jes "Do you have anything from your time with the company? Any paperwork or old pay stubs?"
    FV "Um..."
    "There's a brief pause, both Jessica and Rosa listening intently."
    FV "Listen, I'm not... I don't think I can give these up. I'm fairly certain that I could be held accountable if I did."
    "Jessica angles her head up, casting a sidelong glance up to Rosa."
    FV "And quite frankly, I can't afford to be sued right now."
    Rosa "Ms. Abimbola? Can you hear me?"
    FV "Yes, I can hear you."

    scene day5 ev04-13b
    Rosa "My name is Rosa Jimenez. I'm the lead on this story, and I can promise you, you won't have anything to worry about."
    Rosa "I've been through these sort of things before, and I always protect my sources. No one will know where this information came from. You have absolutely nothing to worry about."
    Rosa "If you'd like, I can give you my number, you can look me up and check my credentials. You'll find that no matter how much pressure is put on me, I never reveal who I've spoken with."
    "There was silence for a moment, only broken by the sound of Jessica writing a message to Rosa."
    "She writes down 'first name is Adanya', receiving a nod on her shoulder from Rosa."
    Rosa "I promise you can trust me, Adanya."
    FV "Al- alright. Give me your number, and I'll think about it."

    scene day5 ev04-14
    "After they exchange information, Adanya hangs up and Jessica gives Rosa a huge smile."
    Jes "Not bad. She sounded like she was going to hang up at any second. I can't believe you got her to agree."
    Rosa "Not the first time I've talked someone into helping. They want to. You just have to convince them it won't come back to bite them."
    Jes "Well, it was very impressive, Rosa."

    if "d02hotRun" in choices:
        JesT "And kind of attractive. I think I might have a thing for such strong, take-charge women."
        "Jessica sighs, enjoying the scent of Rosa's perfume and the feeling of Rosa's large chest brushing against her back."
        JesT "I feel like the cop at the station when I was leaning over him. No wonder he did what I wanted him to so easily."

    Rosa "Thank you. And thank you for finding this. Hopefully what she has will prove useful."
    Jes "You're sure she'll agree?"
    Rosa "She'll get back to me, I'm fairly sure. And if she doesn't, I'll call her back and convince her."
    Jes "We should keep going, though. See if anyone else has anything we can use."
    Rosa "Definitely. Thanks again, Jess."

    scene day5 ev04-15
    "Jessica continues to make the calls. Tommy returns a few minutes later with a few papers in hand."
    Tom "Hey, I have those other names and numbers Rosa wanted me to pull."
    Jes "Okay. Go ahead and give them to Rosa. See what she wants to do with them."
    Tom "Alright."

    scene day5 ev04-16
    "Tommy returns a minute later, as Jessica is nearing the end of the list."
    Jes "I've just got a few numbers left to call. You wanna sit in and listen?"
    Tom "Sure!"

    scene day5 ev04-17
    "Jessica smiles at Tommy's eagerness, cleaning one of her earbuds and handing it over while he pulls a chair to her desk."
    Tom "So how's this work?"
    Jes "Call them up, tell them who we are and what we're looking for. That's it."
    Tom "Sounds pretty easy."

    scene day5 ev04-18
    "She makes the calls, Tommy listening in. As before, no one has anything to give her, but she's hardly surprised."
    Tom "That's annoying."
    Jes "It's normal. With these sort of things, what you're looking for are the few people who are willing to help, so most of your leads will go nowhere."
    Jes "You get used to it."
    "Tommy nodded, listening in on another call. Once it's done, she fixes him with a smile."
    Jes "You wanna give it a try?"
    Tom "Huh?"
    Jes "Yeah. It'll be good practice for your career as a journalist."
    Tom "Having people hang up on me?"
    "Jessica laughs."
    Jes "All part of the job, but you might get lucky, too."

    scene day5 ev04-19
    Jes "Here. This is the next number, a Mr. Gregory Felberger."
    Jes "Just relax, give him your name, tell him you're working for the Gazette, and why you're calling. Just like I did."
    Tom "Okay."
    "The young man's voice was shaky, but Jessica had faith that he could pull it off."
    "The phone rings for a moment, before a gruff voice answers."
    Tom "Hello, sir. My name's Tommy Fitzgerald. I'm with the New Port Gazette. I was wondering if I could ask you some questions about some construction companies you might have worked with?"
    "Jessica smiles, putting her hand on Tommy's shoulder. He's running his words together too quickly, and she hopes to calm him down."
    Tom "Yes, sir. Uh, they would be... Schreber Construction, Shell Beach Construction, John Murdoch Builders, and Hand and Book Home Services."

    scene day5 ev04-19b with dissolve
    Tom "You did?"
    "Jessica flinches in surprise, pleased at Tommy's luck. She squeezes his shoulder, hoping to keep him calm."
    Tom "Great, yeah, anything you can tell me."
    "The pair hunch together eagerly, Jessica's fingers rapidly working as she writes down everything the man has to say, and writing down an address for Tommy to tell the man to email everything to."
    Tom "Sure. Yeah, let me give you our email."
    "Afterward, with a promise that the man will send them what he has, Tommy hangs up, taking a deep, calming breath."
    Tom "I did it."
    "Jessica claps him on the back."
    Jes "You sure did. Come on. Let's see if anyone wants to grab some food. I'm starving."

    scene day5 ev05-01 with fade
    play sound city_ambience_siren_1 loop
    "Gathering up Rosa and Eve, the group head off to the coffee shop to grab a bite."
    "Rosa is beaming as they go, tremendously pleased not only with the contacts Jessica and Tommy managed to get, but also the lead Eve landed while they were working."
    stop sound fadeout 1

    scene day5 ev05-02
    play sound coffee_shop_1 fadein 1 loop
    "The group orders and sits chatting for a while, mostly just the ladies."
    "Tommy speaks up here and there, but is by and large texting on his phone."
    "Eventually, the conversation turns to a bloody mugging that took place the previous night."
    Rosa "This town is going to shit, I tell ya."
    Eve "I wish I could say it's not so bad. I've lived in quite a few cities, but things here have gotten out of hand."
    Rosa "And the police don't seem to be doing anything about it, no matter what Mayor Fatass says."

    scene day5 ev05-03
    "Jessica winces at the mention of the mayor. He definitely came off as genuine when she met him, though she doesn't want to argue the point."
    JesT "I only met him once, after all."
    "She decides to move the conversation a different direction."
    Jes "Maybe a vigilante is just what we need right now."
    Eve "It's certainly what Mr. Birch thinks we need. More superhero, more papers, and all that shit."
    Rosa "I don't know. I think maybe Jessica's right."
    Rosa "Given how bad crime has gotten, maybe someone who's willing to step up and do something about it is a good thing for the city."
    Eve "You're just saying that because you think he's cute."
    Rosa "Sure, but that doesn't mean I can't also think he's good for the city."
    Eve "I would bet that man is going to get himself killed soon, and that will only make things worse."

    scene day5 ev05-04
    Jes "Hopefully, I can find something out about him before that happens. That'd be a hell of a story."
    Eve "And make Mr. Birch so very happy."
    Jes "Everybody wins!"
    "Eve smiles and shakes her head, though Rosa's expression remains stony."
    Rosa "It's a flash-in-the-pan story. He'll sell a few papers, and then that's it. Old news."

    scene day5 ev05-05
    "Rosa turns to Jessica, then back to Eve."
    Rosa "Be careful, both of you. Eve, once Mr. Birch gets his mind on something he tends to put everyone on it."
    Rosa "And going after a man like the vigilante could make you cross paths with his targets, none of whom are men you want to meet."
    "Jessica takes a bite of her food, remaining silent on her attempts to get close to the masked vigilante. She doesn't need a lecture."

    scene day5 ev05-06
    "Her gaze turns to Tommy, who's been silent for most of lunch."
    Jes "What's up with you, Tommy?"
    "Unexpectedly, he jumps in his seat."
    Tom "Uh, what?"
    Jes "You've been awfully quiet this whole time. What have you been talking about with your friends?"
    Tom "Oh, just... nothing much. Like, school stuff."
    Jes "Oh. Cool."

    scene day5 ev05-07
    "Tommy excuses himself, and heads to the restroom."
    Rosa "Oh, that kid."
    Jes "What about him?"
    Rosa "He's just a little timid, and jumpy. He needs a girlfriend."
    Eve "Or just to get laid."
    Rosa "He's a little young, don't you think?"
    Eve "When did you first get laid? Were you younger or older than he was?"
    "Rosa simply rolls her eyes and ignores the question."

    scene day5 ev05-08
    "Jessica is about to contribute to the conversation, but stops as Tommy's phone, left on the table, buzzes with a message. Her eyes briefly flit over the screen, noticing the phrase, 'the blonde'."
    JesT "Huh. You didn't lock your phone, Tommy. Silly boy."
    "Pulling it closer, Jessica opens the message, finding a picture of herself in the log, taken just a moment previous."
    JesT "What the hell? Why did he take a picture of me?"

    scene day5 ev05-09
    "As Eve and Rosa continue talking, Jessica scans through the texts, shocked by Tommy's conversation."
    "TOMMY: Seriously, I'm at lunch with these 3 hot girls from work."
    "ALEX: Bullshit."
    "TOMMY: Check this out!"
    "After that, Tommy sent the picture he'd taken of Jessica, having made sure to capture her cleavage."
    "ALEX: Holy MILF, man, that is one hot bitch!"
    "TOMMY: She's not a bitch, man. She's real nice."
    "ALEX: I can't believe you're eating lunch with a chick that hot."
    "ALEX: I can't believe you're not making a move."
    "ALEX: If I were with her right now, I'd have her screaming my name in five minutes."
    "TOMMY: Yeah right."
    "ALEX: Dude, can you get a picture of her tits?"
    "ALEX: Get a picture of her without her shirt, and I'll give you one of my Iyanden Wraithlords."

    scene day5 ev05-10
    "Jessica just stares at the conversation, several emotions rising in her chest."
    "She feels more than a little offended that Tommy was discussing her in such a way, but feels downright angry at the way this other boy, Alex, is talking about her."
    "At the same time, she feels a swelling of pride. Jessica knows she is an attractive woman, but it is nice to hear such things every now and then."
    "Even if it's in a rather crude and immature manner."
    JesT "I could do Tommy a favor here. Give that little brat Alex a nose bleed and get Tommy... whatever the hell that thing is."
    JesT "If I head over to the restroom real quick and snap a photo with his camera, he'll get what he wants."
    JesT "Tommy has been really helpful, even if he's been talking about me like this."
    JesT "Do I really want to give this Alex brat the satisfaction, though? For that matter, do I want such a picture of me out there?"

    menu:
        "Leave the phone":
            $ choices.append("d05noSelfie")
            JesT "On the other hand, maybe not. Wouldn't necessarily want such a picture of me floating around."

            scene day5 ev05-11 with dissolve
            JesT "This is really not behavior I should be encouraging."
            JesT "Tommy's a good kid, though. Hopefully he won't bring this up."

            scene day5 ev05-12
            "Sliding the phone surreptitiously back into place, Jessica turns her attention back to the other two, who are engaged in a heated debate about the efficacy of vigilantes."
            Eve "Seriously, if he wants to get off dressing up in black leather and beating people, there are clubs for that sort of thing."
            Rosa "That's reductionist. The outfit may be silly, but he's doing good work. At least these people are alive after he beats them. The police would have shot them."

            scene day5 ev05-13
            "Tommy returns a few moments later, sitting down at this seat and immediately grabbing his phone to resume the rather lewd conversation."
            "Jessica ignores him, suggesting it's about time they all headed back to work."
            stop sound fadeout 1

            scene day5 ev05-31a
            "After their lunch, the group heads back to the office, Eve and Rosa still talking excitedly about their work."
            "Behind them trail Jessica and Tommy, the two of them chatting back and forth."
            JesT "It's too bad he won't be around anymore. He's a good kid. And thankfully, he didn't try to talk my shirt off."

            jump day05afterLunch

        "Take a photo for them":
            $ choices.append("d05sexySelfie")
            $ relTommy += 2
            $ slut += 1
            JesT "You know what? Why the hell not? Lets give these boys a thrill."

            scene day5 ev05-20 with dissolve
            JesT "It's not like I even need to show them my bare tits. With the underwear I'm wearing, that should be enough."
            JesT "And I bet it'll shock the hell out of both these boys."

    scene day5 ev05-21
    "Slipping the phone from view, Jessica excuses herself from the table."
    Jes "I'll be back, ladies. I'm gonna run to the restroom real quick."
    "The others nod, then turn back to their own conversation."
    stop sound fadeout 1

    if slut >= 11:
        scene day5 ev05-22
        JesT "This is kind of exciting! I'm about to blow these boys' heads apart."
        JesT "And give them some hot spank material. I hope they enjoy!"

    else:
        scene day5 ev05-23
        JesT "This is a little crazy. I'm about to take a picture of my tits and send it to a strange boy."
        JesT "I should be careful what I show. This picture could get around, so I won't give them everything."

    scene day5 ev05-24
    "Jessica unbuttons her shirt and opens it to reveal her chest covered by her lacy underwear. The cool air feels nice on her chest, and she lets out a little laugh."
    JesT "This feels so damn naughty, the kind of thing I would have done in high school."
    JesT "Maybe I should grow up at some point, but fuck it. This is fun. My heart's beating really fast."

    scene day5 ev05-25
    "With her shirt completely off, her eyes take in her slim, busty body, her breasts partially-visible through the transparent fabric."
    "A smile crosses her face, pleased that she's so attractive she's driving young men wild."
    JesT "Damn, Jess. Maybe you're even hotter than you thought. No wonder that boy wants to see your tits so bad."
    JesT "Of course, they're teenage boys. They want to see every woman's tits, but still."
    JesT "I wish they wouldn't call me a MILF, though. I'm not that old."
    "A noise from outside draws Jessica's attention, giving her a momentary spike of panic."
    JesT "I should hurry and finish this before someone else comes in."

    scene day5 ev05-26
    "At the last moment, Jessica realizes her necklace could be used for identification, and decides to take it off."
    "Picking up the phone, Jessica puts on a seductive look, pushing up her breasts with her arm, and takes the picture."
    JesT "There. Enjoy the sight of my tits when you jerk off, buddy. And you better give Tommy what you promised."
    "Briefly, she thinks that Tommy's probably going to jerk off to the picture too, which brings a brief smile to her face."
    JesT "He's a nice boy. He deserves a little thrill."

    scene day5 ev05-27
    "Before she gets dressed, she send the picture back to Alex, with the message 'Pay up!' attached."
    JesT "There you go, Tommy. Enjoy!"
    "Grabbing up her shirt, she throws it back on, hoping no one walks in while she's dressing, and buttons it back up."

    scene day5 ev05-28
    play sound coffee_shop_1 fadein 1 loop
    "Strolling out of the restroom, Jessica smiles and breathes a sigh of relief."
    "She can see someone walking over, heading directly toward the restroom."
    JesT "Wow. That was lucky. Another thirty seconds and someone may have caught me."
    JesT "Let's get this phone back to Tommy."

    scene day5 ev05-29
    "Taking her seat at the table, Jessica places the phone down next to Tommy."
    Jes "Hey, Tommy. Sorry, but I grabbed your phone by accident."
    Tom "You did?"
    "A slight tremor in his voice tells her he's worried she looked. She just nods and smiles, though, turning back to the other ladies."
    Jes "So, what are we talking about?"

    scene day5 ev05-30
    "As Rosa fills Jessica in on her and Eve's debate about police funding, Jessica sees Tommy looking at his phone out of the corner of her eye."
    "His jaw drops when he sees the chat log, finding the picture she's so pleasantly left for him."
    Jes "Mm-hmm."
    "Jessica nods, feigning interest in what Rosa and Eve have to say, though her attention is entirely focused on her amusement at Tommy's reaction."

    scene day5 ev05-30b with dissolve
    "A gasp leaves the young man's mouth, drawing the attention of all three women."
    Rosa "You okay, Tommy?"
    Tom "Huh? What?"
    "Tommy pulls the phone up, concerned one of them may see what he's staring at."
    Eve "You look like you just got some bad news."
    Tom "Oh. Uh, no. No bad news."
    Jes "So everything's good?"
    "Tommy's eyes meet her own, and he nods."
    Tom "Yeah. It's, uh, it's great."
    stop sound fadeout 1

    scene day5 ev05-31b
    "After their lunch, the group heads back to the office, the trio still talking excitedly about their work."
    "Behind them trails Tommy, his gaze locked onto the picture on his phone."

label day05afterLunch:

    scene day5 ev05-32
    "Back at her desk, Jessica checks her email, verifying the address David had sent her earlier."
    "After planning her route to the garage the man works in, she decides to do a little investigating."
    JesT "Victor Smith, huh? Let's see what I can find on this guy."
    "A quick search reveals little about him, other than information she already possessed."
    "Jessica was hoping for more, but doubts that widening her search will do any good."
    JesT "It's probably not worth the time. I might as well just go meet him."

    scene day5 ev05-33
    Jes "Hey, Rosa?"
    Rosa "What's up?"
    Jes "I've got the address of the guy who might have modified the vigilante's bike. I'm gonna head over and speak with him."
    Rosa "Like I said, be careful."
    Jes "No worries. I doubt the vigilante's gonna be there."
    Rosa "It would be great if something comes of this. Birch is very upset about not publishing what you brought from the station."
    Jes "He gave me a few days, so I should be able to find something in that time."
    Rosa "It might not mean much. He is the boss. If he gets impatient, he could just do it anyway, so get something good."

    scene day5 ev05-34
    Jes "Yeah. I'll work fa-"
    "As Jessica speaks, Rosa picks up the camera she'd been fiddling with and takes a picture."
    "Jessica recoils, a little embarrassed to have her picture taken without her permission."
    Jes "Hey, what the hell?"
    Rosa "It's just for fun. I'm taking some pictures of people around the office, and I wanted to get a candid photo of you."
    Rosa "And you were so confident at that moment, I have to capture it."

    scene day5 ev05-35
    Jes "Okay, just... warn me next time."
    Rosa "Sure."
    Jes "Alright, I'm gonna go say goodbye to Tommy before he leaves."
    Rosa "Oh, I forgot to mention that I extended his stay."
    Jes "Really?"
    Rosa "Yeah. He'll be here next week, but only half a day, after school."
    Jes "Cool. He's been really helpful, and the experience seems to be doing him some good."
    Jes "I'll see you next week, Rosa."
    Rosa "Have a good weekend."

    if "d05sexySelfie" in choices:
        scene day5 ev05-37a
        "Coming up from behind, Jessica surprising Tommy when she puts her hands on his shoulders."
        Jes "Hey there, Tommy."
        Tom "Oh. Hey, Jessica."
        Jes "Rosa tells me you're coming back next week."
        Jes "I'm glad to hear it. It seemed like you really liked it here."
        Tom "It's been great. I'm learning a lot."
        Jes "I'm guessing the 'hot girls from work' are part of the reason too?"

        scene day5 ev05-37b
        Tom "Uh... the thing is, about that guy..."
        Jes "Don't worry about it, Tommy. It's fine. Your friend is a braggart, though. You gonna get that thing he promised?"
        Tom "Yeah. I'm used to Alex's big mouth, and I'm definitely gonna hold him to his bet."
        Jes "Cool! I hope you enjoy. Just do me a favor? Don't share that photo, okay? And would you tell Alex the same?"
        Tom "Yeah, I promise! I won't show it to anyone else!"
        Jes "Okay, I've gotta go see a guy for some info. See you next week."
        Tom "Okay. Good luck, Jessica!"

    else:
        scene day5 ev05-36
        Jes "Hey, Tommy."
        Tom "Hey, Jessica."
        Jes "Rosa tells me you'll be coming back next week."
        Jes "That's good to hear. It seemed like you really liked it here."
        Tom "It's been great. I'm learning a lot."
        Jes "Awesome! I've got to take off, so I'll see you next week then."
        Tom "Bye!"

    scene day5 ev05-38
    Jes "Hey, I'm gonna go speak to a guy about the vigilante. I'll see you next week."
    Eve "Be careful the masked man doesn't find you. He really might be dangerous."
    Jes "I'm not worried. I don't think he'll appear from the shadows and menace me."
    "Eve shrugs."
    Eve "Okay. Don't make me say I told you so."
    "Jessica flashes an insincere smile, and waves goodbye."
    JesT "Don't worry. I have no plans to give you the satisfaction."

label day05bikerVisit:

    scene day5 ev06-01
    "Jessica finds the place without much trouble, thankfully still open."
    JesT "Someone's here, at least. Let's see if Victor's working today."

    scene day5 ev06-02
    "Parking her scooter, Jessica peers inside, finding nobody in view."
    JesT "I don't see him, but someone has to be around."
    JesT "Might as well head in."

    scene day5 ev06-03
    "Once inside, Jessica hears metal music playing in the back."
    Jes "Hello?!"
    "Her voice comes out louder than she'd intended, trying to be heard over the music, but instead echoing around in the first room."
    "When she receives no answer, she heads further inside."

    scene day5 ev06-04
    "In the next room, a muscular, heavily tattooed man is kneeling by a disassembled bike, his head turning as she enters."
    "He stands, his face expressionless."
    MV "Can I help you?"

    scene day5 ev06-05
    Jes "I hope so. I'm looking for Victor Smith."
    "The man nods once, grabbing a towel and wiping his greasy hands."
    Vic "Well, you found him."

    scene day5 ev06-06a
    "Jessica smiles, a little uneasy given his large stature and the sheer number of tattoos on his body, but forces her discomfort away."
    JesT "Just because he's big and has some ink doesn't mean anything, Jess."
    Jes "Hi, I'm Jessica O'Neil. I work for the New Port Gazette."
    "She extends her hand, but Victor simply nods and raises his left one, showing off the grease and grime covering it."
    Vic "You'll have to excuse me."

    scene day5 ev06-06b with dissolve
    Jes "Ah, right. I was told you're the guy to speak to about motorcycle modification."
    "Victor leans slightly to the side, staring out the door and to her scooter."
    "He shrugs."
    Vic "Maybe."
    JesT "Ah, we're gonna have to do this dance, are we? Okay. I guess I'll have to butter him up."

    scene day5 ev06-07
    "Jessica turns to the bike at her side, putting a sweet smile on her face."
    Jes "Did you do this one? It's gorgeous!"
    "He nods."
    Vic "Yep. Every bit, including the paint job."
    Jes "Is it yours?"
    "Again, a nod."
    Vic "That she is. I've been fixing her up, and once she's finished I'll sell her."
    Vic "Why? You interested?"
    "His tone is skeptical, a little chuckle going with the question."
    Jes "She's beautiful, but I doubt I could afford it. Besides, I usually prefer sports bikes."
    "The man scoffs, smirking."
    Vic "Sports bikes are for kids and clowns."
    JesT "Geez, what an ass."

    scene day5 ev06-08
    JesT "Maybe I need to try another tactic."
    Jes "Maybe so, but I like them anyway. Fast, and nimble, and riding them is one hell of a thrill."
    "Victor finally gives her a genuine smile."
    Vic "Oh, there are other ways to get a thrill. Ways that don't involve breaking such a pretty neck."
    JesT "There we go. That's the reaction I was looking for."
    "Jessica smiles, licking her lips."
    Jes "Oh? And what ways would those be?"
    Vic "Well, you could take a ride on my Harley. I guarantee you'd enjoy the ride."
    "She giggles."
    Jes "Wow. You'd let me ride your Harley?"
    Vic "I might, if you ask nicely."
    Jes "I can be very nice, if I want something. A sports bike, for example."

    scene day5 ev06-09
    "Victor lets out a hearty laugh before his expression becomes more serious."
    Vic "So, you want to tell me why you're here? I doubt you came to discuss bikes."
    "A brief pang of frustration flits through Jessica's chest. Victor is a confusing man. Flirting one moment, then serious the next."
    JesT "No point in beating around the bush any longer."

    scene day5 ev06-10a
    "She reaches into her purse and withdraws her phone, showing him the image of the vigilante's bike."
    Jes "I'm looking for the owner of this bike."
    "Victor takes a few seconds to look at the picture on her phone, before shrugging his shoulders wearily."
    Vic "So?"
    Jes "This bike has some strange modifications, and I'm hoping you might know who made them."

    scene day5 ev06-10b with dissolve
    "For several seconds, Victor just stares at her, as if studying her face. Jessica begins to feel a little uncomfortable under his gaze."
    "Then he shifts his body slightly, as if relaxing."
    Vic "Yeah. I know who did it."
    "Jessica waits for the answer, but none are forthcoming, Victor once again playing coy. Jessica begins to feel a little frustrated."
    Jes "Can you tell me who did it?"

    scene day5 ev06-11
    Vic "Yeah. Me. I did that work."
    "Jessica's annoyance is overwhelmed by her joy at having found a concrete connection to the vigilante. She feels practically giddy that she's getting closer."
    Jes "That's great! Do you remember when you did it?"
    Vic "It was a few years back, about two and a half, I think."
    Jes "Are you sure?"
    Vic "Yeah. The bike was blue-black then, but I recognize my own work."
    Jes "Could you tell me who had it done?"
    "Victor sighs, his eyes rolling up and down Jessica."

    scene day5 ev06-12
    Vic "Nah."
    Jes "No?"
    Vic "My clients value their privacy."
    JesT "Oh, this guy's exhausting."
    JesT "Alright, let's turn on the charm. Maybe a little flirting can loosen his tongue."

    scene day5 ev06-13
    "Jessica reaches up, running her finger over Victor's chest."
    Jes "Aw, can't you make an exception? I can promise no one will ever know where I got the information."
    "Victor smiles, his hand moving of its own accord to touch her before he caught himself."
    Vic "Oh yeah? You'll protect me as a source, eh?"
    Jes "I'll never tell anyone."
    "Jessica runs her finger further down his chest, giving him her best puppy-dog eyes."
    Jes "Please? It'll really help me out."
    "His eyes roam over her body, moving down to her breasts and staring into her cleavage."
    JesT "Come on. Stare at the girls. Let them change your mind."
    Vic "I'm curious."
    "Victor's voice is low and soft, bringing a smile to Jessica's face."
    Jes "About what?"

    scene day5 ev06-14a
    Vic "Do you think I'm some horny, dumbass teenager?"
    "Jessica blinks several times as Victor steps back, a smirk on his face."
    Jes "I'm... sorry?"
    Vic "I'm not gonna fall for that shit. It's gonna take more than a sweet words and big tits to make me lose my shit."
    JesT "Fuck. I'm done trying with this guy. Maybe he'll take a bribe."
    Jes "Well, what would make you lose your shit, hmm? I can pay you."
    Vic "Nah. I like where you were going, but I need it to go farther. Flirting doesn't do shit for me. I need full release, baby."
    "Jessica's eyes go wide, shocked at the implications of his words."
    Jes "I beg your pardon?"
    Vic "You know. Get me off, and I just might have some information for you."

    scene day5 ev06-14b with dissolve
    Jes "I don't know who you think you are, but I'm not letting you lay a finger on me, buddy. Oily hands, remember?"
    "Victor shrugs."
    Vic "Oh, I don't need to touch you, though that'd be fun. You can do all the touching. With those pretty lips of yours, maybe."
    Jes "I- I am absolutely not blowing you!"
    Vic "Your hands, then. Get me off, and I may just accidentally leave the information out for you to find."
    JesT "This is... goddamnit."
    JesT "I need that info. If I get that, I could track the guy down tomorrow. Birch will be thrilled, and not only will it help my career, but I could actually become famous."
    JesT "An interview with a vigilante like this could be huge!"
    JesT "The price for it, though..."
    JesT "Do I do it? Do I give this asshole a handjob?"

    menu:
        "Say no":
            JesT "I can't possibly. This is WAY too far. I'll find the vigilante some other way."

            scene day5 ev06-15
            Jes "No. I am absolutely NOT doing that."
            "For a moment, Victor is silent, his face passive."
            "Then, to Jessica's shock, he gives her a genuine smile."
            Vic "Okay, then."
            Jes "Look…"
            Vic "No reason to explain. You're not some slut who'll bend over at a moment's notice."
            Vic "I can respect that."
            JesT "What? I do not get this guy."
            Jes "Really?"
            Vic "Yep."
            Jes "Look, is there any chance…"
            Vic "Nope. Like I said, privacy."
            Jes "I could write an article for you. A special one on bike modifications, featuring you and your garage, and you can speak as the expert for it."
            Jes "It could bring in loads of business."
            Vic "Nah. I'm good."
            JesT "I didn't think that would work. A man like him doesn't usually want the spotlight, but I had to try."
            Jes "Please. There has to be something else you'd take for that information."
            Vic "Hey, you wouldn't just reveal a source, would you? Well, I don't give away my clients."
            Vic "But if you need anything else, I'd be more than happy to help."
            "Jessica scoffs, not sure if she's angrier that he won't help her or that he genuinely seems to mean what he says."

            scene day5 ev06-16
            "Frustrated, Jessica turns on her heel and strolls away, Victor calling after her."
            Vic "That includes that Harley ride! Call me anytime!"
            JesT "Well, that was a waste of time. Stubborn ass."
            JesT "I'll get in touch with David. See if he can get anything out of this guy."

            jump day05afterVictor

        "Agree to give him a handjob":
            $ choices.append("d05victorHJ")
            $ cheat += 1
            $ slut += 2
            JesT "Well, fuck. I guess it's not so bad. If it gets me what I want, I guess I can make the asshole cum."

    scene day5 ev06-20
    Jes "Before we do this, I want to know exactly what you have."
    Vic "I have the address I delivered the parts to. I don't remember him exactly. Some young kid in his early twenties."
    Vic "But a few months back, he called in an order for a hush muffler."
    Vic "Delivered to the same address as before."

    scene day5 ev06-21
    Vic "Let me just close up real quick. Don't want anyone interrupting."

    if slut >= 12:
        JesT "This feels so wrong. I can't believe that I'm kind of excited."
    else:
        JesT "I can't believe I'm gonna do this."

    Vic "Alright. Let's head to the back."

    scene day5 ev06-22
    "Victor pulls out a thick book, then begins flipping through, searching for a specific entry."
    Vic "Yep. Got the address right here. So, I guess I'll just put this down."
    Vic "You do your thing, and then I'll just forget that I left my ledger out for anyone to take a look at."
    Vic "I think it's a pretty good trade."

    scene day5 ev06-23
    Jes "You're such an ass."
    Vic "Hey, you wouldn't reveal a source just because some cute guy flashed a smile, would you?"
    Jes "No. I wouldn't. Not even for a sexual favor."
    Vic "So, you don't want me to give you anything?"
    Jes "Just... go ahead and drop your pants."
    Vic "Haha! Now that's what I'm talking about."
    Jes "Don't- don't talk. Just show me your dick."
    Vic "Well, my hands are dirty. Maybe you should pull down my pants, huh?"

    scene day5 ev06-24
    Jes "Geez. Fine."
    "Jessica reaches down, sliding his pants off and trying to hold back her amazement at the impressive sight within."

    scene day5 ev06-25
    Vic "Not bad, eh?"

    if slut >= 12:
        JesT "Oh, wow. That's… kind of gorgeous."
    else:
        JesT "Well, it would be a lie to call it a tiny peepee, even though I would love to insult him. Too bad I can't."

    Jes "It's... I've seen bigger."
    Vic "I bet you love 'em big, don't you? Love big cocks in your pussy."
    Jes "What'd I say about talking?"

    scene day5 ev06-26
    "Jessica's fingers close around the thick organ, slowly stroking back and forth."
    "Victor groans in pleasure, savoring the sensations."
    Vic "Ah. Yeah. That's good."
    JesT "Good, he's enjoying it. Then we can finish this up quickly and move on."

    scene day5 ev06-27
    "Jessica gradually increases the tempo, her fingers squeezing ever-so-gently."
    JesT "I really can't believe I'm doing this. I'm jerking off a strange man I've never met before."

    if slut >= 12:
        JesT "This really shouldn't be this hot."

    "She is determined, however, to get the information she wants, no matter what she must do."
    "Victor's head lowers, his breathing becoming rapid and shallow."

    scene day5 ev06-28
    "Victor's eyes close, a constant low moaning growl rumbling in his throat."
    Vic "Oh, baby."
    Vic "Ugh."
    Jes "Well? Are you close?"
    Vic "Nah. It's not really working."
    "Jessica sighs, changing up the rhythm of her strokes in the hopes of getting him closer."
    Jes "How's that?"
    Vic "Hmm… nope. Maybe you should use your mouth. I'm sure I'd get off then."
    Jes "No!"
    "A smile briefly lights up Victor's face, but soon disappears."

    scene day5 ev06-29
    "Jessica keeps going for several moments, hoping he's nearing his climax."
    Jes "Are you almost there?"
    Vic "Ugh... uh, nope. Nope, still not feeling it."
    "With another sigh, Jessica is about to try something new when she notices a flicker of a smile on Victor's lips."
    Jes "Wait a minute. You're holding back! You're trying to get me to give you a blowjob!"
    Vic "Hey, you're the one who's giving a shitty handjob. I just want to get off."
    JesT "Shitty handjob?! You fucking asshole! I'll make you cum, whether you want to or not!"
    Jes "Well, we'll see about that."

    scene day5 ev06-29ani-00
    "Jessica redoubles her efforts, determined to make the asshole cum. She begins rapidly and firmly stroking the shaft while her other hand begins squeezing the head of his dick."

    show d05ev06-29ani1
    "Victor's demeanor soon changes. It becomes clear that he's no longer holding back. The pleasure building in his manhood is too much to resist."
    Jes "You still think my handjob's shitty?"
    Vic "Uh…"
    Jes "Huh? Is that good or not?"
    Vic "Yeah. Yeah, it's good."
    Jes "You want to cum?"
    Vic "Oh shit, yeah! Oh shit!"
    Jes "You like that? You like my hands rubbing your cock?"
    Vic "Fuck yeah! Fuck yeah, I'm almost there!"
    "Jessica speeds up, rapidly stroking her hands back and forth, ready to make Victor cum and get what she came for."
    hide d05ev06-29ani1
    Vic "Fuuuuuuck!"

    if slut >= 13:
        scene day5 ev06-30a
        "Victor's cock begins twitching in her hand, cum flying into the air as he moans in ecstasy."
        "A smile comes over Jessica's lips, who is surprised at how much she's enjoying the sight and sensations of his orgasm."
        JesT "I shouldn't like this, but goddamn, that's a gorgeous cumshot."

        scene day5 ev06-30b
        "To her shock, Victor just keeps cumming and cumming, his manhood spewing a seemingly endless supply of his seed."
        JesT "Oh my god! I've never seen a man cum this much! It's everywhere!"
        JesT "I wonder what he tastes like?"
        JesT "Not that I'm gonna find out. There's no way I'm gonna do that for him."

    else:
        scene day5 ev06-30c
        "Jessica takes a step back as Victor's cock begins twitching, cum flying into the air as he moans in ecstasy."
        "Much to her surprise, a smile comes over her face, pleased that she was able to make him cum despite his efforts to resist."
        JesT "Shitty handjob, my ass. I made you finish, dick."

        scene day5 ev06-30d
        "To her shock, Victor just keeps cumming and cumming, his manhood pumping itself into the air and spewing a seemingly endless supply of his seed."
        JesT "Oh my god! I've never seen a man cum this much! It's everywhere!"
        JesT "And I bet it tastes like crap. Yech. It's a good thing he didn't demand a blowjob, or I wouldn't be getting my address. There's no way I would have touched that thing with my lips."

    scene day5 ev06-31
    Vic "Oh, shit! Baby, that was great! You're pretty fuckin' good at that."
    JesT "You bet your ass I am, asshole."
    Jes "Yeah. Now, that address?"
    Vic "Huh? Oh. Right."
    Vic "Anyway, I can't give you anything. Sorry. Now if you'll excuse me, I'm gonna go clean up."

    scene day5 ev06-32
    "Victor heads off to the restroom, leaving Jessica alone with the open ledger."
    "Pulling out her phone, she quickly finds the entry she's looking for and takes several pictures."
    Jes "Got it!"

    if slut >= 13:
        JesT "Okay. I finally have my lead. That wasn't too bad."
        "Without waiting for Victor to return, she strolls outside, ready to be done for the day."
        JesT "Thank God it's time to head home. I'm all worked up now, and I think I'd like to get plowed."
    else:
        JesT "Okay. I finally have my lead. I hope this was worth it. I don't want to have to do this for all my stories."
        "Without waiting for Victor to return, she strolls outside, ready to be done for the day."
        JesT "Thank God it's time to head home. I feel disgusting."

    jump day05afterVictorHJ

label day05afterVictor:

    scene day5 ev06-40
    "Sighing, Jessica takes a seat on her scooter and calls up David's number."
    Dav "Hey, Jess! How's it going?"
    Jes "Hi, David. Eh, I'm having a bit of trouble."
    Dav "What's up?"
    Jes "Well, I'm outside Victor's garage. We had a little talk."
    Jes "He knows something, but he refused to tell me."

    scene day5 ev06-41
    Dav "I'm not surprised. Victor's not the kind of guy who blabs about the work he does."
    Dav "It's kind of important that he doesn't."
    Jes "Well, I tried to convince him, but he wanted more than what I was willing to pay."
    Dav "Yeah. That definitely sounds like Victor."
    Jes "Is there any way you could speak to him? He might be more willing to help you than he was me."
    Dav "You didn't piss him off or anything, did you? It'll be hard to get anything out of him if you did."
    "She shakes her head."
    Jes "No. I was perfectly polite, even if he didn't deserve it."

    scene day5 ev06-42
    Dav "Okay. I'll pay him a visit tomorrow and see what I can get out of him."
    Jes "David, you are a lifesaver. I really appreciate it."
    Dav "Anything for you, Jess. I'll call you after I talk to him."

    scene day5 ev06-43
    "The pair bid each other farewell, though Jessica is still a little nervous."
    JesT "I really hope he can get this guy to talk. I don't have any more leads, and Mr. Birch won't wait long."
    JesT "Well, no point in worrying about it. Might as well just head home."
    JesT "I'll call Conner and let him know to expect company tonight."

    scene day5 ev06-44a
    "The phone rings several times with no answer."
    JesT "I guess he must be busy at the Center."
    "However, he picks up before the call goes to voicemail."
    Con "Hey, babe. What's up?"
    Jes "Not much. I just got done for today and I'm about to head home."
    Con "Cool. Unfortunately, I'm gonna be a little late."
    Jes "You're not on your way back? It sounds like you're in your car."
    Con "I am. I'm out running an errand for the Center. It won't take long, though."

    if "d05heatherPleasure" in choices:
        scene day5 ev06-44b with dissolve
        "Jessica's quietly sighs."
        JesT "Seriously? Again?"
        JesT "Well, I suppose that's okay. It'll give me a little more time alone with Heather."
        JesT "I can think of a few ways she and I could pass the time."
        Jes "Alright, sweetie. Listen, I invited Heather over for dinner, just so you know, but we'll keep each other entertained until you arrive."
        Con "I won't be long. I promise, babe."
        Jes "Take as long as you need, sweetie. I'll see you at home. I love you."
        Con "Love you, babe. Bye."

    elif "d05heatherLesson" in choices:
        scene day5 ev06-44c with dissolve
        "Jessica's quietly sighs."
        JesT "Oh, Conner. You really don't want to leave me hanging tonight."
        Jes "Alright, but please don't be too late. I invited Heather over for dinner."
        Con "I won't be long. I promise, babe."
        Jes "Okay. I'll see you in a bit. I love you."
        Con "Love you, babe. Bye."

    else:
        scene day5 ev06-44b with dissolve
        "Jessica's quietly sighs."
        JesT "I finally have him back in my life, and he's always busy elsewhere."
        Jes "Alright, but please don't be too late. I invited Heather over for dinner."
        Con "I won't be long. I promise, babe."
        Jes "Okay. I'll see you in a bit. I love you."
        Con "Love you, babe. Bye."

    scene day5 ev06-47
    play sound vespa_start_drive
    "Putting away her phone, Jessica starts up her scooter and rides off, eager to get home."
    JesT "Oh, I can't wait to relax. After this week, it'll be nice to get my mind off work for a little while."
    stop sound fadeout 2

    jump day05eveninghome

label day05afterVictorHJ:

    scene day5 ev06-45
    "Exiting the garage, her phone rings, a smile crossing her face."

    if slut >= 13:
        JesT "Wow, what timing. It's a good thing he didn't call when my hands were… occupied."
        JesT "I hope he'll be in the mood when he gets home. After that, I really want his dick inside me."

    scene day5 ev06-46a
    Jes "Hey, sweetie."
    Con "Hey, babe. How's your day going?"
    Jes "Good. I just finished up with my work, and I'll be heading home now."
    Con "Cool. Unfortunately, I'm gonna be a little late."
    Jes "You're not on your way back? It sounds like you're in your car."
    Con "I am. I'm out running an errand for the Center. It won't take long, though."

    if "d05heatherPleasure" in choices:
        "Jessica's quietly sighs."
        JesT "Seriously? Again?"
        JesT "Well, I suppose that's okay. It'll give me a little more time alone with Heather."
        JesT "I can think of a few ways she and I could pass the time."
        Jes "Alright, sweetie. Listen, I invited Heather over for dinner, just so you know, but we'll keep each other entertained until you arrive."
        Con "I won't be long. I promise, babe."
        Jes "Take as long as you need, sweetie. I'll see you at home. I love you."
        Con "Love you, babe. Bye."

    elif "d05heatherLesson" in choices:
        "Jessica's quietly sighs."
        JesT "Oh, Conner. You really don't want to leave me hanging tonight."
        Jes "Alright, but please don't be too late. I invited Heather over for dinner."
        Con "I won't be long. I promise, babe."
        Jes "Okay. I'll see you in a bit. I love you."
        Con "Love you, babe. Bye."

    else:
        scene day5 ev06-46b with dissolve
        "Jessica's quietly sighs."
        JesT "I finally have him back in my life, and he's always busy elsewhere."
        Jes "Alright, but please don't be too late. I invited Heather over for dinner."
        Con "I won't be long. I promise, babe."
        Jes "Okay. I'll see you in a bit. I love you."
        Con "Love you, babe. Bye."

    scene day5 ev06-47
    play sound vespa_start_drive
    "Putting away her phone, Jessica starts up her scooter and rides off, eager to get home."
    JesT "Oh, I can't wait to relax. After this week, it'll be nice to get my mind off work for a little while."
    stop sound fadeout 2

    jump day05eveninghome

label day05eveninghome:

    scene day5 ev07-01 with fade
    "Strolling in, exhausted from her busy week, Jessica is ready to collapse on the couch."
    "Laura is already there, though, sketchbook in hand, pencil-tip rapidly rolling along the paper."
    Jes "Hey, Laura."

    scene day5 ev07-02
    Lau "Oh! Jessica!"
    "Laura quickly scrambles to put the sketchbook away."
    Lau "I didn't hear you come in."
    "Jessica puts her purse down on her desk and takes a seat on the couch, noting Laura's reaction."
    JesT "It's so weird that she's so shy about showing off her work. That still hasn't changed."
    Jes "I can't see your drawing?"

    scene day5 ev07-03
    Lau "Nah. It's not done yet. How was your day?"
    "Jessica groans as she pulls her heels off."
    Jes "Long and exhausting. My feet are killing me."
    Jes "I didn't think you'd be here when I got back. I thought you'd already be out."
    Lau "Well, they each had something to do before we all got together, so I just came back to chill for a bit."

    if "d05victorHJ" in choices:
        scene day5 ev07-04
        Jes "Mmm."
        Lau "Is something wrong?"
        Jes "Just… a little work thing."
        Lau "Anything in particular?"
        Jes "Well… the thing is, I have a story I'm working on. One that could make my career."
        Jes "I just don't know how far I should go for it, you know?"
        Jes "I mean, how far is too far? At what point am I just whoring myself out for my paper?"

        scene day5 ev07-04b with dissolve
        Lau "You mean like with the constant work? Sacrificing all your free time?"
        Lau "I know what you mean. This chick in my dorm, Louisa, is killing herself trying to get this student film done."
        if slut >= 13:
            JesT "No. Not nearly the same as jerking off a guy you just met, with a lovely big dick and gallons of cum."
            JesT "I'll bet it's not nearly as much fun either, even if I do feel like a cheap whore for doing it."
        else:
            JesT "No. Not nearly the same as jerking off a guy you just met. Not nearly as gross, for one thing."

        Lau "Thing is, I mentioned something to Louisa, and she said that she can relax once the project's done. It's a lot of work now, but then she'll have a great piece of work to show off."
        Lau "So, as long as it's temporary and it's not hurting you or Conner, a heavy workload isn't so bad."
        Lau "Plus, you spent so much time getting your degree, and you quit your previous job for this one. Shouldn't you just stick it out?"
        Jes "Huh. So just take the load for my career?"
        Lau "I think that's the best thing, yeah. Don't you think so?"

        scene day5 ev07-05
        Jes "Yeah. Thanks, Laura. That actually really helps."
        Lau "You're welcome."
        Jes "I need to turn to you for advice more often."
        Lau "Yeah, I'm around."
        Jes "When you're not getting high, apparently."
        "Laura rolls her eyes."
        Lau "I'm gonna get you to smoke just to get you to lighten up about that."
        Jes "Honestly? I'd probably go for some right about now."

    else:
        scene day5 ev07-06
        Jes "Just chilling does sound nice after what I just went through."
        Lau "Problems at work?"
        Jes "Kind of. I hit a roadblock with a story, and if I can't find a new lead…"
        Jes "Well, it wouldn't be awful, but it wouldn't be great."

        scene day5 ev07-06b
        Lau "That blows. I hope you can find what you need."
        Jes "Yeah, me too."
        Lau "But then, you never let obstacles bother you. You always found a way around anyone who tried to stop you from doing anything."
        Jes "Yeah. It really pissed Mom off when I got around her rules."
        Lau "Still does. It's like the only thing she ever complains about when it comes to you."

        scene day5 ev07-07
        Jes "Anyway, enough about my day. What about you?"
        Jes "I figured you might already be chill after what you told me earlier."
        Lau "I did not smoke any pot, Jess."
        Jes "Really?"
        Lau "Yep. That's for later tonight."
        "The pair share a laugh and a hug."
        Jes "It's been a while since I've smoked. It might be fun to try again."
        Lau "Oh yeah?"
        Jes "Yeah. Maybe together?"
        Jes "I mean, I haven't had any since high school and college, but I think it could be fun to smoke some weed with my sister."
        Lau "I bet you inhale once and spend an hour coughing."
        Jes "Yeah, probably."

    scene day5 ev07-08 with fade
    "Jessica hears her phone ringing inside her purse. Getting up, she walks over and pulls it out, smiling at Heather's name."
    "She answers, and takes a seat in her chair."
    Jes "Hey, Heather!"
    Heath "Hey, you. How's it going?"
    Jes "Pretty good. I just got in a few minutes ago."
    Jes "I'm gonna go grab a shower real quick."

    if "d05heatherFinger" in choices:
        Heath "Ooh. Can I join you?"
        "Jessica chuckles, but says nothing."
        JesT "That's not a question I can answer right now, Heather."

    Jes "Just come on over whenever. If Laura or I don't answer, just come on in."

    if "d05heatherFinger" in choices:
        Heath "Ah. I see. I'll be there in a few. Bye!"

    else:
        Heath "I'll be there in a few. Bye!"

    scene day5 ev07-09
    Lau "Well, you've got her coming over, so I'm gonna go get ready."
    Jes "Okay. If I don't see you before you leave, have a great night!"
    Lau "You too."

    scene day5 ev07-10 with fade
    "Jessica heads off to her room, undressing and getting in a quick shower."
    "Afterward, she spends quite some time putting up her hair, and trying to decide on just which outfit to wear."
    if "d05victorHJ" in choices and slut >= 13:
        "She smiles, recalling the feeling of Victor's member pulsing in her hand, but soon puts it out of her mind."
        JesT "I should focus on tonight."
    else:
        "She decides to put the earlier incident with Victor out of her mind, and focus solely on the night ahead."

    scene day5 ev07-11 with fade
    "After a while, she settles on a comfortable pink dress that does a wonderful job showing off her curves."
    "Sliding it on, she stares into the mirror, her reflection smiling back at her. She feels incredibly beautiful."
    if "d05heatherFinger" in choices:
        "Her heart beats rapidly in her chest, anticipation building for the night ahead."
        JesT "I hope Heather likes it. I can only try to be as pretty as she is."
        JesT "I can't believe what happened earlier, and the thought of doing it again is making me giddy!"
        "Jessica hears a knock, and what sounds like the front door opening. Taking a deep breath, she pushes her breasts up and nods at her reflection."
        JesT "Okay, girls. Let's go say hi."
    else:
        JesT "Well, this should get me some tonight. Not that I need to show off for Conner, given that he's as ravenous for sex as I am."
        JesT "But I feel so damn sexy right now. I can't wait to see what Conner's like after Heather gives him a few tips."
        if "d03dinnerLick" in choices:
            JesT "And if he doesn't improve, there's always his dick to make me feel better."
        else:
            JesT "And if he's not any good, there's always his dick to make me feel better."

        "Jessica hears a knock, and what sounds like the front door opening. She smiles and heads out to go greet her dinner guest."

    scene day5 ev07-12 with fade
    "Heather is standing in the living room, smiling at Jessica as she enters."
    Jes "Hey, Heather!"
    Heath "Damn, Jessica! That dress is incredible!"
    "Jessica feels herself starting to blush."
    JesT "It really does run in the family."
    Jes "You think?"
    Heath "Definitely. You are absolutely stunning."

    if "d05heatherFinger" in choices:
        scene day5 ev07-13
        "Heather pulls Jessica close, a hunger in her eyes."
        Heath "I just wanna eat you up."
        "Jessica resists, jerking her head back toward the guest bedroom and speaking quietly."
        Jes "Laura's still here, remember?"
        Heath "Okay. Does she want to join us?"
        Jes "Oh my god! You're terrible!"

    scene day5 ev07-14 with fade
    "Heather takes a seat at the dinner table, Jessica bringing a bottle of wine and a couple of glasses."
    Jes "So, you said Christian is out for work?"
    Heath "Mm-hmm. His company's holding a workshop, so he won't be back until Monday."

    scene day5 ev07-15
    Jes "Cool. What's the workshop for?"
    Heath "Creating dynamic solutions in a mobile market or something like that. I don't know."
    Heath "I'll be honest. When he talks about stuff like that, my eyes just kind of glaze over and I think about a movie."
    Heath "And this is coming from a woman who spends her days reading through divorce rulings."
    Heath "So anyway, how'd your day go?"
    "Jessica chuckles."
    Jes "I had an… interesting day. Definitely the kind that warrants a bottle of wine."
    Heath "Rough few hours?"

    scene day5 ev07-16
    Jes "Kind of. I have a big story I've been trying to get, and I ran into a roadblock."
    Heath "What kind?"
    Jes "The kind that wanted certain favors."
    "Heather nods knowingly, taking a sip of her wine."
    Heath "Isn't that the way of it?"
    Heath "You've got to work twice as hard to get ahead, and do some things you're really not proud of."
    Heath "It's almost a rite of passage for any successful woman."
    Jes "It's still bullshit."
    if slut >= 13:
        JesT "Even if it was fun."

    Heath "That it is."
    "Jessica looks up, seeing Laura coming over."

    scene day5 ev07-17
    "Heather turns at Laura's approach, giving the younger woman a smile."
    Heath "Hey, Laura. You look fantastic!"

    if "d05heatherFinger" in choices:
        "Jessica feels a twinge of jealousy. She doesn't like having Heather's attention pulled away, especially given how incredibly hot Laura is looking at that moment."
        "She pushes the feeling down, though, knowing she's being silly."

    Lau "You think?"
    Heath "Absolutely. It's a wonderful dress, and I love those shoes!"
    Heath "You and your sister are both so damn pretty!"
    Lau "Thanks! Personally, I hate my hips, and I was thinking this outfit makes my thighs look way too big."
    Jes "You look beautiful, Laura. Stop listening to what Mom says about your legs."

    scene day5 ev07-18
    Heath "I thought you'd have left before I got here."
    Lau "The others had some things to do, so I came back, but I'm taking off now. You ladies have a good night."
    Jes "I'll see you later, Laura."
    Heath "Bye, Laura. It was nice to see you again!"
    Lau "You too. Take care!"

    scene day5 ev07-19
    "Laura's out the door a moment later, Heather turning back to Jessica."
    Heath "Seriously, your parents must have been incredibly attractive to turn out such beautiful daughters."
    Jes "Flatterer."
    Jes "Yeah, my dad was a good looking guy, and my mom is a pretty woman. That's her on the wall, the one with the blue blazer and white blouse."
    Heath "I can definitely see where you got your beauty from."

    if "d02hotRun" not in choices or "d05heatherStop" in choices:
        Heath "So, what's this big story you're working on?"
        Jes "You know the vigilante that showed up recently?"
        Heath "Mm-hmm."
        Jes "I'm trying to find out about him."
        Jes "Maybe even find him."
        Heath "That's bold. You've been working a week, and already you're tracking down masked brawlers."
        Jes "What can I say? I move fast."
        Jes "Well, I should get dinner started."

    else:
        if "d05heatherLesson" in choices:
            "Heather grins."
            Heath "So, tell me more about the other night. What was it like, having Conner go down on you?"
            Jes "Well, it was just kind of… meh. No, that's not it. Mediocre sex is still fun. This was just disappointing."
            Jes "It wasn't fun at all. It felt like a waste of time."
            Heath "That sucks. But we can give him a nice little show, and a few pointers."
            Heath "By the time we're done, he should be able to make your toes curl with that tongue of his."
            Heath "Does that sound good?"
            Jes "I think it sounds great. I'd really love if Conner could make me cum with his tongue."
            Heath "Fantastic! I can't wait for him to get home. This'll be fun!"
            Jes "I should get dinner started."

        elif "d03lickLie" in choices:
            "Heather grins."
            Heath "So, did you and Conner do anything the other night after you left?"
            Jes "Well, we tried something new. Conner went down on me."
            "An eager smile comes over Heather's face."
            Heath "And?"
            Jes "And it... wasn't great."
            Heath "Ah. He's not great with his tongue, then?"
            Jes "Definitely not."
            Heath "That's unfortunate. But it's not surprising that he wasn't great his first time."
            Heath "I could give him some pointers if you wanted? Maybe see if he can improve his game?"

        else:
            Heath "So, did Conner go down on you at all? Like we discussed the other night?"
            "Jessica shakes her head."
            Jes "No. We haven't tried it yet."
            Heath "You're still interested, though, right?"
            Heath "Would you like me to maybe convince him to try it?"

        if "d03lickLie" in choices or "d03spyNoSex" in choices:
            JesT "Do I want this?"
            JesT "I mean, should I bother when I could just go to Heather for that kind of satisfaction?"
            JesT "I doubt Conner could ever be as good as she is with her tongue."

            menu:
                "Let Heather talk with him":
                    "Jessica feels her nethers tingle in delight at the thought."
                    Jes "Sure. If you could, that would be wonderful."

                "Heather's enough":
                    $ choices.append("d05noConner")
                    Jes "Actually, now that I think about it, I don't think we should bother."
                    "Heather's brow furrows in confusion."
                    Heath "What do you mean?"
                    Jes "I mean… you and I could do this stuff alone. Why go through all the hassle of involving Conner?"
                    "Heather's eyes go wide, unprepared for such a question."
                    Heath "Um… okay."
                    Jes "We can have some fun together, just you and me."
                    "Jessica smiles, then stands and moves toward the kitchen."
                    Jes "Anyway, I should get dinner started."
        else:
            "Jessica feels her nethers tingle in delight at the thought."
            Jes "Sure. If you could, that would be wonderful."
            Heath "Alright, I'll do my magic and set your boy on the right path."
            Jes "I should get dinner started."

    scene day5 ev07-20  with fade
    "Jessica strolls over to the kitchen. She turns on the stove, and is soon frying the meat for their meal while Heather comes over and begins slicing vegetables."
    Heath "I have to say, I'm pretty impressed with how your work is going."
    Heath "You've been there a week and already you're making waves. People like waves."
    Jes "Ha! So do I. This last week has been… very interesting."
    Jes "Who knew so much fucked up shit happens in this city?"
    Heath "Everyone, but I'm sure it's interesting seeing all the details that most of us don't get."
    Jes "Interesting is a word for it. Perverted is another. Remind me to tell you about this ass we met who tried to get me and my coworker into bed."

    if "d05heatherFinger" in choices:
        scene day5 ev07-21b
        Heath "Well, I don't have any room to talk there."
        "Heather moves closer, slipping her arm around Jessica. Jessica gasps, a jolt of energy shooting through her body at the woman's touch."
        Heath "Where's Conner, by the way?"
        Jes "He had to work late. He said he'd be back soon."
        Heath "So then… we have a little while alone?"

        scene day5 ev07-22
        "Jessica turns in Heather's direction, her heart pounding in her chest."
        "Heather quickly takes the lead, moving to plant her lips against Jessica's."
        "The pair pull each other closer, Jessica moaning softly as the embrace deepens."
        JesT "This is incredible. I still can't believe I'm doing this with her."
        JesT "She feels wonderful. Her lips are so soft, and she tastes so sweet."

        scene day5 ev07-23
        "The sizzling of meat draws her attention back to the stove."
        JesT "We really shouldn't be playing next to a fire like this. Plus, I don't want to burn our meal."
        "Jessica awkwardly pulls out of the kiss, turning her attention back to the stove."
        Jes "I, um... *cough* I should make sure this doesn't burn."
        Heath "Mm-hmm."
        "Heather doesn't miss a beat, quickly sliding behind Jessica. Her arms circles Jessica's waist, pulling their bodies together once more as her lips caress Jessica's neck."
        Heath "Mmm."
        "Heather's soft moans begin driving Jessica wild."
        JesT "Oh god, this feels incredible."

        scene day5 ev07-24
        "Heather's hand slips down to Jessica's thigh, slowly pulling up the skirt."
        "Her fingertips begin rolling back and forth in a circular motion, gently stroking Jessica's soft thighs."
        JesT "Fuck, if she keeps this up, I may just cum standing right here."
        Heath "Does that feel nice?"
        "Jessica's moans are answer enough."

        scene day5 ev07-24b with dissolve
        if "d05heatherLesson" in choices:
            JesT "Come on, Jessica. Show some control. We should wait for Conner."
            "Her hand comes down, stopping Heather's caressing of her thigh."
            Jes "Let's wait for Conner. We don't want to have too much fun without him, do we?"
            Heath "Oh, phooey."
            "Heather feigns disappointment, but laughs and plants one more kiss on the back of Jessica's neck."
            Heath "I'm a patient woman. I can wait for what I want."
            JesT "Oh my god. This is gonna be one hell of a night."

        else:
            JesT "Come on, Jessica. Show some self-control. You really are gonna burn dinner."
            "Her hand comes down, stopping Heather's caressing of her thigh."
            Jes "Come on, now. I really do need to cook, unless you want your meal burnt to a crisp."
            Heath "Oh, phooey."
            "Heather feigns disappointment, but laughs and plants one more kiss on the back of Jessica's neck."
            Heath "I'm a patient woman. I can wait for what I want."
            JesT "Oh my god. This woman's going to drive me crazy!"

    else:
        scene day5 ev07-21a
        Heath "I can't say I'm surprised. Still, a woman's allure can open quite a few doors."

        if "d02flirtAngus" in choices or "d03vigilanteVideo" in choices or "d05victorHJ" in choices:
            Jes "Believe me, I know."
            Heath "Oh, do tell."
            Jes "Some other time. I'm a little worried I'll be spilling the beans and Conner will get home."

        Heath "Where is Conner, by the way?"
        Jes "Oh, he had to work late. He said he'd be back soon."

    scene day5 ev07-25 with fade
    "Jessica finishes prepping the meal, and slides it into the oven."
    Jes "There we go. Conner's a patient guy, but he does hate to wait for his food."
    Jes "We have that in common."
    Heath "I know. I saw you eating the other night, like your meal might try to escape."
    "Jessica shrugs."
    Jes "Yeah, I know. My eating habits may be my least feminine trait."

    if "d05heatherFinger" in choices:
        scene day5 ev07-27
        "Jessica moves in close to Heather's side, Heather's arm pulling her close."
        "Once again, an electrifying sensation fills Jessica's body, her heart beating rapidly in her chest."
        Heath "I wouldn't worry about it. You're such a beautiful woman, I doubt anyone really notices."
        Heath "Certainly not when you wear such gorgeous dresses."
        "Jessica blushes, staring up into Heather's eyes."
        Jes "Well, I really like your dress. It shows off your curves so damn well."
        "Heather chuckles."
        Heath "They're nothing next to you, sweetie. I bet you have both men and women falling over themselves to get close to you."
        Heath "I certainly am."

        if "d05heatherLesson" in choices:
            JesT "She's driving me crazy. But we should wait for Conner."
            Jes "Come on, let's drink some more wine while we wait for Conner to join us."

            scene day5 ev07-42 with fade
            "Once the food is in the oven, the pair take a seat at the table and chat about various things."
            "Heather talks about both her own work as well as Christian's, while Jessica relates the tale of her search for the vigilante, though she omits the details involving Victor."
            Heath "So, how does Conner feel about tonight?"
            "Jessica sighs."
            Jes "Well, he seemed pretty excited when I brought it up, but I'm not sure if he thought I was serious or not."
            Jes "We'll see how he reacts. I think he'll probably enjoy himself."
            "After a few minutes, the pair hear keys turning the front door opening."

            scene day5 ev07-43
            "Conner strolls around the corner a second later, looking rather exhausted."
            Con "Hey, ladies. How's it going?"
            Jes "Hey, baby. We're good. Just chatting while the food cooks. How was your day?"
            Con "Long, and tiring. I won't bore you with the details."

            scene day5 ev07-43b
            "Conner strolls over and plants a kiss on Jessica's lips."
            Con "I'm gonna go grab a shower, and then I'll come join you."
            Jes "Okay, baby."

            jump day05dinner

        else:
            scene day5 ev07-28
            $ choices.append("d05wearMine")
            "A moment of tense silence leads to both ladies turning to one another."
            "Their hands grasp one another as their lips come together once again. Soft moans slip from Jessica's lips, accompanied by the wet smacking of the kiss."
            JesT "I really can't remember the last time Conner kissed me like this. He's so rough and commanding, but she's so gentle and caring."
            "The thought of Conner brings the worry of being caught to her mind, but she quickly pushes it back."
            JesT "I don't want to stop. This is incredible. I can't believe how good this feels."

            scene day5 ev07-29
            "Heather's hand soon slips down Jessica's body, over her bosom and to her skirt."
            "Sliding up the hem, Heather's fingers began to caress Jessica's tender sex through her panties."
            "Jessica's moans turn into soft whines, her body tensing as subtle pleasure fills her womanhood."
            JesT "Oh god, that feels good. Don't stop, baby!"
            "Heather's fingers continue to stroke back and forth, rubbing between Jessica's clit and her quickly soaking folds."

            scene day5 ev07-30a with dissolve
            "Gradually, their kiss becomes more passionate, Jessica eagerly returning Heather's affection."
            "Soon, Heather's hand moves upward, sliding into the waistband of Jessica's panties."
            JesT "Please, keep going. I want to feel your fingers on my pussy again!"
            "Jessica feels no need to voice her thoughts. The eagerness of their embrace is more than answer enough to Heather's unspoken question."

            scene day5 ev07-30b with dissolve
            "Heather's fingers move closer to Jessica's tender womanhood, yet don't quite reach their destination."
            "Instead, they circle back and forth, teasingly moving closer and closer before pulling away again."
            "Jessica's whines intensify, as she becomes desperate to feel Heather's fingers on her clit."
            JesT "Goddamnit, stop teasing me, and get in there!"

            scene day5 ev07-31
            "Much to Jessica's surprise, Heather's fingers slip from her panties."
            "Heather then kneels in front of Jessica, her fingers sliding up Jessica's thighs."
            Jes "Ah. What- what are you doing?"
            "Heather grins and chuckles."
            Heath "Oh, I was just thinking these panties are gonna get in the way."

            if persistent.pov == 2:
                scene day5 ev07-31fpov
            Heath "I think I want to get rid of them."
            "Jessica is dumbstruck, unable to think or move."
            "All she can do is stare at the gorgeous woman below her, whose fingers are even now looping through the waistband of her panties and pulling them down."
            JesT "She's so beautiful."
            "Any other thoughts flee Jessica's mind. At the moment, Heather is her world."

            scene day5 ev07-32
            "Soon, Jessica feels her panties sliding down past her knees, Heather smiling up at her with a mischievous smile."
            Heath "There we go. How's that feel?"
            Jes "Freeing. And there's a nice breeze."

            scene day5 ev07-33
            "With a playful laugh that sounds almost maniacal, Heather stands up, holding Jessica's panties out of reach."
            Heath "Now I feel overdressed. Why don't you slip mine off too?"
            Jes "I think that sounds like a fantastic idea."

            scene day5 ev07-34
            "Heather pulls Jessica over to the table and sits her down. Jessica's hands almost immediately begin sliding up Heather's legs."
            "Heather smiles down at her before tossing Jessica's panties onto the other chair and reaching up to caress her cheek."
            "Jessica's hands gently squeeze Heather's legs, enjoying the feeling of her lovely companion's body."

            scene day5 ev07-35
            "Slowly, without either woman saying a word, Jessica begins to push Heather's skirt upward."
            "She's in no hurry, and savors the feeling of Heather's soft, lovely legs."

            scene day5 ev07-35b with dissolve
            "Eventually, her fingers reach the waistband of Heather's panties. She loops the tips through and begins pulling down slowly."
            Heath "I knew you could be a naughty girl, Jessica."

            if slut >= 13:
                Jes "I bet I can be so much naughtier than you think."
                "Heather laughs."
                Heath "We'll see."

            else:
                JesT "Even I'm surprised by what I'm doing."
                JesT "Not that I'm gonna stop. This is too exhilarating."

            scene day5 ev07-36
            "The black undergarment slides down with ease, slipping from Heather's legs with a soft sigh."
            "Heather lifts her leg up, allowing Jessica a glimpse of her bush, just peeking out from beneath her dress."
            JesT "I'm sitting in my kitchen, with another woman's pussy staring right at me while I'm holding her panties in my hand."
            JesT "Of all the things that have happened to me this week, this might be the most unexpected."
            Heath "You like what you see, sweetie?"

            scene day5 ev07-37
            "Jessica is about to respond when she hears the most unwelcome sound in the world: keys sliding into the lock of her front door."
            JesT "Are you fucking kidding me!? Now!?"
            Jes "Shit! Conner's home."
            Jes "Quick, pass me my panties!"

            scene day5 ev07-38
            "Heather reaches over to grab Jessica's panties, but instead of passing them over she sits and begins to put them on yourself."
            Jes "What-?"
            Heath "Just put mine on. Quick."

            scene day5 ev07-39
            "With no options but to hide the black panties somewhere, Jessica quickly begins to slide them up her legs just as she hears the front door open."
            JesT "Shit! Shit! Shit!"
            JesT "Be tired and slow, Conner. Please!"

            scene day5 ev07-40
            "Heather calmly crosses her legs while Jessica pushes them together, her hand involuntarily moving between her thighs as if to hide her shame."
            JesT "Oh wow. Not only are these tight, but they're practically soaked. Heather's just as turned on as I am."
            JesT "This feels so wrong, so incredibly dirty! I have another woman's filth pressed against my pussy!"
            JesT "I've never felt naughtier in my life!"
            "Conner strolls around the corner a second later, looking just as tired as Jessica had hoped he'd be."
            Con "Hey, ladies. How's it going?"
            "Jessica smiles nervously, her voice slightly shaky."
            Jes "Hey, baby. We're, uh, we're good. Just chatting while the food cooks. How was your day?"
            Con "Long, and tiring. I won't bore you with the details."

            scene day5 ev07-41
            "Conner strolls over and plants a kiss on Jessica's lips."
            Con "You okay, baby?"
            Jes "Yeah. Yeah, I'm- I'm fine. Why?"
            Con "You just seem a little flustered."
            Jes "Yep. I'm great."
            JesT "I'm wearing Heather's soaking panties! I'm certainly having a strange evening!"
            Con "Okay then."
            Con "I'm gonna go grab a shower, and then I'll come join you."
            Jes "Okay, baby."

            jump day05dinner

    else:
        scene day5 ev07-26
        Heath "I wouldn't worry about it. I doubt unfeminine is something anyone ever thinks about when looking at you."
        Heath "I mean, you're standing next to me in a bright pink dress."
        Jes "Well, I really like your dress. It shows off your curves so damn well."
        Heath "Well, thank you. Mine still pale in comparison to yours."

        scene day5 ev07-42 with fade
        "Once the food is in the oven, the pair take a seat at the table and chat about various things."
        "Heather talks about both her own work as well as Christian's, while Jessica relates the tale of her search for the vigilante, though she omits the details involving Victor."
        "After a few minutes, the pair hear keys turning the front door opening."

        scene day5 ev07-43
        "Conner strolls around the corner a second later, looking rather exhausted."
        Con "Hey, ladies. How's it going?"
        Jes "Hey, baby. We're good. Just chatting while the food cooks. How was your day?"
        Con "Long, and tiring. I won't bore you with the details."

        scene day5 ev07-43b
        "Conner strolls over and plants a kiss on Jessica's lips."
        Con "I'm gonna go grab a shower, and then I'll come join you."
        Jes "Okay, baby."

        jump day05dinner

label day05dinner:

    scene day5 ev07-44 with fade
    if "d05heatherPleasure" in choices:
        "When Conner closes the door to the bedroom, Jessica breathes a sigh of relief, drawing a smile from Heather."
        Jes "Come on. Let's, uh, set the table."
        "The pair get up, grabbing the silverware and setting a place for each of them."
        Jes "What was that?"
        Heath "With the panties? I thought it'd be hot, and it totally is."
        Heath "I love the idea of you wearing my panties all night, and Conner having no idea."
        Jes "You really are a dirty girl."
        Heath "And you love it!"

    elif "d05heatherLesson" in choices:
        Jes "Come on. Let's set the table."
        "The pair get up, grabbing dinnerware and setting a place for each of them."
        Heath "It was a good idea we stopped earlier. It looks like Conner would have walked in on us, and maybe had the wrong idea."
        Jes "True."
        Heath "Or maybe he would have had the right one and been turned on."
        Jes "Conner may not look it, but he's a sensitive guy. He wouldn't want to see his girlfriend doing anything with anyone else. Not without talking about it first."
        Heath "You're lucky to have such a sweet guy."

    else:
        Jes "Come on. Let's set the table."
        "The pair get up, grabbing dinnerware and setting a place for each of them."

    scene day5 ev07-45 with fade
    "Soon the trio are sitting at the table together, eating and chatting."
    "Jessica goes over how her day went, though she omits certain details of her visit to Victor's garage."
    if "d05heatherFinger" in choices:
        "Not to mention her visit to Heather's."

    "Heather sits quietly for the most part, patiently listening to the couple sharing their daily experiences."
    Con "By the way, we got invited to a wedding next weekend."
    Jes "Oh. Wow. That's so soon. Who's getting married?"
    Con "You remember Jeffrey Hutman? We knew him in high school?"
    "Jessica scoffs."
    Jes "Oh, him. Yeah. Pizza the Hutt."
    Heath "Wait, what?"
    Jes "He was a chubby kid, obsessed with Star Wars. We called him Pizza the Hutt."
    Con "Hey, come on. Don't be mean."
    Jes "Sorry. That was childish. He was creepy, though."
    Con "I know, but he was my friend. It would mean a lot to him if we could go."

    scene day5 ev07-46
    Heath "You should absolutely go. It's a wedding, Jessica. I bet you'll have a blast."
    Jes "Yeah. Sure. It's short notice, but I don't see why not."
    Heath "Just be ready for the inevitable, ‘When are you two getting married?', questions."
    Jes "I'm used to that. I already get that from my mom."
    Con "She just knows how great I am, is all."
    "Conner smiles playfully while Jessica rolls her eyes."
    Jes "Sure, sweetie."

    scene day5 ev07-47
    Heath "Christian and I got that a lot. Obviously, he eventually proposed."
    Heath "Saying yes was a no-brainer, given how incredible that man is in bed."
    JesT "Yeah, if Conner ever proposes, I'll probably say yes just as easily."
    Jes "So, who's Pi-. Sorry. Who's Jeffrey marrying?"
    Con "The head cheerleader from our class. Connie Amiko."
    Jes "Really?"
    Con "Yeah. He got rich, and started dating Connie a little while after. I guess cheerleaders can't help spreading for a man with money."
    "Both Jessica and Heather fix their gaze on Conner."
    Jes "You do remember that I was a cheerleader, right?"
    Heath "So was I."
    "Conner coughs awkwardly."
    Con "Wow, this foot-in-my-mouth tastes delicious, Jess, and have I mentioned how pretty you are tonight?"

    scene day5 ev07-48
    "Jessica sighs and shakes her head."
    Jes "Anyway, you said it's next weekend?"
    Con "Yep."
    Jes "Okay. I'll make sure my work's all wrapped up by then."
    Jes "Anyone else we know going to come?"
    Con "I'm not sure. Hopefully."
    Jes "Well, I did know Connie, at least. It should be fun to catch up."

    if "d05noConner" in choices:
        scene day5 ev07-52
        "After the group finishes dinner, they sit and chat a bit. They talk about Conner's work and Jessica's investigation."
        Heath "Well, I should get going. Dinner was delicious. Thanks for having me over, you guys."
        Con "Thanks for coming over, Heather."
        Jes "Yeah, it's great having you. Come on. I'll walk you out."

        scene day5 ev07-53 with fade
        Heath "I had a wonderful time, Jess. Thanks again."
        Jes "You're welcome. You want to get together tomorrow sometime?"
        "Jessica's smile says what her words cannot, given that her boyfriend is within earshot."
        Heath "I'd like that. Whenever works for you. I've got nothing planned for the day."

        scene day5 ev07-54
        "Heather steps outside, but before Jessica can close the door, Heather drags her outside as well."
        "She makes sure to pull the door shut as far as she can before Heather pulls her into a passionate embrace."
        "Jessica gives in, moaning softly as they share a goodnight kiss."
        "It lasts only a second, so Jessica can go back inside before they're caught."

        scene day5 ev07-54b with dissolve
        Heath "I can't wait to see you tomorrow, sweetie."
        "Jessica licks her lips."
        Jes "Yeah. I'll see you then."
        "Heart pounding inside her chest, Jessica heads back inside."

        scene day5 ev07-55 with fade
        "Heading back inside, Jess strolls over and pats Conner on the back."
        Jes "This was a nice night, sweetie."
        Con "Yeah. It was fun."
        Jes "Let's get this place cleaned up."
        Con "Definitely. I'm exhausted. I think I'm gonna turn in early."
        Jes "I'll join you. I've had a long day too."
        "The pair put the dishes away in the washing machine and head off to bed."

        jump day05end

    else:
        scene day5 ev07-50
        "As the group finishes their dinner, Heather begins telling stories about her marriage to Christian. Eventually, the stories begin becoming quite lewd."
        Heath "And let me tell you, he was good before we met, but now he's incredible!"
        Heath "I never knew how wonderful having a man go down on you was before Christian introduced me to it, but he's only managed to get better and better."

        scene day5 ev07-51
        if "d05heatherLesson" in choices:
            Con "Yeah, I, uh, imagine there's some artistry to it."
            Heath "Most definitely. It's like any other kind of sex. Few people are good at it the first time they try, but keep it up and you can become a master."
            "Conner's eyes briefly flit to Jessica, who meets his gaze before he looks away and coughs."
            Con "Sure, sure. Oh, I'm stuffed."
            "Heather smiles at him, Conner trying to avoid her gaze. He begins picking at the remains of his meal."
            Heath "You know, I've spent quite a bit of time having Christian going down on me. I'm familiar with the proper techniques a man would use."
            Con "You know what we should do? Why don't we go watch something?"
            Con "Dinner was great, babe."
            "Conner quickly gets up, doing his best not to look at either woman."

        elif "d03lickLie" in choices:
            Con "Yeah, I, uh, imagine there's some artistry to it."
            Heath "Most definitely. It's like any other kind of sex. Few people are good at it the first time they try, but keep it up and you can become a master."
            "Conner smiles, his eyes lighting up and briefly flitting to Jessica."
            JesT "Oh geez, he thinks he's the exception. What have I done?"
            JesT "Still, he looks a little uncomfortable talking about it."
            Con "Sure, sure. Oh, I'm stuffed."
            "Heather smiles at him."
            Heath "You know, I've spent quite a bit of time having Christian going down on me. I'm familiar with the proper techniques a man would use."
            Con "You know what we should do? Why don't we go watch something?"
            Con "Dinner was great, babe."
            "Conner quickly gets up, doing his best not to look at either woman."

        else:
            Con "Yeah, I, uh, imagine there's some artistry to it."
            Heath "Most definitely. It's like any other kind of sex. Few people are good at it the first time they try, but keep it up and you can become a master."
            "Conner's eyes briefly flit to Jessica, who meets his gaze before he looks away and coughs."
            Con "Sure, sure. Oh, I'm stuffed."
            "Heather smiles at him, Conner trying to avoid her gaze. He begins picking at the remains of his meal."
            Heath "So, have you ever considered…?"
            Con "You know what we should do? Why don't we go watch something?"
            Con "Dinner was great, babe."
            "Conner quickly gets up, doing his best not to look at either woman."

    scene day5 ev08-01 with fade
    "Conner dims the lights, all three of them moving to the couch while he turns on the TV and begins flipping through channels."
    "For a little while, Conner tries to make small talk, going back over some small details of his day."
    Con "Anyway, that's how he managed to almost choke on his own toe."
    Jes "Wow, that's weird."
    Heath "I was with a guy once who liked the whole foot thing. I have to admit, there was a unique pleasure to having my toes sucked."
    Heath "I prefer a more direct approach to pleasure, though. I like a man going right to the source."
    "Conner says nothing, shifting uncomfortably."

    if "d05heatherLesson" in choices:
        Heath "And believe me, a man who knows what he's doing with his tongue is a gift from the gods."
        Heath "I could give you a few tips if you like."
        "Jessica speaks up before Conner can divert the conversation once again."
        Jes "Come on, baby. She knows how it's done, and we could use the help, right?"

        jump day05womansTouch

    elif "d03lickLie" in choices:
        Heath "And believe me, a man who knows what he's doing with his tongue is a gift from the gods."
        Heath "I could give you a few tips if you like."
        "Jessica speaks up before Conner can divert the conversation once again."
        Jes "Come on, baby. A little advice could help you get even better."

    else:
        Heath "And believe me, a man who knows what he's doing with his tongue is a gift from the gods."
        Heath "Have you ever tried going down on Jessica, Conner?"
        Con "Uh…"
        Jes "No, we've never done that before."
        Heath "Oh, it's wonderful, and so very intimate. A woman loves it when a guy is man enough to make her cum like that."
        Jes "I'll bet."

    scene day5 ev08-02
    "Conner shift in his seat again, but turns his gaze to Heather."

    if "d03lickTrue" in choices:
        Con "Uh, yeah. Why not?"
        "Jessica touches Conner's arm gently, smiling at him in thanks."
        Heath "Well, the most important thing is paying attention to your partner. You want to learn her rhythms, and what makes her feel good."
        Heath "Tease her a little. Treat it like foreplay."
        Heath "Then go slow, and don't try to force anything. Find a technique that makes her feel good, then keep at it. Take your time, and you'll get her there soon."
        "Conner nods, listening intently as Heather goes on. Jessica smiles, happy that Conner's willing to take her advice."

    elif "d03lickLie" in choices:
        Con "Sure. Why not?"
        Heath "Well, the most important thing is paying attention to your partner. You want to learn her rhythms, and what makes her feel good."
        Heath "Tease her a little. Treat it like foreplay."
        Heath "Then go slow, and don't try to force anything. Find a technique that makes her feel good, then keep at it. Take your time, and you'll get her there soon."
        Con "Uh-huh."
        "Jessica's brow curls as she realizes he's not really paying attention."
        JesT "Goddamnit. Lying to him has only made him so cocky he thinks he doesn't need advice."
        "She reaches over and touches Conner's arm."
        Jes "This does sound pretty nice. We should take her advice."
        Con "Of course, babe."
        "Conner smiles at Jessica and nods, turning his attention fully back to Heather."

    else:
        Con "Oh?"
        "Conner's eyes flit from Heather to Jessica and back. Jessica just smiles at him, her expression telling of her delight."
        JesT "Oh, yeah, I want you to make me cum like that, Conner."
        Heath "Definitely. But you've got to take it slow. When a man dives in without knowing what he's doing, he can just end up boring his partner."
        Heath "You've gotta take your time, learn what she likes and bring her slowly toward orgasm."
        Heath "Tease her a little. Build up to the main event, like foreplay."
        Heath "And then, when you get in there, she'll be squealing in delight."

    "Heather goes on, beginning to discuss some basic techniques, while both Conner and Jessica listen raptly."
    "Conner's attention is definitely piqued by Heather's description, and Jessica is fairly certain he's becoming hard just listening."
    "Jessica, though, is becoming soaking wet listening to Heather discuss proper tongue usage."

    if "d05heatherFinger" in choices:
        JesT "Dear god, this is hot! I want of feel Heather's tongue on my pussy more than ever!"
    else:
        JesT "Dear god, this is hot! I want to feel Conner's tongue on my pussy right now!"

    scene day5 ev08-03
    "After a few minutes, Heather smiles, eyes briefly roaming over Conner's pants."
    Heath "Well, I hope that helps. I have a feeling I should probably leave you to it."
    "Jessica smiles, noting the coyness in Heather's voice."
    JesT "Oh, but it would be so very naughty if you stayed."

    if "d02tellConner" in choices:
        JesT "It felt so good having that hobo watch us the other day, and Conner liked it too."
        JesT "I can only imagine how Conner would feel being watched by someone like Heather instead, and I know she'd like to stay."
        JesT "It might be a little too weird, though, having someone else watching us. I've already got butterflies in my stomach."

        menu:
            "Ask Heather to stay":
                $ choices.append("d05heatherWatch")
                $ relHeather += 1
                $ slut += 1
                $ kink += 1
                $ blowjob += 1
                "Jessica smiles soft, rubbing Conner's arm gently with her fingers."
                Jes "Heather, would you… like to stay?"
                Con "Wha-? Really?"
                Jes "Yeah. That way, she can give us a few tips. You know, if we need them."

                jump day05headWithAudience

            "No, it'll be awkward":
                "Jessica sighs softly, feeling extremely awkward."
                JesT "Yeah, maybe it's not such a good idea after all."

                jump day05headNoAudience

    else:
        JesT "It felt so good having that hobo watch us the other day. I bet it would feel so much better having Heather watch us."
        JesT "I'm not sure Conner would be into it, though. He was so embarrassed talking about sex with her."
        JesT "I can only imagine how awkward it would be to have sex in front of her."

        jump day05headNoAudience

label day05headNoAudience:

    scene day5 ev08-04
    Jes "We appreciate all the advice, Heather."
    Con "Yeah. That was, uh, really nice of you."
    "Heather smiles, leaning forward to plan a kiss on Jessica's cheek."
    Heath "I hope it helps. Good night. Have fun you two."
    "She stands and heads for the door, leaving Jessica and Conner alone on the couch."

    scene day5 ev08-05
    "Once the door shuts behind Heather, Jessica rolls her body onto Conner, fixing him with a seductive smile."
    "She chuckles, feeling his erection against her sex, and begins speaking to him softly."
    Jes "So, you seemed to enjoy all that sex talk at the end. Seems like you're still enjoying it."
    "Conner smiles."
    Con "It was a little awkward, but I think it was a pretty good night."
    Jes "I think we should see what you've learned, don't you?"

    scene day5 ev08-06
    "Conner grins, pulling Jessica into his embrace."
    "The pair begin kissing passionately, moaning and grinding together."
    "It lasts but a moment, Jessica eager to begin."
    Jes "Take my dress off, baby."

    if "d05wearMine" in choices:
        scene day5 ev08-07b
    else:
        scene day5 ev08-07a
    "Conner swiftly grabs her dress and begins to pull it up and over her head."
    "His hands briefly paw at her body, squeezing her bosoms and drawing a pleasure-filled moan from her lips."
    Jes "Mmm."

    if "d05wearMine" in choices:
        scene day5 ev08-08b
    else:
        scene day5 ev08-08a
    "After a few seconds of being pleasantly groped, Jessica rises and turns around."
    "Her fingers hook into her panties, slowly pulling them while waving her hips, giving Conner a show."

    if "d05wearMine" in choices:
        JesT "Oh shit! I'm still wearing Heather's undies. God, I feel so dirty! I'm such a filthy girl."
        "Jessica's heart pounds away in her chest, but Conner says nothing."

    if "d05wearMine" in choices:
        scene day5 ev08-09b
    else:
        scene day5 ev08-09a
    "Standing and turning to face him once more, Jessica holds the panties in front of Conner's face."
    "She giggles, swinging them back and forth for a moment before tossing them forward."
    Jes "Here you go, baby."

    if "d05wearMine" in choices:
        scene day5 ev08-10b
    else:
        scene day5 ev08-10a
    "Conner grins, grabbing the lacy garment and pulling it to his nose."
    Con "Mmm, you smell incredibly baby."

    if "d05wearMine" in choices:
        JesT "Oh my god! This is so wrong! He's smelling both of us!"

    scene day5 ev08-11
    "Jessica takes a seat on the couch, smiling at Conner. He moves over to her slowly, pushing her legs apart before taking his place between them."
    "Jessica licks her lips, heart pounding away in her chest."

    if "d03lickLie" in choices:
        scene day5 ev08-11b
        "Unexpectedly, however, Conner quickly dives in, shoving his tongue into Jessica."
        "She gasps, grabbing his face and pulling him up."
        Jes "Baby, let's try going with what Heather suggested. Try taking your time."
        "Conner nods, though he seems a little irritated."
        Con "Okay."
        JesT "I've created a monster. Lesson learned."

    scene day5 ev08-12
    "With a sigh, Conner runs his fingers over the inside of Jessica's thigh, gently caressing her supple flesh."
    "Jessica moans, smiling when he moves to kiss her leg, slowly moving up toward her eager sex."
    JesT "Oh wow. This is already better. Thank you Heather!"

    scene day5 ev08-12b
    "Conner chuckles, moving in to kiss her labia, but only brushing her with his lips before pulling away. Instead, he begins kissing around it instead, as well as moving back to her inner thigh."
    JesT "Oh! Conner, you tease!"
    "Jessica giggles, reaching down to take his head and pull him toward her."
    "To her surprise, he grabs both her hands, holding them down as he moves in closer."

    scene day5 ev08-13
    JesT "Okay, this is nice, but I'm already getting impatient. I need to feel him on me!"
    Jes "Oh Conner, please! Stop teasing and lick me!"
    Con "Well, Heather did say to tease a little."
    Jes "Yeah, tease, not torture."
    "Conner laughs with a grin, before moving in and giving her clit a light flick of his tongue."
    play voices x_moaning_1 loop
    "Jessica releases a shuddering breath."
    Jes "Oh shit!"

    scene day5 ev08-14
    "After a few more teasing licks, Conner releases her hands and starts sucking gently at her clit."
    Jes "Try going from tip to tip, from my pussy to my clit, with just the tip of your tongue."
    "Conner nods, beginning to slowly lick upward."

    if "d03dinnerLick" in choices:
        "Unlike before, his light and patient touch begins to drive Jessica absolutely wild."

    Jes "Oh my god! Oh my god!"
    Jes "Oh my god! Oh my god!"
    "As he kisses her clit, more lightly than before, she squeals in delight, her breath coming fast and heavy."

    scene day5 ev08-15
    "Conner's thumb soon moves over her clit, gently rubbing up and down while his tongue probes just inside her pussy."
    Jes "Oh god! Oh god!"
    "Jessica can feel her orgasm building, approaching quickly."

    if "d03dinnerLick" in choices:
        JesT "This is nothing like last time. Oh god, he's so good!"
    else:
        JesT "This is incredible! I wish we'd done this sooner!"

    if "d03lickLie" in choices:
        scene day5 ev08-16
        "To Jessica's shock, Conner begins working his tongue as he had two nights back."
        "He begins sucking her clit too hard, while shoving his fingers inside and slamming them against her cervix."
        stop voices fadeout 2
        Jes "Ah, babe, no. Not like that."
        Con "Hmm?"
        Jes "Keep going like Heather had said. Just go slow."
        "Conner stops long enough to grin and chuckle."
        Con "You liked it the other night."
        JesT "What have I done!?"
        Jes "Just… lick me gently. I'm almost there."
        "Conner nods, though she can tell he's annoyed by her instructions."
        JesT "I guess this is what I get. Silly me."
        "He does as she requests, soon bringing her back to the brink of ecstasy once more."
        play voices x_moaning_1 loop
        Jes "I'm gonna cum! I'm gonna cum!"

    else:
        scene day5 ev08-16b
        Jes "Baby, that's so good! Keep going!"
        "Jessica is fairly sure she can see a smile on Conner's lips, no doubt pleased with his performance."
        "She keeps her gaze fixed on him, savoring the sight of her lovely boyfriend pleasuring her."
        JesT "This is so beautiful! Who knew I'd love seeing Conner like this!?"
        JesT "Oh my god, I'm almost there!"
        Jes "Keep going, baby! You're gonna make me cum!"

    scene day5 ev08-17
    stop voices fadeout 1
    play voices x_moaning_2
    "With a cry of joy, Jessica feels her sex quiver as her orgasm begins."
    "Pleasure fills her body, wave after wave of ecstasy washing over her."
    "Conner keeps going the entire time, his tongue never stopping."
    stop voices fadeout 1
    JesT "Oh my god, Conner! Thank you so much for being a quick study!"

    if "d03dinnerLick" in choices:
        JesT "That is SO much better than last time."

    scene day5 ev08-18
    "For a moment after her climax concludes, Jessica lies back, the sound of her heavy breathing filling the room."
    "Eventually she raises her head, smiling up at Conner."
    JesT "Holy crap, that was fantastic! Oh, I'm so glad I had Heather over tonight."
    JesT "Oh, wow, I'm exhausted. I kind of just want to go to sleep now."
    JesT "Then again, it's only fair I return the favor."

    menu:
        "Blow him":
            $ choices.append("d05bjSolo")
            $ relCon += 1
            $ blowjob += 1

            JesT "Let's show him how grateful I am."

            jump day05blowNoAudience

        "Go to sleep":
            $ relCon -= 1
            "Jessica lets out an exhausted moan."
            JesT "I'd like to return the favor, but I can barely keep my eyes open after that."

            scene day5 ev08-19
            Jes "That was wonderful, baby."
            "Conner grins back at her."

            if "d03lickTrue" in choices:
                Con "Really? It was good this time."
                Jes "It was amazing!"
                Con "I'm so glad. I want you to feel as amazing as you make me feel, baby."
                "Jessica pulls up her dress, covering part of her naked body."
                Jes "You do, baby. You really do."
                Jes "You made me cum so hard that I'm exhausted. I can barely keep my eyes open."
                "Conner's smile fades, his disappointment clear."
                Con "You sure? I can keep going."
                Jes "Yeah. I just want to curl up with you now."
                Con "Alright, babe.. Let's go to bed."

            elif "d03lickLie" in choices:
                Con "Oh yeah? Better than last time."
                Jes "SO much better than last time."
                Con "I'm so glad. I love that I can make you feel as amazing as you make me feel, baby."
                "Jessica pulls up her dress, covering part of her naked body."
                Jes "You do, baby. You really do."
                Jes "You made me cum so hard that I'm exhausted. I can barely keep my eyes open."
                "Conner's smile fades, his disappointment clear."
                Con "You sure? I can keep going."
                Jes "Yeah. I just want to curl up with you now."
                Con "Alright, babe.. Let's go to bed."

            else:
                Con "Oh yeah?"
                Jes "It was amazing!"
                Con "I'm so glad. I want you to feel as amazing as you make me feel, baby."
                "Jessica pulls up her dress, covering part of her naked body."
                Jes "You do, baby. You really do."
                Jes "You made me cum so hard that I'm exhausted. I can barely keep my eyes open."
                "Conner's smile fades, his disappointment clear."
                Con "You sure? I can keep going."
                Jes "Yeah. I just want to curl up with you now."
                Con "Alright, babe.. Let's go to bed."

            jump day05end

label day05blowNoAudience:

    scene day5 ev08-20 with fade
    if "d05heatherLesson" in choices:
        "As Conner stands up Jessica pulls him down, holding his face closer and planting a loving kiss on his lips."
        Jes "Did you enjoy it?"
        Con "I did, but not as much as you."

    else:
        "Jessica leans in, pulling his face closer and planting a loving kiss on his lips."
        Jes "That was wonderful, baby."
        "Conner grins back at her."
        if "d03lickTrue" in choices:
            Con "Really? It was good this time."
            Jes "It was amazing!"
            Con "I'm so glad. I want you to feel as amazing as you make me feel, baby."
            Jes "You do, baby. You really do. Now, why don't I return the favor?"

        elif "d03lickLie" in choices:
            Con "Oh yeah? Better than last time."
            Jes "SO much better than last time."
            Con "I'm so glad. I love that I can make you feel as amazing as you make me feel, baby."
            Jes "You do, baby. You really do. Now, why don't I return the favor?"

        else:
            Con "Oh yeah?"
            Jes "It was amazing!"
            Con "I'm so glad. I want you to feel as amazing as you make me feel, baby."
            Jes "You do, baby. You really do. Now, why don't I return the favor?"

    scene day5 ev08-21
    "Jessica stands and leans forward, reaching to pull his pants down."
    Jes "Now, it's your turn."
    Con "And you do it so damn well, baby."
    "She laughs."
    Jes "I was fairly sure I did, given how many times I've swallowed."

    scene day5 ev08-22
    "It's Conner's turn to laugh, though it quickly fades as her fingers close about his fully-erect manhood."
    Jes "Mmm, there's my big boy. He's looking so eager tonight."
    "Her hand begins to rise and fall, slowly pumping up and down the shaft."
    "Her gaze meets his own, a look of desire and lust passing between the two."

    scene day5 ev08-23
    "Jessica leans in, her tongue gently lapping at the tip of his cock."
    "She moans, enjoying the feel and taste of his precum as it coats her tongue."

    if slut >= 13:
        JesT "God, I love the taste of his cum. I just can't get enough of it, and I definitely can't get enough of this beautiful dick!"

    "She licks faster and harder, drawing a long moan from Conner as his head falls back."
    JesT "I'm gonna make you feel as good as you made me feel, baby."

    scene day5 ev08-24
    play voices x_bj_1 loop
    "She begins sliding her tongue up and down the shaft, coating his cock in her saliva."
    "Conner's heavy breathing and constant moans telling her she's already on her way to making him explode."
    Jes "You like that, baby?"
    Con "Oh my god, yes! That feels incredible!"
    "She giggles, continuing to run her tongue up and down its length for several moments."

    scene day5 ev08-25
    "She soon wraps her lips around the thick member, sucking firmly as she begins to bob her head back and forth."
    "Her eyes lock with Conner's, enjoying the expression of pleasure on his face."
    JesT "I love seeing him like this. It's wonderful that I can make him feel so good."

    if blowjob >= 1:
        JesT "I think I'm getting better at this. He seems to enjoy it the more I do it."
        JesT "That's fantastic, since I love sucking this dick so fucking much!"

    scene day5 ev08-26a
    "Jessica moans as she sucks harder, enjoying the little reactions on his face each time she does something new."
    JesT "I wonder if I'm actually good at this, or if blowing a guy is just easier?"
    JesT "I guess it doesn't matter. Conner's loving this, and so am I."
    "Her head begins to bob back and forth, while her tongue laps at the shaft."

    scene day5 ev08-26b with dissolve
    Con "Fuck, Jess! That feels incredible! Keep going!"
    JesT "Gladly."
    "Jessica begins to rapidly roll her head back and forth, eager to see him cum."

    scene day5 ev08-27
    Con "Oh, baby. Baby, I'm about to cum!"
    stop voices fadeout 2
    "Jessica pulls his cock from her mouth with an audible pop and begins to rapidly stroke it up and down."
    Jes "Do it, baby. Gimme all that cum. Cum all over my face!"
    "Seconds later, Conner's eyes close as his cock twitches in Jessica's hand. His cum flies out, splashing directly onto her face."
    "She opens her mouth wide as his seed splashes down, moans leaving her throat as she savor the feeling of Conner's warm seed painting her skin."
    Jes "Oh, yeah! That feels so nice!"

    jump day05end

label day05headWithAudience:

    scene day5 ev08-30a
    "Heather leans back, as if settling in for the show."
    Heath "Sure. I'd love to."
    "Jessica humms happily and slides onto Conner's lap. His hands instinctively lift to her waist while she straddles him."
    Con "You're serious?"

    scene day5 ev08-30b
    Jes "Yeah. I think it'll be hot having her watching, don't you think?"
    "Conner says nothing, simply staring and lightly shaking his head in disbelief."
    "Taking his silence has a yes, Jessica leans in and kisses him."

    scene day5 ev08-31
    "She chuckles, feeling his erection against her sex, and begins speaking to him softly."
    Jes "Well, you seemed to enjoy all that sex talk. If that big boy in your pants is any indication, it seems like you're still enjoying it."
    "Conner smiles."
    Con "What can I say? You get me going, Jess."
    Jes "I think we should see what he's learned, don't you, Heather?"
    Heath "Definitely."

    if "d05wearMine" in choices:
        scene day5 ev08-32b
    else:
        scene day5 ev08-32a
    "Conner grins, pulling Jessica into his embrace."
    "The pair begin kissing passionately, moaning and grinding together."
    "It lasts but a moment, Jessica eager to begin."
    Jes "Take my dress off, baby."
    "Conner swiftly grabs her dress and begins to pull it up and over her head."
    "His hands briefly paw at her body, squeezing her bosoms and drawing a pleasure-filled moan from her lips."
    Jes "Mmm."

    if "d05wearMine" in choices:
        scene day5 ev08-33b
    else:
        scene day5 ev08-33a
    "After a few seconds of being pleasantly groped, Jessica rises and turns around."
    "Her fingers hook into her panties, slowly pulling them while waving her hips, giving Conner a show."

    if "d05wearMine" in choices:
        JesT "Oh shit! I'm still wearing Heather's undies. God, I feel so dirty! I'm such a filthy girl."
        "Jessica's heart pounds away in her chest, but Conner says nothing."

    if "d05wearMine" in choices:
        scene day5 ev08-34b
    else:
        scene day5 ev08-34a
    "Standing and turning to face him once more, Jessica holds the panties in front of Conner's face."
    "She giggles, swinging them back and forth for a moment before tossing them forward."
    Jes "Here you go, baby."

    if "d05wearMine" in choices:
        scene day5 ev08-35b
    else:
        scene day5 ev08-35a
    "Conner grins, grabbing the lacy garment and pulling it to his nose."
    Con "Mmm, you smell incredibly baby."

    if "d05wearMine" in choices:
        "Jessica holds back a gasp of shock, Heather doing likewise."
        JesT "Oh my god! This is so wrong! He's smelling both of us!"

        scene day5 ev08-36
        "After a few seconds, Jessica pulls the panties back before tossing them to Heather."
        "Conner leans in to kiss Jessica's body while the ladies share a conspiratorial look."
        Jes "Hold onto ‘my' panties, would you, sweetie?"
        Heath "Absolutely, Jess."
        "Both ladies hold back a grin, fighting not to laugh at their secret little joke."

    scene day5 ev08-37
    "Jessica takes a seat on the couch, smiling at Conner. He moves over to her slowly, pushing her legs apart before taking his place between them."
    "Jessica licks her lips, heart pounding away in her chest."

    if "d03lickLie" in choices:
        scene day5 ev08-37b
        "Unexpectedly, however, Conner quickly dives in, shoving his tongue into Jessica."
        "She gasps, grabbing his face and pulling him up."
        Heath "Way too aggressive, Conner."
        Jes "Baby, let's try going with what Heather suggested. Try taking your time."
        "Conner nods, though he seems a little irritated, particularly by Heather's comment."
        Con "Okay."
        JesT "I've created a monster. Lesson learned."

    if "d05wearMine" in choices:
        scene day5 ev08-38b
    else:
        scene day5 ev08-38a
    "With a sigh, Conner runs his fingers over the inside of Jessica's thigh, gently caressing her supple flesh."
    "Jessica moans, smiling when he moves to kiss her leg, slowly moving up toward her eager sex."
    JesT "Oh wow. This is already better. Thank you, Heather!"
    "To the side, Heather watches with fascination."

    scene day5 ev08-39
    "Conner chuckles, moving in to kiss her labia, but only brushing her with his lips before pulling away. Instead, he begins kissing around it instead, as well as moving back to her inner thigh."
    JesT "Oh! Conner, you tease!"
    "Jessica giggles, her gaze finding Heather's own while Conner's tongue does its work."
    "She reaches down to take his head and pull him toward her, but to her surprise, he grabs both her hands, holding them down as he moves in closer."

    scene day5 ev08-40
    JesT "Okay, this is nice, but I'm already getting impatient. I need to feel him on me!"
    Jes "Oh Conner, please! Stop teasing and lick me!"
    Con "Well, Heather did say to tease a little."
    Jes "Yeah, tease, not torture."
    "Conner laughs with a grin, Heather likewise smiling."
    "Conner then moves in, giving her clit a light flick of his tongue."
    play voices x_moaning_1 loop
    "Jessica releases a shuddering breath."
    Jes "Oh shit!"

    if "d05wearMine" in choices:
        scene day5 ev08-41b
    else:
        scene day5 ev08-41a
    "After a few more teasing licks, Conner releases her hands and starts sucking gently at her clit."
    Jes "Try going from tip to tip, from my pussy to my clit, with just the tip of your tongue."
    "Conner nods, beginning to slowly lick upward."

    if "d03dinnerLick" in choices:
        "Unlike before, his light and patient touch begins to drive Jessica absolutely wild."

    Jes "Oh my god! Oh my god!"
    "As he kisses her clit, more lightly than before, she squeals in delight, her breath coming fast and heavy."
    "With her eyes locked on the amorous couple, Heather leans back against the couch, pulling up her dress."
    "Her fingers begin to gently caress her sex through her panties."
    Heath "You two are so hot!"

    if "d05wearMine" in choices:
        scene day5 ev08-42b
        "Seeing Heather spreading her legs to reveal the borrowed panties, Jessica smiles and reaches over to touch her."
        JesT "That is so hot, seeing her stroking herself with my panties on. I'm glad I can share this with her."
        "Jessica licks her lips while staring at Heather, her twinkling eyes speaking the words of sapphic lust her words cannot."

    else:
        scene day5 ev08-42a
        "Seeing Heather spreading her legs to reveal her soaking panties, Jessica smiles."
        JesT "Oh god, she's going to play with herself while she watches us! This is so incredibly hot!"

    "Conner's thumb soon moves over her clit, gently rubbing up and down while his tongue probes just inside her pussy."
    Jes "Oh god! Oh god!"
    "Jessica can feel her orgasm building, approaching quickly."

    if "d03dinnerLick" in choices:
        JesT "This is nothing like last time. Oh god, he's so good!"
    else:
        JesT "This is incredible! I wish we'd done this sooner!"

    if "d05wearMine" in choices:
        scene day5 ev08-45ani-0b
    else:
        scene day5 ev08-45ani-0a
    "Jessica's gaze returns to Conner, her mouth opening as she feels her climax arriving."
    Jes "I'm gonna cum! I'm gonna cum!"

    if "d05wearMine" in choices:
        show d05ev08-45anib
    else:
        show d05ev08-45ania
    "While Jessica's climax comes closer and closer, Heather's hand rapidly slips into her panties."
    "Her breathing grows heavier as she rubs her own moist sex, and her lips part to allow a long sigh to escape."
    "The sight of Heather masturbating out of the corner of her eye is more than Jessica can take, and pleasure soon begins to fill her sex."
    if "d05wearMine" in choices:
        hide d05ev08-45anib
    else:
        hide d05ev08-45ania
    Jes "AH! I'm cumming! I'm cumming!"
    stop voices fadeout 1
    play voices x_moaning_2

    if "d05wearMine" in choices:
        scene day5 ev08-46b
    else:
        scene day5 ev08-46a
    "With a cry of joy, her orgasm begins, her sex quivering in delight."
    "Pleasure fills her body, wave after wave of ecstasy washing over her."
    "Heather's hand slips into her panties, furiously stroking her clit, her breath coming quick."
    "Conner keeps going the entire time, his tongue never stopping."
    JesT "Oh my god, Conner! Thank you so much for being a quick study!"
    stop voices fadeout 1

    if "d03dinnerLick" in choices:
        JesT "That is SO much better than last time."

    if "d05wearMine" in choices:
        scene day5 ev08-47b
    else:
        scene day5 ev08-47a
    "Jessica takes a moment to catch her breath and gather her strength."
    Jes "Wow. Baby, that was amazing."
    Heath "Oh, it really was."
    "Jessica sees that Heather is still slowly masturbating, having caught Conner's attention."
    JesT "I can't blame him for staring. She's gorgeous."
    JesT "She's already getting me going again, and clearly Conner's ready to go."
    JesT "That was great, but I think we both need something more."
    JesT "Let's continue the show."

    if "d05wearMine" in choices:
        scene day5 ev08-49b
    else:
        scene day5 ev08-49a
    Jes "Hey there. It looks like you're getting distracted."
    Con "Can you blame me? Our neighbor is masturbating right there."
    "Heather giggles, licking her lips. She never stops rubbing her clit."
    Jes "Well, then we should keep the show going. Stand up, baby."

    jump day05blowWithAudience

label day05blowWithAudience:

    if "d05wearMine" in choices:
        scene day5 ev08-50b
    else:
        scene day5 ev08-50a
    "With a nervous smile on his face, Conner stands, Jessica's hands immediately going to his waistband."
    Jes "You excited Heather? My Conner has an amazing cock!"
    Heath "Oh, I can't wait to see it."
    "Conner blushes, but Jessica is fairly certain he shoves his crotch forward ever-so-slightly, as if proudly producing his manhood."

    scene day5 ev08-51
    "Seconds later, Conner's pants are around his ankles, Jessica stroking his thick member."
    "Her eyes remain on Heather, however, teasing both her boyfriend and their guest."
    Jes "Isn't it gorgeous?"
    Heath "Conner, your cock is beautiful! Holy shit, how does Jessica even fit that thing in her mouth?!"
    "Conner gives a small smile, but remains silent, as if unsure of what to say. Jessica, however, chuckles."
    Jes "Why don't I show you?"

    if "d05wearMine" in choices:
        scene day5 ev08-52b
    else:
        scene day5 ev08-52a
    play voices x_bj_3 loop
    "Jessica leans in, her tongue gently lapping at the tip of his cock."
    "She moans, enjoying the feel and taste of his precum as it coats her tongue. Her moans are soon joined by Heather, who seems to be greatly enjoying the show."
    "Conner says nothing, just looking down at Jessica while she works at his rigid dick."

    if slut >= 13:
        JesT "God, I love the taste of his cum. I just can't get enough of it, and I definitely can't get enough of this beautiful dick!"

    "She licks faster and harder, drawing a long moan from Conner as his head falls back."
    JesT "I'm gonna make you feel as good as you made me feel, baby."

    if "d05wearMine" in choices:
        scene day5 ev08-53b
    else:
        scene day5 ev08-53a
    "She begins sliding her tongue up and down the shaft, coating his cock in her saliva."
    "Conner's heavy breathing and constant moans telling her she's already well on her way to making him explode."
    Jes "You like that, baby?"
    Con "Oh my god, yes! That feels incredible!"
    "She giggles, continuing to run her tongue up and down its length for several moments."

    if "d05wearMine" in choices:
        scene day5 ev08-54b
    else:
        scene day5 ev08-54a
    "She soon wraps her lips around the thick member, sucking firmly as she begins to bob her head back and forth."
    "Her eyes lock with Conner's, enjoying the expression of pleasure on his face."
    JesT "I love seeing him like this. It's wonderful that I can make him feel so good."
    JesT "And with Heather right there, watching, I'm feeling pretty fucking good myself."

    if "d05wearMine" in choices:
        scene day5 ev08-55b
    else:
        scene day5 ev08-55a
    "Unexpectedly, Conner reaches down and grabs the back of Jessica's head, pushing her forward while he begins to fuck her face harder."
    JesT "Umm… That's not like him."
    JesT "He usually lets me do all the work when I blow him."
    "Jessica's finding his thick cock a bit harder to take, given how deep he's shoving it down her throat."
    "She even begins to gag a little bit, but manages to find a rhythm in which to breath."

    scene day5 ev08-56
    "Conner continues to face-fuck Jessica, something he's never done before. His eyes, meanwhile, soon turn to Heather."
    JesT "Is he doing this because she's watching? Is he trying to impress her or something?"
    JesT "He's being so rough... I kind of like it."

    if "d05wearMine" in choices:
        scene day5 ev08-57b
    else:
        scene day5 ev08-57a
    "For another minute, Jessica simply sucks at the thick member in her mouth, staring up at her boyfriend while he looks at the other woman."
    "Heather continues to watch, silently, her hands moving back and forth over her sex."
    JesT "I feel kind of dirty right now, like I barely matter."
    JesT "I'm just the mouth Conner happens to be fucking."
    JesT "It's so dirty. It feels… so fucking hot!"

    scene day5 ev08-58a
    stop voices fadeout 1
    "Conner soon pulls out of her mouth, giving her a moment to breathe."
    "Saliva pours out, running down her chin and falling onto her chest."
    "Jessica takes several long breaths while she stares up at Conner."
    Jes "Jesus. That was…"
    Heath "So fucking hot! Why didn't you tell me he fucked you like this?"
    JesT "Because he never has before."
    Con "Keep going."

    scene day5 ev08-58b with dissolve
    play voices x_bj_3 loop
    "Conner shoves himself back into her mouth, ramming his cock in even harder than before."
    "He doesn't seem to care that he's pushing into her cheek, and goes on regardless."
    "Jessica continues to suck at the thick member all the while, doing her best to please him despite his rough behavior."
    JesT "I feel utterly humiliated. Having him fuck my mouth like this, right in front of Heather, it makes me feel…"
    JesT "It makes me feel like a whore. So why the fuck am I loving this so much?"

    if "d05wearMine" in choices:
        scene day5 ev08-59b
    else:
        scene day5 ev08-59a
    "Conner's own voice begins to shudder, his breath coming faster and faster, his orgasm quickly approaching."
    "His pelvis is ramming hard into Jessica's face, his cock smacking against the back of her throat."
    "Saliva pours out from her lips whenever Conner pulls back, spittle dripping down her mouth and falling onto her body."
    JesT "I think I need to have Heather over more often, if this is what Conner's gonna be like in bed."
    Con "Shit! I'm gonna cum!"

    if "d05wearMine" in choices:
        scene day5 ev08-60b
    else:
        scene day5 ev08-60a
    "Despite being prepared, Jessica finds herself gagging when Conner shoves his cock back into her mouth as far as he can manage."
    "The organ begins twitching inside, spraying its load down Jessica's throat, while Conner practically growls in pleasure."
    "Jess finds herself unable to breathe, having quite a bit of trouble swallowing every drop of cum splashing into her mouth."
    "Heather, on the other hand, finds herself driven wild by the display, and with a cry of pleasure finally cums, her hand continuing to rapidly rub across her sex all the while."
    JesT "Conner, finish up! Please, I can't breathe."

    scene day5 ev08-61
    "Jessica taps her hand on Conner's thigh, and he seems to get the idea."
    "He pulls his cock from within her mouth, allowing Jessica some breathing room."
    stop voices fadeout 2
    "Cum sprays all over her, the last spurts of Conner's dick weakly dripping out."
    "She coughs a few times, trying to clear her throat, little droplets of Conner's seed falling from her lips and onto her breasts."
    Con "Holy shit!"
    Heath "Wow."
    "Everyone's breathing is heavy, particularly Jessica, who spends several seconds catching her breath."

    if "d05wearMine" in choices:
        scene day5 ev08-61c
    else:
        scene day5 ev08-61b
    Jes "Definitely wow. I mean, geez, Conner."
    "She flashes him a little smile, then takes the tip of his cock back in her mouth, gladly sucking up more of the seed from his filthy dick."
    JesT "Hehe. That was fun, in a weird, incredibly dirty sort of way."
    Heath "That was so fucking hot! Who knew you kids could be so naughty?"
    Heath "Or that beautiful cock could cum so much?"
    "Conner recoiles slightly, as if suddenly realizing Heather in still there and what he'd just done in front of her."
    "He blushes visibly and coughs."
    Con "Hehe. Right. I, um, I should get cleaned up."
    "Conner quickly heads off, closing the bedroom door behind him."
    Heath "Well, Jessica, thank you so much for having me over. This has been wonderful."

    if "d05heatherFinger" in choices:
        scene day5 ev08-62
        "Heather scoots closer, pulling Jessica's face to her own."
        Heath "Come here. I want a taste before I go."
        "Their lips come together, both ladies moaning softly as they kiss."
        "Their tongues dance together, swapping Conner's seed back and forth. Heather's lips suck at Jessica's, grabbing up what cum she can and eagerly swallowing it."
        Heath "Mmm. He tastes nice. I bet you just love blowing that cock."
        Jes "I do, and I like having someone to share it with."
        "Heather giggles, continuing to kiss Jessica until she'd cleaned the remaining cum from her face."
        Heath "Mmm, that was sweet."
        Heath "Okay, I'm gonna head home, take a shower. Think about you while I masturbate furiously."
        "Jessica laughs."
        Jes "Thank you so much for coming tonight."
        Heath "Sweetie, I'll cum for you anytime you want."
        "With another kiss, Heather stands and heads out."

    else:
        Heath "I'm gonna head home, take a shower. Maybe think about you two while I fall asleep."
        Jes "Thanks for coming over, Heather. Tonight was incredible!"
        Heath "My pleasure. Have a good night, sweetie."

    jump day05end

label day05womansTouch:

    $ relHeather += 1

    scene day5 ev08-30a
    "Jessica rolls her body onto Conner, fixing him with a seductive smile."
    "She chuckles, feeling his erection against her sex, and begins speaking to him softly."
    Jes "So, remember that talk we had the other night?"
    "Conner's eyes briefly move over to Heather."
    Con "You mean the one about having someone else…?"
    "Jessica grins and nods."
    Jes "Mmm-hmm. That's the one."
    "Again, Conner glances over to Heather, who's smiling back from her side of the couch."

    scene day5 ev08-31
    "He begins to stutter, trying to find words, but is cut off when Jessica leans forward to kiss him."
    "When she moves away, he just blinks at her."
    Con "When- I didn't- think you were serious, and I didn't think you'd bring over Heather."
    Jes "I'm serious, baby. It'll be fun. Trust me."
    "He says nothing, just looking back at Heather."
    Jes "Take off my dress, baby."

    scene day5 ev08-32a
    "Conner reaches up and pulls her dress away, his eyes quickly taking Jessica's luscious body."
    JesT "There we go. Just concentrate on me, baby."
    "Conner's reticence seemed to fade away slightly, his attention caught my Jessica's nudity."

    scene day5 ev08-33a
    "Jessica stands up and turns, bending over as she pulls down her panties."
    "She smiles, chuckling, and waves her behind at Conner while she strips."
    JesT "This is so hot! Having two people watch me undress just feels incredible! My heart feels like it wants to jump out of my chest!"

    scene day5 ev08-34a
    "Standing and turning to face him once more, Jessica holds the panties in front of Conner's face."
    "She giggles, swinging them back and forth for a moment before tossing them forward."
    Jes "Here you go, baby."

    scene day5 ev08-35a
    "Conner grins, grabbing the lacy garment and pulling it to his nose."
    Con "Mmm, you smell incredibly baby."
    "Heather licks her lips, holding back a grin."

    scene day5 ev08-65
    "Jessica takes a seat between Conner and Heather, spreading her legs wide."
    "She gives Conner a wry smile, wondering just how he's going to react to what she has in mind."
    "Her gaze remains on Conner as she licks her lips and speaks to Heather."
    Jes "I'm ready, honey."
    Heath "It's about time."

    scene day5 ev08-66
    "Heather kneels down between Jessica's legs, her fingers gingerly caressing Jessica's thigh."
    Heath "First thing's first, sweetie. Start slowly, teasing and caressing her."

    scene day5 ev08-67
    "Heather begins kissing Jessica, starting on her inner thigh and moving in toward her sex."
    "Jessica moans in ecstasy, savoring the feeling of Heather's lips against her body."
    "Heather's warm breath blows gently over Jessica's sopping and eager sex, causing her to quiver in anticipation."
    Heath "Don't rush it. Let her pleasure build."
    "She returns to kissing and licking the edges of Jessica's labia. Jessica's breath becomes quicker and quicker, her pussy becoming wetter with each passing second."
    play voices x_moaning_1 loop

    scene day5 ev08-68
    "With a giggle, Heather plants a small, playful kiss on Jessica's lips. Her hand comes up, her thumb lightly rubbing at Jessica's clit."
    Heath "Focus your attention on her clit, but not too roughly. It takes very little pressure to stimulate the clitoris."
    Heath "And if she doesn't like it, try just flicking it instead of constantly rubbing it."
    JesT "Oh, I'm loving it! Holy shit!"
    "Jessica begins moaning a little louder, mouth falling open as gasps escape her lips."

    scene day5 ev08-69
    "Heather begins licking Jessica in earnest, her tongue lightly but rapidly flicking at the puffy little ball."
    Heath "Pay attention to how she reacts. Her body language will tell you if you're doing well."
    "A small whine leaves Jessica's lips. Her arousal spikes when she hears Heather speaking to Conner, while never moving her lips from Jessica's soaking pussy."
    JesT "Oh, you are doing everything right, Heather!"

    scene day5 ev08-70
    "Heather settles into a rhythm, her nose rubbing gently into Jessica's pubic hair."
    JesT "Hehe. That tickles."
    "Both ladies share a small chuckle, but Heather keeps going, drawing a long moan from Jessica."
    JesT "Oh god! So this is what it feels like when someone who knows what they're doing goes down on you."

    scene day5 ev08-71
    "Jessica closes her eyes, her fingers gently threading through Heather's hair and lightly massaging her head."
    "Conner leans in, his hand running along her thigh, and sending a tingle of delight up her body."
    JesT "God, this feels incredible! Having two people pleasing me at once makes me want to cum now!"

    scene day5 ev08-72
    stop voices fadeout 1
    play voices x_moaning_2
    "The seconds fly by, Jessica existing in a world of utter joy and bliss. Heather's tongue does its job, and she feels herself about to cum."
    "Just as her climax begins, she pulls Conner close and plants her lips against his in a rough, passionate kiss."
    "Her hips buck and shake, pleasure filling her pussy. Muffled whines spill from her mouth, mixing with the wet smacking of she and Conner's kiss."
    stop voices fadeout 2

    scene day5 ev08-73
    "Though her orgasm soon subsides, she continues to kiss Conner, holding their embrace for several seconds longer."
    "Heather tries to stand, only to find herself held in place by Jessica's grasp."
    JesT "Oh my god. That was incredible. This was the best damn idea I've had in a while."
    JesT "Heather was amazing. Her tongue is a gift, and I feel blessed to have received it."
    JesT "Heather deserves a reward after how wonderful she made me feel, and I want to kiss her so badly."

    menu:
        "Kiss her":
            $ choices.append("d053some")
            $ relCon += 1
            $ relHeather += 1
            $ slut += 1
            $ blowjob += 1
            $ sex += 1
            JesT "I need her lips, right now!"

            jump day053some

        "Just thank her":
            JesT "Yeah, I don't think I want to take this that far."

            scene day5 ev08-74
            "Jessica grins at Heather."
            Jes "Thank you so much, Heather. That was amazing."
            "Heather returns the smile, noting Jessica and Conner snuggling together on the couch."
            Heath "I'm glad you liked it, sweetie, and I hope you remember what I said, Conner."
            "He laughs."
            Con "Definitely."
            Heath "Alright. Well, I'm going to go home and, uh, \"relieve some tension\". You kids have a good night."
            Con "Have fun!"
            Jes "Thanks again, Heather! You're amazing!"

            scene day5 ev08-75
            "Heather rises and heads out. After the door closes, Jessica and Conner share a passionate kiss."
            JesT "That was a lot of fun. I'm exhausted, but I kind of want to keep this going."

            menu:
                "Blow him":
                    $ choices.append("d05bjSolo")
                    $ relCon += 1
                    $ blowjob += 1

                    JesT "What the hell. I'll make sure Conner has some fun tonight too."

                    jump day05blowNoAudience

                "Go to sleep":
                    $ relCon -= 1
                    JesT "I can barely keep my eyes open at this point. I think I just want to fall asleep."
                    Jes "I'm exhausted, baby. We should head to bed."
                    "Conner's smile fades, his disappointment clear."
                    Con "You sure?"
                    Jes "Yeah. I just want to curl up with you now."
                    Con "Alright, babe.. Let's go to bed."

                    jump day05end

label day053some:

    scene day5 ev08-76
    "With a smile, Jessica pulls Heather up and kisses her, a sweet, sapphic reward for her gift of pleasure."
    "The kiss goes on for several seconds, Jessica keeping Conner close all the while."
    JesT "I really never thought I'd be in this position, but I'm loving having two beautiful lovers at once."

    scene day5 ev08-77a
    "Jessica pulls away from the kiss, turning her gaze to Conner."
    Jes "Isn't she wonderful, baby? Don't you think she deserves a reward for such a great lesson?"
    "Once again, Conner turns his attention from one woman to the other. He seems uncertain, as if any moment they'll both laugh and tell him it was all a joke."
    Heath "I wouldn't mind a reward."
    "Again, Conner turns to Heather, a massive grin on her face. When he looks back to Jessica, she simply nods."

    scene day5 ev08-77b
    "Leaning forward despite his trepidation, Conner plants his lips against Heather's."
    "Heather moans in satisfaction, seeming to savor all the attention she's receiving."
    "Jessica watches with fascination, feeling her loins stirring once again."
    Jes "Oh, wow. This is… so hot. I can't believe how much I'm enjoying the sight of my boyfriend kissing another woman."

    scene day5 ev08-78
    "Heather continues to kiss Conner for several seconds before pushing him away. She smiles at Jessica, moaning happily."
    "She begins to push Conner back onto the couch."
    Heath "He's been a good student, don't you think, Jessica? And a good teacher sees to her students first."

    scene day5 ev08-79
    "Both Jessica and Heather move between Conner's legs as he spreads them wide."
    "They come together to kiss once more, Jessica savoring the naughty sensation of kissing another woman in front of her boyfriend."
    "Their hands soon drift over Conner's crotch, softly rubbing his erection through the fabric."

    scene day5 ev08-79b
    "The ladies share a conspiratorial smile and a giggle as Jessica begins pulling his pants down."
    JesT "And if Conner still had any trepidation remaining, I'm guessing it's all gone now."
    "Jessica's other hand reaches down to squeeze Heather's ass."
    JesT "It feels so wrong groping my neighbor and my boyfriend at once, but fuck it! I'm loving it, and I'm pretty sure Heather is too!"

    scene day5 ev08-80
    "Both Heather and Jessica take Conner's thick member in their hands, slowly stroking up and down."
    Heath "Mmm, you're so big, Conner! How the hell does Jessica take this thing?"
    Jes "Screaming in pleasure, that's how."
    "Again the ladies laughed, enjoying themselves immensely while Conner moans in ecstasy."

    scene day5 ev08-81
    "The pair lean forward, planting their lips against Conner's erect manhood. Slowly and tenderly, they begin kissing and licking his warm flesh."
    play voices x_bj_3
    "Conner gasps, overwhelmed by the unbelievable sight in front of his eyes."
    Con "Holy shit!"
    "Heather grins, her lips brushing against Jessica's. Their tongues continue to touch briefly every few seconds as they lap at the warm, rigid cock."

    scene day5 ev08-82
    "Heather pulls the head of the cock into her mouth while Jessica sucks at the shaft, her hand gently stroking and squeezing at the base."
    "She pulls Heather closer, wanting to feel the other woman's lips and face touching her own."
    JesT "Mmm. This is even better than when I blow him alone. Sharing his dick with another woman is incredibly erotic."

    if persistent.pov == 1:
        scene day5 ev08-83mpov
    else:
        scene day5 ev08-83
    "The ladies switch positions, Jessica sucking at the head while Heather laps at the shaft."
    "Heather begins sliding herself back and forth, moving her head to the side so she could kiss the entire length, pushing Jessica's hand aside as she does."
    JesT "That's not a bad idea. I'll have to try that next time."
    "For the moment, though, Jessica is perfectly content to feel Heather's tongue touch her own again and again, a gentle caress that nonetheless drives her insane."

    scene day5 ev08-83b
    "Conner's eyes close, constant moans leaving his mouth."
    Con "Fuck, that feels good."
    "Jessica chuckles, her hand moving back to squeeze Heather's ass, the ladies engaging in their own little coupling while they blow Conner."
    JesT "Her ass is like no other! I kind of want to lick it."
    "Jessica smiles around the cock between her lips, inspiration firing up her desperately horny mind."

    scene day5 ev08-84
    stop voices fadeout 1
    "Before Conner can become too excited, Jessica pulls away, her hand leaving Conner's cock."
    Con "Huh?"
    "Jessica leans into Heather, planting another kiss on Heather's lips before patting the couch."
    Jes "Why don't you lie down, Heather? I want to taste you this time."

    scene day5 ev08-85
    "Heather grins and immediately moves onto the cushion, spreading her legs wide. Jessica quickly moves into position, savoring the sight."
    JesT "She's so pretty. Even her pussy is gorgeous."
    JesT "Christian's a lucky man, but tonight, so are Conner and I."
    "Before she can do anything, though, Conner moves behind her, his intention clear."
    JesT "Well, he's not shy about this anymore."

    scene day5 ev08-86ani-00
    "Jessica bends down, tongue probing out to tease Heather's sopping womanhood while Conner grips her hips and shoves himself inside."
    play voices x_sex_2 fadein 1 loop
    JesT "Oh fuck, that feels good!"

    show d05ev08-86ani
    "Jessica begins gently bouncing forward and back while Conner's cock fills her again and again."
    "She keeps her mouth pressed into Heather's cunt, licking and kissing at the other woman's pussy while she's being fucked."
    Heath "Just like that, sweetie. Oh, you're so good, Jess."
    "Small whines are slipping from Jessica's lips, muffled by Heather's pussy. Heather smiles down at her, apparently aroused by the sound of it."
    hide d05ev08-86ani
    JesT "This is… too much. I'm eating pussy while I'm being fucked. This is the craziest thing I've ever done… and it feels incredible!"

    scene day5 ev08-87
    stop voices fadeout 2
    JesT "I want more, though. As amazing as it is, I want to feel Conner fucking another woman!"
    "Moving toward Heather, Conner's dick sliding from inside her, she plants a kiss on Heather's breast before embracing her in a passionate kiss."

    scene day5 ev08-88
    "Almost immediately, she reaches back and grips Conner's wet cock."
    "She pulls lightly, Conner allowing her to lead his dick as she aims it directly toward Heather's cunt."

    scene day5 ev08-89
    "Conner soon pushes himself inside Heather, though his attention remains on Jessica.."
    play voices x_sex_3 fadein 1 loop
    "She pushes down on Heather's shoulder while they're both rocked forward by Conner's thrusts."
    "As Conner begins to fuck her in earnest, he pulls Jessica and his body closer together."

    scene day5 ev08-89b
    "Conner soon groans, savoring the sensation of another woman around his cock."
    "He reaches around Jessica, squeezing her bosom."
    "Jessica moans, and opens her eyes to see Heather staring up at her."
    Jes "How's that feel, baby?"
    Heath "Oh, Conner's cock is magic, Jess! No wonder you love having this inside you!"

    scene day5 ev08-90
    "While the three of them gyrate and roll about together, Heather's fingers come up to rub Jessica's pussy."

    if "d01naughtyVibe" in choices:
        JesT "This is almost exactly like it was in my fantasy! It's so good!"

    "All gentility and patience is gone, Heather's fingers now rapidly rubbing at Jessica's clit. Jessica's cries of ecstasy grow as she's fingered by both her lovers."

    scene day5 ev08-90ani-00
    JesT "Yes! Oh fuck, keep going! Finger my cunt!"

    show d05ev08-90ani
    "While the ladies make out, Conner continues to thrust himself into Heather."
    Con "Ah, yeah. Keep going, ladies. That's so hot!"
    JesT "It's so fucking is!"
    "Both Heather and Jessica are moaning incessantly, Heather herself beginning to whine as pleasure fills her pussy."
    JesT "Enjoy my boyfriend's dick, Heather! I want to hear you cum while he fucks you!"
    hide d05ev08-90ani
    Heath "Mmm..."

    scene day5 ev08-91
    play voices x_sex_4 fadein 1 loop
    "Their orgasms come on rapidly and without warning. Each woman cries into the other's mouth, their kiss continuing as they bodies twitch and buck."
    JesT "Oh god! Oh god!"
    "Jessica's mind goes blank, her thoughts lost in a sea of complete and utter sexual bliss quite unlike any she'd yet visited."

    scene day5 ev08-92
    "The sight of the two women cumming is enough to send Conner over the edge."
    play voices x_sex_5 fadein 1 loop
    "He pulls out from Heather, pressing his cock in between them both as it too begins to twitch, sending his warm semen flying out."
    "It splashes onto Heather's stomach, spraying long white ropes over her beautiful skin."
    "Jessica pulls out of their kiss, still squealing in delight, and stares at the jumping cock covering her sapphic lover in its juices."
    JesT "Wow. That's incredible. It almost looks like it's my cock covering her in cum. Beautiful."
    stop voices fadeout 1

    scene day5 ev08-93
    "Soon, the three come down from their orgasmic bliss."
    "Jessica and Conner collapse onto the couch, Heather sidling up to Jessica. Each of them are exhausted, covered head to toe in sweat."
    "Heather slowly strokes Jessica's face, their wet, warm bodies pressed together."
    JesT "Oh my god, that was incredible! I never thought I'd be so happy to fuck another woman."
    "Heather leans forward, planting a small kiss on Jessica's cheek."
    Heath "This was a wonderful threesome, you two, but I need to go get some rest."
    Con "Have you had one before?"
    "Heather laughs."
    Heath "Thanks, Conner. Tonight was a blast. You too, Jessica. I'm glad we could spend this time together."
    "Jessica's heart beats, her eyes glued to Heather's beautiful face."
    JesT "I don't want her to leave. I want her to stay and sleep with us… then maybe fuck us again in the morning."
    JesT "Then again, maybe that's best. It's been a long day."
    Jes "Have a great night, Heather. Thank you so much."
    "Heather rises and blows them a kiss, then after quickly dresses and heads home."

    scene day5 ev08-94
    "Once Heather's gone, Jessica leans over and kisses Conner, making it long, slow, and loving."
    Jes "That was amazing, Conner."
    Con "Holy shit, it was. Thank you so much for inviting her over."
    "Jessica chuckles and pats his chest."
    Jes "Let's go to bed. My legs are like wet noodles now."

    jump day05end

label day05end:

    scene day5 ev08-99 with fade
    "After brushing her teeth, Jessica climbs into bed."
    "She turns to Conner, planting a kiss on his cheek."
    Jes "Long day?"
    Con "Mmm."
    "Her brow furrows."
    Jes "Something wrong?"
    Con "Hmm?"
    Jes "You seem like you're far away. Are you okay?"
    Con "Oh, I'm just thinking about some stuff from work. Nothing serious."

    if "d05heatherWatch" in choices:
        Jes "Well baby, tonight was amazing. I've never seen you like that before!"
        Con "Yeah, I'm sorry. I don't know what came over me."
        Jes "Don't be sorry. I loved it."
        Jes "I might need to have Heather over more often if that's how you'll act."
        Con "Really?"
        Jes "Hmm… maybe."

        scene day5 ev08-99b with dissolve
        "Jessica rolls over onto her side, leaving the matter unsettled."
        Con "You teasing slut."
        "She laughs."
        Jes "That's the spirit, sweetie."

        jump day06

    "After a short while, Conner curls up and drifts away. Jessica lays at his side, watching him sleep."

    if "d053some" in choices:
        JesT "That was so hot, and so damn exciting! I wouldn't be opposed to having another threesome at some point."

    JesT "Well, this was an interesting day."

    if "d05noConner" in choices:
        JesT "I still can't believe what Heather and I are doing."
        JesT "I feel wrong sneaking around on Conner like this, but I just can't stay away from her."
        JesT "Oh, that reminds me. I need to give her back her panties tomorrow."
        "With a smile, Jessica settles down, already dreaming of her next encounter with her gorgeous redheaded neighbor."

    "With a smile, Jessica settles down and drifts to sleep."

    jump day06
