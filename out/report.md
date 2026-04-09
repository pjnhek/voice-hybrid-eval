# Hybrid Voice Eval Report

## Summary

**Intent Detection Accuracy:** 16/16 (100%)

| Scenario | Intent | Result | Steps Passed |
|----------|--------|--------|--------------|
| cancel_order_004 | ✅ (turn 1) | ✅ PASS | 2/2 |
| cancel_order_009 | ✅ (turn 1) | ✅ PASS | 2/2 |
| change_address_006 | ✅ (turn 1) | ✅ PASS | 2/2 |
| change_address_009 | ✅ (turn 1) | ✅ PASS | 2/2 |
| check_status_005 | ✅ (turn 1) | ❌ FAIL | 1/2 |
| check_status_010 | ✅ (turn 1) | ✅ PASS | 2/2 |
| duplicate_charge_004 | ✅ (turn 1) | ✅ PASS | 2/2 |
| duplicate_charge_009 | ✅ (turn 1) | ✅ PASS | 2/2 |
| missing_package_004 | ✅ (turn 1) | ✅ PASS | 2/2 |
| missing_package_009 | ✅ (turn 1) | ✅ PASS | 2/2 |
| reset_password_005 | ✅ (turn 1) | ✅ PASS | 2/2 |
| reset_password_009 | ✅ (turn 1) | ✅ PASS | 2/2 |
| return_damaged_006 | ✅ (turn 1) | ✅ PASS | 2/2 |
| return_damaged_010 | ✅ (turn 1) | ✅ PASS | 2/2 |
| upgrade_sub_004 | ✅ (turn 1) | ✅ PASS | 2/2 |
| upgrade_sub_009 | ✅ (turn 1) | ✅ PASS | 2/2 |

## cancel_order_004: Cancel an order

### Turn 1 ✅

**User Text:** I need to cancel my order right now. The delivery date keeps getting pushed back and I'm done waiting.

**User ASR:** i need to cancel my order right now. the delivery date keeps getting pushed back and i'm done waiting.

**Bot Text:** I understand your frustration with the delayed delivery. To help cancel your order right away, could you please provide your order number?

**Detected Intent:** Cancel an order ✅

