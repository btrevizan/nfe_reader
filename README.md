# Grocery List

A Nota Fiscal (NF) reader made in Python 3.

## Usage
```bash
usage: main.py [-h] [-f FILE] [-u URL]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Input filepath.
  -u URL, --url URL     NF url.
```

## Example
```bash
$ python3 main.py -f urls.txt
```

You can use with only one URL:
```bash
$ python3 main.py -u https://www.sefaz.rs.gov.br/ASP/AAE_ROOT/NFE/SAT-WEB-NFE-NFC_QRCODE_1.asp?chNFe=43160393015006000970651030000431701166480721&nVersao=100&tpAmb=1&cDest=03325042040&dhEmi=323031362d30332d32385431343a32303a31312d30333a3030&vNF=49.27&vICMS=1.04&digVal=4b4a505a61377366486b59645035754554676c527a366c443336413d&cIdToken=000001&cHashQRCode=9AAD1C95C0F3D4E49132BE771FDED30D775B7010
```

There is an example of input file: `urls.txt`.

## Note
This reader was made based on Rio Grande do Sul's Government Web Service for NF-e.

The code is very readable and can be used as a data getter for Web Scrapers.
