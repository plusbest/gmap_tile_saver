# Simple GoogleMap Tile Save Script

Simple script to save google satellite image tiles via [khms0 google api](khms0.googleapis.com).
* Note: Saves based on relative x, y coordinates -- NOT lat lon coords.

## Dependency


```bash
pip install request
```

## Usage
1. Replace `x_coord_range`, `y_coord_range`, and `zoom` level.

```python
python main.py
```
3. See saved 256x256 px saved tiles in script source folder.

### Disclaimer
Use the embedded googleapi link query at your own risk as multiple queries may result in blacklisting.

## License
[MIT](https://choosealicense.com/licenses/mit/)