import datetime as dt
import pandas as pd
import numpy as np

from OMIEData.DataImport.omie_marginalprice_importer import OMIEMarginalPriceFileImporter


def test_marginal_price_downloader_after_october25_24h():
    # Set the wanted date.
    wantedDate = dt.datetime(2025, 10, 1)

    # This can take time for longer date spans, since it is downloading the files from the website.
    df = OMIEMarginalPriceFileImporter(date_ini=wantedDate, date_end=wantedDate).read_to_dataframe(verbose=True)
    wantedDf = pd.DataFrame([
        {
            'DATE': wantedDate.date(),  'CONCEPT': 'PRICE_SP',
            'H1Q1': 105.1,      'H1Q2': 104.24,     'H1Q3': 102.28,     'H1Q4': 102.0,
            'H2Q1': 106.63,     'H2Q2': 105.68,     'H2Q3': 105.19,     'H2Q4': 105.01,
            'H3Q1': 104.21,     'H3Q2': 102.0,      'H3Q3': 100.0,      'H3Q4': 100.0,
            'H4Q1': 97.57,      'H4Q2': 97.51,      'H4Q3': 97.51,      'H4Q4': 97.91,
            'H5Q1': 98.5,       'H5Q2': 100.0,      'H5Q3': 102.28,     'H5Q4': 105.0,
            'H6Q1': 101.08,     'H6Q2': 101.28,     'H6Q3': 101.76,     'H6Q4': 102.24,
            'H7Q1': 101.76,     'H7Q2': 102.24,     'H7Q3': 104.24,     'H7Q4': 105.68,
            'H8Q1': 106.55,     'H8Q2': 110.41,     'H8Q3': 114.15,     'H8Q4': 122.58,
            'H9Q1': 140.78,     'H9Q2': 130.56,     'H9Q3': 115.17,     'H9Q4': 106.63,
            'H10Q1': 125.5,     'H10Q2': 105.01,    'H10Q3': 92.24,     'H10Q4': 60.0,
            'H11Q1': 100.24,    'H11Q2': 65.0,      'H11Q3': 58.81,     'H11Q4': 45.0,
            'H12Q1': 59.07,     'H12Q2': 44.2,      'H12Q3': 35.87,     'H12Q4': 24.97,
            'H13Q1': 26.76,     'H13Q2': 22.5,      'H13Q3': 23.92,     'H13Q4': 22.5,
            'H14Q1': 16.99,     'H14Q2': 16.68,     'H14Q3': 15.98,     'H14Q4': 15.45,
            'H15Q1': 6.67,      'H15Q2': 15.31,     'H15Q3': 16.35,     'H15Q4': 17.76,
            'H16Q1': 16.68,     'H16Q2': 18.94,     'H16Q3': 16.79,     'H16Q4': 24.57,
            'H17Q1': 19.0,      'H17Q2': 26.56,     'H17Q3': 43.78,     'H17Q4': 58.55,
            'H18Q1': 25.1,      'H18Q2': 50.0,      'H18Q3': 60.0,      'H18Q4': 77.67,
            'H19Q1': 59.07,     'H19Q2': 75.01,     'H19Q3': 101.52,    'H19Q4': 110.69,
            'H20Q1': 105.68,    'H20Q2': 112.21,    'H20Q3': 148.01,    'H20Q4': 134.33,
            'H21Q1': 194.14,    'H21Q2': 217.45,    'H21Q3': 230.0,     'H21Q4': 230.0,
            'H22Q1': 150.0,     'H22Q2': 130.0,     'H22Q3': 123.9,     'H22Q4': 113.75,
            'H23Q1': 114.01,    'H23Q2': 109.0,     'H23Q3': 106.63,    'H23Q4': 104.24,
            'H24Q1': 105.68,    'H24Q2': 104.21,    'H24Q3': 102.0,     'H24Q4': 101.52,
            'H25Q1': np.nan,    'H25Q2': np.nan,    'H25Q3': np.nan,    'H25Q4': np.nan
        },
        {
            'DATE': wantedDate.date(),  'CONCEPT': 'PRICE_PT',
            'H1Q1': 105.1,      'H1Q2': 104.24,     'H1Q3': 102.28,     'H1Q4': 102.0,
            'H2Q1': 106.63,     'H2Q2': 105.68,     'H2Q3': 105.19,     'H2Q4': 105.01,
            'H3Q1': 104.21,     'H3Q2': 102.0,      'H3Q3': 100.0,      'H3Q4': 100.0,
            'H4Q1': 97.57,      'H4Q2': 97.51,      'H4Q3': 97.51,      'H4Q4': 97.91,
            'H5Q1': 98.5,       'H5Q2': 100.0,      'H5Q3': 102.28,     'H5Q4': 105.0,
            'H6Q1': 101.08,     'H6Q2': 101.28,     'H6Q3': 101.76,     'H6Q4': 102.24,
            'H7Q1': 101.76,     'H7Q2': 102.24,     'H7Q3': 104.24,     'H7Q4': 105.68,
            'H8Q1': 106.55,     'H8Q2': 110.41,     'H8Q3': 114.15,     'H8Q4': 122.58,
            'H9Q1': 140.78,     'H9Q2': 130.56,     'H9Q3': 115.17,     'H9Q4': 106.63,
            'H10Q1': 125.5,     'H10Q2': 105.01,    'H10Q3': 92.24,     'H10Q4': 60.87,
            'H11Q1': 100.24,    'H11Q2': 65.0,      'H11Q3': 58.81,     'H11Q4': 45.0,
            'H12Q1': 59.07,     'H12Q2': 44.2,      'H12Q3': 35.87,     'H12Q4': 24.97,
            'H13Q1': 26.76,     'H13Q2': 22.5,      'H13Q3': 23.92,     'H13Q4': 22.5,
            'H14Q1': 16.99,     'H14Q2': 16.68,     'H14Q3': 15.98,     'H14Q4': 15.45,
            'H15Q1': 6.67,      'H15Q2': 15.31,     'H15Q3': 16.35,     'H15Q4': 17.76,
            'H16Q1': 16.68,     'H16Q2': 18.94,     'H16Q3': 16.79,     'H16Q4': 24.57,
            'H17Q1': 19.0,      'H17Q2': 26.56,     'H17Q3': 43.78,     'H17Q4': 58.55,
            'H18Q1': 25.1,      'H18Q2': 50.0,      'H18Q3': 60.0,      'H18Q4': 77.67,
            'H19Q1': 60.0,      'H19Q2': 75.01,     'H19Q3': 101.52,    'H19Q4': 110.69,
            'H20Q1': 105.68,    'H20Q2': 112.21,    'H20Q3': 148.01,    'H20Q4': 134.33,
            'H21Q1': 194.14,    'H21Q2': 217.45,    'H21Q3': 230.0,     'H21Q4': 230.0,
            'H22Q1': 150.0,     'H22Q2': 130.0,     'H22Q3': 123.9,     'H22Q4': 113.75,
            'H23Q1': 114.01,    'H23Q2': 109.0,     'H23Q3': 106.63,    'H23Q4': 104.24,
            'H24Q1': 105.68,    'H24Q2': 104.21,    'H24Q3': 102.0,     'H24Q4': 101.52,
            'H25Q1': np.nan,    'H25Q2': np.nan,    'H25Q3': np.nan,    'H25Q4': np.nan
        },
    ])
    assert df.equals(wantedDf)


