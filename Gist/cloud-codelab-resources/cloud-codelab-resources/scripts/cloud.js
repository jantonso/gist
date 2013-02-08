// Local port; change if another process is running on 8080
var PORT = '8080';

function fetchUserPhotos(input) {
  var form = input.form;
  var personId = form.personSelect.value;
  
  if (personId) {
    var url = 'http://localhost:'+PORT+'/photos?oauth_consumer_key=appengine&opensocial_owner_id=' + personId;

    new Ajax.Request(url, {
      method: 'get',
      onSuccess: function(transport) {
        var container = document.getElementById('fetchUserPhotosResponse');
        container.innerHTML = transport.responseText;
      }
    });
  }
};

function fetchGroupPhotos(input) {
  var form = input.form;
  var peopleSelect = form.peopleSelect;
  var peopleIds = [];
  
  for (i=0; i<peopleSelect.options.length; i++) {
     if (peopleSelect.options[i].selected) {
      peopleIds.push(peopleSelect.options[i].value);
    }
  }
  
  if (peopleIds.length > 0) {
    var url = 'http://localhost:'+PORT+'/photos?oauth_consumer_key=appengine&opensocial_owner_id=00000000000000000000';

    new Ajax.Request(url, {
      method: 'post',
      postBody: 'people='+encodeURIComponent(peopleIds),
      onSuccess: function(transport) {
        var container = document.getElementById('fetchGroupPhotosResponse');
        container.innerHTML = transport.responseText;
      }
    });
  }
};

function addPhotoTag(input) {
  var form = input.form;
  var selectedPhoto = form.photoSelect.value;
  var tag = form.tagInput.value;
  
  if (tag != '') {
    var url = 'http://localhost:'+PORT+'/photo/appengine:00000000000000000000:'+selectedPhoto+'?oauth_consumer_key=appengine&opensocial_owner_id=00000000000000000000';

    new Ajax.Request(url, {
      method: 'post',
      postBody: 'text='+encodeURIComponent(tag),
      onSuccess: function(transport) {
        var container = document.getElementById('addPhotoTagResponse');
        container.innerHTML = 'Tag added!';
      }
    });
  }  
}

function fetchUserTags(input) {
  var form = input.form;
  var personId = form.personSelect.value;
  
  var url = 'http://localhost:'+PORT+'/tags?oauth_consumer_key=appengine&opensocial_owner_id=' + personId;

  new Ajax.Request(url, {
    method: 'get',
    onSuccess: function(transport) {
      var container = document.getElementById('fetchUserTagsResponse');
      container.innerHTML = transport.responseText;
    }
  });
}