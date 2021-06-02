def check_article(noun):
    if noun.startswith(("a", "e", "i", "o", "u")):
        return "an"
    else:
        return "a"

def user_inputs(word):
    return input("Enter "+check_article(word) + " " + word + ": ")

if 'name':
    pet_name = user_inputs('name')


prt = ("Every summer I get totally amped and "+user_inputs('adjetive')+" to go camping in the deep "+user_inputs('adjetive')+" forrests. ")
prt += ("It's good to get away from it all - but not too away, like in getting lost! ")
prt += ("Last year, my friends and I went hiking and got lost for "+user_inputs('number')+" hours. ")
prt += ("We started off on "+user_inputs('ending "ing" adjetive')+" adventure, but we kept losing the trail. ")
prt += ("Night began to fall, and when we heard the howls of a "+user_inputs('large animal')+" we began to panic. ")
prt += ("It was getting darker and our flashlights were running of "+user_inputs('noun')+ ". ")
prt += ("I'm so glad my pet "+user_inputs('animal')+ " " + user_inputs('name')+" was with us. ")
prt += ("He is one gifted creature, because he was able to guide us back by "+user_inputs('ending "ing" action verb')+" the "+user_inputs('adjetive')+ " s'mores by the campfire. ")
prt += ("This year, before setting off on "+user_inputs('ending "ing" adjetive')+" journey, I'll be sure to have working flashlights - and of course, my buddy "+pet_name+"!")

print(prt)




