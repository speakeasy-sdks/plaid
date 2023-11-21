# CreditSessionResults

The set of results for a Link session.


## Fields

| Field                                                                                                                  | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `bank_employment_results`                                                                                              | List[[components.CreditSessionBankEmploymentResult](../../models/components/creditsessionbankemploymentresult.md)]     | :heavy_minus_sign:                                                                                                     | The set of bank employment verifications for the Link session.                                                         |
| `bank_income_results`                                                                                                  | List[[components.CreditSessionBankIncomeResult](../../models/components/creditsessionbankincomeresult.md)]             | :heavy_minus_sign:                                                                                                     | The set of bank income verifications for the Link session.                                                             |
| `document_income_results`                                                                                              | [Optional[components.CreditSessionDocumentIncomeResult]](../../models/components/creditsessiondocumentincomeresult.md) | :heavy_minus_sign:                                                                                                     | The details of a document income verification in Link                                                                  |
| `item_add_results`                                                                                                     | List[[components.CreditSessionItemAddResult](../../models/components/creditsessionitemaddresult.md)]                   | :heavy_minus_sign:                                                                                                     | The set of Item adds for the Link session.                                                                             |
| `payroll_income_results`                                                                                               | List[[components.CreditSessionPayrollIncomeResult](../../models/components/creditsessionpayrollincomeresult.md)]       | :heavy_minus_sign:                                                                                                     | The set of payroll income verifications for the Link session.                                                          |