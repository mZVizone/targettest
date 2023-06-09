import xml.etree.ElementTree as ET

tree = ET.parse(r'Cole o caminho do arquivo base_ex3.xml aqui. ')
root = tree.getroot()

faturamento_diario = []
for dia in root.findall('dia'):
    faturamento = dia.find('faturamento').text
    if faturamento:
        faturamento_diario.append(float(faturamento))

meta_mensal = 30000

menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)

print("Menor faturamento diário: R$ {:.2f}".format(menor_faturamento))
print("Maior faturamento diário: R$ {:.2f}".format(maior_faturamento))


dias_com_faturamento_acima_da_meta = sum(faturamento > meta_mensal for faturamento in faturamento_diario if faturamento > 0)

print("{} dias com faturamento diário acima da meta mensal (R$ {:.2f})".format(dias_com_faturamento_acima_da_meta, meta_mensal))
