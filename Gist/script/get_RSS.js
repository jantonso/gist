var scores=new Array();
var currentindex=0;

google.load("feeds", "1");
      

function isEnter(event){
  if(event.keyCode ===  13){
    console.log('works');
    getRSS(); 
  }
  return true;
}

var searchteam=-1;

var teams = ["Bulls", "Pistons", "Bucks", "Pacers", "Cavs", "Cavaliers", "Nuggets", "Wolves", "Timberwolves", "Blazers", "Trail Blazers", "Thunder", "Jazz", "Celts", "Celtics", "Nets", "Knicks", "76ers", "Raptors", "Mavs", "Mavericks", "Rockets", "Grizzlies", "Hornets", "Spurs", "Hawks", "Bobcats", "Heat", "Magic", "Wizards", "Warriors", "Lakers", "Clippers", "Suns", "Kings"];
var teams2 = ["Chicago Bulls", "Detroit Pistons", "Milwaukee Bucks", "Indiana Pacers", "Cleveland Cavs", "Cleveland Cavaliers", "Denver Nuggets", "Minnesota Wolves","Minnesota Timberwolves", "Portland Blazers", "Portland Trail Blazers", "Oklahoma City Thunder", "Utah Jazz", "Boston Celts", "Boston Celtics", "New Jersey Nets", "New York Knicks", "Philadelphia 76ers", "Toronto Raptors", "Dallas Mavs", "Dallas Mavericks", "Houston Rockets", "Memphis Grizzlies", "New Orleans Hornets", "San Antonio Spurs", "Atlanta Hawks", "Charlotte Bobcats", "Miami Heat", "Orlando Magic", "Washington Wizards", "Golden State Warriors", "Los Angeles Lakers", "Los Angeles Clippers", "Phoenix Suns", "Sacramento Kings"];
function setTeam(user_input){
  user_input=user_input.toLowerCase();
  for (var j=0;j<teams.length;j++) {
    if (teams[j].toLowerCase().indexOf(user_input) !=-1 || teams2[j].toLowerCase().indexOf(user_input)!=-1) {
      searchteam=j;
      break;
    }
  }
  if (searchteam==-1) {
    alert("enter a valid team");
  }
}

var search_button = document.getElementById('search-button');

/*
*  How to find a feed based on a query.
*/

google.load("feeds", "1");


