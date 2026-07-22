# Easypad-V2
A compact macropad featuring RGB lighting with SK6812 MINI-E Neopixel LEDs, a rotary encoder, a SSD1306 OLED Display and 15 (low-profile) choc mechanical switches! Powered by KMK firmware!

<img width="873" height="839" alt="image" src="https://github.com/user-attachments/assets/5bd32174-ac7c-4a0f-bc5a-48186b4f907b" />

# Features:
Per-key RGB lighting via SK6812 MINI-E RGB LEDs, page scrolling via the onboard EC11 rotary encoder, a 0.91" 128x32 SSD1306 OLED display to display current mode, and 15 tactile low profile Kalih Choc V1 switches for compactability.

# Why?
I wanted to experiment with compact designs and Choc switches. I built this to help get the grasp of making keyboards/macropads with Kalih Choc switches since they have a different pin layout and are way more compact. I also wanted to make this because I really love designing hardware projects and PCBs in general every chance I get time.

# Flashing Firmware:
To flash the firmware to the macropad, first you will need to install CircuitPython onto the RPi Pico by first downloading the .uf2 file from the CircuitPython website and then dragging and dropping it to the USB Drive the Pico shows up as. Then, install KMK on it and then upload the code.py to the board. Instructions for installing KMK is on the KMK GitHub repo.

# Schematic:
<img width="3507" height="2480" alt="image" src="https://github.com/user-attachments/assets/262eda4f-6d83-4c55-914e-0b6c521d8cf9" />

# PCB: 
<img width="292" height="326" alt="image" src="https://github.com/user-attachments/assets/25097ea4-ab0a-4d57-9c9a-58eb39b04f80" />

<img width="509" height="565" alt="image" src="https://github.com/user-attachments/assets/80898c1f-b218-4731-84ce-a31d28426eee" />

# CAD Link:
The assembled version is in Assembly 1!
https://cad.onshape.com/documents/4159a499467d346143555145/w/def90a5bdc25ba8320f86079/e/58cc027c9599ddc6d01a6483

# BOM:
| Part | Source | Quantity | Cost | Link |
|---|---|---|---|---|
| PCB | JLCPCB | 5 (MOQ) | $5.30 (with Shipping) | https://jlcpcb.com/ |
| Header Pins | AliExpress | 1 (comes with 5 male-female sets) | $1.79 | https://www.aliexpress.us/item/3256807049277042.html?spm=a2g0o.cart.0.0.79b838daFbyhMJ&mp=1&sourceType=570&pdp_npi=6%40dis%21USD%21USD+6.03%21USD+1.79%21%21USD+1.79%21%21%21%40210311c217847467351336984e0d3d%2112000039908542823%21ct%21US%21861143113%21%211%210%21&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D&gatewayAdapt=glo2usa |
| RPi Pico (clone) | AliExpress | 1 | $2.79 | https://www.aliexpress.us/item/3256807207612469.html?spm=a2g0o.cart.0.0.79b838daFbyhMJ&mp=1&sourceType=570&pdp_npi=6%40dis%21USD%21USD+8.63%21USD+2.59%21%21USD+2.59%21%21%21%40210311c217847467351336984e0d3d%2112000040565295947%21ct%21US%21861143113%21%211%210%21&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D&gatewayAdapt=glo2usa |
| 128x32 OLED | AliExpress | 1 | $1.99 | https://www.aliexpress.us/item/3256807613276538.html?spm=a2g0o.cart.0.0.79b838daFbyhMJ&mp=1&sourceType=570&pdp_npi=6%40dis%21USD%21USD+3.38%21USD+1.99%21%21USD+1.99%21%21%21%40210311c217847467351336984e0d3d%2112000042242093250%21ct%21US%21861143113%21%211%210%21&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D&gatewayAdapt=glo2usa |
| Switches | AliExpress | 2 sets of 10pcs | $5.79 | https://www.aliexpress.us/item/3256811626047380.html?spm=a2g0o.cart.0.0.79b838daFbyhMJ&mp=1&pdp_npi=6%40dis%21USD%21USD+6.11%21USD+5.79%21%21USD+5.79%21%21%21%40210311c217847467351336984e0d3d%2112000056648742495%21ct%21US%21861143113%21%212%210%21&gatewayAdapt=glo2usa |
| 1N4148W Diodes | AliExpress | 100 | $1.48 | https://www.aliexpress.us/item/3256804920500448.html?spm=a2g0o.cart.0.0.79b838daFbyhMJ&mp=1&pdp_npi=6%40dis%21USD%21USD+1.48%21USD+1.48%21%21USD+1.48%21%21%21%40210311c217847467351336984e0d3d%2112000031683474020%21ct%21US%21861143113%21%211%210%21&gatewayAdapt=glo2usa |
| SK6812 Mini E LEDs | AliExpress | 100pcs | $7.33 | https://www.aliexpress.us/item/3256810305129996.html?spm=a2g0o.cart.0.0.79b838daFbyhMJ&mp=1&pdp_npi=6%40dis%21USD%21USD+7.33%21USD+7.33%21%21USD+7.33%21%21%21%40210311c217847467351336984e0d3d%2112000052582134405%21ct%21US%21861143113%21%211%210%21&gatewayAdapt=glo2usa |
| Rotary Encoder | AliExpress | 5 | $3.58 | https://www.aliexpress.us/item/2255799842376254.html?spm=a2g0o.cart.0.0.79b838daFbyhMJ&mp=1&pdp_npi=6%40dis%21USD%21USD+3.58%21USD+2.58%21%21USD+2.58%21%21%21%40210311c217847467351336984e0d3d%2110000000064746984%21ct%21US%21861143113%21%211%210%21&gatewayAdapt=glo2usa |
| Black Keycaps | AliExpress | 20 | $5.61 | https://www.aliexpress.us/item/3256810543438304.html?spm=a2g0o.cart.0.0.79b838daFbyhMJ&mp=1&pdp_npi=6%40dis%21USD%21USD+5.59%21USD+5.59%21%21USD+5.59%21%21%21%40210311c217847467351336984e0d3d%2112000053333576164%21ct%21US%21861143113%21%211%210%21&gatewayAdapt=glo2usa |
