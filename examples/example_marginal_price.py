# This is a sample Python script.
import datetime as dt
from OMIEData.DataImport.omie_marginalprice_importer import OMIEMarginalPriceFileImporter

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    import matplotlib.pyplot as plt
    from OMIEData.Enums.all_enums import DataTypeInMarginalPriceFile

    # download the files
    wantedDate = dt.datetime(2025, 10, 1)

    # This can take time, it is downloading the files from the website.
    df = OMIEMarginalPriceFileImporter(date_ini=wantedDate, date_end=wantedDate).read_to_dataframe(verbose=True)
    df.sort_values(by='DATE', axis=0, inplace=True)
    print(df)

    # Just portugal prices
    str_price_portugal = str(DataTypeInMarginalPriceFile.PRICE_PORTUGAL)
    dfPrices = df[df.CONCEPT == str_price_portugal]

    plt.figure(figsize=(19.2, 10.8))
    plt.plot(dfPrices.T[2:].index, dfPrices.T[2:][1], label='Price')
    plt.xticks(rotation=90)  # Rotates x-axis tick labels to vertical
    plt.tight_layout()
    plt.legend()
    plt.show()