function getRSS() {
  // Adapted from Google Feeds API Sample Code
  // Query for user input on espn.go.com

  if(document.getElementById('user-input').value){
    var user_input=document.getElementById('user-input').value;
  }
  else{
    var user_input="nba"
  }
  setTeam(user_input);
  
  document.getElementById('content').innerHTML=''

  var content=document.getElementById('content');
  while(content.childNodes.length>0) {
    console.log("string");
    content.removeChild(content.lastChild);
  }
  if (searchteam==-1) {
    return;

  }
  var team=teams[searchteam];
  var query = 'site:espn.go.com ' + team;
  google.feeds.findFeeds(query, findDone);
}
        
		
function findDone(result) {
  // Adapted from Google Feeds API Sample Code
	// Make sure we didn't get an error.
	if (!result.error) {
  	// Get content div
    var content = document.getElementById('content');
  	var html = '';
    // Loop through the results and search each for a score
    for (var i = 0; i < result.entries.length; i++) {
      var entry = result.entries[i];
      var con = entry.contentSnippet;   
      var matchteam=-1;
	  //search the entry title/content/link for other team names, stops when it gets a match
      for (var j=0;j<teams.length;j++) {
        if (j!=searchteam && (con.indexOf(teams[j])!=-1 || entry.title.indexOf(teams[j])!=-1 || entry.link.indexOf(teams[j])!=-1)) {
          matchteam=j;
          break;
        }
      }
	  //make sure we dont already have a score against that team
      for (var j=0;j<currentindex;j++) {
        if (scores[j][1]==matchteam) {
          matchteam=-1;
        }
            
      }
	  //if we found a [nother] team in the feed
      if (matchteam>=0) {
        var j;
        var k;
		// IF THE TITLE IS OF THE FORM "TEAM SCORE, TEAM SCORE"
        //find the searchteam in the TITLE
        init=entry.title.indexOf(teams[searchteam])+teams[searchteam].length+5;
        j=init;
		//there should be a number after it - keep going till the end of the number
        while(entry.title.charCodeAt(j)>47 && entry.title.charCodeAt(j)<58) {
          j++;
        }
		//find matchteam in the TITLE
        end=entry.title.indexOf(teams[matchteam])+teams[matchteam].length+1;
        k=end;
		//find the number after matchteam
        while(entry.title.charCodeAt(k)>47 && entry.title.charCodeAt(k)<58) {
          k++;
        }
		
        if (entry.title.indexOf(teams[searchteam])==-1) {
          j=init;
        }
        else if (entry.title.indexOf(teams[matchteam])==-1) {
          k=end;
        }
		//if we found a team name, score in the TITLE, store everything
        if (j>init && k>end) {
          var score=new Array(4);
          score[0]=searchteam;
          score[1]=matchteam;
          score[2]=parseInt(entry.title.substring(init,j));
          score[3]=parseInt(entry.title.substring(end,k));
          score[4]=new Date(entry.publishedDate);
          scores[currentindex]=score;
          currentindex++;
          console.log(teams[matchteam] + " " + score[2] + "-" + score[3]);
        }
		//else search the article
        else {
		//foundfirst is whether we've found the first number in "score-score"
          var foundfirst=false;
		  //founddash is whether we've found a hyphen after a number
		  
          var founddash=false;
		  //etc
          var foundsecond=false;
		  //positions olf the first score, hyphen, second score
          var init=-1;
          var end=-1;
          var dash=-1;
          for (var j=0;j<con.length;j++) {
		  //if we find a number
            if (con.charCodeAt(j)>47 && con.charCodeAt(j)<58) {
              //if we still havent found a first score, set this at the first
			  if (!foundfirst) {
				
                foundfirst=true;
                init=j;
              }
			  //otherwise set it as the second
              else if (foundfirst && founddash && !foundsecond) {
                foundsecond=true;
              }
                    
            }
			//if this is a hyphen, keep it if we've got a first score, discard otherwise
            else if (con.charAt(j)=="-") {
              if (foundfirst && !founddash && !foundsecond) {
                founddash=true;
                dash=j;
				//clear if the number if out of the score range 50..150
                if (Number(con.substring(init,j))<50 || Number(con.substring(init,j))>150) {
                  foundfirst=false;
                  founddash=false;
                  init=-1;
                  end=-1;
                  dash=-1;
                }
              }
			  //a random dash clears everything
              else if (foundfirst && (founddash || foundsecond)) {
                foundfirst=false;
                founddash=false;
                foundsecond=false;
                init=-1;
                end=-1;
                dash=-1;
              }
            }
                  
            else {
			//a non number after finding a score - 
              if (foundfirst && founddash && foundsecond) {
                end=j;
				//if we the scores are out of range clear
                if (Number(con.substring(dash+1,j))<50 || Number(con.substring(dash+1,j))>150) {
                  foundfirst=false;
                  founddash-false;
                  foundsecond=false;
                  init=-1;
                  dash=-1;
                  end=-1;
                }
				//otehrwise breeeeaaaaaaaaaak
                else {
                  break;
                }
              }
              else {
                foundfirst=false;
                founddash=false;
                foundsecond=false;
                init=-1;
                dash=-1;
                end=-1;
              }
            }
                  
          }
          //if we find a score, STORE it
          if (init>=0 && end>=0) {
            var score=new Array(4);
            score[0]=searchteam;
            score[1]=matchteam;
            score[2]=parseInt(con.substring(init,dash));
            score[3]=parseInt(con.substring(dash+1,end));
            score[4]=new Date(entry.publishedDate);
            scores[currentindex]=score;
            currentindex++;
            console.log(teams[matchteam] + " " + scores[currentindex-1][2] + "-" + scores[currentindex-1][3]);

          }
        }
              
      }
    }
    			
  }
  for (var i=0;i<currentindex;i++) {
    keyStats(i);  
    
        
	}
 
      keyPlayers(0);
      keyFacts(0);
    
}

		//google.setOnLoadCallback(getRSS);
