from binarysearchtree import BinarySearchTree

#[Case #1] 
bst = BinarySearchTree()
list_nums = [-55, 60, -95, -6, 86, 51, 49, -4, 84, -98]

for elem in list_nums:
    bst.insert(elem)

bst.remove(51)
assert bst.preorder() == [-55, -95, -98, 60, -6, 49, -4, 86, 84]

bst.remove(-55)
assert bst.preorder() == [-6, -95, -98, 60, 49, -4, 86, 84]

bst.remove(-4)
assert bst.preorder() == [-6, -95, -98, 60, 49, 86, 84]

bst.remove(-98)
assert bst.preorder() == [-6, -95, 60, 49, 86, 84]

bst.remove(84)
assert bst.preorder() == [-6, -95, 60, 49, 86]

bst.remove(86)
assert bst.preorder() == [-6, -95, 60, 49]

bst.remove(60)
assert bst.preorder() == [-6, -95, 49]

bst.remove(-95)
assert bst.preorder() == [-6, 49]

bst.remove(-6)
assert bst.preorder() == [49]

bst.remove(49)
assert bst.preorder() == []

#[Case #2] 
bst = BinarySearchTree()
list_nums = [66, -38, -43, -97, -90, 70, 3, 60, 35, 69]

for elem in list_nums:
    bst.insert(elem)

bst.remove(69)
assert bst.preorder() == [66, -38, -43, -97, -90, 3, 60, 35, 70]

bst.remove(-38)
assert bst.preorder() == [66, 3, -43, -97, -90, 60, 35, 70]

bst.remove(70)
assert bst.preorder() == [66, 3, -43, -97, -90, 60, 35]

bst.remove(66)
assert bst.preorder() == [3, -43, -97, -90, 60, 35]

bst.remove(35)
assert bst.preorder() == [3, -43, -97, -90, 60]

bst.remove(3)
assert bst.preorder() == [60, -43, -97, -90]

bst.remove(-97)
assert bst.preorder() == [60, -43, -90]

bst.remove(-90)
assert bst.preorder() == [60, -43]

bst.remove(-43)
assert bst.preorder() == [60]

bst.remove(60)
assert bst.preorder() == []

#[Case #3] 
bst = BinarySearchTree()
list_nums = [-36, 14, 47, -53, -49, 65, -19, 51, 17, 89]

for elem in list_nums:
    bst.insert(elem)

bst.remove(14)
assert bst.preorder() == [-36, -53, -49, 17, -19, 47, 65, 51, 89]

bst.remove(-49)
assert bst.preorder() == [-36, -53, 17, -19, 47, 65, 51, 89]

bst.remove(17)
assert bst.preorder() == [-36, -53, 47, -19, 65, 51, 89]

bst.remove(47)
assert bst.preorder() == [-36, -53, 51, -19, 65, 89]

bst.remove(-36)
assert bst.preorder() == [-19, -53, 51, 65, 89]

bst.remove(51)
assert bst.preorder() == [-19, -53, 65, 89]

bst.remove(89)
assert bst.preorder() == [-19, -53, 65]

bst.remove(-53)
assert bst.preorder() == [-19, 65]

bst.remove(65)
assert bst.preorder() == [-19]

bst.remove(-19)
assert bst.preorder() == []

#[Case #4] 
bst = BinarySearchTree()
list_nums = [74, -50, 77, 85, -21, 47, 13, 15, 9, -70]

for elem in list_nums:
    bst.insert(elem)

bst.remove(15)
assert bst.preorder() == [74, -50, -70, -21, 47, 13, 9, 77, 85]

bst.remove(74)
assert bst.preorder() == [77, -50, -70, -21, 47, 13, 9, 85]

bst.remove(85)
assert bst.preorder() == [77, -50, -70, -21, 47, 13, 9]

bst.remove(13)
assert bst.preorder() == [77, -50, -70, -21, 47, 9]

bst.remove(9)
assert bst.preorder() == [77, -50, -70, -21, 47]

bst.remove(47)
assert bst.preorder() == [77, -50, -70, -21]

bst.remove(-50)
assert bst.preorder() == [77, -21, -70]

bst.remove(-70)
assert bst.preorder() == [77, -21]

bst.remove(77)
assert bst.preorder() == [-21]

bst.remove(-21)
assert bst.preorder() == []

#[Case #5] 
bst = BinarySearchTree()
list_nums = [70, 76, 12, 68, -96, -61, -74, -53, 45, 92]

for elem in list_nums:
    bst.insert(elem)

bst.remove(92)
assert bst.preorder() == [70, 12, -96, -61, -74, -53, 68, 45, 76]

bst.remove(70)
assert bst.preorder() == [76, 12, -96, -61, -74, -53, 68, 45]

bst.remove(12)
assert bst.preorder() == [76, 45, -96, -61, -74, -53, 68]

bst.remove(-96)
assert bst.preorder() == [76, 45, -61, -74, -53, 68]

bst.remove(-53)
assert bst.preorder() == [76, 45, -61, -74, 68]

bst.remove(68)
assert bst.preorder() == [76, 45, -61, -74]

bst.remove(45)
assert bst.preorder() == [76, -61, -74]

bst.remove(-61)
assert bst.preorder() == [76, -74]

bst.remove(76)
assert bst.preorder() == [-74]

bst.remove(-74)
assert bst.preorder() == []

#[Case #6] 
bst = BinarySearchTree()
list_nums = [98, -25, -82, 70, 28, 55, 15, -1, 3, -45]

for elem in list_nums:
    bst.insert(elem)

bst.remove(-45)
assert bst.preorder() == [98, -25, -82, 70, 28, 15, -1, 3, 55]

bst.remove(-1)
assert bst.preorder() == [98, -25, -82, 70, 28, 15, 3, 55]

bst.remove(-82)
assert bst.preorder() == [98, -25, 70, 28, 15, 3, 55]

bst.remove(3)
assert bst.preorder() == [98, -25, 70, 28, 15, 55]

bst.remove(-25)
assert bst.preorder() == [98, 70, 28, 15, 55]

bst.remove(55)
assert bst.preorder() == [98, 70, 28, 15]

bst.remove(15)
assert bst.preorder() == [98, 70, 28]

bst.remove(70)
assert bst.preorder() == [98, 28]

bst.remove(98)
assert bst.preorder() == [28]

bst.remove(28)
assert bst.preorder() == []

#[Case #7] 
bst = BinarySearchTree()
list_nums = [-67, 87, -86, -2, 0, -1, -94, 48, 96, 2]

for elem in list_nums:
    bst.insert(elem)

