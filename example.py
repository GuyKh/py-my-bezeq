import asyncio
import logging
from datetime import date, timedelta

import aiohttp

from my_bezeq import ElectricReportLevel, MyBezeqAPI

logging.basicConfig(level=logging.DEBUG)


async def main():
    session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False), timeout=aiohttp.ClientTimeout(total=60))

    try:
        api = MyBezeqAPI("1234", "pass", session)
        # print(await api.get_site_config())

        await api.login()
        print("Logged in")

        print(await api.get_dashboard_tab())
        print(await api.get_feeds())
        print(await api.get_invoice_tab())
        print(await api.get_electric_invoice_tab())
        print(await api.get_electricity_tab())

        yesterday = date.today() - timedelta(days=1)
        print(await api.get_elec_usage_report(ElectricReportLevel.HOURLY, yesterday, yesterday))
        print(await api.get_elec_usage_report(ElectricReportLevel.DAILY, yesterday, yesterday))


    finally:
        await session.close()


if __name__ == "__main__":  # pragma: no cover
    asyncio.run(main())
