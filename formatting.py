def createExplanation(account_number, invoice_number):
	return('Account#: ' + account_number + ', Invoice#: ' + invoice_number)

def createStubNotes(account_number, invoice_number):
	return('Account#: ' + account_number + ' Invoice#: ' + invoice_number)

def createDescription(account_number):
	return('FEDEX ' + account_number)

def createOrgDocNum(invoice_number):
	stripped_num  = ''
	for c in invoice_number:
		if c != '-':
			stripped_num = stripped_num + c
	return(stripped_num)

def removeDollarSign(total_amt):
	return(total_amt[1:])