bst.remove(48)
assert bst.preorder() == [-67, -86, -94, 87, -2, 0, -1, 2, 96]

bst.remove(-94)
assert bst.preorder() == [-67, -86, 87, -2, 0, -1, 2, 96]

bst.remove(2)
assert bst.preorder() == [-67, -86, 87, -2, 0, -1, 96]

bst.remove(96)
assert bst.preorder() == [-67, -86, 87, -2, 0, -1]

bst.remove(0)
assert bst.preorder() == [-67, -86, 87, -2, -1]

bst.remove(-67)
assert bst.preorder() == [-2, -86, 87, -1]

bst.remove(-1)
assert bst.preorder() == [-2, -86, 87]

bst.remove(87)
assert bst.preorder() == [-2, -86]

bst.remove(-2)
assert bst.preorder() == [-86]

bst.remove(-86)
assert bst.preorder() == []

#[Case #8] 
bst = BinarySearchTree()
list_nums = [17, 89, 26, -74, -7, -62, -29, -26, -14, -39]

for elem in list_nums:
    bst.insert(elem)

bst.remove(-7)
assert bst.preorder() == [17, -74, -62, -29, -39, -26, -14, 89, 26]

bst.remove(-39)
assert bst.preorder() == [17, -74, -62, -29, -26, -14, 89, 26]

bst.remove(-26)
assert bst.preorder() == [17, -74, -62, -29, -14, 89, 26]

bst.remove(26)
assert bst.preorder() == [17, -74, -62, -29, -14, 89]

bst.remove(17)
assert bst.preorder() == [89, -74, -62, -29, -14]

bst.remove(89)
assert bst.preorder() == [-74, -62, -29, -14]

bst.remove(-14)
assert bst.preorder() == [-74, -62, -29]

bst.remove(-62)
assert bst.preorder() == [-74, -29]

bst.remove(-29)
assert bst.preorder() == [-74]

bst.remove(-74)
assert bst.preorder() == []

#[Case #9] 
bst = BinarySearchTree()
list_nums = [-69, -55, 7, 29, 44, -41, -12, 46, -2, 6]

for elem in list_nums:
    bst.insert(elem)

bst.remove(7)
assert bst.preorder() == [-69, -55, 29, -41, -12, -2, 6, 44, 46]

bst.remove(44)
assert bst.preorder() == [-69, -55, 29, -41, -12, -2, 6, 46]

bst.remove(-12)
assert bst.preorder() == [-69, -55, 29, -41, -2, 6, 46]

bst.remove(29)
assert bst.preorder() == [-69, -55, 46, -41, -2, 6]

bst.remove(-2)
assert bst.preorder() == [-69, -55, 46, -41, 6]

bst.remove(-69)
assert bst.preorder() == [-55, 46, -41, 6]

bst.remove(-55)
assert bst.preorder() == [46, -41, 6]

bst.remove(6)
assert bst.preorder() == [46, -41]

bst.remove(-41)
assert bst.preorder() == [46]

bst.remove(46)
assert bst.preorder() == []

#[Case #10] 
bst = BinarySearchTree()
list_nums = [91, 86, 62, 94, -100, 46, -44, 45, -77, -39]

for elem in list_nums:
    bst.insert(elem)

bst.remove(86)
assert bst.preorder() == [91, 62, -100, 46, -44, -77, 45, -39, 94]

bst.remove(91)
assert bst.preorder() == [94, 62, -100, 46, -44, -77, 45, -39]

bst.remove(62)
assert bst.preorder() == [94, -100, 46, -44, -77, 45, -39]

bst.remove(46)
assert bst.preorder() == [94, -100, -44, -77, 45, -39]

bst.remove(-77)
assert bst.preorder() == [94, -100, -44, 45, -39]

bst.remove(-44)
assert bst.preorder() == [94, -100, 45, -39]

bst.remove(-100)
assert bst.preorder() == [94, 45, -39]

bst.remove(45)
assert bst.preorder() == [94, -39]

bst.remove(-39)
assert bst.preorder() == [94]

bst.remove(94)
assert bst.preorder() == []

#[Case #11] 
bst = BinarySearchTree()
list_nums = [-76, -34, 35, 8, 93, -20, -36, 33, -62, -37]

for elem in list_nums:
    bst.insert(elem)

bst.remove(-34)
assert bst.preorder() == [-76, -20, -36, -62, -37, 35, 8, 33, 93]

bst.remove(-37)
assert bst.preorder() == [-76, -20, -36, -62, 35, 8, 33, 93]

bst.remove(-62)
assert bst.preorder() == [-76, -20, -36, 35, 8, 33, 93]

bst.remove(33)
assert bst.preorder() == [-76, -20, -36, 35, 8, 93]

bst.remove(-20)
assert bst.preorder() == [-76, 8, -36, 35, 93]

bst.remove(-36)
assert bst.preorder() == [-76, 8, 35, 93]

bst.remove(93)
assert bst.preorder() == [-76, 8, 35]

bst.remove(-76)
assert bst.preorder() == [8, 35]

bst.remove(8)
assert bst.preorder() == [35]

bst.remove(35)
assert bst.preorder() == []

#[Case #12] 
bst = BinarySearchTree()
list_nums = [72, -23, 2, -75, 20, -66, -49, 99, 2, -41]

for elem in list_nums:
    bst.insert(elem)

bst.remove(-49)
assert bst.preorder() == [72, -23, -75, -66, -41, 2, 20, 2, 99]

bst.remove(20)
assert bst.preorder() == [72, -23, -75, -66, -41, 2, 2, 99]

bst.remove(-41)
assert bst.preorder() == [72, -23, -75, -66, 2, 2, 99]

bst.remove(-23)
assert bst.preorder() == [72, 2, -75, -66, 2, 99]

bst.remove(-66)
assert bst.preorder() == [72, 2, -75, 2, 99]

bst.remove(2)
assert bst.preorder() == [72, 2, -75, 99]

bst.remove(99)
assert bst.preorder() == [72, 2, -75]

bst.remove(2)
assert bst.preorder() == [72, -75]

bst.remove(-75)
assert bst.preorder() == [72]

bst.remove(72)
assert bst.preorder() == []

#[Case #13] 
bst = BinarySearchTree()
list_nums = [29, 28, -24, -56, 0, -65, 12, -56, 78, -11]

for elem in list_nums:
    bst.insert(elem)

bst.remove(28)
assert bst.preorder() == [29, -24, -56, -65, -56, 0, -11, 12, 78]

bst.remove(-65)
assert bst.preorder() == [29, -24, -56, -56, 0, -11, 12, 78]

bst.remove(-56)
assert bst.preorder() == [29, -24, -56, 0, -11, 12, 78]

