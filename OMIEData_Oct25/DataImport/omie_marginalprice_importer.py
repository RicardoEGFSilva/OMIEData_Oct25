import datetime as dt

from OMIEData_Oct25.DataImport.omie_data_importer_from_responses import OMIEDataImporterFromResponses
from OMIEData_Oct25.Downloaders.marginal_price_downloader import MarginalPriceDownloader
from OMIEData_Oct25.FileReaders.marginal_price_file_reader import MarginalPriceFileReader


class OMIEMarginalPriceFileImporter(OMIEDataImporterFromResponses):

    def __init__(self, date_ini: dt.date, date_end: dt.date):

        flag = date_ini >= dt.date(2025, 10, 1)
        super().__init__(date_ini=date_ini,
                         date_end=date_end,
                         file_downloader=MarginalPriceDownloader(),
                         file_reader=MarginalPriceFileReader(after_october_2025=flag))
