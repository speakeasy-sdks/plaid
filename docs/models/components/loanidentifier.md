# LoanIdentifier

The information used to identify this loan by various parties to the transaction or other organizations.


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `loan_identifier`                                                                        | *Optional[str]*                                                                          | :heavy_check_mark:                                                                       | The value of the identifier for the specified type.                                      |
| `loan_identifier_type`                                                                   | [Optional[components.LoanIdentifierType]](../../models/components/loanidentifiertype.md) | :heavy_check_mark:                                                                       | A value from a MISMO prescribed list that specifies the type of loan identifier.         |
| `additional_properties`                                                                  | Dict[str, *Any*]                                                                         | :heavy_minus_sign:                                                                       | N/A                                                                                      |