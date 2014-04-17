DATE_FORMAT = 'j. F Y'
TIME_FORMAT = 'H:i'
DATETIME_FORMAT = 'j. F Y H:i'
YEAR_MONTH_FORMAT = 'F Y'
MONTH_DAY_FORMAT = 'j. F'
SHORT_DATE_FORMAT = 'd.m.Y'
SHORT_DATETIME_FORMAT = 'd.m.Y H:i'
FIRST_DAY_OF_WEEK = 1

# The *_INPUT_FORMATS strings use the Python strftime format syntax,
# see http://docs.python.org/library/datetime.html#strftime-strptime-behavior
DATE_INPUT_FORMATS = (
    '%d.%m.%Y', '%d/%m/%Y', '%d/%m-%y', # '25-10-2006',
)
TIME_INPUT_FORMATS = (
    '%H:%M:%S',                         # '14:30:59'
    '%H:%M',                            # '14:30'
)
DATETIME_INPUT_FORMATS = (
    '%d.%m.%Y %H:%M:%S',     # '25.10.2006 14:30:59'
    '%d-%m-%Y %H:%M:%S',     # '25-10-2006 14:30:59'
    '%d/%m-%Y %H:%M:%S',     # '25/10-2006 14:30:59'
    '%d/%m/%Y %H:%M:%S',     # '25/10/2006 14:30:59'
)
DECIMAL_SEPARATOR = ','
THOUSAND_SEPARATOR = '.'
NUMBER_GROUPING = 3