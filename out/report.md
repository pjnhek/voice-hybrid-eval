# Hybrid Voice Eval Report

## Summary

| Scenario | Result | Steps Passed |
|----------|--------|--------------|
| billing_refund_001 | ❌ FAIL | 1/2 |
| order_return_001 | ❌ FAIL | 1/2 |
| order_return_variations_001 | ❌ FAIL | 1/2 |
| shipping_address_001 | ❌ FAIL | 1/2 |

## billing_refund_001: Request refund for duplicate charge

### Turn 1 ✅

**User Text:** I was charged twice for $45 last Friday.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/billing_refund_001/user_1.wav](out/audio/billing_refund_001/user_1.wav)
- Bot: [out/audio/billing_refund_001/bot_1.wav](out/audio/billing_refund_001/bot_1.wav)

**Expected:** {'contains_any': ['card', 'last four digits', 'help you with that']}

---

### Turn 2 ❌

**User Text:** Card ending 1234

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/billing_refund_001/user_2.wav](out/audio/billing_refund_001/user_2.wav)
- Bot: [out/audio/billing_refund_001/bot_2.wav](out/audio/billing_refund_001/bot_2.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued']}

---

## order_return_001: Return a damaged item

### Turn 1 ✅

**User Text:** I need to return a broken blender.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/order_return_001/user_1.wav](out/audio/order_return_001/user_1.wav)
- Bot: [out/audio/order_return_001/bot_1.wav](out/audio/order_return_001/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'have your order']}

---

### Turn 2 ❌

**User Text:** Order 12345

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/order_return_001/user_2.wav](out/audio/order_return_001/user_2.wav)
- Bot: [out/audio/order_return_001/bot_2.wav](out/audio/order_return_001/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label']}

---

## order_return_variations_001: Return a damaged item

### Turn 1 ✅

**User Text:** I need to send back this broken item

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/order_return_variations_001/user_1.wav](out/audio/order_return_variations_001/user_1.wav)
- Bot: [out/audio/order_return_variations_001/bot_1.wav](out/audio/order_return_variations_001/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ❌

**User Text:** My order number is 12345

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/order_return_variations_001/user_2.wav](out/audio/order_return_variations_001/user_2.wav)
- Bot: [out/audio/order_return_variations_001/bot_2.wav](out/audio/order_return_variations_001/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label']}

---

## shipping_address_001: Change shipping address

### Turn 1 ✅

**User Text:** I need to update my shipping address.

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/shipping_address_001/user_1.wav](out/audio/shipping_address_001/user_1.wav)
- Bot: [out/audio/shipping_address_001/bot_1.wav](out/audio/shipping_address_001/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #']}

---

### Turn 2 ❌

**User Text:** Order 98765

**User ASR:** 

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/shipping_address_001/user_2.wav](out/audio/shipping_address_001/user_2.wav)
- Bot: [out/audio/shipping_address_001/bot_2.wav](out/audio/shipping_address_001/bot_2.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

