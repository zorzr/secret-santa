function decrypt() {
	var cypher = $('#token').val();
	var key = '0t0IFg1SpOXb4qDPEDZeglB9qH-hYmWQGOh5JXIoKsc=';

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