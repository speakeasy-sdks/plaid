# LinkTokenCreateRequestTransfer

Specifies options for initializing Link for use with the Transfer product.


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `intent_id`                                                                     | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | The `id` returned by the `/transfer/intent/create` endpoint.                    |
| `payment_profile_token`                                                         | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | The `payment_profile_token` returned by the `/payment_profile/create` endpoint. |