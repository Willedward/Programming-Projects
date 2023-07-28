import random

#Words Collection
words = ["aback","abaft","abandoned","abashed","aberrant","abhorrent","abiding","abject","ablaze","able","abnormal","aboard","aboriginal","abortive","abounding","abrasive","abrupt","absent","absorbed","absorbing","abstracted","absurd","afterthought","aggressive","agonizing","agree","agreeable","agreement","ahead","air","airplane","airport","ajar","alarm","alcoholic","alert","alike","alive","alleged","allow","alluring","aloof","amazing","ambiguous","ambitious","bat","bath","bathe","battle","bawdy","bead","beam","bear","beautiful","bed","bedroom","beds","bee","beef","befitting","beg","beginner","behave","behavior","belief","believe","bell","belligerent","bells","belong","beneficial","bent","berry","berserk","best","better","bewildered","big","bike","bikes","billowy","bird","birds","calculator","calendar","call","callous","calm","camera","camp","can","cannon","canvas","cap","capable","capricious","caption","car","card","care","careful","careless","caring","carpenter","carriage","carry","cars","cart","carve","cast","cat","cats","cattle","cause","cautious","cave","ceaseless","contain","continue","control","cooing","cook","cool","cooperative","coordinated","copper","copy","corn","correct","cough","count","country","courageous","cover","cow","cowardly","cows","crabby","digestion","diligent","dime","dinner","dinosaurs","direction","direful","dirt","dirty","disagree","disagreeable","disappear","disapprove","disarm","disastrous","discover","discovery","discreet","discussion","disgusted","disgusting","disillusioned","dislike","dispensable","distance","distinct","distribution","disturbed","encouraging","end","endurable","energetic","engine","enjoy","enormous","enter","entertain","entertaining","enthusiastic","envious","equable","equal","erect","erratic","error","escape","ethereal","evanescent","evasive","even","event","examine","example","farm","fascinated","fast","fasten","fat","faulty","fax","fear","fearful","fearless","feeble","feeling","feigned","female","fence","fertile","festive","fetch","few","field","fierce","file","fill","film","filthy","fine","finger","finicky","fire","fireman","first","fish","fit","five","fix","furtive","future","futuristic","fuzzy","gabby","gainful","gamy","gaping","garrulous","gate","gather","gaudy","gaze","geese","general","gentle","ghost","giant","giants","giddy","gifted","gigantic","giraffe","girl","girls","glamorous","glass","gleaming","glib","glistening","glorious","glossy","glove","glow","glue","godly","gold","good","goofy","gorgeous","government","governor","grab","graceful","grade","grain","grandfather","habitual","hair","haircut","half","hall","hallowed","halting","hammer","hand","handle","hands","handsome","handsomely","handy","hang","hanging","hapless","happen","happy","harass","harbor","illegal","illustrious","imaginary","imagine","immense","imminent","impartial","imperfect","impolite","important","imported","impossible","impress","improve","impulse","incandescent","include","income","incompetent","inconclusive","increase","incredible","industrious","industry","inexpensive","infamous","influence","inform","inject","injure","ink","innate","innocent","inquisitive","insect","insidious","instinctive","instruct","instrument","insurance","intelligent","knowledge","knowledgeable","known","label","labored","laborer","lace","lackadaisical","lacking","ladybug","lake","lame","lamentable","lamp","land","language","languid","large","last","late","laugh","laughable","launch","lavish","lazy","lean","learn","lunch","lunchroom","lush","luxuriant","lying","lyrical","macabre","machine","macho","maddening","madly","magenta","magic","magical","magnificent","maid","mailbox","majestic","makeshift","male","malicious","mammoth","man","manage","maniacal","many","marble","march","mark","marked","market","married","marry","marvelous","mask","mass","massive","match","mate","material","materialistic","matter","mature","meal","mean","measly","measure","mute","mysterious","nail","naive","name","nappy","narrow","nasty","nation","natural","naughty","nauseating","near","neat","nebulous","necessary","neck","need","needle","needless","needy","neighborly","nerve","nervous","nest","new","next","nice","nifty","night","nimble","nine","nippy","nod","obsequious","observant","observation","observe","obsolete","obtain","obtainable","occur","ocean","oceanic","odd","offbeat","offend","offer","office","oil","old","old-fashioned","omniscient","one","onerous","open","opposite","optimal","orange","oranges","order","ordinary","organic","ossified","outgoing","outrageous","outstanding","oval","oven","overconfident","overflow","overjoyed","overrated","overt","overwrought","owe","own","pack","paddle","page","pail","painful","painstaking","paint","pale","paltry","pan","pancake","panicky","panoramic","pull","pump","pumped","punch","puncture","punish","punishment","puny","purple","purpose","purring","push","pushy","puzzled","puzzling","quack","quaint","quarrelsome","quarter","quartz","queen","question","questionable","queue","quick","quickest","quicksand","quiet","quill","quilt","quince","quirky","quiver","quixotic","quizzical","rabbit","rabbits","rabid","race","racial","radiate","ragged","rail","railway","rain","rainstorm","rainy","raise","rake","rambunctious","rampant","sack","sad","safe","sail","salt","salty","same","sand","sassy","satisfy","satisfying","save","savory","saw","scale","scandalous","scarce","scare","scarecrow","scared","scarf","scary","scatter","scattered","scene","scent","school","science","scientific","scintillating","sneaky","sneeze","sniff","snobbish","snore","snotty","snow","soak","soap","society","sock","soda","sofa","soft","soggy","solid","somber","son","song","songs","soothe","sophisticated","sordid","sore","sort","sound","soup","sour","space","spade","suffer","sugar","suggest","suggestion","suit","sulky","summer","sun","super","superb","superficial","supply","support","suppose","supreme","surprise","surround","suspect","suspend","swanky","sweater","sweet","sweltering","swift","swim","swing","switch","symptomatic","synonymous","system","table","taboo","tacit","tacky","tail","talented","talk","tall","tame","tan","tangible","tangy","tank","tap","tart","taste","tasteful","tasteless","tasty","tawdry","tax","tremendous","trick","tricky","trip","trite","trot","trouble","troubled","trousers","truck","trucks","truculent","true","trust","truthful","try","tub","tug","tumble","turkey","turn","twig","twist","two","type","typical","ubiquitous","ugliest","ugly","ultra","umbrella","unable","unaccountable","unadvised","unarmed","unbecoming","unbiased","uncle","uncovered","understood","underwear","undesirable","undress","unequal","unequaled","uneven","unfasten","unhealthy","uninterested","unique","unit","unite","unkempt","unknown","unlock","unnatural","unpack","unruly","unsightly","unsuitable","untidy","unused","unusual","unwieldy","unwritten","upbeat","uppity","upset","uptight","use","used","useful","useless","utopian","utter","uttermost","vacation","vacuous","vagabond","vague","valuable","value","van","vanish","various","vase","vast","vegetable","veil","vein","vengeful","venomous","verdant","verse","wiggly","wild","wilderness","willing","wind","window","windy","wine","wing","wink","winter","wipe","wire","wiry","wise","wish","wistful","witty","wobble","woebegone","woman","womanly","women","wonder","wonderful","wood","wooden","wool","woozy","word","work","workable","worm","worried","worry","worthless","wound","wrap","wrathful","wreck","wren","wrench","wrestle","wretched","wriggle","wrist","writer","writing","wrong","wry","x-ray","yak","yam","yard","yarn","yawn","year","yell","yellow","yielding","yoke","young","youthful","yummy","zany","zealous","zebra","zephyr","zesty","zinc","zip","zipper","zippy","zonked","zoo","zoom"]

