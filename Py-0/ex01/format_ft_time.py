import datetime

t_start = datetime.datetime(1970, 1, 1, 0, 0)
t_end = datetime.datetime.now()

nb = (t_end-t_start).total_seconds()
# nb_s = str(nb)
# nb_length = str(nb).index('.')
# nb_modu3 = str(nb).index('.') % 3

# if (nb_modu3 == 0) : 
#     nb_modu3 = 3

# count = 0

# while (nb_length > 3) :
    
#     if (count == 0) :
#         nb_s = nb_s[:nb_modu3] + ',' + nb_s[nb_modu3:] 
#         nb_length -= nb_modu3
#         count += nb_modu3 + 1
#         continue

#     count += 3 
#     nb_s = nb_s[:count] + ',' + nb_s[count:]
#     count += 1
#     nb_length -= 3


# print("Seconds since January 1, 1970:", nb_s, "or", f"{nb:.2e}", "in scientific notation")
# print(t_end.strftime("%b %d %Y"))

print("Seconds since January 1, 1970:", f"{nb:,.4f}", "or", f"{nb:.2e}", "in scientific notation")
print(t_end.strftime("%b %d %Y"))

# 