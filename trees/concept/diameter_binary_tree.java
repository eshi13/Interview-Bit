int diameter2(TreeNode t, int* height)  
{  
    int lh = 0, rh = 0;  
    int leftD = 0, rightD = 0;  
   
    if(t == NULL)  
    {  
        *height = 0;  
        return 0; /* diameter is also 0 */  
    }  
   
    leftD = diameter2(root->left, &lh);  
    rightD = diameter2(root->right,&rh);  
   
    /* Height of current node is max of heights of left and 
    right subtrees plus 1*/  
    *height = max(lh, rh) + 1;  
   
    return max(lh + rh + 1, leftD, rightD);  
}  
/* Find diameter of binary tree 
    O(N)
*/