
# // C++ program to convert binary to decimal
# #include <iostream>
# using namespace std;
 
# // Function to convert binary to decimal
# int binaryToDecimal(int n)
# {
#     int num = n;
#     int dec_value = 0;
 
#     // Initializing base value to 1, i.e 2^0
#     int base = 1;
 
#     int temp = num;
#     while (temp) {
#         int last_digit = temp % 10;
#         temp = temp / 10;
 
#         dec_value += last_digit * base;
 
#         base = base * 2;
#     }
 
#     return dec_value;
# }
 
# // Driver program to test above function
# int main()
# {
#     int num = 10101001;
 
#     cout << binaryToDecimal(num) << endl;
# }
# def binaryToDecimal(n):
#     num = n;
#     dec_value = 0;
     
#     # Initializing base
#     # value to 1, i.e 2 ^ 0
#     base = 1;
     
#     temp = num;
#     while(temp):
#         last_digit = temp % 10;
#         temp = int(temp / 10);
         
#         dec_value += last_digit * base;
#         base = base * 2;
#     return dec_value;
 
# # Driver Code
# num = 10101001;
# print(binaryToDecimal(num));
 
# def binarynum(n):
#     num=int (n)
#     dec_value = 0
#     base=1
#     temp = int(num)
#     while (temp):
#         last_digit = temp % 10
#         temp = int(temp / 10)
 
#         dec_value += last_digit * base
 
#         base = base * 2
    
 
#     return dec_value

# num=1010
# print(binarynum(num))
n = input()
 
# Convert n to base 2
s = int(n, 10)
 
print(s)