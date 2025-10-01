import datetime as dt
import re
from babel.numbers import parse_decimal, NumberFormatError
import pandas as pd
import numpy as np

from requests import Response
from OMIEData.Enums.all_enums import DataTypeInMarginalPriceFile
from OMIEData.FileReaders.omie_file_reader import OMIEFileReader


class MarginalPriceFileReader(OMIEFileReader):

    # Static or class variables
    __dic_static_concepts__ = {
        'Precio marginal (Cent/kWh)':
            [DataTypeInMarginalPriceFile.PRICE_SPAIN, 10.0],
        'Precio marginal (EUR/MWh)':
            [DataTypeInMarginalPriceFile.PRICE_SPAIN, 1.0],
        'Precio marginal en el sistema español (Cent/kWh)':
            [DataTypeInMarginalPriceFile.PRICE_SPAIN, 10.0],
        'Precio marginal en el sistema español (EUR/MWh)':
            [DataTypeInMarginalPriceFile.PRICE_SPAIN, 1.0],
        'Precio marginal en el sistema portugués (Cent/kWh)':
            [DataTypeInMarginalPriceFile.PRICE_PORTUGAL, 10.0],
        'Precio marginal en el sistema portugués (EUR/MWh)':
            [DataTypeInMarginalPriceFile.PRICE_PORTUGAL, 1.0],
        'Demanda+bombeos (MWh)':
            [DataTypeInMarginalPriceFile.ENERGY_IBERIAN, 1.0],
        'Energía en el programa resultante de la casación (MWh)':
            [DataTypeInMarginalPriceFile.ENERGY_IBERIAN, 1.0],
        'Energía total del mercado Ibérico (MWh)':
            [DataTypeInMarginalPriceFile.ENERGY_IBERIAN, 1.0],
        'Energía total con bilaterales del mercado Ibérico (MWh)':
            [DataTypeInMarginalPriceFile.ENERGY_IBERIAN_WITH_BILLATERAL, 1.0]}

    # List to use before 1/10/2025
    __key_list_retrieve_before__ = ['DATE', 'CONCEPT',
                                    'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12',
                                    'H13', 'H14', 'H15', 'H16', 'H17', 'H18', 'H19', 'H20', 'H21', 'H22', 'H23', 'H24',
                                    'H25']

    # List to use after 1/10/2025
    __key_list_retrieve_after__ = ['DATE', 'CONCEPT',
                                   'H1Q1', 'H1Q2', 'H1Q3', 'H1Q4', 'H2Q1', 'H2Q2', 'H2Q3', 'H2Q4',
                                   'H3Q1', 'H3Q2', 'H3Q3', 'H3Q4', 'H4Q1', 'H4Q2', 'H4Q3', 'H4Q4',
                                   'H5Q1', 'H5Q2', 'H5Q3', 'H5Q4', 'H6Q1', 'H6Q2', 'H6Q3', 'H6Q4',
                                   'H7Q1', 'H7Q2', 'H7Q3', 'H7Q4', 'H8Q1', 'H8Q2', 'H8Q3', 'H8Q4',
                                   'H9Q1', 'H9Q2', 'H9Q3', 'H9Q4', 'H10Q1', 'H10Q2', 'H10Q3', 'H10Q4',
                                   'H11Q1', 'H11Q2', 'H11Q3', 'H11Q4', 'H12Q1', 'H12Q2', 'H12Q3', 'H12Q4',
                                   'H13Q1', 'H13Q2', 'H13Q3', 'H13Q4', 'H14Q1', 'H14Q2', 'H14Q3', 'H14Q4',
                                   'H15Q1', 'H15Q2', 'H15Q3', 'H15Q4', 'H16Q1', 'H16Q2', 'H16Q3', 'H16Q4',
                                   'H17Q1', 'H17Q2', 'H17Q3', 'H17Q4', 'H18Q1', 'H18Q2', 'H18Q3', 'H18Q4',
                                   'H19Q1', 'H19Q2', 'H19Q3', 'H19Q4', 'H20Q1', 'H20Q2', 'H20Q3', 'H20Q4',
                                   'H21Q1', 'H21Q2', 'H21Q3', 'H21Q4', 'H22Q1', 'H22Q2', 'H22Q3', 'H22Q4',
                                   'H23Q1', 'H23Q2', 'H23Q3', 'H23Q4', 'H24Q1', 'H24Q2', 'H24Q3', 'H24Q4',
                                   'H25Q1', 'H25Q2', 'H25Q3', 'H25Q4']

    __dateFormatInFile__ = '%d/%m/%Y'
    __localeInFile__ = "en_DK.UTF-8"

    def __init__(self, types=None, after_october_2025=False):
        self.conceptsToLoad = [v for v in DataTypeInMarginalPriceFile] if not types else types
        self.after_october_2025 = after_october_2025

    def get_keys(self):
        keys = MarginalPriceFileReader.__key_list_retrieve_after__ \
            if self.after_october_2025 \
            else MarginalPriceFileReader.__key_list_retrieve_before__
        return keys

    def get_data_from_response(self, response: Response) -> pd.DataFrame:

        res = pd.DataFrame(columns=self.get_keys())

        # from the first line we get the units and the price date. We just look at the date
        lines = response.text.split("\n")
        matches = re.findall('\d\d/\d\d/\d\d\d\d', lines.pop(0))
        if not (len(matches) == 2):
            print('Response ' + response.url + ' does not have the expected format.')
            raise BaseException
        else:
            # The second date is the one we want
            date = dt.datetime.strptime(matches[1], MarginalPriceFileReader.__dateFormatInFile__).date()

            # Process all the lines

            while lines:

                # read following line
                line = lines.pop(0)
                splits = line.split(sep=';')
                first_col = splits[0]

                if first_col in MarginalPriceFileReader.__dic_static_concepts__.keys():
                    concept_type = MarginalPriceFileReader.__dic_static_concepts__[first_col][0]

                    if concept_type in self.conceptsToLoad:
                        units = MarginalPriceFileReader.__dic_static_concepts__[first_col][1]

                        dico = self._process_line(date=date, concept=concept_type, values=splits[1:], multiplier=units)
                        res = pd.concat([res, pd.DataFrame([dico])], ignore_index=True)

            return res

    def get_data_from_file(self, filename: str) -> pd.DataFrame:

        # Method yield each dictionary one by one
        res = pd.DataFrame(columns=self.get_keys())
        file = open(filename, 'r', encoding='latin-1')

        # from first line we get the units and the price date. We just look at the date
        line = file.readline()
        matches = re.findall('\d\d/\d\d/\d\d\d\d', line)
        if not (len(matches) == 2):
            print('File ' + filename + ' does not have the expected format.')
            raise FileNotFoundError
        else:
            # The second date is the one we want
            date = dt.datetime.strptime(matches[1], MarginalPriceFileReader.__dateFormatInFile__).date()

            # Process all the lines
            while line:
                # read the following line
                line = file.readline()
                splits = line.split(sep=';')
                first_col = splits[0]

                if first_col in MarginalPriceFileReader.__dic_static_concepts__.keys():
                    concept_type = MarginalPriceFileReader.__dic_static_concepts__[first_col][0]

                    if concept_type in self.conceptsToLoad:
                        units = MarginalPriceFileReader.__dic_static_concepts__[first_col][1]
                        dico = self._process_line(date=date, concept=concept_type, values=splits[1:], multiplier=units)
                        res = pd.concat([res, pd.DataFrame([dico])], ignore_index=True)

            return res

    def _process_line(self, date: dt.date, concept: DataTypeInMarginalPriceFile, values: list, multiplier=1.0) -> dict:

        key_list = self.get_keys()

        result = dict.fromkeys(self.get_keys())
        result[key_list[0]] = date
        result[key_list[1]] = str(concept)

        # Note: *values* is a list of floats with 23 to 25 values with an extra position that is filled with '\r'
        # For example:
        # - for 31/3/2024 (23 hours): the list has 23 values + 1 '\r'
        # - for 27/10/2024 (25 hours): the list has 25 values + 1 '\r'
        # - for 26/10/2024 (24 hours): the list has 24 values + 1 '\r'
        # From 1/10/2025, the list has 4 times more values (quarters of hour)
        # - for 31/3/2025 (23 hours): the list has 92 values + 1 '\r'
        # - for 27/10/2025 (25 hours): the list has 100 values + 1 '\r'
        # - for 26/10/2025 (24 hours): the list has 96 values + 1 '\r'
        for i, v in enumerate(values, start=1):
            break_flag = 100 if self.after_october_2025 else 25
            if i > break_flag:
                break  # Break if the '\r' position is reached
            try:
                f = multiplier * float(parse_decimal(v, locale=self.__localeInFile__))
            except NumberFormatError:
                # The exception is raised when the value reached is '\r'
                break_flag_23h = 93 if self.after_october_2025 else 24
                break_flag_24h = 97 if self.after_october_2025 else 25
                if i == break_flag_23h:
                    # Day with 23-hours.
                    # Note: the key_list has always 25+2 or 100+2 positions, even if the day has 23 or 24 hours.
                    #   The first two positions are for 'DATE' and 'CONCEPT'.
                    #   The resulting dictionary will have the same number of key-value pairs.
                    nr_nan_from_last = 8 if self.after_october_2025 else 2
                    for j in range(-1, -nr_nan_from_last-1, -1):
                        result[key_list[j]] = np.nan
                elif i == break_flag_24h:
                    # Day with 24-hours.
                    nr_nan_from_last = 4 if self.after_october_2025 else 1
                    for j in range(-1, -nr_nan_from_last-1, -1):
                        result[key_list[j]] = np.nan
                else:
                    # Since all possible cases are covered, the exception should not happen
                    raise
            else:
                result[key_list[i + 1]] = f

        return result
