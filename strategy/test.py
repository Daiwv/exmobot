#coding=utf-8
import random


def run(capi, logger, storage, conf=None, **params):
    #print capi.delete_orders(['BTC_USD'])
    #print action.delete_orders_for_pair('ETH_USD')
    #print capi.orders_balance()

    '''
    user_info = exmo.user_info()
    eth_amount = user_info['balances']['ETH']

    price =11.29897
    pair = 'ETH_USD'
    order_type = 'sell'
    quantity = eth_amount

    print exmo.order_create(pair=pair, price=price, order_type= order_type, quantity=eth_amount)

    '''

    #print capi.user_orders()
    #print capi.ticker()
    #print capi.user_trades(['BTC_USD'])
    #print capi.user_cancelled_orders(100000, 1000)
    #print capi.order_trades(48267083)
    #print capi.required_amount('BTC_USD', 1)
    #logger.info(res)
    #print res
    #print capi.
    #print capi.order_trades()
    #storage.save('key1', 'value1')
    #storage.save('key2', 'value1')
    #print storage.load('key2')
    #print storage.get_utime('key2')
    #storage.delete('key2')
    #print capi.balance_full()
    ids = random.randrange(100000, 200000, 1)
    storage.order_add(ids, 'ETH_USD', 10.5, 12.45, 'sell', '123')
    storage.order_add(ids+1, 'BTC_USD', 1.1, 645.45, 'sell', '123')
    print storage.orders(session_id='123')
    print '-' * 40
    print storage.orders(pair='LTC_USD', session_id='123')
    storage.order_delete(pair='BTC_USD', session_id='123')
    storage.old_orders_delete(utime=1469620306, pair='ETH_USD', session_id='123')
