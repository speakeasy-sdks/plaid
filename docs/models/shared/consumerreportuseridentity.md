# ConsumerReportUserIdentity

ConsumerReportUserIdentity defines the user identity data collected for consumer report purpose. This field is required to be set if you later use the created user for consumer report purpose.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `additional_properties`                                      | Dict[str, *Any*]                                             | :heavy_minus_sign:                                           | N/A                                                          |
| `emails`                                                     | List[*str*]                                                  | :heavy_check_mark:                                           | The user's emails                                            |
| `first_name`                                                 | *str*                                                        | :heavy_check_mark:                                           | The user's first name                                        |
| `last_name`                                                  | *str*                                                        | :heavy_check_mark:                                           | The user's last name                                         |
| `phone_numbers`                                              | List[*str*]                                                  | :heavy_check_mark:                                           | The user's phone numbers                                     |
| `primary_address`                                            | [components.AddressData](../../models/shared/addressdata.md) | :heavy_check_mark:                                           | Data about the components comprising an address.             |