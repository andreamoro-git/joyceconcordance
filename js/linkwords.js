
function getQueryParams(sParam) {
  var sPageURL = window.location.search.substring(1);
  var sURLVariables = sPageURL.split('&');
  for (var i = 0; i < sURLVariables.length; i++)
  {
    var sParameterName = sURLVariables[i].split('=');
    if (sParameterName[0] == sParam)
    {
      return sParameterName[1];
    }
  }
}
function addHighLight(wordq) {


  var highlightRe = /<span class="highlight">(.*?)<\/span>/g,
    highlightHtml = '<span class="highlight">$1</span>';

  var term = wordq
  var $allrows = $('span.row');
  $.each($allrows, function(i,v) {
  var txt = $(this).html().replace(highlightRe,'$1');
    if(term !== '') {
      txt = txt.replace(new RegExp('(' + term + ')', 'gi'), highlightHtml);
    }
    $(this).html(txt);
  });
}


$(document).ready(function(){

  // check if this is a word search
  var wordq = '';
  if (getQueryParams('w')) {
    var wordq = getQueryParams('w');
  }

  // add links on click
  $('#addlinks').click(function() {
    var $allrows = $('span.row');
    $.each($allrows, function(i,v) {
      var $this = $(this);
      var words = v.innerText.split(/\s+/);
      $(this).empty();
      $.each(words, function(ii,vv) {

        // extract word without punctuation
        var wordonly = RegExp('\\w+','g').exec(vv)
        if (wordonly != null) {
          wordonly = wordonly[0]
          if (wordonly==wordq) {
            $this.append("<span class='highlight'><a href='?w="+wordonly+"'>"+vv+"</a></span> ");
          } else {
            $this.append("<a href='?w="+wordonly+"'>"+vv+"</a> ");
          }
        };
      });
    });
  });

  addHighLight(wordq);

});
