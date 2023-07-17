from csv_diff import load_csv, compare
diff = compare(
    load_csv(open("enterprise.csv"), key="Email"),
    load_csv(open("rc.csv"), key="Email")
)
print(diff)
