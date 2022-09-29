import importlib

def print_result(test_nb, succes_boolean):
    test_string = 'Test ' + str(test_nb)+':'
    if succes_boolean:
        print(test_string, 'correct')
    else:
        print(test_string, 'foutief')

def test_gebruiker_toevoegen(bvp):
    # Test 1
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Lucas")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Patsy")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Julie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Peter")
        succes = bvp.is_gebruiker(netwerk, "Griet") == False
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)
    # Test 2
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Lucas")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Patsy")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Julie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Peter")
        succes = bvp.is_gebruiker(netwerk, "Lucas") == True
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(2, succes)
    # Test 3
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Lucas")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Patsy")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Julie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Peter")
        succes = bvp.is_gebruiker(netwerk, "Marie") == True
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(3, succes)

def test_vriendschap_toevoegen(bvp):
    # Test 1
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Lucas")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Patsy")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Julie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Peter")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Emma")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Kevin")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Tobias")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Suzy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Marie", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Marie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Patsy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Kevin")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Emma")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Julie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Suzy", "Tobias")
        succes = bvp.is_vriend_met(netwerk, "Lucas", "Emma") == True
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)
    # Test 2
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Lucas")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Patsy")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Julie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Peter")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Emma")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Kevin")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Tobias")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Suzy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Marie", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Marie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Patsy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Kevin")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Emma")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Julie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Suzy", "Tobias")
        succes = bvp.is_vriend_met(netwerk, "Lucas", "Kevin") == False
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(2, succes)
    # Test 3
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Lucas")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Patsy")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Julie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Peter")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Emma")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Kevin")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Tobias")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Suzy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Marie", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Marie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Patsy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Kevin")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Emma")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Julie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Suzy", "Tobias")
        succes = bvp.is_vriend_met(netwerk, "Suzy", "Emma") == False
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(3, succes)
    # Test 4
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Lucas")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Patsy")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Julie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Peter")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Emma")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Kevin")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Tobias")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Suzy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Marie", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Marie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Patsy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Kevin")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Emma")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Julie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Suzy", "Tobias")
        succes = bvp.is_vriend_met(netwerk, "Suzy", "Frank") == False
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(4, succes)

def test_geef_populariteits_lijst(bvp):
    # Test 1
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Lucas")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Patsy")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Julie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Peter")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Emma")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Kevin")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Tobias")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Suzy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Marie", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Marie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Patsy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Kevin")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Emma")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Julie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Suzy", "Tobias")
        lijst = bvp.geef_populariteits_lijst(netwerk)
        # Lucas – Emma – Peter – Julie – Kevin – Marie – Patsy – Suzy – Tobias
        succes = lijst[0] == "Lucas" and lijst[1] == "Emma" and lijst[2] == "Peter" and lijst[3] == "Julie" and lijst[4] == "Kevin" and lijst[5] == "Marie" and lijst[6] == "Patsy" and lijst[7] == "Suzy" and lijst[8] == "Tobias"
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)

def test_is_bijna_vriend_met(bvp):
    # Test 1
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Lucas")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Patsy")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Julie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Peter")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Emma")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Kevin")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Tobias")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Suzy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Marie", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Marie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Patsy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Kevin")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Emma")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Julie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Suzy", "Tobias")
        succes = bvp.is_bijna_vriend_met(netwerk, "Lucas", "Emma") == False
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)
    # Test 2
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Lucas")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Patsy")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Julie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Peter")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Emma")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Kevin")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Tobias")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Suzy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Marie", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Marie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Patsy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Kevin")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Emma")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Julie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Suzy", "Tobias")
        succes = bvp.is_bijna_vriend_met(netwerk, "Lucas", "Kevin") == True
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(2, succes)
    # Test 3
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Lucas")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Patsy")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Julie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Peter")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Emma")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Kevin")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Tobias")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Suzy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Marie", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Marie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Patsy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Kevin")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Emma")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Julie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Suzy", "Tobias")
        succes = bvp.is_bijna_vriend_met(netwerk, "Suzy", "Emma") == False
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(3, succes)
    # Test 4
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Lucas")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Patsy")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Julie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Peter")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Emma")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Kevin")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Tobias")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Suzy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Marie", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Marie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Patsy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Kevin")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Emma")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Julie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Suzy", "Tobias")
        succes = bvp.is_bijna_vriend_met(netwerk, "Suzy", "Frank") == False
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(4, succes)

def test_is_via_vriendschappen_verbonden_met(bvp):
    # Test 1
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Lucas")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Patsy")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Julie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Peter")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Emma")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Kevin")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Tobias")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Suzy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Marie", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Marie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Patsy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Kevin")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Emma")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Julie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Suzy", "Tobias")
        succes = bvp.is_via_vriendschappen_verbonden_met(netwerk, "Lucas", "Emma") == True
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)
    # Test 2
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Lucas")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Patsy")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Julie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Peter")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Emma")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Kevin")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Tobias")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Suzy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Marie", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Marie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Patsy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Kevin")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Emma")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Julie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Suzy", "Tobias")
        succes = bvp.is_via_vriendschappen_verbonden_met(netwerk, "Marie", "Julie") == True
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(2, succes)
    # Test 3
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Lucas")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Patsy")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Julie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Peter")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Emma")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Kevin")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Tobias")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Suzy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Marie", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Marie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Patsy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Kevin")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Emma")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Julie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Suzy", "Tobias")
        succes = bvp.is_via_vriendschappen_verbonden_met(netwerk, "Julie", "Tobias") == False
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(3, succes)
    # Test 4
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Marie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Lucas")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Patsy")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Julie")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Peter")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Emma")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Kevin")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Tobias")
        netwerk = bvp.voeg_persoon_toe(netwerk, "Suzy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Marie", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Marie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Lucas", "Patsy")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Emma", "Kevin")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Emma")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Lucas")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Peter", "Julie")
        netwerk = bvp.voeg_vriendschap_toe(netwerk, "Suzy", "Tobias")
        succes = bvp.is_via_vriendschappen_verbonden_met(netwerk, "Julie", "Frank") == False
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(4, succes)

def run_all_tests():
    bvp = importlib.import_module('bvp-practicum2')
    print('###')
    print('Testen voor functie voeg_persoon_toe en is_gebruiker:')
    test_gebruiker_toevoegen(bvp)
    print('###')
    print('Testen voor functie voeg_vriendschap_toe en is_vriend_met:')
    test_vriendschap_toevoegen(bvp)
    print('###')
    print('Testen voor functie geef_populariteits_lijst:')
    test_geef_populariteits_lijst(bvp)
    print('###')
    print('Testen voor functie is_bijna_vriend_met:')
    test_is_bijna_vriend_met(bvp)
    print('###')
    print('Testen voor functie is_via_vriendschappen_verbonden_met:')
    test_is_via_vriendschappen_verbonden_met(bvp)
    print('###')

def main():
    run_all_tests()

if __name__ == "__main__":
    main()