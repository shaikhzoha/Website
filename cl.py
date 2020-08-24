import socket
# a = int(input(&#39;Enter the alpha value&#39;))
# q = int(input(&#39;Enter the prime number greater than alpha&#39;))
#

# prim_check = []
# for i in range(1,q):
# prim_check.append((a**i)%q)
# flag = 1
# prim_set = set(prim_check)
# if len(prim_check) == len(prim_set):
# flag = 0
#
# if flag:
# print(f&#39;{a} is not the primitive root of {q}.Thus Diffie hellman cannot be
#continued.Re-run the program and enter new values&#39;)
# else:
# print(f&#39;{a} is the primitive root of {q}.Thus Diffie hellman can be continued.&#39;)
#
# xa = int(input(&#39;Enter Xa such that it is less than entered prime number&#39;))
a = 2
q = 13
xa = 6
# xb = int(input(&#39;Enter Xb such that it is less than entered prime number&#39;))
xb = 11
yb = a**xb % q
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 1024))
client.send(bytes(str(yb),&quot;utf-8&quot;))
from_server1 = client.recv(4096)
print(f&quot;Exchanged public key is {int(from_server1)}&quot;)
ya = int(from_server1)
kb = ya ** xb % q
from_server2 = client.recv(4096)
client.send(bytes(str(kb),&quot;utf-8&quot;))
print(f&quot;Exchanged secret key is {int(from_server2)}&quot;)
key = int(from_server2)
from_server3 = client.recv(4096)
plain = from_server3.decode(&quot;utf-8&quot;)
print(f&#39;The encrypted text sent by server is {plain}&#39;)

uppercase = [&#39;A&#39;, &#39;B&#39;, &#39;C&#39;, &#39;D&#39;, &#39;E&#39;, &#39;F&#39;, &#39;G&#39;, &#39;H&#39;, &#39;I&#39;, &#39;J&#39;, &#39;K&#39;, &#39;L&#39;, &#39;M&#39;, &#39;N&#39;, &#39;O&#39;, &#39;P&#39;, &#39;Q&#39;, &#39;R&#39;, &#39;S&#39;, &#39;T&#39;, &#39;U&#39;,
&#39;V&#39;, &#39;W&#39;, &#39;X&#39;, &#39;Y&#39;, &#39;Z&#39;,&#39; &#39;]
lowercase = [&#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;d&#39;, &#39;e&#39;, &#39;f&#39;, &#39;g&#39;, &#39;h&#39;, &#39;i&#39;, &#39;j&#39;, &#39;k&#39;, &#39;l&#39;, &#39;m&#39;, &#39;n&#39;, &#39;o&#39;, &#39;p&#39;, &#39;q&#39;, &#39;r&#39;, &#39;s&#39;, &#39;t&#39;, &#39;u&#39;, &#39;v&#39;, &#39;w&#39;,
&#39;x&#39;, &#39;y&#39;, &#39;z&#39;]
outText = []
for eachLetter in plain:
if eachLetter in uppercase:
index = uppercase.index(eachLetter)
decrypting = ((index + 27) - key) % 27
newLetter = uppercase[decrypting]
outText.append(newLetter)
elif eachLetter in lowercase:
index = lowercase.index(eachLetter)
decrypting = ((index + 26) - key) % 26
newLetter = lowercase[decrypting]
outText.append(newLetter)
a = &#39;&#39;.join(outText)
print(&#39;The decrypted text from server is : &#39;, a)
client.close()