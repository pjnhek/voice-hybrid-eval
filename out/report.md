# Hybrid Voice Eval Report

## Summary

| Scenario | Result | Steps Passed |
|----------|--------|--------------|
| order_return_001 | ✅ PASS | 2/2 |
| billing_refund_001 | ✅ PASS | 2/2 |
| order_return_variations_001 | ✅ PASS | 2/2 |
| shipping_address_001 | ✅ PASS | 2/2 |

## order_return_001: Return a damaged item

### Turn 1 ✅

**User Text:** I need to return a broken blender.

**User ASR:** i need to return a broken blender.

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/order_return_001/user_1.wav](out/audio/order_return_001/user_1.wav)
- Bot: [out/audio/order_return_001/bot_1.wav](out/audio/order_return_001/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'have your order']}

---

### Turn 2 ✅

**User Text:** Order 12345

**User ASR:** order 12,345.

**Bot Text:** Thank you! I have initiated the return for order 12345. I've emailed you a return label and you should receive it shortly.

**Audio Files:**
- User: [out/audio/order_return_001/user_2.wav](out/audio/order_return_001/user_2.wav)
- Bot: [out/audio/order_return_001/bot_2.wav](out/audio/order_return_001/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label']}

---

## billing_refund_001: Request refund for duplicate charge

### Turn 1 ✅

**User Text:** I was charged twice for $45 last Friday.

**User ASR:** i was charged twice for $45 last friday.

**Bot Text:** I can help you with that. Could you please provide the last four digits of your card?

**Audio Files:**
- User: [out/audio/billing_refund_001/user_1.wav](out/audio/billing_refund_001/user_1.wav)
- Bot: [out/audio/billing_refund_001/bot_1.wav](out/audio/billing_refund_001/bot_1.wav)

**Expected:** {'contains_any': ['card', 'last four digits', 'help you with that']}

---

### Turn 2 ✅

**User Text:** Card ending 1234

**User ASR:** card ending 1,234.

**Bot Text:** Thank you! I have processed your refund for the duplicate charge ending in 1234. You should see the credit within 3-5 business days.

**Audio Files:**
- User: [out/audio/billing_refund_001/user_2.wav](out/audio/billing_refund_001/user_2.wav)
- Bot: [out/audio/billing_refund_001/bot_2.wav](out/audio/billing_refund_001/bot_2.wav)

**Expected:** {'contains_any': ['refund initiated', 'processed your refund', 'credit issued']}

---

## order_return_variations_001: Return a damaged item

### Turn 1 ✅

**User Text:** I need to send back this broken item

**User ASR:** i need to send back this broken item.

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/order_return_variations_001/user_1.wav](out/audio/order_return_variations_001/user_1.wav)
- Bot: [out/audio/order_return_variations_001/bot_1.wav](out/audio/order_return_variations_001/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #', 'which order']}

---

### Turn 2 ✅

**User Text:** My order number is 12345

**User ASR:** my order number is 12,345.

**Bot Text:** Thank you! I have initiated the return for order 12. I've emailed you a return label and you should receive it shortly.

**Audio Files:**
- User: [out/audio/order_return_variations_001/user_2.wav](out/audio/order_return_variations_001/user_2.wav)
- Bot: [out/audio/order_return_variations_001/bot_2.wav](out/audio/order_return_variations_001/bot_2.wav)

**Expected:** {'contains_any': ['initiated the return', 'return created', 'emailed you a label']}

---

## shipping_address_001: Change shipping address

### Turn 1 ✅

**User Text:** I need to update my shipping address.

**User ASR:** i need to update my shipping address.

**Bot Text:** I can help you with that. Could you please provide your order number?

**Audio Files:**
- User: [out/audio/shipping_address_001/user_1.wav](out/audio/shipping_address_001/user_1.wav)
- Bot: [out/audio/shipping_address_001/bot_1.wav](out/audio/shipping_address_001/bot_1.wav)

**Expected:** {'contains_any': ['order number', 'order #']}

---

### Turn 2 ✅

**User Text:** Order 98765

**User ASR:** order 98,765.

**Bot Text:** Thank you! I have updated your shipping address for order 98765. The change has been confirmed.

**Audio Files:**
- User: [out/audio/shipping_address_001/user_2.wav](out/audio/shipping_address_001/user_2.wav)
- Bot: [out/audio/shipping_address_001/bot_2.wav](out/audio/shipping_address_001/bot_2.wav)

**Expected:** {'contains_any': ['updated your address', 'address has been changed', 'change confirmed', 'shipping address']}

---