#Get Word
def valid_word(words):
    word = random.choice(words)
    
    while " " in word or "-" in word or len(word)<5 or len(word)>9:
        word = random.choice(words)
    return word.upper()

#Introduction
print("Welcome to The Hangman Game!!!")
print("This is a game for convicted criminals to redeem their crimes.")
print("Here are the rules: \n 1. The number of lives you will have is the length of the word + 3 additional lives. \n 2. The words you will be guessing has a minimum length of 5 alphabets and maximum length of 9 alphabets.\n 3. Guess ALL the words correctly.\nNOTICE : If you fail, there will be no second chances!")
ready = input("Are you ready? (press [y] to begin): ")
while ready != "y":
    ready = input("Are you ready? (press [y] to begin): ")
if ready == "y":
    print("Let The Games Begin")
    print()


word = valid_word(words)

#initiating blankspace
current_word = "-"*len(word)
blankspace = list(current_word)

#Hangman Game
def hangman(word):
    lives = len(word) + 3
    store = ""
    print("Word: " + "-"*len(word))
    while lives != 0:
        user_input = input("Enter a Letter: ").upper()
        n = 0
        if user_input in word:
            for i in range(0, len(word)):
                if user_input == word[i]:
                    blankspace[i] = word[i]
                    n = 1               
        if n == 1:
            print("The letter {} is in the word.".format(user_input))
        elif n == 0:
            print("The letter {} is not in the word.".format(user_input))
        lives = lives - 1
        store = store + user_input + " "
        xy = " ".join(blankspace)
        print("You have {} lives left".format(lives))
        print("You have used these letters: " + store)
        print("The current word is " + xy)
        print()
    if xy.split(" ") == word:
        print("Congratulations!!! Your freedom awaits you!")
        print("The word is " + word)
    elif xy.split(" ") != word:
        print("You Lose! Get ready to for the punishment!!!")
        print("The right answer is", word)

        
print(hangman(word))




