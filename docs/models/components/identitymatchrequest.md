# IdentityMatchRequest

IdentityMatchRequest defines the request schema for `/identity/match`


## Fields

| Field                                                                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `access_token`                                                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                    | The access token associated with the Item data is being requested for.                                                                                                                                                                                                                |
| `client_id`                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                    | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.                                                                                                                                      |
| `options`                                                                                                                                                                                                                                                                             | [Optional[components.IdentityMatchRequestOptions]](../../models/components/identitymatchrequestoptions.md)                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                    | An optional object to filter /identity/match results                                                                                                                                                                                                                                  |
| `secret`                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                    | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.                                                                                                                                               |
| `user`                                                                                                                                                                                                                                                                                | [Optional[components.IdentityMatchUser]](../../models/components/identitymatchuser.md)                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                    | The user's legal name, phone number, email address and address used to perform fuzzy match. If Financial Account Matching is enabled in the Identity Verification product, leave this field empty to automatically match against PII collected from the Identity Verification checks. |