function decrypt() {
	var cypher = $('#token').val();
	var key = 'lcyi9SxSWd8Myyta7aMrEiEUO3G3ymaCvAgMsjAWzeA=';

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