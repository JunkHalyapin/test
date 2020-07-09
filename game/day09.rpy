label day09:

    scene day9 with fade
    "DAY 9"

    scene day9 ev01-01 with fade
    Jes "Mmm, Mr. Hammond, I want some ice-cream too."
    Jes "Hmm? Oh."
    "Jessica yawns, but stops herself from stretching since it seems like Conner's still sleeping."
    JesT "He must be pretty tired. He was out late, after all."
    JesT "Might as well let him sleep."
    JesT "I'd wait for him to wake up, but I've gotta get moving."

    scene day9 ev01-03 with fade
    play sound sink_water_1 loop
    "Jessica starts getting ready for her jog with Heather, going through her morning routine."
    "Her thoughts turn to her pending visit with her old high school."
    JesT "It's gonna be weird to see the old alma mater."
    JesT "I wonder how much has changed."
    JesT "I wonder if Principal Sheers is still in charge."
    stop sound fadeout 1

    scene day9 ev01-04 with fade
    "After getting dressed, Jessica heads over to the bed."
    Jes "Hey, sweetie?"
    Con "Mmm. Mmm?"
    Jes "I'm going on a run with Heather."
    Con "‘Kay."
    Jes "You should get up or you'll be late."
    Con "Nah, I have the morning free. Gonna sleep."
    "Jessica nods to herself, then heads out."

    scene day9 ev01-05 with fade
    play sound neighborhood_1 fadein 1 loop
    "Jessica steps outside, the weather sunny, but cool."
    "Heather is already out stretching."
    Heath "Hey, sweetie."
    Jes "Hey, Heather. You're looking wonderful today."

    if "d07firstLesbian" in choices:
        JesT "She's always beautiful. Small wonder she has such a hold on me."

    scene day9 ev01-06
    Heath "Why, thank you. Shall we get going?"
    Jes "Sure thing."
    Heath "By the way, I hope Christian didn't bother you with his behavior last night."
    Jes "It's no problem. I'm a big girl."

    scene day9 ev01-07
    "The two start their jog, chatting casually as they go."
    "Their conversation quickly turns to work."
    Heath "So, how are things going at your job?"
    Jes "Pretty good, actually. I visited the mayor's office yesterday."
    Heath "Again? Ooh. You two are getting close."
    Heath "Are you sleeping with him?"
    Jes "Heather!"
    Heath "What? It was an honest question."
    Jes "No, I'm not sleeping with him. Why would even think that?"
    Heath "You know. Man with power, a penchant for affairs with beautiful women, and you've met him twice."
    Heath "Just curious if you're… pumping him for information."
    stop sound fadeout 1

    scene day9 ev01-08
    play sound park_1 fadein 1 loop
    "Jessica shakes her head and laughs."
    Jes "No. I'm not pumping him… for information or anything else."

    if "d04mayorTease" or "d08mayorTease" in choices:
        JesT "Not that I haven't been having a little fun with him."
    else:
        JesT "Not that he hasn't glanced my way."

    Jes "We've just been discussing city affairs. I'm trying to establish a working relationship with city hall."
    Heath "Yeah, I'll bet you are."
    Jes "Oh my god, you're so bad!"

    scene day9 ev01-09
    Heath "I know he wants to fuck you."
    Jes "Yeah, probably, but that's not going to happen."
    Heath "You could always let on that you'll consider it. If a woman can profit from a man thinking with his dick, we can often get ahead in life."
    Jes "Are you saying I should have an affair?"
    Heath "Not necessarily, but it doesn't hurt to lead him on a little. Men can be very cooperative if they think they can get into your panties."
    Heath "You just have to leave the door open, so to speak."
    Jes "So I should encourage him?"
    Heath "Just don't cut him off completely. And if you can wiggle your tail his way, all the better."
    Jes "Have you done this?"
    Heath "Of course. My boss was all over me when I first started, and I was happy to let him think I was available."
    Heath "For the first few months we were pretty close. I even let him get a little touchy."
    "Jessica finds herself breathing just a bit faster, wondering what happened next."
    Heath "And by the time things went too far and I had to cut him off, I had connections and clients of my own, cases I was involved with. He couldn't just fire me anymore."
    Jes "So just teasing and flirting? No sex?"
    Heath "Mmm-hmm. I mean, it's up to you to decide. Sex in the workplace is complicated, after all. Just make sure you have some leverage of your own, in case you need to put a stop to it."
    stop sound fadeout 1

    scene day9 ev01-15 with fade
    play sound neighborhood_1 fadein 1 loop
    "The conversation moves away from sex and more toward Heather's own projects."
    JesT "Huh. I think we're getting close to Mr. Parker's newsstand."
    JesT "I should stop by real quick and see if he talked to that ex-cop friend of his."
    Jes "Would you mind if we take a quick detour? I'd like to say hi to someone I know."
    Heath "Sure. Whatever works for you."
    stop sound fadeout 1

    scene day9 ev01-16 with fade
    play sound city_ambience_5 fadein 1 loop
    "The pair arrive at Mr. Parker's newsstand, Jessica knocking before inviting herself inside."
    Jes "Hey there."
    Parker "Jessica! Hello! Come on in!"

    scene day9 ev01-17
    "Jessica gives him a hug and a kiss."
    Jes "How are you today?"
    Parker "Good. Just getting things ready."

    if "d04parkerNoApology" in choices:
        JesT "Please behave in front of Heather. We don't need to give her ideas."

    scene day9 ev01-18
    Parker "Who's your friend."
    Jes "Mr. Parker, this is Heather. Heather, Mr. Parker."
    Heath "Hello."
    Parker "A pleasure to meet you."
    Jes "Mr. Parker was one of the top journalists at the Gazette. Now he's my mentor."
    Heath "Ah, so you're Jessica's Obi-Wan?"
    Parker "Ha! Kind of."
    Heath "Didn't you write that bit on the Trail murders?"
    Parker "I did! I'm surprised you recognized my name."
    Heath "Well, I was on the defense team for one of the defendants in that case."
    Heath "So, thank you! You helped get my career started."
    "He gives her a hearty laugh."
    Parker "You're very welcome!"

    scene day9 ev01-19
    Jes "I just came by to ask if you'd had a chance to talk to your friend."
    Parker "I'm actually meeting him for a beer tonight. These things are always better face-to-face."
    Parker "You can come if you like. I'm sure he'd enjoy meeting you."
    JesT "That's not a bad idea, although it would be a little weird going out with two men."

    if "d04parkerNoApology" in choices:
        JesT "And given what I've been doing with him, that might be a little weird."
    else:
        JesT "It's just work, though. Conner would understand."

    menu:
        "Agree to accompany him":
            $ choices.append("d09dateParker")
            $ relParker += 1
            JesT "Why not? It wouldn't hurt to meet the guy. Plus, an ex-cop could be a useful contact if I need to work the precinct again."
            Jes "Sure. That'll work."
            Parker "Great! I'll come by your place and pick you up so we can go together. Around eight sound good?"
            Jes "Yeah, that's fine. I'll see you then."
            Parker "Have a nice day, ladies."

            scene day9 ev01-30a with fade
            play sound city_ambience_4 fadein 1 loop
            "Jessica and Heather start their run back, Heather chuckling once they get away from the newsstand."
            Heath "Wow, Jessica. I didn't know how much of a SLUT you were."
            Jes "Excuse me?"
            Heath "A date with two men? And one of them old enough to be your grandpa? Mmm. You must want it bad, sweetie."
            Jes "This is not a date. It's work-related."
            Heath "Oh yeah? So Obi-Wan back there isn't going to show you his lightsaber?"
            "Jessica says nothing, suddenly very self-conscious."
            Heath "Hey, I'm not judging. I just told you to use your looks. Shake your thang, girl."

            if "d04parkerNoApology" in choices:
                JesT "Well, I have kind of felt his \"lightsaber\" already."
            stop sound fadeout 1

        "Say you have plans already":
            JesT "Nah. A kind of 'date' with two men is just a little too weird for me, even if Mr. Parker's one of them."
            Jes "I'm sorry, Mr. Parker, but I already have plans for this evening."
            Parker "No worries, Jessica. I'll make sure the guy's willing to help out."
            Jes "Thank you so much."
            Jes "Alright, let's get going, Heather. Bye, Mr. Parker."
            Parker "Have a good day, ladies."

            scene day9 ev01-30b with fade
            play sound city_ambience_4 fadein 1 loop
            "Jessica and Heather start their run back, Heather chuckling once they get away from the newsstand."
            Heath "Well, that was kind of rude."
            Jes "What?"
            Heath "Cutting the old man off when he was asking for a date."
            "Jessica laughs."
            Jes "He's just a friend, Heather."
            Heath "You can do stuff with friends."

            if "d05heatherFinger" in choices:
                Heath "We do."
                "Jessica blushes, saying nothing."
            stop sound fadeout 1

    if "d05heatherFinger" in choices:
        scene day9 ev01-31b with fade
        "The two talk for a bit as they head inside, hand in hand."
        Jes "This was fun. We need to go running together more often."
        Heath "Any time I can spend with you is good."
        "Heather squeezes Jessica's hand, making Jessica smile and look down at her feet."
        Jes "Okay, I better get a shower in before I head off to work."

        scene day9 ev01-32
        "Before she can move off, Heather pushes her into the wall, bringing their lips close together."
        Jes "Heather! It's early! Someone might see."
        Heath "Mmm-hmm."
        "Heedless, Heather plants her lips against Jessica's."
        "The quiet sounds of kissing are thunderous in Jessica's ears, but she lets it go on regardless."
        JesT "This is stupid, but I just love being in her arms so much."
        "They kiss for several long moments before Heather suddenly pulls away with one last peck on Jessica's mouth."
        Heath "Okay. You have a good day, sweetie."
        "Heather heads off to her apartment, while Jessica slowly slinks into her own."

        scene day9 ev01-33 with fade
        "After a quick, and cold shower to forget about Heather, Jessica gets dressed for work."

    else:
        scene day9 ev01-31a with fade
        "The two talk for a bit as they head inside."
        Jes "Alright, I'm gonna go get a shower in before I head to work."
        Heath "Me too. Have a good one, Jess."
        Jes "You too."

        scene day9 ev01-33 with fade
        "After a quick shower, Jessica gets dressed for work."

    "She picks out a particularly lacy set of underwear, wanting to feel as sexy as possible even on a casual work day."
    "As she's attaching her garter straps, Conner stirs on the bed."
    "His eyes open, and after a moment he smiles."

    scene day9 ev01-34
    Con "Now THAT'S a sight to wake up to."
    "He starts to reach over to her leg, but she bats him away."
    Jes "Sorry, Mister. You slept too long. I've got to get to work."
    Con "Hell of an outfit for work. You have a second job I don't know about?"
    "She snorts."
    Jes "Shut up. So, how did things go last night?"
    Con "Not bad. I found my friend in a bar. Sat with him a while, then took him home."
    Jes "Was he drunk?"
    Con "Nah. He didn't fall off the wagon. Close call, though. If I hadn't gone, I don't know what would've happened."
    Jes "Glad to hear it."
    "Jessica finishes putting on her clothes. After a quick goodbye, she heads out."

    scene day9 ev01-35 with fade
    play sound vespa_start_drive fadein 1 loop
    "After checking directions one last time, she hops on her scooter and drives off, heading toward her old high school."
    JesT "This is gonna be fun! I wonder if Mrs. Prichstein is still there. God, she was such a bitch."
    JesT "I miss sitting in the lunch room and making fun of her. Man, I was a bitch back then too. Good times."
    stop sound fadeout 1

    scene day9 ev02-01 with fade
    play sound city_street_with_vespa fadein 1 loop
    "Driving up, Jessica has a huge smile on her face."
    JesT "Wow! It's exactly the same! It's like time froze!"
    JesT "Even the uniforms look exactly the same! I looked so damn cute in that little skirt!"
    stop sound fadeout 1

    scene day9 ev02-02 with fade
    "Inside, Jessica looks around with a grin."
    JesT "Mrs. Brubacher is still working here? Terrorizing students in the lobby instead of in Calculus now, I guess."
    Jes "Mrs. Brubacher?"
    Bru "Yes? Can I help you?"
    Jes "My name is Jessica O'Neil. I was a student here about eight years ago."

    scene day9 ev02-03
    Bru "I… think I remember. Weren't you on the school news team?"
    Jes "Yes. For my junior and senior years."
    Bru "Of course. How are you, Ms. O'Neil? You've really grown up, haven't you?"
    Jes "Well, thank you."
    Bru "What brings you by today?"
    Jes "I'm actually working for the New Port Gazette. I have an appointment with the principal today."
    Bru "Of course. Head on over. You remember where it is?"
    "Jessica chuckles."
    Jes "Uh, sadly. I got called there a few times."
    "The pair share a laugh before Jessica heads down the hall."

    scene day9 ev02-04 with fade
    "The door is open when she arrives, so Jessica leans in and knocks."
    Pri "Yes?"
    Jes "Principal Sheers? I'm Jessica O'Neil with the New Port Gazette. I have an appointment."
    "The man gives her a warm smile and motions her inside."
    Pri "Of course! Please, come in. Go ahead and close the door, if you wouldn't mind. The students can get loud."
    "Seeing him again after so long brings back pleasant memories to Jessica."
    JesT "I used to have such a huge crush on him. I always did have a thing for authority figures."

    scene day9 ev02-05
    "After closing the door, Jessica strides over to the desk, shaking his hand."
    Pri "Jessica O'Neil. Did you use to go here?"
    Jes "Yeah! I was class of 2010."
    if persistent.pov == 1:
        scene day9 ev02-05mpov
    Pri "Ha! When I saw your face, I thought you looked so familiar."
    Jes "Well, I did appear on school news every morning."

    scene day9 ev02-06
    "Principal Sheers motions toward the chair, and she takes a seat, placing her purse down beside it."
    Pri "You've gone far since your days in the school news room. A reporter for a major newspaper. That's impressive."
    Jes "Thank you. It's a long way from making school announcements, but I kind of miss the old days."
    Jes "Lots of kids who didn't know a damn thing all trying to act like reporters."
    Pri "You and your team were good at it. You won quite a few awards, if I remember correctly. The only ones we've had that aren't sports trophies."

    scene day9 ev02-07
    "The pair chat for a little while about Jessica's days at school."
    Pri "Well, Ms. O'Neil, what brings you here today?"
    Jes "I was hoping you could help me with some documents I'm looking for."
    Jes "It's relating to the East Wing reconstruction Project from 2012."

    scene day9 ev02-08
    Pri "I'm confused. Those documents should be public record."
    Jes "Some of them are, but there's quite a lot that's been left out. We were hoping you could help us get the full records."
    "Principal Sheers leans back in his seat, his relaxed demeanor going rigid."
    Pri "I'm sorry, Ms. O'Neil. I'd really like to help you, but I'm afraid those documents are confidential. To get them I'd have to make a request to the county office, and they'd have to agree to release them."
    Pri "It's extremely unlikely they would. They detest releasing documents to the press, and I would be putting my own career in jeopardy if I did so."
    Jes "Please, Principal Sheers. It would be an immense help, and I can guarantee we wouldn't reveal our source."
    Jes "I would be so very grateful for your assistance, sir."
    "Despite working to make her voice soft and bat her eyes, the Principal seems unconvinced."
    Pri "I'm sorry. There's just nothing I can do. The school administration has become much stricter about these sort of things in recent years. I'd be risking my job."
    Pri "If we kept the documents here, I'd be more than happy to do you this favour."

    scene day9 ev02-09
    "He goes on, talking about school and county policy."
    "Jessica sighs and turns away, her eyes landing on the teacher's pointer lying at the end of his desk."
    JesT "Wow, he still has that, huh? He loves that thing."
    JesT "He used to terrorize us with it, threatening to spank us if we got out of line, \"just like the old days\"."
    JesT "Not that he ever did. Corporal punishment isn't allowed here."
    JesT "You know, come to think of it, he used to threaten the female students with spanking a lot more than the boys."
    JesT "And he always did have a strange twinkle in his eyes when he threatened us, like he really wanted to do it."
    "Her eyes move back to the Principal, who's still droning on."
    JesT "I wonder if he'd like to live that fantasy, maybe use that pointer on a young woman like me."

    if "d08connerFun" in choices:
        JesT "Conner paddled my ass hard last night. I bet I could take a few swats with that thing."

    JesT "And it's not like it'll be sexual, for me anyway."
    JesT "Then again, maybe that's going too far. Asking a principal to spank his former student, just like he always wanted. Is that too much?"

    menu:
        "Let it go":
            JesT "Yeah, it's probably too far."

            scene day9 ev02-10
            "Jessica heaves a weary sigh."
            Jes "I understand."
            Pri "I'm sorry I couldn't do more for you."
            Jes "Well, thank you for your time, Mr. Sheers. I will leave you to your work."

            scene day9 ev02-11
            "As Jessica stands up, the Principal walks around his desk and takes her hand."
            Pri "Well, it was a pleasure meeting you again, and I'm so glad to see one of our students working at the Gazette."
            Jes "It was nice speaking to you again, without the dread of having been called here from class."
            Pri "Hahaha! Yes, I imagine so. Again, I'm very sorry I couldn't help, but if you need anything in the future, don't hesitate to come by."
            Jes "I will. Thank you."

        "Try to tempt him":
            $ choices.append("d09teasePrincipal")
            $ work += 1
            JesT "Well, if it works, it works. Let's see how badly he wants to indulge his kink."

            scene day9 ev02-12
            "Jessica stands up and moves toward him, teasing him with her stare and her body language."
            "Her hand runs along the pointer as she goes."
            Jes "You know, Mr. Sheers, I remember getting called to this office a few times when I was a student."
            Jes "You loved to tell us, \"Bad girls should be spanked!\""

            scene day9 ev02-13
            "She picks up the pointer and takes a seat on his desk, his eyes immediately drawn to her ass."
            Pri "I, uh… don't recall…"
            Jes "Oh, but I do. My girlfriends and I were always so afraid that you'd spank us. Hard."
            Pri "Well, if I did, it was only to frighten you. So you'd behave."

            scene day9 ev02-14
            Jes "Were you tempted to do it? To give one of us bad girls a good ssspanking?"
            "Jessica lightly slaps the pointer onto her own hand for emphasis, and does it a few more times as she goes on."
            Jes "I bet you were thinking about the sound this made when it hit a young girl's tight, firm little bottom, and seeing it shake with the impact."
            "Principal Sheers finally regains his composure, and straightens in his chair."
            Pri "I would never do that to a student."
            Jes "Of course you wouldn't. That would be wrong. But… what about an ex-student?"
            "He mumbles under his breath."
            Pri "What do you mean?"

            scene day9 ev02-15
            "Jessica turns around, presenting her ass."
            "There's no longer any attempt to hide that he's looking at her backside."
            Jes "What if I said I've been a bad girl for a long time? What if I was just waiting for you to call me to your office for… proper discipline?"

            scene day9 ev02-16
            Jes "I knew you wouldn't do it while I was a student, but I'm not a student anymore, though I'm still a very bad girl."
            Jes "Do you think the good spanking I've needed all these years will help me be a good girl?"
            "Sheers nods several times, his eyes glued to her bottom."
            Pri "Yes. Bad girls should be spanked. It'll make you good."

            scene day9 ev02-17
            "He's breathing heavily, speaking in short bursts."
            JesT "I've got you, you pervy old man."
            Jes "Here."
            "She places the pointer next to her bottom, and he takes it with a shaky hand."
            Jes "I was thinking, I'll come back tomorrow. If the documents I need are on your desk, I won't be able to help myself. I'll have to look at them."
            Jes "Because I'm a very bad girl."
            Pri "Yeah…"
            Jes "And in that case, you could help properly discipline me with your… stick."
            Pri "Yeah. I would have to… punish you properly. And I will… if you do that."

            scene day9 ev02-18
            JesT "Okay. I think that's enough."
            "Jessica turns around and straightens up."
            Jes "Well, I should be off for today. It was a pleasure to see you again, Mr. Sheers."
            Jes "It brought back some good memories."
            Jes "I'll be back tomorrow. If you've found those documents for me, I'd love to see your education methods."

            scene day9 ev02-19
            "She grabs her purse and heads for the door, making sure to sway her ass as she goes."
            Pri "Uh, Ms. O'Neil!"
            Jes "Hmm?"
            Pri "Do you still have your cheerleading uniform?"
            Jes "I think I have it somewhere."
            Pri "Uh, wear it here Friday after 5pm, and I'll have those documents for you."
            "Jessica laughs as she leaves the office."

    scene day9 ev02-20 with fade
    play sound city_street_with_vespa fadein 1 loop
    "Jessica's mind is working as she climbs onto her scooter, considering what she'll say at work."

    if "d09teasePrincipal" in choices:
        JesT "Well, Rosa should be happy I got him to agree to give me the documents."
        JesT "She won't be happy if she figures out HOW I did it. I should just keep that little tidbit to myself."
        JesT "And I have to admit, it was kind of fun."
    else:
        JesT "Well, Rosa will be disappointed I couldn't get the documents."
        JesT "She'd have disapproved of my idea for getting them, anyway."
        JesT "She's right, though. I really shouldn't be acting like a horny schoolgirl to get what I need."
        JesT "Besides, I now know where we can find them. That's something, at least."
    stop sound fadeout 1

    scene day9 ev03-01 with fade
    "Back at the office, Jessica strides in to find an older woman sitting in Rosa's chair."
    "Rosa herself is sitting on her desk, talking to the stranger."

    scene day9 ev03-02
    Jes "Hey, Rosa."
    Rosa "Good morning, Jessica."
    "Jessica turns to the strange woman."
    Jes "Good morning, Miss."
    F "Hello, Jessica.."
    Rosa "Oh, do you two know each other?"
    F "We sort of met, but under… unusual circumstances."
    "Jessica is surprised, both by the idea that they've met and by the woman's presence."
    "She almost seems to control the space around her without moving an inch."
    Jes "I'm sorry. I don't really remember."
    F "Don't worry about it."

    scene day9 ev03-03
    Rosa "This is the paper's CFO, Barbara Palmero."
    "Barbara stands, pushing just enough into Jessica's persona space, making her take a step back."
    "She extends her hand, Jessica taking it in greeting."
    Barb "A pleasure to meet you formally, Jessica."
    Jes "Likewise."
    Barb "Well, I need to get back to work. I'll speak to you later, ladies."
    Rosa "Later, Barb."

    scene day9 ev03-04 with fade
    Jes "She seems nice."
    Rosa "She can be."
    Jes "But I don't remember meeting her."
    Rosa "Well, maybe Barb was wrong."
    "Rosa chuckles."
    Rosa "Because people who meet her don't usually forget it."
    if persistent.pov == 2:
        scene day9 ev03-04fpov
    Jes "She did seem kind of intimidating, didn't she?"
    Rosa "It's fairly normal for those with power."
    Rosa "Only Birch is above her at the company, and it doesn't always look that way."
    Jes "I'll have to make sure I get on her good side, then."
    Rosa "If you want a permanent position here, having a woman like her on your side would certainly help."
    Rosa "But I think you already have it. I haven't usually seen Barb be so nice to anyone."

    scene day9 ev03-05
    Rosa "But speaking of work, how did things go at the school?"

    if "d09teasePrincipal" in choices:
        Jes "He seemed willing to help. I should be able to have the records on Friday."
        Rosa "That's great! Get them to me as soon as you have them."
        "She takes a look at the time."
        Rosa "Excuse me. I have to talk to Duncan about a story."

    else:
        Jes "Sorry. Apparently they don't even keep the records there. They're at the county education offices."
        Rosa "Alright. I appreciate the effort."
        Rosa "I might be able to get them from those offices myself."
        "She takes a look at the time."
        Rosa "Anyway, I need to talk to Duncan about the story. Excuse me."

    Jes "Okay. I'm gonna get some research done on the vigilante story."
    Rosa "Oh, one more thing. Mr. Birch wants to talk to you and Eve."
    Rosa "When Eve gets back from her assignment, you two should go see him."
    Jes "Got it."

    scene day9 ev03-06 with fade
    "Jessica takes a seat at her desk and begins looking for information."
    JesT "I should call the owner of the warehouse the vigilante had the motorcycle delivered to."
    JesT "They might be able to give me some of the information I need."
    "She finds the number for one of the owners in the information she's already collected, and gives him a call."
    "The phone rings for a few moments before a scratchy voice answers."
    MV "Hello?"
    Jes "Mr. George Tremblay?"
    Trem "Yes?"
    Jes "My name is Jessica O'Neil with the New Port Gazette."
    Jes "We are writing an article about the local business, and I was wondering if I could speak to you about the closed Cellco warehouse."
    "The man gives her a heavy sigh."
    Trem "What about it?"
    Jes "I have some questions about the building and its closure."
    Trem "Okay. Look, I don't really have time right now. If you want to meet up tomorrow, I can tell you whatever you need to know."
    Jes "That would be wonderful, sir."
    "After a brief exchange of information, the guy man hangs up without a farewell."
    JesT "Well, he sounds a bit snippy. Oh well."
    JesT "Now, let's see if any new info's turned up on our hero."

    scene day9 ev03-07 with fade
    "She works for about an hour before Eve returns."
    Jes "Hey there, Eve."
    "Eve nods in greeting."
    Eve "Jessica. How are you?"
    Jes "Not bad. Mr. Birch wanted to see the two of us as soon as you got back."
    Eve "Oh? Curious. Well, let's not keeping him waiting."

    scene day9 ev03-08 with fade
    "The two of them make their way to Birch's office, stopping at the receptionist's desk."
    "A beautiful woman Jessica hasn't seen before stands to greet them."
    Rec "Can I help you?"
    JesT "Jesus. That woman's gorgeous! Her face is like a Greek Goddess!"
    Jes "Hi. I'm Jessica O'Neil, and this is Eve Beaulieu. Mr. Birch is expecting us."
    Rec "Of course. He's in a conference call at the moment. Please, take a seat, and I'll let you know when he's ready to see you."

    scene day9 ev03-09 with fade
    "Eve and Jessica head over and sit down waiting to be called."
    Jes "So, have you made any progress with the police?"
    "Eve bobs her head nonchalantly."
    Eve "I've gathered what information I can, but it's difficult without a man on the inside."
    Jes "You still think someone on the force is involved with the rising crime wave?"
    Eve "Oh, I do not think it. I know it."

    scene day9 ev03-10
    "Eve's eyes narrow as if taking Jessica's measure."
    Eve "There were numerous emergency calls to 9-1-1 last year with a response time four-hundred percent slower than usual."
    Jes "That's not terribly unusual. There are some places the police really don't like to go."
    Eve "This isn't about specific neighborhoods. Their responses were delayed to areas that would normally see swift responses."
    Eve "In several cases, the police didn't show up until thirty minutes after the call was made."
    Eve "In one instance, the response time was almost an hour."

    scene day9 ev03-11
    Jes "Are you sure? They're actually delaying their response intentionally?"
    Eve "In some cases. I can't prove it, but the evidence looks awfully suspicious."
    "Their conversation is interrupted by the receptionist."
    Rec "Mr. Birch will see you now."

    scene day9 ev03-12 with fade
    "She leads them into the office, then speaks briefly with Mr. Birch about administrative tasks."
    "After giving his receptionist her instructions, he turns and smiles at Jessica and Eve."
    Birch "Good morning, ladies. Can I get either of you a drink?"
    Jes "Uh, no, thank you."
    Eve "Non, merci."

    scene day9 ev03-13 with fade
    "He stands and motions toward the chairs."
    Birch "Please, have a seat. I wanted to have a talk with our newest hires."
    Birch "Don't worry, I don't bite. Not unless I have to, anyway. Ha!"

    scene day9 ev03-14 with fade
    "Both of them chuckle and take a seat, though Jessica feels more than a little nervous."
    JesT "I feel like I just got called into the Principal's office. Is that irony? No, just coincidence."
    "Birch takes a seat on his desk and fixes both ladies with a smile."
    Birch "So, how was your first week? Everything going well?"
    Jes "Very well."
    Eve "Yes. I've very much enjoyed myself."
    Birch "Great! Glad to hear it!"
    Birch "You've both gotten settled in, figured out how things work around here."
    Eve "Yes, Mr. Birch. I feel very much at home."
    JesT "Suck up."
    Birch "And you, Jessica?"
    Jes "Definitely. Everyone's been very helpful in getting me acclimated."
    Birch "Wonderful."

    scene day9 ev03-15
    Birch "So Jessica, this vigilante story. Have you made any progress?"
    Jes "I have a good lead. I know it's going to take me to solid info. Definitely something we can print."

    if "d03vigilanteVideo" in choices:
        Birch "What about that video you got from the police? Are we ready to publish it?"

    else:
        Birch "What about that picture you got from the police? Are we ready to publish it?"

    Jes "I spoke with a detective investigating the vigilante yesterday and tried to exchange information about the case. Specifically the revelation about the motorcycle."
    Birch "That they already knew about."
    Jes "Exactly. I figured if I tried giving them what they already have, they wouldn't think I got it from them in the first place."
    Birch "Covering your source. Not bad."
    Jes "He still won't be happy if I we use what I got from him. And we can burn a valuable asset."
    Jes "I'd like to talk to him again. Maybe I can convince him to give us consent to use the materials."
    Birch "Alright, I'll think about it."
    Birch "Now, Eve, tell me how the story you're working with Rosa is going."
    Eve "Excellent, sir. We've made some wonderful progress."
    "Eve goes on for a few minutes, describing the work she and Rosa have been doing."
    Eve "I love working with Rosa. She's fantastic."
    Eve "It's truly a privilege to work here."
    JesT "Could you be sucking up any more? The only way you could be trying harder to make him like you is by sucking his dick."
    JesT "Oh. I hope she's not sucking his dick. That wouldn't bode well for me."

    scene day9 ev03-16
    Birch "Wonderful. Wonderful. It sounds like you're both doing very well here, and I think you both have what it takes to make it as journalists nowadays."
    Birch "See, here's the thing. Rosa and Duncan have proven themselves over the years. They're damn good at their jobs, and they'll keep being good at them."
    Birch "But I need something BOLD from my journalists. I need stories that will really POP!"
    Birch "Duncan gets all riled up when I talk like this, but the truth is that boldness is what will keep this business going!"
    Birch "Not that I want to turn our paper into some gossip rag for lonely and bored housewives who sit around reading about Batboy, or the coming apocalypse, or crap like that all day long."
    Birch "I need new blood that will reinvigorate this paper! Crooked politicians? Who gives a shit? But a politician using public funds to organize underground fight clubs? That sells!"
    Birch "I want you two, fresh blood with fresh eyes, to really bring something new to this paper!"
    "He motions toward Eve, then Jessica."
    Birch "Be it with murder at construction sites, or shots of a vigilante beating the hell out of gansters."
    Birch "This is what we really need!"

    scene day9 ev03-17
    Birch "Alright, that's all for now. Go out and do your thing, ladies."
    "Before Jessica can say anything, Eve stands up and leans toward Mr. Birch."
    Eve "I won't disappoint you, sir."
    "She plants a kiss on his cheek, much to Jessica's surprise and Mr. Birch's clear enjoyment."
    Birch "I know you won't! Not with that kind of energy, young lady."
    JesT "You slutty bitch. You really will do anything to make sure you get this job, won't you?"

    scene day9 ev03-18
    "Jessica stands up as well, giving Mr. Birch a smile."
    Jes "I'll make sure to find everything there is to know about this guy, Mr. Birch. I promise you."
    "He almost looks a little disappointed."
    Birch "Remember, Jessica. Be bold, and take the initiative!"
    Birch "Show me that hiring you was the right decision!"
    JesT "You mean act like a horny little schoolgirl, like Eve there?"
    JesT "If I don't give him a kiss too, she'll definitely have left this meeting with the upper hand. The bitch."
    JesT "Damnit. Do I do it? It's only a kiss. Maybe not one I should have to give, but still. It's just a kiss."

    menu:
        "Just say goodbye":
            JesT "No. I'm not going to act like that just because Eve did."
            JesT  "I can still beat her the old fashioned way."

            scene day9 ev03-19
            Jes "I will, sir. You'll have your story. I promise you that."
            Birch "Excellent. Thanks for coming ladies."

        "Give him a kiss":
            $ choices.append("d09kissBirch")
            $ relBirch += 1

            JesT "What the hell. Might as well keep the boss happy. Like Heather said, there's nothing wrong with a little flirting."
            JesT "And I can play this game too, Eve. If this is a competition, I'm gonna win it."

            scene day9 ev03-20
            "Jessica leans in and plants a soft kiss on Birch's cheek. He's smiling wide as she does so."
            Jes "You'll have your story, sir. I promise you that."
            "He laughs."
            Birch "I know you ladies will deliver. Now get out there and do your thing."

    scene day9 ev03-21 with fade
    "The two of them head out together, both striding confidently."
    Jes "Well, you were awfully eager to please the boss, weren't you?"
    "Eve doesn't even break stride, giving just a hint of a smile."
    Eve "I told you, I'm going to have this job. Whatever it takes."
    JesT "Well, at least she's honest about it."

    if "d09kissBirch" in choices:
        Eve "Besides, you didn't seem too bothered by kissing him either."
        JesT "She's right. I wonder if I can do what women like Eve and Heather can."

    scene day9 ev04-01 with fade
    "Back at their desks, Eve and Jessica get to chatting about their meeting with Birch, pondering his words."
    Jes "Well, regardless of whether or not there's only one position, it's clear he won't accept anything but total success."
    Eve "Which means we need to work our asses off finding something, or it will be \"au revoir\" for us both."
    Rosa "Hey girls."
    Jes "Hey, Rosa. Please tell me that you brought extra of whatever the hell smells so good!"
    Rosa "Oh, this is lunch for all of us. Hope you like Chinese!"
    Eve "Dieu merci! I am starving!"

    scene day9 ev04-02 with fade
    "The three of them have lunch together, discussing their individual assignments."
    Jes "I just have this feeling that I'm so close to finding something about this vigilante."
    Jes "I have a meeting tomorrow, and I'm hoping it'll point me toward his identity."

    if "d09teasePrincipal" not in choices:
        Rosa "Oh, by the way. I think I found somebody who can get us those files."
        Eve "Maybe you could have charmed him like you did the mayor, Jessica. I'm sure he would have given them to you then."
        "Eve chuckles at her own joke, but Rosa shakes her head."
        Rosa "Don't listen to her. We get the job done by acting like professionals."
        JesT "And yet Eve seems willing to use her looks. It's gonna make it hard to compete with her."

    scene day9 ev04-03 with fade
    "After lunch, Jessica goes back to her desk and resumes her search for info on the vigilante."
    "Rosa pops by a few minutes later."
    Rosa "So, how did the meeting with Birch go?"
    Jes "Well, he's happy, but the man is demanding."
    "She explains how the meeting went."
    Rosa "Look, don't let the old man push you into doing something dangerous."
    Rosa "This job requires knowing when to stop before you get hurt. Talk to Duncan before going out to do something crazy."
    Jes "Ugh. You sound just like Conner."

    scene day9 ev04-04
    Rosa "I'm sure Conner just cares about you."
    Jes "He does."
    Rosa "He sounds like a sweet guy."
    Jes "He is. He's wonderful."
    Rosa "We should go on a double date sometimes. You, me, and our boys. I don't get out with my husband much."
    Jes "That sounds great."

    scene day9 ev04-05 with fade
    "The two of them get lost in conversation, and neither notices Tommy arrive."
    Tom "Uh, hey."
    Rosa "Oh. Hi."
    Jes "Hey, Tommy! How's it going?"
    Tom "Not too bad."

    scene day9 ev04-06
    Rosa "Jess, you have something for Tommy to do now that he's here?"
    Jes "I'm afraid not. I've cleared my work since I thought I was going to be heading out to meet someone today, but we moved it to tomorrow."
    Rosa "Okay. Tommy, why don't you come with me. I've got an interview, and you can tag along."
    Tom "Sure."
    Rosa "I've got to grab some things. Meet me out in front of the building, okay?"
    Tom "Okay."

    scene day9 ev04-07
    Jes "So, how are you liking journalism? The grunt work hasn't ruined it for you?"
    Tom "No, it's fine. They told us that's pretty much what it would be in school."
    Tom "I mean, I did think there would be more snooping around, and less, like, paperwork and searching through documents, you know?"

    scene day9 ev04-08
    Jes "Hahaha! And what would you be doing if you weren't here right now?"
    Tom "I don't know. Playing a game, probably, or maybe LARPing with my friends."
    Jes "That's the live-action stuff, right? With the fake swords and everything?"
    Tom "Right. It's a lot of fun, actually."

    scene day9 ev04-09
    Tom "You could… come by and check it out, if you want? If you're still interested, you know?"
    JesT "Oh, that's right. I did say I'd be interested in check it out."

    menu:
        "Agree to go with him":
            $ choices.append("d09geekDate")
            $ relTommy += 1
            JesT "It does sound a little weird, but I did say I'd like to come see."
            JesT "Besides, I like the whole 'Lord of the Rings' kind of thing. It could be fun."

            scene day9 ev04-10
            Jes "Sure. I'd love to come by and check it out."
            Tom "Really? Awesome!"
            Jes "I mean, I've never been to one of these things, so I have no idea what to do or wear."
            Tom "That's cool! I'll show you the ropes. And your regular clothes will be fine if you're just watching."
            Tom "I'll ask my friends when we're doing it next, and I'll get back to you tomorrow."
            Jes "Cool. I look forward to it. You should be going, though. Rosa will be waiting."
            Tom "Right. Right. I'll talk to you later."
            Jes "Bye!"

        "Maybe some other time":
            $ relTommy -= 1
            JesT "Oh, this sounds weird, and kind of boring. I only really showed any interest because Eve was mocking him."
            JesT "Plus, it would be SUPER awkward hanging around a bunch of high school kids."

            scene day9 ev04-11
            Jes "I'm sorry. I'm kind of swamped. I won't have any free time for a while."
            Tom "Oh. Okay. That's cool."
            Jes "If you want, you could bring some pictures to show me."
            Tom "Yeah. I'll do that."
            Jes "Anyway, you should get going. Rosa will be waiting."
            Tom "Right. I'll talk to you later."
            Jes "Bye."
            JesT "I hate to disappoint the kid like that. Oh well."

    scene day9 ev04-12 with fade
    "Jessica goes back to her research, working on that as well as a few other projects."
    "Before too long she realizes that whole work day has passed."
    JesT "Oh damn. It's late. I should get going."

    scene day9 ev04-13 with fade
    "Grabbing her things, Jessica starts to head out, finding Eve still at her desk."
    Jes "You heading out soon?"
    Eve "I'm almost done. I just need a few more minutes. This damn site loads way too slow."
    Jes "Alright. Have a good night."
    Eve "You too."
    JesT "It really is too bad she's such a bitch. We could be good friends, if she wasn't trying to get my job. Oh well."

    scene day9 ev05-01 with fade
    "Jessica is groaning when she gets home, kicking off her shoes and beginning to undress immediately."
    Jes "Babe, you here?"
    JesT "... Hmm. Guess not."
    JesT "Too bad. I could really do with a foot massage right about now."

    scene day9 ev05-02 with fade
    "Going down to her undergarments, Jessica plops down onto the sofa and checks her phone, finding a text from Conner."
    Con "be home l8, don't wait for dinner"
    Con "Love you"
    "She sighs."
    JesT "He's gonna be home late. Again. Great."
    JesT "I guess I'll just make myself something then."

    scene day9 ev05-03 with fade
    "She puts on a pair of shorts, then fixes herself dinner."
    "Taking a seat on the sofa, she turns on her Nook and begins reading, eating as she does so."
    "The day's stress finally begins to bleed away, her body relaxing at last."

    scene day9 ev05-04 with fade
    "After dinner, she calls Laura. They talk for a bit about various things."
    "Laura tells her that their mother won't be visiting that week, her appointment having changed."
    Jes "Oh good. I love Mom, but I'm too tired to deal with her right now."
    Lau "Problems?"

    if "d09dateParker" in choices:
        Jes "Nothing much. Just a lot going on… Hang on."
        JesT "Oh. Mr. Parker's calling."
        Jes "Hey, I've got another call."
        Lau "Okay. Talk later, sis. Bye-bye!"
        Jes "Bye, Laura."
        "She changes over to the other call."
        Jes "Mr. Parker! Hi!"
        Parker "Hey, Jessica! I'm on my way over. Be there in about thirty, maybe forty minutes."
        Jes "Okay! See you soon!"

        jump day09dateParker

    else:
        Jes "Nothing much. Just a lot going on lately. With work and Conner."
        Jes "Don't worry about it."
        Lau "Okay."
        "The sisters chat for a little while longer, then say goodbye to one another."

        jump day09lonelyEvening

