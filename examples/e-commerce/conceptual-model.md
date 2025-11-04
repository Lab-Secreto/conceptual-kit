# Conceptual Model & Object Mapping

## E-Commerce Platform

Based on Johnson & Henderson's Conceptual Models Framework

---

## 1. Executive Summary

**Purpose:** Define the conceptual model users form when shopping and selling on an e-commerce platform.

Following Johnson & Henderson's principles, this document focuses on:

- **Objects:** Products, shopping cart, orders, reviews, sellers
- **Attributes:** Price, quantity, ratings, shipping info, availability
- **Actions:** Browsing, adding to cart, purchasing, reviewing, tracking
- **Relationships:** How products relate to carts, orders, and sellers
- **Mental Models:** E-commerce as "digital shopping mall" and "personal marketplace"

**Key Stakeholders:**

- Product Team
- UX/UI Design
- Engineering
- Business/Marketing
- Customer Support

---

## 2. Core Conceptual Model

### 2.1 The Central Metaphor

**"Your Digital Shopping Mall"**

Users think of the E-Commerce Platform as a virtual mall where they can:

- Browse stores and products like walking through aisles
- Pick up items and put them in their cart
- Check out and pay at the register
- Track their purchases on the way home
- Return items if they don't work out

### 2.2 Mental Model Hierarchy

```
E-Commerce Platform
├── Storefront (The Mall)
│   ├── Categories (Departments)
│   ├── Search (Directory)
│   └── Featured (Window Displays)
├── Shopping Cart (My Basket)
│   ├── Items (Things I'm Buying)
│   ├── Saved for Later (Wishlist)
│   └── Checkout (Register)
├── My Account (Personal Space)
│   ├── Orders (Purchase History)
│   ├── Addresses (Delivery Locations)
│   └── Payment Methods (Wallet)
└── Product Pages (Individual Stores)
    ├── Product Details (Item Info)
    ├── Reviews (Customer Opinions)
    └── Similar Items (Recommendations)
```

### 2.3 Key Conceptual Principles

1. **Browse Before Buy:** Users explore before committing
2. **Cart as Temporary:** Items in cart aren't purchased yet
3. **Trust Through Reviews:** Other buyers' opinions matter
4. **Visual Product Display:** Images show what you're getting
5. **Secure Checkout:** Payment feels safe and protected

---

## 3. Object Model

### 3.1 Primary Objects

#### PRODUCT (The Item for Sale)

**What users think it is:** "Something I might want to buy"

**Attributes visible to users:**

