#include <sys/time.h>

#define init_timer struct timeval tim; double tim1, t1

#define gtod gettimeofday(&tim, NULL)
#define fetch_time tim.tv_sec+(tim.tv_usec/1000000.0)

#define first_step_timer gtod; t1=fetch_time
#define second_step_timer gtod; tim1=(double)(fetch_time-t1)

#define print_time(s) printf("%s:=%lf;\n", s, tim1)
#define print_time_notln(s) printf("%s:=%lf;\t", s, tim1)
#define print_time_to_plot printf("%lf\t", tim1)
