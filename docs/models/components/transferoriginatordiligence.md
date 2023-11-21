# TransferOriginatorDiligence

The diligence information for the originator.


## Fields

| Field                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `address`                                                                                                                                                                                                                       | [components.TransferOriginatorAddress](../../models/components/transferoriginatoraddress.md)                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                              | The originator's address.                                                                                                                                                                                                       |
| `credit_usage_configuration`                                                                                                                                                                                                    | [Optional[components.TransferCreditUsageConfiguration]](../../models/components/transfercreditusageconfiguration.md)                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                              | Specifies the originator's expected usage of credits. For all dollar amounts, use a decimal string with two digits of precision e.g. "10.00". This field is required if the originator is expected to process credit transfers. |
| `dba`                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                              | The business name of the originator.                                                                                                                                                                                            |
| `debit_usage_configuration`                                                                                                                                                                                                     | [Optional[components.TransferDebitUsageConfiguration]](../../models/components/transferdebitusageconfiguration.md)                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                              | Specifies the originator's expected usage of debits. For all dollar amounts, use a decimal string with two digits of precision e.g. "10.00". This field is required if the originator is expected to process debit transfers.   |
| `naics_code`                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                              | The NAICS code of the originator.                                                                                                                                                                                               |
| `tax_id`                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                              | The tax ID of the originator.                                                                                                                                                                                                   |
| `website`                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                              | The website of the originator.                                                                                                                                                                                                  |