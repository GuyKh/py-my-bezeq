BASE_URL = "https://my-api.bezeq.co.il/"
BASE_URL_WITH_VERSION = "https://my-api.bezeq.co.il/{version}/"

VERSION_URL = "https://my.bezeq.co.il/version.json"

# Auth
USERNAME_LOGIN_URL = BASE_URL_WITH_VERSION + "api/Auth/LoginByUserName"
VERIFY_MOBILE_FIRST_URL = BASE_URL_WITH_VERSION + "api/Auth/VerifyMobileFirst"
VERIFY_BY_PAYMENT_DETAILS_URL = BASE_URL_WITH_VERSION + "api/Auth/VerifyByPaymentDetails"
VERIFY_BY_CUSTOMER_NUMBER_URL = BASE_URL_WITH_VERSION + "api/Auth/VerifyByCustomerNumber"
VERIFY_FOR_MULTIPLE_SUBSCRIBERS_URL = BASE_URL_WITH_VERSION + "api/Auth/VerifyForMultipleSubscribers"
LOGIN_BY_USERNAME_URL = BASE_URL_WITH_VERSION + "api/Auth/LoginByUserName"
VERIFY_OTP_SMS_URL = BASE_URL_WITH_VERSION + "api/Auth/VerifyOtpSms"
SEND_OTP_URL = BASE_URL_WITH_VERSION + "api/Auth/SendOtp"
CHANGE_PASSWORD_URL = BASE_URL_WITH_VERSION + "api/Auth/ChangePassword"
IMP_PERSONATE_URL = BASE_URL_WITH_VERSION + "api/Auth/Impersonate"
REGISTER_SSO_URL = BASE_URL_WITH_VERSION + "api/Auth/RegisterSSO"
GEN_GLASSIX_TOKEN_URL = BASE_URL_WITH_VERSION + "api/Auth/GenGlassixToken"
SET_SUBSCRIBER_URL = BASE_URL_WITH_VERSION + "api/Auth/setSubscriber"

# Dashboard
DASHBOARD_URL = BASE_URL_WITH_VERSION + "api/Dashboard/GetDashboard"
CUSTOMER_MESSAGES_URL = BASE_URL_WITH_VERSION + "api/Dashboard/GetCustomerMessages"
CARD_DATA_URL = BASE_URL_WITH_VERSION + "api/Dashboard/GetCardData"
APPROVE_MESSAGE_URL = BASE_URL_WITH_VERSION + "api/Dashboard/ApproveMessage"
ADD_TO_SPAM_URL = BASE_URL_WITH_VERSION + "api/Dashboard/AddToSpam"
SET_KOSHER_NUM_URL = BASE_URL_WITH_VERSION + "api/Dashboard/SetKosherNum"

# Internet
FEEDS_URL = BASE_URL_WITH_VERSION + "api/InternetTab/GetFeeds"
INTERNET_TAB_URL = BASE_URL_WITH_VERSION + "api/InternetTab/GetInternetTab"
ROUTER_MNG_PAGE_URL = BASE_URL_WITH_VERSION + "api/InternetTab/GetRouterMngPage"
ISP_CARD_URL = BASE_URL_WITH_VERSION + "api/InternetTab/GetIspCard"
BNET_CARD_URL = BASE_URL_WITH_VERSION + "api/InternetTab/GetBnetCard"
EXTENDERS_DETAILS_URL = BASE_URL_WITH_VERSION + "api/InternetTab/GetExtendersDetails"
MESH_MGMT_URL = BASE_URL_WITH_VERSION + "api/InternetTab/GetMeshMgmt"
SET_MESH_NAME_URL = BASE_URL_WITH_VERSION + "api/InternetTab/SetMeshName"
SET_WLAN_URL = BASE_URL_WITH_VERSION + "api/InternetTab/SetWlan"
SEND_BFIBER_LEAD_URL = BASE_URL_WITH_VERSION + "api/InternetTab/SendBfiberLead"
SPEED_TEST_CARD_URL = BASE_URL_WITH_VERSION + "api/InternetTab/GetSpeeTestdCard"
REGISTERED_DEVICES_URL = BASE_URL_WITH_VERSION + "api/InternetTab/GetRegisteredDevices"
UPDATE_DEVICE_NAME_URL = BASE_URL_WITH_VERSION + "api/InternetTab/UpdateDeviceName"
UPDATE_ZONE_URL = BASE_URL_WITH_VERSION + "api/InternetTab/UpdateZone"
UPDATE_CYBER_PROTECTION_URL = BASE_URL_WITH_VERSION + "api/InternetTab/UpdateCyberProtection"
ADD_PORT_URL = BASE_URL_WITH_VERSION + "api/InternetTab/AddPort"
DELETE_PORT_URL = BASE_URL_WITH_VERSION + "api/InternetTab/DeletePort"
PORTS_URL = BASE_URL_WITH_VERSION + "api/InternetTab/GetPorts"
UPDATE_TRACKED_DEVICE_URL = BASE_URL_WITH_VERSION + "api/InternetTab/UpdateTrackedDevice"
DELETE_TRACKED_DEVICE_URL = BASE_URL_WITH_VERSION + "api/InternetTab/DeleteTrackedDevice"
WIFI_DATA_URL = BASE_URL_WITH_VERSION + "api/InternetTab/GetWifiData"
SET_WIFI_DATA_URL = BASE_URL_WITH_VERSION + "api/InternetTab/SetWifiData"

