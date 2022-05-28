/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
    int t = 0;  //total elements counter
    ListNode* save = head;
    ListNode* ans = head;
        ListNode* temp = head;
        
    // calculating total number of nodes
        while(head->next != NULL){
        cout<<head->val;
        head = head->next;   
        t++; 
    }
     
    t = t+1; // finializing total number of element as last node would point to null    
    cout<<"\n";
    int pos = t - n;
    cout<<pos<<"\n";
    int ctr = 0 ;
    if(pos == 0){ // if there are less than 3 nodes
        cout<<ans->val;
        cout<<"Here";
        return ans->next;
    }
    
    while(save->next != NULL)
    {
         ctr++;
        if (ctr == pos){   //if the pointer at pos-1 
           temp = save->next; //hold the address of the next node in the temp var
            save->next = temp->next; // assign the adress held by the temp in the original ptr
            cout<<save->val;
            break; //break the loop
        }
          
        save = save->next;
    }
        
   return ans;
    }
};

/*
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

*/
