# Marktstammdaten-API

Dokumentation der APIs des [Marktstammdatenregisters](https://www.marktstammdatenregister.de/MaStR).

Das Marktstammdatenregister ist das Register für den deutschen Strom- und Gasmarkt, abgekürzt MaStR. Im MaStR werden vor allem die Stammdaten zu Strom- und Gaserzeugungsanlagen registriert, sowie die Stammdaten von Marktakteuren wie Anlagenbetreibern, Netzbetreibern und Energielieferanten. Das MaStR wird von der Bundesnetzagentur geführt.

## Inhalt

Informationen zu öffentlichen Stromerzeugungseinheiten (Solardächern, Biogasanlagen,...)


## Beispiel

```bash
datenStromerzeugung=$(curl "https://www.marktstammdatenregister.de/MaStR/Einheit/EinheitJson/GetErweiterteOeffentlicheEinheitStromerzeugung?filter=In%20Betrieb~eq~35&page=1&pageSize=1")
filterStromerzeugung=$(curl https://www.marktstammdatenregister.de/MaStR/Einheit/EinheitJson/GetFilterColumnsErweiterteOeffentlicheEinheitStromerzeugung)
filterStromverbrauch=$(curl https://www.marktstammdatenregister.de/MaStR/Einheit/EinheitJson/GetFilterColumnsErweiterteOeffentlicheEinheitStromverbrauch)
filterGaserzeugung=$(curl https://www.marktstammdatenregister.de/MaStR/Einheit/EinheitJson/GetFilterColumnsErweiterteOeffentlicheEinheitGaserzeugung)
filterGasverbrauch=$(curl https://www.marktstammdatenregister.de/MaStR/Einheit/EinheitJson/GetFilterColumnsErweiterteOeffentlicheEinheitGasverbrauch)
```