label day09dateParker:

    scene day9 ev05-05 with fade
    "Jessica takes a quick shower, then gets dressed and does her makeup."
    JesT "Well, if Conner's going to stay out late, I'm gonna have some fun without him."

    if "d04parkerNoApology" in choices:
        JesT "His loss… and maybe Mr. Parker's gain."
        "She smiles, and blushes ever-so-slightly."

    "Her phone chimes, a message from Parker coming up saying he's just outside."
    "Grabbing her keys and purse, she heads out to join him."

    scene day9 ev06-01 with fade
    play sound neighborhood_1 fadein 1 loop
    "He's waiting outside for her, standing by his car."
    Parker "Good evening, Jessica. You look absolutely stunning tonight."
    Jes "Why, thank you so much, Mr. Parker. Although the real vision of beauty here is your car. She's gorgeous."
    Parker "Yeah, she's a classic. I don't drive her much."

    scene day9 ev06-02
    Jes "Well, I'm flattered you brought her out for me tonight."
    Parker "My pleasure. Here, let me get the door for you."
    Jes "Thank you."
    stop sound fadeout 1

    scene day9 ev06-03
    play sound car_driving_2_ambient fadein 1 loop
    Jes "So, where are we meeting your friend?"
    Parker "He's meeting us at a bar called the Red Baron."
    Jes "So what's he like, this friend of yours?"
    Parker "His name's Jack. Ex-cop, like I said. I've known him for a long while. He's a… character. You'll see soon enough."
    Parker "But he's a good guy, and reliable."
    Jes "I hope he can put me in contact with someone. I could really use a source with contacts in the PD."
    Parker "Everything okay at work?"
    Jes "Well, me and Eve, she's the new girl at work, had a chat with Birch earlier, and he made his expectations about \"revolutionizing the newspaper business\" pretty clear."
    Parker "Ah."

    if "d04parkerGrope" in choices:
        scene day9 ev06-04
        "As she's speaking, Parker puts his hand on her leg."
        JesT "Speaking of men and their expectations."
        JesT "Although this time I can't say I mind at all."
        "She goes on talking while he gently squeezes, his hand just firm enough."
        Parker "I wouldn't be worried, Jess. I know you'll deliver."
        "She gives him a warm smile and pats his hand. He pulls it away to concentrate on driving."

    else:
        Parker "I wouldn't be worried, Jess. I know you'll deliver."

    scene day9 ev06-05
    Jes "Thank you, Mr. Parker."
    Parker "Besides, this just how he gets. He's been going on about his whole \"newspaper revolution\" since I've known him."
    Parker "And if Birch is being too much of a pain, I can pay him a visit and talk to him."
    Jes "I appreciate it, but hopefully that won't be necessary. If your friend can help me, it would be a huge boon for my work."
    stop sound fadeout 1

    scene day9 ev06-06 with fade
    "The bar is nicer than Jessica had been expecting. Pleasant smells are coming in from the kitchen, and the mountains of top-shelf liquor behind the bar are already making her mouth water."
    Jes "Not too loud, not too many people around. It's a good place to have a little talk."
    Parker "There. That guy sitting alone is Jack."

    scene day9 ev06-07
    "Jack smiles when he sees Parker and rises to greet him."
    Parker "Hey, Jack."
    "Jack nods, but his eyes are on Jessica."
    Jack "Hello. Ben mentioned his friend was pretty, but he undersold it."
    "He picks up Jessica's hand, planting a rough kiss on her fingers."
    Jack "I'm Jack Dale. A pleasure to meet you."
    Jes "Charmed. I'm Jessica."

    scene day9 ev06-08
    Jack "Hey, Big Ben."
    Parker "Jack. Still a horn-dog, I see."
    Jack "Always. I was gonna bust your balls for not calling me for so long, but you made up for it with your choice of dates."
    Jes "Oh, we're just friends. I've known Mr. Parker for quite a while."
    Jack "Okay. Well, have a seat you guys. I'll go grab some drinks."

    scene day9 ev06-09 with fade
    "Jack heads off to the bar, coming back a moment later with a mug of beer and a martini."
    Jack "Martini for the lady. And let's see if old Big Ben here can still drink like a man."
    Parker "Do I have a choice?"
    Jack "Hell no. Beer is the best lubricant. For friendly conversation."
    JesT "Hehe. Subtle."

    scene day9 ev06-10
    Jack "So, Jessica, how do you know Big Ben here?"
    Jes "I'm a journalist working down at the New Port Gazette. Mr. Parker here is kind of my mentor, and has been sharing his years of experience with me."
    Jack "Many, many years, as a matter of fact."
    Parker "You're such an asshole, Jack."
    Jack "Guilty as charged. Gotta say, though, Ben here's still got his game if he has a friend like you, Jessica."
    "Parker shakes his head and turns to Jessica."
    Parker "Don't pay him much mind. That's just how he is."
    "Jessica smiles and takes a sip of her martini."
    Jes "So, Mr. Parker tells me you used to be a cop."
    Jack "Used to be. Now I'm a private eye."

    scene day9 ev06-11
    "Jack pulls out a business card and hands it to her."
    Jack "Jack Dale Investigations. Seeing as how you're a journalist, I figure you might need some PI work from time to time. Call me if you ever need anything."
    Parker "Jack here is like a traveling salesman. He's always ready to peddle his wares."
    Jack "I never let an opportunity pass me by, that is true. Especially one as beautiful as you, Jessica."
    "He gives her a wink, and Jessica has to keep from rolling her eyes."
    JesT "Oh brother."

    scene day9 ev06-12
    Jes "Well, I'm currently working a few stories that could use a good source in the NPPD."
    Jes "I was hoping you might be able to put me in contact with some of your buddies at the precinct. Someone willing to collaborate and share information from time to time."
    Parker "Like we used to do."
    Jack "Hmm. Well, I could introduce you to Detective Naomi Marshall."
    Jack "She's a young detective. Ambitious, honest, direct. If you have something to give her, she'll give you something back."

    scene day9 ev06-13
    "Jessica sighs."
    Jes "Damn."
    Parker "What's wrong."
    Jes "I actually met Detective Marshall yesterday. We didn't get off to a good start."
    Jes "I don't think she likes me much."
    Jack "Don't worry about it. I'll give her a ring, makes sure she gives you another chance."
    Jack "She'll definitely expect something in return, not like the way I used to just give this old bastard anything he asked for."
    Parker "Hey, I solved more of your cases than I remember. And how many beers did I buy you?"
    Jack "Not nearly enough."
    Parker "How many would have been enough?"
    Jack "No such thing. Anyway, you're losing your memory, old man."
    Parker "Oh yeah? Remember the Kripke case? With the guy driving the Impala full of guns."
    Jack "That guy who thought Satan was trying to possess him? Come on, I would have solved that one."
    "The two continue to bicker back and forth, Jessica listening to the two of them with amusement."

    scene day9 ev06-14 with fade
    "Jack and Parker start telling Jessica their stories, about working together to solve cases and get stories for the paper."
    "They can't agree on the details though, both of them claiming a greater contribution than the other."
    "Jack is downing one beer after another, and encouraging the other two to do so as well."
    "Jessica is taking tiny sips, while Parker keeps insisting he has to drive."
    Jack "Ah, lightweights! You used to be able to drink Ireland under the table, Ben!"
    Jack "And speaking of old times, you still remember how to play pool?"
    Parker "It's been a while, but I'll give it a shot."
    Jack "How about you, Jessica? Can you play?"
    Jes "Oh yes."

    scene day9 ev06-15 with fade
    "Jack downs the remainder of his beer and lets out a loud belch."
    Jack "Gonna grab another. Be right back."
    Parker "Here."
    Jes "Thank you. Jack certainly likes his beers, doesn't he?"
    Parker "Oh, he's just getting started. I'll bet we have to dump him into a cab by evening's end."

    scene day9 ev06-16 with fade
    "Jessica and Parker head over to the pool table, chatting until Jack returns, a beer in one hand and a martini in the other."
    Jack "Here you go, Jessica. It wouldn't be fair for us to play drunk while you're sober."
    Jes "Thank you."
    Jack "Hey, what's up with the Mr. Parker thing?"
    Jack "You two seem close enough for you to call him Ben."
    "Jessica shrugs."
    Jes "It's just a sign of respect."
    Parker "I keep trying to get her to call me Ben, but she's stubborn."

    if "d04parkerNoApology" in choices:
        JesT "And if I'm being honest, it's kind of kinky calling him Mr. Parker. It reminds me how naughty it is flirting with a man his age."

    scene day9 ev06-17 with fade
    "Jack racks the balls while Parker gets a cue and chalks it up."
    Jack "Alright, old man. I'll even give you first break."
    Parker "Let's do it."
    "Jessica sits back and watches."
    JesT "Mr. Parker certainly does have some interesting friends. Then again, the people I've been meeting lately have been fairly colorful."
    JesT "I wonder if Mr. Parker is the kind of person I could end up being. Hopefully not working at a newsstand, though."

    scene day9 ev06-18 with fade
    "The game goes on with Parker and Jack throwing a great deal of shade each other's way."
    "It's clear their relationship is genial, though, and that they're good, long-time friends."
    "Jessica is quite amused listening to their back and forth, finding their interactions sweet."
    "The fact that both of them keep trying to impress her with their shots is also flattering."

    scene day9 ev06-19 with fade
    "Jessica plays herself, though it's been some time. She acquits herself well enough, despite not being nearly as good as Parker or Jack."
    "She doesn't mind, though, and is just having fun hanging out with the guys."
    "Jack is relentless with his flirting, passing endless compliments Jessica's way."
    "And she definitely feels his eyes on her ass when she leans down to line up a shot."
    "She thinks the alcohol is exacerbating Jack's need to flirt, quite an accomplishment considering how shameless he was before he was drunk."

    scene day9 ev06-20 with fade
    "After a few games, Jack drunkenly drapes himself over his friend."
    Jack "Alright, Big Ben. Whaddya say we up the stakes, eh?"
    Parker "What did you have in mind?"
    Jack "Remember that baseball you caught at the World Series game?"
    Parker "Back in 2000, when the stars aligned and the Gryphons actually made it? Of course. I still have the ball."
    Jack "Okay. One game, you and Jessica against me. I win, I get the ball."
    Parker "And if we win?"
    Jack "Then not only will I talk to Detective Marshall, I'll become Jessica's informant. I still have quite a few contacts on the force."
    Jes "Hold on…"
    Parker "Done! Let's do it!"
    JesT "Well, that would be really nice, but…"

    scene day9 ev06-21
    "While Jack racks the balls, Jessica sidles up to Mr. Parker."
    Jes "Mr. Parker, you don't have to do this. Plus, I'm not a very good partner. I'll probably lose you that ball."
    Parker "Don't worry about it, Jess. It's just a ball."
    Parker "Besides, we have no plan to lose, right?"
    Jes "No one plans to lose, it's just sort of happens!"
    Parker "Trust me. We'll be fine."
    JesT "If you say so."

    scene day9 ev06-23 with fade
    Jack "Alright, Jessica. Your break. Let's see what you got."
    "Jessica tries to show a confidence she doesn't have."
    Jes "My pleasure. And it's gonna be my pleasure to have you as an informant, Mr. Dales."
    Jack "Oh. So cocky. Makes you even prettier."
    "Jessica just smirks and makes the break."

    if "d04parkerNoApology" in choices:
        scene day9 ev06-24a with fade
        "As the game begins, Parker gets close to Jessica and helps her line up her shots."
        Parker "Alright. Just like that. Remember to hit the ball on the side to get the spin you need."
        "Jessica nods slowly, lining up her shot while trying not to blush. Having his hands on hers and his body pressed so close is giving her pleasant sensation."

    else:
        scene day9 ev06-24b with fade
        "As the game begins, Parker gets close to Jessica and helps her line up her shots."
        Parker "Alright. Just like that. Remember to hit the ball on the side to get the spin you need."
        "Jessica nods slowly, lining up her shot."

    "Her hit is perfect, making Jack scoff as she sinks her ball."
    Jack "Yo, wait your turn, Ben. That's just cheating, is what that is."

    scene day9 ev06-25 with fade
    "After a few hits she finally misses, Jack stepping up to make his play."
    "Jessica heads over back over to the bar."
    JesT "I'm not as rusty as I figured I would be. Or maybe Mr. Parker's just a good partner."

    scene day9 ev06-26a
    "Jessica takes a big sip of her drink, turning around just in time to see Jack miss."
    "As Parker steps up to make his shot, Jack comes over to the bar to speak with her."
    Jes "Are you okay, knowing you're going to lose to a girl?"
    "He gives her a hearty but quiet laugh."
    Jack "Oh, I can't possibly lose."
    Jes "How so?"
    Jack "I win, Big Ben's baseball becomes mine. You win, I get to see you again."
    Jack "It's win-win for me, sweetie."
    "He raises his glass in a toast."
    Jack "May the best man win."

    scene day9 ev06-26b with dissolve
    "After the drink, Jessica raises her glass again, but presents it to Jack."
    Jes "May the best woman win."
    "He grins and takes a sip."
    Jack "Why, are you trying to get me drunk?"
    Jes "Maybe, but I bet you're even better when you're drunk."
    JesT "And if not, all the better for me. Maybe Heather was right. Flirting a little to get what I need might not be so bad."

    scene day9 ev06-27 with fade
    "Jack takes his turn, leaving a few solids on the table when he misses."
    "Jessica steps up, sinking all the remaining stripes."
    Parker "Not bad at all, Jessica."
    Jes "Thank you. Now, let's see if I can put this away."
    "Unfortunately, she fails to get the 8-ball in on the next shot."

    scene day9 ev06-28
    Jack "Ooooh, back luck."
    Jack "Sorry, Big Ben. Looks like that ball is mine."
    Parker "Well, I always thought you needed some balls."
    Jes "I'm sorry, Mr. Parker. I should have sunk that one."
    Parker "Hey, don't worry about it, Jess. He could still screw up."

    scene day9 ev06-29 with fade
    "Jack takes his shots, sinking the remaining solids."
    "He starts chalking up his cue again, mocking Mr. Parker while he does it."
    "During that moment, though, Jessica gets an idea."
    JesT "Heather, I could kiss you."
    "She leans on the side of the table, pulling her skirt up a bit and showing off her leg and her fishnets."
    "Jack immediately takes notice, with Jessica running her fingers slowly up her thigh."

    scene day9 ev06-30
    "Jack returns his concentration to the ball with some effort, then takes his shot, but Jessica's plan worked."
    "The 8-ball rolls away, Jack audibly groaning in disappointment."
    Jack "Well, damn."
    JesT "God bless drunk, horny men."

    scene day9 ev06-31
    "Parker doesn't even hesitate, moving to the other side to line up his shot."
    Jes "You can do it, Mr. Parker."
    Parker "Jack, old friend, you always did have a weakness…"
    "He easily and confidently sinks the final shot."
    Parker "...when it came to sinking the 8-ball."
    JesT "Among other things."

    scene day9 ev06-32
    "Jessica cheers happily and hugs Parker close."
    Jack "Ah shit. And I was planning on lording that over him for the rest of his life. Was gonna call it \"Big Ben's Big Ball That Now Gives Him Blue Balls\". Or something. Whatever."
    Jack "Well, I guess fair's fair, and I have to live up to my end of the bet."
    Jack "And if I knew I'd get a big hug out of this, I would have played even harder."

    scene day9 ev06-33
    Jes "Then next time maybe you should play on my side."
    Jack "I'll remember that. You ain't as rusty as you made yourself out to be."
    Jack "Good game, you two."

    scene day9 ev06-35 with fade
    "Jessica and Parker take a seat at the bar while Jack goes to get more beer."
    "He comes back with two mugs, one for himself and one for Parker."
    Parker "Thanks, but I can't have any more. I've got to drive Jessica home."
    Jack "Ah, no worries. I'll make sure the police don't bother you tonight."
    "Parker groans, but he accepts the mug and takes a sip."

    scene day9 ev06-36 with fade
    "The group sits around and chats for a little while longer, Jack doing most of the talking."
    "He begins to get a little wobbly on his feet, so Parker eventually gets up from the stool and has him sit down."
    Parker "I think you've maybe had enough."
    Jack "Nah, I'm good. I can handle a few more. Easy. I'm good at drinking."
    "Jessica chuckles, amused by his slurred words."
    Jes "Yeah, I think maybe you're about done, buddy."

    scene day9 ev06-37 with fade
    "Jack just keeps going, though, the group having a fun time for a little while longer."
    Jes "Well, this was a blast, guys, but I do need to get back home. Conner will probably be wondering where I am."
    Jack "Wait, you have a boyfriend? I thought you two were an item."
    Parker "Like we said, we're just friends, Jack."

    scene day9 ev06-38 with fade
    "The two of them help Jack up. He hugs them both close, both Jessica and Parker deciding to use it to get him outside."
    Jes "Should we call you a cab, Jack?"
    Jack "Nah, nah, nah. I brought my car. I'm good- good to drive."
    Parker "You're not even good enough to walk. Come on. We'll squeeze into my car, and I'll get you home."
    Jack "Okay. You're a good friend, Big Ben."
    Jes "Yeah, he's a pretty good guy."

    scene day9 ev07-01 with fade
    play sound neighborhood_1 fadein 1 loop
    Jack "You still drive that old thing?"
    Parker "I'm faithful to all my ladies."
    "Jessica opens the door for Jack."
    Jes "Here you go."
    Parker "Actually, why don't you get inside first. Sitting by an open window would be good for him."
    Jack "Hehehe. The old man is afraid I'll puke in his car."

    scene day9 ev07-02 with fade
    "She does as asked, Parker putting Jack in beside her, then getting in on the driver's side."
    "Jessica finds herself squeezed between the two men, trying to make herself as small as possible."
    JesT "Huh. I wonder if this is what it feels like being in a two-man threesome."
    Parker "You okay, Jessica."
    Jes "Yeah. It's a bit tight, but I'm fine."
    Jack "Ha! I'm used to this kind of ride in Parker's little clown car."
    stop sound fadeout 1

    scene day9 ev07-03
    play sound car_driving_2_ambient fadein 1 loop
    "Parker starts the ignition, then reaches over to the gearshift."
    Parker "Sorry, Jess. Didn't think about this when I thought of this arrangement."

    if "d04parkerNoApology" in choices:
        "Gently, she squeezes his hand while it's between her thighs, giving him a smile."
        Jes "No worries."

    Jack "Who knew such an old car would be a great way to get between a woman's legs?"
    Parker "Don't be an ass."
    Jack "Hey man, it's just a joke. You're no fun when you're sober."

    scene day9 ev07-04
    Jack "Remember that night in the Havana Club, when you showed, ahem, 'The Tower' to that cute waitress?"
    "Jessica tries to hold back a laugh. She turns to Jack, and speaks sarcastically."
    Jes "What's 'The Tower'?"
    Parker "It's, uh, it's nothing. Don't worry about it."
    "Jessica is curious to know more, but she can see Parker is clearly embarrassed."

    menu:
        "Let it go":
            JesT "It seems like he's a little shy in that area. Maybe I shouldn't push it."

            scene day9 ev07-05
            "Leaning over, Jessica squeezes his arm."
            Jes "Hey, who hasn't done silly things when they're drunk?"
            Parker "Well, it was a long time ago, and I don't really remember much about that night."
            Jack "That's too bad. That waitress was something else, man."
            Parker "That's what happens when you drink too much. I doubt you'll remember much tomorrow, bud."
            "Jack turns his eyes to Jessica."
            Jack "Oh, I'll remember the important stuff."
            Jes "You better. You're my informant now, and don't you forget it."
            "His laughter fills the tiny compartment."

        "Ask Jack for details":
            $ choices.append("d09curiousKitty")
            JesT "I know Mr. Parker seems shy in this area, but I've got to hear this story."

            scene day9 ev07-06
            Jes "So, Jack. Tell me about this… Tower."
            "Jack leans in, a huge grin on his face, and pulls Jessica closer."
            Jack "Well, let's just say there's a reason I call him BIG Ben."

            if "d04parkerNoApology" in choices:
                JesT "You don't have to tell me."

            else:
                JesT "Wow, really? Who would have guessed."
                Jes "Huh. How about that."

            Jack "And he whipped that big boy out, right in front of the waitress! All because he lost a bet!"
            Jes "A bet?"
            Jack "Hahahaha! Yeah! The waitress had been flirting with him all night, and FLOP! Out it comes, and she just has this shocked look on her face, and we can't tell if she's horrified or horny! Ahahaha!"

            scene day9 ev07-07
            "Still laughing, Jack leans over and pats Parker on the back."
            Jack "Yeah, the old man had quite a way with the ladies back in the day."
            Parker "I'm almost glad I don't remember that night."
            Jack "It's a shame. I'm pretty sure that waitress liked what she saw."
            "Parker blushes, with Jessica smiling at him."
            JesT "Poor guy. He's so bashful."
            JesT "Then again, if he's hung like a horse, I guess calling him 'poor guy' is kind of silly."
            Parker "That's what happens when you drink too much. I doubt you'll remember much tomorrow, bud."
            "Jack turns his eyes to Jessica."
            Jack "Oh, I'll remember the important stuff."
            Jes "You better. You're my informant now, and don't you forget it."
            "His laughter fills the tiny compartment."

    stop sound fadeout 1

    scene day9 ev07-08 with fade
    play sound city_street_night_1 fadein 1 loop
    "They pull into a small alley. Jack gets out of the car, then turns back around."
    Parker "Have a good one, Jack."
    Jes "It was a pleasure meeting you. We'll talk soon."
    Jack "I'm already looking forward to it. I'll let you know as soon as I have something for you."
    Jack "And feel free to call me any time, for anything."
    Jes "I will. Thanks, Jack."
    Jack "And call me more often, you old bastard."

    scene day9 ev07-09
    "Jack stumbles away toward his building, Parker watching as he goes."
    Parker "I want to make sure he goes inside. He gets into trouble when he's drunk."
    Jes "He didn't seem so bad."
    Parker "Oh, tonight he was behaving himself, if you can believe that."
    Parker "Maybe he's getting old after all, or he just wanted to make a good impression with you."

    scene day9 ev07-10
    Parker "If you don't mind, I'd like to wait a few minutes. Just to make sure he doesn't sneak back out."
    Jes "Not a problem. It's nice of you to watch out for him like this."
    Parker "I'd say he'd do the same for me, but if I tried to sneak out drinking, he'd just join me."
    Jes "Not surprising at all."

    if "d09curiousKitty" not in choices:
        "The two talk for a bit to occupy themselves for the next few minutes."
        Jes "I appreciate you introducing me to Jack."
        Parker "He'll be a good source of info. He knows a lot of police officers."
        Parker "It's a damn good thing we won that game."
        Jes "Plus, we saved your ball."
        "He laughs."
        Parker "Which makes me very happy. I really didn't want to lose that."
        Jes "You did say it was just a ball."
        Parker "Yeah, I was lying. I really love that thing. But it was worth the risk."

        scene day9 ev07-40
        "When Jack doesn't reappear, Parker drives back to Jessica's building."
        Jes "Thanks for inviting me. This was a fun evening."
        Parker "I'm glad you enjoyed it. Have a good night, Jessica."
        Jes "You too, Mr. Parker."

        jump day09lateHome

    else:
        scene day9 ev07-11a
        Jes "So, about you and that waitress. You really don't remember what happened?"
        "He sighs, and turns away."
        Parker "I actually remember the whole thing. I just didn't want to give Jack the satisfaction."
        Parker "And he can't keep his mouth shut about these kind of things?"
        Jes "What kind of things."
        Parker "Ugh. She and I had sex later that night."

        scene day9 ev07-11b with dissolve
        Jes "Just showing your dick was enough to make her drop her panties?"
        Parker "Well no, we'd been flirting the whole night. Showing her my… thing… was just a little encouragement, I guess."

        if "d04parkerNoApology" in choices:
            Jes "Well, I know for a fact it ain't little."

        else:
            Jes "Well, according to Jack, it ain't little."

        "Parker smiles and gives a little nod, but doesn't say anything."
        JesT "Just how big is it, I wonder?"

        if "d04parkerNoApology" in choices:
            JesT "I couldn't tell through his pants."

        if "d04parkerNoApology" in choices:

            menu:
                "Drop the subject":
                    JesT "As amusing as this has been, I should probably leave well enough alone. He's clearly not comfortable talking about this."
                    Jes "Anyway, we should probably call it a night."
                    Parker "Agreed."

                    scene day9 ev07-40 with fade
                    "Parker drives back to Jessica's building."
                    Jes "Thanks for inviting me. This was a fun evening."
                    Parker "I'm glad you enjoyed it. Have a good night, Jessica."
                    Jes "You too, Mr. Parker."
                    stop sound fadeout 1

                    jump day09lateHome

                "Ask to see it":
                    $ choices.append("d09parkerShow")
                    $ relParker += 2
                    $ slut += 2
                    JesT "Now I'm too curious. I need to see just how big it is."

                    jump day09theTower

        else:
            JesT "As amusing as this has been, it's not a subject we should be talking about."
            Jes "Anyway, we should probably call it a night."
            Parker "Agreed."

            scene day9 ev07-40 with fade
            "Parker drives back to Jessica's building."
            Jes "Thanks for inviting me. This was a fun evening."
            Parker "I'm glad you enjoyed it. Have a good night, Jessica."
            Jes "You too, Mr. Parker."
            stop sound fadeout 1

            jump day09lateHome

