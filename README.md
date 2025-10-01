# OMIEData_Oct25: 

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI version fury.io](https://img.shields.io/pypi/v/OMIEData.svg)](https://pypi.org/project/OMIEData/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/OMIEData.svg)](https://www.python.org/)

Since October 2025, the original package OMIEData from which this is forked has become obsolete for obtaining 
daily market prices since the data source changed from hourly to a quarter-hourly format. 
This fork, OMIEData_Oct25, is adapted to the new data source and structure, although being only  
adapted to download the OMIE marginal prices. Other functionalities will not be added in the future.
Note: OMIE (Iberian Peninsula's Electricity Market Operator): https://www.omie.es/

Concretely, you can easily access to data for the following markets:

- Daily market: hourly prices in Spain and Portugal.


## Installation 

To install the package, just type in the command line:

```python
python -m pip install git+https://github.com/RicardoEGFSilva/OMIEData_Oct25

```

in the command line. 

## Examples:

A very simple example to download the hourly electricity prices for a given date:

```python
import datetime as dt
import matplotlib.pyplot as plt

from OMIEData.DataImport.omie_marginalprice_importer import OMIEMarginalPriceFileImporter
from OMIEData.Enums.all_enums import DataTypeInMarginalPriceFile

# Set the wanted date, from 2025-10-01 onwards.
wantedDate = dt.datetime(2025, 10, 1)

# This can take time for longer date spans, since it is downloading the files from the website.
df = OMIEMarginalPriceFileImporter(date_ini=wantedDate, date_end=wantedDate).read_to_dataframe(verbose=True)
df.sort_values(by='DATE', axis=0, inplace=True)
print(df)

# Filter the dataframe to consider just portugal prices.
str_price_portugal = str(DataTypeInMarginalPriceFile.PRICE_PORTUGAL)
dfPrices = df[df.CONCEPT == str_price_portugal]

# Plot the prices.
plt.figure(figsize=(19.2, 10.8))
plt.plot(dfPrices.T[2:].index, dfPrices.T[2:][1], label='Price')
plt.xticks(rotation=90)
plt.tight_layout()
plt.legend()
plt.show()
```
The code will generate a data-frame like the following one:

```python
         DATE   CONCEPT   H1Q1    H1Q2  ...  H25Q1  H25Q2  H25Q3  H25Q4
0  2025-10-01  PRICE_SP  105.1  104.24  ...    NaN    NaN    NaN    NaN
1  2025-10-01  PRICE_PT  105.1  104.24  ...    NaN    NaN    NaN    NaN
[2 rows x 102 columns]
```

The plot will look like this:
![alt text](https://github.com/RicardoEGFSilva/OMIEData_Oct25/tree/dev/images/PricesPT_1Oct25.png)