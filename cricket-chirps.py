import pandas as pd
import matplotlib.pyplot as plt


#Read the text as a CSV file with commas as seperators i.e sep=','. Note single quotes for sep arghument
#The text file has no header so the DataFrame created will have columns "chirps" and"temp"
df=pd.read_csv("C:\data\cricket_chirps_versus_temperature.txt", sep=',', header=None, names=["chirps","temp"])


#Plot cricket chirps versus temperature
df.plot(x="temp",y="chirps",kind="scatter",title="Cricket Chirps Vs. Temperature")

plt.show()

#Also save the data in a csv file for future use
df.to_csv("C:\data\cricket_chirps_versus_temperature.csv")
df.to_excel("C:\data\cricket_chirps_versus_temperature.xls")#creating so many errors
df.to_html("C:\data\cricket_chirps_versus_temperature.html")
df.to_latex("C:\data\cricket_chirps_versus_temperature.latex")