label day09theTower:

    scene day9 ev07-12
    Jes "So… Mr. Parker… will you show it to me?"
    Parker "I… uh, I beg your pardon?"
    Jes "Yeah. I'm intrigued. I want to see how big your dick is."
    Parker "Y- um- I mean- what, now? Here?"
    Jes "Yeah. It's dark, there's no traffic. No one will see."
    "He goes a little pale, his eyes darting about."
    Jes "Come on. You showed the waitress. You can show me."
    "After looking around for a moment more, he nods to Jessica, then reaches down to unzip his pants."

    scene day9 ev07-13
    "He produces his cock, throbbing in his hand as he brings it out to display."
    JesT "Wow. It is pretty big, and it's not even hard yet."
    Jes "Can.. can you get hard for me? I want to see how big it can get."
    Parker "A week ago, I wouldn't have been sure, but given what we've been doing lately, I have hope."
    "Jessica smiles, feeling a warm sensation in her chest."
    JesT "I guess I've brought new life to an old man, and his little man."
    "Parker's hand moves up and down his dick, Jessica watching in fascination."
    Parker "The beers aren't exactly helping."
    Jes "What would help? I want to see it hard."
    "Parker opens his mouth, but before he can say anything Jessica hits upon the answer."
    Jes "Tell me about the waitress."
    Parker "Oh, Jessica. She was incredible. Not as hot as you, but still wonderful."
    Parker "A beautiful latina, sensuous, busty, with shapely legs and full, pouty lips."
    JesT "Sounds a bit like Rosa, actually. I wonder if he has a type."
    Jes "Where did you fuck her, hmm? Where did you stick that big dick in her hot pussy?"
    Parker "Right here, where we're sitting."
    "Jessica laughs, though her eyes never leave his penis."
    JesT "Wow. I'm sitting where he fucked a woman with that gorgeous dick of his. That's so naughty!"
    Jes "Tell me how you fucked her."
    "Jessica is leaning in close, softly whispering in his ear."
    Parker "Well, we started by kissing."

    scene day9 ev07-14a
    "Much to her surprise, he pulls her close and kisses her softly."
    JesT "What the…?!"
    "For a brief moment, she's utterly shocked at his audacity, and considers pulling away."
    play voices x_mf_kissing_1 fadein 1 loop
    "However, she hesitates for but a moment before she kisses him as well."

    scene day9 ev07-14b with dissolve
    JesT "Holy shit! I'm actually doing this! Kissing another man!"
    "She takes in deep breaths, her heart pounding in her chest."
    JesT "He kisses nothing like Conner. He's gentler, not so rough."
    stop voices fadeout 1

    scene day9 ev07-14c with dissolve
    "Eventually, she pulls out of the kiss and looks down at his dick."
    JesT "It definitely looks bigger."
    Jes "What did you do next?"

    scene day9 ev07-15
    "Suddenly, Parker shifts, pushing Jessica back against the seat."
    "He spreads her legs wide, moving his body between them. Her skirt rides high on her hips, revealing her black lace panties to him."
    "Jessica instinctively tries to shuffle away from him, but can't manage to move in the cramped confines of the car."
    Jes "What the… what are you doing?"
    Parker "You asked for details, and showing you is easier than explaining."
    Jes "Mr. Parker, I'm not going to have sex with you."
    Parker "Didn't say we would. I'm just reenacting it."

    scene day9 ev07-16
    play voices x_moaning_low_1 fadein 1 loop
    "She can feel his rigid cock sliding between her legs, along her quickly moistening sex."
    JesT "Okay, this is pretty goddamn kinky, and it feels incredible, but…"
    JesT "It's fine… I think. He's rubbing his dick along my panties, not my pussy."
    "Mr. Parker sighs through barely opened lips, savoring the feeling of Jessica's crotch against his erect manhood."
    Parker "I took her roughly, then and there, just like this."
    "He begins shoving his cock forward for emphasis, running it roughly along her sex."
    Parker "Shoving in hard and fast."

    scene day9 ev07-17
    "He spreads her legs even wider, her right heel hitting the windshield in rhythm with his trusts."
    JesT "Oh my god! This is incredible! And it feels amazing!"
    JesT "I wonder what this must look like from outside, an old man fucking a young woman, her legs spread wide?"
    JesT "Anyone who walks by would think he's fucking me. I feel like such a slut!"
    Jes "Was her pussy tight?"
    Parker "So tight. She felt wonderful, and she was already screaming in pleasure."
    Parker "And she had great tits, like these."

    scene day9 ev07-18
    "His hand comes up to caress her breast, gently but firmly squeezing."
    "He continues to thrust his cock back and forth all the while, never once letting up."
    JesT "This is definitely the sluttiest thing I've ever done in my life. I'm so goddamn wet, I'm pretty sure I'm gonna have to take my panties off before I go home!"
    JesT "And I can definitely feel Mr. Parker's dick getting hard!"
    "He gets bolder, lifting her leg onto his arm, and beginning to thrust against Jessica longer and harder."
    JesT "Fuck, I'm so wet!"
    JesT "Oh my god! If he keeps going, he's gonna cum all over me! I'll have another man's cum spraying on me!"

    scene day9 ev07-19
    "The hand that had been stroking her breast moves up, grabbing her dress and pulling it down to reveal her naked bosom."
    Jes "Hey!"
    Parker "Oh Jessica! Your breasts are even more beautiful than hers were!"

    scene day9 ev07-20
    "Jessica's hand comes up, covering her breast."
    "She knows she's losing control of the situation and that it's time to stop it."
    JesT "I can feel he's hard already, and I can't get more wet than this."
    "He begins rapidly sliding his dick along her sex, clearly on his way to an orgasm."
    stop voices fadeout 3

    scene day9 ev07-21
    Jes "Okay, I think it worked."
    Parker "What?"
    Jes "We were trying to get you hard, remember? And I'm pretty sure you're hard. You should take your seat again."
    Parker "Oh. Oh, right. Okay."

    scene day9 ev07-22 with fade
    "Parker moves back to the driver's seat, Jessica taking a moment to fix her clothes."
    "When she's done, she turns back to him to see his huge, throbbing cock sitting in his hand."
    Jes "Wow. You really are huge."
    "He simply smiles, nodding slightly while continuing to stroke his hand back and forth."
    JesT "He looks like he's trying to hold back, as if he's ready to explode and trying not to."
    JesT "God, I want to touch it so bad! After all that, I really want to feel his dick!"
    JesT "But this has maybe gone way too far."

    menu:
        "Thank him for showing it":
            JesT "No, no. This has gone too far already. I do still want to see him cum, though."
            Jes "Thank you… for showing me. It's beautiful."
            Jes "Can you take care of yourself now?"
            "His eyes show that he longs for her touch, but he knows he won't receive it."
            play voices x_hj_1 fadein 1 loop
            "He nods, beginning to stroke himself faster and faster."
            Jes "Keep telling me what you were doing. How you fucked her."
            "Mr. Parker chuckles and nods."

            scene day9 ev07-30
            Parker "Next I sat here, and she climbed on my lap."
            Parker "She started riding me hard, slamming herself onto my dick."
            Jes "It's too bad the club's gone. We could've gone back and found her."

            scene day9 ev07-31ani-0
            Jes "I would have liked to watch you fuck her with your big cock."
            show d09ev07-31ani
            "He laughs, stroking himself faster."
            Jes "That'd be so hot, watching her bouncing up and down in your lap, her big brown boobs bouncing in your face, your huge cock sliding in and out of her sopping wet pussy…"
            "An image of a naked Rosa bouncing on Parker's cock springs briefly into her mind."
            "The mental image makes Jessica feel an intense tingling between her legs."
            hide d09ev07-31ani
            Parker "Oh god!"
            stop voices fadeout 1

            scene day9 ev07-32
            play voices x_hj_orgasm_1 fadein 1
            "Jessica's words are too much for him. His member twitches in his hand, ropes of cum spraying all about as he tries in vain to contain it."
            "All the while, Jessica watches with wide eyes, entranced by the spectacle."
            stop voices fadeout 1

            scene day9 ev07-33 with fade
            "Once he's finally done, Mr. Parker pulls his hand from his penis, wiping the cum off on his pants."
            Parker "Well, that was the craziest thing I've done in a while."
            Jes "Yeah, that was the craziest thing I've {b}ever{/b} done!"

            scene day9 ev07-41 with fade
            "The two settle in and get back on the road. After a short and slightly awkward ride, they pull up outside Jessica's building."
            "She leans in, giving him a little peck right beside his lips."
            Parker "Jessica, someone might see!"
            Jes "It's dark. Besides, you deserve it after giving me such a wonderful night."
            Parker "Well, have a good night. I need to get home and wash these clothes before it stains."
            "Jessica chuckles."
            Jes "You do that. I'll see you later, Mr. Parker."
            stop sound fadeout 1

            jump day09lateHome

        "Touch him":
            $ choices.append("d09parkerHJ")
            $ relParker += 2
            $ slut += 2
            $ cheat += 1
            JesT "I want to touch it so bad! Touching the cock of a man old enough to be my grandad would be the dirtiest thing I've ever done!"

            scene day9 ev07-23 with fade
            "She leans closer, her hand probing out toward his dick."
            "Seeing what she's doing, Mr Parker stops stroking it and points it toward her."
            "Her fingers merely brush at it at first, teasing him."
            JesT "Oh my god! What am I doing?! He was just thrusting his dick against my pussy, and now I'm touching it!"
            JesT "I really can't believe I'm doing this to someone other than Conner."

            if "d05victorHJ" in choices:
                JesT "Well, there was that asshole Victor, but that was different, it was for work."

            scene day9 ev07-24
            "She forces herself not to think about it, and closes her fingers around his cock."
            "Parker gasps, making Jessica smile a little bit."
            JesT "It's a little softer than Conner's. Probably because of its size."

            scene day9 ev07-25
            "Her hand begins moving up down, slowly and steadily. Pre-cum is already leaking from the tip, a little dripping onto her hand."
            JesT "Maybe a little bit of my own juices, too, given how wet I was when he was rubbing me."
            "Jessica's eyes come up, her gaze locking with his, her hand continuing to go up and down."
            Jes "Do you like it?"
            "He gives a small nod."
            Parker "Yeah."

            scene day9 ev07-26ani-0
            play voices x_hj_1 fadein 1 loop
            "She speeds up, moving her hand faster and faster."
            show d09ev07-26ani
            Jes "I want to see you cum. I want to see your dick explode."
            Jes "Cum for me."
            "His eyes close, his breathing heavy."
            Jes "Was the waitress fucking you this fast?"
            Parker "Faster."
            "Her hand moves faster, then faster, Mr. Parker's breath coming quicker and growing louder."
            Jes "Did you cum in her pussy? In her hot fucking pussy?"
            Parker "Yes!"
            Jes "Then cum! Cum just like you did in her pussy!"
            Parker "Ah! Jessica! I'm gonna cum!"
            hide d09ev07-26ani
            Jes "Do it!  Cum for me!"
            stop voices fadeout 1

            scene day9 ev07-27
            play voices x_hj_orgasm_1 fadein 1
            "He cries out, his cock throbbing in Jessica's hand."
            "His cum sprays everywhere, on his pants, his shirt, the steering wheel, all while Jessica continues to stroke his huge cock."
            "She watches in fascination, her eyes wide and her heart beating rapidly."
            JesT "There's so much cum! I wonder when he last came like this?"
            stop voices fadeout 1

            scene day9 ev07-28 with fade
            "Eventually it comes to an end, Jessica releasing the warm, slick member."
            "She grabs a tissue from her purse, cleaning her own hand before passing him one as well."
            Parker "Thank you."
            Jes "Wow. It's everywhere. You really made a mess."
            Parker "Yeah. I guess I did. That's alright."
            "He takes a moment to clean up the cum and fix his clothes."
            Parker "Well, we should go."
            Jes "Yeah. We should."

            scene day9 ev07-41 with fade
            "The two settle in and get back on the road. After a short and slightly awkward ride, they pull up outside Jessica's building."
            Jes "Well, Mr. Parker, thank you for a wonderful evening."
            "She leans in, giving him a little peck right beside his lips."
            Parker "Jessica, someone might see!"
            Jes "It's dark. Besides, you deserve it after giving me such a wonderful night."
            Parker "Well, it was my pleasure, Jessica. That was the wildest thing I've done in a long time."
            Jes "That was the wildest thing I've {b}ever{/b} done. Anyway, have a good night, Mr. Parker."
            Parker "You too, Jessica."
            stop sound fadeout 1

            jump day09lateHome