bst.remove(29)
assert bst.preorder() == [78, -24, -56, 0, -11, 12]

bst.remove(12)
assert bst.preorder() == [78, -24, -56, 0, -11]

bst.remove(-56)
assert bst.preorder() == [78, -24, 0, -11]

bst.remove(0)
assert bst.preorder() == [78, -24, -11]

bst.remove(-24)
assert bst.preorder() == [78, -11]

bst.remove(78)
assert bst.preorder() == [-11]

bst.remove(-11)
assert bst.preorder() == []

#[Case #14] 
bst = BinarySearchTree()
list_nums = [-11, 81, 78, -60, 38, 48, 98, -48, 49, 83]

for elem in list_nums:
    bst.insert(elem)

bst.remove(38)
assert bst.preorder() == [-11, -60, -48, 81, 78, 48, 49, 98, 83]

bst.remove(98)
assert bst.preorder() == [-11, -60, -48, 81, 78, 48, 49, 83]

bst.remove(48)
assert bst.preorder() == [-11, -60, -48, 81, 78, 49, 83]

bst.remove(-60)
assert bst.preorder() == [-11, -48, 81, 78, 49, 83]

bst.remove(-11)
assert bst.preorder() == [49, -48, 81, 78, 83]

bst.remove(-48)
assert bst.preorder() == [49, 81, 78, 83]

bst.remove(81)
assert bst.preorder() == [49, 83, 78]

bst.remove(83)
assert bst.preorder() == [49, 78]

bst.remove(49)
assert bst.preorder() == [78]

bst.remove(78)
assert bst.preorder() == []

#[Case #15] 
bst = BinarySearchTree()
list_nums = [27, -71, -28, -97, -32, 22, 69, -57, -32, -33]

for elem in list_nums:
    bst.insert(elem)

bst.remove(-97)
assert bst.preorder() == [27, -71, -28, -32, -57, -33, -32, 22, 69]

bst.remove(27)
assert bst.preorder() == [69, -71, -28, -32, -57, -33, -32, 22]

bst.remove(-32)
assert bst.preorder() == [69, -71, -28, -32, -57, -33, 22]

bst.remove(69)
assert bst.preorder() == [-71, -28, -32, -57, -33, 22]

bst.remove(22)
assert bst.preorder() == [-71, -28, -32, -57, -33]

bst.remove(-32)
assert bst.preorder() == [-71, -28, -57, -33]

bst.remove(-57)
assert bst.preorder() == [-71, -28, -33]

bst.remove(-71)
assert bst.preorder() == [-28, -33]

bst.remove(-28)
assert bst.preorder() == [-33]

bst.remove(-33)
assert bst.preorder() == []

#[Case #16] 
bst = BinarySearchTree()
list_nums = [-95, 86, 90, 5, -30, 66, 46, -98, -70, -68]

for elem in list_nums:
    bst.insert(elem)

bst.remove(66)
assert bst.preorder() == [-95, -98, 86, 5, -30, -70, -68, 46, 90]

bst.remove(-98)
assert bst.preorder() == [-95, 86, 5, -30, -70, -68, 46, 90]

bst.remove(46)
assert bst.preorder() == [-95, 86, 5, -30, -70, -68, 90]

bst.remove(5)
assert bst.preorder() == [-95, 86, -30, -70, -68, 90]

bst.remove(-95)
assert bst.preorder() == [86, -30, -70, -68, 90]

bst.remove(-30)
assert bst.preorder() == [86, -70, -68, 90]

bst.remove(90)
assert bst.preorder() == [86, -70, -68]

bst.remove(86)
assert bst.preorder() == [-70, -68]

bst.remove(-68)
assert bst.preorder() == [-70]

bst.remove(-70)
assert bst.preorder() == []

#[Case #17] 
bst = BinarySearchTree()
list_nums = [61, -97, -46, 76, -54, -6, 21, 50, -17, 7]

for elem in list_nums:
    bst.insert(elem)

bst.remove(-17)
assert bst.preorder() == [61, -97, -46, -54, -6, 21, 7, 50, 76]

bst.remove(-46)
assert bst.preorder() == [61, -97, -6, -54, 21, 7, 50, 76]

bst.remove(61)
assert bst.preorder() == [76, -97, -6, -54, 21, 7, 50]

bst.remove(21)
assert bst.preorder() == [76, -97, -6, -54, 50, 7]

bst.remove(76)
assert bst.preorder() == [-97, -6, -54, 50, 7]

bst.remove(50)
assert bst.preorder() == [-97, -6, -54, 7]

bst.remove(-6)
assert bst.preorder() == [-97, 7, -54]

bst.remove(-54)
assert bst.preorder() == [-97, 7]

bst.remove(7)
assert bst.preorder() == [-97]

bst.remove(-97)
assert bst.preorder() == []

#[Case #18] 
bst = BinarySearchTree()
list_nums = [-40, 30, 65, 88, -78, -19, 91, 4, -21, 20]

for elem in list_nums:
    bst.insert(elem)

bst.remove(20)
assert bst.preorder() == [-40, -78, 30, -19, -21, 4, 65, 88, 91]

bst.remove(-40)
assert bst.preorder() == [-21, -78, 30, -19, 4, 65, 88, 91]

bst.remove(4)
assert bst.preorder() == [-21, -78, 30, -19, 65, 88, 91]

bst.remove(-78)
assert bst.preorder() == [-21, 30, -19, 65, 88, 91]

bst.remove(88)
assert bst.preorder() == [-21, 30, -19, 65, 91]

bst.remove(-19)
assert bst.preorder() == [-21, 30, 65, 91]

bst.remove(65)
assert bst.preorder() == [-21, 30, 91]

bst.remove(30)
assert bst.preorder() == [-21, 91]

bst.remove(91)
assert bst.preorder() == [-21]

bst.remove(-21)
assert bst.preorder() == []

#[Case #19] 
bst = BinarySearchTree()
list_nums = [-54, -61, -6, 34, -46, 25, 28, -32, 97, 67]

for elem in list_nums:
    bst.insert(elem)

bst.remove(-46)
assert bst.preorder() == [-54, -61, -6, -32, 34, 25, 28, 97, 67]

bst.remove(97)
assert bst.preorder() == [-54, -61, -6, -32, 34, 25, 28, 67]

bst.remove(-54)
assert bst.preorder() == [-32, -61, -6, 34, 25, 28, 67]

bst.remove(28)
assert bst.preorder() == [-32, -61, -6, 34, 25, 67]

bst.remove(34)
assert bst.preorder() == [-32, -61, -6, 67, 25]

