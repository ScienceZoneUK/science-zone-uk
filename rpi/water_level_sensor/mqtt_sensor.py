# === Pico W/W2 Water Level -> Adafruit IO (MQTT) + LED Toggle ===
import time, ssl, wifi, socketpool, board, digitalio, analogio
import adafruit_minimqtt.adafruit_minimqtt as MQTT
from adafruit_io.adafruit_io import IO_MQTT

# ---------- CONFIG ----------
AIO_USERNAME = "YOUR_USERNAME"
AIO_KEY      = "YOUR_AIO_KEY"   # (regenerate if you’ve shared it)
WIFI_SSID    = "YOUR_WIFI"
WIFI_PASS    = "YOUR_PASSWORD"

FEED_PUBLISH = "water-level"     # where level in cm will be published
FEED_TOGGLE  = "toggle-led"      # dashboard Toggle feed for LED control
PUBLISH_EVERY_SECONDS = 5
# ---------------------------

# --- LED setup ---
led = digitalio.DigitalInOut(board.LED)
led.switch_to_output(value=False)  # start OFF

# --- Sensor setup (GP26 == ADC0) ---
water_sensor = analogio.AnalogIn(board.GP26)

# --- Calibration (measure these on your setup) ---
RAW_EMPTY = 12000   # ADC value when empty
RAW_FULL  = 52000   # ADC value when full
TANK_DEPTH_CM = 20  # tank height

# --- Mapping helpers ---
def map_value(value, start1, stop1, start2, stop2):
    """Remap value from [start1, stop1] to [start2, stop2]."""
    return ((value - start1) * (stop2 - start2) / (stop1 - start1)) + start2

def adc_to_level(raw):
    # Clamp within expected range to avoid negative/overshoot
    raw = max(min(raw, RAW_FULL), RAW_EMPTY)
    return map_value(raw, RAW_EMPTY, RAW_FULL, 0, TANK_DEPTH_CM)

# --- Wi-Fi ---
print("Connecting to Wi-Fi…")
wifi.radio.connect(WIFI_SSID, WIFI_PASS)
print("IP:", wifi.radio.ipv4_address)

# --- MQTT (TLS/SSL on 8883) ---
pool = socketpool.SocketPool(wifi.radio)
mqtt = MQTT.MQTT(
    broker="io.adafruit.com",
    username=AIO_USERNAME,
    password=AIO_KEY,
    socket_pool=pool,
    ssl_context=ssl.create_default_context(),
)
io = IO_MQTT(mqtt)

# IO_MQTT delivers the topic to the callback as the *feed key* (e.g. "toggle-led")
def handle_connect(client):
    print("Connected to Adafruit IO")
    print("Subscribing to:", FEED_TOGGLE)
    io.subscribe(FEED_TOGGLE)

def handle_message(client, topic, payload):
    text = str(payload).strip().lower()
    print(f"[MSG] {topic} -> '{text}'")
    if topic == FEED_TOGGLE:
        led.value = text in ("on", "1", "true", "high")
        print("LED =>", "ON" if led.value else "OFF")

io.on_connect = handle_connect
io.on_message = handle_message

io.connect()

# --- Main loop: publish level + process MQTT ---
last_pub = 0
while True:
    io.loop()  # process incoming MQTT messages

    now = time.monotonic()
    if now - last_pub >= PUBLISH_EVERY_SECONDS:
        last_pub = now

        raw_value = water_sensor.value
        level_cm = adc_to_level(raw_value)

        # Print locally
        print(f"ADC: {raw_value}  Level: {level_cm:.2f} cm")

        # Publish to Adafruit IO (as a simple string/number)
        io.publish(FEED_PUBLISH, f"{level_cm:.2f}")

    time.sleep(0.02)
