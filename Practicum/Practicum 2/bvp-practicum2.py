#########################################################################
# Enkele functies voor het aanmaken en invullen van de datastructuur
#########################################################################

def creeer_leeg_netwerk():
    dictionary = {}
    return dictionary

# deze functie creeert een lege data-structuur, d.w.z. een initiële
# data-structuur, zonder gegevens over personen en vriendschapsrelaties

# en geeft die data-structuur als return-waarde terug

def voeg_persoon_toe(sn, naam_persoon):
    if naam_persoon not in sn:
        sn[naam_persoon] = set()
    return sn


# deze functie voegt aan de data-structuur ‘sn' (afkorting van ‘social network’)

# de informatie toe over de persoon naam_persoon; deze functie geeft als return-
# waarde de aangepaste datastructuur terug; als een persoon met dezelfde naam eerder
# al werd toegevoegd, dan mag deze persoon geen 2e maal worden toegevoegd


def voeg_vriendschap_toe(sn, naam_persoon1, naam_persoon2):
    if naam_persoon1 in sn and naam_persoon2 in sn:
        sn[naam_persoon1].add(naam_persoon2)
        sn[naam_persoon2].add(naam_persoon1)
    return sn

# als beide personen al in het netwerk werden toegevoegd, dan voegt deze functie

# aan de datastructuur toe dat deze 2 personen een

# vriendschapsrelatie met elkaar hebben; als één of beide personen niet in

# het netwerk voorkomen, dan verandert de datastructuur gewoonweg niet;

# als tussen beide personen eerder al een vriendschapsrelatie werd toegevoegd, mag dat

# geen 2e maal worden toegevoegd;

# deze functie geeft als return-waarde de (eventueel aangepaste) datastructuur terug


#########################################################################
# Twee functies voor eenvoudige vragen aan de datastructuur
#########################################################################


def is_gebruiker(sn, naam_persoon):
    if naam_persoon in sn:
        return True
    else:
        return False

# deze functie geeft een boolean als return-waarde die aangeeft of de person

# met deze naam al in het netwerk ‘sn’ was toegevoegd


def is_vriend_met(sn, naam_persoon1, naam_persoon2):
    if naam_persoon1 in sn and naam_persoon2 in sn:
        if naam_persoon1 in sn[naam_persoon2]:
            return True
        else:
            return False
    else:
        return False


# deze functie geeft een boolean als return-waarde die aangeeft of beide personen

# in social network ‘sn’ via een vriendschapsrelatie verbonden zijn; hou hier dus

# rekening met wederkerigheid: als eerder een vriendschap tussen persoon 2 en

# persoon 1 werd toegevoegd, dan geldt dat ook persoon 1 vriend is met persoon 2;

# deze functie mag er niet vanuit gaan dat beide personen in het netwerk zijn

# opgenomen; indien één of beide personen niet in het netwerk zijn opgenomen

# geeft de functie uiteraard false als resultaat


#########################################################################
# Enkele meer geavanceerde functies die de datastructuur ondervragen
#########################################################################

def geef_populariteits_lijst(sn):
    popularity_list = {}
    popularity_numbers = []
    for key in sn:
        popularity_list[key] = len(sn[key])
        popularity_numbers.append(len(sn[key]))

    popularity_numbers = sorted(popularity_numbers,reverse = True)
    popularity_people = sorted(popularity_list)

    new_list = []
    for number in popularity_numbers:
        counter = 0
        while counter < len(popularity_people):
            key = popularity_people[counter]
            if number == popularity_list[key]:
                new_list.append(key)
                popularity_people.remove(key)
                counter = len(popularity_people)
            counter += 1
    return new_list




# deze functie geeft een lijst van namen als return-waarde die gesorteerd is

# op basis van het aantal vriendschapsrelaties dat de personen hebben; personen die

# evenveel vriendschappen hebben worden hierbij alfabetisch gesorteerd


def is_bijna_vriend_met(sn, naam_persoon1, naam_persoon2):
    if naam_persoon1 in sn and naam_persoon2 in sn:
        if len(sn[naam_persoon1].intersection({naam_persoon2})) > 0:
            return False
        else:
            return len(sn[naam_persoon1].intersection(sn[naam_persoon2])) > 0
    else:
        return False

# deze functie geeft een boolean als return-waarde die ‘true’ teruggeeft als beide

# personen via 1 tussenschakel met elkaar bevriend zijn – dus als er een 3e persoon

# bestaat die zowel met persoon 1 als persoon 2 bevriend is; als beide personen

# rechtstreeks bevriend zijn, of als er niet zo’n 3e gemeenschappelijke vriend

# bestaat, dan moet deze functie false teruggeven;

# deze functie mag er niet vanuit gaan dat beide personen in het netwerk zijn

# opgenomen; indien één of beide personen niet in het netwerk zijn opgenomen

# geeft de functie uiteraard false als resultaat

