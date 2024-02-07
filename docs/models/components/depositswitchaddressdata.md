# DepositSwitchAddressData

The user's address.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `city`                                                       | *str*                                                        | :heavy_check_mark:                                           | The full city name                                           |
| `country`                                                    | *str*                                                        | :heavy_check_mark:                                           | The ISO 3166-1 alpha-2 country code                          |
| `postal_code`                                                | *str*                                                        | :heavy_check_mark:                                           | The postal code                                              |
| `region`                                                     | *str*                                                        | :heavy_check_mark:                                           | The region or state<br/>Example: `"NC"`                      |
| `street`                                                     | *str*                                                        | :heavy_check_mark:                                           | The full street address<br/>Example: `"564 Main Street, APT 15"` |
| `additional_properties`                                      | Dict[str, *Any*]                                             | :heavy_minus_sign:                                           | N/A                                                          |