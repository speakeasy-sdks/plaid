# LinkTokenCreateRequestPaymentInitiation

Specifies options for initializing Link for use with the Payment Initiation (Europe) product. This field is required if `payment_initiation` is included in the `products` array. Either `payment_id` or `consent_id` must be provided.


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `consent_id`                                                                    | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | The `consent_id` provided by the `/payment_initiation/consent/create` endpoint. |
| `payment_id`                                                                    | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | The `payment_id` provided by the `/payment_initiation/payment/create` endpoint. |