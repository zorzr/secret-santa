function decrypt() {
	var cypher = $('#token').val();
	var key = '-zlbWml6P3Nw8FDg3C38b88UyK-ZdXs3GqK000qpb38=';

	var plain = fernet_decode(cypher, key);
	$('#plaintext').val(plain);
}

function fernet_decode(cyphertext, key) {
	try {
		var token = new fernet.Token({
			secret: new fernet.Secret(key),
			token: cyphertext,
			ttl: 0
		});
		return token.decode();
	} catch (error) {
		console.log(error);
		return '';
	}
}