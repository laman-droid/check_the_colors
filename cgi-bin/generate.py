import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()

read = open("colornames.csv", encoding="utf8")
colors_list = read.read()
colors_list = colors_list.lower()

submitted_value = form["submitted-color"].value

submitted_value = submitted_value.lower()

print("Content-Type: text/html")
print()
if submitted_value in colors_list:
    print(f"{submitted_value} is a color!")
else:
    print(f"{submitted_value} is not a color!")






