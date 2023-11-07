# TransferUserAddressInRequest

The address associated with the account holder. Providing this data will improve the likelihood that Plaid will be able to guarantee the transfer, if applicable.


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `city`                                               | *Optional[str]*                                      | :heavy_minus_sign:                                   | Ex. "San Francisco"                                  |
| `country`                                            | *Optional[str]*                                      | :heavy_minus_sign:                                   | A two-letter country code (e.g., "US").              |
| `postal_code`                                        | *Optional[str]*                                      | :heavy_minus_sign:                                   | The postal code (e.g., "94103").                     |
| `region`                                             | *Optional[str]*                                      | :heavy_minus_sign:                                   | The state or province (e.g., "CA").                  |
| `street`                                             | *Optional[str]*                                      | :heavy_minus_sign:                                   | The street number and name (i.e., "100 Market St."). |