# PaymentProfileCreateResponse

PaymentProfileCreateResponse defines the response schema for `/payment_profile/create`


## Fields

| Field                                                                                                                                       | Type                                                                                                                                        | Required                                                                                                                                    | Description                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                     | Dict[str, *Any*]                                                                                                                            | :heavy_minus_sign:                                                                                                                          | N/A                                                                                                                                         |
| `payment_profile_token`                                                                                                                     | *str*                                                                                                                                       | :heavy_check_mark:                                                                                                                          | A payment profile token associated with the Payment Profile data that is being requested.                                                   |
| `request_id`                                                                                                                                | *str*                                                                                                                                       | :heavy_check_mark:                                                                                                                          | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |