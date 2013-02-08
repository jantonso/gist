#include <assert.h>
#include <limits.h>
#include <stdlib.h>
#include <signal.h>

#include "lib/xalloc.h"
#include "lib/contracts.h"
#include "lib/stacks.h"

#include "include/bare.h"
#include "c0vm.h"
#include "c0vm_c0ffi.h"

/* call stack frames */
typedef struct frame * frame;
struct frame {
    c0_value *V; /* local variables */
    stack S;     /* operand stack */
    ubyte *P;    /* function body */
    size_t pc;      /* return address */
};

/* functions for handling errors */
void c0_memory_error(char *err) {
    fprintf(stderr, "Memory error: %s\n", err);
    raise(SIGUSR1);
}

void c0_division_error(char *err) {
    fprintf(stderr, "Division error: %s\n", err);
    raise(SIGUSR2);
}

/* TODO: implement execute function */
int execute(struct bc0_file *bc0) {

  /* Variables used for bytecode interpreter. You will need to initialize
     these appropriately. */

  /* callStack to hold frames when functions are called */
  stack callStack = stack_new();
  (void) callStack;
  /* initial program is the "main" function, function 0 (which must exist) */
  struct function_info main_fn = bc0->function_pool[0];
  /* array to hold local variables for function */
  c0_value *V = xcalloc((uint32_t)main_fn.num_vars,sizeof(c0_value));
  (void) V;
  /* stack for operands for computations */
  stack S = stack_new();
  /* array of (unsigned) bytes that make up the program */
  ubyte *P = main_fn.code;
  /* program counter that holds "address" of next bytecode to interpret from
     program P */
  size_t pc = 0;

  while (true) {
   //printf("current opcode: %d, current pc: %d \n",(int)P[pc],(int)pc);

#ifdef DEBUG
   printf("Executing opcode %x  --- Operand stack size: %zu\n",
        P[pc], stack_size(S));
#endif

    switch (P[pc]) {

        /* GENERAL INSTRUCTIONS: Implement the following cases for each of the
           possible bytecodes.  Read the instructions in the assignment to see
           how far you should go before you test your code at each stage.  Do
           not try to write all of the code below at once!  Remember to update
           the program counter (pc) for each case, depending on the number of
           bytes needed for each bytecode operation.  See PROG_HINTS.txt for
           a few more hints.

           IMPORTANT NOTE: For each case, the case should end with a break
           statement to prevent the execution from continuing on into the
           next case.  See the POP case for an example.  To introduce new
           local variables in a case, use curly braces to create a new block.
           See the DUP case for an example.

           See C_IDIOMS.txt for further information on idioms you may find
           useful.
        */

      /* Additional stack operation: */

      case POP: 
        {
          pc++;
          pop(S);
          break;
        }

      case DUP: 
        {
          pc++;
          c0_value v = pop(S);
          push(S,v);
          push(S,v);
          break;
        }

      case SWAP: 
	{
	  pc++;
	  c0_value v2 = pop(S);
	  c0_value v1 = pop(S);
	  push(S,v2);
	  push(S,v1);
	  break;
	}

       /* Arithmetic and Logical operations */

      case IADD:
	{
	  pc++;
	  void* y = VAL(pop(S));
	  void* x = VAL(pop(S));
	  uint32_t sum = (uint32_t)INT(x) + (uint32_t)INT(y);
	  push(S,VAL((int32_t)sum));
	  break;
	}

      case ISUB:
	{
          pc++;
          void* y = VAL(pop(S));
          void* x = VAL(pop(S));
	  uint32_t result = (uint32_t)INT(x) - (uint32_t)INT(y);
	  push(S,VAL((int32_t)result));
	  break;
	}

      case IMUL:
	{
          pc++;
          void* y = VAL(pop(S));
          void* x = VAL(pop(S));
	  uint32_t product = (uint32_t)INT(x) * (uint32_t)INT(y);
	  push(S,VAL((int32_t)product));
	  break;	
	}

      case IDIV:
	{
          pc++;
          void* y = VAL(pop(S));
          void* x = VAL(pop(S));
	  if ((INT(y) == (int32_t)0) || ((INT(x) == (int32_t)0x80000000) && (INT(y) == (int32_t)-1)))
	      c0_division_error("Results in Overflow!");
	  int32_t result = (int32_t)INT(x) / (int32_t)INT(y);
	  push(S,VAL(result));
	  break;	  
	}

      case IREM:
	{
          pc++;
          void* y = VAL(pop(S));
          void* x = VAL(pop(S));
	  if ((INT(y) == (int32_t)0) || ((INT(x) == (int32_t)0x80000000) && (INT(y) == (int32_t)-1)))
              c0_division_error("Results in Overflow!");
	  int32_t result = (int32_t)INT(x) % (int32_t)INT(y);
	  push(S,VAL(result));
	  break;
	}

      case IAND:
	{
          pc++;
          void* y = VAL(pop(S));
          void* x = VAL(pop(S));
          uint32_t result = (uint32_t)INT(x) & (uint32_t)INT(y);
	  push(S,VAL((int32_t)result));
	  break;
	}

      case IOR:
	{
          pc++;
          void* y = VAL(pop(S));
          void* x = VAL(pop(S));
	  uint32_t result = (uint32_t)INT(x) | (uint32_t)INT(y);
	  push(S,VAL((int32_t)result));
	  break;
	}

      case IXOR:
	{
          pc++;
          void* y = VAL(pop(S));
          void* x = VAL(pop(S));
	  uint32_t result = (uint32_t)INT(x) ^ (uint32_t)INT(y);
	  push(S,VAL((int32_t)result));
	  break;
	}

      case ISHL:
	{
          pc++;
          void* y = VAL(pop(S));
          void* x = VAL(pop(S));
	  uint32_t result = (uint32_t)INT(x) << ((uint32_t)INT(y) & 0x1F);
	  push(S,VAL((int32_t)result));
	  break;
        }

      case ISHR:
	{
          pc++;
          void* y = VAL(pop(S));
          void* x = VAL(pop(S));
	  int32_t result = INT(x) >> ((uint32_t)INT(y) & 0x1F);
	  push(S,VAL((int32_t)result));
	  break;
	}

      /* Pushing small constants */

      case BIPUSH:
	{
	  pc++;
          int32_t x = (int8_t)P[pc];
	  push(S,VAL(x));
	  pc++;
	  break;
	}

      /* Returning from a function */

      case RETURN:
	{
	  /*
	  free(V);
	  pc++;
	  ASSERT(!stack_empty(S));
          void* result = VAL(pop(S));	
	  stack_free(S,&free);
	  return INT(result);
	  */
	  if (stack_empty(callStack)){
	      free(V);
	      stack_free(callStack,NULL);
	      pc++;
	      ASSERT(!stack_empty(S));
	      void* result = VAL(pop(S));
	      stack_free(S,NULL);
	      return INT(result);
	  } else {
		bool bool_push = false;
		c0_value temp_value = NULL;
		if (!stack_empty(S)){
		    temp_value = pop(S);
		    bool_push = true;
		}
		stack_free(S,NULL);
		free(V);
	        frame temp_frame = (frame)pop(callStack);
	        ASSERT(temp_frame != NULL);
	        pc = temp_frame->pc;
	        V = temp_frame->V;
	        S = temp_frame->S;
		P = temp_frame->P;
		free(temp_frame);
		V = V;
		push(S,temp_value);
		if (bool_push == false){
		    pop(S);
		}
	    }
	  break;
	}

      /* Operations on local variables */

      case VLOAD:
	{
	  pc++;
	  c0_value v = V[P[pc]];
	  push(S,v);
	  pc++;
	  break;
	}

      case VSTORE:
	{
	  pc++;
	  void* v = VAL(pop(S));
	  V[P[pc]] = v;
	  pc++;
	  break;
	}

      case ACONST_NULL:
	{
	  pc++;
	  push(S,NULL);
	  break;
	}

      case ILDC:
	{
	  pc++;
	  uint32_t c1 = (uint32_t)P[pc];
	  pc++;
	  uint32_t c2 = (uint32_t)P[pc];
	  pc++;
	  int32_t x = (int)(bc0->int_pool[(c1<<8) | c2]);
	  push(S,VAL(x));
	  break;
	}

      case ALDC:
	{
	  pc++;
	  uint32_t c1 = (uint32_t)P[pc];
          pc++;
          uint32_t c2 = (uint32_t)P[pc];
          pc++;
	  void* a = &((bc0->string_pool)[(c1<<8) | c2]);
	  push(S,a);	
	  break;
	}

      /* Control flow operations */

      case NOP:
	{
	  pc++;
	  break;
	}

      case IF_CMPEQ:
	{
	  size_t index = pc + 1;
	  c0_value v2 = pop(S);
          c0_value v1 = pop(S);
	  if (v1 == v2){
	    int32_t o1 = (int32_t)P[index];
	    index++;
	    int32_t o2 = (int32_t)P[index];
	    pc = pc + (int16_t)((o1<<8) | o2);
	  } else {pc = pc + 3;}
	  break;
	}

      case IF_CMPNE:
	{
          size_t index = pc + 1;
          c0_value v2 = pop(S);
          c0_value v1 = pop(S);
          if (v1 != v2){
            int32_t o1 = (int32_t)P[index];
            index++;
            int32_t o2 = (int32_t)P[index];
            pc = pc + (int16_t)((o1<<8) | o2);
	} else {pc = pc + 3;}
          break;
        }

      case IF_ICMPLT:
	{
          size_t index = pc + 1;
          int32_t y = INT(pop(S));
          int32_t x = INT(pop(S));
	  if (x < y){
            int32_t o1 = (int32_t)P[index];
            index++;
            int32_t o2 = (int32_t)P[index];
            pc = pc + (int16_t)((o1<<8) | o2);
          } else {pc = pc + 3;}
          break;
        }

      case IF_ICMPGE:
	{
          size_t index = pc + 1;
          int32_t y = INT(pop(S));
          int32_t x = INT(pop(S));
          if (x >= y){
            int32_t o1 = (int32_t)P[index];
            index ++;
            int32_t o2 = (int32_t)P[index];
            pc = pc + (int16_t)((o1<<8) | o2);
          } else {pc = pc + 3;}
	  break;
        }

      case IF_ICMPGT:
	{
          size_t index = pc + 1;
          int32_t y = INT(pop(S));
          int32_t x = INT(pop(S));
          if (x > y){
            int32_t o1 = (int32_t)P[index];
            index++;
            int32_t o2 = (int32_t)P[index];
            pc = pc + (int16_t)((o1<<8) | o2);
	} else {pc = pc + 3;}
          break;
        }

      case IF_ICMPLE:
	{
          size_t index = pc + 1;
          int32_t y = INT(pop(S));
          int32_t x = INT(pop(S));
	  if (x <= y){
            int32_t o1 = (int32_t)P[index];
            index ++;
            int32_t o2 = (int32_t)P[index];
	    pc = pc + (int16_t)((o1<<8) | o2);
          } else {pc = pc + 3;}
          break;
        }

      case GOTO:
	{
	  size_t index = pc + 1;
	  int32_t o1 = (int32_t)P[index];
	  index ++;
	  int32_t o2 = (int32_t)P[index];
	  pc = pc + (int16_t)((o1<<8) | o2);
	  break;
	}

      /* Function call operations: */

      case INVOKESTATIC:
	{
	  pc++;
	  uint32_t c1 = (uint32_t)P[pc];
	  pc++;
	  uint32_t c2 = (uint32_t)P[pc];
	  pc++;
	  struct function_info g = bc0->function_pool[(c1<<8) | c2];
          frame temp_frame = xmalloc(sizeof(struct frame));
	  temp_frame->pc = pc;
	  temp_frame->V = V;
	  temp_frame->S = S;
	  temp_frame->P = P;
	  push(callStack,temp_frame);
	  pc = 0;
	  c0_value * new_variable_array = xcalloc((uint32_t)g.num_vars,sizeof(c0_value));
	  uint16_t temp_num_args = g.num_args;
	  V = new_variable_array;
	  while (temp_num_args != (uint32_t)0){
	      V[temp_num_args-1] = pop(S);
	      temp_num_args = temp_num_args - 1;
	  }
	  stack new_stack = stack_new();
	  S = new_stack;
	  P = g.code;
	  break;
	}

      case INVOKENATIVE:
	{
	  pc++;
          uint32_t c1 = (uint32_t)P[pc];
          pc++;
          uint32_t c2 = (uint32_t)P[pc];
          pc++;
          struct native_info nat = bc0->native_pool[(c1<<8) | c2];
	  uint16_t num_args = nat.num_args;
	  uint16_t index = nat.function_table_index;	
	  c0_value* temp_array = xcalloc(num_args,sizeof(c0_value));
	  while (num_args != 0){
	      temp_array[num_args-1] = pop(S);
	      num_args = num_args - 1;
	  }
	  native_fn address = native_function_table[index];
	  c0_value result = (*address)(temp_array);
	  push(S,result);
	  free(temp_array);
	  break;
	}

      /* Memory allocation operations: */

      case NEW:
	{
	  pc++;
	  uint8_t s = (uint8_t)P[pc];
	  pc++;
	  void* a = xmalloc(s);
	  push(S,a);
	  break;
	}

      case NEWARRAY:
	{
	  pc++;
	  uint8_t s = (uint8_t)P[pc];
	  pc++;
	  void* n = VAL(pop(S));
	  if (((int32_t)INT(n)) < 0)
	      c0_memory_error("Allocating negative size array!");
	  struct c0_array *a = xcalloc((uint32_t)(INT(n)), sizeof(struct c0_array) + (s*(uint32_t)(INT(n))));
	  a->count = (uint32_t)(INT(n));
	  a->elt_size = s;
	  push(S,a);
	  break;
	}

      case ARRAYLENGTH:
	{
	  pc++;
	  struct c0_array *a = VAL(pop(S));
	  uint32_t length = (uint32_t)(a->count);
	  push(S,VAL(length));
	  break;
	}

      /* Memory access operations: */

      case AADDF:
	{
	  pc++;
	  uint8_t f = (uint8_t)P[pc];
	  char* a = (char*)(pop(S));
	  if (a == NULL)
	    c0_memory_error("Memory Error!");
	  push(S,(void*)(a+f));
	  pc++;
	  break;
	}

      case AADDS:
	{
	  pc++;
	  int32_t index = (int32_t)INT(pop(S));
	  struct c0_array *a = VAL(pop(S));
	  if (a == NULL)
	    c0_memory_error("Memory Error!");
	  if (!(0 <= index && index < (a->count)))
	    c0_memory_error("Memory Error!");
	  void* address = &(a->elems[a->elt_size*index]);
	  push(S,address);
	  break;
	}

      case IMLOAD:
	{
	  pc++;
	  void* a = VAL(pop(S));
	  if (a == NULL)
	    c0_memory_error("Memory Error!");
	  int32_t x = *((int*)a);
	  push(S,VAL(x));
	  break;
	}

      case IMSTORE:
	{
	  pc++;
	  int32_t x = INT(pop(S));
	  void* a = VAL(pop(S));
	  if (a == NULL)
	    c0_memory_error("Memory Error!");
	  *((int*)a) = x;
	  break;
	}

      case AMLOAD:
	{
          pc++;
          void* a = VAL(pop(S));
          if (a == NULL)
            c0_memory_error("Memory Error!");
	  void* b = &(*((char*)a));
          push(S,b);
          break;
        } 

      case AMSTORE:
	{
	  pc++;
	  void* b = VAL(pop(S));
	  void* a = VAL(pop(S));
	  if (a == NULL)
	    c0_memory_error("Memory Error!");
	  *((char*)a) = *((char*)b);
	  break;
	}

      case CMLOAD:
	{
	  pc++;
	  char* a = (char*)VAL(pop(S));
	  if (a == NULL)
	    c0_memory_error("Memory Error!");
	  int32_t x = (int32_t)(*a);
	  push(S,VAL(x));
	  break;
	}

      case CMSTORE:
	{
	  pc++;
	  int32_t x = INT(pop(S));
	  char* a = (char*)VAL(pop(S));
	  if (a == NULL)
	    c0_memory_error("Memory Error!");
	  *a = (x & 0x7f);
	  break;
	}

      default:
        fprintf(stderr, "invalid opcode: 0x%02x\n", P[pc]);
        abort();
    }
  }

  /* cannot get here from infinite loop */
  assert(false);
}

