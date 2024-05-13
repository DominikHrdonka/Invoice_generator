from docxtpl import DocxTemplate

doc = DocxTemplate("INVOICE_template_RWS.docx")


doc.render({})
doc.save("new_invoice.docx")

