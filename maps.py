import webbrowser

address = input("Enter your address:")


list_address = list(address)
new_list = ["+" if x == " " else x for x in list_address]
new_address = (''.join(new_list))
link = "https://www.google.com/maps/search/" + new_address
webbrowser.open(link)