def check_maximum_palindromes_length(input_string : str) -> int:
    max_length_palindrome = ""

    for index, character in enumerate(input_string):
        max_length_palindrome = max(
            max_length_palindrome, 
            check_palindrome_non_recursive(f"{character}", index-1, index+1, input_string), 
            key=len)
        max_length_palindrome = max(
            max_length_palindrome, 
            check_palindrome_non_recursive("", index-1, index, input_string), 
            key=len)

    return max_length_palindrome

def check_palindrome(current_palindrome, index_left, index_right, input_string):
    if index_left < 0 or index_right >=  len(input_string):
        return current_palindrome
    if input_string[index_left] == input_string[index_right]:
        current_palindrome = f"{input_string[index_left]}{current_palindrome}{input_string[index_right]}"
        current_palindrome = check_palindrome(
            current_palindrome, index_left-1, index_right+1, input_string
        )
        return current_palindrome
    else:
        return current_palindrome

def check_palindrome_non_recursive(current_palindrome, index_left, index_right, input_string):
    while index_left >= 0 and index_right < len(input_string):
        if (char_left:=input_string[index_left]) == (char_right:=input_string[index_right]):
            current_palindrome = f"{char_left}{current_palindrome}{char_right}"
            index_left-=1
            index_right+=1
        else:
            break
    return current_palindrome
    