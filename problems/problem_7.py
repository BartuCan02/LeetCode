def reverse(x: int) -> int:
        """
        Given a signed 32-bit integer x, return x with its digits reversed.
         If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
        """

        if x > 0:
            x = str(x)
            x_reversed = x[::-1]
            if x_reversed[0] == "0":
                return 0 if int(x_reversed) > 2**31 - 1 else int(x_reversed[1:])
            else:
                 return 0 if int(x_reversed) > 2**31 - 1 else int(x_reversed)
        elif x < 0:
             x = str(x)
             x = x[1:]
             x_reversed = x[::-1]
             if x_reversed[0] == "0":
                  return 0 if -2**31 > -int(x_reversed[1:]) < 2**31 - 1 else -int(x_reversed[1:])
             else:
                  return 0 if -2**31 > -int(x_reversed) else -int(x_reversed)
        else:
             return x
            

      

print(reverse(x=123))
print(reverse(x=-123))
print(reverse(x=120))