// Graham S. Paul (9-script.js)
$(document).ready(function sayHello () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
    const hello = data.hello;
    $('DIV#hello').text(hello);
  });
});