label day09lonelyEvening:

    scene day9 ev08-01 with fade
    "With Conner out and not coming home anytime soon, Jessica watches some TV, then eventually settles onto the couch to read."
    "She flips through her reader for a few seconds, then spends some time reading a collection of philosophy articles from Jean-Paul Sartre."
    JesT "Hmm. \"If you are lonely when you are alone, you are in bad company\"."
    JesT "I must be particularly bad company."

    scene day9 ev08-02a with fade
    "The phone rings, bringing Jessica from her existential reverie."
    Jes "Heather, hey!"
    Heath "Hey, Jes. How you doing?"
    Jes "Alone and in bad company."
    Heath "Huh?"
    Jes "Nevermind. Conner's out late again. What are you up to?"
    Heath "Me and Christian were watching Wild Things."
    Jes "I never saw that one."
    Heath "Oh, it's great! We just watched this scene where these two girls are making out and getting naked."
    Heath "But there's this guy spying on them from the bushes."
    Jes "Eww."
    Heath "It's hotter than it looks. The guy didn't come to watch them fuck, but he's getting a show anyway. So naughty, watching people have sex like that. Like someone I know."

    scene day9 ev08-02b with dissolve
    "Jessica feels herself blushing and her heart beating faster."
    Heath "Anyway, we're about to have dinner. I was wondering if you wanted to join us."
    Jes "Oh, I already ate. Sorry."
    Heath "That's fine. Why not drop by in a half hour or so for a drink?"
    if "d07firstLesbian" in choices:
        "Jessica smiles, thinking of the warmth of Heather's lips."
    elif "d08chrisFlirt" in choices:
        "Jessica smiles, thinking of Christian's rugged, handsome smile."
    Jes "Sure. I'll see you in a bit, then."
    Heath "Alrighty! Just let yourself in when you get here. Just like before."
    "Jessica mumbles a bashful goodbye, then hangs up."

    scene day9 ev08-03 with fade
    "A short while later, Jessica strolls inside, both Christian and Heather waving at her."
    Jes "Hey, guys!"
    Heath "Hey, sweetie!"
    Chris "Evening, Jessica. You're looking good."
    Jes "Thank you."
    Chris "I was just grabbing a bottle of wine. Care for a glass?"
    Jes "Sure."

    if "d08chrisFlirt" in choices:
        scene day9 ev08-04
        "He moves closer, putting his arm around her waist and pulling her in."
        Chris "I'm happy you came by. Always a pleasure to have you over."
        "Jessica finds herself a little surprised, but chuckles."
        Jes "Always a pleasure to be had."
        JesT "Why the hell did I say that?!"

    scene day9 ev08-05
    "Jessica takes a seat next to Heather, the pair giving each other a quick kiss."
    Heath "Thanks for coming over, sweetie."
    Jes "Always happy to hang out with you guys."
    if "d07firstLesbian" in choices:
        JesT "God, she smells so good. Just like when we had sex."
        JesT "I want to kiss her so bad, but I should probably hold back in front of Christian."

    scene day9 ev08-06
    "The trio sit and chat for a little while, each sipping at their wine."
    "They discuss work and the general goings-on of their daily lives."
    Jes "And tonight I've just been sitting around feeling lonely."
    Heath "You're welcome over any time, Jes."

    scene day9 ev08-07
    "After a little while, Christian puts on a movie."
    "Despite being an alleged comedy, Jessica barely finds herself even chuckling."
    JesT "Wow, this movie sucks."

    if "d07firstLesbian" in choices:
        scene day9 ev08-08b
        "She takes off her shoes, then settles into a more comfortable position, hoping the movie will get better."
        Jes "Jennifer Aniston, naked dentist. Best part of the movie, so far."
        Chris "You don't hear me complaining."
        Heath "Ugh, I hate her. She's so perfect."
        "While she's watching, hoping for a joke, Jessica feels a gentle caress on her thigh."
        "She ignores it at first, until she realizes that it's Heather's foot, gently sliding back and forth."
        "Her stomach begins to feel all tingly."
        JesT "Heather, you are such a naughty girl! Your husband is right there!"
        JesT "It does feel nice, though, and it suddenly made this movie fun."

    else:
        scene day9 ev08-08
        "She takes off her shoes, then settles into a more comfortable position, hoping the movie will get better."
        Jes "Jennifer Aniston, naked dentist. Best part of the movie, so far."
        Chris "You don't hear me complaining."
        Heath "Ugh, I hate her. She's so perfect."

    scene day9 ev08-09
    "A short while later, Heather playfully taps on Jessica's shoulder."
    Heath "It's gotta be strange for you?"
    Jes "Hmm?"
    Heath "Coming in and finding us drinking on the couch instead of having sexy fun."
    Jes "Guh!"
    Chris "Wait. What's this now?"
    Heath "Yeah, she let herself in to get her phone back. I guess we didn't hear her knock cause you were… busy... at the time."
    Jes "I didn't mean to walk in on you two doing… that! If I had known, I would have knocked louder. And I really need my phone for work."
    "For a moment, Christian's face is shocked. Then he gives off a hearty laugh."
    Chris "So you saw me going down on her, huh?"
    Jes "Not intentionally!"
    if "d03dinnerSpy" in choices:
        JesT "I mean, I watched you two fuck intentionally, but he doesn't need to know that."
    Heath "I'm just sorry you didn't see the full show."
    if "d03dinnerSpy" in choices:
        JesT "Oh, but I did!"

    scene day9 ev08-10
    Heath "A pity you didn't follow us to the bedroom. When we make love, it's a thing of true beauty. Isn't that right, baby?"
    "As they talk, Heather reaches into Christian's pants."
    Chris "It really is."
    Heath "We could have put on one hell of a show for you."
    "Seeing what Heather's doing, Jessica turns away."

    scene day9 ev08-11a
    "Jessica shifts on the couch, unsure of how she should feel."
    "Heather keeps teasing her, gently rubbing her fingertips along Jessica's shoulder."
    Heath "Do you want to see what you missed last time?"
    "Her hand is moving all the while, clearly sliding back and forth along Christian's hidden manhood."
    if "d05heatherWatch" in choices:
        JesT "Wow. Does Heather think that because she watched Conner and me that I want to watch them?"
    elif "d053some" in choices:
        JesT "Wow. Do these two want a threesome? Was Conner right to be worried?"

    scene day9 ev08-11b with dissolve
    Jes "Look, why don't we just keep watching the movie."
    Heath "Nah, you're clearly bored. Jennifer Aniston is the only thing you've liked so far."
    Heath "Besides, the show we have in mind will be so much more fun."

    scene day9 ev08-12
    "Before Jessica can think or speak, Heather pulls out Christian's dick."
    "Her hand strokes slowly up and down, Jessica's breath catching in her throat."
    JesT "Okay, this is actually happening. Far more serious than I'd thought this was going to be."
    JesT "Not sure what I thought would happen, though. Both of them have been pretty shameless with me."
    JesT "I'm sure they'll put on one hell of a show, but I'm not sure if I should watch it. Should I stay?"

    menu:
        "Leave":
            JesT "No. No, this is way too awkward. I should go."
            if "d07firstLesbian" in choices:
                JesT "As much as I want to spend time with Heather, I don't really want to watch her play around with her husband."
            elif slut >= 20:
                JesT "It would be so hot to watch them, but our relationship is already complicated enough."
            else:
                JesT "It would be weird to watch them on my own. Maybe if Conner wanted to watch too, but not without him."

            scene day9 ev08-13
            "Slipping from the couch, Jessica grabs her shoes and phone."
            Jes "Um… I think I'm gonna head out."
            Heath "Really?"
            Jes "Yeah. It's late, I have work tomorrow. Um… thanks for the drink."
            Chris "Have a good night."

            scene day9 ev08-14 with fade
            "Jessica puts her shoes on and heads out. Heather follows her to the door."
            Heath "Hey. I'm sorry. I didn't mean to scare you off."


            if "d02hotRun" in choices:
                Heath "I mean… you weren't that shy a few nights ago. When we were together."
                Jes "You didn't scare me off. It was just different when it was the two of us."
                Heath "Ah. I get it. Um, look. I'm going to this fitness center tomorrow. Belongs to a client of mine."
                Heath "You want to join me? Just the two of us?"

                scene day9 ev08-15
                Jes "Sure. That sounds good. Gimme a call and let me know when to show up."
                Heath "I will. I hope you have a good night, sweetie."
                "Heather reaches up, barely stroking Jessica's cheek. Jessica smiles, happy to have a moment alone."
                Jes "I will."

                scene day9 ev08-16
                "Heather comes close, and for a moment Jessica considers the fact that the door is wide open and someone might see them."
                "As soon as their lips touch, all concerns melt away."
                "It's gentle, comforting, and exactly what she'd hoped for when she came over."
                "Heather smiles when it's done and waves goodbye."
                Heath "Sleep well, sweetie. I'll see you tomorrow."
                Jes "Good night."

            else:
                Heath "I just figured… you know. You weren't that shy some of the other nights we went out."
                Jes "It's not a problem. It just went to an awkward place, and I don't want our relationship to get weird. Especially since Conner isn't here."
                Heath "I understand. Have a good night, Jes."
                Jes "Good night, Heather."

            jump day09lateHome

        "Stay and watch them":
            $ choices.append("d09watchNeighbors")
            $ relHeather += 2
            $ relChristian += 2
            $ slut += 2
            JesT "Well… what the hell? Why not?"

            scene day9 ev08-20
            "Letting her inhibitions slink off, Jessica watches Heather's hand move up and down on Christian's dick."
            JesT "It's one hell of a sight."
            Jes "Sure. What the heck, right?"
            Heath "That's my girl."

    scene day9 ev08-21
    Heath "So, what do you want to see?"
    Jes "Huh?"
    Chris "Yeah. What would you like us to show you?"
    "Jessica is taken aback, having never been asked what kind of sex show she'd like."
    Jes "I guess… last time I was here he went down on you, Heather. So… why don't you go down on him?"
    Jes "If- if that's alright?"

    scene day9 ev08-22
    "Heather chuckles, amused either by the suggestion or by Jessica's hesitation."
    "She then slides to the other side of the couch with practiced ease, her hand never leaving her husband's cock, while he slipped his shorts off."
    Heath "Mmm, I do love pleasing my husband's beautiful cock. And it makes me happy to know it'll please you, too."
    "Her hand keeps going while she rubs her chin up and down, sliding her face along Christian's tip."

    scene day9 ev08-23
    "Both of them keep their eyes on Jessica all the while, watching her reactions."
    "She's keenly aware of Christian's eyes roaming up and down her body, and she's surprised just how arousing it is."
    "Her breathing quickens, her eyes locked with Heather's as her friend begins licking the rigid member in her hand."
    Heath "Mmm, he has the most delicious cock in the world."

    scene day9 ev08-24
    play voices x_bj_3 fadein 1 loop
    "Finally, her lips wrap around the rigid member, sucking hard while her head begins to bob up and down."
    JesT "Jesus, I can't believe I'm watching this!"
    JesT "I'm sitting on my friend's couch and watching her suck her husband's dick!"
    if "d05heatherWatch" in choices:
        JesT "Heather watched Conner and I, but it feels so weird when I'm the one watching."
    elif "d053some" in choices:
        JesT "Heather did join us for a threesome, but it feels so weird when I'm the one watching."
    elif slut >= 20:
        JesT "This is making me so fucking horny!"

    scene day9 ev08-25ani-00
    "Heather begins working her mouth up and down faster, watching Jessica out of the corner of her eye."
    show d09ev08-25ani
    Heath "Mmm."
    Chris "Baby, that's so good."
    JesT "It really is. Just beautiful."
    Jes "Gorgeous…"
    "Christian chuckles at the comment Jessica didn't even realize she spoke out loud."
    hide d09ev08-25ani
    JesT "I don't think I've ever seen more beautiful people making love."

    scene day9 ev08-26
    "Unconsciously, Jessica's hand slips between her thighs while her own loins burn with desire."
    "She imagines what his manhood must feel and taste like, and wonders how different he is from Conner."
    JesT "He's a bit smaller than Conner, but that's still plenty big. Heather's definitely a pro at this, taking all that in so easily."
    JesT "Maybe she could teach me a thing or two."

    scene day9 ev08-27
    "A heavy breath spills from Jessica's lips. It's almost a moan, but she manages to hold back."
    "Her sex begs to be touched, her fingers itch to satisfy her need, but she instead pushes her thighs tighter onto her hand."
    JesT "Don't act like such a slutty bitch, Jessica. Have some self control."
    JesT "Just because this is one of the most beautiful displays of spousal affection you've ever seen doesn't mean you should just start rubbing yourself."
    stop voices fadeout 1
    "While Jessica is holding herself back, Heather pulls her head up, licks her lips, and smiles at Christian."
    Heath "Let's show her a little more, eh dear?"

    scene day9 ev08-28 with fade
    "Without waiting for an answer, Heather stands and slips her clothing off. Without missing a beat, she's back on the couch, spreading her legs for Jessica."
    "Christian turns to his wife, his hands groping and caressing her naked body, all for the benefit of their guest."
    Chris "Not bad, huh?"
    Jes "Holy shit."
    Chris "Isn't she the most beautiful woman in the world?"
    if "d02hotRun" in choices:
        JesT "She really is gorgeous."

    scene day9 ev08-29
    play voices x_moaning_1 fadein 1 loop
    "Both of them continue to watch Jessica while Christian gently toys with Heather's sex."
    Heath "Mmm, he has magic fingers, Jess. I've never met a man who can touch me like he can."
    "Jessica nods, unable to tear her gaze away from the fingertips brushing over Heather's sopping wet cunt."
    Jes "Uh-huh."

    scene day9 ev08-30a
    "His fingers push her lips apart, gently working their way in. Heather leans back into him, eyes closing in pleasure."
    Heath "Oh yes."
    "He rolls the tips around in circles several times, drawing small squeals of delight from Heather, before he finally pushes them inside."

    scene day9 ev08-30b with dissolve
    Heath "Oh god!"
    "Heather's hips buck once before settling back down. She begins writhing slowly against Christian, mewls of delight slipping from her lips."
    Chris "Is that good, baby?"
    Heath "So good! Oh baby, keep going!"

    scene day9 ev08-31
    "Jessica's mouth remains open the whole time, amazed by the sight before her."
    "Even the moments she spied on them pale in comparison to the current spectacle."
    JesT "It's one thing watching them fuck, but I can't believe they're doing this when they know they're being watched."
    JesT "I'm on the same couch with them!"

    scene day9 ev08-32
    "She feels as if she's watching erotic art. Christian's hands move as if created to please women."
    "The sight of his fingers moving inside Heather makes her desperate to feel someone's hands inside her own sopping-wet womanhood."
    JesT "God, she must feel incredible. How she hasn't cum already is beyond me."
    stop voices fadeout 1

    scene day9 ev08-33 with fade
    "So enthralled is she that it takes a moment to register in her brain that Christian is moving Heather."
    "She watches, stunned, as he lays his wife in her lap."
    Jes "Whoa, what- what are you doing?"
    Heath "Relax, sweetie. He just wants to give you a better view."
    if "d07firstLesbian" in choices:
        "Jessica's heart beats faster feeling Heather's naked flesh against her legs."
        "She has to stop herself from bending over to kiss her lover."

    scene day9 ev08-34
    "Christian bends low and begins licking Heather. She moans in pleasure, watching intently along with Jessica."
    play voices x_moaning_1 fadein 1 loop
    Jes "Wow."
    Chris "Yeah baby. Just like that. Show Jessica what you can do with that tongue."

    scene day9 ev08-35
    "As if accepting her challenge, he begins licking her fervently."
    "His tongue works up one side of the labia, then the other, flicking her clit each time."
    Heath "That's good, baby. That's good."
    JesT "He really knows what he's doing."

    scene day9 ev08-36
    "Heather leans further back, moaning in joy."
    "Jessica continues to watch, still unable to believe what's happening."
    JesT "This feels like a dream. They're making love… on me. It's so surreal!"
    if "d07firstLesbian" in choices and "d08chrisFlirt" in choices:
        JesT "And Heather, you are so beautiful. I almost want to rip off my clothing and join in."
    elif "d07firstLesbian" in choices:
        JesT "And Heather, you are so beautiful. I want to make love to you so bad. Maybe next time we're alone."

    scene day9 ev08-37
    "Heather's moans grow into cries of ecstasy, her body bucking in pleasure as Christian continues to pleasure her."
    "Almost without thinking, Jessica reaches up to gently squeeze Heather's breast."
    play voices x_moaning_2 fadein 1 loop
    "A moment later, Heather screams in joy, her body tensing as she cums."
    Heath "Yes! God, yes!"
    "Christian keeps going all the while, Jessica watching, enraptured by the sight of Heather's moment of bliss."
    stop voices fadeout 2

    scene day9 ev08-38 with fade
    "For a few seconds after Heather finishes, the trio stay still, enjoying the moment together."
    "Then, before Jessica can say anything, Christian lifts Heather and pushes her back."
    "Jessica tries to move out of the way, but ends up pinned against the armrest, Heather sitting between her legs."
    Jes "Uh… this is a little awkward."
    Heath "You're fine, sweetie."
    "Figuring she might as well just go with the flow, Jessica puts her arm around Heather and watches as Christian lifts himself up and discards this shirt, ready to fuck his wife silly."

    scene day9 ev08-39
    play voices x_sex_2 fadein 1 loop
    "He pushes inside of her, Jessica watching in fascination as his cock disappears."
    Jes "He's so big. Does he hurt?"
    Heath "Sometimes, but it's a good kind of hurt."
    Jes "I'll bet. It's beautiful."
    "Christian just smiles, enjoying the two ladies talking about his dick, and begins thrusting into Heather."

    scene day9 ev08-40
    "His strokes are slow, steady, lifting toward the end. Heather moans with each and every thrust."
    Heath "Oh yes. That's good."
    "Christian begins grunting, clearly lost in the moment."
    "His body is tense and his muscles flexing, a sight to behold for Jessica."

    scene day9 ev08-41
    "The couple's faces are inches away as they make love, their eyes locked together."
    "Jessica can't help but appreciate being allowed to be part of such an intimate moment."
    JesT "It feels almost like I'm involved in this, especially with Heather's naked body pushing into me."
    play voices x_sex_3 fadein 1 loop
    if "d07firstLesbian" in choices:
        JesT "Any excuse to get this close to her is a good one."
    elif "d08chrisFlirt" in choices:
        JesT "I wonder what Christian's body would feel between my legs."

    scene day9 ev08-42
    "Swiftly, Christian's strokes become faster and harder. Jessica can feel Heather's body pushing into herself with greater power and speed."
    Heath "GOD, yes! That's so good!"
    Chris "Oh, it is!"
    "Heather's cries of joy grow louder, even as Christian speeds up further."

    scene day9 ev08-43
    Jes "Looks like he's getting close, Heather."
    Heath "Yes! Give it to me, baby!"
    "Her words push Christian even further, and soon he's ramming himself into her harder and harder!"
    "He leans in close, kissing Heather and speaking into her lips."

    scene day9 ev08-44ani-00
    Chris "Ah! You feel incredible!"
    show d09ev08-44ani
    "He's practically slamming himself into Heather at this point, her body rolling back into Jessica with each impact."
    "Jessica's open legs allow Heather's sweaty body to give her sex the tender touch she's been so desperately craving."
    "Heather continues to mewl in delight, crying out into her husband's mouth as he brings himself closer and closer to his inevitable orgasm."
    Chris "Ah! Yes! Almost there!"
    hide d09ev08-44ani
    "His groans become grunt, and with several more rapid thrusts he is finally ready to climax."
    play voices x_sex_5 fadein 1

    if "d07firstLesbian" in choices:
        scene day9 ev08-45a
        "The sights and sensations are too much for Jessica. Just as Christian climaxes, she pulls Heather's face back and plants a deep kiss on her lips."
        "Both ladies moan as they embrace, locked together in a moment of passionate, carnal lust."
        "Christian smiles, clearly enjoying the sight of his wife kissing another woman while he cums inside her."
        stop voices fadeout 2
        JesT "Wow. I feel so incredibly naughty."
        if slut >= 24:
            JesT "This is fantastic. I should let my neighbors fuck on top of me more often."

    elif "d08chrisFlirt" in choices:
        scene day9 ev08-45b
        "Just as Christian climaxes, he leans forward and plants a deep kiss on Jessica's lips."
        "The pair moan as they embrace, locked together in a moment of passionate, carnal lust."
        "Heather moans and rolls her head back into Jessica, clearly enjoying the sight of her husband kissing another woman while he cums inside her."
        stop voices fadeout 2
        JesT "Wow. I feel so incredibly naughty."
        if slut >= 24:
            JesT "This is fantastic. I should let my neighbors fuck on top of me more often."

    else:
        scene day9 ev08-45c
        "Just before he climaxes, Christian pulls out and sprays his seed all over his wife."
        "Thick ropes of cum land on her stomach, one of them even striking Jessica's hand."
        stop voices fadeout 2
        JesT "Oh wow! Look at it all! And it's so warm."
        "The sight of it makes her think about having to clean it off before she goes home, which makes her wonder if Conner is back yet."
        JesT "Oh crap. I should get going."

    scene day9 ev08-46
    "Jessica slips out from under Heather, grabbing her shirt and her phone."
    Jes "Guys, that was incredible, but I have to get back. Conner might be home by now."
    Heath "Really? So soon."
    Jes "Yeah. Sorry. That was awesome. Thanks for having me over. I'll, uh… I'll call you tomorrow, Heather. Bye."
    Chris "Bye. Thanks for coming."

    if "d02hotRun" in choices:
        scene day9 ev08-50
        "Just as Jessica gets to the door, Heather catches up to her, holding her shirt in front of her nudity."
        Heath "So, did you enjoy the show more than last time?"
        Jes "Oh yeah. That was… something else. Far more than I expected when I came over."
        Heath "Hey, I'm going to this fitness center tomorrow. Belongs to a client of mine."
        Heath "You want to join me? Just the two of us?"
        Jes "Sure. That sounds good. Gimme a call and let me know when to show up."

        scene day9 ev08-51
        Heath "I will. I hope you have a good night, sweetie."
        "Heather comes close, and for a moment Jessica considers the fact that the door is wide open and someone might see them."
        "As soon as their lips touch, all concerns melt away."
        "It's gentle, comforting, and exactly what she'd hoped for when she came over."
        "Heather smiles when it's done and waves goodbye."
        Heath "Sleep well, sweetie. I'll see you tomorrow."
        Jes "Good night."

    jump day09lateHome

