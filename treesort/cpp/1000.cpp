#include <vector>
#include <iostream>
using namespace std;
struct Node
{
  int data;
  struct Node *left,*right;
};
//Function to create new Node
struct Node *newnode(int key)
{
  struct Node *temp=new Node;
  temp->data=key;
  temp->left=NULL;
  temp->right=NULL;
  return temp;
}
Node* insert(Node *node,int key)
{
  if(node==NULL) return newnode(key);//If tree is empty return new node
  if(key < node->data)
    node->left=insert(node->left,key);
  else
    node->right=insert(node->right,key);
  return node;
}
void store(Node *root,int a[],int &i)
{
  if(root!=NULL)
  {
    store(root->left,a,i);
    a[i++]=root->data;
    store(root->right,a,i);
  }
}
void TreeSort(vector<int>& a)
{
    struct Node *root = NULL;
    //Construct binary search tree
    root = insert(root, a[0]);
    for (size_t i=1; i<a.size(); i++)
        insert(root, a[i]);
    //Sorting the array using inorder traversal on BST
    int i = 0;
    store(root, a.data() , i);
}
int main()
{ 
    vector<int> a{420, 10, 118, 295, 885, 912, 335, 776, 880, 688, 532, 238, 744, 962, 652, 406, 895, 985, 98, 320, 80, 378, 283, 402, 304, 727, 750, 862, 498, 860, 40, 936, 182, 232, 384, 33, 322, 89, 423, 117, 221, 543, 876, 385, 877, 710, 200, 444, 261, 483, 246, 660, 128, 606, 861, 367, 457, 263, 141, 97, 12, 184, 669, 984, 453, 85, 737, 968, 751, 612, 93, 399, 627, 946, 151, 490, 972, 694, 927, 137, 472, 891, 621, 352, 785, 581, 415, 389, 941, 226, 391, 871, 695, 893, 663, 616, 371, 326, 963, 762, 55, 615, 205, 756, 760, 149, 851, 334, 361, 186, 54, 782, 889, 228, 267, 574, 970, 645, 979, 236, 639, 947, 27, 949, 153, 22, 76, 817, 329, 20, 179, 576, 143, 942, 673, 439, 919, 592, 243, 598, 930, 484, 210, 679, 914, 208, 840, 624, 242, 733, 870, 357, 712, 345, 120, 193, 773, 379, 894, 443, 734, 784, 50, 993, 766, 504, 114, 88, 707, 227, 313, 155, 845, 725, 897, 332, 739, 353, 735, 67, 305, 847, 995, 983, 366, 493, 355, 792, 381, 105, 479, 147, 848, 813, 657, 69, 557, 533, 92, 84, 90, 920, 666, 211, 173, 724, 625, 583, 201, 585, 372, 796, 448, 572, 380, 938, 77, 382, 780, 510, 53, 167, 636, 11, 869, 294, 909, 198, 547, 539, 365, 481, 364, 711, 761, 350, 866, 911, 287, 39, 5, 206, 622, 342, 185, 299, 716, 317, 47, 769, 859, 933, 68, 164, 277, 702, 170, 748, 31, 528, 324, 1, 247, 715, 307, 195, 718, 509, 518, 671, 579, 924, 19, 250, 506, 978, 575, 181, 655, 975, 66, 383, 703, 563, 469, 700, 580, 935, 37, 218, 499, 562, 306, 216, 145, 798, 578, 312, 906, 160, 905, 952, 620, 561, 683, 728, 850, 421, 474, 542, 154, 888, 843, 648, 468, 253, 502, 358, 123, 73, 665, 937, 534, 165, 467, 9, 4, 704, 604, 610, 981, 252, 2, 875, 96, 23, 806, 130, 723, 566, 531, 901, 466, 511, 564, 781, 81, 900, 374, 398, 811, 104, 82, 339, 732, 758, 168, 285, 831, 943, 432, 394, 708, 634, 497, 668, 844, 341, 802, 209, 759, 565, 390, 428, 21, 915, 808, 814, 112, 649, 262, 7, 163, 955, 113, 953, 503, 268, 494, 680, 348, 190, 456, 45, 308, 70, 786, 644, 951, 538, 638, 803, 956, 480, 982, 513, 793, 275, 519, 977, 442, 270, 846, 804, 175, 525, 458, 48, 157, 56, 75, 233, 127, 939, 656, 34, 136, 126, 32, 281, 922, 311, 72, 300, 140, 321, 61, 965, 691, 957, 797, 705, 599, 987, 789, 436, 997, 820, 908, 148, 729, 87, 577, 413, 63, 244, 254, 928, 721, 874, 960, 272, 83, 330, 256, 726, 292, 237, 462, 336, 488, 902, 452, 177, 79, 485, 171, 713, 522, 722, 340, 41, 156, 838, 131, 410, 526, 507, 422, 910, 594, 590, 274, 424, 630, 245, 241, 520, 567, 887, 768, 892, 258, 807, 6, 816, 755, 745, 986, 231, 197, 903, 884, 220, 351, 886, 584, 188, 746, 929, 858, 486, 257, 697, 284, 719, 301, 560, 778, 664, 183, 222, 608, 855, 328, 433, 650, 681, 821, 788, 495, 213, 176, 431, 343, 64, 492, 552, 430, 878, 646, 314, 477, 801, 122, 674, 440, 298, 667, 591, 988, 549, 670, 346, 463, 400, 595, 833, 809, 207, 354, 17, 370, 434, 101, 647, 872, 601, 632, 333, 426, 158, 51, 235, 611, 356, 548, 174, 521, 132, 135, 418, 832, 293, 377, 248, 842, 623, 251, 491, 961, 58, 44, 863, 810, 736, 849, 537, 692, 144, 464, 28, 626, 461, 172, 325, 618, 290, 822, 753, 999, 589, 827, 587, 230, 812, 783, 662, 59, 921, 556, 95, 690, 279, 119, 180, 265, 553, 74, 60, 605, 864, 805, 487, 642, 678, 841, 752, 651, 687, 454, 945, 989, 558, 600, 259, 393, 482, 554, 401, 204, 550, 596, 416, 35, 882, 613, 396, 659, 71, 309, 948, 412, 437, 835, 918, 570, 741, 973, 337, 203, 125, 536, 992, 108, 111, 30, 742, 868, 255, 818, 3, 940, 273, 991, 535, 14, 676, 515, 362, 323, 286, 765, 836, 169, 730, 26, 706, 278, 386, 971, 212, 429, 643, 202, 637, 451, 24, 631, 571, 271, 214, 505, 852, 925, 609, 749, 166, 373, 602, 29, 950, 404, 559, 958, 501, 368, 302, 512, 0, 834, 824, 764, 395, 954, 234, 86, 774, 597, 146, 588, 489, 686, 516, 628, 815, 121, 100, 161, 825, 857, 932, 478, 107, 138, 142, 677, 344, 476, 856, 445, 327, 672, 249, 405, 586, 641, 980, 99, 926, 473, 331, 408, 790, 795, 508, 568, 376, 819, 916, 923, 865, 675, 65, 194, 738, 913, 740, 459, 223, 310, 62, 839, 854, 199, 196, 967, 441, 829, 57, 614, 417, 470, 8, 103, 896, 449, 883, 899, 52, 91, 303, 698, 990, 369, 49, 545, 757, 116, 291, 316, 460, 189, 994, 282, 500, 359, 42, 523, 387, 907, 349, 529, 78, 438, 770, 109, 661, 13, 633, 224, 162, 573, 338, 403, 375, 134, 689, 475, 260, 799, 446, 791, 397, 779, 881, 392, 139, 496, 582, 269, 465, 701, 102, 315, 593, 25, 998, 363, 217, 288, 823, 427, 514, 969, 38, 867, 36, 551, 763, 43, 684, 966, 517, 419, 110, 635, 693, 944, 787, 152, 46, 360, 16, 318, 540, 225, 996, 853, 617, 115, 654, 471, 931, 974, 777, 447, 15, 414, 524, 133, 276, 619, 280, 830, 904, 18, 106, 714, 229, 178, 717, 629, 129, 239, 219, 450, 837, 685, 240, 873, 682, 541, 266, 794, 150, 527, 411, 607, 407, 771, 455, 124, 215, 767, 720, 435, 976, 775, 743, 191, 709, 772, 696, 603, 425, 731, 319, 658, 747, 546, 800, 264, 187, 754, 544, 94, 959, 934, 289, 296, 530, 699, 555, 653, 917, 964, 192, 347, 159, 569, 640, 898, 297, 388, 826, 879, 828, 409, 890
};
    TreeSort(a); 
    cout<<"The sorted array is :\n";
    //Printing the sorted array
    for(size_t i=0;i<a.size();i++)
    {
      cout<<a[i]<<" ";
    }
    return 0;
}