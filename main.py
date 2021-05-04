import yfinance as yf
from os import path


def get_ESGRating(tickerList_fileUrl : str = "tickers.txt") -> None:
    tickers = dict()

    if not path.isfile(tickerList_fileUrl):
        raise FileNotFoundError

    with open(tickerList_fileUrl, "r") as db:
        for line in db.readlines():
            line = line.rstrip("\n")
            try:
                tickers[line] = yf.Ticker(line).sustainability.to_dict()["Value"]["totalEsg"]
            except AttributeError as e:
                print(f"no able to retrieve ESG for {line}")

    with open("tickers-esg.csv", "w") as db:
        db.writelines([f'{k}\t{tickers[k]}\n' for k in tickers.keys()])


def get_BetaRatings(tickerList_fileUrl : str = "tickers.txt") -> object:
    tickers = dict()
    
    with open(tickerList_fileUrl,"r") as db:
        for line in db.readlines():
            line = line.rstrip("\n")
            try:
                tickers[line] = yf.Ticker(line).get_info()["beta"]
            except KeyError as e:
                print(f"no able to retrieve beta for {line}")

    with open("tickers-beta.csv", "w") as db:
        db.writelines([f'{k}\t{tickers[k]}\n' for k in tickers.keys()])


def main():

    menu = {
        "1": get_ESGRating,
        "2": get_BetaRatings,
    }

    menu[input("\nHi, what do you need this time?\n[1] Gather ESG rating\n[2] Collect Betha ratings")]()
    print("Operation Compleed")

    while input("\n\nDo you wanna show the menu again? (Y/N)") in ("Y", "y"):
        menu[input("\n[1] Gather ESG rating\n[2] Collect Betha ratings")]()
        print("Operation Compleed")

    return


main()