label day09lateHome:

    if "d09dateParker" in choices:
        scene day9 ev09-01a with fade
        "Still thinking about Mr. Parker as she strolls in, Jessica checks her phone to find a few messages from Conner."

    else:
        scene day9 ev09-01b with fade
        "Still thinking about Heather and Christian as she strolls in, Jessica checks her phone to find a few messages from Conner."

    JesT "Oh crap. I must have muted my phone."
    JesT "He's wondering where I was. I hope he wasn't too worried."

    if "d09dateParker" in choices:
        scene day9 ev09-02a
    else:
        scene day9 ev09-02b
    "Walking into the living room, she finds Conner asleep on the couch."
    JesT "Huh. I guess he fell asleep waiting for me."
    JesT "He must be exhausted if he didn't wake up when I came in."

    if "d09dateParker" in choices:
        scene day9 ev09-03a with fade
    else:
        scene day9 ev09-03b with fade
    JesT "I'll just let him sleep here. No need to wake him."
    JesT "Besides, he can have a night on the couch for staying out so late."
    if "d09parkerShow" in choices or "d09watchNeighbors" in choices:
        JesT "Not that I've been a saint tonight."
    "Grabbing a blanket, Jessica drapes it over Conner. He doesn't even stir."

    if "d09dateParker" in choices:
        scene day9 ev09-04a
    else:
        scene day9 ev09-04b
    JesT "This sucks. He's finally back, but it feels like we never see each other."
    JesT "He runs off to do… whatever, and I'm out working."
    JesT "I thought I'd be so happy to have him back, but there's still this distance between us."
    if slut >= 24 or cheat >= 2:
        JesT "The weird part is… I'm not sure that I mind."
        JesT "I love him, but I can have fun without him."
        JesT "Maybe our time apart changed me. I used to want to spend every waking moment with him."
    else:
        JesT "I really miss spending time with him, even if it's just watching a movie together."
        JesT "I should talk to him about it soon."
    JesT "Oh, this is giving me a headache. I should just go to bed."

    if "d09dateParker" in choices:
        scene day9 ev09-05a with fade
    else:
        scene day9 ev09-05b with fade
    "After changing, she crawls into bed, mind still racing."

    if "d09parkerShow" in choices:
        JesT "Well, this has been one hell of an evening."
        JesT "Definitely one I won't ever forget."
        JesT "I had no idea how bold Mr. Parker could be. That was a sight to see… and it felt better than it should have."
    elif "d09watchNeighbors" in choices:
        JesT "Well, this has been one hell of an evening."
        JesT "Christian and Heather are incredible. I wouldn't mind being able to fuck like they do."
        JesT "Maybe I should bring a change of panties when I go over there. Just in case."
    else:
        JesT "Well, this was an interesting evening."

    "Exhausted, her mind eventually settles and she drifts off to sleep."

    jump day10
