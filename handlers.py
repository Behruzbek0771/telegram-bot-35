from telegram import Update
from telegram.ext import CallbackContext

def handle_photo(update: Update, context: CallbackContext):
    photo = update.message.photo[-1]
    update.message.reply_photo(
        photo=photo,
        caption="Siz yuborgan rasm"
    )

def handle_video(update: Update, context: CallbackContext):
    video = update.message.video
    update.message.reply_video(
        video=video,
        caption="Siz yuborgan video"
    )

def handle_audio(update: Update, context: CallbackContext):
    audio = update.message.audio
    update.message.reply_audio(
        audio=audio,
        caption="Siz yuborgan audio"
    )

def handle_voice(update: Update, context: CallbackContext):
    voice = update.message.voice
    update.message.reply_voice(
        voice=voice,
        caption="Siz yuborgan ovozli xabar"
    )

def handle_video_note(update: Update, context: CallbackContext):
    video_note = update.message.video_note
    update.message.reply_video_note(
        video_note=video_note
    )

def handle_document(update: Update, context: CallbackContext):
    document = update.message.document
    update.message.reply_document(
        document=document,
        caption="Siz yuborgan hujjat"
    )

def handle_location(update: Update, context: CallbackContext):
    location = update.message.location
    update.message.reply_location(
        latitude=location.latitude,
        longitude=location.longitude
    )

def handle_contact(update: Update, context: CallbackContext):
    contact = update.message.contact
    update.message.reply_contact(
        first_name=contact.first_name,
        phone_number=contact.phone_number
    )

def handle_dice(update: Update, context: CallbackContext):
    dice = update.message.dice
    update.message.reply_dice(
        emoji=dice.emoji
    )

def handle_animation(update: Update, context: CallbackContext):
    animation = update.message.animation
    update.message.reply_animation(
        animation=animation,
        caption="Siz yuborgan gif"
    )

def handle_sticker(update: Update, context: CallbackContext):
    sticker = update.message.sticker
    update.message.reply_sticker(
        sticker=sticker.file_id
    )

def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    update.message.reply_text(
        f"Assalomu alaykum {user.full_name}! Botimizga xush kelibsiz.\n"
        "Siz nima yuborsangiz, men shuni qaytaraman "
    )

def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Menga rasm, video, audio, kontakt, joylashuv, hujjat, gif, stiker, video xabar va boshqa fayllarni yuboring — men ularni sizga qaytaraman."
    )

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