bst.remove(-6)
assert bst.preorder() == [-32, -61, 67, 25]

bst.remove(67)
assert bst.preorder() == [-32, -61, 25]

bst.remove(25)
assert bst.preorder() == [-32, -61]

bst.remove(-32)
assert bst.preorder() == [-61]

bst.remove(-61)
assert bst.preorder() == []

#[Case #20] 
bst = BinarySearchTree()
list_nums = [-68, -9, -47, 36, 70, 60, -83, 70, -62, -15]

for elem in list_nums:
    bst.insert(elem)

bst.remove(36)
assert bst.preorder() == [-68, -83, -9, -47, -62, -15, 70, 60, 70]

bst.remove(-15)
assert bst.preorder() == [-68, -83, -9, -47, -62, 70, 60, 70]

bst.remove(-68)
assert bst.preorder() == [-62, -83, -9, -47, 70, 60, 70]

bst.remove(-83)
assert bst.preorder() == [-62, -9, -47, 70, 60, 70]

bst.remove(70)
assert bst.preorder() == [-62, -9, -47, 70, 60]

bst.remove(-9)
assert bst.preorder() == [-62, 60, -47, 70]

bst.remove(60)
assert bst.preorder() == [-62, 70, -47]

bst.remove(70)
assert bst.preorder() == [-62, -47]

bst.remove(-62)
assert bst.preorder() == [-47]

bst.remove(-47)
assert bst.preorder() == []

#[Case #21] 
bst = BinarySearchTree()
list_nums = [-75, 71, 39, -77, -30, -36, -73, -34, -4, 73]

for elem in list_nums:
    bst.insert(elem)

bst.remove(71)
assert bst.preorder() == [-75, -77, 73, 39, -30, -36, -73, -34, -4]

bst.remove(39)
assert bst.preorder() == [-75, -77, 73, -30, -36, -73, -34, -4]

bst.remove(-34)
assert bst.preorder() == [-75, -77, 73, -30, -36, -73, -4]

bst.remove(-75)
assert bst.preorder() == [-73, -77, 73, -30, -36, -4]

bst.remove(-30)
assert bst.preorder() == [-73, -77, 73, -4, -36]

bst.remove(-4)
assert bst.preorder() == [-73, -77, 73, -36]

bst.remove(-36)
assert bst.preorder() == [-73, -77, 73]

bst.remove(73)
assert bst.preorder() == [-73, -77]

bst.remove(-77)
assert bst.preorder() == [-73]

bst.remove(-73)
assert bst.preorder() == []

#[Case #22] 
bst = BinarySearchTree()
list_nums = [-85, -79, -32, 10, -93, 84, -80, -83, 64, -15]

for elem in list_nums:
    bst.insert(elem)

bst.remove(84)
assert bst.preorder() == [-85, -93, -79, -80, -83, -32, 10, -15, 64]

bst.remove(-32)
assert bst.preorder() == [-85, -93, -79, -80, -83, 10, -15, 64]

bst.remove(-15)
assert bst.preorder() == [-85, -93, -79, -80, -83, 10, 64]

bst.remove(-80)
assert bst.preorder() == [-85, -93, -79, -83, 10, 64]

bst.remove(64)
assert bst.preorder() == [-85, -93, -79, -83, 10]

bst.remove(-93)
assert bst.preorder() == [-85, -79, -83, 10]

bst.remove(-85)
assert bst.preorder() == [-79, -83, 10]

bst.remove(-79)
assert bst.preorder() == [10, -83]

bst.remove(-83)
assert bst.preorder() == [10]

bst.remove(10)
assert bst.preorder() == []

#[Case #23] 
bst = BinarySearchTree()
list_nums = [92, 72, -35, 44, 11, 5, -51, -8, 13, -60]

for elem in list_nums:
    bst.insert(elem)

bst.remove(92)
assert bst.preorder() == [72, -35, -51, -60, 44, 11, 5, -8, 13]

bst.remove(-8)
assert bst.preorder() == [72, -35, -51, -60, 44, 11, 5, 13]

bst.remove(13)
assert bst.preorder() == [72, -35, -51, -60, 44, 11, 5]

bst.remove(-51)
assert bst.preorder() == [72, -35, -60, 44, 11, 5]

bst.remove(-60)
assert bst.preorder() == [72, -35, 44, 11, 5]

bst.remove(72)
assert bst.preorder() == [-35, 44, 11, 5]

bst.remove(11)
assert bst.preorder() == [-35, 44, 5]

bst.remove(-35)
assert bst.preorder() == [44, 5]

bst.remove(5)
assert bst.preorder() == [44]

bst.remove(44)
assert bst.preorder() == []

#[Case #24] 
bst = BinarySearchTree()
list_nums = [75, 93, 3, -79, 72, 100, -24, -86, 4, 10]

for elem in list_nums:
    bst.insert(elem)

bst.remove(72)
assert bst.preorder() == [75, 3, -79, -86, -24, 4, 10, 93, 100]

bst.remove(3)
assert bst.preorder() == [75, 4, -79, -86, -24, 10, 93, 100]

bst.remove(-24)
assert bst.preorder() == [75, 4, -79, -86, 10, 93, 100]

bst.remove(100)
assert bst.preorder() == [75, 4, -79, -86, 10, 93]

bst.remove(-79)
assert bst.preorder() == [75, 4, -86, 10, 93]

bst.remove(-86)
assert bst.preorder() == [75, 4, 10, 93]

bst.remove(4)
assert bst.preorder() == [75, 10, 93]

bst.remove(93)
assert bst.preorder() == [75, 10]

bst.remove(10)
assert bst.preorder() == [75]

bst.remove(75)
assert bst.preorder() == []

#[Case #25] 
bst = BinarySearchTree()
list_nums = [99, -4, 75, -86, -41, 61, 36, 15, 31, 1]

for elem in list_nums:
    bst.insert(elem)

bst.remove(36)
assert bst.preorder() == [99, -4, -86, -41, 75, 61, 15, 1, 31]

bst.remove(-41)
assert bst.preorder() == [99, -4, -86, 75, 61, 15, 1, 31]

bst.remove(1)
assert bst.preorder() == [99, -4, -86, 75, 61, 15, 31]

bst.remove(61)
assert bst.preorder() == [99, -4, -86, 75, 15, 31]

bst.remove(31)
assert bst.preorder() == [99, -4, -86, 75, 15]

bst.remove(-4)
assert bst.preorder() == [99, 15, -86, 75]

bst.remove(75)
assert bst.preorder() == [99, 15, -86]

bst.remove(-86)
assert bst.preorder() == [99, 15]

bst.remove(99)
assert bst.preorder() == [15]

