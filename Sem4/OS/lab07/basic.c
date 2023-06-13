#include<time.h>
#include<stdio.h>

int main() {
	time_t t = time(NULL);
	struct tm now = *localtime(&t);

	printf("Date -- %d/%d/%d",now.tm_mday, now.tm_mon+1, now.tm_year+1900);
	printf("\nTime -- %d:%d:%d",now.tm_hour, now.tm_min, now.tm_sec);

	printf("\n");
	return 0;
}
