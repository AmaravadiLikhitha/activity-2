import re
def check_url(ip_url):
# Regular expression for URL
    re_exp = ("((http|https)://)(www.)?" + "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" + "{2,6}\\b([-a-zA-Z0-9@:%" + "._\\+~#?&//=]*)")
    exp = re.compile(re_exp)
    if (ip_url == None):
        print("Input string is empty")
    if(re.search(exp, ip_url)):
        print("URL is valid!")
    else:
        print(" URL is invalid!")
ip_url = input("Enter the URL: ")
check_url(ip_url)