define A = Character("Aria")
define S = Character("Sam")
define AD = Character("Aria’s dad")
define AM = Character("Aria’s mom")
define SD = Character("Sam’s dad")
define BGU = Character("???")

image aria supprised = "aria_supprised.png"
image aria smiling = "aria_smiling.png"
image aria = "aria.png"
#image open_chest = "openchest.png"


label start:


    scene bg_forest_landscape2

    BGU "Quickly! After her!"
    "Aria runs as fast as she can through the woods desperately trying to stay ahead of the men chasing her."
    "She sees a clearing in the woods ahead."
    "As she gets to the clearing suddenly her footing is lost. In front of her is a cliff over a lake."
    label first_choice:
    menu the_cliff:
        "What should I do?"
        "I could try jumping and swimming ashore. The fall is too big I might not make it!":
            jump jump_and_swim
        "Or I could stand and fight I might be able to get the upper hand.":
            jump stand_and_fight
    
    label stand_and_fight:
    "Aria decides to fight."
    "Aria manages a swift kick on the first man to approach her but the others surround and grab her. "
    show aria_supprised at right
    "Violent murder happens maybe some blood sqleching sounds and a scream *YOU DEAD BITCH*"
    "Game Over"
    return
    
    label jump_and_swim:
    show aria_supprised at right
    "Aria decides to jump."
    show aria_supprised at right
    "Aria crashes into the lake"
    "Aria is finding it hard to keep going, She feels like all the energy is zapped out of her."
    hide aria_supprised
    "She needs to power through and continue. She needs to get to safety and find out why this all happened."
    "Aria swims to shore and catches her breath. "
    scene bg_forest_landscape1
    "After a brief rest Aria continues on."
    show aria
    "She moves though the forest at a slower pace, looking out for her pursuers."
    "Aria comes to a road and sees a car passing by."
    hide aria
    "She waves frantically for help."
    show aria_supprised at right
    A "Help!"
    "As the vehicle comes to a stop her pursuers catch up to her."
    hide aria_supprised
    show aria
    "Aria notices the man in the vehicle looks familiar."
    "The truck screeches to a halt."
    hide aria
    #scene bg_truck_stops
    show aria at right
    show sam at left #I need a sprite for Sam
    BGU "Do you need help?"
    A "Yes please there are people after me."
    BGU "Well as sketch as that sounds get in."
    "The man unlocks the truck door."
    "Aria gets in the truck."
    "They drive off quickly."
    #scene bg_truck_driving_in_woods
    BGU "So Aria? What are you doing here?"
    A "Ye, yes….. do I know you?"
    hide aria
    show aria_supprised at right
    "The tires screech as the man suddenly stops the truck."
    hide aria_supprised
    show aria_confused at right #I need a confused sprite for Aria
    BGU "…….. You really don’t remember me?"
    A "I mean you seem familiar but no. Sorry?"
    BGU "…….ugh I can’t believe you."
    S "Sam.…..You remember we used to play together as kids?"
    A "Sam!? Really!? What are you doing I thought you wanted to go live the city life?"
    "Sam starts the truck again."
    S "Yeah that's me. Still is but I got some business to take care of."
    S "I should be the one asking you the questions though."
    S "What is going on? Why were those people chasing you?"
    A "I’m not sure. I think they want this though..."
    "Aria pull out a chest"
    A "Grams left it for me. It was the last thing she gave me before….."
    S "I’m sorry for your loss."
    A "Thanks…. I don’t know what to do now."
    S "I know what I would do..."
    "Sam looks at the box."
    A "I’m not sure. Whatever it is may not be valuable but those guys certainly wanted it."
    S "Won’t know till we look? Will we?"
    A "Yeah but I’m not sure it is worth the risk. Maybe I should just chuck it and skip town?"
    S "That’s one option or we could go to the police?"
    S "Or here’s a thought..."
    S "open it?"

    label choice_open_the_box:
    menu open_the_box:
        "What should I do?"
        "Leave the chest and skip town.":
            jump options2_choice1
        "Go to the cops":
            jump options2_choice2
        "Open the box":
            jump options2_choice3
    
    label options2_choice1:
    label options2_choice2:
    label options2_choice3:
    A "Yeah you are right Let's open it."
    "Aria opens the chest"
    #show open_chest #need a sprite for this
    "Inside is a branch."
    "Aria picks it up."
    A "Well they must be mistaken. This couldn’t have any value could it?"
    "Sam glances over and slams on the breaks"
    A "Again!? can’t you drive?"
    "Sam looks at the branch like he just realized something was missing."
    S "I’m not sure what this is all about..."
    S "But I have a feeling I know where that goes."
    A "It goes to a tree….?"
    S "Yes a tree of course it goes to a tree; but Not just any TREE!"
    "Sam pulls out a map"
    S "This tree!"
    "Sam points at a crude drawing of a branch and an x"
    A "What is this? Where did you get this?"
    S "My dad gave it to me before I left for college."
    S "He said it would be better off far away from here."
    A "I don’t get it! Why all the mystery who cares about some branch and a tree."
    S "I’m not sure but I think that's what your granny wanted you to find out."
    S "I was actually coming back into town to see her. I got a letter from her just the other day."
    A "You couldn’t have!"
    A "There is no way..."
    A "She past away a month ago!"
    S "So you’re saying someone was pretending to be her?"
    A "I don’t know, but I don’t think its a coincidence."
    S "Well I’m sure the end of this map will have some clue."
    A "I hope you are right so we can get out of this nightmare!"

