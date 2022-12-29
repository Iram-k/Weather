import webbrowser
data1=input("Country :")
data2=input("City :")
print("Hold on Sir, I will show you weather condition of " + data2 + " in Country"+data1+".")
webbrowser.open("https://www.timeanddate.com/weather/"+data1+"/"+data2 )