def test_marginal_price_downloader_after_october25_23h():
    # todo: include here the test for 23h after october 26, 2025 when the time change happens
    pass


def test_marginal_price_downloader_after_october25_25h():
    # todo: include here the test for 23h after march 29, 2026 when the time change happens
    pass


def test_marginal_price_downloader_before_october25_24h():
    # Set the wanted date.
    wantedDate = dt.datetime(2025, 9, 30)

    # This can take time for longer date spans, since it is downloading the files from the website.
    df = OMIEMarginalPriceFileImporter(date_ini=wantedDate, date_end=wantedDate).read_to_dataframe(verbose=True)
    wantedDf = pd.DataFrame([
        {
            'DATE': wantedDate.date(),  'CONCEPT': 'PRICE_SP',
            'H1': 95.46,    'H2': 88.25,    'H3': 80.0,     'H4': 76.43,
            'H5': 78.0,     'H6': 80.0,     'H7': 97.11,    'H8': 105.68,
            'H9': 120.0,    'H10': 93.97,   'H11': 60.1,    'H12': 31.0,
            'H13': 24.47,   'H14': 21.9,    'H15': 22.0,    'H16': 29.08,
            'H17': 35.0,    'H18': 54.94,   'H19': 84.0,    'H20': 117.0,
            'H21': 199.34,  'H22': 172.11,  'H23': 119.9,   'H24': 101.5,
            'H25': np.nan
        },
        {
            'DATE': wantedDate.date(),  'CONCEPT': 'PRICE_PT',
            'H1': 95.46,    'H2': 88.25,    'H3': 80.0,     'H4': 76.43,
            'H5': 78.0,     'H6': 80.0,     'H7': 97.11,    'H8': 105.68,
            'H9': 120.0,    'H10': 93.97,   'H11': 60.1,    'H12': 31.0,
            'H13': 24.47,   'H14': 21.9,    'H15': 22.0,    'H16': 29.08,
            'H17': 35.0,    'H18': 54.94,   'H19': 84.0,    'H20': 117.0,
            'H21': 199.34,  'H22': 172.11,  'H23': 119.9,   'H24': 101.5,
            'H25': np.nan
        }
    ])
    assert df.equals(wantedDf)


