import os


class Initialize:

    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    Environment = 'Test'

    Navegador = u'Chrome'

    Celda_Usuario = '3'

    Celda = '3'

    Path_Evidencias = basedir + u'\data\capturas'

    Json = basedir + u"/pages"

    Path_Evidencias = basedir + u'/data/capturas'

    Excel = basedir + u'/data/dataTest.xlsx'

    if Environment == 'Test':
        Url = 'https://www.demoblaze.com/index.html'
        User = ''
        Pass = ''

