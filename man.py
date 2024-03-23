from telethon import TelegramClient, events
import asyncio

api_id = 27808751
api_hash = '6822ceeefdd46e51f2b3705335be4f33'

client = TelegramClient('session_name', api_id, api_hash)

async def send_message_to_all_groups(message):
    """
    Tüm gruplara belirli bir mesajı iletir.
    """
    async for dialog in client.iter_dialogs():
        if dialog.is_group or dialog.is_channel:
            await client.send_message(dialog.id, message)
    print("Tüm gruplara mesaj iletildi.")

@client.on(events.NewMessage(pattern='.paylas', outgoing=True))
async def paylas(event):
    """
    '.paylas' komutu ile yanıtlanan bir mesajı tüm gruplara iletir.
    """
    replied_message = await event.get_reply_message()
    if replied_message:
        message = replied_message.text
        print("Yanıtlanan Mesaj:", message)
        await event.respond(f"Paylaşılan mesaj: {message}")
        await send_message_to_all_groups(message)
    else:
        await event.respond("Lütfen bir mesaj yanıtlayın.")

async def main():
    """
    Ana işlem döngüsünü başlatır.
    """
    await client.start()
    while True:
        await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
