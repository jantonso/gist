var scores=new Array();
var currentindex=0;

google.load("feeds", "1");
			

var searchteam=-1;
var teams = ["Bulls", "Pistons", "Bucks", "Pacers", "Cavs", "Cavaliers", "Nuggets", "Wolves", "Timberwolves", "Blazers", "Trail Blazers", "Thunder", "Jazz", "Celts", "Celtics", "Nets", "Knicks", "76ers", "Raptors", "Mavs", "Mavericks", "Rockets", "Grizzlies", "Hornets", "Spurs", "Hawks", "Bobcats", "Heat", "Magic", "Wizards", "Warriors", "Lakers", "Clippers", "Suns", "Kings"];

for ( var j=0;j<teams.length;j++) {
	if (teams[j].indexOf(user_input) !=-1) {
		searchteam=j;
		break;
	}
}
   if (searchteam==-1) {
	document.write("enter a valid team");
}