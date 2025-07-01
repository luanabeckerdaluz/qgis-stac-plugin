# Commands to generate plugin zip

1) Install dependencies using poetry:
``` 
poetry update --lock
poetry install --no-root
```

2) After all changes on soure code, build using:
```
poetry run python admin.py install
```
This will generate the *build/* folder.

3) To zip the folder *qgis_stac/* inside this *build/* folder, run:
```
cd build/ && zip -o qgis_stac.zip qgis_stac/* && cp qgis_stac.zip ../ && cd ..
```

4) Then, install it on QGIS using **Install from zip** option.


# qgis-stac-plugin

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/stac-utils/qgis-stac-plugin/ci.yml?branch=main)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/stac-utils/qgis-stac-plugin?include_prereleases)
![GitHub](https://img.shields.io/github/license/stac-utils/qgis-stac-plugin)

QGIS plugin for reading STAC APIs

Site https://stac-utils.github.io/qgis-stac-plugin

**The QGIS STAC API Browser currently lacks funding for maintenance,
bug fixes and new features; therefore development will be slow for now.
However we’re dedicated to maintaining the project. 
For assistance or if you have funding to contribute 
please reach out to Kartoza ([info@kartoza.com](mailto:info@kartoza.com))**

### Installation

During the development phase the plugin is available to install via 
a dedicated plugin repository 
https://stac-utils.github.io/qgis-stac-plugin/repository/plugins.xml

Open the QGIS plugin manager, then select the **Settings** page, click **Add** 
button on the **Plugin Repositories** group box and use the above url to create
the new plugin repository.
![Add plugin repository](docs/images/plugin_settings.png)

After adding the new repository, the plugin should be available from the list
of all plugins that can be installed.

**NOTE:** While the development phase is on going the plugin will be flagged as experimental, make
sure to enable the QGIS plugin manager in the **Settings** page to show the experimental plugins
in order to be able to install it.

Alternatively the plugin can be installed using **Install from ZIP** option on the 
QGIS plugin manager. Download zip file from the required plugin released version
https://github.com/stac-utils/qgis-stac-plugin/releases/download/{tagname}/qgis_stac.{version}.zip.

From the **Install from ZIP** page, select the zip file and click the **Install** button to install
plugin
![Screenshot for install from zip option](docs/images/install_from_zip.png)

When the development work is complete the plugin will be available on the QGIS
official plugin repository.


#### Development 

To use the plugin for development purposes, clone the repository locally,
install poetry, a python dependencies management tool see https://python-poetry.org/docs/#installation
then using the poetry tool, update the poetry lock file and install plugin dependencies by running 
``` 
poetry update --lock
poetry install --no-dev
```

To install the plugin into the QGIS application use the below command
```
poetry run python admin.py install
```


