$.get('http://fourtonfish.com/hellosalut/?mode=auto', function (data) {
  $('div#hello').text(data.hello)
});
