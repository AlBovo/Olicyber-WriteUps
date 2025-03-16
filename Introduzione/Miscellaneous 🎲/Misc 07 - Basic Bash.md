
### Per risolvere questa Challenge leggere attentamente la descrizione della challenge per capire le azioni da eseguire al fine di completare con successo la scoperta della flag.

Ogni comando ci permetterà di scoprire "parte" della flag che alla fine comporremo.

I comandi da eseguire sono i seguenti:

1. <code>'ls -l .esempio'</code> output <code>'-rw-r--r-- 1 root root 109 Feb 10 15:27 .esempio'</code>

2. <code>'cat gatto'</code> output <code>'ffeaf8a1a4a9a9ef'</code>

3. <code>'./eseguibile'</code> output <code>'banananana'</code>

4. <code>'grep -r olicyber'</code> output <code>'sottocartella/9e8b1fd8f180b627:olicybercamp2025'</code>

Componendo l'intera flag otterremo:

<code> flag{109_ffeaf8a1a4a9a9ef_banananana_9e8b1fd8f180b627} </code>