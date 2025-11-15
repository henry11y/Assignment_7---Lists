
def analyze_loans(input_csv_path):
    """
    Read CSV (columns: loan_intent, loan_grade, loan_amnt, loan_int_rate),
    group rows by loan_intent into lists containing [loan_grade, loan_amnt, loan_int_rate],
    compute the most common grade, average amount, and average interest rate per intent,
    and write results to loan_intent_analysis.csv.
    """
    import csv
    from collections import Counter


    def _parse_num(s):
        if s is None:
            return None
        s = s.strip().replace(',', '')
        if s.endswith('%'):
            s = s[:-1]
        if s == '':
            return None
        try:
            return float(s)
        except ValueError:
            return None

    intents = {}  

    # Read the CSV file
    with open(input_csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            intent = (row.get('loan_intent') or '').strip()
            if not intent:
                continue  # skip blank intents

            grade = (row.get('loan_grade') or '').strip()
            amount = _parse_num(row.get('loan_amnt'))
            rate = _parse_num(row.get('loan_int_rate'))

            # Add this row to the correct list
            if intent not in intents:
                intents[intent] = []
            intents[intent].append([grade, amount, rate])

    # Prepare rows for the output CSV
    out_rows = []
    for intent in sorted(intents.keys()):
        records = intents[intent]

        grades = [r[0] for r in records if r[0] != '']
        amounts = [r[1] for r in records if isinstance(r[1], (int, float))]
        rates = [r[2] for r in records if isinstance(r[2], (int, float))]

        most_common_grade = Counter(grades).most_common(1)[0][0] if grades else ''
        avg_amount = sum(amounts) / len(amounts) if amounts else 0.0
        avg_rate = sum(rates) / len(rates) if rates else 0.0

        out_rows.append([
            intent,
            most_common_grade,
            f"{avg_amount:.2f}",
            f"{avg_rate:.2f}"
        ])

    # Write results to output CSV
    with open('loan_intent_analysis.csv', 'w', newline='', encoding='utf-8') as out_f:
        writer = csv.writer(out_f)
        writer.writerow(['loan_intent', 'most_common_grade', 'avg_amount', 'avg_interest_rate'])
        writer.writerows(out_rows)

if __name__ == "__main__":
    analyze_loans("LoansDataset.csv")

