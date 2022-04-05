# Nome : form.py
# Desenvolvedor : Marco Aurélio
# Data : 05-04-2022

from tkinter import *
from cep import BuscaCEP

formu = Tk()
# width padrão
wid = 25
# variaveis das informações

rcep = StringVar()
rlogr = StringVar()
rcomp = StringVar()
rbairro = StringVar()
rlocal = StringVar()
ruf = StringVar()
ribge = StringVar()
rgia = StringVar()
rddd = StringVar()
rsiafi = StringVar()

# metodo de busca
def Pegar(dados):
    dc = BuscaCEP(dados)
    dc.Buscar()
    rcep.set(dc.get_cep())
    rlogr.set(dc.get_logradouro())
    rcomp.set(dc.get_complemento())
    rbairro.set(dc.get_bairro())
    rlocal.set(dc.get_localidade())
    ruf.set(dc.get_uf())
    ribge.set(dc.get_ibge())
    rgia.set(dc.get_gia())
    rddd.set(dc.get_ddd())
    rsiafi.set(dc.get_siafi())
    
# Criando formulario
formu.title("Buscar CEP")
formu.geometry("250x300+250+250")
formu.resizable(False, False)

# Criando elementos de tela

lc = Label(formu, text="CEP" , width=5, pady=2, padx=2)
tc =Entry(formu, width=10)

b1 = Button(formu, text="Procurar", command=lambda: Pegar(tc.get()))
lres = Label(formu, text="Resultado")

Lcep = Label(formu, text="CEP", width=5)
lt = Entry(formu, textvariable=rcep, width=10)

Llog = Label(formu, text="Logradouro")
Tc = Entry(formu, width=wid ,textvariable=rlogr)

Lcomp = Label(formu, text="Complemento")
Tcomp = Entry(formu, width=wid , textvariable=rcomp)

Lbairro = Label(formu, text="Bairro")
Tbairro = Entry(formu, width=wid , textvariable=rbairro)

Llocal = Label(formu, text="Localidade")
Tlocal = Entry(formu, width=wid ,textvariable=rlocal)

Luf = Label(formu, text="UF")
Tuf = Entry(formu, width=wid ,textvariable=ruf)

Libge = Label(formu, text="IBGE")
Tibge = Entry(formu, width=wid ,textvariable=ribge)

Lgia = Label(formu, text="Gia")
Tgia = Entry(formu, width=wid ,textvariable=rgia)

Lddd = Label(formu, text="DDD")
Tddd = Entry(formu, width=wid ,textvariable=rddd)

Lsiafi = Label(formu, text="Siafi")
Tsiafi = Entry(formu, width=wid ,textvariable=rsiafi)

# Inserindo eles no grid

# Campo Label e Entry de entrada e botao
lc.grid(row=0)
tc.grid(row=0, column=1)
b1.grid(row=1, sticky=E)

# Label("Resultado")
lres.grid(row=2)

# Label e Entry de saída de dados CEP
Lcep.grid(row=3)
lt.grid(row=3, column=1)

# Label e Entry de saída de dados Logradouro
Llog.grid(row=4)
Tc.grid(row=4, column=1)

# Label e Entry de saída de dados Complemento
Lcomp.grid(row=5)
Tcomp.grid(row=5, column=1)

# Label e Entry de saída de dados Bairro
Lbairro.grid(row=6)
Tbairro.grid(row=6, column=1)

# Label e Entry de saída de dados Localidade
Llocal.grid(row=7)
Tlocal.grid(row=7, column=1)

# Label e Entry de saída de dados UF
Luf.grid(row=8)
Tuf.grid(row=8, column=1)

# Label e Entry de saída de dados IBGE
Libge.grid(row=9)
Tibge.grid(row=9, column=1)

# Label e Entry de saída de dados Gia
Lgia.grid(row=10)
Tgia.grid(row=10, column=1)

# Label e Entry de saída de dados DDD
Lddd.grid(row=11)
Tddd.grid(row=11, column=1)

# Label e Entry de saída de dados Siafi
Lsiafi.grid(row=12)
Tsiafi.grid(row=12, column=1)

formu.mainloop()