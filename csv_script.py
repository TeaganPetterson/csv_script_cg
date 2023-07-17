from csv_diff import load_csv, compare
diff = compare(
    load_csv(open("one.csv"), key="id"),
    load_csv(open("two.csv"), key="id")
)