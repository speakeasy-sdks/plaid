# CreditPayStubAddress

Address on the pay stub.


## Fields

| Field                                | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `city`                               | *Optional[str]*                      | :heavy_check_mark:                   | The full city name.                  |
| `country`                            | *Optional[str]*                      | :heavy_check_mark:                   | The ISO 3166-1 alpha-2 country code. |
| `postal_code`                        | *Optional[str]*                      | :heavy_check_mark:                   | The postal code of the address.      |
| `region`                             | *Optional[str]*                      | :heavy_check_mark:                   | The region or state.<br/>Example: `"NC"` |
| `street`                             | *Optional[str]*                      | :heavy_check_mark:                   | The full street address.             |
| `additional_properties`              | Dict[str, *Any*]                     | :heavy_minus_sign:                   | N/A                                  |