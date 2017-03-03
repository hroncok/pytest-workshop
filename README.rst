Workshop o testování v Pythonu
==============================

Toto není soběstačný studijní materiál, ale pouze pomůcka k workshopu.

Workshop staví nad již `proběhlým workshopem o psaní TwitterWall v Pythonu
<https://notehub.org/nf98l>`_, tentokrát podle připomínek začínáme s gitovým
repositářem, aby se vám při workshopu lépe opisovalo. Nic se neděje, pokud jste
na předešlém workshopu nebyli.

V repozitáři je teď vypracovaná úloha *TwitterWall v Pythonu* se kterou se včas
seznámíme. Pro rozjetí musíte mít přihlašovací údaje k Twitteru:

Po přihlášení na Twitter (pokud nemáte, můžete si vytvořit nějaký dummy účet,
ale musíte přidat telefonní číslo) jděte na `apps.twitter.com
<https://apps.twitter.com/>`_ a vytvořte aplikaci (URL si můžete vymyslet).
Po vytvoření najdete na kartě *Keys and Access Tokens* *API Key* a
*API Secret*. Nemusíme doufám zdůrazňovat, že se jedná prakticky o hesla k
vašemu Twitter účtu, a proto by je nikdo kromě vás neměl vidět.
Tyto hodnoty uložte do souboru ``~/.twitter.ini`` v následujícím formátu:

.. code :: ini

    [auth]
    key = D4HJp6PKmpon9eya1b2c3d4e5
    secret = rhvasRMhvbuHJpu4MIuAb4WO50gnoQa1b2c3d4e5f6g7h8i9j0

Poté budete potřebovat prostředí pro Python:

.. code :: bash

    $ python3.5 -m venv env  # vytvoření virtualenvu
    $ . env/bin/activate  # aktivace
    (env)$ python -m pip install -r requirements.txt  # příkaz na instalaci balíčků puštěný ve virtualenvu
    (env)$ ...  # práce "uvnitř"
    (env)$ deactivate  # vypnutí virtualenvu

Zbytek si ukážeme a vysvětlíme na workshopu.

Studijní materiály
------------------

Pokud hledáte materiály, podívejte se na `cvičení o testování z předmětu MI-PYT
<https://github.com/cvut/MI-PYT/blob/master/tutorials/04_testovani.md>`_
(Pokročilý Python).

Licence
-------

Všechny ukázky kódu i texty v tomto repozitáři jsou vydané pod licencí
`CC0 1.0 Universal Public Domain Dedication
<https://creativecommons.org/publicdomain/zero/1.0/>`_.
Znamená to, že si s nimi můžete dělat, co uznáte za vhodné.
