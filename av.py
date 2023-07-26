import py_avataaars as pa

avatar = pa.PyAvataaar(style=pa.AvatarStyle.CIRCLE,
    mouth_type=pa.MouthType.SMILE,
    eye_type=pa.EyesType.SQUINT,
    nose_type=pa.NoseType.DEFAULT,
    eyebrow_type=pa.EyebrowType.DEFAULT,
    accessories_type=pa.AccessoriesType.DEFAULT,
    clothe_type=pa.ClotheType.COLLAR_SWEATER,
    clothe_color=pa.Color.BLUE_03,
    clothe_graphic_type=pa.ClotheGraphicType.BAT,
    skin_color=pa.SkinColor.BROWN,
    hair_color=pa.HairColor.BROWN_DARK,
    facial_hair_type=pa.FacialHairType.DEFAULT,
    facial_hair_color=pa.HairColor.BROWN_DARK,
    top_type=pa.TopType.SHORT_HAIR_SHAGGY_MULLET,
    )
avatar.render_png_file('avat.png')
