import yfinance as yf
import datetime

today = datetime.datetime.today().strftime("%Y-%m-%d")


def dl_hist_data(ticker, start_date, end_date=today):
    """

    :param ticker: Ticker Symbol default is current date
    :param start_date: Starting Date
    :param end_date: Ending Date
    :return: DataFrame
    """

    try:

        data = yf.download(ticker, start=start_date, end=end_date)
        data["Ticker"] = ticker

        return data

    except Exception as e:
        print(e)



