from po.ios.pages.accountdomainselectpage import AccountDomainsSelectPage
from po.ios.pages.contactdetails import ContactDetails
from po.ios.pages.contactlistpage import ContactListPage
from po.ios.pages.emailcontentpage import EmailContentPage
from po.ios.pages.emailhistorypage import EmailHistoryPage
from po.ios.pages.loginpage import LoginPage
from po.ios.pages.messagelistpage import MessageListPage
from po.ios.pages.navigationpage import NavigationPage
from po.ios.pages.selectcontactpage import SelectContactPage
from po.ios.pages.writeemailpage import WriteEmailPage


class IOSPages:
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
