# CreditBankIncomeWarning

The warning associated with the data that was unavailable for the Bank Income Report.


## Fields

| Field                                                                                                                                                                                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `cause`                                                                                                                                                                                                                                                                                                                                                                                                                  | [Optional[components.CreditBankIncomeCause]](../../models/components/creditbankincomecause.md)                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                       | An error object and associated `item_id` used to identify a specific Item and error when a batch operation operating on multiple Items has encountered an error in one of the Items.                                                                                                                                                                                                                                     |
| `warning_code`                                                                                                                                                                                                                                                                                                                                                                                                           | [Optional[components.CreditBankIncomeWarningCode]](../../models/components/creditbankincomewarningcode.md)                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                       | The warning code identifies a specific kind of warning.<br/>`IDENTITY_UNAVAILABLE`: Unable to extract identity for the Item<br/>`TRANSACTIONS_UNAVAILABLE`: Unable to extract transactions for the Item<br/>`ITEM_UNAPPROVED`: User exited flow before giving permission to share data for the Item<br/>`REPORT_DELETED`: Report deleted due to customer or consumer request<br/>`DATA_UNAVAILABLE`: No relevant data was found for the Item |
| `warning_type`                                                                                                                                                                                                                                                                                                                                                                                                           | [Optional[components.CreditBankIncomeWarningType]](../../models/components/creditbankincomewarningtype.md)                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                       | The warning type which will always be `BANK_INCOME_WARNING`.                                                                                                                                                                                                                                                                                                                                                             |