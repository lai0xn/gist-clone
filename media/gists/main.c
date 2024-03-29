#include "stdio.h"

//homework s2 student : Charfaoui Ahmed Aymen

typedef struct {
	int hours;
	int minutes;
	int seconds;
}TTime;



// sec_to_ttime takes a time in seconds and returns the equivalent ttime
TTime sec_to_ttime(int seconds){
  TTime time;
  time.hours = seconds / 3600;
  time.minutes = (seconds % 3600) / 60;
  time.seconds = (seconds % 3600) % 60;
  return time;
}

//ttime_to_sec takes a TTime type and returns the equivalent time in seconds
int ttime_to_sec(TTime time){
  return time.hours * 3600 + time.minutes * 60 + time.seconds;
}

int main() {
  //variables declaration
  
  
  TTime player_1, player_2, diff_ttime;
  int player_1_sec, player_2_sec, diff;
  
  //user input 

  //player1
  printf("What's the training time of the first player ? \n");
  printf("hours : ");
  scanf("%d",&player_1.hours);
  printf("minutes : ");
  scanf("%d",&player_1.minutes);
  printf("seconds : ");
  scanf("%d",&player_1.seconds);

  //player2  
  printf("What's the training time of the second player ? \n");
  printf("hours : ");
  scanf("%d",&player_2.hours);
  printf("minutes : ");
  scanf("%d",&player_2.minutes);
  printf("seconds : ");
  scanf("%d",&player_2.seconds);

  //connvert each time to seconds and substract them 
  diff = ttime_to_sec(player_1) - ttime_to_sec(player_2);

  // use the tenary operator to make the code shorter 
  diff = (diff > 0) ? diff : -diff;
  diff_ttime =  sec_to_ttime(diff);

  //dislayng the result
  printf("the difference is %dh %dmin %ds\n",diff_ttime.hours,diff_ttime.minutes,diff_ttime.seconds);
  
}
