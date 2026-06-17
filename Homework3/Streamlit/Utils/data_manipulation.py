import pandas as pd

def tot_t(start,end,df):
    # Changing from str type to datetime type.
    df["Date"] = pd.to_datetime(df["Date"],dayfirst = True,errors="coerce")
    
    # Selecting the interval.
    df_t = df[(df["Date"]>= start) & (df["Date"]<=end)].copy()

    # Choosing only SELL and BUY for TransactionsType.
    df_t = df_t[(df_t["TransactionType"] == "SELL") | (df_t["TransactionType"] == "BUY")]

    # Taking only the day and not the hour.
    df_t["Day"] = df_t["Date"].dt.normalize()

    # Counting the total numer of transactions for each day and taking the series.
    df_t = df_t.groupby(df_t["Day"]).agg(number_of_transactions = ("TransactionType","count"))
    transactions = df_t["number_of_transactions"]

    # Creating a range day by day. 
    days = pd.date_range(start=start, end=end, freq='D')

    # Make a comparison between the series and the date_range, if some days are missing in the series,
    # it adds a 0.
    line_chart_data = transactions.reindex(days, fill_value=0)

    return line_chart_data

def top3(start,end,df):
    df_top3 = df[(df["Date"]>= start) & (df["Date"]<=end)].copy()
    df_top3 = df_top3.groupby("symbol").agg(n_transactions = ("TransactionType","count")).nlargest(3,"n_transactions")
    df_top3 = df_top3.sort_values("n_transactions",ascending=True)
    return df_top3

def top5_sector(start,end,df):
    df_top5_sector = df[(df["Date"]>= start) & (df["Date"]<=end)].copy()
    df_top5_sector = df_top5_sector.groupby("sector").agg(n_transactions = ("TransactionType","count")).nlargest(5,"n_transactions")
    df_top5_sector = df_top5_sector.sort_values("n_transactions",ascending=True)
    return df_top5_sector

def top5_industry(start,end,df):
    df_top5_industry = df[(df["Date"]>= start) & (df["Date"]<=end)].copy()
    df_top5_industry = df_top5_industry.groupby("industry").agg(n_transactions = ("TransactionType","count")).nlargest(5,"n_transactions")
    df_top5_industry = df_top5_industry.sort_values("n_transactions",ascending=True)
    return df_top5_industry