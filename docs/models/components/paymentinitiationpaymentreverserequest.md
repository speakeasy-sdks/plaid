# PaymentInitiationPaymentReverseRequest

PaymentInitiationPaymentReverseRequest defines the request schema for `/payment_initiation/payment/reverse`


## Fields

| Field                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `amount`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [Optional[components.PaymentAmountToRefund]](../../models/components/paymentamounttorefund.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | The amount and currency of a payment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `client_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `idempotency_key`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | A random key provided by the client, per unique wallet transaction. Maximum of 128 characters.<br/><br/>The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. If a request to execute a wallet transaction fails due to a network connection error, then after a minimum delay of one minute, you can retry the request with the same idempotency key to guarantee that only a single wallet transaction is created. If the request was successfully processed, it will prevent any transaction that uses the same idempotency key, and was received within 24 hours of the first request, from being processed. |
| `payment_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | The ID of the payment to reverse                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `reference`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | A reference for the refund. This must be an alphanumeric string with 6 to 18 characters and must not contain any special characters or spaces.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `secret`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |