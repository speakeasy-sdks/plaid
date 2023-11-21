# CreditCardLiability

An object representing a credit card account.


## Fields

| Field                                                                                                                                                                                 | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                                                               | Dict[str, *Any*]                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `account_id`                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                    | The ID of the account that this liability belongs to.                                                                                                                                 |
| `aprs`                                                                                                                                                                                | List[[components.Apr](../../models/components/apr.md)]                                                                                                                                | :heavy_check_mark:                                                                                                                                                                    | The various interest rates that apply to the account. APR information is not provided by all card issuers; if APR data is not available, this array will be empty.                    |
| `is_overdue`                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                    | true if a payment is currently overdue. Availability for this field is limited.                                                                                                       |
| `last_payment_amount`                                                                                                                                                                 | *Optional[float]*                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                    | The amount of the last payment.                                                                                                                                                       |
| `last_payment_date`                                                                                                                                                                   | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                          | :heavy_check_mark:                                                                                                                                                                    | The date of the last payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). Availability for this field is limited.                   |
| `last_statement_balance`                                                                                                                                                              | *Optional[float]*                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                    | The total amount owed as of the last statement issued                                                                                                                                 |
| `last_statement_issue_date`                                                                                                                                                           | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                          | :heavy_check_mark:                                                                                                                                                                    | The date of the last statement. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).                                                         |
| `minimum_payment_amount`                                                                                                                                                              | *Optional[float]*                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                    | The minimum payment due for the next billing cycle.                                                                                                                                   |
| `next_payment_due_date`                                                                                                                                                               | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                          | :heavy_check_mark:                                                                                                                                                                    | The due date for the next payment. The due date is `null` if a payment is not expected. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). |