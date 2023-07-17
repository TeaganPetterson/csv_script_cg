import csv

with open("enterprise.csv") as enterpriseFile, open("rc.csv") as rcFile, open("updated_rc.csv", "w", newline='') as updatedFile:
    enterpriseData = list(csv.reader(enterpriseFile, delimiter=','))
    rcData = list(csv.reader(rcFile, delimiter=','))
    first_ent_row = enterpriseData[0]
    first_rc_row = rcData[0]
    ent_phone_spot = first_ent_row.index("Mobile Phone")
    rc_phone_spot = first_rc_row.index("Mobile Phone")

    for rcRow in rcData[1:]:
        if rcRow[rc_phone_spot] == '':
            for entRow in enterpriseData[1:]:
                if rcRow[rc_phone_spot - 1] == entRow[ent_phone_spot - 1]:
                    rcRow[rc_phone_spot] = entRow[ent_phone_spot]
                    break

    writer = csv.writer(updatedFile)
    writer.writerow(first_rc_row) 
    writer.writerows(rcData[1:]) 

print("Script execution completed.")
