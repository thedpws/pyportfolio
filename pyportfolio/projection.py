from datetime import timedelta

import dateutil.utils
import pandas as pd
class Projection:
    def __init__(self, *args, **kwargs):
        self.start_date = kwargs.get('start_date', dateutil.utils.today())
        n_years = kwargs.get('years')
        self.end_date = self.start_date + timedelta(days=365*n_years)

    def to_dataframe(self) -> pd.DataFrame:
        pass
