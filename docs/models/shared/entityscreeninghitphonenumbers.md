# EntityScreeningHitPhoneNumbers

Phone number information associated with the entity screening hit


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `additional_properties`                                                  | Dict[str, *Any*]                                                         | :heavy_minus_sign:                                                       | N/A                                                                      |                                                                          |
| `phone_number`                                                           | *str*                                                                    | :heavy_check_mark:                                                       | A phone number in E.164 format.                                          | +14025671234                                                             |
| `type`                                                                   | [components.PhoneType](../../models/shared/phonetype.md)                 | :heavy_check_mark:                                                       | An enum indicating whether a phone number is a phone line or a fax line. |                                                                          |