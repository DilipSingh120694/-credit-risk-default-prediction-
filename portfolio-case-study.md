# Portfolio Case Study: Credit Risk Analysis

## Context and objective
This academic project examines whether borrower attributes can help identify loan default risk. It is framed for a retail banking credit team; it does not represent work commissioned by a bank or a deployed underwriting system.

## My analytical work
The submitted report describes preparing a Kaggle dataset of 32,581 borrower records, exploring grade, income, loan-to-income ratio and prior default history, then comparing logistic regression and decision tree classification. It also reports an independent-samples t-test for income differences by default outcome.

Reported preprocessing removes missing employment-length and interest-rate values and ages above 100, and encodes categorical variables. The reported holdout split is 80/20. The exact retained row count and settings remain to be reconciled with the original notebook.

## Results supported by the figures
| Outcome | Logistic regression | Decision tree |
| --- | ---: | ---: |
| Test observations | 5,727 | 5,727 |
| Correctly identified defaults | 535 | 760 |
| Missed defaults | 679 | 454 |
| Non-defaults incorrectly flagged | 232 | 274 |
| Accuracy | 84.09% | 87.29% |
| Default recall | 44.07% | 62.60% |

The tree captures 225 more defaults, while incorrectly flagging 42 additional non-defaults. The comparison shows why business interpretation should include both kinds of error rather than accuracy alone.

The exploratory figure shows higher default rates for lower loan grades and prior-default borrowers. The tree importance chart highlights loan-to-income ratio, grade and income. The report's income test gives `p < 0.001`, but the underlying test output is unavailable for independent reproduction.

## Management interpretation
The decision tree is a candidate for further validation because it identifies more observed defaults at its displayed operating point. Its learned rules could support analyst investigation, but do not justify a universal rejection policy. No financial savings or real-world performance gains were measured.

Next steps are to confirm the source code and data provenance, evaluate probability calibration and business costs, and test stability on another time period and across relevant groups. Income differences alone do not establish causality or justify treating low-income applicants unfairly.

## Skills demonstrated
- Framing a business question as a binary classification problem.
- Describing data preparation and exploratory analysis.
- Comparing interpretable model outputs.
- Reading confusion matrices and translating error trade-offs into business implications.
- Communicating statistical findings with clear limitations.

## Portfolio improvement
The original narrative contains conflicting accuracy values and feature rankings. This portfolio uses figures as the evidence for corrected performance claims, adds precision/recall/F1 and a majority-class reference, and separates reported methods from verified calculations. The supplementary audit reproduces only the arithmetic from the supplied figures.

## Interview explanation
I investigated loan default risk using a Kaggle dataset and compared logistic regression with a decision tree. The figures show that the tree identified about 63% of observed defaults, compared with about 44% for logistic regression. That helped me understand why accuracy alone is insufficient: identifying more defaults also meant flagging more non-default borrowers. I would verify the original pipeline, quantify error costs and evaluate calibration and subgroup performance before recommending operational use.
