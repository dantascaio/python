import os

def main():
    ts = 1621859884500
    indicador_spoof = 'S'
    tela = 'MonitorHD'
    ambiente = 'Interno'
    aparelho = 'iPhone7'
    raiz = r'C:\Users\ccesa\Documents\Spoofs'
    barra = '\\'

    for file in os.listdir(raiz):
        ts_str = str(ts)
        atual = raiz + barra + file
        novo = raiz + barra + ts_str + '_' + indicador_spoof + '_' + tela + '_' + ambiente + '_' + aparelho + '.jpeg'
        os.rename(atual, novo)
        ts += 1

if __name__ == '__main__':
    main()