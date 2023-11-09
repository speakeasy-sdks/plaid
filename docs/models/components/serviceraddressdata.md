# ServicerAddressData

The address of the student loan servicer. This is generally the remittance address to which payments should be sent.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `additional_properties`                                      | Dict[str, *Any*]                                             | :heavy_minus_sign:                                           | N/A                                                          |
| `city`                                                       | *Optional[str]*                                              | :heavy_check_mark:                                           | The full city name                                           |
| `country`                                                    | *Optional[str]*                                              | :heavy_check_mark:                                           | The ISO 3166-1 alpha-2 country code                          |
| `postal_code`                                                | *Optional[str]*                                              | :heavy_check_mark:                                           | The postal code                                              |
| `region`                                                     | *Optional[str]*                                              | :heavy_check_mark:                                           | The region or state<br/>Example: `"NC"`                      |
| `street`                                                     | *Optional[str]*                                              | :heavy_check_mark:                                           | The full street address<br/>Example: `"564 Main Street, APT 15"` |