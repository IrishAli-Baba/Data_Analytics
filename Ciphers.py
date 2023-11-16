coded_message = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'

def alphabetter():
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  alphabet_list = []
  for letter in alphabet:
    alphabet_list.append(letter)
  return alphabet_list,alphabet

def decode_message(message, offset, en_de):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  alphabet_list = []
  for letter in alphabet:
    alphabet_list.append(letter)
    decoded_message = ''
  for letter in message:
    if letter in alphabet:
      index = alphabet.find(letter)
      if not en_de:
        decoded_message = decoded_message + alphabet_list[(index+offset)%len(alphabet_list)]
      else:
        decoded_message = decoded_message + alphabet_list[(index-offset)%len(alphabet_list)]
    else:
      decoded_message = decoded_message + letter
  return(decoded_message)


vishal_brute = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
index = 0
for letter in range(26):
  de = decode_message(vishal_brute,letter,0)
  index += 1
  #print(index)
  #print(de)

def vig_decode(message,keyword):
  alpha = alphabetter()[1]
  alpha_list = alphabetter()[0]
  index = 0
  decoded_message = ''
  for letter in message:
    if letter in alpha:
      keyword_index = index%len(keyword)
      index +=1
      letter_to_shift = alpha.find(letter)
      shift = alpha.find(keyword[keyword_index])
      shifted_letter = alpha_list[(letter_to_shift+shift)%len(alpha_list)]
      decoded_message = decoded_message + shifted_letter
    else:
      decoded_message = decoded_message + letter
  return(decoded_message)

def vig_encode(message,keyword):
  alpha = alphabetter()[1]
  alpha_list = alphabetter()[0]
  index = 0
  encoded_message = ''
  for letter in message:
    if letter in alpha:
      keyword_index = index%len(keyword)
      index +=1
      letter_to_shift = alpha.find(letter)
      shift = alpha.find(keyword[keyword_index])
      shifted_letter = alpha_list[(letter_to_shift-shift)%len(alpha_list)]
      encoded_message = encoded_message + shifted_letter
    else:
      encoded_message = encoded_message + letter
  return(encoded_message)

decoded = vig_decode("txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!","friends")
re_encoded = vig_encode(decoded,"friends")
print(decoded, re_encoded)
