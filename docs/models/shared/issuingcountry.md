# IssuingCountry

A binary match indicator specifying whether the country that issued the provided document matches the country that the user separately provided to Plaid.

Note: You can configure whether a `no_match` on `issuing_country` fails the `documentary_verification` by editing your Plaid Template.


## Values

| Name       | Value      |
| ---------- | ---------- |
| `MATCH`    | match      |
| `NO_MATCH` | no_match   |