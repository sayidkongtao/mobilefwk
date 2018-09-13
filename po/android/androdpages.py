
from po.android.pages.accountdomainselectpage import AccountDomainsSelectPage
from po.android.pages.contactdetails import ContactDetails
from po.android.pages.contactlistpage import ContactListPage
from po.android.pages.emailcontentpage import EmailContentPage
from po.android.pages.emailhistorypage import EmailHistoryPage
from po.android.pages.loginpage import LoginPage
from po.android.pages.messagelistpage import MessageListPage
from po.android.pages.navigationpage import NavigationPage
from po.android.pages.selectcontactpage import SelectContactPage
from po.android.pages.writeemailpage import WriteEmailPage


class AndroidPages:
    def __init__(self, driver):
        self.accountdomainselectpage = AccountDomainsSelectPage(driver)
        self.contactdetailspage = ContactDetails(driver)
        self.contactlistpage = ContactListPage(driver)
        self.emailcontentpage = EmailContentPage(driver)
        self.emailhistorypage = EmailHistoryPage(driver)
        self.loginpage = LoginPage(driver)
        self.messagelistpage = MessageListPage(driver)
        self.navigationpage = NavigationPage(driver)
        self.selectcontactpage = SelectContactPage(driver)
        self.writeemailpage = WriteEmailPage(driver)

