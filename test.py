import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = 27573321
API_HASH = "ab789476abc75fb010bda8dbc484a237"

async def test_otp():
    # Buat client
    client = TelegramClient(StringSession(), API_ID, API_HASH)
    await client.connect()
    
    # Minta kode telepon
    phone = "+6283840151859"  # Ganti dengan nomor Anda
    result = await client.send_code_request(phone)
    print(f"Kode terkirim. Hash: {result.phone_code_hash}")
    
    # Tunggu input manual
    code = input("Masukkan kode yang Anda terima: ")
    
    # Coba sign in
    try:
        await client.sign_in(phone=phone, code=code, phone_code_hash=result.phone_code_hash)
        print("Berhasil! Anda sekarang sudah login.")
        me = await client.get_me()
        print(f"Info Anda: {me.first_name} {me.last_name} (@{me.username})")
    except Exception as e:
        print(f"Error saat login: {str(e)}")
    
    await client.disconnect()

asyncio.run(test_otp())
