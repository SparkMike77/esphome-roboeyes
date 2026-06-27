# esphome-roboeyes

Roboeyes implementation for ESPHome — animated eyes for OLED/TFT displays.

## Installation (local, no internet required at compile time)

Clone or copy this repo directly into your ESPHome config's `components/` folder,
named `roboeyes`:

```bash
# Option A: git clone into the right place
git clone https://github.com/SparkMike77/esphome-roboeyes \
    ~/esphome/components/roboeyes

# Option B: copy the folder
cp -r esphome-roboeyes/ ~/esphome/components/roboeyes/
```

Result:

```
esphome/
├── your-device.yaml
└── components/
    └── roboeyes/        ← this repo
        ├── __init__.py
        ├── roboeyes.h
        └── roboeyes.cpp
```

ESPHome automatically discovers components in `config/components/` — no
`external_components:` block needed in your YAML.

## Configuration

```yaml
display:
  - platform: ssd1306_i2c
    model: "SSD1306 128x64"
    id: my_display
    address: 0x3C

roboeyes:
  display_id: my_display
```

Call `id(roboeyes_id).draw()` inside your display lambda to render each frame.

## API

- `blink_once()` — trigger a single blink
- `open_eye()` — force eye open
- `move_pupil(x, y)` — move pupil to pixel position
- `set_pupil_radius(r)` — set pupil size in pixels
- `draw()` — render to the display (call from display lambda)
