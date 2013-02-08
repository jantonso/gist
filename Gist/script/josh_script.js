function createSpanResults(index)
    {
        var spanTag = document.createElement("span");
       
        spanTag.id = "span" + index;

        spanTag.className ="results";

        document.getElementById('content').innerHTML='';

        document.getElementById("content").appendChild(spanTag);
    }

function createSpanKeyPlayers(index)
    {
        var spanTagKeyPlayers = document.createElement("span");
       
        spanTagKeyPlayers.id = "spanKeyPlayers" + index;

        spanTagKeyPlayers.className ="keyPlayers";

        document.getElementById("content").appendChild(spanTagKeyPlayers);
    }

function createSpanKeyScorer(index)
    {
        var spanTagKeyScorer = document.createElement("span");
       
        spanTagKeyScorer.id = "spanKeyScorer" + index;

        spanTagKeyScorer.className ="keyScorer";

        document.getElementById("content").appendChild(spanTagKeyScorer);
    }

function keyStats(index) {
  //console.log("Keystats index"+index);
  input(index);
  //keyPlayers(index);
  //keyFacts(index);  
}

//var player = "Rose";
//var points = "97"
function keyScorer(player,points) 
{
 createSpanKeyScorer(index);
 var txt = document.createTextNode(player + " scored " + points + " !\n");
 document.getElementById("spanKeyScorer" + index).appendChild(txt);
 document.getElementById("spanKeyScorer" + index).write; 
}

function input(index)
{
  var score1=scores[index][2];
  var score2=scores[index][3];
  var team1=teams[scores[index][0]];
  var team2=teams[scores[index][1]];
  var difference = score1 - score2;
   if (difference > 0)
    {
     if (difference >15)
      {
       createSpanResults(index)
       var txt = document.createTextNode(team1 + " won in a blowout " + score1+"-"+score2+" against the " + team2 + "!\n");
       document.getElementById("span" + index).appendChild(txt);
      }
     else if (difference < 5) 
      {
       createSpanResults(index)
       var txt = document.createTextNode(team1 + " " + "won a close game " + score1+"-"+score2+" against the " + team2 + "!\n");
       document.getElementById("span" + index).appendChild(txt);
      }
     else if (difference >= 5 && difference <= 15)
      {
       createSpanResults(index)
       var txt = document.createTextNode(team1 + " " + "won " + score1+"-"+score2+" against the " + team2 + "!\n");
       document.getElementById("span" + index).appendChild(txt);
      }
    }
   if (difference < 0)
    {
     if (Math.abs(difference) >15)
      {
       createSpanResults(index)
       var txt = document.createTextNode(team1 + " lost in a blowout " + score1+"-"+score2+" against the " + team2 + "!\n");
       document.getElementById("span" + index).appendChild(txt);
      }
     else if (Math.abs(difference) < 5) 
      {
       createSpanResults(index)
       var txt = document.createTextNode(team1 + " " + "lost a close game " + score1+"-"+score2+" against the " + team2 + "!\n");
       document.getElementById("span" + index).appendChild(txt);
      }
     else if (Math.abs(difference) >= 5 && Math.abs(difference) <= 15)
      {
       createSpanResults(index)
       var txt = document.createTextNode(team1 + " " + "lost " + score1+"-"+score2+" against the " + team2 + "!\n");
       document.getElementById("span" + index).appendChild(txt);
      }
    }
 document.getElementById("span" + index).write;
}

