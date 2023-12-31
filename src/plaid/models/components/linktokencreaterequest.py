"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .consumerreportpermissiblepurpose import ConsumerReportPermissiblePurpose
from .countrycode import CountryCode
from .linktokenaccountfilters import LinkTokenAccountFilters
from .linktokencreatehostedlink import LinkTokenCreateHostedLink
from .linktokencreateinstitutiondata import LinkTokenCreateInstitutionData
from .linktokencreaterequestauth import LinkTokenCreateRequestAuth
from .linktokencreaterequestbasereport import LinkTokenCreateRequestBaseReport
from .linktokencreaterequestdepositswitch import LinkTokenCreateRequestDepositSwitch
from .linktokencreaterequestemployment import LinkTokenCreateRequestEmployment
from .linktokencreaterequestidentityverification import LinkTokenCreateRequestIdentityVerification
from .linktokencreaterequestincomeverification import LinkTokenCreateRequestIncomeVerification
from .linktokencreaterequestpaymentinitiation import LinkTokenCreateRequestPaymentInitiation
from .linktokencreaterequeststatements import LinkTokenCreateRequestStatements
from .linktokencreaterequesttransfer import LinkTokenCreateRequestTransfer
from .linktokencreaterequestupdate import LinkTokenCreateRequestUpdate
from .linktokencreaterequestuser import LinkTokenCreateRequestUser
from .linktokeneuconfig import LinkTokenEUConfig
from .linktokeninvestments import LinkTokenInvestments
from .linktokeninvestmentsauth import LinkTokenInvestmentsAuth
from .products import Products
from dataclasses_json import Undefined, dataclass_json
from plaid import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LinkTokenCreateRequest:
    r"""LinkTokenCreateRequest defines the request schema for `/link/token/create`"""
    client_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_name') }})
    r"""The name of your application, as it should be displayed in Link. Maximum length of 30 characters. If a value longer than 30 characters is provided, Link will display \\"This Application\\" instead."""
    country_codes: List[CountryCode] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country_codes') }})
    r"""Specify an array of Plaid-supported country codes using the ISO-3166-1 alpha-2 country code standard. Institutions from all listed countries will be shown. For a complete mapping of supported products by country, see https://plaid.com/global/.

    If Link is launched with multiple country codes, only products that you are enabled for in all countries will be used by Link. Note that while all countries are enabled by default in Sandbox and Development, in Production only US and Canada are enabled by default. Access to European institutions requires additional compliance steps. To request access to European institutions in the Production environment, [file a product access Support ticket](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access) via the Plaid dashboard. If you initialize with a European country code, your users will see the European consent panel during the Link flow.

    If using a Link customization, make sure the country codes in the customization match those specified in `country_codes`, or the customization may not be applied.

    If using the Auth features Instant Match, Same-day Micro-deposits, or Automated Micro-deposits, `country_codes` must be set to `['US']`.
    """
    language: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('language') }})
    r"""The language that Link should be displayed in. When initializing with Identity Verification, this field is not used; for more details, see [Identity Verification supported languages](https://www.plaid.com/docs/identity-verification/#supported-languages).

    Supported languages are:
    - Danish (`'da'`)
    - Dutch (`'nl'`)
    - English (`'en'`)
    - Estonian (`'et'`)
    - French (`'fr'`)
    - German (`'de'`)
    - Italian (`'it'`)
    - Latvian (`'lv'`)
    - Lithuanian (`'lt'`)
    - Norwegian (`'no'`)
    - Polish (`'pl'`)
    - Portuguese (`'pt'`)
    - Romanian (`'ro'`)
    - Spanish (`'es'`)
    - Swedish (`'sv'`)

    When using a Link customization, the language configured here must match the setting in the customization, or the customization will not be applied.
    """
    user: LinkTokenCreateRequestUser = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    r"""An object specifying information about the end user who will be linking their account."""
    access_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token'), 'exclude': lambda f: f is None }})
    r"""The `access_token` associated with the Item to update or reference, used when updating, modifying, or accessing an existing `access_token`. Used when launching Link in update mode, when completing the Same-day (manual) Micro-deposit flow, or (optionally) when initializing Link for a returning user as part of the Transfer UI flow."""
    account_filters: Optional[LinkTokenAccountFilters] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_filters'), 'exclude': lambda f: f is None }})
    r"""By default, Link will provide limited account filtering: it will only display Institutions that are compatible with all products supplied in the `products` parameter of `/link/token/create`, and, if `auth` is specified in the `products` array, will also filter out accounts other than `checking` and `savings` accounts on the Account Select pane. You can further limit the accounts shown in Link by using `account_filters` to specify the account subtypes to be shown in Link. Only the specified subtypes will be shown. This filtering applies to both the Account Select view (if enabled) and the Institution Select view. Institutions that do not support the selected subtypes will be omitted from Link. To indicate that all subtypes should be shown, use the value `\\"all\\"`. If the `account_filters` filter is used, any account type for which a filter is not specified will be entirely omitted from Link. For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#account-type-schema).

    For institutions using OAuth, the filter will not affect the list of accounts shown by the bank in the OAuth window.
    """
    additional_consented_products: Optional[List[Products]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additional_consented_products'), 'exclude': lambda f: f is None }})
    r"""(Beta) This field has no effect unless you are participating in the [Data Transparency](https://plaid.com/docs/link/data-transparency-messaging-migration-guide) beta program.
    List of additional Plaid product(s) you wish to collect consent for. These products will not be billed until you start using them by calling the relevant endpoints.

    `balance` is *not* a valid value, the Balance product does not require explicit initialization and will automatically have consent collected.

    Institutions that do not support these products will still be shown in Link
    """
    android_package_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('android_package_name'), 'exclude': lambda f: f is None }})
    r"""The name of your app's Android package. Required if using the `link_token` to initialize Link on Android. Any package name specified here must also be added to the Allowed Android package names setting on the [developer dashboard](https://dashboard.plaid.com/team/api). When creating a `link_token` for initializing Link on other platforms, `android_package_name` must be left blank and `redirect_uri` should be used instead."""
    auth: Optional[LinkTokenCreateRequestAuth] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth'), 'exclude': lambda f: f is None }})
    r"""Specifies options for initializing Link for use with the Auth product. This field can be used to enable or disable extended Auth flows for the resulting Link session. Omitting any field will result in a default that can be configured by your account manager."""
    base_report: Optional[LinkTokenCreateRequestBaseReport] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('base_report'), 'exclude': lambda f: f is None }})
    r"""Specifies options for initializing Link for use with the Base Report product. This field is required if `assets` is included in the `products` array and the client is CRA-enabled."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    consumer_report_permissible_purpose: Optional[ConsumerReportPermissiblePurpose] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('consumer_report_permissible_purpose'), 'exclude': lambda f: f is None }})
    r"""This enum describes the reason a consumer report is created for

    `ACCOUNT_REVIEW_CREDIT`: In connection with a consumer credit transaction for the review or collection of an account pursuant to FCRA Section 604(a)(3)(A).
    `ACCOUNT_REVIEW_NON_CREDIT`: For a legitimate business need of the information to review a non-credit account provided primarily for personal, family, or household purposes to determine whether the consumer continues to meet the terms of the account pursuant to FCRA Section 604(a)(3)(F)(2).
    `EMPLOYMENT`: For employment purposes pursuant to FCRA 604(a)(3)(B), including hiring, retention and promotion purposes.
    `EXTENSION_OF_CREDIT`: In connection with a credit transaction initiated by and involving the consumer pursuant to FCRA Section 604(a)(3)(A).
    `LEGITIMATE_BUSINESS_NEED_TENANT_SCREENING`: For a legitimate business need in connection with a business transaction initiated by the consumer primarily for personal, family, or household purposes in connection with a property rental assessment pursuant to FCRA Section 604(a)(3)(F)(i).
    `LEGITIMATE_BUSINESS_NEED_OTHER`: For a legitimate business need in connection with a business transaction made primarily for personal, family, or household initiated by the consumer pursuant to FCRA Section 604(a)(3)(F)(i).
    `WRITTEN_INSTRUCTION_PREQUALIFICATION`: In accordance with the written instructions of the consumer pursuant to FCRA Section 604(a)(2), to evaluate an application’s profile to make an offer to the consumer.
    `WRITTEN_INSTRUCTION_OTHER`: In accordance with the written instructions of the consumer pursuant to FCRA Section 604(a)(2), such as when an individual agrees to act as a guarantor or assumes personal liability for a consumer, business, or commercial loan.
    """
    deposit_switch: Optional[LinkTokenCreateRequestDepositSwitch] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deposit_switch'), 'exclude': lambda f: f is None }})
    r"""Specifies options for initializing Link for use with the Deposit Switch (beta) product. This field is required if `deposit_switch` is included in the `products` array."""
    employment: Optional[LinkTokenCreateRequestEmployment] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('employment'), 'exclude': lambda f: f is None }})
    r"""Specifies options for initializing Link for use with the Employment product. This field is required if `employment` is included in the `products` array."""
    eu_config: Optional[LinkTokenEUConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eu_config'), 'exclude': lambda f: f is None }})
    r"""Configuration parameters for EU flows"""
    hosted_link: Optional[LinkTokenCreateHostedLink] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hosted_link'), 'exclude': lambda f: f is None }})
    r"""Configuration parameters for Hosted Link"""
    identity_verification: Optional[LinkTokenCreateRequestIdentityVerification] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('identity_verification'), 'exclude': lambda f: f is None }})
    r"""Specifies option for initializing Link for use with the Identity Verification product."""
    income_verification: Optional[LinkTokenCreateRequestIncomeVerification] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('income_verification'), 'exclude': lambda f: f is None }})
    r"""Specifies options for initializing Link for use with the Income product. This field is required if `income_verification` is included in the `products` array."""
    institution_data: Optional[LinkTokenCreateInstitutionData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution_data'), 'exclude': lambda f: f is None }})
    r"""A map containing data used to highlight institutions in Link."""
    institution_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution_id'), 'exclude': lambda f: f is None }})
    r"""Used for certain Europe-only configurations, as well as certain legacy use cases in other regions."""
    investments: Optional[LinkTokenInvestments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('investments'), 'exclude': lambda f: f is None }})
    r"""Configuration parameters for the Investments product"""
    investments_auth: Optional[LinkTokenInvestmentsAuth] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('investments_auth'), 'exclude': lambda f: f is None }})
    r"""Configuration parameters for the Investments Auth Product"""
    link_customization_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_customization_name'), 'exclude': lambda f: f is None }})
    r"""The name of the Link customization from the Plaid Dashboard to be applied to Link. If not specified, the `default` customization will be used. When using a Link customization, the language in the customization must match the language selected via the `language` parameter, and the countries in the customization should match the country codes selected via `country_codes`."""
    payment_initiation: Optional[LinkTokenCreateRequestPaymentInitiation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_initiation'), 'exclude': lambda f: f is None }})
    r"""Specifies options for initializing Link for use with the Payment Initiation (Europe) product. This field is required if `payment_initiation` is included in the `products` array. Either `payment_id` or `consent_id` must be provided."""
    products: Optional[List[Products]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('products'), 'exclude': lambda f: f is None }})
    r"""List of Plaid product(s) you wish to use. If launching Link in update mode, should be omitted (unless you are using update mode to add Income or Assets to an Item); required otherwise.

    `balance` is *not* a valid value, the Balance product does not require explicit initialization and will automatically be initialized when any other product is initialized.

    The products specified here will determine which institutions will be available to your users in Link. Only institutions that support *all* requested products can be selected; a if a user attempts to select an institution that does not support a listed product, a \"Connectivity not supported\" error message will appear in Link. To maximize the number of institutions available, initialize Link with the minimal product set required for your use case. Additional products can be included via the [`required_if_supported_products`](https://plaid.com/docs/api/tokens/#link-token-create-request-required-if-supported-products) field, or can be initialized by calling the endpoint after obtaining an access token. For details and exceptions, see [Choosing when to initialize products](https://plaid.com/docs/link/initializing-products/).

    Note that, unless you have opted to disable Instant Match support, institutions that support Instant Match will also be shown in Link if `auth` is specified as a product, even though these institutions do not contain `auth` in their product array.

    In Production, you will be billed for each product that you specify when initializing Link. Note that a product cannot be removed from an Item once the Item has been initialized with that product. To stop billing on an Item for subscription-based products, such as Liabilities, Investments, and Transactions, remove the Item via `/item/remove`.
    """
    redirect_uri: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('redirect_uri'), 'exclude': lambda f: f is None }})
    r"""A URI indicating the destination where a user should be forwarded after completing the Link flow; used to support OAuth authentication flows when launching Link in the browser or via a webview. The `redirect_uri` should not contain any query parameters. When used in Production or Development, must be an https URI. To specify any subdomain, use `*` as a wildcard character, e.g. `https://*.example.com/oauth.html`. Note that any redirect URI must also be added to the Allowed redirect URIs list in the [developer dashboard](https://dashboard.plaid.com/team/api). If initializing on Android, `android_package_name` must be specified instead and `redirect_uri` should be left blank."""
    required_if_supported_products: Optional[List[Products]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required_if_supported_products'), 'exclude': lambda f: f is None }})
    r"""List of Plaid product(s) you wish to use only if the institution and account(s) selected by the user support the product. Institutions that do not support these products will still be shown in Link. The products will only be extracted and billed if the user selects an institution and account type that supports them.

    There should be no overlap between `products` and `required_if_supported_products`. The `products` array must have at least one product.

    For more details on using this feature, see [Required if Supported Products](https://www.plaid.com/docs/link/initializing-products/#required-if-supported-products).
    """
    secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret'), 'exclude': lambda f: f is None }})
    r"""Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    statements: Optional[LinkTokenCreateRequestStatements] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statements'), 'exclude': lambda f: f is None }})
    r"""Specifies options for initializing Link for use with the Statements product."""
    transfer: Optional[LinkTokenCreateRequestTransfer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transfer'), 'exclude': lambda f: f is None }})
    r"""Specifies options for initializing Link for use with the Transfer product."""
    update: Optional[LinkTokenCreateRequestUpdate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('update'), 'exclude': lambda f: f is None }})
    r"""Specifies options for initializing Link for [update mode](https://plaid.com/docs/link/update-mode)."""
    user_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_token'), 'exclude': lambda f: f is None }})
    r"""A user token generated using `/user/create`. Any Item created during the Link session will be associated with the user."""
    webhook: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhook'), 'exclude': lambda f: f is None }})
    r"""The destination URL to which any webhooks should be sent. Note that webhooks for Payment Initiation (e-wallet transactions only), Transfer, Bank Transfer (including Auth micro-deposit notification webhooks) and Identity Verification are configured via the Dashboard instead."""
    

