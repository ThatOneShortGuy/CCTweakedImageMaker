local monitor = peripheral.find("monitor")
monitor.setTextScale(0.5)
local letters = string.rep(" ", 100)
local letterColors = string.rep("0", 100)
monitor.setPaletteColor(1, 0x1a1334)
monitor.setPaletteColor(2, 0xa1a0a9)
monitor.setPaletteColor(4, 0xf8ea9a)
monitor.setPaletteColor(8, 0x796151)
monitor.setPaletteColor(16, 0x281c47)
monitor.setPaletteColor(32, 0x5c2c28)
monitor.setPaletteColor(64, 0xcfbc84)
monitor.setPaletteColor(128, 0x48197b)
monitor.setPaletteColor(256, 0x4a4251)
monitor.setPaletteColor(512, 0x34181a)
monitor.setPaletteColor(1024, 0x808192)
monitor.setPaletteColor(2048, 0xfbf5dc)
monitor.setPaletteColor(4096, 0xa38d6a)
monitor.setPaletteColor(8192, 0x31155e)
monitor.setPaletteColor(16384, 0x63607a)
monitor.setPaletteColor(32768, 0x130d22)
monitor.setCursorPos(1, 1)
monitor.blit(letters, letterColors,"f0ff00000000008dddddddd40000040000000000000000000fffffffff00000000000ffffff000000000000000000044440f")
monitor.setCursorPos(1, 2)
monitor.blit(letters, letterColors,"f400f00000000d7dddddddd444444840000000000000f00ffffffffffffffffffffffffff40ff00000000040004d4dddd40f")
monitor.setCursorPos(1, 3)
monitor.blit(letters, letterColors,"ff00f0000044d77dddddddddd44ddd4000000000000ffffffffffffffffffff0fffffffff80ffff0000004e004d7dddddd40")
monitor.setCursorPos(1, 4)
monitor.blit(letters, letterColors,"fffff0004dd77ee8ddddddddd4e848553500000004fffff00ffffffffffffffffffffffff08ffffffff000444ddddddddd40")
monitor.setCursorPos(1, 5)
monitor.blit(letters, letterColors,"fffff000d7ea1aae77ddddddd8599553cc9f0ff0fffffff0fffffffffffff00fffffff000000fffffff000004d77ddddd40f")
monitor.setCursorPos(1, 6)
monitor.blit(letters, letterColors,"ffffff048e1bb1ae77ddddddd899955366cffffffffffffffffffffffff0800ffffff0000440fff00f00000dd777dddd40ff")
monitor.setCursorPos(1, 7)
monitor.blit(letters, letterColors,"ffffff04e1bbbbaeaed4404448ff99553623fffffffffffffffffff000008008fffff4444dd40ff0f00000d77777dd4400f0")
monitor.setCursorPos(1, 8)
monitor.blit(letters, letterColors,"0040ff08e1bbbbaaaed0000048ff995553c353cc3599fffffffff0000000004800ff0044dd440000000000dd7777d400000f")
monitor.setCursorPos(1, 9)
monitor.blit(letters, letterColors,"00000008e1bbbb8eeed004408efff995333c6263590f0000000000000000444000000444d4444000000004ddd777d0fff0ef")
monitor.setCursorPos(1, 10)
monitor.blit(letters, letterColors,"0000000de1bbb198ee85999988f9995553626388800000000000004444444448884444488444000000004ddddddd0fffffff")
monitor.setCursorPos(1, 11)
monitor.blit(letters, letterColors,"000000048a1bb199e885999fff99999953c3c2c38400000000444444404404436c888888888840000004dddddd40ffffffff")
monitor.setCursorPos(1, 12)
monitor.blit(letters, letterColors,"00000004dea11a994d4488599999999955c6bb2c84000000000000044000004c2c33cccccc3384444444dddd40ffffffffff")
monitor.setCursorPos(1, 13)
monitor.blit(letters, letterColors,"00000004488ee899f8400088338959931222222c840000000000000000000083ccc62222666c3884444444440fffffffffff")
monitor.setCursorPos(1, 14)
monitor.blit(letters, letterColors,"00000044444d8899900004486b31bb56bb222263840000f00ffff0000ff0048ccc22222222226c38844440000fffff0f0fff")
monitor.setCursorPos(1, 15)
monitor.blit(letters, letterColors,"4444444444444ff900004888623bbb3cbb2226c38444ffffffff0fffff004483c622bbbb222226c3388844000fffffffffff")
monitor.setCursorPos(1, 16)
monitor.blit(letters, letterColors,"444ed4dd44444ff9f4444448c6ccbb5cbbb26c388400ffffffff0ffff004488c622bbbbbbb2222666c3388884400ffffffff")
monitor.setCursorPos(1, 17)
monitor.blit(letters, letterColors,"44d8d4dd4440ff99444444888cc3bbccbbb2c388440000fffff0fff0440483c622bbbbbbbbb22222226cccc3388400000000")
monitor.setCursorPos(1, 18)
monitor.blit(letters, letterColors,"8ddd4444440ffff90444444483c62bb22b2235844440000fff4894833383c6622bbbbbbbbbbbbbbb2222222266c333400000")
monitor.setCursorPos(1, 19)
monitor.blit(letters, letterColors,"ddddd444444fff99488444448833622226c3c6c5444444440f498838333ac6222bbbbbbbbbbbbbbb22222222266cc3400000")
monitor.setCursorPos(1, 20)
monitor.blit(letters, letterColors,"ddddddd4d44fff99988844444488562bc5536cc59444488440983838333c16222bbbbbbbbbbbbb222226666c338840000000")
monitor.setCursorPos(1, 21)
monitor.blit(letters, letterColors,"ddddd444dd44953cc3e88444408353c35553536cc5553388408888383aa162222bbbbbbbbbbb222226c33388844400000000")
monitor.setCursorPos(1, 22)
monitor.blit(letters, letterColors,"7ddd44444d88cbb22338844000855555555553366336bb63998883333333c66222bbbbbbbbb2226cc3888444400000000000")
monitor.setCursorPos(1, 23)
monitor.blit(letters, letterColors,"7ddd44444488cbb22c338440839555355555353c3562bbc95338333cc40448c6222bbbbbbb22263388400000000000000000")
monitor.setCursorPos(1, 24)
monitor.blit(letters, letterColors,"7ddd44444488c2222c33848335953355599535555562bb3553c995930044486662222bbb22226388400f0ef0000000004444")
monitor.setCursorPos(1, 25)
monitor.blit(letters, letterColors,"7dd4444444883622c5588335559955999995359995b226355539555c04444883c6222222222c3844000f04f0044dd8444444")
monitor.setCursorPos(1, 26)
monitor.blit(letters, letterColors,"77d44000444883c239333555999999999999535999c22635999559840000884483c2222222c3840000ffff044dd777dd4444")
monitor.setCursorPos(1, 27)
monitor.blit(letters, letterColors,"77dd400000448883353559999559f9ff999536699553c68999953350400044004883c666c33840000fff0044ddd777ddd8ee")
monitor.setCursorPos(1, 28)
monitor.blit(letters, letterColors,"ddd440000004488995599999555fffff9995c1c955588859959995900000000f04488333838000000000444ddd777777ea11")
monitor.setCursorPos(1, 29)
monitor.blit(letters, letterColors,"7dd440000000044899999999959fffff9955c655955944499395550000000000000444444880000004444ddddd777777ea11")
monitor.setCursorPos(1, 30)
monitor.blit(letters, letterColors,"7dddd4000000000499999ff099fffff999532c955555544999555000000000000000444440000004444ddddddd77eeaa1111")
monitor.setCursorPos(1, 31)
monitor.blit(letters, letterColors,"77ddd400000fffffffff0000fffffff99953239995555500f999000000000000000000000ff004ddddddddddddea11111111")
monitor.setCursorPos(1, 32)
monitor.blit(letters, letterColors,"77ddd400000ffffffff000fffffffff9995c65f9f59999900000000000000000000000000f004dddddddeddd7e11111111aa")
monitor.setCursorPos(1, 33)
monitor.blit(letters, letterColors,"777ddd400000fffffffffffffffff9999556c900000000000000000f44000000000044d4004ddddddddd7dd7a11111111aaa")
monitor.setCursorPos(1, 34)
monitor.blit(letters, letterColors,"77777dd40000000ff0ff04fff493c3f995563000000000000000000000000000ff04dddd444ddddddddddd7a11111111aaaa")
monitor.setCursorPos(1, 35)
monitor.blit(letters, letterColors,"777777dd4400000000489ffff0e268f995369000000000ffffff0f00000040000004dd7dddddd777ddddd7e111111aaaaaaa")
monitor.setCursorPos(1, 36)
monitor.blit(letters, letterColors,"77777ddd44000000085fffff0cc8ff9995cc5000000000ff0fffff0000044044444ddd777ddddd777ddddea1111aaaaaaaaa")
monitor.setCursorPos(1, 37)
monitor.blit(letters, letterColors,"7777777ddd44444485f99fff40fffff995cc30404400000f00ffff000044444ddddddd7771addddd77dd7ea111aaaaaaeaaa")
monitor.setCursorPos(1, 38)
monitor.blit(letters, letterColors,"d777777777dd444489f999fffffffff953c654444400ffffffffff0004444dddddddd77771addddddddd7ea111aaaaaeeeae")
monitor.setCursorPos(1, 39)
monitor.blit(letters, letterColors,"47777777777dd44899999ffffffffff9955cc4ddd4400f08ff0ff0004ddddddd7777777777ddddddddddeea1aaaaaaaeeeee")
monitor.setCursorPos(1, 40)
monitor.blit(letters, letterColors,"ee7777777777d48899999fff009ffff99955cc4dd4440008ffff0004ddddddd7777777777ddddddddd8e111aaaaaaaeeeeee")
monitor.setCursorPos(1, 41)
monitor.blit(letters, letterColors,"aaae777d7777d83999fff99f99999fff995553c54d44440fff00004ddddd7777777777777dddd44448e1111aaaaaaaeeeeee")
monitor.setCursorPos(1, 42)
monitor.blit(letters, letterColors,"aaaee777ddddd3999ff9fff9999999999995553c34d44440004444dddd77777777777777eaaaae8d8ea1111aaaaaeeeeeeee")
monitor.setCursorPos(1, 43)
monitor.blit(letters, letterColors,"aaaaedddd4483999ff9f0444440fff9999995553354d444444d444dd77777777777777ea111111aaea11111aaaaaaaaeeee8")
monitor.setCursorPos(1, 44)
monitor.blit(letters, letterColors,"aaaae8848885999fff0ddddd444440ffff9999555554ddd8eeedddd77777777777777ea11111111aa11111aaaaaaaaaeeee8")
monitor.setCursorPos(1, 45)
monitor.blit(letters, letterColors,"aaaae84999fff9ff0dddddd4444444440f99999955554dd77ddd444d7777e7777777ea11111111aaa11111aaaaaaaaaaee88")
monitor.setCursorPos(1, 46)
monitor.blit(letters, letterColors,"aaaaaae89ffffff4ddddddd40044444440f99999999554d4553c666c8777777eeeeeea1111111aaaaa1111aaaaaaaaaeee88")
monitor.setCursorPos(1, 47)
monitor.blit(letters, letterColors,"aaaaa11ae89ff4dddddddd440f00444440f999995999555333cc333339d7ea1111aaa11111111aaaaaaa1aaaaaaaaaaeee88")
monitor.setCursorPos(1, 48)
monitor.blit(letters, letterColors,"eeeaa1111a898ddddddd44000fff0044440f99995999955555555555555ea111111aa1111111aaaaaaaaaaaaaaaaaaeee888")
monitor.setCursorPos(1, 49)
monitor.blit(letters, letterColors,"eeeaaa1111aadddddd44000fffff0004440f99999999999955959958558aa111111aaaaaa1aaaaaeeeeeaaaaaaaaaeeee888")
monitor.setCursorPos(1, 50)
monitor.blit(letters, letterColors,"88eeaaaa111ed444400000fffffff0004400f999999999955998eaaaaaaaaaaaaaaaaaaaaaaaaeeeeeeeeeeeeeeeeeee8888")
monitor.setCursorPos(1, 51)
monitor.blit(letters, letterColors,"88eeaaaaaaaaae840000ffffffffff0004000ff9999958eaaaaa1aaaaaaaaaaaaaaeeeeeaaeeeee88888eeeeeeeeee888888")
monitor.setCursorPos(1, 52)
monitor.blit(letters, letterColors,"888eeeeeeaaaaaae80fffffffffffff000000ff99998eaaaaa11aaaaaaaaaaaaaeeeeeeeeeee888888888888888888888888")
