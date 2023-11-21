# Enhancements

A grouping of the Plaid produced transaction enhancement fields.


## Fields

| Field                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `additional_properties`                                                                                                                                                                                                                                                                                | Dict[str, *Any*]                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                                                                                                    |
| `category`                                                                                                                                                                                                                                                                                             | List[*str*]                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                     | A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).                                                                                                     |
| `category_id`                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                                                     | The ID of the category to which this transaction belongs. For a full list of categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).                                                                                                                     |
| `check_number`                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | The check number of the transaction. This field is only populated for check transactions.                                                                                                                                                                                                              |
| `counterparties`                                                                                                                                                                                                                                                                                       | List[[components.Counterparty](../../models/components/counterparty.md)]                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | The counterparties present in the transaction. Counterparties, such as the merchant or the financial institution, are extracted by Plaid from the raw description.                                                                                                                                     |
| `location`                                                                                                                                                                                                                                                                                             | [components.Location](../../models/components/location.md)                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                     | A representation of where a transaction took place                                                                                                                                                                                                                                                     |
| `logo_url`                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | The URL of a logo associated with this transaction, if available. The logo is formatted as a 100x100 pixel PNG file.                                                                                                                                                                                   |
| `merchant_name`                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | The name of the primary counterparty, such as the merchant or the financial institution, as extracted by Plaid from the raw description.                                                                                                                                                               |
| `payment_channel`                                                                                                                                                                                                                                                                                      | [components.PaymentChannel](../../models/components/paymentchannel.md)                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                     | The channel used to make a payment.<br/>`online:` transactions that took place online.<br/><br/>`in store:` transactions that were made at a physical location.<br/><br/>`other:` transactions that relate to banks, e.g. fees or deposits.                                                            |
| `personal_finance_category`                                                                                                                                                                                                                                                                            | [Optional[components.PersonalFinanceCategory]](../../models/components/personalfinancecategory.md)                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | Information describing the intent of the transaction. Most relevant for personal finance use cases, but not limited to such use cases.<br/><br/>See the [`taxonomy csv file`](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories. |
| `personal_finance_category_icon_url`                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | A link to the icon associated with the primary personal finance category. The logo will always be 100x100 pixels.                                                                                                                                                                                      |
| `website`                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                     | The website associated with this transaction, if available.                                                                                                                                                                                                                                            |