def test_marginal_price_downloader_before_october25_23h():
    # Set the wanted date.
    wantedDate = dt.datetime(2024, 3, 31)

    # This can take time for longer date spans, since it is downloading the files from the website.
    df = OMIEMarginalPriceFileImporter(date_ini=wantedDate, date_end=wantedDate).read_to_dataframe(verbose=True)
    wantedDf = pd.DataFrame([
        {
            'DATE': wantedDate.date(),  'CONCEPT': 'PRICE_SP',
            'H1': 3.2,      'H2': 1.63,     'H3': 0.5,      'H4': 0.5,
            'H5': 0.5,      'H6': 0.6,      'H7': 0.5,      'H8': 0.6,
            'H9': 0.5,      'H10': 0.5,     'H11': 0.4,     'H12': 0.0,
            'H13': 0.0,     'H14': 0.0,     'H15': 0.0,     'H16': 0.0,
            'H17': 0.0,     'H18': 0.0,     'H19': 0.0,     'H20': 1.69,
            'H21': 3.2,     'H22': 3.2,     'H23': 1.63,    'H24': np.nan,
            'H25': np.nan
        },
        {
            'DATE': wantedDate.date(),  'CONCEPT': 'PRICE_PT',
            'H1': 3.2,      'H2': 1.63,     'H3': 0.5,      'H4': 0.5,
            'H5': 0.5,      'H6': 0.6,      'H7': 0.5,      'H8': 0.6,
            'H9': 0.5,      'H10': 0.5,     'H11': 0.4,     'H12': 0.0,
            'H13': 0.0,     'H14': 0.0,     'H15': 0.0,     'H16': 0.0,
            'H17': 0.0,     'H18': 0.0,     'H19': 0.0,     'H20': 1.69,
            'H21': 3.2,     'H22': 3.2,     'H23': 1.63,    'H24': np.nan,
            'H25': np.nan
        }
    ])
    assert df.equals(wantedDf)


def test_marginal_price_downloader_before_october25_25h():
    # Set the wanted date.
    wantedDate = dt.datetime(2024, 10, 27)

    # This can take time for longer date spans, since it is downloading the files from the website.
    df = OMIEMarginalPriceFileImporter(date_ini=wantedDate, date_end=wantedDate).read_to_dataframe(verbose=True)
    wantedDf = pd.DataFrame([
        {
            'DATE': wantedDate.date(), 'CONCEPT': 'PRICE_SP',
            'H1': 87.71,    'H2': 83.31,    'H3': 82.23,    'H4': 80.68,
            'H5': 81.3,     'H6': 80.68,    'H7': 70.0,     'H8': 80.0,
            'H9': 86.24,    'H10': 81.3,    'H11': 64.36,   'H12': 54.72,
            'H13': 42.5,    'H14': 39.99,   'H15': 40.0,    'H16': 55.19,
            'H17': 44.99,   'H18': 63.97,   'H19': 81.25,   'H20': 96.27,
            'H21': 128.7,   'H22': 115.51,  'H23': 107.36,  'H24': 90.58,
            'H25': 102.99
        },
        {
            'DATE': wantedDate.date(), 'CONCEPT': 'PRICE_PT',
            'H1': 87.71,    'H2': 83.31,    'H3': 82.23,    'H4': 80.68,
            'H5': 81.3,     'H6': 80.68,    'H7': 70.0,     'H8': 80.0,
            'H9': 86.24,    'H10': 81.3,    'H11': 64.36,   'H12': 54.72,
            'H13': 42.5,    'H14': 39.99,   'H15': 40.0,    'H16': 55.19,
            'H17': 44.99,   'H18': 63.97,   'H19': 81.25,   'H20': 96.27,
            'H21': 128.7,   'H22': 115.51,  'H23': 107.36,  'H24': 90.58,
            'H25': 102.99
        }
    ])
    assert df.equals(wantedDf)


if __name__ == '__main__':
    test_marginal_price_downloader_after_october25_24h()
    test_marginal_price_downloader_after_october25_23h()
    test_marginal_price_downloader_after_october25_25h()
    test_marginal_price_downloader_before_october25_24h()
    test_marginal_price_downloader_before_october25_23h()
    test_marginal_price_downloader_before_october25_25h()
