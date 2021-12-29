import webbrowser
n=input()

link=(f"https://www.amazon.in/s?k={n}&crid=3NZ0OBGAO995C&sprefix=ardu%2Caps%2C756&ref=nb_sb_noss_2")
link2=(f"https://www.flipkart.com/search?q={n}&sid=6bo%2Cjdy%2Cdus&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=ssd+internal+hard+drive%7CInternal+Hard+Drive&requestId=a3d078bd-c99c-47af-8316-9da98370e781&as-searchtext=ssd")
webbrowser.open(link)
webbrowser.open(link2)
