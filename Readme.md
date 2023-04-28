# Cafe Square One

Anything related to cafe square one

## Setting up development

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Environment Variable

Cafe Square One
- `SHORT_URL`: cafe-square-one
- `GUID`: f45640aa-3350-4e46-81a4-1712171ad916

Eggcellent
- `SHORT_URL`: eggcellent
- `GUID`: 8e50a1c4-8c0b-46d5-aeb0-ff222be50152

```
export SHORT_URL=eggcellent
export GUID="8e50a1c4-8c0b-46d5-aeb0-ff222be50152"
```


## Import Menu

### As txt for website
```
python get_menu_txt.py
```

### Generate html for print
```
python get_menu_csv.py
python generate_html.py food.csv food.html
```

## Reference

https://github.com/dasmer/piatto
