import pywhatkit as pw

txt="""This is th tesxt that is being converted to handwriting"""

pw.text_to_handwriting(txt,"demo1.png",[0,0,138])
print("END___")