# Hybrid Voice Eval Report

## Summary

| Scenario | Result | Steps Passed |
|----------|--------|--------------|
| cancel_order_001 | ❌ FAIL | 0/2 |
| cancel_order_002 | ❌ FAIL | 0/2 |
| cancel_order_003 | ❌ FAIL | 0/2 |
| cancel_order_004 | ❌ FAIL | 0/2 |
| cancel_order_005 | ❌ FAIL | 0/2 |
| cancel_order_006 | ❌ FAIL | 0/2 |
| cancel_order_007 | ❌ FAIL | 0/1 |
| cancel_order_008 | ❌ FAIL | 0/1 |
| cancel_order_009 | ❌ FAIL | 0/2 |
| cancel_order_010 | ❌ FAIL | 0/2 |
| change_address_001 | ❌ FAIL | 0/2 |
| change_address_002 | ❌ FAIL | 0/2 |
| change_address_003 | ❌ FAIL | 0/2 |
| change_address_004 | ❌ FAIL | 0/2 |
| change_address_005 | ❌ FAIL | 0/2 |
| change_address_006 | ❌ FAIL | 0/2 |
| change_address_007 | ❌ FAIL | 0/1 |
| change_address_008 | ❌ FAIL | 0/1 |
| change_address_009 | ❌ FAIL | 0/2 |
| change_address_010 | ❌ FAIL | 0/2 |
| check_status_001 | ❌ FAIL | 0/2 |
| check_status_002 | ❌ FAIL | 0/2 |
| check_status_003 | ❌ FAIL | 0/2 |
| check_status_004 | ❌ FAIL | 0/2 |
| check_status_005 | ❌ FAIL | 0/2 |
| check_status_006 | ❌ FAIL | 0/2 |
| check_status_007 | ❌ FAIL | 0/1 |
| check_status_008 | ❌ FAIL | 0/1 |
| check_status_009 | ❌ FAIL | 0/2 |
| check_status_010 | ❌ FAIL | 0/2 |
| duplicate_charge_001 | ❌ FAIL | 0/2 |
| duplicate_charge_002 | ❌ FAIL | 0/2 |
| duplicate_charge_003 | ❌ FAIL | 0/2 |
| duplicate_charge_004 | ❌ FAIL | 0/2 |
| duplicate_charge_005 | ❌ FAIL | 0/2 |
| duplicate_charge_006 | ❌ FAIL | 0/2 |
| duplicate_charge_007 | ❌ FAIL | 0/1 |
| duplicate_charge_008 | ❌ FAIL | 0/1 |
| duplicate_charge_009 | ❌ FAIL | 0/2 |
| duplicate_charge_010 | ❌ FAIL | 0/2 |
| missing_package_001 | ❌ FAIL | 0/2 |
| missing_package_002 | ❌ FAIL | 0/2 |
| missing_package_003 | ❌ FAIL | 0/2 |
| missing_package_004 | ❌ FAIL | 0/2 |
| missing_package_005 | ❌ FAIL | 0/2 |
| missing_package_006 | ❌ FAIL | 0/2 |
| missing_package_007 | ❌ FAIL | 0/1 |
| missing_package_008 | ❌ FAIL | 0/1 |
| missing_package_009 | ❌ FAIL | 0/2 |
| missing_package_010 | ❌ FAIL | 0/2 |
| reset_password_001 | ❌ FAIL | 0/2 |
| reset_password_002 | ❌ FAIL | 0/2 |
| reset_password_003 | ❌ FAIL | 0/2 |
| reset_password_004 | ❌ FAIL | 0/2 |
| reset_password_005 | ❌ FAIL | 0/2 |
| reset_password_006 | ❌ FAIL | 0/2 |
| reset_password_007 | ❌ FAIL | 0/1 |
| reset_password_008 | ❌ FAIL | 0/1 |
| reset_password_009 | ❌ FAIL | 0/2 |
| reset_password_010 | ❌ FAIL | 0/2 |
| return_damaged_001 | ❌ FAIL | 0/2 |
| return_damaged_002 | ❌ FAIL | 0/2 |
| return_damaged_003 | ❌ FAIL | 0/2 |
| return_damaged_004 | ❌ FAIL | 0/2 |
| return_damaged_005 | ❌ FAIL | 0/2 |
| return_damaged_006 | ❌ FAIL | 0/2 |
| return_damaged_007 | ❌ FAIL | 0/1 |
| return_damaged_008 | ❌ FAIL | 0/1 |
| return_damaged_009 | ❌ FAIL | 0/2 |
| return_damaged_010 | ❌ FAIL | 0/2 |
| upgrade_sub_001 | ❌ FAIL | 0/2 |
| upgrade_sub_002 | ❌ FAIL | 0/2 |
| upgrade_sub_003 | ❌ FAIL | 0/2 |
| upgrade_sub_004 | ❌ FAIL | 0/2 |
| upgrade_sub_005 | ❌ FAIL | 0/2 |
| upgrade_sub_006 | ❌ FAIL | 0/2 |
| upgrade_sub_007 | ❌ FAIL | 0/1 |
| upgrade_sub_008 | ❌ FAIL | 0/1 |
| upgrade_sub_009 | ❌ FAIL | 0/2 |
| upgrade_sub_010 | ❌ FAIL | 0/2 |

## cancel_order_001: Cancel an order

### Turn 1 ❌

**User Text:** Hi, I'd like to cancel an order I placed earlier today if it hasn't shipped yet.

