import csv

filename = 'by_company.csv'

with open('result.csv', 'w') as result:
    fieldnames = ['employer_domain', 'talent_email']
    writer = csv.DictWriter(result, fieldnames=fieldnames)
    writer.writeheader()

    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            employer_domain = row[1]
            emails = row[3:]
            for talent_email in emails:
                writer.writerow({
                    'employer_domain': employer_domain,
                    'talent_email': talent_email,
                })
