# MortgagePropertyAddress

Object containing fields describing property address.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `additional_properties`                                      | Dict[str, *Any*]                                             | :heavy_minus_sign:                                           | N/A                                                          |
| `city`                                                       | *Optional[str]*                                              | :heavy_check_mark:                                           | The city name.                                               |
| `country`                                                    | *Optional[str]*                                              | :heavy_check_mark:                                           | The ISO 3166-1 alpha-2 country code.                         |
| `postal_code`                                                | *Optional[str]*                                              | :heavy_check_mark:                                           | The five or nine digit postal code.                          |
| `region`                                                     | *Optional[str]*                                              | :heavy_check_mark:                                           | The region or state (example "NC").                          |
| `street`                                                     | *Optional[str]*                                              | :heavy_check_mark:                                           | The full street address (example "564 Main Street, Apt 15"). |