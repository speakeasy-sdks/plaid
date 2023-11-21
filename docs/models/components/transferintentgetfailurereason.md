# TransferIntentGetFailureReason

The reason for a failed transfer intent. Returned only if the transfer intent status is `failed`. Null otherwise.


## Fields

| Field                                                                                                                 | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                               | Dict[str, *Any*]                                                                                                      | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `error_code`                                                                                                          | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | A code representing the reason for a failed transfer intent (i.e., an API error or the authorization being declined). |
| `error_message`                                                                                                       | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | A human-readable description of the code associated with a failed transfer intent.                                    |
| `error_type`                                                                                                          | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | A broad categorization of the error.                                                                                  |