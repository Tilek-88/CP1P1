def string_length(word):
    return len(word)
    
#write your code here...
#DO NOT remove lines below here, this is designed to test your code.
def test_string_length():
    assert string_length('hello!') == 6
    assert string_length('banana') == 6
    assert string_length('8') == 1
    assert string_length('funnyguys') == 9
    assert string_length('101') == 3
    print("YOUR CODE IS CORRECT!")
#test your code by un-commenting the line(s) below
test_string_length()