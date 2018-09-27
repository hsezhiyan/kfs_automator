import io
from google.cloud import vision


def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()
    previous_string = ''
    pprevious_string = ''
    po_box = ''
    total_amt = ''
    invoice_number = ''
    account_number = ''
    accounts_payable = []
    amounts_payable = []

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print('Texts:')

    for text in texts:
        if pprevious_string == 'Invoice' and previous_string == 'Number' and invoice_number == '':
            invoice_number = text.description

        if pprevious_string == 'Account' and previous_string == 'Number' and account_number == '':
            account_number = text.description

        if pprevious_string == 'P.O.' and previous_string == 'Box' and po_box == '':
            po_box = text.description

        if pprevious_string == 'USD' and previous_string == 'USD' and po_box == '':
            total_amt = text.description

       	if previous_string == 'CUSREF':
       		accounts_payable.append(text.description)

       	if pprevious_string == 'Account' and previous_string == 'Amount':
       		amounts_payable.append(text.description)

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
        pprevious_string = previous_string
        previous_string = text.description
    '''
    print("Invoice number: ", invoice_number)
    print("Account number: ", account_number)
    print("PO Box number: ", po_box)
    print("Total amount number: ", total_amt)
    print('Account payable: ', accounts_payable)
    print('Amount payable: ', amounts_payable)
    '''

    return invoice_number, account_number, po_box, total_amt, accounts_payable, amounts_payable

invoice_number, account_number, po_box, total_amt, accounts_payable, amounts_payable = detect_text('images/out.jpg')
