text = "X-DSPAM-Confidence:    0.8475"
x = text.find('0.8475')
y= text[23:29]
z = float(y)
print(z)

