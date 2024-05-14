from docxtpl import DocxTemplate

doc = DocxTemplate("/root/workspace/github.com/DominikHrdonka/Invoice_generator/INVOICE_template_RWS.docx")
invoice_list= [
    ["PCZHC183154","CAN_YHOAJM_158", 186.25],
    ["PCZHC183153","CAN_YHOAJM_158", 217.46],
    

    
]

doc.render(
    {
        "date":"14. 5. 2024",
        "invoice_list": invoice_list,
        "invoice_num":"2024-0015",
        "order_num": "RWS17"
    }
)

doc.save("new_invoice.docx")

