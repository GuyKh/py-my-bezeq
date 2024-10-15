BASE_URL = "https://my-api.bezeq.co.il/"
BASE_URL_WITH_VERSION = "https://my-api.bezeq.co.il/{version}/"

VERSION_URL = "https://my.bezeq.co.il/version.json"
USERNAME_LOGIN_URL = BASE_URL_WITH_VERSION + "api/Auth/LoginByUserName"
DASHBOARD_URL = BASE_URL_WITH_VERSION + "api/Dashboard/GetDashboard"
CUSTOMER_MESSAGES_URL = BASE_URL_WITH_VERSION + "api/Dashboard/GetCustomerMessages"
INVOICES_URL = BASE_URL_WITH_VERSION + "api/InvoicesTab/GetInvoicesTab"
FEEDS_URL = BASE_URL_WITH_VERSION + "api/InternetTab/GetFeeds"
ELECTRIC_INVOICES_PDF_URL = (
    BASE_URL_WITH_VERSION + "api/GeneralActions/GetInvoiceById?InvoiceId={invoice_id}&JWTToken={jwt_token}"
)
ELECTRIC_INVOICES_URL = BASE_URL_WITH_VERSION + "api/InvoicesTab/GetElectInvoiceTab"
ELECTRIC_REPORT_BY_DAY_URL = BASE_URL_WITH_VERSION + "api/ElectricityTab/GetElectReportByDay"
ELECTRIC_REPORT_BY_MONTH_URL = BASE_URL_WITH_VERSION + "api/ElectricityTab/GetElectReportByMonth"
ELECTRIC_REPORT_BY_YEAR_URL = BASE_URL_WITH_VERSION + "api/ElectricityTab/GetElectReportByYear"
ELECTRICITY_TAB_URL = BASE_URL_WITH_VERSION + "api/ElectricityTab/GetElectricityTab"
SITE_CONFIG_URL = BASE_URL_WITH_VERSION + "api/GeneralActions/GetSiteConfig"
