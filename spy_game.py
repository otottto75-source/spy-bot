import random
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Герої
DOTA_HEROES = {
    "Abaddon": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/abaddon.png",
    "Alchemist": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/alchemist.png",
    "Ancient Apparition": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/ancient_apparition.png",
    "Anti-Mage": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/antimage.png",
    "Axe": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/axe.png",
    "Bane": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/bane.png",
    "Bloodseeker": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/bloodseeker.png",
    "Bounty Hunter": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/bounty_hunter.png",
    "Bristleback": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/bristleback.png",
    "Clinkz": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/clinkz.png",
    "Crystal Maiden": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/crystal_maiden.png",
    "Dark Willow": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/dark_willow.png",
    "Dawnbreaker": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/dawnbreaker.png",
    "Dazzle": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/dazzle.png",
    "Doom": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/doom.png",
    "Drow Ranger": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/drow_ranger.png",
    "Earthshaker": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/earthshaker.png",
    "Ember Spirit": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/ember_spirit.png",
    "Enigma": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/enigma.png",
    "Faceless Void": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/faceless_void.png",
    "Hoodwink": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/hoodwink.png",
    "Huskar": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/huskar.png",
    "Invoker": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/invoker.png",
    "Io": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/wisp.png",
    "Juggernaut": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/juggernaut.png",
    "Kunkka": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/kunkka.png",
    "Legion Commander": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/legion_commander.png",
    "Lina": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/lina.png",
    "Lion": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/lion.png",
    "Marci": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/marci.png",
    "Mars": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/mars.png",
    "Mirana": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/mirana.png",
    "Monkey King": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/monkey_king.png",
    "Morphling": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/morphling.png",
    "Necrophos": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/necrolyte.png",
    "Ogre Magi": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/ogre_magi.png",
    "Phantom Assassin": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/phantom_assassin.png",
    "Primal Beast": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/primal_beast.png",
    "Puck": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/puck.png",
    "Pudge": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/pudge.png",
    "Queen of Pain": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/queenofpain.png",
    "Rubick": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/rubick.png",
    "Shadow Fiend": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/nevermore.png",
    "Slark": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/slark.png",
    "Sniper": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/sniper.png",
    "Sven": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/sven.png",
    "Techies": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/techies.png",
    "Tinker": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/tinker.png",
    "Ursa": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/ursa.png",
    "Wraith King": "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/skeleton_king.png"
}

game = {
    "total_players": 0,
    "current_player_index": 0,
    "spy_index": -1,
    "selected_hero": "",
    "hero_image": ""
}

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("3 гравці", callback_data="set_3"), InlineKeyboardButton("4 гравці", callback_data="set_4")],
        [InlineKeyboardButton("5 гравців", callback_data="set_5"), InlineKeyboardButton("6 гравців", callback_data="set_6")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "🕵️‍♂️ Вітаємо у грі 'Шпигун'!\n"
        "Передавайте телефон по колу, щоб дізнатися свою роль.\n\n"
        "Скільки людей буде грати?", 
        reply_markup=reply_markup
    )

def handle_buttons(update, context):
    query = update.callback_query
    query.answer()
    data = query.data

    if data.startswith("set_"):
        game["total_players"] = int(data.split("_")[1])
        game["current_player_index"] = 0
        game["spy_index"] = random.randint(0, game["total_players"] - 1)
        
        game["selected_hero"] = random.choice(list(DOTA_HEROES.keys()))
        game["hero_image"] = DOTA_HEROES[game["selected_hero"]]

        show_prepare_screen(query)

    elif data == "show_role":
        idx = game["current_player_index"]
        keyboard = [[InlineKeyboardButton("👌 Запам'ятав, сховати", callback_data="hide_role")]]
        
        if idx == game["spy_index"]:
            text = f"🤫 ГРАВЕЦЬ {idx + 1}\n\n🕵️‍♂️ ТИ ШПИГУН!"
            query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup(keyboard))
        else:
            text = f"<a href='{game['hero_image']}'>&#160;</a>🤫 ГРАВЕЦЬ {idx + 1}\n\n🦸‍♂️ Герой: <b>{game['selected_hero']}</b>"
            query.edit_message_text(text=text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "hide_role":
        game["current_player_index"] += 1
        
        if game["current_player_index"] >= game["total_players"]:
            query.edit_message_text(
                text="🎮 УСІ РОЛІ РОЗПОДІЛЕНО!\n\n"
                     "Поверніть телефон першому гравцю. "
                     "Запускайте таймер і починайте гру."
            )
        else:
            show_prepare_screen(query)

def show_prepare_screen(query):
    idx = game["current_player_index"]
    text = (
        f"📱 ПЕРЕДАЙТЕ ТЕЛЕФОН ГРАВЦЮ {idx + 1}!\n\n"
        f"Гравець {idx + 1}, коли візьмеш телефон, натисни кнопку нижче."
    )
    keyboard = [[InlineKeyboardButton(f"👀 Показати роль Гравця {idx + 1}", callback_data="show_role")]]
    query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup(keyboard))

def main():
    TOKEN = os.environ.get("BOT_TOKEN")

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(handle_buttons))

    print("Бот 'Шпигун' запущений...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()