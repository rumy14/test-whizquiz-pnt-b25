# Dashboard Overview & Menu Structure

## Available Menu Items:
1. **Dashboard** - Main dashboard page
2. **Users** - User management
3. **Categories** - Quiz categories
4. **Quizzes** - Quiz management
5. **Plans** - Subscription plans
6. **Subscriptions** - User subscriptions
7. **Cash Payments** - Payment management
8. **Transactions** - Transaction history
9. **Languages** - Language settings
10. **Currencies** - Currency settings
11. **Mails** - Email settings
12. **Settings** - System settings

## Menu Navigation:
- All menu items are in the left sidebar
- Each menu item is an anchor tag (`<a>`) with href pointing to `/admin/[section]`
- Dashboard displays successfully after login with user greeting

## Key Dashboard Elements:
- Dashboard Title: `.fi-header-heading`
- Menu Links: `a[href*='/admin/']`
- User Menu: Top right corner with sign-out option
- Language Switcher: Multiple language options available
- Sidebar: Toggleable left navigation

## Test Procedure:
1. Login with credentials (admin@gmail.com / 123456)
2. Dashboard loads with sidebar menu
3. Click any menu link to navigate to that section
4. Sections load with respective management pages
