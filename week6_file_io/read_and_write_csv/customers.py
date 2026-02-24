import csv


def main():
    with open("customers-100.csv") as customers_file, open(
        "customer_copy.csv", "w"
    ) as copy_file:
        reader = csv.DictReader(customers_file)
        writer = csv.DictWriter(copy_file, fieldnames=reader.fieldnames + ["Age"])
        writer.writeheader()

        for row in reader:
            writer.writerow({**row, "Age": calculate_age(row["Birth Date"])})


def calculate_age(birthdate):
    return 2026 - int(birthdate.split("-")[0])


if __name__ == "__main__":
    main()
