# LiabilitiesGetRequestOptions

An optional object to filter `/liabilities/get` results. If provided, `options` cannot be null.


## Fields

| Field                                                                                                                              | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `account_ids`                                                                                                                      | List[*str*]                                                                                                                        | :heavy_minus_sign:                                                                                                                 | A list of accounts to retrieve for the Item.<br/><br/>An error will be returned if a provided `account_id` is not associated with the Item |