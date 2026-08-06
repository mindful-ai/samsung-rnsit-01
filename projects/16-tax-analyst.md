# AI Tax Saving Advisor using Groq

## Workshop Duration

60–90 Minutes

---

# Objective

Develop an AI-powered Tax Saving Advisor using Python and the Groq LLM.

The application analyzes an individual's annual financial information and generates personalized tax-saving recommendations.

The AI assistant should compare tax regimes, identify unused deductions, recommend suitable investments, estimate tax savings, and generate a professional report with charts.

The objective is to demonstrate how LLMs can assist financial advisors in analyzing financial profiles and generating actionable insights.

---

# Learning Objectives

Students will learn how to

- Read Markdown/Text files
- Structure financial information
- Build effective prompts
- Use the Groq API
- Generate structured JSON responses
- Visualize AI outputs
- Create professional reports using AI

---

# Functional Requirements

The application shall

## 1. Read Financial Information

Read a Markdown (.md) or Text (.txt) file containing

- Personal Information
- Income Details
- Salary Components
- Investments
- Insurance
- Loans
- Medical Expenses
- Donations
- HRA Information
- Rent Details
- Family Information

---

## 2. Analyze the Financial Profile

The AI shall identify

- Annual taxable income
- Existing deductions
- Existing investments
- Insurance benefits
- Loan benefits
- Missing information
- Potential deductions

---

## 3. Compare Tax Regimes

The AI shall compare

Old Tax Regime

vs

New Tax Regime

and explain

- Estimated tax under Old Regime
- Estimated tax under New Regime
- Difference
- Recommended regime
- Reasons for recommendation

---

## 4. Analyze Existing Deductions

Evaluate whether the user has fully utilized

- Section 80C
- Section 80CCD(1B)
- Section 80D
- HRA
- LTA
- Home Loan Interest
- Education Loan Interest
- Donations
- Other applicable deductions

Highlight

- Fully utilized
- Partially utilized
- Not utilized

---

## 5. Suggest Tax Saving Opportunities

Recommend suitable tax-saving options

Examples

- ELSS
- PPF
- NPS
- Sukanya Samriddhi Yojana
- Tax Saving Fixed Deposit
- National Savings Certificate
- Senior Citizen Savings Scheme
- Health Insurance
- Home Loan
- Additional NPS Contribution
- HRA Optimization
- LTA Claims
- Donations under eligible sections

Each recommendation should include

- Description
- Relevant Section
- Estimated Investment
- Estimated Tax Benefit
- Priority
- Remarks

---

## 6. Recommend an Investment Mix

Suggest a balanced investment portfolio.

Example

40% ELSS

25% PPF

20% NPS

10% Fixed Deposit

5% Emergency Fund

Explain

- Risk
- Liquidity
- Lock-in
- Expected benefits

---

## 7. Generate an Action Plan

Create

Immediate Actions

Within 30 Days

Within Financial Year

Long-term Recommendations

---

## 8. Generate Reports

Generate

Tax_Report.md

Include

# Financial Summary

# Current Tax Position

# Old vs New Regime Comparison

# Existing Deductions

# Missed Opportunities

# Investment Recommendations

# Suggested Investment Mix

# Estimated Tax Savings

# Action Plan

---

## 9. Generate Visualizations

Create charts

- Tax Saving by Category
- Investment Allocation
- Utilized vs Remaining Deductions
- Old vs New Tax Comparison

---

# Input

inputs/person_profile.md

---

# Output

outputs/

Tax_Report.md

tax_saving_chart.png

investment_mix.png

deduction_utilization.png

tax_regime_comparison.png

---

# Folder Structure

Tax-Advisor/

│

├── app.py

├── requirements.txt

├── .env

│

├── inputs/

│      person_profile.md

│

└── outputs/

       Tax_Report.md

       tax_saving_chart.png

       investment_mix.png

       deduction_utilization.png

       tax_regime_comparison.png

---

# Evaluation

Input Handling................10

Prompt Engineering............20

Groq Integration...............20

Tax Analysis...................20

Visualization..................20

Code Quality...................10

Total........................100