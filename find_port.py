import serial
import time

# Test edilecek portlar
test_ports = ['COM3', 'COM4', 'COM5', 'COM6', 'COM8', 'COM9']

print("🔍 Aktif Bluetooth portunu arıyorum...\n")

for port in test_ports:
    try:
        print(f"📡 {port} deneniyor...", end=" ")
        ser = serial.Serial(port, 9600, timeout=2)
        time.sleep(1)

        # Port açılabildi mi?
        if ser.is_open:
            print("✅ AÇILDI!")

            # Veri göndermeyi dene
            ser.write(b"<100>")
            time.sleep(0.5)

            # Yanıt var mı?
            if ser.in_waiting > 0:
                print(f"   📩 Veri alındı: Arduino'ya bağlı!")
            else:
                print(f"   📭 Veri yok ama port çalışıyor")

            ser.close()
        else:
            print("❌ Port açılamadı")

    except serial.SerialException as e:
        if "PermissionError" in str(e):
            print("🔒 MEŞGUL (Başka program kullanıyor)")
        elif "could not open port" in str(e):
            print("❌ KULLANILAMAZ (Hayalet port)")
        else:
            print(f"❌ Hata: {e}")
    except Exception as e:
        print(f"❌ Beklenmeyen hata: {e}")

print("\n✅ Test tamamlandı!")