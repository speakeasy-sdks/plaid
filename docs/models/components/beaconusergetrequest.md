# BeaconUserGetRequest

Request input for fetching a Beacon User


## Fields

| Field                                                                                                                                            | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      | Example                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `beacon_user_id`                                                                                                                                 | *str*                                                                                                                                            | :heavy_check_mark:                                                                                                                               | ID of the associated Beacon User.                                                                                                                | becusr_11111111111111                                                                                                                            |
| `client_id`                                                                                                                                      | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |                                                                                                                                                  |
| `secret`                                                                                                                                         | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.          |                                                                                                                                                  |