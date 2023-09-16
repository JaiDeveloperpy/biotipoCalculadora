def menu():
    print('{:=^46}'.format(' MENU '))
    print('{:-^46}'.format('[1] CALCULAR IMC'))
    print('{:-^46}'.format(' [2] ENCERRAR '))
    print('=' * 46)
def ecto():
    print('{:=^46}'.format(' TREINO ECTOMORFO '))
    print('{:-^46}'.format(' Treino com peso '))
    print('{:-^46}'.format(' Consumir mais calorias '))
    print('{:-^46}'.format(' Evitar excesso de exercícios aeróbicos '))
    print('{:-^46}'.format(' Consumir mais calorias '))
    print('='*46)
def meso():
    print('{:=^46}'.format(' TREINO MESOMORFO '))
    print('{:-^46}'.format(' Treino de força e aeróbico '))
    print('{:-^46}'.format('Dieta equilibrada '))
    print('{:-^46}'.format(' Calorias equilibradas '))
    print('{:-^46}'.format(' Falha concêntrica é fundamental '))
    print('='*46)
def endo():
    print('{:=^46}'.format(' TREINO ENDOMORFO '))
    print('{:-^46}'.format(' Foco em exercícios aeróbicos '))
    print('{:-^46}'.format('Déficit calórico '))
    print('{:-^46}'.format(' Dieta equilibrada '))
    print('{:-^46}'.format(' Treino de força para construção muscular '))
    print('='*46)
def fim():
    print('-='*23)
    print('{:-^46}'.format(' OBRIGADO POR USAR O PROGAMA! '))
    print('{:-^46}'.format(' Queremos deixar claro que '))
    print('{:-^46}'.format(' A relação entre IMC e biotipo corporal '))
    print('{:-^46}'.format(' não é absoluta, variando entre '))
    print('{:-^46}'.format(' indivíduos, genética, estilo de vida e '))
    print('{:-^46}'.format(' composição corporal '))
    print('{:-^46}'.format(' também afetam essa relação. '))
    print('-='*23)
'''DEFINIDO FUNÇÕES'''

menu()
r = int(input(' '))
if r == 1:
    rr = 'S'
while rr == 'S':
    print('{:=^46}'.format(' CALCULO IMC '))
    i = input('Qual a sua idade? ')
    kg = float(input('Quanto Voçê Pesa (Kg)? '))
    m = float(input('Qual a sua altura (M)? '))
    imc = kg / (m**2)
    print('Seu IMC é {:.1f}'.format(imc))
    print('=' * 46)
    if imc < 18.5:
        tipo = 1 #ecto abaixo
    elif 18.5 <= imc < 25:
        tipo = 2 #meso ideal
    elif 25 <= imc < 30:
        tipo = 3 #endo sobrepeso
    elif 30 <= imc < 40:
        tipo = 4 #endo obesidade
    elif imc > 40:
        tipo = 5 #endo obesidade morbida
    match tipo:
        case 1:
            print('{:-^46}'.format(' Você está abaixo do peso ideal '))
            print('{:-^46}'.format(' Aqui estão algumas dicas para você '))
            print('=' * 46)
            print(' ')
            ecto()
        case 2:
            print('{:-^46}'.format(' Você está com o peso ideal '))
            print('{:-^46}'.format(' Aqui estão algumas dicas para você '))
            print('=' * 46)
            print(' ')
            meso()
        case 3:
            print('{:-^46}'.format(' Você está acima do peso ideal '))
            print('{:-^46}'.format(' Aqui estão algumas dicas para você '))
            print('=' * 46)
            print(' ')
            endo()
        case 4:
            print('{:-^46}'.format(' Você está muito acima peso ideal '))
            print('{:-^46}'.format(' Aqui estão algumas dicas para você '))
            print('=' * 46)
            print(' ')
            endo()
        case 5:
            print('{:-^46}'.format(' Você está em obesidade mórbida '))
            print('{:-^46}'.format(' Procure um médico! '))
            print('=' * 46)
    rr = input(('quer continuar [S/N]')).upper()
fim()