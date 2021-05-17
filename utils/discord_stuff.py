from operator import itemgetter
import aiohttp
import typing


async def get_bot_guilds(aio_session: aiohttp.ClientSession=None, *, token=None) -> tuple:
    if aio_session is None:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://discord.com/api/v6/users/@me/guilds",
            headers={"Authorization": f"Bot {token}"}) as response:
                return await response.json()
    async with aio_session.get("https://discord.com/api/v6/users/@me/guilds",
            headers={"Authorization": f"Bot {token}"}) as response:
        return await response.json()

def _get_ids_from_li(_li: list) -> list:
    return list(map(itemgetter("id"), _li))

async def get_mutuals(user_gs: list, user_two: list = None, *, token: str=None, perms: typing.Union[str, list]='administrator') -> list:

    if user_two is None:
        user_two = await get_bot_guilds(token=token)
    
    bg_in_id = _get_ids_from_li(user_two)
    print(bg_in_id)
    if isinstance(perms, list):
        return [guild for guild in user_gs if (str(guild.id) in bg_in_id) and 
                    all(getattr(guild.permissions, permission) for permission in perms)]
    return [guild for guild in user_gs if (str(guild.id) in bg_in_id) and getattr(guild.permissions, perms)]