**Audio Files:**
- User: [recordings/cancel_order_004/user_1.m4a](recordings/cancel_order_004/user_1.m4a)
- Bot: [out/audio/cancel_order_004/bot_1.wav](out/audio/cancel_order_004/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ✅

**User Text:** Order 58463. Just cancel it.

**User ASR:** order 5-8463, just cancel it.

**Bot Text:** I'll cancel order 5-8463 for you right away. Your order has been cancelled.

**Detected Intent:** Cancel an order ✅

**Audio Files:**
- User: [recordings/cancel_order_004/user_2.m4a](recordings/cancel_order_004/user_2.m4a)
- Bot: [out/audio/cancel_order_004/bot_2.wav](out/audio/cancel_order_004/bot_2.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## cancel_order_009: Cancel an order

### Turn 1 ✅

**User Text:** Um so I think I wanna cancel something I bought? I'm not even sure if it shipped yet or what.

**User ASR:** so i think i want to cancel something i bought, i'm not even sure if it shipped  yet or what.

**Bot Text:** I'd be happy to help you cancel your order. Could you please provide your order number?

**Detected Intent:** Cancel an order ✅

**Audio Files:**
- User: [recordings/cancel_order_009/user_1.m4a](recordings/cancel_order_009/user_1.m4a)
- Bot: [out/audio/cancel_order_009/bot_1.wav](out/audio/cancel_order_009/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ✅

**User Text:** I think it's uh... order 19548? Let me double check. Yeah, 19548.

**User ASR:** i think it's uh order 19548. let me double check. yeah, 19548.

**Bot Text:** Perfect! I'll cancel order 19548 for you right away.

**Detected Intent:** Cancel an order ✅

**Audio Files:**
- User: [recordings/cancel_order_009/user_2.m4a](recordings/cancel_order_009/user_2.m4a)
- Bot: [out/audio/cancel_order_009/bot_2.wav](out/audio/cancel_order_009/bot_2.wav)

**Expected:** {'contains_any': ['cancelled', 'canceled', 'cancellation confirmed', 'order has been cancelled']}

---

## change_address_006: Change shipping address

### Turn 1 ✅

**User Text:** This is so frustrating. I already called once and the address still wasn't changed. I need someone to actually update it this time.

**User ASR:** it's so frustrating. i already called once and the other still wasn't changed. i need someone to actually update at this time

**Bot Text:** I understand your frustration. I'd be happy to help update your shipping address right away. Could you please provide your order number?

**Detected Intent:** Change shipping address ✅

**Audio Files:**
- User: [recordings/change_address_006/user_1.m4a](recordings/change_address_006/user_1.m4a)
- Bot: [out/audio/change_address_006/bot_1.wav](out/audio/change_address_006/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ✅

**User Text:** Order 65739. And please make sure it actually goes through this time.

**User ASR:** order 6 5 7 3 9 and please make sure it actually goes through this time

**Bot Text:** Thank you for providing your order number 657339. I'll make sure your shipping address is updated right away. Please provide me with the new shipping address you'd like to use for this order.

**Detected Intent:** Change shipping address ✅

**Audio Files:**
- User: [recordings/change_address_006/user_2.m4a](recordings/change_address_006/user_2.m4a)
- Bot: [out/audio/change_address_006/bot_2.wav](out/audio/change_address_006/bot_2.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## change_address_009: Change shipping address

### Turn 1 ✅

**User Text:** So um I think my package might be going to the wrong place? Like I'm not sure if I put the right address in when I ordered.

**User ASR:** so, um, i think my package might be going to the raw place.  like, i'm not sure if i put the right address in when i ordered.

**Bot Text:** I can help you change the shipping address. Could you please provide your order number?

**Detected Intent:** Change shipping address ✅

**Audio Files:**
- User: [recordings/change_address_009/user_1.m4a](recordings/change_address_009/user_1.m4a)
- Bot: [out/audio/change_address_009/bot_1.wav](out/audio/change_address_009/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ✅

**User Text:** Oh right, uh... I think it was order 21456.

**User ASR:** oh, right. i think it was order 21-456.

**Bot Text:** Perfect! I can update the shipping address for order 21-456. What is the new address you'd like to use?

**Detected Intent:** Change shipping address ✅

**Audio Files:**
- User: [recordings/change_address_009/user_2.m4a](recordings/change_address_009/user_2.m4a)
- Bot: [out/audio/change_address_009/bot_2.wav](out/audio/change_address_009/bot_2.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

## check_status_005: Check order status

### Turn 1 ✅

**User Text:** I've been waiting for over a week for this package. This is unacceptable. Where is it?

**User ASR:** i've been waiting for over a week for this package. this is unacceptable. where is it?

**Bot Text:** I understand your frustration. To check on your package status, could you please provide your order number?

**Detected Intent:** Check order status ✅

**Audio Files:**
- User: [recordings/check_status_005/user_1.m4a](recordings/check_status_005/user_1.m4a)
- Bot: [out/audio/check_status_005/bot_1.wav](out/audio/check_status_005/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** It's 71845. Someone better tell me what's going on.

**User ASR:** it's 71845, someone better tell me what's going on.

**Bot Text:** I apologize for the wait. Unfortunately, I don't have access to the tracking details for order 71845 at this moment. Please contact our support team directly with your order number so they can provide you with the current status of your package.

**Detected Intent:** Check order status ✅

**Audio Files:**
- User: [recordings/check_status_005/user_2.m4a](recordings/check_status_005/user_2.m4a)
- Bot: [out/audio/check_status_005/bot_2.wav](out/audio/check_status_005/bot_2.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## check_status_010: Check order status

### Turn 1 ✅

**User Text:** I got an email about something shipping but I don't know which order it was. Can you look it up?

**User ASR:** i got an email about something shipping, but i don't know which order it was. can you look it up?

**Bot Text:** I'd be happy to help! Could you please provide your order number so I can look up the shipping status?

**Detected Intent:** Check order status ✅

**Audio Files:**
- User: [recordings/check_status_010/user_1.m4a](recordings/check_status_010/user_1.m4a)
- Bot: [out/audio/check_status_010/bot_1.wav](out/audio/check_status_010/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ✅

**User Text:** Hmm let me find it... order 88256 I think.

**User ASR:** hmm, let me find it. order 888256 i think.

**Bot Text:** I'll check the status of order 888256 for you right away.

**Detected Intent:** Check order status ✅

**Audio Files:**
- User: [recordings/check_status_010/user_2.m4a](recordings/check_status_010/user_2.m4a)
- Bot: [out/audio/check_status_010/bot_2.wav](out/audio/check_status_010/bot_2.wav)

**Expected:** {'contains_any': ['status', 'shipped', 'on its way', 'delivered', 'in transit', 'processing']}

---

## duplicate_charge_004: Request refund for duplicate charge

### Turn 1 ✅

**User Text:** I've been charged twice for the same order and this is completely unacceptable. I want my money back right now.

**User ASR:** i've been charged twice for the same order and this is completely unacceptable and what my money bag right now

**Bot Text:** I apologize for the duplicate charge. To process your refund, could you please provide the last four digits of the card that was charged?

**Detected Intent:** Request refund for duplicate charge ✅

**Audio Files:**
- User: [recordings/duplicate_charge_004/user_1.m4a](recordings/duplicate_charge_004/user_1.m4a)
- Bot: [out/audio/duplicate_charge_004/bot_1.wav](out/audio/duplicate_charge_004/bot_1.wav)

**Expected:** {'contains_any': ['last four digits', 'card', 'last four', 'card ending']}

---

### Turn 2 ✅

**User Text:** Card ending 9241. How long is this gonna take?

**User ASR:** card ending 9241. how long is this gonna take?

**Bot Text:** I'll process your refund right away for the duplicate charge on card ending 9241. You should see the credit back to your account within 3-5 business days.

**Detected Intent:** Request refund for duplicate charge ✅

**Audio Files:**
- User: [recordings/duplicate_charge_004/user_2.m4a](recordings/duplicate_charge_004/user_2.m4a)
- Bot: [out/audio/duplicate_charge_004/bot_2.wav](out/audio/duplicate_charge_004/bot_2.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## duplicate_charge_009: Request refund for duplicate charge

### Turn 1 ✅

**User Text:** I got charged for something? I don't know, it was on my credit card. It looks like it went through twice maybe?

**User ASR:** i got charged for something. i don't know. it was on my credit card. it looks like it went through twice maybe

**Bot Text:** I'm sorry you were charged twice. To help process your refund, could you please provide the last four digits of the card that was charged?

**Detected Intent:** Request refund for duplicate charge ✅

**Audio Files:**
- User: [recordings/duplicate_charge_009/user_1.m4a](recordings/duplicate_charge_009/user_1.m4a)
- Bot: [out/audio/duplicate_charge_009/bot_1.wav](out/audio/duplicate_charge_009/bot_1.wav)

**Expected:** {'contains_any': ['last four digits', 'card', 'last four', 'card ending']}

---

### Turn 2 ✅

**User Text:** Umm which card... oh the one ending in 1472.

**User ASR:** hmm, which card? oh, the one ending in 1472

**Bot Text:** Thank you. I'll process your refund right away for the duplicate charge on the card ending in 1472.

**Detected Intent:** Request refund for duplicate charge ✅

**Audio Files:**
- User: [recordings/duplicate_charge_009/user_2.m4a](recordings/duplicate_charge_009/user_2.m4a)
- Bot: [out/audio/duplicate_charge_009/bot_2.wav](out/audio/duplicate_charge_009/bot_2.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued', 'refund']}

---

## missing_package_004: Report a missing package

### Turn 1 ✅

**User Text:** Someone stole my package or your driver delivered it to the wrong house. Either way, I don't have it and I'm furious.

**User ASR:** someone stole my package or your driver delivered it to the wrong house. either way, i don't have it and i'm furious.

**Bot Text:** I understand how frustrating that is. To help you right away, could you please provide your order number?

**Detected Intent:** Report a missing package ✅

**Audio Files:**
- User: [recordings/missing_package_004/user_1.m4a](recordings/missing_package_004/user_1.m4a)
- Bot: [out/audio/missing_package_004/bot_1.wav](out/audio/missing_package_004/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ✅

**User Text:** Order 61934. I want this resolved today.

**User ASR:** order 61934. i want this result today.

**Bot Text:** I'm opening an investigation into your missing package for order 61934 right away. We'll look into this urgently and get back to you as soon as possible.

**Detected Intent:** Report a missing package ✅

**Audio Files:**
- User: [recordings/missing_package_004/user_2.m4a](recordings/missing_package_004/user_2.m4a)
- Bot: [out/audio/missing_package_004/bot_2.wav](out/audio/missing_package_004/bot_2.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## missing_package_009: Report a missing package

### Turn 1 ✅

**User Text:** Hey so uh, I was expecting something in the mail and it never showed up? I'm not really sure what happened to it.

**User ASR:** hey, so i was expecting something in the mail and never showed up. i'm not really sure what happened to it

**Bot Text:** I'm sorry to hear your package didn't arrive. To help you right away, could you please provide your order number?

**Detected Intent:** Report a missing package ✅

**Audio Files:**
- User: [recordings/missing_package_009/user_1.m4a](recordings/missing_package_009/user_1.m4a)
- Bot: [out/audio/missing_package_009/bot_1.wav](out/audio/missing_package_009/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ✅

**User Text:** Oh um, the order number... let me look. I think it's 16549.

**User ASR:** oh, um, the order number, let me look, i think it's 16549.

**Bot Text:** Thank you! I'm opening an investigation into order number 16549 right away to find out what happened to your missing package.

**Detected Intent:** Report a missing package ✅

**Audio Files:**
- User: [recordings/missing_package_009/user_2.m4a](recordings/missing_package_009/user_2.m4a)
- Bot: [out/audio/missing_package_009/bot_2.wav](out/audio/missing_package_009/bot_2.wav)

**Expected:** {'contains_any': ['investigation', 'looking into', 'investigate', 'opened a case', 'filed a report']}

---

## reset_password_005: Reset account password

### Turn 1 ✅

**User Text:** I've been locked out for two days and I need to place an order. Why is this so difficult?

**User ASR:** i've been locked up for two days and i need to place an order. why is this so difficult?

**Bot Text:** I'd be happy to help you reset your password so you can place your order. Could you please provide the email address associated with your account?

**Detected Intent:** Reset account password ✅

**Audio Files:**
- User: [recordings/reset_password_005/user_1.m4a](recordings/reset_password_005/user_1.m4a)
- Bot: [out/audio/reset_password_005/bot_1.wav](out/audio/reset_password_005/bot_1.wav)

**Expected:** {'contains_any': ['email', 'email address', 'email on file']}

---

### Turn 2 ✅

**User Text:** robert.james.finn@gmail.com. Please actually send it this time.

**User ASR:** robert dot james dot finn at gmail.com. please actually send it this time

**Bot Text:** I'll send a password reset link to robert.james.finn@gmail.com right away. Please check your email for the reset link.

**Detected Intent:** Reset account password ✅

**Audio Files:**
- User: [recordings/reset_password_005/user_2.m4a](recordings/reset_password_005/user_2.m4a)
- Bot: [out/audio/reset_password_005/bot_2.wav](out/audio/reset_password_005/bot_2.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## reset_password_009: Reset account password

### Turn 1 ✅

**User Text:** So uh, I can't get in. Like I'm typing my password and it keeps saying it's wrong. I don't know what to do.

**User ASR:** so i can't get in like i'm typing my password and keep saying it's wrong. i don't know what to do

**Bot Text:** I'd be happy to help you reset your password. Could you please provide the email address associated with your account?

**Detected Intent:** Reset account password ✅

**Audio Files:**
- User: [recordings/reset_password_009/user_1.m4a](recordings/reset_password_009/user_1.m4a)
- Bot: [out/audio/reset_password_009/bot_1.wav](out/audio/reset_password_009/bot_1.wav)

**Expected:** {'contains_any': ['email', 'email address', 'email on file']}

---

### Turn 2 ✅

**User Text:** Oh, my email? I think I used... tom.baker.99@gmail.com. Or wait, no. Yeah, that one.

**User ASR:** oh, my email. i think i'm used  tom.baker.99 at gmail.com or wait, no. wait, yeah, that's the one.

**Bot Text:** I'll send a password reset link to tom.baker.99@gmail.com right away. Please check your email for instructions to reset your password.

**Detected Intent:** Reset account password ✅

**Audio Files:**
- User: [recordings/reset_password_009/user_2.m4a](recordings/reset_password_009/user_2.m4a)
- Bot: [out/audio/reset_password_009/bot_2.wav](out/audio/reset_password_009/bot_2.wav)

**Expected:** {'contains_any': ['reset link', 'sent you a link', 'password reset', 'check your email']}

---

## return_damaged_006: Return a damaged item

### Turn 1 ✅

**User Text:** Look, I've been waiting on hold for twenty minutes. The blender I ordered arrived cracked and I need to return it now.

**User ASR:** look, i've been waiting on the hold for 20 minutes, the blender-eye ordered rive crack, and then you need to return it now.

**Bot Text:** I understand you need to return your blender. To help you right away, could you please provide your order number?

**Detected Intent:** Return a damaged item ✅

**Audio Files:**
- User: [recordings/return_damaged_006/user_1.m4a](recordings/return_damaged_006/user_1.m4a)
- Bot: [out/audio/return_damaged_006/bot_1.wav](out/audio/return_damaged_006/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'have your order', 'which order']}

---

### Turn 2 ✅

**User Text:** It's order 41087, come on.

**User ASR:** it's order 41087 come on.

**Bot Text:** I can help you return the damaged blender from order 41087. I'll process your return and send you a return label right away.

**Detected Intent:** Return a damaged item ✅

**Audio Files:**
- User: [recordings/return_damaged_006/user_2.m4a](recordings/return_damaged_006/user_2.m4a)
- Bot: [out/audio/return_damaged_006/bot_2.wav](out/audio/return_damaged_006/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## return_damaged_010: Return a damaged item

### Turn 1 ✅

**User Text:** So I ordered something a while back and it wasn't in good condition when it got here. I don't really know what to do about it.

**User ASR:** so i ordered something a while back and it wasn't in good condition when it got here. i don't really know what to do about it

**Bot Text:** I'm sorry to hear your item arrived damaged. I'd be happy to help you with a return. Could you please provide your order number?

**Detected Intent:** Return a damaged item ✅

**Audio Files:**
- User: [recordings/return_damaged_010/user_1.m4a](recordings/return_damaged_010/user_1.m4a)
- Bot: [out/audio/return_damaged_010/bot_1.wav](out/audio/return_damaged_010/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'have your order', 'which order']}

---

### Turn 2 ✅

**User Text:** Hmm I think the number was... hold on... 60473.

**User ASR:** hmm, i think the number was hold on 60473

**Bot Text:** Thank you! I'll process a return for order number 60473. We'll send you a return label so you can ship the damaged item back to us.

**Detected Intent:** Return a damaged item ✅

**Audio Files:**
- User: [recordings/return_damaged_010/user_2.m4a](recordings/return_damaged_010/user_2.m4a)
- Bot: [out/audio/return_damaged_010/bot_2.wav](out/audio/return_damaged_010/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label', 'return label']}

---

## upgrade_sub_004: Upgrade subscription plan

### Turn 1 ✅

**User Text:** I've been trying to upgrade on your website and it keeps crashing. Can you just do it for me? This is so annoying.

**User ASR:** i've been trying to upgrade on your website. it keeps crashing. can you just do it for me? this is so annoying.

**Bot Text:** I understand how frustrating that is. I can help you upgrade right away. Could you please provide your account number?

**Detected Intent:** Upgrade subscription plan ✅

**Audio Files:**
- User: [recordings/upgrade_sub_004/user_1.m4a](recordings/upgrade_sub_004/user_1.m4a)
- Bot: [out/audio/upgrade_sub_004/bot_1.wav](out/audio/upgrade_sub_004/bot_1.wav)

**Expected:** {'contains_any': ['account number', 'account', 'account details']}

---

### Turn 2 ✅

**User Text:** Account 69105. Just upgrade it already.

**User ASR:** i count 6905 just upgraded already.

**Bot Text:** Perfect! Your subscription has been upgraded to your new plan. Is there anything else I can help you with?

**Detected Intent:** Upgrade subscription plan ✅

**Audio Files:**
- User: [recordings/upgrade_sub_004/user_2.m4a](recordings/upgrade_sub_004/user_2.m4a)
- Bot: [out/audio/upgrade_sub_004/bot_2.wav](out/audio/upgrade_sub_004/bot_2.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

## upgrade_sub_009: Upgrade subscription plan

### Turn 1 ✅

**User Text:** So I think I wanna change my plan? Like get more features or whatever? I'm not sure what's available.

**User ASR:** so i think i want to change my plan like get more features or whatever. i'm not sure what's available

**Bot Text:** I'd be happy to help you upgrade your subscription plan. Could you please provide your account number so I can assist you?

**Detected Intent:** Upgrade subscription plan ✅

**Audio Files:**
- User: [recordings/upgrade_sub_009/user_1.m4a](recordings/upgrade_sub_009/user_1.m4a)
- Bot: [out/audio/upgrade_sub_009/bot_1.wav](out/audio/upgrade_sub_009/bot_1.wav)

**Expected:** {'contains_any': ['account number', 'account', 'account details']}

---

### Turn 2 ✅

**User Text:** Uh I think my account is... hold on... 18603? Yeah.

**User ASR:** uh, i think my account is hold on 18603.  yeah.

**Bot Text:** Perfect! I'm upgrading your subscription plan now. Your account 18603 has been updated to a higher tier with more features. Is there anything else I can help you with?

**Detected Intent:** Upgrade subscription plan ✅

**Audio Files:**
- User: [recordings/upgrade_sub_009/user_2.m4a](recordings/upgrade_sub_009/user_2.m4a)
- Bot: [out/audio/upgrade_sub_009/bot_2.wav](out/audio/upgrade_sub_009/bot_2.wav)

**Expected:** {'contains_any': ['upgraded', 'upgrade confirmed', 'subscription has been updated', 'new plan']}

---

