def text_caesar (text: str, shift: int) -> str:
    alphabet_lower = 'qwertyuioplkjhgfdsazxcvbnm'
    alphabet_upper = alphabet_lower.upper ()
    
    ord_first_litter_lower = ord ('a')
    ord_first_litter_upper = ord ('A') 
   
    new_text = '' 
    
    for i in text:
        if i in alphabet_lower:
            new_text += chr (((ord (i) + shift) - ord_first_litter_upper + shift) % 25 + ord_first_litter_lower) 
        elif i in alphabet_upper:
            new_text += chr (((ord (i) + shift) - ord_first_litter_upper + shift) % 25 + ord_first_litter_upper)
        else:
            new_text += i 
   
    return new_text
  
  
def decrypt_text_caesar (text: str, shift: int) -> str:
    return text_caesar (text, -shift) 
    
if __name__ == '__main__':
    print (text_caesar ('HEllo bro', 1))
