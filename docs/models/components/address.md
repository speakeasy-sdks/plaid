# Address

A physical mailing address.


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `data`                                                                    | [components.AddressData](../../models/components/addressdata.md)          | :heavy_check_mark:                                                        | Data about the components comprising an address.                          |
| `additional_properties`                                                   | Dict[str, *Any*]                                                          | :heavy_minus_sign:                                                        | N/A                                                                       |
| `primary`                                                                 | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | When `true`, identifies the address as the primary address on an account. |