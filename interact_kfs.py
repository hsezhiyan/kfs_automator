from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass

import data_collector
import formatting

driver = webdriver.Chrome('/Users/hsezhiyan/desktop/kfs/chromedriver/chromedriver')  # Optional argument, if not specified will search path.
driver.get("https://kfs.ucdavis.edu/kfs-prd/financialDisbursementVoucher.do?methodToCall=docHandler&command=initiate&docTypeName=DV#topOfForm")

loginPass = getpass.getpass("Enter your Kerberos credentials")

invoice_number, account_number, po_box, total_amt, accounts_payable, amounts_payable = data_collector.detect_text('images/out.jpg')


description = driver.find_element_by_xpath("//input[@name='document.documentHeader.documentDescription']")
description.send_keys(formatting.createDescription(account_number))

explanation = driver.find_element_by_xpath("//textarea[@name='document.documentHeader.explanation']")
explanation.send_keys(formatting.createExplanation(account_number, invoice_number))

doc_number = driver.find_element_by_xpath("//input[@name='document.documentHeader.organizationDocumentNumber']")
doc_number.send_keys(formatting.createOrgDocNum(invoice_number))

check_amt = driver.find_element_by_xpath("//input[@name='document.disbVchrCheckTotalAmount']")
check_amt.clear()
check_amt.send_keys(formatting.removeDollarSign(total_amt))

stub_notes = driver.find_element_by_xpath("//textarea[@name='document.disbVchrCheckStubText']")
stub_notes.send_keys(formatting.createStubNotes(account_number, invoice_number))
'''
driver.find_element_by_xpath('//*[@class="tinybutton"]').click()
'''
