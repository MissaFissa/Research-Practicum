import data

NA = 0.39
n_IL = 1.33
n_air = 1.0

df200 = data.df_200
df400 = data.df_400
dict200 = data.dict_200
dict400 = data.dict_400
info200 = data.info_200
info400 = data.info_400

t200 = list(info200.iloc[0])
t400 = list(info400.iloc[0])

print(t200)
print(t400)

wavelengths = df400[dict400[0]]

fresnel_200_5ms_0deg = df200[dict200[3]]
fresnel_200_5ms_0deg_dark = df200[dict200[4]]
fresnel_200_1400ms_15deg = df200[dict200[1]]
fresnel_200_1400ms_15deg_dark = df200[dict200[2]]

fresnel_400_6ms_0deg = df400[dict400[3]]
fresnel_400_6ms_0deg_dark = df400[dict400[4]]
fresnel_400_280ms_15deg = df400[dict400[1]]
fresnel_400_280ms_15deg_dark = df400[dict400[2]]

water_200_73ms_0deg = df200[dict200[11]]
water_200_73ms_0deg_dark = df200[dict200[12]]
water_200_1600ms_15deg = df200[dict200[9]]
water_200_1600ms_15deg_dark = df200[dict200[10]]

water_400_107ms_0deg = df400[dict400[9]]
water_400_107ms_0deg_dark = df400[dict400[10]]
water_400_2000ms_15deg = df400[dict400[11]]
water_400_2000ms_15deg_dark = df400[dict400[12]]

IL_200_5ms_0deg = df200[dict200[7]]
IL_200_5ms_0deg_dark = df200[dict200[8]]
IL_200_5ms_15deg = df200[dict200[5]]
IL_200_5ms_15deg_dark = df200[dict200[6]]

IL_400_6ms_0deg = df400[dict400[7]]
IL_400_6ms_0deg_dark = df400[dict400[8]]
IL_400_6ms_15deg = df400[dict400[5]]
IL_400_6ms_15deg_dark = df400[dict400[6]]

def eta_lim(n_sample):

    return (NA / n_sample) ** 2

def refraction(R_ref, I_sample, I_sample_back, I_ref, I_ref_back):

    return R_ref * ((I_sample - I_sample_back) / I_ref - I_ref_back)

eta_lim_air = eta_lim(n_air)
eta_lim_IL = eta_lim(n_IL)

# for i in range(1,13):

