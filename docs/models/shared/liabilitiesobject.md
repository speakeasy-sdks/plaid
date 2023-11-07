# LiabilitiesObject

An object containing liability accounts


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `additional_properties`                                                            | Dict[str, *Any*]                                                                   | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `credit`                                                                           | List[[components.CreditCardLiability](../../models/shared/creditcardliability.md)] | :heavy_check_mark:                                                                 | The credit accounts returned.                                                      |
| `mortgage`                                                                         | List[[components.MortgageLiability](../../models/shared/mortgageliability.md)]     | :heavy_check_mark:                                                                 | The mortgage accounts returned.                                                    |
| `student`                                                                          | List[[components.StudentLoan](../../models/shared/studentloan.md)]                 | :heavy_check_mark:                                                                 | The student loan accounts returned.                                                |