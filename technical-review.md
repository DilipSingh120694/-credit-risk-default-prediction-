# Technical Review and Next Steps

This review distinguishes evidence visible in the submitted report from items requiring the original dataset or notebook.

## Corrections made in the portfolio
| Original issue | Evidence and portfolio treatment |
| --- | --- |
| Text gives roughly 82% / 85% accuracy | Confusion matrices and comparison chart support 84.09% / 87.29%; metric audit reproduces the arithmetic. |
| Loan grade described as strongest in both models | Tree chart ranks ratio first, grade second, income third. Logistic coefficients are not directly comparable across different scales. |
| Overall default rate described as under 10% | Held-out matrix counts imply 21.20% defaults. This test-set rate is not asserted for the whole dataset. |
| About 28,000 cleaned rows | Tree root shows 22,906 samples and test matrices show 5,727: combined 28,633, assuming matching runs. Needs notebook confirmation. |
| All 12 features said to be retained | Report says 12 total columns, including target; chart shows eight predictors. Exact training columns remain unverified. |
| Loan-to-income ratio described as repayment-to-income | Do not interpret a loan amount/income ratio as annual repayment burden. Confirm the data dictionary and formula. |
| A 40% lending cap proposed | Descriptive analysis and one fitted tree do not validate a policy cutoff. The tree root split is around 0.305. No automatic rejection rule is proposed in the portfolio. |
| All E-G rates said to exceed 60% | Figure shows E 64.4%, F 70.5%, G 98.4%; rates are figure readings, not an independently recomputed combined rate. |
| Prior default treated as dominant in both models | EDA shows 37.9% vs 18.4%, but its importance is very small in the displayed tree. Association and fitted importance are different measures. |
| Rounded p-value displayed as zero | Retain report's `p < 0.001`, not `p = 0`. Exact output and assumptions are unavailable. |
| Currency shown as pounds | Source currency is unverified. Use dataset units in portfolio text. |
| Improvement over traditional lending claimed | No actual bank scoring/manual underwriting baseline was evaluated. Only a majority-class reference can be calculated here. |
| Dataset called free of ethical concerns | Dataset source, anonymisation, licence, sensitive proxies and fairness require assessment. Public availability does not establish absence of concerns. |

## Reproducibility checks for the original notebook
1. Export and inspect every cell, including import/package versions and random seeds.
2. Record input rows, missing counts, exclusions, final rows and duplicate handling.
3. Confirm target labels, predictor columns and category mappings.
4. Confirm the split was stratified or report why it was not; verify no borrower leakage and the same test set for both models.
5. Fit learned preprocessing on training data only.
6. For nominal features such as loan intent or home ownership, use an encoding that does not invent an order. Document treatment of ordinal grade and binary default history.
7. Scale continuous inputs appropriately for logistic regression, check convergence and document model settings. Inspect tree depth, minimum leaf sizes and tuning.
8. Report class-wise precision, recall, F1, balanced accuracy and confusion matrices. Add ROC-AUC/PR-AUC and calibration only after obtaining probability predictions; these cannot be recovered from one matrix.
9. Verify the income test statistic, group sizes, variances, outliers, effect size and confidence interval. Consider Welch's t-test if the variance assumptions warrant it. An association test does not validate out-of-sample prediction.
10. Test thresholds using validation data and quantify business costs. Avoid optimising on the final test set.
11. Evaluate external/time-based generalisation and meaningful subgroup errors where the data and intended use allow it.

## Remaining evidence gaps
The original `.ipynb`, raw CSV, trained model objects and prediction probabilities were not supplied. The Colab link could not be retrieved during preparation. The source report's statement that it is shared with anyone holding the link was not independently verified. Dataset licence wording and authenticity/anonymisation are also unverified.

The portfolio can present this as an academic case study now. Exporting the original notebook is the most valuable addition for a code-focused recruiter.

## Technical references
- [scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [scikit-learn categorical encoding](https://scikit-learn.org/stable/modules/preprocessing.html#encoding-categorical-features)
- [scikit-learn common pitfalls and leakage](https://scikit-learn.org/stable/common_pitfalls.html)

These references support the improvement plan; they do not independently validate the academic results.
