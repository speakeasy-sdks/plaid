# ClientProvidedTransactionLocation

A representation of where a transaction took place.

Use this field to pass in structured location information you may have about your transactions. Providing location data is optional but can increase result quality. If you have unstructured location information, it may be appended to the `description` field.


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `additional_properties`                             | Dict[str, *Any*]                                    | :heavy_minus_sign:                                  | N/A                                                 |
| `address`                                           | *Optional[str]*                                     | :heavy_minus_sign:                                  | The street address where the transaction occurred.  |
| `city`                                              | *Optional[str]*                                     | :heavy_minus_sign:                                  | The city where the transaction occurred.            |
| `country`                                           | *Optional[str]*                                     | :heavy_minus_sign:                                  | The country where the transaction occurred.         |
| `postal_code`                                       | *Optional[str]*                                     | :heavy_minus_sign:                                  | The postal code where the transaction occurred.     |
| `region`                                            | *Optional[str]*                                     | :heavy_minus_sign:                                  | The region or state where the transaction occurred. |