bst.remove(15)
assert bst.preorder() == []

#[Case #26] 
bst = BinarySearchTree()
list_nums = [29, -79, -8, 16, -36, 29, -61, 48, 100, -99]

for elem in list_nums:
    bst.insert(elem)

bst.remove(16)
assert bst.preorder() == [29, -79, -99, -8, -36, -61, 29, 48, 100]

bst.remove(29)
assert bst.preorder() == [29, -79, -99, -8, -36, -61, 48, 100]

bst.remove(48)
assert bst.preorder() == [29, -79, -99, -8, -36, -61, 100]

bst.remove(-8)
assert bst.preorder() == [29, -79, -99, -36, -61, 100]

bst.remove(-99)
assert bst.preorder() == [29, -79, -36, -61, 100]

bst.remove(-36)
assert bst.preorder() == [29, -79, -61, 100]

bst.remove(100)
assert bst.preorder() == [29, -79, -61]

bst.remove(29)
assert bst.preorder() == [-79, -61]

bst.remove(-79)
assert bst.preorder() == [-61]

bst.remove(-61)
assert bst.preorder() == []

#[Case #27] 
bst = BinarySearchTree()
list_nums = [-40, 92, -92, 9, 58, -83, -38, 84, -79, -40]

for elem in list_nums:
    bst.insert(elem)

bst.remove(-38)
assert bst.preorder() == [-40, -92, -83, -79, 92, 9, -40, 58, 84]

bst.remove(-40)
assert bst.preorder() == [-40, -92, -83, -79, 92, 9, 58, 84]

bst.remove(9)
assert bst.preorder() == [-40, -92, -83, -79, 92, 58, 84]

bst.remove(92)
assert bst.preorder() == [-40, -92, -83, -79, 58, 84]

bst.remove(-40)
assert bst.preorder() == [58, -92, -83, -79, 84]

bst.remove(-79)
assert bst.preorder() == [58, -92, -83, 84]

bst.remove(58)
assert bst.preorder() == [84, -92, -83]

bst.remove(-83)
assert bst.preorder() == [84, -92]

bst.remove(-92)
assert bst.preorder() == [84]

bst.remove(84)
assert bst.preorder() == []

#[Case #28] 
bst = BinarySearchTree()
list_nums = [79, -67, -76, 55, 51, -4, -63, 47, -86, 75]

for elem in list_nums:
    bst.insert(elem)

bst.remove(51)
assert bst.preorder() == [79, -67, -76, -86, 55, -4, -63, 47, 75]

bst.remove(-76)
assert bst.preorder() == [79, -67, -86, 55, -4, -63, 47, 75]

bst.remove(-63)
assert bst.preorder() == [79, -67, -86, 55, -4, 47, 75]

bst.remove(-67)
assert bst.preorder() == [79, -4, -86, 55, 47, 75]

bst.remove(-4)
assert bst.preorder() == [79, 47, -86, 55, 75]

bst.remove(-86)
assert bst.preorder() == [79, 47, 55, 75]

bst.remove(47)
assert bst.preorder() == [79, 55, 75]

bst.remove(55)
assert bst.preorder() == [79, 75]

bst.remove(75)
assert bst.preorder() == [79]

bst.remove(79)
assert bst.preorder() == []

#[Case #29] 
bst = BinarySearchTree()
list_nums = [71, -78, 40, -8, 32, 54, -27, -17, -21, -77]

for elem in list_nums:
    bst.insert(elem)

bst.remove(71)
assert bst.preorder() == [-78, 40, -8, -27, -77, -17, -21, 32, 54]

bst.remove(-17)
assert bst.preorder() == [-78, 40, -8, -27, -77, -21, 32, 54]

bst.remove(54)
assert bst.preorder() == [-78, 40, -8, -27, -77, -21, 32]

bst.remove(-27)
assert bst.preorder() == [-78, 40, -8, -21, -77, 32]

bst.remove(-8)
assert bst.preorder() == [-78, 40, 32, -21, -77]

bst.remove(-77)
assert bst.preorder() == [-78, 40, 32, -21]

bst.remove(32)
assert bst.preorder() == [-78, 40, -21]

bst.remove(-78)
assert bst.preorder() == [40, -21]

bst.remove(-21)
assert bst.preorder() == [40]

bst.remove(40)
assert bst.preorder() == []

#[Case #30] 
bst = BinarySearchTree()
list_nums = [-90, -96, 9, -5, -81, 78, -65, -67, 81, -68]

for elem in list_nums:
    bst.insert(elem)

bst.remove(-90)
assert bst.preorder() == [-81, -96, 9, -5, -65, -67, -68, 78, 81]

bst.remove(-5)
assert bst.preorder() == [-81, -96, 9, -65, -67, -68, 78, 81]

bst.remove(-81)
assert bst.preorder() == [-68, -96, 9, -65, -67, 78, 81]

bst.remove(-65)
assert bst.preorder() == [-68, -96, 9, -67, 78, 81]

bst.remove(78)
assert bst.preorder() == [-68, -96, 9, -67, 81]

bst.remove(-67)
assert bst.preorder() == [-68, -96, 9, 81]

bst.remove(9)
assert bst.preorder() == [-68, -96, 81]

bst.remove(-68)
assert bst.preorder() == [81, -96]

bst.remove(81)
assert bst.preorder() == [-96]

bst.remove(-96)
assert bst.preorder() == []

#[Case #31] 
bst = BinarySearchTree()
list_nums = [-77, -100, 54, -1, 13, 63, -44, 37, 56, -40]

for elem in list_nums:
    bst.insert(elem)

bst.remove(63)
assert bst.preorder() == [-77, -100, 54, -1, -44, -40, 13, 37, 56]

bst.remove(56)
assert bst.preorder() == [-77, -100, 54, -1, -44, -40, 13, 37]

bst.remove(-1)
assert bst.preorder() == [-77, -100, 54, 13, -44, -40, 37]

bst.remove(13)
assert bst.preorder() == [-77, -100, 54, 37, -44, -40]

bst.remove(-44)
assert bst.preorder() == [-77, -100, 54, 37, -40]

bst.remove(54)
assert bst.preorder() == [-77, -100, 37, -40]

bst.remove(-77)
assert bst.preorder() == [-40, -100, 37]

bst.remove(-100)
assert bst.preorder() == [-40, 37]

bst.remove(-40)
assert bst.preorder() == [37]

bst.remove(37)
assert bst.preorder() == []

#[Case #32] 
bst = BinarySearchTree()
list_nums = [91, -26, 53, -26, -86, -61, 94, -53, 60, 36]

