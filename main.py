from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import TOKEN

from handlers import (start, help, echo , handle_photo, handle_contact,
                    handle_video, handle_dice, handle_audio,handle_voice,
                    handle_animation, handle_document, handle_location,
                    handle_sticker, handle_video_note)

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # command handler
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))

    # message handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dispatcher.add_handler(MessageHandler(Filters.contact, handle_contact))
    dispatcher.add_handler(MessageHandler(Filters.photo, handle_photo))
    dispatcher.add_handler(MessageHandler(Filters.video, handle_video))
    dispatcher.add_handler(MessageHandler(Filters.dice, handle_dice))
    dispatcher.add_handler(MessageHandler(Filters.audio, handle_audio))
    dispatcher.add_handler(MessageHandler(Filters.voice, handle_voice))
    dispatcher.add_handler(MessageHandler(Filters.document, handle_document))
    dispatcher.add_handler(MessageHandler(Filters.location, handle_location))
    dispatcher.add_handler(MessageHandler(Filters.animation, handle_animation))
    dispatcher.add_handler(MessageHandler(Filters.sticker, handle_sticker))
    dispatcher.add_handler(MessageHandler(Filters.video_note, handle_video_note))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
