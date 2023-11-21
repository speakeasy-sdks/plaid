# CreditBankIncome

The report of the Bank Income data for an end user.


## Fields

| Field                                                                                                                                                        | Type                                                                                                                                                         | Required                                                                                                                                                     | Description                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `bank_income_id`                                                                                                                                             | *Optional[str]*                                                                                                                                              | :heavy_minus_sign:                                                                                                                                           | The unique identifier associated with the Bank Income Report.                                                                                                |
| `bank_income_summary`                                                                                                                                        | [Optional[components.CreditBankIncomeSummary]](../../models/components/creditbankincomesummary.md)                                                           | :heavy_minus_sign:                                                                                                                                           | Summary for bank income across all income sources and items (max history of 730 days).                                                                       |
| `days_requested`                                                                                                                                             | *Optional[int]*                                                                                                                                              | :heavy_minus_sign:                                                                                                                                           | The number of days requested by the customer for the Bank Income Report.                                                                                     |
| `generated_time`                                                                                                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                         | :heavy_minus_sign:                                                                                                                                           | The time when the Bank Income Report was generated.                                                                                                          |
| `items`                                                                                                                                                      | List[[components.CreditBankIncomeItem](../../models/components/creditbankincomeitem.md)]                                                                     | :heavy_minus_sign:                                                                                                                                           | The list of Items in the report along with the associated metadata about the Item.                                                                           |
| `warnings`                                                                                                                                                   | List[[components.CreditBankIncomeWarning](../../models/components/creditbankincomewarning.md)]                                                               | :heavy_minus_sign:                                                                                                                                           | If data from the Bank Income report was unable to be retrieved, the warnings will contain information about the error that caused the data to be incomplete. |