# Invoices
INVOICES_URL = BASE_URL_WITH_VERSION + "api/InvoicesTab/GetInvoicesTab"
SET_BEN_URL = BASE_URL_WITH_VERSION + "api/InvoicesTab/SetBen"
SET_ELECT_BEN_URL = BASE_URL_WITH_VERSION + "api/InvoicesTab/SetElectBen"
GET_INVOICES_PDF_URL = (
    BASE_URL_WITH_VERSION + "api/GeneralActions/GetInvoiceById?InvoiceId={invoice_id}&JWTToken={jwt_token}"
)
GET_INVOICES_EXCEL_URL = (
    BASE_URL_WITH_VERSION + "api/GeneralActions/GetExcelInvoiceById?InvoiceId={invoice_id}&JWTToken={jwt_token}"
)
ELECTRIC_INVOICES_URL = BASE_URL_WITH_VERSION + "api/InvoicesTab/GetElectInvoiceTab"

# Electricity
ELECTRIC_REPORT_BY_DAY_URL = BASE_URL_WITH_VERSION + "api/ElectricityTab/GetElectReportByDay"
ELECTRIC_REPORT_BY_MONTH_URL = BASE_URL_WITH_VERSION + "api/ElectricityTab/GetElectReportByMonth"
ELECTRIC_REPORT_BY_YEAR_URL = BASE_URL_WITH_VERSION + "api/ElectricityTab/GetElectReportByYear"
ELECTRICITY_TAB_URL = BASE_URL_WITH_VERSION + "api/ElectricityTab/GetElectricityTab"
SET_ELECT_SUBSCRIBER_URL = BASE_URL_WITH_VERSION + "api/ElectricityTab/SetElectSubscriber"

# Personal
PERSONAL_URL = BASE_URL_WITH_VERSION + "api/PersonalTab/GetPersonalTab"
UPDATE_USER_DETAILS_URL = BASE_URL_WITH_VERSION + "api/PersonalTab/UpdateUserDetails"

# General Actions
SITE_CONFIG_URL = BASE_URL_WITH_VERSION + "api/GeneralActions/GetSiteConfig"
SEND_WEBTRENDS_API_URL = BASE_URL_WITH_VERSION + "api/GeneralActions/SendWebtrends"
START_ACTIONS_URL = BASE_URL_WITH_VERSION + "api/GeneralActions/GetStartActions"
MENU_URL = BASE_URL_WITH_VERSION + "api/GeneralActions/GetMenu"

# Tech Coordinator API
TIME_WINDOWS_URL = BASE_URL_WITH_VERSION + "api/TechCoord/GetTimeWindows"
ASSIGN_TIME_WINDOW_URL = BASE_URL_WITH_VERSION + "api/TechCoord/AssignTimeWindow"
CANCEL_TECHNICIAN_URL = BASE_URL_WITH_VERSION + "api/TechCoord/CancelTechnician"

# Phone API
PHONE_TAB_URL = BASE_URL_WITH_VERSION + "api/PhoneTab/GetPhoneTab"
CALL_LOG_URL = BASE_URL_WITH_VERSION + "api/PhoneTab/GetCallLog"
CALL_LOG_EXCEL_URL = (
    BASE_URL_WITH_VERSION + "api/PhoneTab/GetCallLogExcel?FromDate={from_date}}&ToDate={to_date}&JWTToken={jwt_token}"
)
SEND_SMS_URL = BASE_URL_WITH_VERSION + "api/PhoneTab/SendSms"
