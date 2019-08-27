import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_excl = pd.read_csv('Saham_EXCL.csv', index_col=False, parse_dates=['Tanggal'])
df_excl.set_index('Tanggal', inplace=True)
df_excl.sort_index(inplace=True)

df_fren = pd.read_csv('Saham_FREN.csv', index_col=False, parse_dates=['Tanggal'])
df_fren.set_index('Tanggal', inplace=True)
df_fren.sort_index(inplace=True)

df_isat = pd.read_csv('Saham_ISAT.csv', index_col=False, parse_dates=['Tanggal'])
df_isat.set_index('Tanggal', inplace=True)
df_isat.sort_index(inplace=True)

df_tlkm = pd.read_csv('Saham_TLKM.csv', index_col=False, parse_dates=['Tanggal'])
df_tlkm.set_index('Tanggal', inplace=True)
df_tlkm.sort_index(inplace=True)


# plt.style.use('seaborn')
plt.style.use('seaborn')
plt.plot(df_excl.index,  df_excl['Close'], 'green')
plt.plot(df_fren.index,  df_fren['Close'], 'cyan')
plt.plot(df_isat.index,  df_isat['Close'], 'blue')
plt.plot(df_tlkm.index,  df_tlkm['Close'], 'red')
plt.title('Harga Historis Saham 2016-2019', fontdict={'fontsize':'22'}, pad=40)
plt.legend(['PT XL Axiata Tbk','PT XL Smartfren Telecom Tbk','PT Indosat Tbk','PT XL Telekomuniasi Indonesia Tbk'], loc='upper center', bbox_to_anchor=(0.5, 1.06), ncol=4)
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')
plt.subplots_adjust(bottom=0.16, top=0.85)
plt.xticks(rotation=30)
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator(
    interval=3))

plt.show()