#Wes's part
    label second_to_last_choice:
    menu Past_or_future: 
        "What should I do?"
        "I could give up. It might be our only way out of this. If he keeps his word.":
            jump Give_up
        "He is close. It's risky but I just might be able to get to him before he can fire!":
            jump FIGHT 
        "I could try to go back. Maybe I can find a solution to this!":
            jump Go_back_to_the_past
        "I don't understand this fully! Maybe I should see what happens if I grab the sappling?":
            jump Go_to_the_future

    label Give_up: 
            A ".....Fine....You win I'll come out!"
            BGU ".....Glad you could see reason. Believe me I didn't want things to go this far hon."
            A "...Just get him help!"
            "Aria grabs the branch off the tree"
            "It snaps off"
            "The roots around begin to open up"
            "BG and his goons are waiting"
            "Aria hands the branch to BG"
            "BG's men go to help Sam"
            BGU "We are going to make the world a better place Aria. You will see."
            "In the following months Aria hears constant head lines of BG. BG the hero, BG the billionaire."
            "Aria herself has a hefty sum given to her from anonymous donors"
            "Sam succemed to his wounds. Aria is still dealing with the guilt. She feels responsible."
            "Aria's memeory of her parents is unchanged. She fears she will never see them again"
            "Over time Aria began to notice many changes though out the records of history. Discriptions, paintings and stories all describing BG"
            
            "Game Over!"
            return
    label FIGHT:
            "Aria rips the branch off the tree"
            A "I'll give it right to you then!!"
            "The roots recede and the world opens up"
            "Aria sees BG and a couple of his goons"
            A "Here it is!!"
            "Aria charges at BG branch in hand"
            BGU "STOP!!"
            "BANG BANG BANG!"
            "Aria feels hot in her chest, stomach and shoulder but that doesn't slow her down."
            "She reaches BG at last and slams the sharp end right into his neck!"
            BGU "UGH.....ugh....Ariaaghhh"
            A "HERE IT IS!"
            "Aria feels exhausted as she notices her wounds."
            "She screams and pushes the branch as far as it will go!"
            "BG Falls over dead."
            "The goons look at Aria covred in blood and flee."
            "Aria unable to stand any longer collapses."
            A "....Sa....Sam...Looks..like..it..all ends with us."
            "The light fades from Aria's eyes."
            "The wolrd may never know of their sacrifices. The timelines are safe only for as long as the mysteries of the tree remain undiscovered."

            "Game Over!"
            return
    label Go_back_to_the_past: 
            A ".....I have all the time in the world BG!"
            A "Hang on Sam! I'll get you help!"
            BGU "Aria!! You can't win!"
            A "...heh we will see about that"
            " Aria heads back to the tree and grabs the old withered branch."
            "She hears BG, and the gunshots again"
            "Aria jumps through"
            "Aria sees herself and sam"
            BGU "Well maybe... let's see if you can use it! *cocking his gun*"
            "BANG BANG BANG!"
            A "..Sam!"
            A "Sam!"
            "Aria looks over and sees Aria by the tree."
            A "Aria snap out of it! I'll take care of Sam! You go back and stop this!"
            "Aria pauses for only a moment then with a nod is back in the past"
            "Aria comes back with another Aria!"
            "Both Aria's: 'We couldn't stop him! Sam still got shot?"
            A "Go back again!"
            "They both go back"
            BGU "What's goin on in there Aria!?"
            "A flash of light"
            "Even more Aria's"
            "Aria's We are back!"
            A "How did it go?"
            "Aria 1: Well in my timeline I was going to stab him with the branch but this Aria pulled me in!"
            "Aria 2: I didn't pull you in! That was her!"
            "Aria 3: Yeah!"
            "Aria 4: It doesn't matter! Did any of our plans work?"
            "All 4 Aria's: No."
            A "We have to try again! Go back!"
            BGU "I must be hearing things in there"
            "All Aria's: Shut up!"
            "The Aria's go back"
            "Another flash and even more Aria's"
            A "How many now?"
            "There's 8 of us!"
            "Aria sitting behind the crowd : Nine of us!"
            A "So were we able to figure this out?"
            "Aria 1: I think we can save Sam! We brought supplies!"
            "Aria 9: I've been through this so many times.... I don't care anymore"
            A "Okay. Aria 1 and 2 you tend to Sam"
            A "All the rest of you. Get ready!"
            A "I'll stay here in case we have to go back again"
            A "We are going to make it this time!"
            "Aria 9: Ive seen it all before... I'll just sit this out"
            A "Enough! We can do this!"
            "Each Aria grabs a root"
            "The roots open up"
            "Aria's charge BG"
            BGU "What! WAH Wha ARIA!"
            "He attempts to fire but before he can get a shot off he is overwhelmed."
            BGU "Stop! Please...ugh...Agh"
            "BG is beaten to an absolute plup"
            "Aria 9: Wait we did it this time?"
            "Aria 9: HAHA...HA..HA!! Finally!"
            "She jumps to life and grabs one of the chainsaws"
            "Aria 9: Payback Time!!"
            "She revs it and chases after the two henchmen who are shocked beyound belief"
            "Aria 1: We stopped the bleeding! Sam's going to make it!"
            S "Ughh Aria?"
            "He sees all 10 Aria's"
            S "What? Is this heaven?"
            "Aria 1: Oh sam. *blushingly*"
            "Aria 2: Relax Sam. We are going to get you help!"
            A "We did it! We won."
            BGU "....ugh...You can still be a hero"
            BGU "We can still do so much good!"
            BGU "You see. You know now you can use it!"
            A "This was reckless. I didn't have any other choice"
            BGU "You think this is over!?"
            BGU "I've done too much to give up now!"
            "BG reaches for his gun"
            "He is stopped by the other Arias"
            BGU "I'll never give up!"
            BGU "ARIA!!"
            BGU "You'll just have to kill me!"
            "Aria 1: Well that is an option."
            "Aria 2: We could turn him in as well"
            "Aria 3: Yeah no one will believe his crazy rants. We could get him committed."
            "Aria 3: Plus with Sam's injuries we have plenty of evidence."
            "Aria 1: Wait. Which one of us is the original?"
            "Aria 2: Me."
            "Aria 1: No. I brought you here!"
            A "It's me. I'm the first one to go back in the past. I think."
            "Aria 1: Okay. So. I think you should make the choice."
            A "Okay...."
            label Kill_Commit:
                menu K_C:
                    "What are we going to do with BG?"
                    "He won't stop coming for this. No matter what. We need to kill him.":
                        jump Kill
                    "We can't let him get away with this. However killing him isn't right.":
                        jump Commit
                        label Kill:
                            A "He's too dangerous to keep around."
                            BGU "You can't be serious Aria baby! C'mon I was like family to you!"
                            "Aria 1: This is how you treat family?"
                            "Aria 1 picks up his gun and shoot him"
                            BGU "ughhhh"
                            "Aria 1 unloads the rest of the magazine into him"
                            A "It's finally over!"
                            "Aria 9: Not yet! This timeline is safe but we still have to save each of our lines"
                            "They bury BG and the Aria of this timeline gets Sam to the hospital."
                            "They return to each timeline and do the same."
                            "Exhausted having beat BG for the last time. Each Aria returns to their own timeline."

                            "A few days later"
                            "S is still in his hospital bed"
                            "Aria walks in"
                            S "So which one are you?"
                            A "I'm just Aria. The only one still here."
                            S "So I missed a lot what happened?"
                            A "BG won't be a problem anymore."
                            jump Ending_C_choice 

                        label Commit: 
                            A "He's too dangerous to keep around."
                            A "We can't just kill him, but We need to make sure he is no longer a threat."
                            A "I'll bring Sam to the hospital and BG to the authorities"
                            "Aria 1: If thats what you think is best."
                            BGU "You can't be serious Aria baby! C'mon I was like family to you!"
                            "Aria 1: This is how you treat family?"
                            "Aria 1 kicks him while the rest come to tie him up"
                            A "It's finally over!"
                            "Aria 9: Not yet! This timeline is safe but we still have to save each of our lines."
                            "The Aria of this timeline gets Sam to the hospital and BG to the authorities."
                            "They return to each timeline and do the same."
                            "Exhausted having beat BG for the last time. Each Aria returns to their own timeline."

                            "A few days later"
                            "S is still in his hospital bed"
                            "Aria walks in"
                            S "So which one are you?"
                            A "I'm just Aria. The only one still here."
                            S "So I missed a lot what happened?"
                            A "BG was sent to a clinic for the criminally insane."
                            jump Ending_C_choice

                            label Ending_C_choice:
                                S "So we are finally safe?"
                                A "For now yes."
                                A "If we stay safe however. If the world stays safe. That's up to us."
                                S "Okay. Yeah. This is playing with fire. Someones going to get burned"
                                S "So. I guess we have a few options"
                                S "We can keep the map and branch separate like our parents did."
                                S "Or we can burn it to the ground."
                                A "You forgot option number 3."
                                S "Option 3?"
                                A "We can use it!"
                                S "Aria you can't be serious!? After what we just went through?"
                                A "BG did have a point. A lot of good can be done with this power."
                                A "We could do a lot of good out there in the world."
                                A "I've been in the past a few times now. I think I'm getting the hang of this."
                                S "Aria!"
                                A "It's too big for just one of us to decide. We have to agree on this."
                                A "If you say no that will be the end of it!"
                                A "Sam this has impacted our lives too much! However some good can still come from it if we care careful."
                                A "Whatever you decide Sam, I'll go with!"
                                menu C_last_Choice: 
                                    "Can we keep the timeline safe?"
                                    "This is too dangerous Aria. We have to burn it!":
                                        jump Burn_It
                                    "Aria. This is too much for either of us. We should split this up":
                                        jump Seperate
                                    "Aria. Where to first?":
                                        jump Use_it

                                        label Burn_It: 
                                        S "Aria. Lets burn this down. It's too dangerous!"
                                        A "Okay Sam"
                                        "Days later when Sam is released the two head back to the tree"
                                        "They ignite the flames"
                                        "They watch as the tree burns"
                                        "The flames seem to glow in a magnificent light"
                                        "As the flames die down the light from the tree fades"
                                        "By the end nothing is left but ash"
                                        A "It's finally over."
                                        S "Yeah. What are you going to do now?"
                                        A "I feel like I've had enough adventure for now."
                                        A "What about you? Are you going back home?"
                                        S "Maybe I'll stick around this time."
                                        A "That would be nice."
                                        "Though this may have been the end of their adventure. Their lives together may just be begining"
                                        "Game over."
                                        return
                                        label Seperate: 
                                        S "Aria. This isn't so simple. I don't think either of us can make this decision."
                                        S "For now I think it's best we split everything up. We can go on living our lives."
                                        A "Okay Sam."
                                        "Days later when Sam is released"
                                        A "All set?"
                                        S "Yeah. I'm ready to get back home"
                                        A "I'll keep my half safe. Don't worry about me. Take care of yourself Sam."
                                        S "I will Aria. I don't plan on getting shot again!"
                                        A "ha ha. Don't joke around like that!"
                                        S "See you around Aria."
                                        A "Bye Sam."
                                        "Aria and Sam had said their goodbyes. They agreed to keep everything seperate and secret. They took the secrets to their graves."
                                        return
                                        label Use_it:
                                        S "Aria. Where to first."
                                        A "Sam....You mean it?"
                                        "Days later when Sam is released the two head back to the tree."
                                        S "So should we stop a plauge? Evacuate a town? Prevent a War?"
                                        A "Lets start with something small Sam. We will get there evetually."
                                        S "Baby steps. Got it."
                                        A "Shall we go? *Extending her hand to Sam"
                                        S "Lets go."
                                        "This was just the start of the many adventures for the two. History books soon changed. There have been many photographs, paintings and stories of a couple of unknown heros throughtout time."
                                        "Game Over."
                                        return
    label Go_to_the_future:
        A "…...I have all the time in the world BG!"
        A "Hang on Sam! I’ll get you help!"
        BGU "Aria!! You can’t win!"
        A "….heh we will see"
        "Aria heads back to the tree"
        "She grabs the Young sapling."
        "Colors fly all around her" 
        "She holds on for what seems to be years."
        "Eventually She feels a pull"
        "Aria are yanked to the ground." 
        "She takes a moment and observes her surroundings."
        "This is still the tree but no Sam and no BG in sight." 
        "Aria notices a man standing there in strange attire."
        "???: So when are you coming from?"
        A "I .. (year)"
        "???: Wow no way!"
        "???: This is Pivotal! Oh I shouldn’t say much this is just too exciting."
        "???: What’s your name?"
        A "Aria... and you?"
        "???: No way!! Aria! Oh I can’t tell you my name. Who knows what could happen!"
        "???: This is rich! Okay I can’t say anything about the future because it might have lasting effects on the past. But I can say is that this current course of action works!"
        A "Okay but I need help!"
        "???: OH I KNOW Trust me I’ve heard this story so many times."
        A "you...have?"
        "??? Ahhh can’t say anymore. I have to take you back now!"
        A "You know how to use this?"
        "??? Of course only the best taught me."
        A "Okay can you help me my friend he’s injured!"
        "???: Sure not for long though."
        "???: Come on"
        "The man Grabs Aria’s hand and rips through a portal"
        "Before Aria can realize it she is back in her own timeline"
        "???: Oh okay."
        BGU "Aria!! COME ON OUT!"
        "???: Psh this guy again!?"
        "The man walks over to Sam with what looks like a shot and a cream
        He puts a cream on Sams wounds and injects him with a substance"
        "Sam screams but his wound is healing!"
        A "Sam!"
        "??? That’s one part taken care of….Now for our friends."
        "The man rips off the branch the roots all fall down"
        BGU "Who are you?"
        "The man doesn’t say a word but all you see is a bright flash"
        "BG falls to the ground instantly"
        "His goons run away at the sight but soon after they fall as well."
        A "What happened?"
        "???: Can’t say sorry. I’m sure you will know some day though *winks*"
        "???: Okay so looks like this timeline is set!"
        "???: I can’t say much more, but it was good seeing you Grams!"
        A "GRAMS!?"
        "*The man looks embarrassed*"
        "???:Oh I mean I’m from the future remember. So everyone from this time is like a granny to me."
        "???: I gotta go before I mess anything else up."
        "???: Just keep this old thing protected will ya?"
        "???: With another flash the man is gone along with BG’s body and the henchmen."
        A "I can’t believe what I just saw"
        jump Ending_D 

        label Ending_D: 
                "A few days later"
                "S is still in his hospital bed"
                "Aria walks in"
                A "Sam! Are you feeling any better?"
                S "I'll make it"
                S "So I get the feeling I missed a lot. What happened?"
                A "BG won't be a problem anymore."
                A "I don't know if you would believe the rest"
                S "So we are finally safe?"
                A "For now yes."
                A "If we stay safe however. If the world stays safe. That's up to us."
                S "Okay. Yeah. This is playing with fire. Someones going to get burned"
                S "So. I guess we have a few options"
                S "We can keep the map and branch separate like our parents did."
                S "Or we can burn it to the ground."
                A "You forgot a few options."
                S "Whats that?"
                A "Well we could keep it around. No need to go our separate ways or burn anything."
                A "We just watch it nurture it and safe guard it together."
                A "It's too valuable to destory but too dangerous to leave alone."
                A "Or..... We can use it!"
                S "Aria you can't be serious!? After what we just went through?"
                A "BG did have a point. A lot of good can be done with this power."
                A "We could do a lot of good out there in the world."
                A "I've been in the past a few times now. I think I'm getting the hang of this."
                S "Aria!"
                A "It's too big for just one of us to decide. We have to agree on this."
                A "If you say no that will be the end of it!"
                A "Sam this has impacted our lives too much! However some good can still come from it if we care careful."
                A "Whatever you decide Sam, I'll go with!"
                menu D_last_Choice: 
                        "Can we keep the timeline safe?"
                        "This is too dangerous Aria. We have to burn it!":
                            jump Burn_It2
                        "Aria. This is too much for either of us. We should split this up":
                            jump Seperate2
                        "Aria. Where to first?":
                            jump Use_it2
                        "We can take care of this together Aria.":
                            jump nurture

                            label Burn_It2: 
                                S "Aria. Lets burn this down. It's too dangerous!"
                                A "Okay Sam"
                                "Days later when Sam is released the two head back to the tree"
                                "They ignite the flames"
                                "They watch as the tree burns"
                                "The flames seem to glow in a magnificent light"
                                "As the flames die down the light from the tree fades"
                                "By the end nothing is left but ash"
                                A "It's finally over."
                                S "Yeah. What are you going to do now?"
                                A "I feel like I've had enough adventure for now."
                                A "What about you? Are you going back home?"
                                S "Maybe I'll stick around this time."
                                A "That would be nice."
                                "Though this may have been the end of their adventure. Their lives together may just be begining"
                                "Game over."
                                return
                            label Seperate2: 
                                S "Aria. This isn't so simple. I don't think either of us can make this decision."
                                S "For now I think it's best we split everything up. We can go on living our lives."
                                A "Okay Sam."
                                "Days later when Sam is released"
                                A "All set?"
                                S "Yeah. I'm ready to get back home"
                                A "I'll keep my half safe. Don't worry about me. Take care of yourself Sam."
                                S "I will Aria. I don't plan on getting shot again!"
                                A "ha ha. Don't joke around like that!"
                                S "See you around Aria."
                                A "Bye Sam."
                                "Aria and Sam had said their goodbyes. They agreed to keep everything seperate and secret. They took the secrets to their graves."
                                return
                            label Use_it2:
                                S "Aria. Where to first."
                                A "Sam....You mean it?"
                                "Days later when Sam is released the two head back to the tree."
                                S "So should we stop a plauge? Evacuate a town? Prevent a War?"
                                A "Lets start with something small Sam. We will get there evetually."
                                S "Baby steps. Got it."
                                A "Shall we go? *Extending her hand to Sam"
                                S "Lets go."
                                "This was just the start of the many adventures for the two. History books soon changed. There have been many photographs, paintings and stories of a couple of unknown heros throughtout time."
                                "Game Over."
                                return               
                            label nurture: 
                                S "Aria. We can take care of this together!"
                                A "Sam are you sure? It's not going to be easy!"
                                S "Aria. I know with you at my side we can make it!"
                                A "Oh Sam. Okay. Together."
                                "Sam stayed in town with Aria. Together the two protected the tree. Protected histroy together. As well as generations after." 





    return
