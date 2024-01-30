import asyncio

async def main():
    task = asyncio.create_task(other_funtion())
    print("A")
    await asyncio.sleep(3)
    print("B")
    await task
async def other_funtion():
    print("1")
    await asyncio.sleep(2)
    print("2")
asyncio.run(main())