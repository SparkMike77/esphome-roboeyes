# esphome-roboeyes

Roboeyes implementation for ESPHome — animated eyes for OLED/TFT displays.

## Component structure

```
components/roboeyes/
├── __init__.py      ← ESPHome Python schema + code generation
├── roboeyes.h       ← C++ class definition
├── roboeyes.cpp     ← C++ implementation
└── component.yaml   ← metadata (name, version)
```

## Usage

### Option 1: GitHub external component

```yaml
external_components:
  - source: github://SparkMike77/esphome-roboeyes
    components: [roboeyes]
```

### Option 2: Copy locally

Copy the `components/` folder from this repo next to your ESPHome YAML:

```
esphome/
├── roboeyes-test.yaml
└── my_components/
    └── roboeyes/
        ├── __init__.py
        ├── roboeyes.h
        └── roboeyes.cpp
```

Then reference it in your YAML:

```yaml
external_components:
  - source:
      type: local
      path: my_components
    components: [roboeyes]
```

## Configuration

```yaml
display:
  - platform: ssd1306_i2c
    model: "SSD1306 128x64"
    id: my_display
    address: 0x3C
    # draw lambda calls roboeyes.draw() each frame

roboeyes:
  display_id: my_display
```

## API

Call these from lambdas or automations:

- `id(roboeyes_id).blink_once()` — trigger a single blink
- `id(roboeyes_id).open_eye()` — force eye open
- `id(roboeyes_id).move_pupil(x, y)` — move pupil to pixel position
- `id(roboeyes_id).set_pupil_radius(r)` — set pupil size
- `id(roboeyes_id).draw()` — call inside a display lambda to render
