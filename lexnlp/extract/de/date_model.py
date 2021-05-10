__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2021, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-lexnlp/blob/2.0.0/LICENSE"
__version__ = "2.0.0"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"

import string


DE_ALPHABET = 'äöüẞ' + 'äöüẞ'.upper()
DATE_MODEL_CHARS = []
DATE_MODEL_CHARS.extend(DE_ALPHABET + string.ascii_letters)
DATE_MODEL_CHARS.extend(string.digits)
DATE_MODEL_CHARS.extend(["-", "/", " ", "%", "#", "$"])
