# LinkTokenCreateRequestBaseReport

Specifies options for initializing Link for use with the Base Report product. This field is required if `assets` is included in the `products` array and the client is CRA-enabled.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `days_requested`                                                             | *Optional[int]*                                                              | :heavy_minus_sign:                                                           | The maximum integer number of days of history to include in the Base Report. |