def is_via_vriendschappen_verbonden_met(sn, naam_persoon1, naam_persoon2):
    if naam_persoon1 in sn and naam_persoon2 in sn:
        friends_pool_persoon = set()
        to_be_checked_pool = {naam_persoon1}
        prev_len_pool_persoon = -1
        while len(friends_pool_persoon) > prev_len_pool_persoon:
            prev_len_pool_persoon = len(friends_pool_persoon)
            new_to_be_checked_pool = set()
            for friend in to_be_checked_pool:
                friends_pool_persoon.add(friend)
                new_to_be_checked_pool = new_to_be_checked_pool.union(sn[friend])
            to_be_checked_pool = new_to_be_checked_pool
            to_be_checked_pool = to_be_checked_pool.difference(friends_pool_persoon)

            if naam_persoon2 in friends_pool_persoon:
                return True

        return False
    else:
        return False


# deze functie geeft een boolean als return-waarde die ‘true’ teruggeeft als beide

# personen rechtstreeks of via een aantal tussenpersonen door vriendschapsrelaties

# verbonden zijn; dus bv. als persoon 1 vriend is met persoon 3, die vriend is met

# persoon 4, die op haar beurt vriend is met persoon 2, dan zeggen we dat persoon 1

# ‘via vriendschappen verbonden is met’ persoon 2.

# deze functie mag er niet vanuit gaan dat beide personen in het netwerk zijn

# opgenomen; indien één of beide personen niet in het netwerk zijn opgenomen

# geeft de functie uiteraard false als resultaat


#############################################################################
# Hieronder vind je 1 voorbeeld van een hoofdprogramma. Dit pas je uiteraard
# aan om je programma te testen, en wordt op zich niet verbeterd.

# Van dit voorbeeldje zie je hieronder ook een schematische voorstelling.
#############################################################################

def main():
    netwerk = creeer_leeg_netwerk()

    netwerk = voeg_persoon_toe(netwerk, "Marie")
    netwerk = voeg_persoon_toe(netwerk, "Marie")
    netwerk = voeg_persoon_toe(netwerk, "Lucas")
    netwerk = voeg_persoon_toe(netwerk, "Patsy")
    netwerk = voeg_persoon_toe(netwerk, "Julie")
    netwerk = voeg_persoon_toe(netwerk, "Peter")
    netwerk = voeg_persoon_toe(netwerk, "Emma")
    netwerk = voeg_persoon_toe(netwerk, "Kevin")
    netwerk = voeg_persoon_toe(netwerk, "Tobias")
    netwerk = voeg_persoon_toe(netwerk, "Suzy")

    netwerk = voeg_vriendschap_toe(netwerk, "Marie", "Lucas")

    netwerk = voeg_vriendschap_toe(netwerk, "Lucas", "Marie")
    netwerk = voeg_vriendschap_toe(netwerk, "Lucas", "Patsy")
    netwerk = voeg_vriendschap_toe(netwerk, "Emma", "Lucas")
    netwerk = voeg_vriendschap_toe(netwerk, "Emma", "Kevin")
    netwerk = voeg_vriendschap_toe(netwerk, "Peter", "Emma")
    netwerk = voeg_vriendschap_toe(netwerk, "Peter", "Lucas")
    netwerk = voeg_vriendschap_toe(netwerk, "Peter", "Julie")

    netwerk = voeg_vriendschap_toe(netwerk, "Suzy", "Tobias")

    print(is_gebruiker(netwerk, "Griet") )  # false

    print(is_gebruiker(netwerk, "Lucas") )  # true

    print(is_vriend_met(netwerk, "Lucas", "Emma") )  # true

    print(is_vriend_met(netwerk, "Lucas", "Kevin") )  # false

    print(is_vriend_met(netwerk, "Suzy", "Emma") )  # false

    print(is_vriend_met(netwerk, "Suzy", "Frank") )  # false

    print(is_bijna_vriend_met(netwerk, "Lucas", "Emma") )  # false

    print(is_bijna_vriend_met(netwerk, "Lucas", "Kevin") )  # true

    print(is_bijna_vriend_met(netwerk, "Suzy", "Emma") )  # false

    print(is_bijna_vriend_met(netwerk, "Suzy", "Frank") )  # false

    print(is_via_vriendschappen_verbonden_met(netwerk, "Lucas", "Emma") )  # true

    print(is_via_vriendschappen_verbonden_met(netwerk, "Marie", "Julie"))  # true

    print(is_via_vriendschappen_verbonden_met(netwerk, "Julie", "Tobias") )  # false

    print(is_via_vriendschappen_verbonden_met(netwerk, "Julie", "Frank") )  # false

    print(geef_populariteits_lijst(netwerk))



    # Lucas – Emma – Peter – Julie – Kevin – Marie – Patsy – Suzy – Tobias

    # (Lucas heeft 4 vrienden, Emma en Peter elk 3, de anderen hebben elk 1 vriend)


#########################################################################
# Gebruik zeker onderstaande lijnen om je eigen hoofdprogramma op te
# starten.
#########################################################################

if __name__ == "__main__":
    main()