- Name/Title (what it is)
- Price (how much it costs)
- Images (what it looks like)
- Description (details about it)
- Rating (what others think)
- Availability (in stock/out of stock)
- Seller (who's selling it)
- Shipping info (delivery details)
- Variants (size, color, etc.)

**Actions users can perform:**

- View details
- Add to cart
- Add to wishlist
- Compare products
- Read reviews
- Share product
- Ask questions
- Report issue

**System attributes (hidden from users):**

- Product ID
- SKU
- Inventory count
- Cost basis
- Margin
- Category IDs

**User-visible structure:**

```
┌────────────────────────────────┐
│ [Product Image]                │
│                                │
│ Wireless Headphones            │
│ ⭐⭐⭐⭐☆ (4.2) 1,234 reviews  │
│                                │
│ $79.99  🚚 Free shipping      │
│                                │
│ • Noise cancelling             │
│ • 30hr battery                 │
│ • Available in 3 colors        │
│                                │
│ [Add to Cart] [♡ Wishlist]    │
└────────────────────────────────┘
```

---

#### SHOPPING CART (The Basket)

**What users think it is:** "Things I'm planning to buy"

**Attributes visible to users:**

- Items list (what's in the cart)
- Quantity (how many of each)
- Subtotal (items total)
- Shipping cost (delivery fee)
- Tax (government fees)
- Total (final price)

**Actions users can perform:**

- Add items
- Remove items
- Update quantity
- Apply coupon
- Proceed to checkout
- Save for later
- Clear cart

**System attributes (hidden from users):**

- Cart ID
- Session token
- Expiration time
- Abandoned cart flag

---

#### ORDER (The Purchase)

**What users think it is:** "Things I've bought"

**Attributes visible to users:**

- Order number (tracking reference)
- Items purchased (what I bought)
- Total paid (how much I spent)
- Order date (when I ordered)
- Status (where is it?)
- Shipping address (where it's going)
- Estimated delivery (when it arrives)

**Actions users can perform:**

- Track shipment
- View details
- Download invoice
- Request return
- Contact seller
- Review products
- Reorder items

**System attributes (hidden from users):**

- Order ID
- Payment transaction ID
- Fulfillment status
- Warehouse location

---

#### REVIEW (Customer Feedback)

**What users think it is:** "What other customers think"

**Attributes visible to users:**

- Rating (stars)
- Review text (written feedback)
- Reviewer name (who wrote it)
- Date (when posted)
- Verified purchase (did they buy it?)
- Helpful votes (useful feedback)

**Actions users can perform:**

- Write review
- Rate product
- Upload photos
- Mark helpful
- Report review

---

### 3.2 Object Types & Categories

#### PHYSICAL PRODUCT

**Mental model:** "Something that will be shipped to me"

---

#### DIGITAL PRODUCT

**Mental model:** "Something I download or access online"

---

#### SUBSCRIPTION PRODUCT

**Mental model:** "Something I pay for regularly"

---

### 3.3 Layout/Structure System

**Mental model:** "Grid of products I scroll through"

**Visual representation:**

```
[Category Nav] [Search Bar] [Cart (3)]

Featured Products
┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
│ [IMG]  │ │ [IMG]  │ │ [IMG]  │ │ [IMG]  │
│ Product│ │ Product│ │ Product│ │ Product│
│ $49.99 │ │ $79.99 │ │ $29.99 │ │ $99.99 │
│ ⭐⭐⭐⭐  │ │ ⭐⭐⭐⭐⭐ │ │ ⭐⭐⭐   │ │ ⭐⭐⭐⭐  │
└────────┘ └────────┘ └────────┘ └────────┘
```

---

## 4. Relationships & Rules

### 4.1 Object Relationships

```
User (1) ───── has ───────→ Shopping Cart (1)
Cart (1) ───── contains ───→ Items (0..n)
User (1) ───── places ─────→ Orders (0..n)
Order (1) ──── contains ───→ Products (1..n)
Product (1) ── sold by ────→ Seller (1)
Product (1) ── has ────────→ Reviews (0..n)
User (1) ───── writes ─────→ Reviews (0..n)
Product (1) ── belongs to ─→ Category (1..n)
```

### 4.2 Conceptual Rules (User's Understanding)

1. **Cart Isn't Final:** "Items in cart aren't purchased until checkout"
2. **Price Can Change:** "Prices may go up or down"
3. **Stock Isn't Reserved:** "In cart doesn't mean it's mine yet"
4. **Reviews Are Verified:** "Verified badge means they bought it"
5. **Shipping Costs Extra:** "Final price includes shipping and tax"
6. **Return Policy Exists:** "I can return if I don't like it"

### 4.3 System Constraints (Learned Through Use)

- Cart expires after 90 days of inactivity
- Maximum 999 quantity per item
- Minimum order: $10 (platform dependent)
- Reviews only from verified purchasers
- Return window: 30 days from delivery
- Images maximum: 10 per product

---

## 5. User Actions & Workflows

### 5.1 Primary Action Flows

#### Browsing Products (Discovery Flow)

**Mental model:** "Looking around for things I might want"

**Flow:**

1. Land on homepage → "What's available?"
2. Browse categories or search → "Find what I need"
3. Click product → "Tell me more"
4. View images/details → "Is this what I want?"
5. Check reviews → "What do others think?"
6. Decide: buy, save, or leave → "Make a decision"

**Objects involved:**

- Product catalog
- Categories
- Search
- Product pages
- Reviews

---

#### Adding to Cart (Selection Flow)

**Mental model:** "Putting items in my basket"

**Flow:**

1. Click "Add to Cart" → "I want this"
2. See confirmation → "It's in my cart"
3. Choose: continue shopping or checkout → "What's next?"

**Objects involved:**

- Product
- Shopping cart

---

#### Checkout (Purchase Flow)

**Mental model:** "Paying for what I've chosen"

**Flow:**

1. Review cart → "Is everything here?"
2. Enter shipping address → "Where should it go?"
3. Select shipping method → "How fast do I need it?"
4. Enter payment → "How am I paying?"
5. Review order → "Everything correct?"
6. Confirm purchase → "Make it official"
7. Receive confirmation → "It's done!"

**Objects involved:**

- Shopping cart
- Shipping address
- Payment method
- Order

---

#### Tracking Order (Fulfillment Flow)

**Mental model:** "Where is my stuff?"

**Flow:**

1. Open "My Orders" → "What have I bought?"
2. Click recent order → "Tell me about this one"
3. View tracking → "Where is it now?"
4. See estimated delivery → "When will it arrive?"

**Objects involved:**

- Order
- Tracking information
- Delivery status

---

#### Writing Review (Feedback Flow)

**Mental model:** "Sharing my experience"

**Flow:**

1. Receive product → "Got it, tried it"
2. Get review prompt → "What did I think?"
3. Rate with stars → "Overall impression"
4. Write review → "Detailed thoughts"
5. Upload photos (optional) → "Show what I got"
6. Submit → "Help others decide"

**Objects involved:**

- Order
- Product
- Review

---

## 6. Information Architecture

### 6.1 Conceptual Hierarchy (User's View)

```
My Shopping Experience
├── Browse & Discover
│   ├── Categories
│   ├── Search Results
│   ├── Featured/Deals
│   └── Recommendations
├── My Cart
│   ├── Items to Buy
│   ├── Saved for Later
│   └── Checkout
├── My Account
│   ├── Order History
│   ├── Track Shipments
│   ├── Addresses
│   ├── Payment Methods
│   └── Wishlist
└── Product Details
    ├── Images & Description
    ├── Pricing & Availability
    ├── Reviews & Ratings
    └── Similar Products
```

### 6.2 Visual Hierarchy Principles

- **Size = Importance:** Bigger images for featured products
- **Stars = Quality:** Rating immediately visible
- **Color = Action:** Primary button for "Add to Cart"
- **Badge = Status:** Special indicators for deals, new items
- **Position = Priority:** Best products shown first

---

## 7. State Model

### 7.1 Product States (User Perception)

```
┌─────────────┐
│ IN STOCK    │
│"Available"  │
└──────┬──────┘
       │
       ├──→ ┌─────────────┐
       │    │ LOW STOCK   │
       │    │"Almost gone"│
       │    └─────────────┘
       │
       └──→ ┌─────────────┐
            │ OUT OF STOCK│
            │"Can't buy"  │
            └─────────────┘
```

### 7.2 Order States (User Perception)

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  ORDERED    │ ──→│ PROCESSING  │ ──→│  SHIPPED    │
│"Confirmed"  │    │"Being       │    │"On the way" │
│             │    │ prepared"   │    │             │
└─────────────┘    └─────────────┘    └──────┬──────┘
                                              │
                                              ↓
                                       ┌─────────────┐
                                       │ DELIVERED   │
                                       │"Arrived"    │
                                       └─────────────┘
```

---

## 8. Error & Exception Handling

### 8.1 Conceptual Error Messages

| System Error | User Sees | User Thinks |
|-------------|-----------|-------------|
| Out of stock | "This item is currently unavailable" | "I can't buy it right now" |
| Payment failed | "Payment could not be processed" | "My card was declined" |
| Address invalid | "Please check your shipping address" | "I typed it wrong" |
| Coupon expired | "This coupon is no longer valid" | "I missed the deadline" |
| Cart item removed | "This item is no longer available" | "It sold out before I bought it" |

### 8.2 Graceful Degradation

When services fail, the conceptual model remains intact:

- Payment gateway down → Show alternative payment methods
- Image server down → Show placeholder with product name
- Review service down → Hide review section, show rating only
- Inventory system down → Show "Call to confirm availability"

---

## 9. Metaphorical Consistency

### 9.1 Metaphors Throughout

| System Concept | Metaphor | User Language |
|---------------|----------|---------------|
| Product catalog | "Store shelves" | "Browse products" |
| Shopping cart | "Shopping basket" | "My cart" |
| Checkout | "Cash register" | "Pay for items" |
| Order history | "Purchase receipts" | "My orders" |
| Wishlist | "Window shopping" | "Saved for later" |
| Reviews | "Word of mouth" | "What others say" |

### 9.2 Language & Terminology

**Use ✅**

- Cart, basket
- Checkout, pay
- Shipping, delivery
- Order, purchase
- Review, rating
- In stock, available

**Avoid ❌**

- SKU, inventory ID
- Transaction, payment gateway
- Database record
- API endpoint
- Session, token

---

## 10. Progressive Disclosure Model

### 10.1 Complexity Layers

**Layer 1: Novice (First Purchase)**

- **Sees:** Product grid, basic search, simple cart
- **Thinks:** "It's like online shopping"
- **Can do:** Browse, add to cart, checkout

**Layer 2: Regular (Multiple Purchases)**

- **Sees:** Saved addresses, order history, wishlists
- **Thinks:** "My personal shopping account"
- **Can do:** Quick reorder, track shipments, save preferences

**Layer 3: Power User (Frequent Shopper)**

- **Sees:** Price tracking, deal alerts, subscription management
- **Thinks:** "My smart shopping assistant"
- **Can do:** Compare prices, manage subscriptions, bulk ordering

---

## 11. Platform-Specific Adaptations

### 11.1 Mental Model Shifts

- **Desktop:** "Full catalog browsing - research and compare"
- **Mobile:** "Quick purchase on the go - impulse buying"
- **Tablet:** "Couch shopping - relaxed browsing"

### 11.2 Interaction Patterns

| Gesture/Input | Desktop Action | Mobile Action | User Expects |
|--------------|---------------|---------------|--------------|
| Click/Tap | View product | View product | "See details" |
| Hover | Show quick view | - | "Preview" |
| Scroll | Browse products | Browse products | "See more" |
| Pinch | - | Zoom image | "Closer look" |
| Swipe | - | Next image | "More photos" |

---

## 12. Design Principles from Model

### 12.1 Core Principles

1. **Trust First:** Show reviews, verified badges, secure payment
2. **Visual Shopping:** High-quality images are essential
3. **Easy Discovery:** Search and categories make finding easy
4. **Frictionless Checkout:** Minimize steps to purchase
5. **Clear Pricing:** No surprise costs at checkout
6. **Post-Purchase Care:** Easy tracking and returns

### 12.2 Key Design Decisions

- **Grid layout for products:** Mimics physical store shelves
- **Persistent cart icon:** Always visible shopping status
- **Star ratings prominent:** Trust signal
- **One-click add to cart:** Reduce friction
- **Progress indicator at checkout:** Show steps remaining
- **Order confirmation email:** Proof of purchase

---

## 13. Implementation Notes for Designers

### 13.1 Visual Cues for Object Types

- **Featured products:** Larger images, "Featured" badge
- **Sale items:** Red price, "Sale" badge, crossed-out original price
- **Low stock:** Yellow "Only 3 left" warning
- **Out of stock:** Grayed out, "Notify me" button
- **New arrivals:** "New" badge, slight animation

### 13.2 Maintaining Conceptual Integrity

Critical rules to never break:

- Cart always accessible from any page
- Price always visible on product cards
- Reviews always show verified purchase badge
- Checkout progress always visible
- Order status always trackable

---

## 14. Validation & Testing

### 14.1 Conceptual Model Validation Tests

1. **Product discovery:** Can users find products within 3 clicks?
2. **Add to cart:** Can users add items without confusion?
3. **Checkout flow:** Can users complete purchase without errors?
4. **Order tracking:** Can users find their order status easily?
5. **Return process:** Do users understand how to return items?

### 14.2 Success Metrics

- Add to cart rate > 15%
- Cart abandonment < 70%
- Checkout completion > 60%
- Order tracking usage > 80%
- Review submission rate > 5% of orders

---

## Summary

**Core Metaphor:** E-Commerce is a digital shopping mall where users browse, select, purchase, and receive products.

**Key Principles:**

- Visual product presentation
- Trust through reviews and verification
- Simple, clear checkout process
- Transparent pricing
- Easy post-purchase support

**Critical Success Factors:**

- Users can find what they want
- Adding to cart is obvious
- Checkout is quick and secure
- Order tracking is transparent
- Returns are straightforward

---

## Appendices

### A. Glossary of Terms

- **Cart:** Collection of items user intends to purchase
- **Checkout:** Process of finalizing a purchase
- **Order:** Completed purchase transaction
- **SKU:** Stock Keeping Unit (internal product identifier)
- **Review:** Customer feedback on a product
- **Wishlist:** Saved products for future consideration

### B. Related Documents

- Payment Gateway Integration Specs
- Shipping Partner APIs
- Product Catalog Schema
- Review Moderation Guidelines

### C. Version History

- v1.0 - Initial e-commerce conceptual model

---

*This conceptual model captures how users think about shopping online, focusing on familiar metaphors that make e-commerce intuitive.*
