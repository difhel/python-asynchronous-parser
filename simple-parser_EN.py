'''
Simple asynchronous Python Parser
License: MIT
Author: Mark Fomin
Contact: luring.uliksir@gmail.com
'''

#some imports
import aiohttp
import asyncio

#create the main function. It will be used as main worker.
async def main():
    #create the asynchronous session
    async with aiohttp.ClientSession() as session:
        #create GET-request from official VK Page of the developer of the parser
        async with session.get("https://vk.com/na_official") as response:
            #print the response status code
            print("Status:", response.status)
            #print the content-type
            print("Content-type:", response.headers['content-type'])
            #create variable with the text of the page
            html = await response.text()
            #print it
            print("Body:", html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())