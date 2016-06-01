#-------------------------------------------------------------------------------
#
# The purpose of this file is to exercise some Python via basic cryptology.
#
# This program automatically execute a unit test to ensure valid results.
#
#-------------------------------------------------------------------------------

DEBUG_OUTPUT_ENABLED = False

def xor_generate_matching_length_key(text, key):

    if DEBUG_OUTPUT_ENABLED:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("XOR Generating Matching Length Key...")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    longKey = ""
    keyIterator = 0
    for i in range( len(text) ):
        longKey += key[keyIterator]
        keyIterator += 1
        if keyIterator >= len(key):
            keyIterator = 0

    if DEBUG_OUTPUT_ENABLED:
        print("encryption target string: ", text)
        print("encryption target string length: ", len(text))
        print("extended encryption key string: ", longKey)
        print("extended encryption key length: ", len(longKey))
    
    return longKey

def xor_characters_with_key(targetText, matchingLengthKey):

    if DEBUG_OUTPUT_ENABLED:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Starting XOR iteration on characters...")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    processedCharacters = ""
    for i in range(len(matchingLengthKey)):
        processedCharacters += chr( ord(targetText[i]) ^ ord(matchingLengthKey[i]) )

    return processedCharacters

def xor_encrypt(text, key):

    if DEBUG_OUTPUT_ENABLED:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Starting to XOR Encrypt Text:")
        print( text )
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    matchingLengthKey = xor_generate_matching_length_key(text, key)

    return xor_characters_with_key(text, matchingLengthKey)

def xor_decrypt(text, key):

    if DEBUG_OUTPUT_ENABLED:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Starting to XOR Decrypt Text...")
        print( text )
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    matchingLengthKey = xor_generate_matching_length_key(text, key)

    return xor_characters_with_key(matchingLengthKey, text)

def run_unit_test():
    testText = "01234"
    testKey = "asde"

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Running encrypt decrypt unit test...")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    encryptedTextResult = xor_encrypt( testText, testKey )
    decryptedTextResult = xor_decrypt( encryptedTextResult, testKey )
    print("testText: \t\t", testText)
    print("testKey: \t\t", testKey)
    print("encryptedTextResult: \t", encryptedTextResult)
    print("decryptedTextResult: \t", decryptedTextResult)
    conditionOne_PASSED = False
    conditionTwo_PASSED = False

    if encryptedTextResult == "QBVVU":
        conditionOne_PASSED = True
    if decryptedTextResult == "01234":
        conditionTwo_PASSED = True

    if conditionOne_PASSED and conditionTwo_PASSED:
        print( "\n TEST SUCCESSFULL, ENCRYPT AND DECRYPT RESULTS LOGICAL \n" )

run_unit_test()
