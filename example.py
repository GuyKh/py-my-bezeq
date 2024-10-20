import asyncio
import calendar
import logging
import os
from datetime import date, timedelta

import aiohttp

from my_bezeq import ElectricReportLevel, MyBezeqAPI

logging.basicConfig(level=logging.INFO)


async def main():
    session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False), timeout=aiohttp.ClientTimeout(total=60))
    username = os.environ['MY_BEZEQ_USERNAME'] or "12345"
    password = os.environ['MY_BEZEQ_PASSWORD'] or "password"

    try:
        api = MyBezeqAPI(username, password, session)
        # print(await api.get_site_config())

        await api.login()
        print("Logged in")

        print(await api.dashboard.get_dashboard_tab())
        print(await api.internet.get_feeds())
        print(await api.invoices.get_invoice_tab())
        print(await api.invoices.get_electric_invoice_tab())
        print(await api.electric.get_electricity_tab("12345"))
        print(await api.dashboard.get_customer_messages())

        today = date.today()
        last_day_of_month = calendar.monthrange(today.year, today.month)[1]

        print(await api.electric.get_elec_usage_report(ElectricReportLevel.HOURLY, today - timedelta(days=5),
                                               today - timedelta(days=4)))
        print(await api.electric.get_elec_usage_report(ElectricReportLevel.DAILY, today.replace(day=1),
                                              today.replace(day=last_day_of_month)))
        print(await api.electric.get_elec_usage_report(ElectricReportLevel.MONTHLY, today + timedelta(days=1), today))


    finally:
        await session.close()


if __name__ == "__main__":  # pragma: no cover
    asyncio.run(main())