**User ASR:** hi, i'd like to cancel an order i placed earlier today if it hasn't shipped yet.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/cancel_order_001/user_1.wav](out/audio/cancel_order_001/user_1.wav)
- Bot: [out/audio/cancel_order_001/bot_1.wav](out/audio/cancel_order_001/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** It's order 47382.

**User ASR:** it's order 47,382.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/cancel_order_001/user_2.wav](out/audio/cancel_order_001/user_2.wav)
- Bot: [out/audio/cancel_order_001/bot_2.wav](out/audio/cancel_order_001/bot_2.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## cancel_order_002: Cancel an order

### Turn 1 ❌

**User Text:** Hello, I changed my mind about a purchase and would like to cancel it please.

**User ASR:** hello, i changed my mind about a purchase and would like to cancel it, please.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/cancel_order_002/user_1.wav](out/audio/cancel_order_002/user_1.wav)
- Bot: [out/audio/cancel_order_002/bot_1.wav](out/audio/cancel_order_002/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** The order number is 61250.

**User ASR:** the order number is 61,250.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/cancel_order_002/user_2.wav](out/audio/cancel_order_002/user_2.wav)
- Bot: [out/audio/cancel_order_002/bot_2.wav](out/audio/cancel_order_002/bot_2.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## cancel_order_003: Cancel an order

### Turn 1 ❌

**User Text:** Good afternoon. I need to cancel an order. I found a better price somewhere else.

**User ASR:** good afternoon. i need to cancel an order. i found a better price somewhere else.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/cancel_order_003/user_1.wav](out/audio/cancel_order_003/user_1.wav)
- Bot: [out/audio/cancel_order_003/bot_1.wav](out/audio/cancel_order_003/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Sure thing, it's order 29817.

**User ASR:** sure thing, it's order 29,817.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/cancel_order_003/user_2.wav](out/audio/cancel_order_003/user_2.wav)
- Bot: [out/audio/cancel_order_003/bot_2.wav](out/audio/cancel_order_003/bot_2.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## cancel_order_004: Cancel an order

### Turn 1 ❌

**User Text:** I need to cancel my order right now. The delivery date keeps getting pushed back and I'm done waiting.

**User ASR:** i need to cancel my order right now.  the delivery date keeps getting pushed back and i'm done waiting.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/cancel_order_004/user_1.wav](out/audio/cancel_order_004/user_1.wav)
- Bot: [out/audio/cancel_order_004/bot_1.wav](out/audio/cancel_order_004/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 58463. Just cancel it.

**User ASR:** order 5-8-4-6-3. just cancel it.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/cancel_order_004/user_2.wav](out/audio/cancel_order_004/user_2.wav)
- Bot: [out/audio/cancel_order_004/bot_2.wav](out/audio/cancel_order_004/bot_2.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## cancel_order_005: Cancel an order

### Turn 1 ❌

**User Text:** I've been trying to cancel this order on your app for two days and nothing works. Can you just do it for me?

**User ASR:** i've been trying to cancel this order on your app for two days and nothing works.  can you just do it for me?

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/cancel_order_005/user_1.wav](out/audio/cancel_order_005/user_1.wav)
- Bot: [out/audio/cancel_order_005/bot_1.wav](out/audio/cancel_order_005/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** It's 73916. And your app is terrible by the way.

**User ASR:** it's 73,916 and your app is terrible by the way.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/cancel_order_005/user_2.wav](out/audio/cancel_order_005/user_2.wav)
- Bot: [out/audio/cancel_order_005/bot_2.wav](out/audio/cancel_order_005/bot_2.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## cancel_order_006: Cancel an order

### Turn 1 ❌

**User Text:** Yeah so you charged me the wrong amount and I just want to cancel the whole thing. This is so annoying.

**User ASR:** yes, so you charged me the wrong amount and i just want to cancel the whole thing.  this is so annoying.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/cancel_order_006/user_1.wav](out/audio/cancel_order_006/user_1.wav)
- Bot: [out/audio/cancel_order_006/bot_1.wav](out/audio/cancel_order_006/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 84205. Please confirm it's actually cancelled this time.

**User ASR:** order 8-4-205. please confirm it's actually canceled this time.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/cancel_order_006/user_2.wav](out/audio/cancel_order_006/user_2.wav)
- Bot: [out/audio/cancel_order_006/bot_2.wav](out/audio/cancel_order_006/bot_2.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## cancel_order_007: Cancel an order

### Turn 1 ❌

**User Text:** Hey, I need to cancel order 36710. I accidentally ordered the wrong size.

**User ASR:** hey, i need to cancel order 36710.  i accidentally ordered the wrong size.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/cancel_order_007/user_1.wav](out/audio/cancel_order_007/user_1.wav)
- Bot: [out/audio/cancel_order_007/bot_1.wav](out/audio/cancel_order_007/bot_1.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## cancel_order_008: Cancel an order

### Turn 1 ❌

**User Text:** Can you cancel order 52194 for me? I don't need it anymore.

**User ASR:** can you cancel order 52,194 for me?  i don't need it anymore.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/cancel_order_008/user_1.wav](out/audio/cancel_order_008/user_1.wav)
- Bot: [out/audio/cancel_order_008/bot_1.wav](out/audio/cancel_order_008/bot_1.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## cancel_order_009: Cancel an order

### Turn 1 ❌

**User Text:** Um so I think I wanna cancel something I bought? I'm not even sure if it shipped yet or what.

**User ASR:** i'm so i think i want to cancel something i bought?  i'm not even sure if it's shipped yet or what.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/cancel_order_009/user_1.wav](out/audio/cancel_order_009/user_1.wav)
- Bot: [out/audio/cancel_order_009/bot_1.wav](out/audio/cancel_order_009/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** I think it's uh... order 19548? Let me double check. Yeah, 19548.

**User ASR:** i think it's up, order 19,548?  let me double-check, yeah, 19,548.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/cancel_order_009/user_2.wav](out/audio/cancel_order_009/user_2.wav)
- Bot: [out/audio/cancel_order_009/bot_2.wav](out/audio/cancel_order_009/bot_2.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## cancel_order_010: Cancel an order

### Turn 1 ❌

**User Text:** I don't know, I just want to stop the order from coming. Is it too late? Can I still do that?

**User ASR:** i don't know, i just want to stop the order from coming.  is it too late? can i still do that?

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/cancel_order_010/user_1.wav](out/audio/cancel_order_010/user_1.wav)
- Bot: [out/audio/cancel_order_010/bot_1.wav](out/audio/cancel_order_010/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Oh right. Hold on... order 40673.

**User ASR:** all right, hold on, order 40,673.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/cancel_order_010/user_2.wav](out/audio/cancel_order_010/user_2.wav)
- Bot: [out/audio/cancel_order_010/bot_2.wav](out/audio/cancel_order_010/bot_2.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## change_address_001: Change shipping address

### Turn 1 ❌

**User Text:** Hi, I just realized I put the wrong shipping address on my order. Can I change it?

**User ASR:** hi. i just realized i put the wrong shipping address on my order. can i change it?

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/change_address_001/user_1.wav](out/audio/change_address_001/user_1.wav)
- Bot: [out/audio/change_address_001/bot_1.wav](out/audio/change_address_001/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** It's order 34921.

**User ASR:** it's order 34,921.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/change_address_001/user_2.wav](out/audio/change_address_001/user_2.wav)
- Bot: [out/audio/change_address_001/bot_2.wav](out/audio/change_address_001/bot_2.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## change_address_002: Change shipping address

### Turn 1 ❌

**User Text:** Hello, I recently moved and need to update the delivery address for a package I ordered.

**User ASR:** hello, i recently moved and need to update the delivery address for a package i ordered.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/change_address_002/user_1.wav](out/audio/change_address_002/user_1.wav)
- Bot: [out/audio/change_address_002/bot_1.wav](out/audio/change_address_002/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** The order number is 78215.

**User ASR:** the order number is 78,215.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/change_address_002/user_2.wav](out/audio/change_address_002/user_2.wav)
- Bot: [out/audio/change_address_002/bot_2.wav](out/audio/change_address_002/bot_2.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## change_address_003: Change shipping address

### Turn 1 ❌

**User Text:** Hey, good morning. I need to change where my order gets delivered to, if that's possible.

**User ASR:** hey, good morning. i need to change where my order gets delivered to, if that's possible.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/change_address_003/user_1.wav](out/audio/change_address_003/user_1.wav)
- Bot: [out/audio/change_address_003/bot_1.wav](out/audio/change_address_003/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Sure, order 56043.

**User ASR:** sure, order 56,043.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/change_address_003/user_2.wav](out/audio/change_address_003/user_2.wav)
- Bot: [out/audio/change_address_003/bot_2.wav](out/audio/change_address_003/bot_2.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## change_address_004: Change shipping address

### Turn 1 ❌

**User Text:** I've been trying to change my shipping address on the website for an hour and it won't let me. Can someone just do it?

**User ASR:** i've been trying to change my shipping address on the website for an hour and it won't let me.  can someone just do it?

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/change_address_004/user_1.wav](out/audio/change_address_004/user_1.wav)
- Bot: [out/audio/change_address_004/bot_1.wav](out/audio/change_address_004/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 91387. Please just fix it.

**User ASR:** order 91387. please just fix it.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/change_address_004/user_2.wav](out/audio/change_address_004/user_2.wav)
- Bot: [out/audio/change_address_004/bot_2.wav](out/audio/change_address_004/bot_2.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## change_address_005: Change shipping address

### Turn 1 ❌

**User Text:** My order is shipping to my old address and if it goes there I'm never gonna get it. I need this changed immediately.

**User ASR:** my order is shipping to my old address, and if it goes there i'm never gonna get it.  i need this change immediately.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/change_address_005/user_1.wav](out/audio/change_address_005/user_1.wav)
- Bot: [out/audio/change_address_005/bot_1.wav](out/audio/change_address_005/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** It's 42876. Hurry please, it's supposed to ship tomorrow.

**User ASR:** it's 42,876.  hurry, please.  it's supposed to ship tomorrow.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/change_address_005/user_2.wav](out/audio/change_address_005/user_2.wav)
- Bot: [out/audio/change_address_005/bot_2.wav](out/audio/change_address_005/bot_2.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## change_address_006: Change shipping address

### Turn 1 ❌

**User Text:** This is so frustrating. I already called once and the address still wasn't changed. I need someone to actually update it this time.

**User ASR:** this is so frustrating.  i already called once and the address still wasn't changed.  i need someone to actually update at this time.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/change_address_006/user_1.wav](out/audio/change_address_006/user_1.wav)
- Bot: [out/audio/change_address_006/bot_1.wav](out/audio/change_address_006/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 65739. And please make sure it actually goes through this time.

**User ASR:** order 65739. and please make sure it actually goes through this time.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/change_address_006/user_2.wav](out/audio/change_address_006/user_2.wav)
- Bot: [out/audio/change_address_006/bot_2.wav](out/audio/change_address_006/bot_2.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## change_address_007: Change shipping address

### Turn 1 ❌

**User Text:** Hi, I need to change the shipping address for order 30482. I moved last week.

**User ASR:** hi, i need to change the shipping address for order 30482.  i moved last week.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/change_address_007/user_1.wav](out/audio/change_address_007/user_1.wav)
- Bot: [out/audio/change_address_007/bot_1.wav](out/audio/change_address_007/bot_1.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## change_address_008: Change shipping address

### Turn 1 ❌

**User Text:** Hey, order 87654 needs to go to a different address. Can you update that for me?

**User ASR:** hey, order 87,654 needs to go to a different address.  can you update that for me?

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/change_address_008/user_1.wav](out/audio/change_address_008/user_1.wav)
- Bot: [out/audio/change_address_008/bot_1.wav](out/audio/change_address_008/bot_1.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## change_address_009: Change shipping address

### Turn 1 ❌

**User Text:** So um I think my package might be going to the wrong place? Like I'm not sure if I put the right address in when I ordered.

**User ASR:** so all my think my package might be going to the wrong place?  like i'm not sure if i put the right address in when i ordered.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/change_address_009/user_1.wav](out/audio/change_address_009/user_1.wav)
- Bot: [out/audio/change_address_009/bot_1.wav](out/audio/change_address_009/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Oh right, uh... I think it was order 21456.

**User ASR:** alright, uh, i think it was order 21456.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/change_address_009/user_2.wav](out/audio/change_address_009/user_2.wav)
- Bot: [out/audio/change_address_009/bot_2.wav](out/audio/change_address_009/bot_2.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## change_address_010: Change shipping address

### Turn 1 ❌

**User Text:** I need to like, change something on my order? The address part. I'm not really sure how this works.

**User ASR:** i need to like, change something on my order?  the address part. i'm not really sure how this works.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/change_address_010/user_1.wav](out/audio/change_address_010/user_1.wav)
- Bot: [out/audio/change_address_010/bot_1.wav](out/audio/change_address_010/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Hmm hold on... I got it somewhere. Order 50198.

**User ASR:** homehold on, i got it somewhere, order 50,198.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/change_address_010/user_2.wav](out/audio/change_address_010/user_2.wav)
- Bot: [out/audio/change_address_010/bot_2.wav](out/audio/change_address_010/bot_2.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## check_status_001: Check order status

### Turn 1 ❌

**User Text:** Hi, I was just wondering if you could tell me where my order is? I placed it a few days ago.

**User ASR:** hi, i was just wondering if you could tell me where my order is.  i placed it a few days ago.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/check_status_001/user_1.wav](out/audio/check_status_001/user_1.wav)
- Bot: [out/audio/check_status_001/bot_1.wav](out/audio/check_status_001/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 82714.

**User ASR:** order 82,714.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/check_status_001/user_2.wav](out/audio/check_status_001/user_2.wav)
- Bot: [out/audio/check_status_001/bot_2.wav](out/audio/check_status_001/bot_2.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## check_status_002: Check order status

### Turn 1 ❌

**User Text:** Hello, I'd like to check on the status of a recent order please.

**User ASR:** hello, i'd like to check on the status of a recent border please.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/check_status_002/user_1.wav](out/audio/check_status_002/user_1.wav)
- Bot: [out/audio/check_status_002/bot_1.wav](out/audio/check_status_002/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Yeah, the order number is 59301.

**User ASR:** yeah, the order number is 59,301.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/check_status_002/user_2.wav](out/audio/check_status_002/user_2.wav)
- Bot: [out/audio/check_status_002/bot_2.wav](out/audio/check_status_002/bot_2.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## check_status_003: Check order status

### Turn 1 ❌

**User Text:** Hey there, I'm hoping to get an update on my package. It was supposed to arrive yesterday.

**User ASR:** hey there, i'm hoping to get an update on my package.  it was supposed to arrive yesterday.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/check_status_003/user_1.wav](out/audio/check_status_003/user_1.wav)
- Bot: [out/audio/check_status_003/bot_1.wav](out/audio/check_status_003/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Sure, it's order 46083.

**User ASR:** sure, it's order 46,883.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/check_status_003/user_2.wav](out/audio/check_status_003/user_2.wav)
- Bot: [out/audio/check_status_003/bot_2.wav](out/audio/check_status_003/bot_2.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## check_status_004: Check order status

### Turn 1 ❌

**User Text:** Where's my order? It was supposed to be here three days ago and I've got nothing.

**User ASR:** where's my order? it was supposed to be here three days ago, and i've got nothing.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/check_status_004/user_1.wav](out/audio/check_status_004/user_1.wav)
- Bot: [out/audio/check_status_004/bot_1.wav](out/audio/check_status_004/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 37462. I need an answer.

**User ASR:** order 3-7-4-6-2. i need an answer.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/check_status_004/user_2.wav](out/audio/check_status_004/user_2.wav)
- Bot: [out/audio/check_status_004/bot_2.wav](out/audio/check_status_004/bot_2.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## check_status_005: Check order status

### Turn 1 ❌

**User Text:** I've been waiting for over a week for this package. This is unacceptable. Where is it?

**User ASR:** i've been waiting for over a week for this package.  this is unacceptable. where is it?

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/check_status_005/user_1.wav](out/audio/check_status_005/user_1.wav)
- Bot: [out/audio/check_status_005/bot_1.wav](out/audio/check_status_005/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** It's 71845. Someone better tell me what's going on.

**User ASR:** it's 71,845, someone better tell me what's going on.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/check_status_005/user_2.wav](out/audio/check_status_005/user_2.wav)
- Bot: [out/audio/check_status_005/bot_2.wav](out/audio/check_status_005/bot_2.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## check_status_006: Check order status

### Turn 1 ❌

**User Text:** I'm calling because your tracking page hasn't updated in five days. What is happening with my order?

**User ASR:** i'm calling because your tracking page hasn't updated in five days.  what is happening with my order?

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/check_status_006/user_1.wav](out/audio/check_status_006/user_1.wav)
- Bot: [out/audio/check_status_006/bot_1.wav](out/audio/check_status_006/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 20569. And your website tracking is broken apparently.

**User ASR:** order 20569 and your website tracking is broken apparently.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/check_status_006/user_2.wav](out/audio/check_status_006/user_2.wav)
- Bot: [out/audio/check_status_006/bot_2.wav](out/audio/check_status_006/bot_2.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## check_status_007: Check order status

### Turn 1 ❌

**User Text:** Hey, can I get a status update on order 93471? Just wanna know when it'll be here.

**User ASR:** hey, can i get a status update on order 93471?  just want to know when it'll be here.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/check_status_007/user_1.wav](out/audio/check_status_007/user_1.wav)
- Bot: [out/audio/check_status_007/bot_1.wav](out/audio/check_status_007/bot_1.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## check_status_008: Check order status

### Turn 1 ❌

**User Text:** I'm checking on order 64108. It should have arrived by now, what's the status?

**User ASR:** i'm checking on order 6418.  it should have arrived by now, what's the status?

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/check_status_008/user_1.wav](out/audio/check_status_008/user_1.wav)
- Bot: [out/audio/check_status_008/bot_1.wav](out/audio/check_status_008/bot_1.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## check_status_009: Check order status

### Turn 1 ❌

**User Text:** So like, I ordered something a while back and I'm not really sure if it's coming or not? Is there a way to check?

**User ASR:** so like, i ordered something a while back and i'm not really sure if it's coming or not.  is there a way to check?

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/check_status_009/user_1.wav](out/audio/check_status_009/user_1.wav)
- Bot: [out/audio/check_status_009/bot_1.wav](out/audio/check_status_009/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Um... I think it was order 15923? Or maybe... yeah, 15923.

**User ASR:** um, i think it was order 15,923?  or maybe.  yeah, 15,923.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/check_status_009/user_2.wav](out/audio/check_status_009/user_2.wav)
- Bot: [out/audio/check_status_009/bot_2.wav](out/audio/check_status_009/bot_2.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## check_status_010: Check order status

### Turn 1 ❌

**User Text:** I got an email about something shipping but I don't know which order it was. Can you look it up?

**User ASR:** i got an email about something shipping, but i don't know which order it was.  can you look it up?

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/check_status_010/user_1.wav](out/audio/check_status_010/user_1.wav)
- Bot: [out/audio/check_status_010/bot_1.wav](out/audio/check_status_010/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Hmm let me find it... order 88256 I think.

**User ASR:** him let me find it, order 88,256, i think.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/check_status_010/user_2.wav](out/audio/check_status_010/user_2.wav)
- Bot: [out/audio/check_status_010/bot_2.wav](out/audio/check_status_010/bot_2.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## duplicate_charge_001: Request refund for duplicate charge

### Turn 1 ❌

**User Text:** Hi, I noticed I was charged twice for my last order. I'd like to get a refund for the extra charge please.

**User ASR:** hi, i noticed i was charged twice for my last order.  i'd like to get a refund for the extra charge please.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/duplicate_charge_001/user_1.wav](out/audio/duplicate_charge_001/user_1.wav)
- Bot: [out/audio/duplicate_charge_001/bot_1.wav](out/audio/duplicate_charge_001/bot_1.wav)

**Expected:** {'contains_any': ['last four digits', 'card', 'last four', 'card ending']}

---

### Turn 2 ❌

**User Text:** Sure, the card ends in 4829.

**User ASR:** sure, the card ends in 4,829.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/duplicate_charge_001/user_2.wav](out/audio/duplicate_charge_001/user_2.wav)
- Bot: [out/audio/duplicate_charge_001/bot_2.wav](out/audio/duplicate_charge_001/bot_2.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## duplicate_charge_002: Request refund for duplicate charge

### Turn 1 ❌

**User Text:** Hello, I'm seeing two identical charges on my statement from your store. Could you help me sort that out?

**User ASR:** hello, i'm seeing two identical charges on my statement from your store.  could you help me sort that out?

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/duplicate_charge_002/user_1.wav](out/audio/duplicate_charge_002/user_1.wav)
- Bot: [out/audio/duplicate_charge_002/bot_1.wav](out/audio/duplicate_charge_002/bot_1.wav)

**Expected:** {'contains_any': ['last four digits', 'card', 'last four', 'card ending']}

---

### Turn 2 ❌

**User Text:** It's the card ending in 7163.

**User ASR:** it's the card ending in 7,163.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/duplicate_charge_002/user_2.wav](out/audio/duplicate_charge_002/user_2.wav)
- Bot: [out/audio/duplicate_charge_002/bot_2.wav](out/audio/duplicate_charge_002/bot_2.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## duplicate_charge_003: Request refund for duplicate charge

### Turn 1 ❌

**User Text:** Good afternoon. I was double charged for a purchase and would like a refund on the duplicate.

**User ASR:** good afternoon. i was double-charged for a purchase and would like a refund on the duplicate.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/duplicate_charge_003/user_1.wav](out/audio/duplicate_charge_003/user_1.wav)
- Bot: [out/audio/duplicate_charge_003/bot_1.wav](out/audio/duplicate_charge_003/bot_1.wav)

**Expected:** {'contains_any': ['last four digits', 'card', 'last four', 'card ending']}

---

### Turn 2 ❌

**User Text:** Yeah the last four are 5308.

**User ASR:** yeah, the last 4 or 5,308.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/duplicate_charge_003/user_2.wav](out/audio/duplicate_charge_003/user_2.wav)
- Bot: [out/audio/duplicate_charge_003/bot_2.wav](out/audio/duplicate_charge_003/bot_2.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## duplicate_charge_004: Request refund for duplicate charge

### Turn 1 ❌

**User Text:** I've been charged twice for the same order and this is completely unacceptable. I want my money back right now.

**User ASR:** i've been charged twice for the same order and this is completely unacceptable.  i want my money back right now.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/duplicate_charge_004/user_1.wav](out/audio/duplicate_charge_004/user_1.wav)
- Bot: [out/audio/duplicate_charge_004/bot_1.wav](out/audio/duplicate_charge_004/bot_1.wav)

**Expected:** {'contains_any': ['last four digits', 'card', 'last four', 'card ending']}

---

### Turn 2 ❌

**User Text:** Card ending 9241. How long is this gonna take?

**User ASR:** card ending 9241. how long is this going to take?

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/duplicate_charge_004/user_2.wav](out/audio/duplicate_charge_004/user_2.wav)
- Bot: [out/audio/duplicate_charge_004/bot_2.wav](out/audio/duplicate_charge_004/bot_2.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## duplicate_charge_005: Request refund for duplicate charge

### Turn 1 ❌

**User Text:** This is the third time I've called about this! You guys double charged me and nobody's fixed it yet!

**User ASR:** this is the third time i've called about this.  you guys double charged me and nobody's fixed it yet.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/duplicate_charge_005/user_1.wav](out/audio/duplicate_charge_005/user_1.wav)
- Bot: [out/audio/duplicate_charge_005/bot_1.wav](out/audio/duplicate_charge_005/bot_1.wav)

**Expected:** {'contains_any': ['last four digits', 'card', 'last four', 'card ending']}

---

### Turn 2 ❌

**User Text:** Card ending 3756. I shouldn't have to keep calling.

**User ASR:** card ending 3756. i shouldn't have to keep calling.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/duplicate_charge_005/user_2.wav](out/audio/duplicate_charge_005/user_2.wav)
- Bot: [out/audio/duplicate_charge_005/bot_2.wav](out/audio/duplicate_charge_005/bot_2.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## duplicate_charge_006: Request refund for duplicate charge

### Turn 1 ❌

**User Text:** Seriously? I just checked my bank and there's two charges from you for the exact same amount. Fix this please.

**User ASR:** seriously? i just checked my bank and there's two charges from you for the exact same amount.  fix this please.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/duplicate_charge_006/user_1.wav](out/audio/duplicate_charge_006/user_1.wav)
- Bot: [out/audio/duplicate_charge_006/bot_1.wav](out/audio/duplicate_charge_006/bot_1.wav)

**Expected:** {'contains_any': ['last four digits', 'card', 'last four', 'card ending']}

---

### Turn 2 ❌

**User Text:** It's 6184. And I want a confirmation email.

**User ASR:** it's 6184, and i want a confirmation email.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/duplicate_charge_006/user_2.wav](out/audio/duplicate_charge_006/user_2.wav)
- Bot: [out/audio/duplicate_charge_006/bot_2.wav](out/audio/duplicate_charge_006/bot_2.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## duplicate_charge_007: Request refund for duplicate charge

### Turn 1 ❌

**User Text:** Hey, I got double charged on my card ending 2047 and I need the duplicate refunded.

**User ASR:** hey, i got double charged on my card ending 2047 and i need the duplicate refunded.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/duplicate_charge_007/user_1.wav](out/audio/duplicate_charge_007/user_1.wav)
- Bot: [out/audio/duplicate_charge_007/bot_1.wav](out/audio/duplicate_charge_007/bot_1.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## duplicate_charge_008: Request refund for duplicate charge

### Turn 1 ❌

**User Text:** I see two charges for the same thing on my Visa ending in 8593. Can you reverse one of them?

**User ASR:** i see two charges for the same thing on my visa ending in 8593.  can you reverse one of them?

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/duplicate_charge_008/user_1.wav](out/audio/duplicate_charge_008/user_1.wav)
- Bot: [out/audio/duplicate_charge_008/bot_1.wav](out/audio/duplicate_charge_008/bot_1.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## duplicate_charge_009: Request refund for duplicate charge

### Turn 1 ❌

**User Text:** I got charged for something? I don't know, it was on my credit card. It looks like it went through twice maybe?

**User ASR:** i got charged for something. i don't know. it was on my credit card. it looks like it went through twice, maybe?

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/duplicate_charge_009/user_1.wav](out/audio/duplicate_charge_009/user_1.wav)
- Bot: [out/audio/duplicate_charge_009/bot_1.wav](out/audio/duplicate_charge_009/bot_1.wav)

**Expected:** {'contains_any': ['last four digits', 'card', 'last four', 'card ending']}

---

### Turn 2 ❌

**User Text:** Umm which card... oh the one ending in 1472.

**User ASR:** on which card, over one ending in 1472.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/duplicate_charge_009/user_2.wav](out/audio/duplicate_charge_009/user_2.wav)
- Bot: [out/audio/duplicate_charge_009/bot_2.wav](out/audio/duplicate_charge_009/bot_2.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## duplicate_charge_010: Request refund for duplicate charge

### Turn 1 ❌

**User Text:** So there's this weird charge on my statement, and I think it might be a duplicate? I'm not really sure what happened.

**User ASR:** so there's this weird charge on my statement, and i think it might be a duplicate?  i'm not really sure what happened.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/duplicate_charge_010/user_1.wav](out/audio/duplicate_charge_010/user_1.wav)
- Bot: [out/audio/duplicate_charge_010/bot_1.wav](out/audio/duplicate_charge_010/bot_1.wav)

**Expected:** {'contains_any': ['last four digits', 'card', 'last four', 'card ending']}

---

### Turn 2 ❌

**User Text:** Uh let me check... card ending 6039 I think.

**User ASR:** i'll let me check, card ending 6, 1939 i think.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/duplicate_charge_010/user_2.wav](out/audio/duplicate_charge_010/user_2.wav)
- Bot: [out/audio/duplicate_charge_010/bot_2.wav](out/audio/duplicate_charge_010/bot_2.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## missing_package_001: Report a missing package

### Turn 1 ❌

**User Text:** Hi, my tracking says my package was delivered but I don't have it. I checked everywhere.

**User ASR:** hi, my tracking says my package was delivered, but i don't have it.  i check everywhere.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/missing_package_001/user_1.wav](out/audio/missing_package_001/user_1.wav)
- Bot: [out/audio/missing_package_001/bot_1.wav](out/audio/missing_package_001/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 74219.

**User ASR:** order 74,219.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/missing_package_001/user_2.wav](out/audio/missing_package_001/user_2.wav)
- Bot: [out/audio/missing_package_001/bot_2.wav](out/audio/missing_package_001/bot_2.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## missing_package_002: Report a missing package

### Turn 1 ❌

**User Text:** Hello, I got a delivery notification yesterday but there's nothing at my door. Can you help me figure out what happened?

**User ASR:** hello, i got a delivery notification yesterday, but there's nothing in my door.  can you help me figure out what happened?

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/missing_package_002/user_1.wav](out/audio/missing_package_002/user_1.wav)
- Bot: [out/audio/missing_package_002/bot_1.wav](out/audio/missing_package_002/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** It's order 38105.

**User ASR:** it's order 38,105.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/missing_package_002/user_2.wav](out/audio/missing_package_002/user_2.wav)
- Bot: [out/audio/missing_package_002/bot_2.wav](out/audio/missing_package_002/bot_2.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## missing_package_003: Report a missing package

### Turn 1 ❌

**User Text:** Hey, I think my package might be lost. It says delivered but I've checked the porch, the mailbox, everything.

**User ASR:** hey, i think my package might be lost. it says delivered, but i've checked the porch.  the mailbox, everything.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/missing_package_003/user_1.wav](out/audio/missing_package_003/user_1.wav)
- Bot: [out/audio/missing_package_003/bot_1.wav](out/audio/missing_package_003/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Yeah, order 52847.

**User ASR:** yeah, order 52,847.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/missing_package_003/user_2.wav](out/audio/missing_package_003/user_2.wav)
- Bot: [out/audio/missing_package_003/bot_2.wav](out/audio/missing_package_003/bot_2.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## missing_package_004: Report a missing package

### Turn 1 ❌

**User Text:** Someone stole my package or your driver delivered it to the wrong house. Either way, I don't have it and I'm furious.

**User ASR:** someone stole my package or your driver delivered it to the wrong house.  either way, i don't have it and i'm furious.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/missing_package_004/user_1.wav](out/audio/missing_package_004/user_1.wav)
- Bot: [out/audio/missing_package_004/bot_1.wav](out/audio/missing_package_004/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 61934. I want this resolved today.

**User ASR:** order 61934. i want this resolved today.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/missing_package_004/user_2.wav](out/audio/missing_package_004/user_2.wav)
- Bot: [out/audio/missing_package_004/bot_2.wav](out/audio/missing_package_004/bot_2.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## missing_package_005: Report a missing package

### Turn 1 ❌

**User Text:** This is the second time a package has gone missing. I'm seriously considering never ordering from you again.

**User ASR:** this is the second time a package has gone missing.  i'm seriously considering never ordering from you again.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/missing_package_005/user_1.wav](out/audio/missing_package_005/user_1.wav)
- Bot: [out/audio/missing_package_005/bot_1.wav](out/audio/missing_package_005/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** It's 90283. And don't tell me to wait, I already waited three days.

**User ASR:** it's $90,283 and don't tell me to wait, i already waited three days.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/missing_package_005/user_2.wav](out/audio/missing_package_005/user_2.wav)
- Bot: [out/audio/missing_package_005/bot_2.wav](out/audio/missing_package_005/bot_2.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## missing_package_006: Report a missing package

### Turn 1 ❌

**User Text:** Your delivery driver marked it delivered but I have a ring camera and nobody came to my door. Where is my stuff?

**User ASR:** your delivery driver marked it delivered, but i have a ring camera and nobody came to my door.  where is my stuff?

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/missing_package_006/user_1.wav](out/audio/missing_package_006/user_1.wav)
- Bot: [out/audio/missing_package_006/bot_1.wav](out/audio/missing_package_006/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 45672. I can send you the camera footage if you need it.

**User ASR:** order 45672.  i can send you the camera footage if you need it.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/missing_package_006/user_2.wav](out/audio/missing_package_006/user_2.wav)
- Bot: [out/audio/missing_package_006/bot_2.wav](out/audio/missing_package_006/bot_2.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## missing_package_007: Report a missing package

### Turn 1 ❌

**User Text:** Hey, order 27318 says it was delivered but it's not here. I need to report it missing.

**User ASR:** hey, order 27,318 says it was delivered but it's not here. i need to report it missing.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/missing_package_007/user_1.wav](out/audio/missing_package_007/user_1.wav)
- Bot: [out/audio/missing_package_007/bot_1.wav](out/audio/missing_package_007/bot_1.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## missing_package_008: Report a missing package

### Turn 1 ❌

**User Text:** I'm calling about order 83056. Tracking shows delivered two days ago and I never got it.

**User ASR:** i'm calling about order 83056.  tracking shows delivered two days ago and i never got it.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/missing_package_008/user_1.wav](out/audio/missing_package_008/user_1.wav)
- Bot: [out/audio/missing_package_008/bot_1.wav](out/audio/missing_package_008/bot_1.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## missing_package_009: Report a missing package

### Turn 1 ❌

**User Text:** Hey so uh, I was expecting something in the mail and it never showed up? I'm not really sure what happened to it.

**User ASR:** hey soa, i was expecting something in the mail and it never showed up?  i'm not really sure what happened to it.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/missing_package_009/user_1.wav](out/audio/missing_package_009/user_1.wav)
- Bot: [out/audio/missing_package_009/bot_1.wav](out/audio/missing_package_009/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Oh um, the order number... let me look. I think it's 16549.

**User ASR:** oh, um, the order number.  let me look.  i think it's 16,549.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/missing_package_009/user_2.wav](out/audio/missing_package_009/user_2.wav)
- Bot: [out/audio/missing_package_009/bot_2.wav](out/audio/missing_package_009/bot_2.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## missing_package_010: Report a missing package

### Turn 1 ❌

**User Text:** I think my package might not have come? Like the app says something about delivery but I didn't see anything outside.

**User ASR:** i think my package might not have come.  like the app says something about delivery, but i didn't see anything outside.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/missing_package_010/user_1.wav](out/audio/missing_package_010/user_1.wav)
- Bot: [out/audio/missing_package_010/bot_1.wav](out/audio/missing_package_010/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Hmm I'm not sure where to find the order number... oh here. Order 73401.

**User ASR:** i'm not sure where to find the order number.  oh here.  order 73,401.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/missing_package_010/user_2.wav](out/audio/missing_package_010/user_2.wav)
- Bot: [out/audio/missing_package_010/bot_2.wav](out/audio/missing_package_010/bot_2.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## reset_password_001: Reset account password

### Turn 1 ❌

**User Text:** Hi, I can't seem to log into my account. I think I need to reset my password.

**User ASR:** hi, i can't seem to log into my account. i think i need to reset my password.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/reset_password_001/user_1.wav](out/audio/reset_password_001/user_1.wav)
- Bot: [out/audio/reset_password_001/bot_1.wav](out/audio/reset_password_001/bot_1.wav)

**Expected:** {'contains_any': ['email', 'email address', 'email on file']}

---

### Turn 2 ❌

**User Text:** Sure, it's jennifer.walsh@gmail.com.

**User ASR:** sure, it's jennifer.wallshadgmail.com

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/reset_password_001/user_2.wav](out/audio/reset_password_001/user_2.wav)
- Bot: [out/audio/reset_password_001/bot_2.wav](out/audio/reset_password_001/bot_2.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## reset_password_002: Reset account password

### Turn 1 ❌

**User Text:** Hello, I forgot my password and I need to get back into my account. Can you help?

**User ASR:** hello, i forgot my password and i need to get back into my account.  can you help?

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/reset_password_002/user_1.wav](out/audio/reset_password_002/user_1.wav)
- Bot: [out/audio/reset_password_002/bot_1.wav](out/audio/reset_password_002/bot_1.wav)

**Expected:** {'contains_any': ['email', 'email address', 'email on file']}

---

### Turn 2 ❌

**User Text:** My email is marcus.chen88@yahoo.com.

**User ASR:** my email is markest.chenn88 at yahu.com.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/reset_password_002/user_2.wav](out/audio/reset_password_002/user_2.wav)
- Bot: [out/audio/reset_password_002/bot_2.wav](out/audio/reset_password_002/bot_2.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## reset_password_003: Reset account password

### Turn 1 ❌

**User Text:** Hey, I'm locked out of my account. I've tried a few passwords but none of them work.

**User ASR:** hey, i'm locked out of my account.  i've tried a few passwords, but none of them work.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/reset_password_003/user_1.wav](out/audio/reset_password_003/user_1.wav)
- Bot: [out/audio/reset_password_003/bot_1.wav](out/audio/reset_password_003/bot_1.wav)

**Expected:** {'contains_any': ['email', 'email address', 'email on file']}

---

### Turn 2 ❌

**User Text:** It's sarah.k.morrison@outlook.com.

**User ASR:** it's sarah.k. morrison at outlook.com.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/reset_password_003/user_2.wav](out/audio/reset_password_003/user_2.wav)
- Bot: [out/audio/reset_password_003/bot_2.wav](out/audio/reset_password_003/bot_2.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## reset_password_004: Reset account password

### Turn 1 ❌

**User Text:** Your stupid reset email never comes through! I've requested it four times and nothing. I need my password reset NOW.

**User ASR:** your stupid reset e-mail never comes through. i've requested it four times and nothing. i need my password reset now.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/reset_password_004/user_1.wav](out/audio/reset_password_004/user_1.wav)
- Bot: [out/audio/reset_password_004/bot_1.wav](out/audio/reset_password_004/bot_1.wav)

**Expected:** {'contains_any': ['email', 'email address', 'email on file']}

---

### Turn 2 ❌

**User Text:** d.gonzalez@hotmail.com. And check my spam folder? I already did.

**User ASR:** d. gonzales at hotmail.com.  and check my spam folder.  i already did.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/reset_password_004/user_2.wav](out/audio/reset_password_004/user_2.wav)
- Bot: [out/audio/reset_password_004/bot_2.wav](out/audio/reset_password_004/bot_2.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## reset_password_005: Reset account password

### Turn 1 ❌

**User Text:** I've been locked out for two days and I need to place an order. Why is this so difficult?

**User ASR:** i've been locked out for two days and i need to place an order.  why is this so difficult?

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/reset_password_005/user_1.wav](out/audio/reset_password_005/user_1.wav)
- Bot: [out/audio/reset_password_005/bot_1.wav](out/audio/reset_password_005/bot_1.wav)

**Expected:** {'contains_any': ['email', 'email address', 'email on file']}

---

### Turn 2 ❌

**User Text:** robert.james.finn@gmail.com. Please actually send it this time.

**User ASR:** robert.james.fin at gmail.com.  please actually send it this time.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/reset_password_005/user_2.wav](out/audio/reset_password_005/user_2.wav)
- Bot: [out/audio/reset_password_005/bot_2.wav](out/audio/reset_password_005/bot_2.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## reset_password_006: Reset account password

### Turn 1 ❌

**User Text:** This is ridiculous. I changed my password last week and now it doesn't work again. Something's wrong with your system.

**User ASR:** this is ridiculous. i changed my password last week and now it doesn't work again.  something's wrong with your system.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/reset_password_006/user_1.wav](out/audio/reset_password_006/user_1.wav)
- Bot: [out/audio/reset_password_006/bot_1.wav](out/audio/reset_password_006/bot_1.wav)

**Expected:** {'contains_any': ['email', 'email address', 'email on file']}

---

### Turn 2 ❌

**User Text:** It's natalie.p.brooks@icloud.com.

**User ASR:** it's natalie.p.brooks at icloud.com.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/reset_password_006/user_2.wav](out/audio/reset_password_006/user_2.wav)
- Bot: [out/audio/reset_password_006/bot_2.wav](out/audio/reset_password_006/bot_2.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## reset_password_007: Reset account password

### Turn 1 ❌

**User Text:** I need a password reset for my account, the email on file is kevin.adler@gmail.com.

**User ASR:** i need a password reset for my account, the email on file is kevin.addler at gmail.com

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/reset_password_007/user_1.wav](out/audio/reset_password_007/user_1.wav)
- Bot: [out/audio/reset_password_007/bot_1.wav](out/audio/reset_password_007/bot_1.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## reset_password_008: Reset account password

### Turn 1 ❌

**User Text:** Hey can you send a password reset to amy.liu.writes@yahoo.com? I'm totally locked out.

**User ASR:** hey, can you send a password reset to amy.lu.rightset-yahu.com?  i'm totally locked out.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/reset_password_008/user_1.wav](out/audio/reset_password_008/user_1.wav)
- Bot: [out/audio/reset_password_008/bot_1.wav](out/audio/reset_password_008/bot_1.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## reset_password_009: Reset account password

### Turn 1 ❌

**User Text:** So uh, I can't get in. Like I'm typing my password and it keeps saying it's wrong. I don't know what to do.

**User ASR:** so uh, i can't get in, like i'm typing my password and it keeps saying it's wrong.  i don't know what to do.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/reset_password_009/user_1.wav](out/audio/reset_password_009/user_1.wav)
- Bot: [out/audio/reset_password_009/bot_1.wav](out/audio/reset_password_009/bot_1.wav)

**Expected:** {'contains_any': ['email', 'email address', 'email on file']}

---

### Turn 2 ❌

**User Text:** Oh, my email? I think I used... tom.baker.99@gmail.com. Or wait, no. Yeah, that one.

**User ASR:** oh, my email? i think i used thom.baker.99 at gmail.com.  or wait, no, yeah, that one.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/reset_password_009/user_2.wav](out/audio/reset_password_009/user_2.wav)
- Bot: [out/audio/reset_password_009/bot_2.wav](out/audio/reset_password_009/bot_2.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## reset_password_010: Reset account password

### Turn 1 ❌

**User Text:** I'm having trouble with my account thing. The login isn't working? I'm not sure if it's my password or what.

**User ASR:** i'm having trouble with my account thing.  the login isn't working?  i'm not sure if it's my password or what.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/reset_password_010/user_1.wav](out/audio/reset_password_010/user_1.wav)
- Bot: [out/audio/reset_password_010/bot_1.wav](out/audio/reset_password_010/bot_1.wav)

**Expected:** {'contains_any': ['email', 'email address', 'email on file']}

---

### Turn 2 ❌

**User Text:** Hmm let me think... it's either lisa.v.wright@outlook.com or... no that's the one.

**User ASR:** let me think, it's either lisa.v.ri that outlook.com or know that's the one.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/reset_password_010/user_2.wav](out/audio/reset_password_010/user_2.wav)
- Bot: [out/audio/reset_password_010/bot_2.wav](out/audio/reset_password_010/bot_2.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## return_damaged_001: Return a damaged item

### Turn 1 ❌

**User Text:** Hi there, I received a product that's damaged and I'd like to return it please.

**User ASR:** hi there, i received a product that's damaged and i'd like to return it please.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/return_damaged_001/user_1.wav](out/audio/return_damaged_001/user_1.wav)
- Bot: [out/audio/return_damaged_001/bot_1.wav](out/audio/return_damaged_001/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'have your order', 'which order']}

---

### Turn 2 ❌

**User Text:** Sure, it's order 48291.

**User ASR:** sure, it's order 48,291.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/return_damaged_001/user_2.wav](out/audio/return_damaged_001/user_2.wav)
- Bot: [out/audio/return_damaged_001/bot_2.wav](out/audio/return_damaged_001/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## return_damaged_002: Return a damaged item

### Turn 1 ❌

**User Text:** Good morning, I got a package yesterday and the item inside was broken. I'd like to send it back.

**User ASR:** good morning, i got a package yesterday and the item inside was broken.  i'd like to send it back.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/return_damaged_002/user_1.wav](out/audio/return_damaged_002/user_1.wav)
- Bot: [out/audio/return_damaged_002/bot_1.wav](out/audio/return_damaged_002/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'have your order', 'which order']}

---

### Turn 2 ❌

**User Text:** Yeah the order number is 57134.

**User ASR:** yeah, the order number is 57134.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/return_damaged_002/user_2.wav](out/audio/return_damaged_002/user_2.wav)
- Bot: [out/audio/return_damaged_002/bot_2.wav](out/audio/return_damaged_002/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## return_damaged_003: Return a damaged item

### Turn 1 ❌

**User Text:** Hello, I'm hoping you can help me. I need to return something that came in pretty bad shape.

**User ASR:** hello, i'm hoping you can help me.  i need to return something that came in pretty bad shape.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/return_damaged_003/user_1.wav](out/audio/return_damaged_003/user_1.wav)
- Bot: [out/audio/return_damaged_003/bot_1.wav](out/audio/return_damaged_003/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'have your order', 'which order']}

---

### Turn 2 ❌

**User Text:** Let me check... okay it's order 63408.

**User ASR:** let me check. okay, it's order 63,408.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/return_damaged_003/user_2.wav](out/audio/return_damaged_003/user_2.wav)
- Bot: [out/audio/return_damaged_003/bot_2.wav](out/audio/return_damaged_003/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## return_damaged_004: Return a damaged item

### Turn 1 ❌

**User Text:** Yeah I need to return this thing, it showed up completely smashed. This is ridiculous.

**User ASR:** yeah, i need to return this thing. it showed up completely smashed.  this is ridiculous.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/return_damaged_004/user_1.wav](out/audio/return_damaged_004/user_1.wav)
- Bot: [out/audio/return_damaged_004/bot_1.wav](out/audio/return_damaged_004/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'have your order', 'which order']}

---

### Turn 2 ❌

**User Text:** It's 29174. Can we hurry this up?

**User ASR:** it's $29,174. can we hurry this up?

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/return_damaged_004/user_2.wav](out/audio/return_damaged_004/user_2.wav)
- Bot: [out/audio/return_damaged_004/bot_2.wav](out/audio/return_damaged_004/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## return_damaged_005: Return a damaged item

### Turn 1 ❌

**User Text:** This is the second time I've gotten a broken item from you guys. I want to return it and honestly I'm pretty upset about it.

**User ASR:** this is the second time i've gotten a broken item from you guys.  i want to return it and honestly i'm pretty upset about it.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/return_damaged_005/user_1.wav](out/audio/return_damaged_005/user_1.wav)
- Bot: [out/audio/return_damaged_005/bot_1.wav](out/audio/return_damaged_005/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'have your order', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 83652. And I want this handled quickly please.

**User ASR:** order 83652. and i want this handled quickly, please.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/return_damaged_005/user_2.wav](out/audio/return_damaged_005/user_2.wav)
- Bot: [out/audio/return_damaged_005/bot_2.wav](out/audio/return_damaged_005/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## return_damaged_006: Return a damaged item

### Turn 1 ❌

**User Text:** Look, I've been waiting on hold for twenty minutes. The blender I ordered arrived cracked and I need to return it now.

**User ASR:** look, i've been waiting on hold for 20 minutes.  the blender i ordered arrived cracked and i need to return it now.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/return_damaged_006/user_1.wav](out/audio/return_damaged_006/user_1.wav)
- Bot: [out/audio/return_damaged_006/bot_1.wav](out/audio/return_damaged_006/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'have your order', 'which order']}

---

### Turn 2 ❌

**User Text:** It's order 41087, come on.

**User ASR:** it's order 41,087, come on.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/return_damaged_006/user_2.wav](out/audio/return_damaged_006/user_2.wav)
- Bot: [out/audio/return_damaged_006/bot_2.wav](out/audio/return_damaged_006/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## return_damaged_007: Return a damaged item

### Turn 1 ❌

**User Text:** Hey I need to return order 72563, it arrived with a huge crack in it.

**User ASR:** hey, i need to return order 70,563. it arrived with a huge crack in it.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/return_damaged_007/user_1.wav](out/audio/return_damaged_007/user_1.wav)
- Bot: [out/audio/return_damaged_007/bot_1.wav](out/audio/return_damaged_007/bot_1.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## return_damaged_008: Return a damaged item

### Turn 1 ❌

**User Text:** Hi, my order number is 19846 and the toaster I got is completely busted, I need to send it back.

**User ASR:** hi, my order number is 19,846 and the toaster i got is completely busted. i need to send it back.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/return_damaged_008/user_1.wav](out/audio/return_damaged_008/user_1.wav)
- Bot: [out/audio/return_damaged_008/bot_1.wav](out/audio/return_damaged_008/bot_1.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## return_damaged_009: Return a damaged item

### Turn 1 ❌

**User Text:** Um yeah so I got this thing and it's like... not right? It's all messed up. I think I wanna send it back.

**User ASR:** um, yeah, so i got this thing and it's like, not right?  it's all messed up.  i think i want to send it back.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/return_damaged_009/user_1.wav](out/audio/return_damaged_009/user_1.wav)
- Bot: [out/audio/return_damaged_009/bot_1.wav](out/audio/return_damaged_009/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'have your order', 'which order']}

---

### Turn 2 ❌

**User Text:** Oh uh, let me look... I think it's like... order 35021? Yeah that one.

**User ASR:** oh, uh, let me look. i think it's like order 35, 2021? yeah, that one.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/return_damaged_009/user_2.wav](out/audio/return_damaged_009/user_2.wav)
- Bot: [out/audio/return_damaged_009/bot_2.wav](out/audio/return_damaged_009/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## return_damaged_010: Return a damaged item

### Turn 1 ❌

**User Text:** So I ordered something a while back and it wasn't in good condition when it got here. I don't really know what to do about it.

**User ASR:** so i ordered something a while back and it wasn't in good condition when it got here.  i don't really know what to do about it.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/return_damaged_010/user_1.wav](out/audio/return_damaged_010/user_1.wav)
- Bot: [out/audio/return_damaged_010/bot_1.wav](out/audio/return_damaged_010/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'have your order', 'which order']}

---

### Turn 2 ❌

**User Text:** Hmm I think the number was... hold on... 60473.

**User ASR:** whom i think the number was, hold on, 60,473.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/return_damaged_010/user_2.wav](out/audio/return_damaged_010/user_2.wav)
- Bot: [out/audio/return_damaged_010/bot_2.wav](out/audio/return_damaged_010/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## upgrade_sub_001: Upgrade subscription plan

### Turn 1 ❌

**User Text:** Hi, I'd like to upgrade my subscription to the premium plan please.

**User ASR:** hi, i'd like to upgrade my subscription to the premium plan, please.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/upgrade_sub_001/user_1.wav](out/audio/upgrade_sub_001/user_1.wav)
- Bot: [out/audio/upgrade_sub_001/bot_1.wav](out/audio/upgrade_sub_001/bot_1.wav)

**Expected:** {'contains_any': ['account number', 'account', 'account details']}

---

### Turn 2 ❌

**User Text:** My account number is 80421.

**User ASR:** my account number is 80,421.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/upgrade_sub_001/user_2.wav](out/audio/upgrade_sub_001/user_2.wav)
- Bot: [out/audio/upgrade_sub_001/bot_2.wav](out/audio/upgrade_sub_001/bot_2.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

## upgrade_sub_002: Upgrade subscription plan

### Turn 1 ❌

**User Text:** Hello, I'm currently on the basic plan and I want to move up to the next tier.

**User ASR:** hello, i'm currently on the basic plan and i want to move up to the next tier.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/upgrade_sub_002/user_1.wav](out/audio/upgrade_sub_002/user_1.wav)
- Bot: [out/audio/upgrade_sub_002/bot_1.wav](out/audio/upgrade_sub_002/bot_1.wav)

**Expected:** {'contains_any': ['account number', 'account', 'account details']}

---

### Turn 2 ❌

**User Text:** Sure, the account number is 56738.

**User ASR:** sure, the account number is 56,738.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/upgrade_sub_002/user_2.wav](out/audio/upgrade_sub_002/user_2.wav)
- Bot: [out/audio/upgrade_sub_002/bot_2.wav](out/audio/upgrade_sub_002/bot_2.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

## upgrade_sub_003: Upgrade subscription plan

### Turn 1 ❌

**User Text:** Hey, I've been thinking about upgrading my plan. Can you walk me through that?

**User ASR:** hey, i've been thinking about upgrading my plan. can you walk me through that?

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/upgrade_sub_003/user_1.wav](out/audio/upgrade_sub_003/user_1.wav)
- Bot: [out/audio/upgrade_sub_003/bot_1.wav](out/audio/upgrade_sub_003/bot_1.wav)

**Expected:** {'contains_any': ['account number', 'account', 'account details']}

---

### Turn 2 ❌

**User Text:** Oh right, it's account 32914.

**User ASR:** alright, it's a count 32,914

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/upgrade_sub_003/user_2.wav](out/audio/upgrade_sub_003/user_2.wav)
- Bot: [out/audio/upgrade_sub_003/bot_2.wav](out/audio/upgrade_sub_003/bot_2.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

## upgrade_sub_004: Upgrade subscription plan

### Turn 1 ❌

**User Text:** I've been trying to upgrade on your website and it keeps crashing. Can you just do it for me? This is so annoying.

**User ASR:** i've been trying to upgrade on your website and it keeps crashing.  can you just do it for me?  this is so annoying.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/upgrade_sub_004/user_1.wav](out/audio/upgrade_sub_004/user_1.wav)
- Bot: [out/audio/upgrade_sub_004/bot_1.wav](out/audio/upgrade_sub_004/bot_1.wav)

**Expected:** {'contains_any': ['account number', 'account', 'account details']}

---

### Turn 2 ❌

**User Text:** Account 69105. Just upgrade it already.

**User ASR:** account 69105. just upgrade it already.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/upgrade_sub_004/user_2.wav](out/audio/upgrade_sub_004/user_2.wav)
- Bot: [out/audio/upgrade_sub_004/bot_2.wav](out/audio/upgrade_sub_004/bot_2.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

## upgrade_sub_005: Upgrade subscription plan

### Turn 1 ❌

**User Text:** Why is it so hard to upgrade my plan? I've clicked every button on your site and nothing happens.

**User ASR:** why is it so hard to upgrade my plan?  i've clicked every button on your site and nothing happens.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/upgrade_sub_005/user_1.wav](out/audio/upgrade_sub_005/user_1.wav)
- Bot: [out/audio/upgrade_sub_005/bot_1.wav](out/audio/upgrade_sub_005/bot_1.wav)

**Expected:** {'contains_any': ['account number', 'account', 'account details']}

---

### Turn 2 ❌

**User Text:** It's 47283. And you really need to fix that page.

**User ASR:** it's 47,283 and you really need to fix that page.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/upgrade_sub_005/user_2.wav](out/audio/upgrade_sub_005/user_2.wav)
- Bot: [out/audio/upgrade_sub_005/bot_2.wav](out/audio/upgrade_sub_005/bot_2.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

## upgrade_sub_006: Upgrade subscription plan

### Turn 1 ❌

**User Text:** I emailed about upgrading a week ago and never heard back. I'm calling now because clearly nobody reads emails over there.

**User ASR:** i emailed about upgrading a week ago and never heard back.  i'm calling now because clearly nobody reads emails over there.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/upgrade_sub_006/user_1.wav](out/audio/upgrade_sub_006/user_1.wav)
- Bot: [out/audio/upgrade_sub_006/bot_1.wav](out/audio/upgrade_sub_006/bot_1.wav)

**Expected:** {'contains_any': ['account number', 'account', 'account details']}

---

### Turn 2 ❌

**User Text:** Account number is 91560.

**User ASR:** account number is 91,560.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/upgrade_sub_006/user_2.wav](out/audio/upgrade_sub_006/user_2.wav)
- Bot: [out/audio/upgrade_sub_006/bot_2.wav](out/audio/upgrade_sub_006/bot_2.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

## upgrade_sub_007: Upgrade subscription plan

### Turn 1 ❌

**User Text:** Hey, account 24897 here, I want to upgrade to the premium tier.

**User ASR:** hey, account 24,897 here. i want to upgrade to the premium tier.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/upgrade_sub_007/user_1.wav](out/audio/upgrade_sub_007/user_1.wav)
- Bot: [out/audio/upgrade_sub_007/bot_1.wav](out/audio/upgrade_sub_007/bot_1.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

## upgrade_sub_008: Upgrade subscription plan

### Turn 1 ❌

**User Text:** I'm calling to upgrade my subscription. My account number is 75346 and I want the highest plan.

**User ASR:** i'm calling to upgrade my subscription.  my account number is 75,346 and i want the highest plan.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/upgrade_sub_008/user_1.wav](out/audio/upgrade_sub_008/user_1.wav)
- Bot: [out/audio/upgrade_sub_008/bot_1.wav](out/audio/upgrade_sub_008/bot_1.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

## upgrade_sub_009: Upgrade subscription plan

### Turn 1 ❌

**User Text:** So I think I wanna change my plan? Like get more features or whatever? I'm not sure what's available.

**User ASR:** so i think i want to change my plan, like get more features or whatever, i'm not sure what's available.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/upgrade_sub_009/user_1.wav](out/audio/upgrade_sub_009/user_1.wav)
- Bot: [out/audio/upgrade_sub_009/bot_1.wav](out/audio/upgrade_sub_009/bot_1.wav)

**Expected:** {'contains_any': ['account number', 'account', 'account details']}

---

### Turn 2 ❌

**User Text:** Uh I think my account is... hold on... 18603? Yeah.

**User ASR:** i think my account is. hold on. 18,603? yeah.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/upgrade_sub_009/user_2.wav](out/audio/upgrade_sub_009/user_2.wav)
- Bot: [out/audio/upgrade_sub_009/bot_2.wav](out/audio/upgrade_sub_009/bot_2.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

## upgrade_sub_010: Upgrade subscription plan

### Turn 1 ❌

**User Text:** Hi, um, someone told me I could get a better plan? I don't really know the difference between them.

**User ASR:** hi, um, someone told me i could get a better plan.  i don't really know the difference between them.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/upgrade_sub_010/user_1.wav](out/audio/upgrade_sub_010/user_1.wav)
- Bot: [out/audio/upgrade_sub_010/bot_1.wav](out/audio/upgrade_sub_010/bot_1.wav)

**Expected:** {'contains_any': ['account number', 'account', 'account details']}

---

### Turn 2 ❌

**User Text:** My account... hmm... I think it's 53082.

**User ASR:** my account, thumb, i think it's 53,882.

**Bot Text:** I'm sorry, I encountered an error. Could you please try again?

**Audio Files:**
- User: [out/audio/upgrade_sub_010/user_2.wav](out/audio/upgrade_sub_010/user_2.wav)
- Bot: [out/audio/upgrade_sub_010/bot_2.wav](out/audio/upgrade_sub_010/bot_2.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