function keyPlayers(index)
 {
  var team1=teams[searchteam];
  if (team1 == "Bulls")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Derrick Rose, Luol Deng, Carlos Boozer, Rip Hamilton, Joakim Noah\n");
    document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Celtics" || team1=="Celts")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Paul Pierce, Ray Allen, Rajon Rondo, Kevin Garnett\n");
    document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Nets")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Kris Humphries, Deron Williams, DeShawn Stevenson, Brook Lopez\n");
    document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Knicks")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Carmello Anthony, Amare Stoudemire, Jeremy Lin, Tyson Chandler\n");
    document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "76ers")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Elton Brand, Andre Iguodola, Jrue Holliday, Thaddeus Young\n");
    document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Raptors")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Andrea Bargnani, Leandro Barbosa, Jose Calderon, DeMar Derozan\n");
    document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   } 
  else if (team1 == "Warriors")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Monta Ellis, Steph Curry, David Lee, Andris Biedrins \n");
    document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Clippers")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Blake Griffin, Chris Paul, Kenyon Martin, Chauncey Billips, Caron Butler\n");
    document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Lakers")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Kobe Bryant, Pau Gasol, Andrew Bynum, Derek Fisher, Luke Walton\n");
    document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Suns")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Steve Nash, Channing Frye, Robin Lopez, Josh Childress\n");
    document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Kings")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Tyreke Evans, Jimmer Fredette, John Salmons, DeMarcus Cousins, Marcus Thornton\n");
    document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Cavaliers" || team1=="Cavs")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Kyrie Irving, Antawn Jamison, Anderson Varejao, Tristan Thompson\n");
    document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Pistons")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Ben Gordon, Tayshaun Prince, Charlie Villanueva, Ben Wallace, Brandon Knight\n");
    document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Pacers")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Tyler Hansbrough, David West, Danny Granger\n");
    document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Bucks")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Brandon Jennings, Stephen Jackson, Andrew Bogut, Beno Udrih, Drew Gooden\n");
    document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Mavericks" || team1=="Mavs")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Dirk Nowitzki, Jason Terry, Jason Kidd, Lamar Odom, Shawn Marion\n");
    document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Rockets")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Kevin Martin, Luis Scola, Samuel Dalembert, Hasheem Thabeet, Kyle Lowry\n");
      document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Grizzlies")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Rudy Gay, O.J. Mayo, Zach Randolph, Mike Conley, Marc Gasol\n");
      document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Hornets")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Chris Kaman, Emeka Okafor, Jarrett Jack, Carl Landry, Trevor Ariza\n");
      document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Spurs")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Tim Duncan, Tony Parker, Manu Ginobili, Richard Jefferson, DeJuan Blair\n");
     document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Hawks")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Joe Johnson, Al Horford, Josh Smith, Kirk Hinrich, Jeff Teague\n");
      document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Bobcats")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Cory Maggette, Boris Diaw, Kemba Walker, D.J. Augustin, Tyrus Thomas\n");
      document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Heat")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("LeBron James, Dwayne Wade, Chris Bosh, Mario Chalmers, Noris Cole, Udonis Haslem\n");
      document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Magic")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Dwight Howard, Hedo Turkoglu, Jason Richardson, Jameer Nelson, J.J. Reddick\n");
      document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Wizards")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("John Wall, Rashard Lewis, Andray Blatche, JaVale McGee, Nick Young\n");
      document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Nuggets")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Nene Hilario, Aaron Afflalo, Rudy Fernandez, Danillo Gallinari, Andre Miller\n");
      document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Timberwolves" || team1=="Wolves")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Kevin Love, Ricky Rubio, Michael Beasley, Darko Milicic, Jose Barea\n");
      document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Thunder")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Kevin Durant, Russell Westbrook, James Harden, Serge Ibaka, Thabo Sefolosha\n");
    document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Trail Blazers" || team1=="Blazers")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Gerald Wallace, Greg Oden, LaMarcus Aldridge, Marcus Camby, Wesley Matthews\n");
      document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else if (team1 == "Jazz")
   {
    createSpanKeyPlayers(index)
    var txt = document.createTextNode("Al Jefferson, Devin Harris, Paul Millsap, Gordon Hayward, Enes Kanter\n");
      document.getElementById("spanKeyPlayers" + index).appendChild(txt);
   }
  else
  {
    alert("Must be an actual team")
  }
  //txt=txt+'\n';
  //document.getElementById("spanKeyPlayers" + index).appendChild(txt);
  document.getElementById("spanKeyPlayers" + index).write;
 }
/*var sport = "basketball";
var team1 = "Chicago Bulls";
var team2 = "Milwaukee Bucks";


/*****************************NEW CODE******************************************/
function createSpanKeyFacts(index)
    {
        var spanTagKeyFacts = document.createElement("span");
       
        spanTagKeyFacts.id = "spanKeyFacts" + index;

        spanTagKeyFacts.className ="keyFacts";

        document.getElementById("content").appendChild(spanTagKeyFacts);
    }


function keyFacts(index)
 {
  var team1=teams[searchteam];
  if (team1 == "Bulls")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Derrick Rose Reigning 2011 MVP\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if ((team1 == "Mavericks") || (team1 == "Mavs"))
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Mavericks are 2011 NBA Champions\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
 else if (team1 == "Pistons")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Pistons Win 4th Straight\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
 else if ((team1 == "Cavaliers") || (team1 == "Cavs"))
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Kyrie Irving 1st Pick Overall 2011 NBA Draft\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
 else if (team1 == "Pacers")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Roy Hibbert is a 2012 NBA All-Star\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
 else if (team1 == "Bucks")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Brandon Jennings Eyes Free Agency in 2014\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Rockets")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Houston to Host 2012 NBA All-Star Game\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Grizzlies")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Marc Gasol is a 2012 NBA All-Star\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Hornets")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Hornets 8 Game Losing Streak Continues\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Spurs")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Tony Parker is a 2012 NBA All-Star\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if ((team1 == "Celtics") || (team1 == "Celts"))
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Paul Pierce Passes Larry Bird on Celtics All-Time Scoring List\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Nets")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Deron Williams is a 2012 NBA All-Star\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Knicks")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Jeremy Lin emerges as Nicks Phenom\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "76ers")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Andre Iguodola is a 2012 NBA All-Star\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Raptors")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Andrea Bargnani misses 14th Game with Calf Injury\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Nuggets")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Danillo Gallinari out with Injury\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if ((team1 == "Timberwolves") || (team1 == "Wolves"))
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Kevin Love is a 2012 NBA All-Star\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Blazers" || team1=="Trail Blazers")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("LaMarcus Aldredge is a 2012 NBA All-Star\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Thunder")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Russell Westbrook and Kevin Durant are 2012 NBA All-Stars\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Jazz")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Gordon Hayward to Play in 2012 NBA Rising-Star Challenge\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Hawks")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Joe Johnson is a 2012 NBA All-Star\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Bobcats")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Kemba Walker to Play in 2012 NBA Rising-Star Challenge\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Heat")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Miami Heat move on from 2011 NBA Finals Loss\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Magic")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Dwight Howard Hopes to be Traded\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Wizards")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("John Wall to Play in 2012 NBA Rising-Star Challenge\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Warriors")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Steph Curry injures Surgically Repaired Ankle\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Clippers")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Blake Griffin to Play in 2012 NBA Rising-Star Challenge\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Lakers")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Kobe Bryant is a 2012 NBA All-Star\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Suns")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("Steve Nash is a 2012 NBA All-Star\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  else if (team1 == "Kings")
   {
    createSpanKeyFacts(index)
    var txt = document.createTextNode("DeMarcus Cousins to Plays in 2012 NBA Rising-Star Challenge\n");
    document.getElementById("spanKeyFacts" + index).appendChild(txt);
   }
  document.getElementById("spanKeyFacts" + index).write;
 }