for elem in list_nums:
    bst.insert(elem)

bst.remove(-26)
assert bst.preorder() == [91, -26, -86, -61, -53, 53, 36, 60, 94]

bst.remove(-61)
assert bst.preorder() == [91, -26, -86, -53, 53, 36, 60, 94]

bst.remove(-86)
assert bst.preorder() == [91, -26, -53, 53, 36, 60, 94]

bst.remove(-26)
assert bst.preorder() == [91, 36, -53, 53, 60, 94]

bst.remove(-53)
assert bst.preorder() == [91, 36, 53, 60, 94]

bst.remove(36)
assert bst.preorder() == [91, 53, 60, 94]

bst.remove(91)
assert bst.preorder() == [94, 53, 60]

bst.remove(60)
assert bst.preorder() == [94, 53]

bst.remove(94)
assert bst.preorder() == [53]

bst.remove(53)
assert bst.preorder() == []

#[Case #33] 
bst = BinarySearchTree()
list_nums = [55, -25, 29, 28, 84, -37, 74, -89, 88, 93]

for elem in list_nums:
    bst.insert(elem)

bst.remove(55)
assert bst.preorder() == [74, -25, -37, -89, 29, 28, 84, 88, 93]

bst.remove(-37)
assert bst.preorder() == [74, -25, -89, 29, 28, 84, 88, 93]

bst.remove(74)
assert bst.preorder() == [84, -25, -89, 29, 28, 88, 93]

bst.remove(93)
assert bst.preorder() == [84, -25, -89, 29, 28, 88]

bst.remove(29)
assert bst.preorder() == [84, -25, -89, 28, 88]

bst.remove(88)
assert bst.preorder() == [84, -25, -89, 28]

bst.remove(28)
assert bst.preorder() == [84, -25, -89]

bst.remove(-89)
assert bst.preorder() == [84, -25]

bst.remove(84)
assert bst.preorder() == [-25]

bst.remove(-25)
assert bst.preorder() == []

#[Case #34] 
bst = BinarySearchTree()
list_nums = [72, 80, 29, -100, -55, -3, -6, -14, -38, -2]

for elem in list_nums:
    bst.insert(elem)

bst.remove(-100)
assert bst.preorder() == [72, 29, -55, -3, -6, -14, -38, -2, 80]

bst.remove(-14)
assert bst.preorder() == [72, 29, -55, -3, -6, -38, -2, 80]

bst.remove(29)
assert bst.preorder() == [72, -55, -3, -6, -38, -2, 80]

bst.remove(-38)
assert bst.preorder() == [72, -55, -3, -6, -2, 80]

bst.remove(-6)
assert bst.preorder() == [72, -55, -3, -2, 80]

bst.remove(-55)
assert bst.preorder() == [72, -3, -2, 80]

bst.remove(-2)
assert bst.preorder() == [72, -3, 80]

bst.remove(80)
assert bst.preorder() == [72, -3]

bst.remove(-3)
assert bst.preorder() == [72]

bst.remove(72)
assert bst.preorder() == []

#[Case #35] 
bst = BinarySearchTree()
list_nums = [-16, 56, 4, -88, -66, 38, -70, 35, 57, 98]

for elem in list_nums:
    bst.insert(elem)

bst.remove(-70)
assert bst.preorder() == [-16, -88, -66, 56, 4, 38, 35, 57, 98]

bst.remove(56)
assert bst.preorder() == [-16, -88, -66, 57, 4, 38, 35, 98]

bst.remove(-66)
assert bst.preorder() == [-16, -88, 57, 4, 38, 35, 98]

bst.remove(-16)
assert bst.preorder() == [4, -88, 57, 38, 35, 98]

bst.remove(35)
assert bst.preorder() == [4, -88, 57, 38, 98]

bst.remove(-88)
assert bst.preorder() == [4, 57, 38, 98]

bst.remove(57)
assert bst.preorder() == [4, 98, 38]

bst.remove(4)
assert bst.preorder() == [98, 38]

bst.remove(38)
assert bst.preorder() == [98]

bst.remove(98)
assert bst.preorder() == []

#[Case #36] 
bst = BinarySearchTree()
list_nums = [-2, 59, 85, -31, 96, -56, 0, 84, -98, -94]

for elem in list_nums:
    bst.insert(elem)

bst.remove(-31)
assert bst.preorder() == [-2, -56, -98, -94, 59, 0, 85, 84, 96]

bst.remove(-2)
assert bst.preorder() == [0, -56, -98, -94, 59, 85, 84, 96]

bst.remove(85)
assert bst.preorder() == [0, -56, -98, -94, 59, 96, 84]

bst.remove(-94)
assert bst.preorder() == [0, -56, -98, 59, 96, 84]

bst.remove(-56)
assert bst.preorder() == [0, -98, 59, 96, 84]

bst.remove(-98)
assert bst.preorder() == [0, 59, 96, 84]

bst.remove(96)
assert bst.preorder() == [0, 59, 84]

bst.remove(0)
assert bst.preorder() == [59, 84]

bst.remove(84)
assert bst.preorder() == [59]

bst.remove(59)
assert bst.preorder() == []

#[Case #37] 
bst = BinarySearchTree()
list_nums = [56, -5, 98, 15, -98, 40, 99, -33, 77, 0]

for elem in list_nums:
    bst.insert(elem)

bst.remove(15)
assert bst.preorder() == [56, -5, -98, -33, 40, 0, 98, 77, 99]

bst.remove(77)
assert bst.preorder() == [56, -5, -98, -33, 40, 0, 98, 99]

bst.remove(56)
assert bst.preorder() == [98, -5, -98, -33, 40, 0, 99]

bst.remove(-5)
assert bst.preorder() == [98, 0, -98, -33, 40, 99]

bst.remove(0)
assert bst.preorder() == [98, 40, -98, -33, 99]

bst.remove(40)
assert bst.preorder() == [98, -98, -33, 99]

bst.remove(-98)
assert bst.preorder() == [98, -33, 99]

bst.remove(98)
assert bst.preorder() == [99, -33]

bst.remove(99)
assert bst.preorder() == [-33]

bst.remove(-33)
assert bst.preorder() == []

#[Case #38] 
bst = BinarySearchTree()
list_nums = [48, -52, 18, 52, -70, 16, 54, -14, 30, -52]

for elem in list_nums:
    bst.insert(elem)

bst.remove(52)
assert bst.preorder() == [48, -52, -70, 18, 16, -14, -52, 30, 54]

bst.remove(48)
assert bst.preorder() == [54, -52, -70, 18, 16, -14, -52, 30]

bst.remove(-52)
assert bst.preorder() == [54, -52, -70, 18, 16, -14, 30]

