# Dataset Source and Variables

The submitted report attributes the data to [Laotse's Credit Risk Dataset on Kaggle](https://www.kaggle.com/datasets/laotse/credit-risk-dataset) and describes 32,581 records with 12 columns. Neither the CSV nor a verified licence was available during portfolio preparation. No data is bundled here. Confirm the current licence before redistributing any records.

## Variables named in the report and figures
| Variable | Description used in this project | Note |
| --- | --- | --- |
| `person_age` | Borrower age | Report filters values above 100. |
| `person_income` | Borrower annual income | Currency unverified; do not assume GBP. |
| `person_emp_length` | Employment length | Unit must be confirmed in source dictionary. |
| `loan_amnt` | Loan amount | Dataset units. |
| `loan_int_rate` | Interest rate | Percentage representation should be confirmed. |
| `loan_grade` | Grade A-G | Report says mapped to 0-6. |
| `loan_percent_income` | Loan-to-income ratio | Do not call this repayment burden without verifying formula. |
| `loan_intent` | Loan purpose | Nominal category; exact encoding unverified. |
| `cb_person_default_on_file` | Prior default flag | Report convention Y/N. |
| `loan_status` | Binary model target | Report convention 0 non-default, 1 default. |

This is a partial glossary grounded in the supplied report, not a verified complete data dictionary. The other two columns of the reported 12-column dataset are not documented here without the CSV or authoritative dictionary.

## Reproduction
Download the dataset from its source after checking the licence. Export the original Colab notebook and inspect its file-loading cell for the expected CSV filename and schema. Record the download date, dataset version, file checksum and exact retained row count. Do not overwrite the figure-based metric audit with newly trained model results.
