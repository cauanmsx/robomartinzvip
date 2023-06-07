import requests
import time
import telebot
import json

token = "6272964130:AAFDU-4_aCADWv8WeQOxwDPrw79uwu5UeVA"  # coloca o teu token do bot
chat_id = "-1001807277977"  # coloca o id do chat, para o bot colocar no grupo  -100 antes

bot = telebot.TeleBot(token)

bot.send_message(chat_id, text="Iniciando Atividades🤖🟠...")
time.sleep(3)
bot.send_message(chat_id, text="Fazendo Ajustes Necessários⚙️")
time.sleep(2)
bot.send_message(chat_id, text="ROBÔ LIGADO🤖🟢")


def enviar_status(wins, los, white):
    total = wins + los
    assertividade = wins / total * 100 if total > 0 else 0

    t4 = "🚦PLACAR ROBÔ MARTINZ (VIP💙)🚦"
    p2 = f"𝗔𝗰𝗲𝗿𝘁𝗼𝘀: {wins}✅"
    p3 = f"𝗘𝗿𝗿𝗼𝘀: {los}❌"
    p4 = f"𝗕𝗿𝗮𝗻𝗰𝗼𝘀: {white}⚪️"
    p5 = f"Assertividade🎯: {assertividade:.2f}%"

    bot.send_message(chat_id, text=f"{t4}\n\n{p2}\n{p3}\n{p4}\n\n{p5}")


analise_sinal = False
entrada = 0
max_gale = 2

resultado = []
check_resultado = []
acertos = 21
erros = 4
brancos = 1


def reset():
    global analise_sinal
    global entrada

    entrada = 0
    analise_sinal = False
    return


def martingale(color):
    global entrada
    entrada += 1

    if entrada <= max_gale:
        bot.send_message(chat_id, text=f"Fazendo GALE {entrada} 🥶")
    else:
        loss(color)
        reset()
    return


def api():
    global resultado
    api_url = 'https://blaze.com/api/roulette_games/recent'
    req = requests.get(api_url)
    a = json.loads(req.content)
    jogo = [x['roll'] for x in a]
    resultado = jogo
    return jogo


def win(color):
    global acertos
    acertos += 1
    bot.send_message(chat_id, text=f"Green no {color}🔥✅✅")
    bot.send_message(chat_id, text="Bateu a metinha, vaza do mercado!!!")
    enviar_status(acertos, erros, brancos)
    return


def loss(color):
    global erros
    erros += 1
    bot.send_message(chat_id, text=f"Loss no {color}😭❌")
    bot.send_message(chat_id, text="Não veio, mas vamos recuperar na próxima!!!")
    enviar_status(acertos, erros, brancos)
    return


def correcao(results, color):
    global brancos
    global acertos
    if results[0:1] == ['P'] and color == '⚫️':
        win(color)
        reset()
        return

    elif results[0:1] == ['V'] and color == '🔴':
        win(color)
        reset()
        return

    elif results[0:1] == ['B']:
        brancos += 1
        acertos += 1
        bot.send_message(chat_id, text=f"Green no ⚪️🔥🔥🔥✅")
        enviar_status(acertos, erros, brancos)
        reset()
        return

    elif results[0:1] == ['P'] and color == '🔴':
        martingale(color)
        return

    elif results[0:1] == ['V'] and color == '⚫️':
        martingale(color)
        return


def enviar_sinal(cor):
    bot.send_message(chat_id, text=f'''
🔔Entrada Confirmada🔔
Entrar no {cor}
Proteger no ⚪️
<a href="https://www.blaze.com/pt/games/double">🎲Jogar Agora</a>
<a href="https://t.me/c/1807277977/28047">🕐Melhor Horario para Apostar</a>
<a href="instagram.com/robomartinz">📱Instagram</a>''', parse_mode='HTML', disable_web_page_preview=True)
    return


numeros = []
cores = []
cor_sinal = None


def estrategy(resultad):
    global analise_sinal
    global cor_sinal
    global cores
    global numeros

    cores = []
    for x in resultad:
        if 1 <= x <= 7:
            color = 'V'
            cores.append(color)
        elif 8 <= x <= 14:
            color = 'P'
            cores.append(color)
        elif x >= 0:
            color = 'B'
            cores.append(color)
    print(cores)

    numeros = []
    for x in resultad:
        if x == 1:
            roll = '1'
            numeros.append(roll)
        if x == 2:
            roll = '2'
            numeros.append(roll)
        if x == 3:
            roll = '3'
            numeros.append(roll)
        if x == 4:
            roll = '4'
            numeros.append(roll)
        if x == 5:
            roll = '5'
            numeros.append(roll)
        if x == 6:
            roll = '6'
            numeros.append(roll)
        if x == 7:
            roll = '7'
            numeros.append(roll)
        if x == 8:
            roll = '8'
            numeros.append(roll)
        if x == 9:
            roll = '9'
            numeros.append(roll)
        if x == 10:
            roll = '10'
            numeros.append(roll)
        if x == 11:
            roll = '11'
            numeros.append(roll)
        if x == 12:
            roll = '12'
            numeros.append(roll)
        if x == 13:
            roll = '13'
            numeros.append(roll)
        if x == 14:
            roll = '14'
            numeros.append(roll)
        if x == 0:
            color = '0'
            numeros.append(color)
    print(numeros)

    if analise_sinal:
        correcao(cores, cor_sinal)
    if analise_sinal:
        correcao(numeros, cor_sinal)
    else:
        if numeros[0:1] == ['7']:
            cor_sinal = '⚫️'
            enviar_sinal(cor_sinal)
            analise_sinal = True
            print('sinal enviado')

        if numeros[0:1] == ['8']:
            cor_sinal = '⚫️'
            enviar_sinal(cor_sinal)
            analise_sinal = True
            print('sinal enviado')

        if numeros[0:1] == ['11']:
            cor_sinal = '⚫️'
            enviar_sinal(cor_sinal)
            analise_sinal = True
            print('sinal enviado')

        if numeros[0:1] == ['1']:
            cor_sinal = '🔴'
            enviar_sinal(cor_sinal)
            analise_sinal = True
            print('sinal enviado')

        if numeros[0:1] == ['4']:
            cor_sinal = '🔴'
            enviar_sinal(cor_sinal)
            analise_sinal = True
            print('sinal enviado')

        if numeros[0:1] == ['14']:
            cor_sinal = '🔴'
            enviar_sinal(cor_sinal)
            analise_sinal = True
            print('sinal enviado')


while True:
    api()
    if resultado != check_resultado:
        check_resultado = resultado
        # print(resultado)
        estrategy(resultado)
