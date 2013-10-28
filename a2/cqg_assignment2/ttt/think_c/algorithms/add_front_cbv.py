question_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$x1','int'],['$y0','int'],['$y1','int'],
]

tuple_list = [
	['add_front_cbv_',
		[None,10,None],
		[None,15,None],
		[4,None,None],
		[3,None,None],	
		[None,None,None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
d	#include &lt;stdlib.h>
x	#include <stdlib.h>
dx
dx	struct node {
dx		int x;
dx		struct node * next;
dx	};
dx
dx	struct node *head;
dx
dx	int add_front(struct node* head_ptr,int x)
dx	{
dx		struct node *new;
dx
dx		// allocate and initialize a new node
dx		new = (struct node*)malloc(sizeof(struct node));
dx		if (new == NULL) {
dx			return 0;
dx		}
dx		new->x = x;
dx
dx		// link in the new node
dx		new->next = head_ptr;
dx		head_ptr = new;
dx
dx		return 1;
dx	}
'''

main_code_template = '''\
dx		int i,s0,s1;
dx		struct node *p;
dx	
dx		head = NULL;
dx	
dx		s0 = 0;
dx		for (i = 0; i < $x1; i++) {
dx			s0 += i;
dx			add_front(head,i);
dx		}
dx	
dx		s1 = 0;
dx		for (p = head; p != NULL; p = p->next) {
dx			s1 += p->x;
dx		}
dx	
dx		printf("%d\\n",s0);
dx		printf("%d\\n",s1);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
$y1
'''
