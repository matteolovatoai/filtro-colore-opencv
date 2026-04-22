# Filtro colore su immagini  

Lo script legge un'immagine e crea una nuova immagine mantenendo il colore rosso inalterato ed il resto in bianco e nero  

Lo scopo del progetto è imparare ad usare openCV per modificare immagini, spazio colori, maschere.  

Le immagini utilizzate sono prese da pexels.com
Foto di Hatice Noğman da Pexels: [mela.jpg](https://www.pexels.com/it-it/foto/cibo-sgabello-apple-mela-14833259/)

Immagine originale che rappresenta una mela su uno sgabello:
<img width="480" height="640" alt="mela" src="https://github.com/user-attachments/assets/5a266693-6dc3-4200-8625-468f8cf5f1d0" />
Sicoome il colore rosso è sia all'inzio (0-10) che alla fine (160-180) dello spettro HSV ho calcolato 2 maschere per poi unirle
maschera 1 rosso-arancio (ho usato il valore da 0 a 6 per escludere parti marroni del legno)
<img width="480" height="640" alt="mask_1" src="https://github.com/user-attachments/assets/e51fdb16-1448-4eb5-bced-1fb17524fb22" />
maschera 2 rosso-viola
<img width="480" height="640" alt="mask_2" src="https://github.com/user-attachments/assets/2879072d-8926-44c0-b610-412cc671058c" />
maschera totale (ho unito le 2 maschere) con applicato l'apertura, ovvero una fase di erosione dell'immagine con un kernel (10,10), nella pratica significa togliere dai bordi un blocco (10,10), come passare un pennello all'interno del bordo, questo ci permette di uccidere i pixel singoli sparsi per la maschera (polvere o riflessi) che generano rumore, seguita da una fase di dilatazione, l'esatto opposto dell'erosione, ovvero passo il kernel all'esterno del bordo, per riportare gli oggetti rilevati alla dimensione e forma originale (i pixel singoli che sono stati mangiati dall'erosione restano spenti). Ora che l'apertura è conclusa, viene applicata la chiusura, ossia, applico prima la dilatazione e poi l'erosione, questo permette di unire i contorni vicini (se ad esempio un oggetto viene spezzato in 2 per un riflesso, questo lo riunisce sotto lo stesso oggetto)
<img width="480" height="640" alt="maschera" src="https://github.com/user-attachments/assets/ff6b57ad-872e-4665-a3ae-b3d33ebee1bf" />
Applico la maschera all'immagine a colori per ottenere la mela rossa:
<img width="480" height="640" alt="masked_mela" src="https://github.com/user-attachments/assets/56700062-7386-4a66-9af1-52c2cb5c583d" />
Inverto la maschera e la applico all'immagine con lo spazio colori su scala di grigi
<img width="480" height="640" alt="masked_mela_gray" src="https://github.com/user-attachments/assets/b3273fc1-9a2d-457f-a718-652d58584fba" />
Unisco le due immagini per ottenere il filtro, resta solo il rosso ed il resto compare in bianco e nero
<img width="480" height="640" alt="result_mela" src="https://github.com/user-attachments/assets/0725f686-d63a-45b7-96bf-5a61cc338acc" />
Dalla maschera ottengo le informazioni dei contorni, calcolo il contorno più grande e recupero le informazioni (x, y, w, h) del boundingRect, il rettangolo dritto più piccolo che contiene il contorno rilevato, uso le stesse informazioni per scrivere la label
<img width="480" height="640" alt="box_mela" src="https://github.com/user-attachments/assets/0984c936-7bae-45fb-a302-808d32226c0f" />