bst.remove(-70)
assert bst.preorder() == [54, -52, 18, 16, -14, 30]

bst.remove(30)
assert bst.preorder() == [54, -52, 18, 16, -14]

bst.remove(-52)
assert bst.preorder() == [54, 18, 16, -14]

bst.remove(18)
assert bst.preorder() == [54, 16, -14]

bst.remove(54)
assert bst.preorder() == [16, -14]

bst.remove(-14)
assert bst.preorder() == [16]

bst.remove(16)
assert bst.preorder() == []

#[Case #39] 
bst = BinarySearchTree()
list_nums = [52, -61, 28, -69, -89, -47, 8, -36, -33, -73]

for elem in list_nums:
    bst.insert(elem)

bst.remove(-33)
assert bst.preorder() == [52, -61, -69, -89, -73, 28, -47, 8, -36]

bst.remove(-69)
assert bst.preorder() == [52, -61, -89, -73, 28, -47, 8, -36]

bst.remove(28)
assert bst.preorder() == [52, -61, -89, -73, -47, 8, -36]

bst.remove(52)
assert bst.preorder() == [-61, -89, -73, -47, 8, -36]

bst.remove(8)
assert bst.preorder() == [-61, -89, -73, -47, -36]

bst.remove(-73)
assert bst.preorder() == [-61, -89, -47, -36]

bst.remove(-47)
assert bst.preorder() == [-61, -89, -36]

bst.remove(-61)
assert bst.preorder() == [-36, -89]

bst.remove(-89)
assert bst.preorder() == [-36]

bst.remove(-36)
assert bst.preorder() == []

#[Case #40] 
bst = BinarySearchTree()
list_nums = [-37, -87, -45, 25, -13, 99, 63, 70, 63, -4]

for elem in list_nums:
    bst.insert(elem)

bst.remove(-87)
assert bst.preorder() == [-37, -45, 25, -13, -4, 99, 63, 70, 63]

bst.remove(-45)
assert bst.preorder() == [-37, 25, -13, -4, 99, 63, 70, 63]

bst.remove(-37)
assert bst.preorder() == [25, -13, -4, 99, 63, 70, 63]

bst.remove(99)
assert bst.preorder() == [25, -13, -4, 63, 70, 63]

bst.remove(-4)
assert bst.preorder() == [25, -13, 63, 70, 63]

bst.remove(63)
assert bst.preorder() == [25, -13, 70, 63]

bst.remove(-13)
assert bst.preorder() == [25, 70, 63]

bst.remove(63)
assert bst.preorder() == [25, 70]

bst.remove(70)
assert bst.preorder() == [25]

bst.remove(25)
assert bst.preorder() == []

#[Case #41] 
bst = BinarySearchTree()
list_nums = [12, -47, 5, -21, 60, 93, 83, -4, 4, -25]

for elem in list_nums:
    bst.insert(elem)

bst.remove(-47)
assert bst.preorder() == [12, 5, -21, -25, -4, 4, 60, 93, 83]

bst.remove(60)
assert bst.preorder() == [12, 5, -21, -25, -4, 4, 93, 83]

bst.remove(93)
assert bst.preorder() == [12, 5, -21, -25, -4, 4, 83]

bst.remove(83)
assert bst.preorder() == [12, 5, -21, -25, -4, 4]

bst.remove(-21)
assert bst.preorder() == [12, 5, -4, -25, 4]

bst.remove(-25)
assert bst.preorder() == [12, 5, -4, 4]

bst.remove(4)
assert bst.preorder() == [12, 5, -4]

bst.remove(-4)
assert bst.preorder() == [12, 5]

bst.remove(12)
assert bst.preorder() == [5]

bst.remove(5)
assert bst.preorder() == []

#[Case #42] 
bst = BinarySearchTree()
list_nums = [-56, 84, 74, 45, 32, 97, -12, 70, 76, -67]

for elem in list_nums:
    bst.insert(elem)

bst.remove(-12)
assert bst.preorder() == [-56, -67, 84, 74, 45, 32, 70, 76, 97]

bst.remove(-56)
assert bst.preorder() == [32, -67, 84, 74, 45, 70, 76, 97]

bst.remove(84)
assert bst.preorder() == [32, -67, 97, 74, 45, 70, 76]

bst.remove(32)
assert bst.preorder() == [45, -67, 97, 74, 70, 76]

bst.remove(-67)
assert bst.preorder() == [45, 97, 74, 70, 76]

bst.remove(70)
assert bst.preorder() == [45, 97, 74, 76]

bst.remove(45)
assert bst.preorder() == [97, 74, 76]

bst.remove(74)
assert bst.preorder() == [97, 76]

bst.remove(97)
assert bst.preorder() == [76]

bst.remove(76)
assert bst.preorder() == []

#[Case #43] 
bst = BinarySearchTree()
list_nums = [-99, -57, 34, -2, -37, 54, 67, -24, 42, -100]

for elem in list_nums:
    bst.insert(elem)

bst.remove(-24)
assert bst.preorder() == [-99, -100, -57, 34, -2, -37, 54, 42, 67]

bst.remove(-100)
assert bst.preorder() == [-99, -57, 34, -2, -37, 54, 42, 67]

bst.remove(54)
assert bst.preorder() == [-99, -57, 34, -2, -37, 67, 42]

bst.remove(67)
assert bst.preorder() == [-99, -57, 34, -2, -37, 42]

bst.remove(-99)
assert bst.preorder() == [-57, 34, -2, -37, 42]

bst.remove(-37)
assert bst.preorder() == [-57, 34, -2, 42]

bst.remove(-2)
assert bst.preorder() == [-57, 34, 42]

bst.remove(34)
assert bst.preorder() == [-57, 42]

bst.remove(-57)
assert bst.preorder() == [42]

bst.remove(42)
assert bst.preorder() == []

#[Case #44] 
bst = BinarySearchTree()
list_nums = [9, -36, 60, 5, -34, 93, -66, -65, 83, 19]

for elem in list_nums:
    bst.insert(elem)

bst.remove(60)
assert bst.preorder() == [9, -36, -66, -65, 5, -34, 83, 19, 93]

bst.remove(-65)
assert bst.preorder() == [9, -36, -66, 5, -34, 83, 19, 93]

bst.remove(-34)
assert bst.preorder() == [9, -36, -66, 5, 83, 19, 93]

bst.remove(9)
assert bst.preorder() == [19, -36, -66, 5, 83, 93]

bst.remove(5)
assert bst.preorder() == [19, -36, -66, 83, 93]

bst.remove(83)
assert bst.preorder() == [19, -36, -66, 93]

