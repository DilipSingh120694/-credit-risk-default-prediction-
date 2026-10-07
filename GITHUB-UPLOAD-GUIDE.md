# GitHub Upload Guide for Dilip

## 1. Extract the download
Unzip `credit-risk-github-package.zip` on your computer. Inside is a project folder named `credit-risk-default-prediction`, plus these instructions and a profile template.

## 2. Create the project repository
Sign in at https://github.com/new.
- Repository name: `credit-risk-default-prediction`
- Description: `Academic Python credit risk project comparing logistic regression and a decision tree, with exploratory analysis and a figure-based evaluation audit.`
- Visibility: Public, if you want recruiters to view it.
- Leave the README, .gitignore and licence initialisation options unselected: this package already includes README and .gitignore. A third-party licence has not been verified, so do not select a blanket dataset licence.
- Click Create repository.

## 3. Upload the files
On the new repository page, choose the link to upload an existing file. For an existing repository use Add file > Upload files.

Open the LOCAL `credit-risk-default-prediction` folder. Drag its CONTENTS into GitHub's upload area, including `images`, `reports`, `data`, `notebooks`, `src` and `results`. Drag folders as well as files so their structure is preserved. Do not upload the ZIP as your only project file, and do not upload the enclosing folder as an extra nested directory.

The correct root will contain `README.md` alongside those folders. If the README is buried inside another project folder, upload again at the repository root with the correct layout.

Commit message: `Add credit risk portfolio documentation and figure evidence`
Choose Commit changes. A commit is a recorded save.

Hidden files may not appear in your file picker. The `.gitignore` is useful but not required to display the portfolio; add it separately with Add file > Create new file if needed.

Browser uploads are limited to 25 MiB per file. The supplied package files are below that limit.

## 4. Check the finished page
- README renders on the repository main page.
- All five images embedded in it display.
- Links to the case study, technical review, data notes and metric notebook work.
- The notebook renders its code and output.
- Your name is correct and the public page contains no student ID.
- Test the original Colab link in a signed-out/private browser. If it fails, fix sharing or replace it with the exported notebook link.
- Preserve the note that original training has not been reproduced until you actually rerun it.

## 5. Add your original model notebook
Open the Colab link referenced in the project README. Download the notebook using File > Download > Download .ipynb, or the equivalent download control.

Name the export `credit-risk-original-analysis.ipynb`. Upload it into `notebooks/`. Check outputs and code for private data and credentials. Record the source data and exact package versions, then run all cells in a fresh environment before saying the model is reproducible.

Add this relative link to the project README after uploading:
`[Original model training notebook](notebooks/credit-risk-original-analysis.ipynb)`

Do not remove the supplementary audit notebook: it independently checks the reported matrix arithmetic.

## 6. Set project topics
On the repository main page, edit the About section and add relevant topics:
`credit-risk`, `business-analytics`, `python`, `machine-learning`, `logistic-regression`, `decision-tree`, `classification`, `portfolio`.

Do not add Power BI or SQL for this project unless you add work that actually uses those tools.

## 7. Create your profile introduction
Create another PUBLIC repository whose name is EXACTLY your GitHub username. Add a file named `README.md` at its root.

Copy the contents of `PROFILE-README-TEMPLATE.md` into it. Replace `YOUR_GITHUB_USERNAME` with your real username and `YOUR_LINKEDIN_URL` with your LinkedIn profile URL. Do not publish these placeholders unchanged. Only retain tools you can demonstrate.

The credit risk link will work after the project repository exists. The skills listed reflect your stated learning areas, not a claim of professional analyst employment.

## 8. Pin the project
Open your GitHub profile, select Customize your pins, choose `credit-risk-default-prediction`, and save.

## 9. Put it on your CV and LinkedIn
CV project entry:
**Credit Risk Analysis | Python, scikit-learn, SciPy**
Analysed borrower characteristics and compared logistic regression with decision tree classification using a Kaggle credit risk dataset. Interpreted confusion matrices and default-detection trade-offs; documented model limitations and recommendations for further validation.

Avoid claiming deployed savings, improved fairness or bank policy impact without evidence.

Add your profile URL to your CV contact section. On LinkedIn, add the project repository link as a Featured item and describe it as an academic project.

## Official guidance
- Repository creation: https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories
- Upload files: https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- Profile README: https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme
- Pin projects: https://docs.github.com/en/account-and-profile/how-tos/profile-customization/pinning-items-to-your-profile
