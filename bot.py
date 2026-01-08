from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    ChatJoinRequestHandler,
    CallbackQueryHandler,
    ContextTypes
)

# ====== بيانات البوت ======
TOKEN = "8451629398:AAGcQ83YW3jtPywGo1t9fBRc2V56SGB5WoE"

# 👇 سيب السطر ده زي ما هو دلوقتي
GROUP_ID = None


# ====== القواعد المختصرة ======
RULES_SHORT = """
🎨 مرحبًا بك في نادي المصممين السري

بانضمامك أنت توافق على:
1️⃣ الاحترام الكامل – لا إساءة ولا تقليل.
2️⃣ ممنوع الدخول الخاص بدون إذن.
3️⃣ يمنع المحتوى المقرصن أو المخالف للحقوق.
4️⃣ النقاشات داخل (نقاش النادي).
5️⃣ الروابط والدعم داخل (دعم المصممين).

📌 مخالفة القواعد قد تؤدي للحذف أو الطرد.
"""


# ====== أول مرحلة: نطلع ID الجروب ======
async def get_group_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.chat_join_request.chat.id
    print("GROUP ID IS:", chat_id)

    await context.bot.send_message(
        chat_id=update.chat_join_request.from_user.id,
        text="⏳ جاري تجهيز الجروب، سيتم تفعيل الانضمام قريبًا."
    )


# ====== تشغيل البوت ======
app = ApplicationBuilder().token(TOKEN).build()

# مؤقتًا: بنستخدمه بس عشان نعرف ID الجروب
app.add_handler(ChatJoinRequestHandler(get_group_id))

app.run_polling()
