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
| change_address_001 | ❌ FAIL | 1/2 |
| change_address_002 | ❌ FAIL | 1/2 |
| change_address_003 | ❌ FAIL | 1/2 |
| change_address_004 | ❌ FAIL | 1/2 |
| change_address_005 | ❌ FAIL | 1/2 |
| change_address_006 | ❌ FAIL | 1/2 |
| change_address_007 | ❌ FAIL | 0/1 |
| change_address_008 | ❌ FAIL | 0/1 |
| change_address_009 | ❌ FAIL | 1/2 |
| change_address_010 | ❌ FAIL | 1/2 |
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
| duplicate_charge_001 | ❌ FAIL | 1/2 |
| duplicate_charge_002 | ❌ FAIL | 1/2 |
| duplicate_charge_003 | ❌ FAIL | 1/2 |
| duplicate_charge_004 | ❌ FAIL | 1/2 |
| duplicate_charge_005 | ❌ FAIL | 1/2 |
| duplicate_charge_006 | ❌ FAIL | 1/2 |
| duplicate_charge_007 | ❌ FAIL | 0/1 |
| duplicate_charge_008 | ❌ FAIL | 0/1 |
| duplicate_charge_009 | ❌ FAIL | 1/2 |
| duplicate_charge_010 | ❌ FAIL | 1/2 |
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
| return_damaged_001 | ❌ FAIL | 1/2 |
| return_damaged_002 | ❌ FAIL | 1/2 |
| return_damaged_003 | ❌ FAIL | 1/2 |
| return_damaged_004 | ❌ FAIL | 1/2 |
| return_damaged_005 | ❌ FAIL | 1/2 |
| return_damaged_006 | ❌ FAIL | 1/2 |
| return_damaged_007 | ❌ FAIL | 0/1 |
| return_damaged_008 | ❌ FAIL | 0/1 |
| return_damaged_009 | ❌ FAIL | 1/2 |
| return_damaged_010 | ❌ FAIL | 1/2 |
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

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/cancel_order_001/user_1.wav](out/audio/cancel_order_001/user_1.wav)
- Bot: [out/audio/cancel_order_001/bot_1.wav](out/audio/cancel_order_001/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** It's order 47382.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/cancel_order_001/user_2.wav](out/audio/cancel_order_001/user_2.wav)
- Bot: [out/audio/cancel_order_001/bot_2.wav](out/audio/cancel_order_001/bot_2.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## cancel_order_002: Cancel an order

### Turn 1 ❌

**User Text:** Hello, I changed my mind about a purchase and would like to cancel it please.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/cancel_order_002/user_1.wav](out/audio/cancel_order_002/user_1.wav)
- Bot: [out/audio/cancel_order_002/bot_1.wav](out/audio/cancel_order_002/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** The order number is 61250.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/cancel_order_002/user_2.wav](out/audio/cancel_order_002/user_2.wav)
- Bot: [out/audio/cancel_order_002/bot_2.wav](out/audio/cancel_order_002/bot_2.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## cancel_order_003: Cancel an order

### Turn 1 ❌

**User Text:** Good afternoon. I need to cancel an order. I found a better price somewhere else.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/cancel_order_003/user_1.wav](out/audio/cancel_order_003/user_1.wav)
- Bot: [out/audio/cancel_order_003/bot_1.wav](out/audio/cancel_order_003/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Sure thing, it's order 29817.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/cancel_order_003/user_2.wav](out/audio/cancel_order_003/user_2.wav)
- Bot: [out/audio/cancel_order_003/bot_2.wav](out/audio/cancel_order_003/bot_2.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## cancel_order_004: Cancel an order

### Turn 1 ❌

**User Text:** I need to cancel my order right now. The delivery date keeps getting pushed back and I'm done waiting.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/cancel_order_004/user_1.wav](out/audio/cancel_order_004/user_1.wav)
- Bot: [out/audio/cancel_order_004/bot_1.wav](out/audio/cancel_order_004/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 58463. Just cancel it.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/cancel_order_004/user_2.wav](out/audio/cancel_order_004/user_2.wav)
- Bot: [out/audio/cancel_order_004/bot_2.wav](out/audio/cancel_order_004/bot_2.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## cancel_order_005: Cancel an order

### Turn 1 ❌

**User Text:** I've been trying to cancel this order on your app for two days and nothing works. Can you just do it for me?

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/cancel_order_005/user_1.wav](out/audio/cancel_order_005/user_1.wav)
- Bot: [out/audio/cancel_order_005/bot_1.wav](out/audio/cancel_order_005/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** It's 73916. And your app is terrible by the way.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/cancel_order_005/user_2.wav](out/audio/cancel_order_005/user_2.wav)
- Bot: [out/audio/cancel_order_005/bot_2.wav](out/audio/cancel_order_005/bot_2.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## cancel_order_006: Cancel an order

### Turn 1 ❌

**User Text:** Yeah so you charged me the wrong amount and I just want to cancel the whole thing. This is so annoying.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/cancel_order_006/user_1.wav](out/audio/cancel_order_006/user_1.wav)
- Bot: [out/audio/cancel_order_006/bot_1.wav](out/audio/cancel_order_006/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 84205. Please confirm it's actually cancelled this time.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/cancel_order_006/user_2.wav](out/audio/cancel_order_006/user_2.wav)
- Bot: [out/audio/cancel_order_006/bot_2.wav](out/audio/cancel_order_006/bot_2.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## cancel_order_007: Cancel an order

### Turn 1 ❌

**User Text:** Hey, I need to cancel order 36710. I accidentally ordered the wrong size.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/cancel_order_007/user_1.wav](out/audio/cancel_order_007/user_1.wav)
- Bot: [out/audio/cancel_order_007/bot_1.wav](out/audio/cancel_order_007/bot_1.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## cancel_order_008: Cancel an order

### Turn 1 ❌

**User Text:** Can you cancel order 52194 for me? I don't need it anymore.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/cancel_order_008/user_1.wav](out/audio/cancel_order_008/user_1.wav)
- Bot: [out/audio/cancel_order_008/bot_1.wav](out/audio/cancel_order_008/bot_1.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## cancel_order_009: Cancel an order

### Turn 1 ❌

**User Text:** Um so I think I wanna cancel something I bought? I'm not even sure if it shipped yet or what.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/cancel_order_009/user_1.wav](out/audio/cancel_order_009/user_1.wav)
- Bot: [out/audio/cancel_order_009/bot_1.wav](out/audio/cancel_order_009/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** I think it's uh... order 19548? Let me double check. Yeah, 19548.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/cancel_order_009/user_2.wav](out/audio/cancel_order_009/user_2.wav)
- Bot: [out/audio/cancel_order_009/bot_2.wav](out/audio/cancel_order_009/bot_2.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## cancel_order_010: Cancel an order

### Turn 1 ❌

**User Text:** I don't know, I just want to stop the order from coming. Is it too late? Can I still do that?

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/cancel_order_010/user_1.wav](out/audio/cancel_order_010/user_1.wav)
- Bot: [out/audio/cancel_order_010/bot_1.wav](out/audio/cancel_order_010/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Oh right. Hold on... order 40673.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/cancel_order_010/user_2.wav](out/audio/cancel_order_010/user_2.wav)
- Bot: [out/audio/cancel_order_010/bot_2.wav](out/audio/cancel_order_010/bot_2.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## change_address_001: Change shipping address

### Turn 1 ✅

**User Text:** Hi, I just realized I put the wrong shipping address on my order. Can I change it?

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/change_address_001/user_1.wav](out/audio/change_address_001/user_1.wav)
- Bot: [out/audio/change_address_001/bot_1.wav](out/audio/change_address_001/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** It's order 34921.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/change_address_001/user_2.wav](out/audio/change_address_001/user_2.wav)
- Bot: [out/audio/change_address_001/bot_2.wav](out/audio/change_address_001/bot_2.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## change_address_002: Change shipping address

### Turn 1 ✅

**User Text:** Hello, I recently moved and need to update the delivery address for a package I ordered.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/change_address_002/user_1.wav](out/audio/change_address_002/user_1.wav)
- Bot: [out/audio/change_address_002/bot_1.wav](out/audio/change_address_002/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** The order number is 78215.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/change_address_002/user_2.wav](out/audio/change_address_002/user_2.wav)
- Bot: [out/audio/change_address_002/bot_2.wav](out/audio/change_address_002/bot_2.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## change_address_003: Change shipping address

### Turn 1 ✅

**User Text:** Hey, good morning. I need to change where my order gets delivered to, if that's possible.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/change_address_003/user_1.wav](out/audio/change_address_003/user_1.wav)
- Bot: [out/audio/change_address_003/bot_1.wav](out/audio/change_address_003/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Sure, order 56043.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/change_address_003/user_2.wav](out/audio/change_address_003/user_2.wav)
- Bot: [out/audio/change_address_003/bot_2.wav](out/audio/change_address_003/bot_2.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## change_address_004: Change shipping address

### Turn 1 ✅

**User Text:** I've been trying to change my shipping address on the website for an hour and it won't let me. Can someone just do it?

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/change_address_004/user_1.wav](out/audio/change_address_004/user_1.wav)
- Bot: [out/audio/change_address_004/bot_1.wav](out/audio/change_address_004/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 91387. Please just fix it.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/change_address_004/user_2.wav](out/audio/change_address_004/user_2.wav)
- Bot: [out/audio/change_address_004/bot_2.wav](out/audio/change_address_004/bot_2.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## change_address_005: Change shipping address

### Turn 1 ✅

**User Text:** My order is shipping to my old address and if it goes there I'm never gonna get it. I need this changed immediately.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/change_address_005/user_1.wav](out/audio/change_address_005/user_1.wav)
- Bot: [out/audio/change_address_005/bot_1.wav](out/audio/change_address_005/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** It's 42876. Hurry please, it's supposed to ship tomorrow.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/change_address_005/user_2.wav](out/audio/change_address_005/user_2.wav)
- Bot: [out/audio/change_address_005/bot_2.wav](out/audio/change_address_005/bot_2.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## change_address_006: Change shipping address

### Turn 1 ✅

**User Text:** This is so frustrating. I already called once and the address still wasn't changed. I need someone to actually update it this time.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/change_address_006/user_1.wav](out/audio/change_address_006/user_1.wav)
- Bot: [out/audio/change_address_006/bot_1.wav](out/audio/change_address_006/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 65739. And please make sure it actually goes through this time.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/change_address_006/user_2.wav](out/audio/change_address_006/user_2.wav)
- Bot: [out/audio/change_address_006/bot_2.wav](out/audio/change_address_006/bot_2.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## change_address_007: Change shipping address

### Turn 1 ❌

**User Text:** Hi, I need to change the shipping address for order 30482. I moved last week.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/change_address_007/user_1.wav](out/audio/change_address_007/user_1.wav)
- Bot: [out/audio/change_address_007/bot_1.wav](out/audio/change_address_007/bot_1.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## change_address_008: Change shipping address

### Turn 1 ❌

**User Text:** Hey, order 87654 needs to go to a different address. Can you update that for me?

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/change_address_008/user_1.wav](out/audio/change_address_008/user_1.wav)
- Bot: [out/audio/change_address_008/bot_1.wav](out/audio/change_address_008/bot_1.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## change_address_009: Change shipping address

### Turn 1 ✅

**User Text:** So um I think my package might be going to the wrong place? Like I'm not sure if I put the right address in when I ordered.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/change_address_009/user_1.wav](out/audio/change_address_009/user_1.wav)
- Bot: [out/audio/change_address_009/bot_1.wav](out/audio/change_address_009/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Oh right, uh... I think it was order 21456.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/change_address_009/user_2.wav](out/audio/change_address_009/user_2.wav)
- Bot: [out/audio/change_address_009/bot_2.wav](out/audio/change_address_009/bot_2.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## change_address_010: Change shipping address

### Turn 1 ✅

**User Text:** I need to like, change something on my order? The address part. I'm not really sure how this works.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/change_address_010/user_1.wav](out/audio/change_address_010/user_1.wav)
- Bot: [out/audio/change_address_010/bot_1.wav](out/audio/change_address_010/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Hmm hold on... I got it somewhere. Order 50198.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/change_address_010/user_2.wav](out/audio/change_address_010/user_2.wav)
- Bot: [out/audio/change_address_010/bot_2.wav](out/audio/change_address_010/bot_2.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## check_status_001: Check order status

### Turn 1 ❌

**User Text:** Hi, I was just wondering if you could tell me where my order is? I placed it a few days ago.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/check_status_001/user_1.wav](out/audio/check_status_001/user_1.wav)
- Bot: [out/audio/check_status_001/bot_1.wav](out/audio/check_status_001/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 82714.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/check_status_001/user_2.wav](out/audio/check_status_001/user_2.wav)
- Bot: [out/audio/check_status_001/bot_2.wav](out/audio/check_status_001/bot_2.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## check_status_002: Check order status

### Turn 1 ❌

**User Text:** Hello, I'd like to check on the status of a recent order please.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/check_status_002/user_1.wav](out/audio/check_status_002/user_1.wav)
- Bot: [out/audio/check_status_002/bot_1.wav](out/audio/check_status_002/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Yeah, the order number is 59301.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/check_status_002/user_2.wav](out/audio/check_status_002/user_2.wav)
- Bot: [out/audio/check_status_002/bot_2.wav](out/audio/check_status_002/bot_2.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## check_status_003: Check order status

### Turn 1 ❌

**User Text:** Hey there, I'm hoping to get an update on my package. It was supposed to arrive yesterday.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/check_status_003/user_1.wav](out/audio/check_status_003/user_1.wav)
- Bot: [out/audio/check_status_003/bot_1.wav](out/audio/check_status_003/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Sure, it's order 46083.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/check_status_003/user_2.wav](out/audio/check_status_003/user_2.wav)
- Bot: [out/audio/check_status_003/bot_2.wav](out/audio/check_status_003/bot_2.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## check_status_004: Check order status

### Turn 1 ❌

**User Text:** Where's my order? It was supposed to be here three days ago and I've got nothing.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/check_status_004/user_1.wav](out/audio/check_status_004/user_1.wav)
- Bot: [out/audio/check_status_004/bot_1.wav](out/audio/check_status_004/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 37462. I need an answer.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/check_status_004/user_2.wav](out/audio/check_status_004/user_2.wav)
- Bot: [out/audio/check_status_004/bot_2.wav](out/audio/check_status_004/bot_2.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## check_status_005: Check order status

### Turn 1 ❌

**User Text:** I've been waiting for over a week for this package. This is unacceptable. Where is it?

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/check_status_005/user_1.wav](out/audio/check_status_005/user_1.wav)
- Bot: [out/audio/check_status_005/bot_1.wav](out/audio/check_status_005/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** It's 71845. Someone better tell me what's going on.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/check_status_005/user_2.wav](out/audio/check_status_005/user_2.wav)
- Bot: [out/audio/check_status_005/bot_2.wav](out/audio/check_status_005/bot_2.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## check_status_006: Check order status

### Turn 1 ❌

**User Text:** I'm calling because your tracking page hasn't updated in five days. What is happening with my order?

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/check_status_006/user_1.wav](out/audio/check_status_006/user_1.wav)
- Bot: [out/audio/check_status_006/bot_1.wav](out/audio/check_status_006/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 20569. And your website tracking is broken apparently.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/check_status_006/user_2.wav](out/audio/check_status_006/user_2.wav)
- Bot: [out/audio/check_status_006/bot_2.wav](out/audio/check_status_006/bot_2.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## check_status_007: Check order status

### Turn 1 ❌

**User Text:** Hey, can I get a status update on order 93471? Just wanna know when it'll be here.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/check_status_007/user_1.wav](out/audio/check_status_007/user_1.wav)
- Bot: [out/audio/check_status_007/bot_1.wav](out/audio/check_status_007/bot_1.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## check_status_008: Check order status

### Turn 1 ❌

**User Text:** I'm checking on order 64108. It should have arrived by now, what's the status?

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/check_status_008/user_1.wav](out/audio/check_status_008/user_1.wav)
- Bot: [out/audio/check_status_008/bot_1.wav](out/audio/check_status_008/bot_1.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## check_status_009: Check order status

### Turn 1 ❌

**User Text:** So like, I ordered something a while back and I'm not really sure if it's coming or not? Is there a way to check?

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/check_status_009/user_1.wav](out/audio/check_status_009/user_1.wav)
- Bot: [out/audio/check_status_009/bot_1.wav](out/audio/check_status_009/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Um... I think it was order 15923? Or maybe... yeah, 15923.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/check_status_009/user_2.wav](out/audio/check_status_009/user_2.wav)
- Bot: [out/audio/check_status_009/bot_2.wav](out/audio/check_status_009/bot_2.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## check_status_010: Check order status

### Turn 1 ❌

**User Text:** I got an email about something shipping but I don't know which order it was. Can you look it up?

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/check_status_010/user_1.wav](out/audio/check_status_010/user_1.wav)
- Bot: [out/audio/check_status_010/bot_1.wav](out/audio/check_status_010/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Hmm let me find it... order 88256 I think.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/check_status_010/user_2.wav](out/audio/check_status_010/user_2.wav)
- Bot: [out/audio/check_status_010/bot_2.wav](out/audio/check_status_010/bot_2.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## duplicate_charge_001: Request refund for duplicate charge

### Turn 1 ✅

**User Text:** Hi, I noticed I was charged twice for my last order. I'd like to get a refund for the extra charge please.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/duplicate_charge_001/user_1.wav](out/audio/duplicate_charge_001/user_1.wav)
- Bot: [out/audio/duplicate_charge_001/bot_1.wav](out/audio/duplicate_charge_001/bot_1.wav)

**Expected:** {'contains_any': ['last four digits', 'card', 'last four', 'card ending']}

---

### Turn 2 ❌

**User Text:** Sure, the card ends in 4829.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/duplicate_charge_001/user_2.wav](out/audio/duplicate_charge_001/user_2.wav)
- Bot: [out/audio/duplicate_charge_001/bot_2.wav](out/audio/duplicate_charge_001/bot_2.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## duplicate_charge_002: Request refund for duplicate charge

### Turn 1 ✅

**User Text:** Hello, I'm seeing two identical charges on my statement from your store. Could you help me sort that out?

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/duplicate_charge_002/user_1.wav](out/audio/duplicate_charge_002/user_1.wav)
- Bot: [out/audio/duplicate_charge_002/bot_1.wav](out/audio/duplicate_charge_002/bot_1.wav)

**Expected:** {'contains_any': ['last four digits', 'card', 'last four', 'card ending']}

---

### Turn 2 ❌

**User Text:** It's the card ending in 7163.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/duplicate_charge_002/user_2.wav](out/audio/duplicate_charge_002/user_2.wav)
- Bot: [out/audio/duplicate_charge_002/bot_2.wav](out/audio/duplicate_charge_002/bot_2.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## duplicate_charge_003: Request refund for duplicate charge

### Turn 1 ✅

**User Text:** Good afternoon. I was double charged for a purchase and would like a refund on the duplicate.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/duplicate_charge_003/user_1.wav](out/audio/duplicate_charge_003/user_1.wav)
- Bot: [out/audio/duplicate_charge_003/bot_1.wav](out/audio/duplicate_charge_003/bot_1.wav)

**Expected:** {'contains_any': ['last four digits', 'card', 'last four', 'card ending']}

---

### Turn 2 ❌

**User Text:** Yeah the last four are 5308.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/duplicate_charge_003/user_2.wav](out/audio/duplicate_charge_003/user_2.wav)
- Bot: [out/audio/duplicate_charge_003/bot_2.wav](out/audio/duplicate_charge_003/bot_2.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## duplicate_charge_004: Request refund for duplicate charge

### Turn 1 ✅

**User Text:** I've been charged twice for the same order and this is completely unacceptable. I want my money back right now.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/duplicate_charge_004/user_1.wav](out/audio/duplicate_charge_004/user_1.wav)
- Bot: [out/audio/duplicate_charge_004/bot_1.wav](out/audio/duplicate_charge_004/bot_1.wav)

**Expected:** {'contains_any': ['last four digits', 'card', 'last four', 'card ending']}

---

### Turn 2 ❌

**User Text:** Card ending 9241. How long is this gonna take?

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/duplicate_charge_004/user_2.wav](out/audio/duplicate_charge_004/user_2.wav)
- Bot: [out/audio/duplicate_charge_004/bot_2.wav](out/audio/duplicate_charge_004/bot_2.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## duplicate_charge_005: Request refund for duplicate charge

### Turn 1 ✅

**User Text:** This is the third time I've called about this! You guys double charged me and nobody's fixed it yet!

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/duplicate_charge_005/user_1.wav](out/audio/duplicate_charge_005/user_1.wav)
- Bot: [out/audio/duplicate_charge_005/bot_1.wav](out/audio/duplicate_charge_005/bot_1.wav)

**Expected:** {'contains_any': ['last four digits', 'card', 'last four', 'card ending']}

---

### Turn 2 ❌

**User Text:** Card ending 3756. I shouldn't have to keep calling.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/duplicate_charge_005/user_2.wav](out/audio/duplicate_charge_005/user_2.wav)
- Bot: [out/audio/duplicate_charge_005/bot_2.wav](out/audio/duplicate_charge_005/bot_2.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## duplicate_charge_006: Request refund for duplicate charge

### Turn 1 ✅

**User Text:** Seriously? I just checked my bank and there's two charges from you for the exact same amount. Fix this please.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/duplicate_charge_006/user_1.wav](out/audio/duplicate_charge_006/user_1.wav)
- Bot: [out/audio/duplicate_charge_006/bot_1.wav](out/audio/duplicate_charge_006/bot_1.wav)

**Expected:** {'contains_any': ['last four digits', 'card', 'last four', 'card ending']}

---

### Turn 2 ❌

**User Text:** It's 6184. And I want a confirmation email.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/duplicate_charge_006/user_2.wav](out/audio/duplicate_charge_006/user_2.wav)
- Bot: [out/audio/duplicate_charge_006/bot_2.wav](out/audio/duplicate_charge_006/bot_2.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## duplicate_charge_007: Request refund for duplicate charge

### Turn 1 ❌

**User Text:** Hey, I got double charged on my card ending 2047 and I need the duplicate refunded.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/duplicate_charge_007/user_1.wav](out/audio/duplicate_charge_007/user_1.wav)
- Bot: [out/audio/duplicate_charge_007/bot_1.wav](out/audio/duplicate_charge_007/bot_1.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## duplicate_charge_008: Request refund for duplicate charge

### Turn 1 ❌

**User Text:** I see two charges for the same thing on my Visa ending in 8593. Can you reverse one of them?

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/duplicate_charge_008/user_1.wav](out/audio/duplicate_charge_008/user_1.wav)
- Bot: [out/audio/duplicate_charge_008/bot_1.wav](out/audio/duplicate_charge_008/bot_1.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## duplicate_charge_009: Request refund for duplicate charge

### Turn 1 ✅

**User Text:** I got charged for something? I don't know, it was on my credit card. It looks like it went through twice maybe?

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/duplicate_charge_009/user_1.wav](out/audio/duplicate_charge_009/user_1.wav)
- Bot: [out/audio/duplicate_charge_009/bot_1.wav](out/audio/duplicate_charge_009/bot_1.wav)

**Expected:** {'contains_any': ['last four digits', 'card', 'last four', 'card ending']}

---

### Turn 2 ❌

**User Text:** Umm which card... oh the one ending in 1472.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/duplicate_charge_009/user_2.wav](out/audio/duplicate_charge_009/user_2.wav)
- Bot: [out/audio/duplicate_charge_009/bot_2.wav](out/audio/duplicate_charge_009/bot_2.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## duplicate_charge_010: Request refund for duplicate charge

### Turn 1 ✅

**User Text:** So there's this weird charge on my statement, and I think it might be a duplicate? I'm not really sure what happened.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/duplicate_charge_010/user_1.wav](out/audio/duplicate_charge_010/user_1.wav)
- Bot: [out/audio/duplicate_charge_010/bot_1.wav](out/audio/duplicate_charge_010/bot_1.wav)

**Expected:** {'contains_any': ['last four digits', 'card', 'last four', 'card ending']}

---

### Turn 2 ❌

**User Text:** Uh let me check... card ending 6039 I think.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/duplicate_charge_010/user_2.wav](out/audio/duplicate_charge_010/user_2.wav)
- Bot: [out/audio/duplicate_charge_010/bot_2.wav](out/audio/duplicate_charge_010/bot_2.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## missing_package_001: Report a missing package

### Turn 1 ❌

**User Text:** Hi, my tracking says my package was delivered but I don't have it. I checked everywhere.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/missing_package_001/user_1.wav](out/audio/missing_package_001/user_1.wav)
- Bot: [out/audio/missing_package_001/bot_1.wav](out/audio/missing_package_001/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 74219.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/missing_package_001/user_2.wav](out/audio/missing_package_001/user_2.wav)
- Bot: [out/audio/missing_package_001/bot_2.wav](out/audio/missing_package_001/bot_2.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## missing_package_002: Report a missing package

### Turn 1 ❌

**User Text:** Hello, I got a delivery notification yesterday but there's nothing at my door. Can you help me figure out what happened?

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/missing_package_002/user_1.wav](out/audio/missing_package_002/user_1.wav)
- Bot: [out/audio/missing_package_002/bot_1.wav](out/audio/missing_package_002/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** It's order 38105.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/missing_package_002/user_2.wav](out/audio/missing_package_002/user_2.wav)
- Bot: [out/audio/missing_package_002/bot_2.wav](out/audio/missing_package_002/bot_2.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## missing_package_003: Report a missing package

### Turn 1 ❌

**User Text:** Hey, I think my package might be lost. It says delivered but I've checked the porch, the mailbox, everything.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/missing_package_003/user_1.wav](out/audio/missing_package_003/user_1.wav)
- Bot: [out/audio/missing_package_003/bot_1.wav](out/audio/missing_package_003/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Yeah, order 52847.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/missing_package_003/user_2.wav](out/audio/missing_package_003/user_2.wav)
- Bot: [out/audio/missing_package_003/bot_2.wav](out/audio/missing_package_003/bot_2.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## missing_package_004: Report a missing package

### Turn 1 ❌

**User Text:** Someone stole my package or your driver delivered it to the wrong house. Either way, I don't have it and I'm furious.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/missing_package_004/user_1.wav](out/audio/missing_package_004/user_1.wav)
- Bot: [out/audio/missing_package_004/bot_1.wav](out/audio/missing_package_004/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 61934. I want this resolved today.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/missing_package_004/user_2.wav](out/audio/missing_package_004/user_2.wav)
- Bot: [out/audio/missing_package_004/bot_2.wav](out/audio/missing_package_004/bot_2.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## missing_package_005: Report a missing package

### Turn 1 ❌

**User Text:** This is the second time a package has gone missing. I'm seriously considering never ordering from you again.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/missing_package_005/user_1.wav](out/audio/missing_package_005/user_1.wav)
- Bot: [out/audio/missing_package_005/bot_1.wav](out/audio/missing_package_005/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** It's 90283. And don't tell me to wait, I already waited three days.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/missing_package_005/user_2.wav](out/audio/missing_package_005/user_2.wav)
- Bot: [out/audio/missing_package_005/bot_2.wav](out/audio/missing_package_005/bot_2.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## missing_package_006: Report a missing package

### Turn 1 ❌

**User Text:** Your delivery driver marked it delivered but I have a ring camera and nobody came to my door. Where is my stuff?

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/missing_package_006/user_1.wav](out/audio/missing_package_006/user_1.wav)
- Bot: [out/audio/missing_package_006/bot_1.wav](out/audio/missing_package_006/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 45672. I can send you the camera footage if you need it.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/missing_package_006/user_2.wav](out/audio/missing_package_006/user_2.wav)
- Bot: [out/audio/missing_package_006/bot_2.wav](out/audio/missing_package_006/bot_2.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## missing_package_007: Report a missing package

### Turn 1 ❌

**User Text:** Hey, order 27318 says it was delivered but it's not here. I need to report it missing.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/missing_package_007/user_1.wav](out/audio/missing_package_007/user_1.wav)
- Bot: [out/audio/missing_package_007/bot_1.wav](out/audio/missing_package_007/bot_1.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## missing_package_008: Report a missing package

### Turn 1 ❌

**User Text:** I'm calling about order 83056. Tracking shows delivered two days ago and I never got it.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/missing_package_008/user_1.wav](out/audio/missing_package_008/user_1.wav)
- Bot: [out/audio/missing_package_008/bot_1.wav](out/audio/missing_package_008/bot_1.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## missing_package_009: Report a missing package

### Turn 1 ❌

**User Text:** Hey so uh, I was expecting something in the mail and it never showed up? I'm not really sure what happened to it.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/missing_package_009/user_1.wav](out/audio/missing_package_009/user_1.wav)
- Bot: [out/audio/missing_package_009/bot_1.wav](out/audio/missing_package_009/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Oh um, the order number... let me look. I think it's 16549.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/missing_package_009/user_2.wav](out/audio/missing_package_009/user_2.wav)
- Bot: [out/audio/missing_package_009/bot_2.wav](out/audio/missing_package_009/bot_2.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## missing_package_010: Report a missing package

### Turn 1 ❌

**User Text:** I think my package might not have come? Like the app says something about delivery but I didn't see anything outside.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/missing_package_010/user_1.wav](out/audio/missing_package_010/user_1.wav)
- Bot: [out/audio/missing_package_010/bot_1.wav](out/audio/missing_package_010/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** Hmm I'm not sure where to find the order number... oh here. Order 73401.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/missing_package_010/user_2.wav](out/audio/missing_package_010/user_2.wav)
- Bot: [out/audio/missing_package_010/bot_2.wav](out/audio/missing_package_010/bot_2.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## reset_password_001: Reset account password

### Turn 1 ❌

**User Text:** Hi, I can't seem to log into my account. I think I need to reset my password.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/reset_password_001/user_1.wav](out/audio/reset_password_001/user_1.wav)
- Bot: [out/audio/reset_password_001/bot_1.wav](out/audio/reset_password_001/bot_1.wav)

**Expected:** {'contains_any': ['email', 'email address', 'email on file']}

---

### Turn 2 ❌

**User Text:** Sure, it's jennifer.walsh@gmail.com.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/reset_password_001/user_2.wav](out/audio/reset_password_001/user_2.wav)
- Bot: [out/audio/reset_password_001/bot_2.wav](out/audio/reset_password_001/bot_2.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## reset_password_002: Reset account password

### Turn 1 ❌

**User Text:** Hello, I forgot my password and I need to get back into my account. Can you help?

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/reset_password_002/user_1.wav](out/audio/reset_password_002/user_1.wav)
- Bot: [out/audio/reset_password_002/bot_1.wav](out/audio/reset_password_002/bot_1.wav)

**Expected:** {'contains_any': ['email', 'email address', 'email on file']}

---

### Turn 2 ❌

**User Text:** My email is marcus.chen88@yahoo.com.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/reset_password_002/user_2.wav](out/audio/reset_password_002/user_2.wav)
- Bot: [out/audio/reset_password_002/bot_2.wav](out/audio/reset_password_002/bot_2.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## reset_password_003: Reset account password

### Turn 1 ❌

**User Text:** Hey, I'm locked out of my account. I've tried a few passwords but none of them work.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/reset_password_003/user_1.wav](out/audio/reset_password_003/user_1.wav)
- Bot: [out/audio/reset_password_003/bot_1.wav](out/audio/reset_password_003/bot_1.wav)

**Expected:** {'contains_any': ['email', 'email address', 'email on file']}

---

### Turn 2 ❌

**User Text:** It's sarah.k.morrison@outlook.com.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/reset_password_003/user_2.wav](out/audio/reset_password_003/user_2.wav)
- Bot: [out/audio/reset_password_003/bot_2.wav](out/audio/reset_password_003/bot_2.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## reset_password_004: Reset account password

### Turn 1 ❌

**User Text:** Your stupid reset email never comes through! I've requested it four times and nothing. I need my password reset NOW.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/reset_password_004/user_1.wav](out/audio/reset_password_004/user_1.wav)
- Bot: [out/audio/reset_password_004/bot_1.wav](out/audio/reset_password_004/bot_1.wav)

**Expected:** {'contains_any': ['email', 'email address', 'email on file']}

---

### Turn 2 ❌

**User Text:** d.gonzalez@hotmail.com. And check my spam folder? I already did.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/reset_password_004/user_2.wav](out/audio/reset_password_004/user_2.wav)
- Bot: [out/audio/reset_password_004/bot_2.wav](out/audio/reset_password_004/bot_2.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## reset_password_005: Reset account password

### Turn 1 ❌

**User Text:** I've been locked out for two days and I need to place an order. Why is this so difficult?

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/reset_password_005/user_1.wav](out/audio/reset_password_005/user_1.wav)
- Bot: [out/audio/reset_password_005/bot_1.wav](out/audio/reset_password_005/bot_1.wav)

**Expected:** {'contains_any': ['email', 'email address', 'email on file']}

---

### Turn 2 ❌

**User Text:** robert.james.finn@gmail.com. Please actually send it this time.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/reset_password_005/user_2.wav](out/audio/reset_password_005/user_2.wav)
- Bot: [out/audio/reset_password_005/bot_2.wav](out/audio/reset_password_005/bot_2.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## reset_password_006: Reset account password

### Turn 1 ❌

**User Text:** This is ridiculous. I changed my password last week and now it doesn't work again. Something's wrong with your system.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/reset_password_006/user_1.wav](out/audio/reset_password_006/user_1.wav)
- Bot: [out/audio/reset_password_006/bot_1.wav](out/audio/reset_password_006/bot_1.wav)

**Expected:** {'contains_any': ['email', 'email address', 'email on file']}

---

### Turn 2 ❌

**User Text:** It's natalie.p.brooks@icloud.com.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/reset_password_006/user_2.wav](out/audio/reset_password_006/user_2.wav)
- Bot: [out/audio/reset_password_006/bot_2.wav](out/audio/reset_password_006/bot_2.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## reset_password_007: Reset account password

### Turn 1 ❌

**User Text:** I need a password reset for my account, the email on file is kevin.adler@gmail.com.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/reset_password_007/user_1.wav](out/audio/reset_password_007/user_1.wav)
- Bot: [out/audio/reset_password_007/bot_1.wav](out/audio/reset_password_007/bot_1.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## reset_password_008: Reset account password

### Turn 1 ❌

**User Text:** Hey can you send a password reset to amy.liu.writes@yahoo.com? I'm totally locked out.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/reset_password_008/user_1.wav](out/audio/reset_password_008/user_1.wav)
- Bot: [out/audio/reset_password_008/bot_1.wav](out/audio/reset_password_008/bot_1.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## reset_password_009: Reset account password

### Turn 1 ❌

**User Text:** So uh, I can't get in. Like I'm typing my password and it keeps saying it's wrong. I don't know what to do.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/reset_password_009/user_1.wav](out/audio/reset_password_009/user_1.wav)
- Bot: [out/audio/reset_password_009/bot_1.wav](out/audio/reset_password_009/bot_1.wav)

**Expected:** {'contains_any': ['email', 'email address', 'email on file']}

---

### Turn 2 ❌

**User Text:** Oh, my email? I think I used... tom.baker.99@gmail.com. Or wait, no. Yeah, that one.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/reset_password_009/user_2.wav](out/audio/reset_password_009/user_2.wav)
- Bot: [out/audio/reset_password_009/bot_2.wav](out/audio/reset_password_009/bot_2.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## reset_password_010: Reset account password

### Turn 1 ❌

**User Text:** I'm having trouble with my account thing. The login isn't working? I'm not sure if it's my password or what.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/reset_password_010/user_1.wav](out/audio/reset_password_010/user_1.wav)
- Bot: [out/audio/reset_password_010/bot_1.wav](out/audio/reset_password_010/bot_1.wav)

**Expected:** {'contains_any': ['email', 'email address', 'email on file']}

---

### Turn 2 ❌

**User Text:** Hmm let me think... it's either lisa.v.wright@outlook.com or... no that's the one.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/reset_password_010/user_2.wav](out/audio/reset_password_010/user_2.wav)
- Bot: [out/audio/reset_password_010/bot_2.wav](out/audio/reset_password_010/bot_2.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## return_damaged_001: Return a damaged item

### Turn 1 ✅

**User Text:** Hi there, I received a product that's damaged and I'd like to return it please.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/return_damaged_001/user_1.wav](out/audio/return_damaged_001/user_1.wav)
- Bot: [out/audio/return_damaged_001/bot_1.wav](out/audio/return_damaged_001/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'have your order', 'which order']}

---

### Turn 2 ❌

**User Text:** Sure, it's order 48291.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/return_damaged_001/user_2.wav](out/audio/return_damaged_001/user_2.wav)
- Bot: [out/audio/return_damaged_001/bot_2.wav](out/audio/return_damaged_001/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## return_damaged_002: Return a damaged item

### Turn 1 ✅

**User Text:** Good morning, I got a package yesterday and the item inside was broken. I'd like to send it back.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/return_damaged_002/user_1.wav](out/audio/return_damaged_002/user_1.wav)
- Bot: [out/audio/return_damaged_002/bot_1.wav](out/audio/return_damaged_002/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'have your order', 'which order']}

---

### Turn 2 ❌

**User Text:** Yeah the order number is 57134.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/return_damaged_002/user_2.wav](out/audio/return_damaged_002/user_2.wav)
- Bot: [out/audio/return_damaged_002/bot_2.wav](out/audio/return_damaged_002/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## return_damaged_003: Return a damaged item

### Turn 1 ✅

**User Text:** Hello, I'm hoping you can help me. I need to return something that came in pretty bad shape.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/return_damaged_003/user_1.wav](out/audio/return_damaged_003/user_1.wav)
- Bot: [out/audio/return_damaged_003/bot_1.wav](out/audio/return_damaged_003/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'have your order', 'which order']}

---

### Turn 2 ❌

**User Text:** Let me check... okay it's order 63408.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/return_damaged_003/user_2.wav](out/audio/return_damaged_003/user_2.wav)
- Bot: [out/audio/return_damaged_003/bot_2.wav](out/audio/return_damaged_003/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## return_damaged_004: Return a damaged item

### Turn 1 ✅

**User Text:** Yeah I need to return this thing, it showed up completely smashed. This is ridiculous.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/return_damaged_004/user_1.wav](out/audio/return_damaged_004/user_1.wav)
- Bot: [out/audio/return_damaged_004/bot_1.wav](out/audio/return_damaged_004/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'have your order', 'which order']}

---

### Turn 2 ❌

**User Text:** It's 29174. Can we hurry this up?

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/return_damaged_004/user_2.wav](out/audio/return_damaged_004/user_2.wav)
- Bot: [out/audio/return_damaged_004/bot_2.wav](out/audio/return_damaged_004/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## return_damaged_005: Return a damaged item

### Turn 1 ✅

**User Text:** This is the second time I've gotten a broken item from you guys. I want to return it and honestly I'm pretty upset about it.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/return_damaged_005/user_1.wav](out/audio/return_damaged_005/user_1.wav)
- Bot: [out/audio/return_damaged_005/bot_1.wav](out/audio/return_damaged_005/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'have your order', 'which order']}

---

### Turn 2 ❌

**User Text:** Order 83652. And I want this handled quickly please.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/return_damaged_005/user_2.wav](out/audio/return_damaged_005/user_2.wav)
- Bot: [out/audio/return_damaged_005/bot_2.wav](out/audio/return_damaged_005/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## return_damaged_006: Return a damaged item

### Turn 1 ✅

**User Text:** Look, I've been waiting on hold for twenty minutes. The blender I ordered arrived cracked and I need to return it now.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/return_damaged_006/user_1.wav](out/audio/return_damaged_006/user_1.wav)
- Bot: [out/audio/return_damaged_006/bot_1.wav](out/audio/return_damaged_006/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'have your order', 'which order']}

---

### Turn 2 ❌

**User Text:** It's order 41087, come on.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/return_damaged_006/user_2.wav](out/audio/return_damaged_006/user_2.wav)
- Bot: [out/audio/return_damaged_006/bot_2.wav](out/audio/return_damaged_006/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## return_damaged_007: Return a damaged item

### Turn 1 ❌

**User Text:** Hey I need to return order 72563, it arrived with a huge crack in it.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/return_damaged_007/user_1.wav](out/audio/return_damaged_007/user_1.wav)
- Bot: [out/audio/return_damaged_007/bot_1.wav](out/audio/return_damaged_007/bot_1.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## return_damaged_008: Return a damaged item

### Turn 1 ❌

**User Text:** Hi, my order number is 19846 and the toaster I got is completely busted, I need to send it back.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/return_damaged_008/user_1.wav](out/audio/return_damaged_008/user_1.wav)
- Bot: [out/audio/return_damaged_008/bot_1.wav](out/audio/return_damaged_008/bot_1.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## return_damaged_009: Return a damaged item

### Turn 1 ✅

**User Text:** Um yeah so I got this thing and it's like... not right? It's all messed up. I think I wanna send it back.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/return_damaged_009/user_1.wav](out/audio/return_damaged_009/user_1.wav)
- Bot: [out/audio/return_damaged_009/bot_1.wav](out/audio/return_damaged_009/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'have your order', 'which order']}

---

### Turn 2 ❌

**User Text:** Oh uh, let me look... I think it's like... order 35021? Yeah that one.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/return_damaged_009/user_2.wav](out/audio/return_damaged_009/user_2.wav)
- Bot: [out/audio/return_damaged_009/bot_2.wav](out/audio/return_damaged_009/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## return_damaged_010: Return a damaged item

### Turn 1 ✅

**User Text:** So I ordered something a while back and it wasn't in good condition when it got here. I don't really know what to do about it.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/return_damaged_010/user_1.wav](out/audio/return_damaged_010/user_1.wav)
- Bot: [out/audio/return_damaged_010/bot_1.wav](out/audio/return_damaged_010/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'have your order', 'which order']}

---

### Turn 2 ❌

**User Text:** Hmm I think the number was... hold on... 60473.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/return_damaged_010/user_2.wav](out/audio/return_damaged_010/user_2.wav)
- Bot: [out/audio/return_damaged_010/bot_2.wav](out/audio/return_damaged_010/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## upgrade_sub_001: Upgrade subscription plan

### Turn 1 ❌

**User Text:** Hi, I'd like to upgrade my subscription to the premium plan please.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/upgrade_sub_001/user_1.wav](out/audio/upgrade_sub_001/user_1.wav)
- Bot: [out/audio/upgrade_sub_001/bot_1.wav](out/audio/upgrade_sub_001/bot_1.wav)

**Expected:** {'contains_any': ['account number', 'account', 'account details']}

---

### Turn 2 ❌

**User Text:** My account number is 80421.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/upgrade_sub_001/user_2.wav](out/audio/upgrade_sub_001/user_2.wav)
- Bot: [out/audio/upgrade_sub_001/bot_2.wav](out/audio/upgrade_sub_001/bot_2.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

## upgrade_sub_002: Upgrade subscription plan

### Turn 1 ❌

**User Text:** Hello, I'm currently on the basic plan and I want to move up to the next tier.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/upgrade_sub_002/user_1.wav](out/audio/upgrade_sub_002/user_1.wav)
- Bot: [out/audio/upgrade_sub_002/bot_1.wav](out/audio/upgrade_sub_002/bot_1.wav)

**Expected:** {'contains_any': ['account number', 'account', 'account details']}

---

### Turn 2 ❌

**User Text:** Sure, the account number is 56738.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/upgrade_sub_002/user_2.wav](out/audio/upgrade_sub_002/user_2.wav)
- Bot: [out/audio/upgrade_sub_002/bot_2.wav](out/audio/upgrade_sub_002/bot_2.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

## upgrade_sub_003: Upgrade subscription plan

### Turn 1 ❌

**User Text:** Hey, I've been thinking about upgrading my plan. Can you walk me through that?

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/upgrade_sub_003/user_1.wav](out/audio/upgrade_sub_003/user_1.wav)
- Bot: [out/audio/upgrade_sub_003/bot_1.wav](out/audio/upgrade_sub_003/bot_1.wav)

**Expected:** {'contains_any': ['account number', 'account', 'account details']}

---

### Turn 2 ❌

**User Text:** Oh right, it's account 32914.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/upgrade_sub_003/user_2.wav](out/audio/upgrade_sub_003/user_2.wav)
- Bot: [out/audio/upgrade_sub_003/bot_2.wav](out/audio/upgrade_sub_003/bot_2.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

## upgrade_sub_004: Upgrade subscription plan

### Turn 1 ❌

**User Text:** I've been trying to upgrade on your website and it keeps crashing. Can you just do it for me? This is so annoying.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/upgrade_sub_004/user_1.wav](out/audio/upgrade_sub_004/user_1.wav)
- Bot: [out/audio/upgrade_sub_004/bot_1.wav](out/audio/upgrade_sub_004/bot_1.wav)

**Expected:** {'contains_any': ['account number', 'account', 'account details']}

---

### Turn 2 ❌

**User Text:** Account 69105. Just upgrade it already.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/upgrade_sub_004/user_2.wav](out/audio/upgrade_sub_004/user_2.wav)
- Bot: [out/audio/upgrade_sub_004/bot_2.wav](out/audio/upgrade_sub_004/bot_2.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

## upgrade_sub_005: Upgrade subscription plan

### Turn 1 ❌

**User Text:** Why is it so hard to upgrade my plan? I've clicked every button on your site and nothing happens.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/upgrade_sub_005/user_1.wav](out/audio/upgrade_sub_005/user_1.wav)
- Bot: [out/audio/upgrade_sub_005/bot_1.wav](out/audio/upgrade_sub_005/bot_1.wav)

**Expected:** {'contains_any': ['account number', 'account', 'account details']}

---

### Turn 2 ❌

**User Text:** It's 47283. And you really need to fix that page.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/upgrade_sub_005/user_2.wav](out/audio/upgrade_sub_005/user_2.wav)
- Bot: [out/audio/upgrade_sub_005/bot_2.wav](out/audio/upgrade_sub_005/bot_2.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

## upgrade_sub_006: Upgrade subscription plan

### Turn 1 ❌

**User Text:** I emailed about upgrading a week ago and never heard back. I'm calling now because clearly nobody reads emails over there.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/upgrade_sub_006/user_1.wav](out/audio/upgrade_sub_006/user_1.wav)
- Bot: [out/audio/upgrade_sub_006/bot_1.wav](out/audio/upgrade_sub_006/bot_1.wav)

**Expected:** {'contains_any': ['account number', 'account', 'account details']}

---

### Turn 2 ❌

**User Text:** Account number is 91560.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/upgrade_sub_006/user_2.wav](out/audio/upgrade_sub_006/user_2.wav)
- Bot: [out/audio/upgrade_sub_006/bot_2.wav](out/audio/upgrade_sub_006/bot_2.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

## upgrade_sub_007: Upgrade subscription plan

### Turn 1 ❌

**User Text:** Hey, account 24897 here, I want to upgrade to the premium tier.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/upgrade_sub_007/user_1.wav](out/audio/upgrade_sub_007/user_1.wav)
- Bot: [out/audio/upgrade_sub_007/bot_1.wav](out/audio/upgrade_sub_007/bot_1.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

## upgrade_sub_008: Upgrade subscription plan

### Turn 1 ❌

**User Text:** I'm calling to upgrade my subscription. My account number is 75346 and I want the highest plan.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/upgrade_sub_008/user_1.wav](out/audio/upgrade_sub_008/user_1.wav)
- Bot: [out/audio/upgrade_sub_008/bot_1.wav](out/audio/upgrade_sub_008/bot_1.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

## upgrade_sub_009: Upgrade subscription plan

### Turn 1 ❌

**User Text:** So I think I wanna change my plan? Like get more features or whatever? I'm not sure what's available.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/upgrade_sub_009/user_1.wav](out/audio/upgrade_sub_009/user_1.wav)
- Bot: [out/audio/upgrade_sub_009/bot_1.wav](out/audio/upgrade_sub_009/bot_1.wav)

**Expected:** {'contains_any': ['account number', 'account', 'account details']}

---

### Turn 2 ❌

**User Text:** Uh I think my account is... hold on... 18603? Yeah.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/upgrade_sub_009/user_2.wav](out/audio/upgrade_sub_009/user_2.wav)
- Bot: [out/audio/upgrade_sub_009/bot_2.wav](out/audio/upgrade_sub_009/bot_2.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

## upgrade_sub_010: Upgrade subscription plan

### Turn 1 ❌

**User Text:** Hi, um, someone told me I could get a better plan? I don't really know the difference between them.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/upgrade_sub_010/user_1.wav](out/audio/upgrade_sub_010/user_1.wav)
- Bot: [out/audio/upgrade_sub_010/bot_1.wav](out/audio/upgrade_sub_010/bot_1.wav)

**Expected:** {'contains_any': ['account number', 'account', 'account details']}

---

### Turn 2 ❌

**User Text:** My account... hmm... I think it's 53082.

**User ASR:** 

**Bot Text:** I'm not sure I understand. Could you please clarify what you'd like help with?

**Audio Files:**
- User: [out/audio/upgrade_sub_010/user_2.wav](out/audio/upgrade_sub_010/user_2.wav)
- Bot: [out/audio/upgrade_sub_010/bot_2.wav](out/audio/upgrade_sub_010/bot_2.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

