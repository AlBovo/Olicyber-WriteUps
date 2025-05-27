Per risolvere questa challenge bisognerà:
1. Scaricare il file "nw-intro08.pcap"
2. Aprire il file con Wireshark
3. Usare il filtro per mostrare solo i pacchetti TCP contenenti dati <code>tcp.stream eq 0 && tcp.len > 0</code>
4. Visualizzare i dettagli del pacchetto concentrandosi sulla sezione Data, cliccando con il tasto destro del mouse scegliamo "Show Packet Bytes" e ci verrà mostrata la flag: <code>**flag{Byt35_Ex7rAct10n_1s_3a5y!}**</code>
