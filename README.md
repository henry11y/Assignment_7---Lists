# Assignment_7 Lists
Purpose

The purpose of this program is to analyze loan data by creating individual lists for each unique `loan_intent` and calculating useful statistics from the dataset.

What the Program Does

Reads a CSV file that contains the columns:

	loan_intent
	'loan_grade'
	'loan_amnt'
	'loan_int_rate'


Groups all rows by their 'loan_intent' value

Builds list for each intent containing:

	loan_grade
	loan_amnt
	loan_int_rate

Calculates for each loan_intent:

	The most common laon_grade
	The average loan_amnt
	The average loan_int_rate
Writes the results into a new CSV file called loan_intent_analysis.csv



