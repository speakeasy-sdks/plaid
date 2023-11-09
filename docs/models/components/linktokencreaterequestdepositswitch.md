# LinkTokenCreateRequestDepositSwitch

Specifies options for initializing Link for use with the Deposit Switch (beta) product. This field is required if `deposit_switch` is included in the `products` array.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `deposit_switch_id`                                                        | *str*                                                                      | :heavy_check_mark:                                                         | The `deposit_switch_id` provided by the `/deposit_switch/create` endpoint. |