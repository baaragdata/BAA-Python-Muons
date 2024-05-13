import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import webbrowser

print(pd.__version__)

df = pd.read_csv('data1.txt', sep=' ', skiprows=6)

# print(df.head(10))

# print(df.columns)

# print(df['Temp'])

# print('Mean =', df['Temp'].mean())

# print('Mean = {:.2f}'.format(df['Temp'].mean()))



# print(df[['Time_el', 'mV']])    


y1 = df['mV']
y2 = df['mV'].rolling(window=12).mean()
x = df['Time_el'] / 1000

fig = plt.figure(figsize = (16,6))

plt.scatter(x, y1, label='SiPM(mV)', marker='.')
plt.plot(x, y2, label='Rolling Mean - 12 point window', color='red')

plt.xlabel('Elapsed Time (s)')
plt.ylabel('SiPM(mV)')
plt.title('Elapsed Time vs SiPM(mV)')
plt.grid(True)
plt.legend()
# save plt as png file
plt.savefig('simple_plot.png')

#plt.show()

HtmlStr = mpld3.fig_to_html(fig)

with open('index.html', 'w') as html_file:
    html_file.write(HtmlStr)
    
webbrowser.open('index.html', new=2)

print('Done!')












