import datetime

from main.templatetags.no_l10n_date import no_l10n_date


def test_no_l10n_date():
    assert no_l10n_date(datetime.date(2022, 10, 29)) == "2022-10-29"
    assert no_l10n_date(datetime.datetime(2022, 10, 29, 22, 59), "DATETIME_FORMAT") == "2022-10-29 22:59"
