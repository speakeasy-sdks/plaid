# PhoneNumber

A phone number


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `data`                                                                        | *str*                                                                         | :heavy_check_mark:                                                            | The phone number.                                                             |
| `primary`                                                                     | *bool*                                                                        | :heavy_check_mark:                                                            | When `true`, identifies the phone number as the primary number on an account. |
| `type`                                                                        | [components.PhoneNumberType](../../models/components/phonenumbertype.md)      | :heavy_check_mark:                                                            | The type of phone number.                                                     |
| `additional_properties`                                                       | Dict[str, *Any*]                                                              | :heavy_minus_sign:                                                            | N/A                                                                           |