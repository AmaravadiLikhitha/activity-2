import re 
while True :
  input_code=input("ënter your country code:")
  valid_code=False
  if(len(input_code)<2 or len(input_code)>3):
    print("int valid! total digits should be between 2-3 in country code")
    continue 
  elif not re.search("[+]",input_code):
    print("not valid![+] should exist in phone number")
    continue 
  else:
    valid_code=True
    break
if(valid_code==True):
  while True:
    num=input("enter a mobile number:")
    pattern=re.compile("[7-9][0-9]{9}")
    if pattern.match(num):
      print("valid mobile number")
      break
    else:
      print("invalid mobile number")