bst.remove(93)
assert bst.preorder() == [19, -36, -66]

bst.remove(-66)
assert bst.preorder() == [19, -36]

bst.remove(-36)
assert bst.preorder() == [19]

bst.remove(19)
assert bst.preorder() == []

#[Case #45] 
bst = BinarySearchTree()
list_nums = [-42, -88, -54, 89, 92, -84, -91, -67, 34, -57]

for elem in list_nums:
    bst.insert(elem)

bst.remove(-54)
assert bst.preorder() == [-42, -88, -91, -84, -67, -57, 89, 34, 92]

bst.remove(89)
assert bst.preorder() == [-42, -88, -91, -84, -67, -57, 92, 34]

bst.remove(-84)
assert bst.preorder() == [-42, -88, -91, -67, -57, 92, 34]

bst.remove(-91)
assert bst.preorder() == [-42, -88, -67, -57, 92, 34]

bst.remove(-88)
assert bst.preorder() == [-42, -67, -57, 92, 34]

bst.remove(34)
assert bst.preorder() == [-42, -67, -57, 92]

bst.remove(92)
assert bst.preorder() == [-42, -67, -57]

bst.remove(-57)
assert bst.preorder() == [-42, -67]

bst.remove(-42)
assert bst.preorder() == [-67]

bst.remove(-67)
assert bst.preorder() == []

#[Case #46] 
bst = BinarySearchTree()
list_nums = [30, 25, 80, -62, 94, 36, 40, -35, -56, 82]

for elem in list_nums:
    bst.insert(elem)

bst.remove(80)
assert bst.preorder() == [30, 25, -62, -35, -56, 82, 36, 40, 94]

bst.remove(25)
assert bst.preorder() == [30, -62, -35, -56, 82, 36, 40, 94]

bst.remove(-35)
assert bst.preorder() == [30, -62, -56, 82, 36, 40, 94]

bst.remove(40)
assert bst.preorder() == [30, -62, -56, 82, 36, 94]

bst.remove(-62)
assert bst.preorder() == [30, -56, 82, 36, 94]

bst.remove(30)
assert bst.preorder() == [36, -56, 82, 94]

bst.remove(94)
assert bst.preorder() == [36, -56, 82]

bst.remove(82)
assert bst.preorder() == [36, -56]

bst.remove(-56)
assert bst.preorder() == [36]

bst.remove(36)
assert bst.preorder() == []

#[Case #47] 
bst = BinarySearchTree()
list_nums = [1, -74, 10, -55, -33, -10, 47, -29, -74, 37]

for elem in list_nums:
    bst.insert(elem)

bst.remove(10)
assert bst.preorder() == [1, -74, -55, -74, -33, -10, -29, 47, 37]

bst.remove(-29)
assert bst.preorder() == [1, -74, -55, -74, -33, -10, 47, 37]

bst.remove(37)
assert bst.preorder() == [1, -74, -55, -74, -33, -10, 47]

bst.remove(-74)
assert bst.preorder() == [1, -55, -74, -33, -10, 47]

bst.remove(-55)
assert bst.preorder() == [1, -33, -74, -10, 47]

bst.remove(-10)
assert bst.preorder() == [1, -33, -74, 47]

bst.remove(-74)
assert bst.preorder() == [1, -33, 47]

bst.remove(1)
assert bst.preorder() == [47, -33]

bst.remove(-33)
assert bst.preorder() == [47]

bst.remove(47)
assert bst.preorder() == []

#[Case #48] 
bst = BinarySearchTree()
list_nums = [30, 92, -59, 80, 71, 38, 27, -42, -18, 99]

for elem in list_nums:
    bst.insert(elem)

bst.remove(71)
assert bst.preorder() == [30, -59, 27, -42, -18, 92, 80, 38, 99]

bst.remove(99)
assert bst.preorder() == [30, -59, 27, -42, -18, 92, 80, 38]

bst.remove(30)
assert bst.preorder() == [38, -59, 27, -42, -18, 92, 80]

bst.remove(38)
assert bst.preorder() == [80, -59, 27, -42, -18, 92]

bst.remove(-42)
assert bst.preorder() == [80, -59, 27, -18, 92]

bst.remove(92)
assert bst.preorder() == [80, -59, 27, -18]

bst.remove(-59)
assert bst.preorder() == [80, 27, -18]

bst.remove(80)
assert bst.preorder() == [27, -18]

bst.remove(27)
assert bst.preorder() == [-18]

bst.remove(-18)
assert bst.preorder() == []

#[Case #49] 
bst = BinarySearchTree()
list_nums = [-62, 60, 12, -1, 21, 53, 6, -88, -24, 97]

for elem in list_nums:
    bst.insert(elem)

bst.remove(21)
assert bst.preorder() == [-62, -88, 60, 12, -1, -24, 6, 53, 97]

bst.remove(-62)
assert bst.preorder() == [-24, -88, 60, 12, -1, 6, 53, 97]

bst.remove(97)
assert bst.preorder() == [-24, -88, 60, 12, -1, 6, 53]

bst.remove(-88)
assert bst.preorder() == [-24, 60, 12, -1, 6, 53]

bst.remove(60)
assert bst.preorder() == [-24, 12, -1, 6, 53]

bst.remove(6)
assert bst.preorder() == [-24, 12, -1, 53]

bst.remove(53)
assert bst.preorder() == [-24, 12, -1]

bst.remove(-24)
assert bst.preorder() == [12, -1]

bst.remove(12)
assert bst.preorder() == [-1]

bst.remove(-1)
assert bst.preorder() == []

#[Case #50] 
bst = BinarySearchTree()
list_nums = [27, -6, -15, 12, 80, 66, -61, -37, -33, 38]

for elem in list_nums:
    bst.insert(elem)

bst.remove(-37)
assert bst.preorder() == [27, -6, -15, -61, -33, 12, 80, 66, 38]

bst.remove(66)
assert bst.preorder() == [27, -6, -15, -61, -33, 12, 80, 38]

bst.remove(27)
assert bst.preorder() == [38, -6, -15, -61, -33, 12, 80]

bst.remove(-15)
assert bst.preorder() == [38, -6, -61, -33, 12, 80]

bst.remove(-6)
assert bst.preorder() == [38, 12, -61, -33, 80]

bst.remove(38)
assert bst.preorder() == [80, 12, -61, -33]

bst.remove(-61)
assert bst.preorder() == [80, 12, -33]

bst.remove(80)
assert bst.preorder() == [12, -33]

bst.remove(12)
assert bst.preorder() == [-33]

bst.remove(-33)
assert bst.preorder() == []

