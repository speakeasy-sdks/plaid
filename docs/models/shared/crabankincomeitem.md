# CraBankIncomeItem

The details and metadata for an end user's Item.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `bank_income_accounts`                                                               | List[[components.CraBankIncomeAccount](../../models/shared/crabankincomeaccount.md)] | :heavy_minus_sign:                                                                   | The Item's accounts that have Bank Income data.                                      |
| `bank_income_sources`                                                                | List[[components.CraBankIncomeSource](../../models/shared/crabankincomesource.md)]   | :heavy_minus_sign:                                                                   | The income sources for this Item. Each entry in the array is a single income source. |
| `institution_id`                                                                     | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | The unique identifier of the institution associated with the Item.                   |
| `institution_name`                                                                   | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | The name of the institution associated with the Item.                                |
| `last_updated_time`                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)                 | :heavy_minus_sign:                                                                   | The time when this Item's data was last retrieved from the financial institution.    |