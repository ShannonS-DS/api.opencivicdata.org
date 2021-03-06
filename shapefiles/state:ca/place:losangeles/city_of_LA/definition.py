from datetime import date
from django.utils.text import slugify

import boundaries

def sector_namer(feature):
    return feature.get('CITY_NAME')

def ocd_id_func(feature):
    return 'ocd-division/country:us/state:ca/place:los_angeles'

boundaries.register('city-of-la',
    file='',
    last_updated=date(2016, 12, 21),
    name='City of Los Angeles',
    singular='City of Los Angeles',
    domain='City of Los Angeles',
    authority='Los Angeles County Metropolitan Transportation',
    source_url='',
    licence_url='',
    start_date=None,
    end_date=None,
    notes='',
    name_func=sector_namer,
    id_func=ocd_id_func,
    is_valid_func=lambda feature: True,
    label_point_func=lambda feature: None,
)