import asyncio
import logging

import aiohttp

from src import MyBezeqAPI

logging.basicConfig(level=logging.DEBUG)


async def main():
    session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False), timeout=aiohttp.ClientTimeout(total=60))

    try:
        api = MyBezeqAPI("1234", "password", session)
        print(await api.get_site_config())

        await api.login()
        print("Logged in")

        print(await api.get_dashboard_tab())
        print(await api.get_feeds())
        print(await api.get_invoice_tab())
        print(await api.get_electric_invoice_tab())
        print(await api.get_electricity_tab())

    finally:
        await session.close()


if __name__ == "__main__":  # pragma: no cover
    asyncio.run(main())
