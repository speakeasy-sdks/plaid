# LiabilitiesObject

An object containing liability accounts


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `credit`                                                                               | List[[components.CreditCardLiability](../../models/components/creditcardliability.md)] | :heavy_check_mark:                                                                     | The credit accounts returned.                                                          |
| `mortgage`                                                                             | List[[components.MortgageLiability](../../models/components/mortgageliability.md)]     | :heavy_check_mark:                                                                     | The mortgage accounts returned.                                                        |
| `student`                                                                              | List[[components.StudentLoan](../../models/components/studentloan.md)]                 | :heavy_check_mark:                                                                     | The student loan accounts returned.                                                    |
| `additional_properties`                                                                | Dict[str, *Any*]                                                                       | :heavy_minus_sign:                                                                     | N/A                                                                                    |