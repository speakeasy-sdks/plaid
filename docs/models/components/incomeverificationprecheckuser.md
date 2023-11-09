# IncomeVerificationPrecheckUser

Information about the user whose eligibility is being evaluated.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `email_address`                                                                        | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | The user's email address                                                               |
| `first_name`                                                                           | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | The user's first name                                                                  |
| `home_address`                                                                         | [Optional[components.SignalAddressData]](../../models/components/signaladdressdata.md) | :heavy_minus_sign:                                                                     | Data about the components comprising an address.                                       |
| `last_name`                                                                            | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | The user's last name                                                                   |