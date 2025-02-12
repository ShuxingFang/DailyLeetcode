from solutions.check_if_palindrome import check_if_palindrome

def test_check_if_palindrome():
    assert check_if_palindrome("racecar") == True
    assert check_if_palindrome("hello") == False
    assert check_if_palindrome("a") == True
    assert check_if_palindrome("") == True