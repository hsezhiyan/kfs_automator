# KFS Data Entry Automation

**Overview**
I work for the UC Davis Shared Services Center. A lot of my work is incredibly boring, involving manual reading for invoices and inputtng the data into the the university payment data, Kuali (kfs.ucdavis.edu). This project automates the process of inputting FedEx invoice data entry. It takes a PDF of the invoice as input, extracts the appropriate text using Google Vision, and inputs the data using Selenium.

**Ongoing**
This is ongoing. Currently, I've been able to extract basic text like invoice/account#s, and check amount. The Selenium scripts puts the data into the form. Ongoing work involves attaching files on the form, and adding functionality for new forms.

**Technologies Used**
  - Google Vision API
  - Selenium
  - Kuali financial database system
  
 **How to use**
 To run this file:
 `python interact_kfs.py`
 
