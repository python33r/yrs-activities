"""Functions for plotting points on maps."""

__author__ = "Nick Efford"
__version__ = "1.0"


_PAGE_TOP = """\
<!doctype HTML>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Earthquake Map</title>
<script type="text/javascript" src="http://www.google.com/jsapi"></script>
<script type="text/javascript">
  google.load("visualization", "1", {packages:["map"]});
  google.setOnLoadCallback(drawMap);
  function drawMap() {
    var data = new google.visualization.arrayToDataTable([
      ['Lat', 'Lon', 'Details'],"""

_PAGE_BOTTOM = """\
    ]);
    var map = new google.visualization.Map(document.getElementById('map'));
    map.draw(data, {showTip: true});
  }
</script>
</head>
<body>
  <div id="map" style="width:800px; height:500px"></div>
</body>
</html>"""


def google_map(points, filename):
    """Generates a Google map of the given points, in the given file.

       Points must be supplied as a list of tuples in which the first
       two items are the longitude and latitude, respectively, and
       the third item is a string of information.
    """
    with open(filename, "wt") as outfile:
        print(_PAGE_TOP, file=outfile)
        for lon, lat, info in points:
            line = '      [{}, {}, "{}"],'.format(lat, lon, info)
            print(line, file=outfile)
        print(_PAGE_BOTTOM, file=outfile)
