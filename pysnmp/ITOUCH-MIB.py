#
# PySNMP MIB module ITOUCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ITOUCH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:46:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, enterprises, MibIdentifier, iso, Integer32, ModuleIdentity, Unsigned32, IpAddress, Bits, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "enterprises", "MibIdentifier", "iso", "Integer32", "ModuleIdentity", "Unsigned32", "IpAddress", "Bits", "TimeTicks", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
iTouch = MibIdentifier((1, 3, 6, 1, 4, 1, 33))
agent = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8))
class DateTime(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class AddressType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("local", 3), ("ip", 4), ("ethernet", 5))

class TypedAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class SoftwareType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("terminalServer", 1), ("bridge", 3), ("repeater", 4), ("bridgeRouter", 5), ("router", 6), ("bridgeRouterRepeater", 7), ("switch", 8), ("oem", 9))

class HardwareType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 74, 75, 76, 77, 78, 79, 80, 81, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 105, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 230))
    namedValues = NamedValues(("unknown", 1), ("em1608", 29), ("ir7520", 30), ("ir9020", 31), ("ir7020", 32), ("mxTServJ8", 33), ("mxTservJ16", 34), ("mxManF2", 35), ("mx1500", 36), ("mx1100", 37), ("mx1800", 38), ("mxNpcP1", 39), ("mxTsrLJ16", 40), ("mxTsrvLJ8", 41), ("mxTsrvMj8", 42), ("mxTsrvNJ8", 43), ("mxTsrvOJ8", 44), ("mx1400", 45), ("mx6510", 46), ("mxRb2", 47), ("mx1500x8", 49), ("mx1710", 50), ("mx2710", 51), ("ts3395", 52), ("mx1120", 53), ("mx1520", 54), ("mx1820", 55), ("mx2220", 56), ("mx3510", 57), ("mx6625", 58), ("mx2120", 59), ("mx6020", 60), ("mx3610", 61), ("etsmim", 62), ("mx3010", 63), ("mx6025", 64), ("lannetTs", 65), ("fn1500", 66), ("dpXp1", 67), ("mx3710", 68), ("mx3210", 69), ("mx6710", 70), ("mx6220", 71), ("mx1600a", 74), ("mx1450", 75), ("ts720", 76), ("so3395aTs", 77), ("mx1608", 78), ("mx2210a", 79), ("br401", 80), ("mx6800a", 81), ("notApplicable", 83), ("rp210", 84), ("mx6800b", 85), ("mx1620", 86), ("mx2240", 87), ("ps3m", 88), ("lb2Wan", 89), ("nio1600", 90), ("asy160", 91), ("mx1640", 92), ("br220", 93), ("rp211", 94), ("br221", 95), ("mx2210b", 96), ("mx1600b", 97), ("mx1600c", 98), ("mx800a", 99), ("mx1600d", 100), ("tokenRing", 101), ("mx800b", 102), ("br501", 103), ("br350", 105), ("br350ExpansionSlot", 107), ("n3000", 108), ("br402", 109), ("sw610", 110), ("sw610S", 111), ("br501s", 112), ("br501c", 113), ("br501sc", 114), ("routeRunnerIsdnSt", 115), ("routeRunner", 116), ("mx1608a", 117), ("routerRunnerIsdnU", 118), ("mx1608b", 119), ("mx1604", 120), ("n3000Ias", 123), ("irMgr0Rdc", 124), ("ir9040", 125), ("ir7040", 126), ("irMgr0", 127), ("irM800", 128), ("irM700", 129), ("ir8020", 130), ("ir8040", 131), ("ir7004", 132), ("ir7008", 133), ("ir8004", 134), ("ir8008", 135), ("irM900", 136), ("irMGR0AC", 137), ("irMGR0AC-IN", 138), ("ir9004", 139), ("ir9008", 140), ("ir9504", 141), ("n3000SP", 230))

class ChassisType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("mx45xx", 2), ("net9000", 3), ("net9000SWITCH", 4))

class IOType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(16, 32, 33, 34, 35, 36, 37, 38, 39, 40, 128, 129, 144, 145, 146, 147, 148, 149, 150, 155, 156, 157, 158, 160, 174, 175, 176, 177, 178, 179, 180, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 207, 209, 210, 214, 224, 225, 226, 227, 231, 232, 233, 234, 235, 236, 237, 238, 239))
    namedValues = NamedValues(("io616", 16), ("dualE175", 32), ("dualT1", 33), ("bri8", 34), ("io351d", 35), ("io352d", 36), ("dualE1120", 37), ("singleT1", 38), ("singleE175", 39), ("singleE1120", 40), ("io625", 128), ("io626", 129), ("io601", 144), ("io602", 145), ("io603", 146), ("io601A", 147), ("io602A", 148), ("io603A", 149), ("io604", 150), ("io621", 155), ("io622", 156), ("io623", 157), ("io624", 158), ("io301x12", 160), ("io521", 174), ("io522", 175), ("io512x3", 176), ("io511x3", 177), ("io520", 178), ("io514", 179), ("io513", 180), ("io470x4", 182), ("io469x2", 183), ("io467x4", 184), ("io467x2", 185), ("io468x4", 186), ("io468x2", 187), ("io466x4", 188), ("io465x2", 189), ("io464x4", 190), ("io463x2", 191), ("io201", 192), ("io202", 193), ("io204", 194), ("io203", 195), ("io251", 196), ("io231", 197), ("io254", 198), ("io206", 199), ("io253", 200), ("io256", 201), ("io201a", 202), ("io202a", 203), ("io203a", 204), ("ioRepeater", 207), ("io205x12", 209), ("io205", 210), ("io255", 214), ("io722", 224), ("io721", 225), ("io411", 226), ("io724", 227), ("io725", 231), ("io723", 232), ("io462", 233), ("io412", 234), ("ioTS16a", 235), ("ioTS16b", 236), ("io461", 237), ("io101", 238), ("io119", 239))

terminalServer = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1))
tsMxCard1M = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 1))
tsMxBox1M = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 2))
tsMxCard = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 3))
tsMxBox = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 4))
tsN9 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 5))
tsPrint = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 6))
tsX25 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 7))
em1608 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 29))
ir7520 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 30))
ir9020 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 31))
ir7020 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 32))
irMgr0Rdc = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 124))
ir9040 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 125))
ir7040 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 126))
irMgr0 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 127))
irM800 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 128))
irM700 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 129))
ir8020 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 130))
ir8040 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 131))
ir7004 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 132))
ir7008 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 133))
ir8004 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 134))
ir8008 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 135))
irM900 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 136))
irMGR0AC = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 137))
irMGR0AC_IN = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 138)).setLabel("irMGR0AC-IN")
ir9004 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 139))
ir9008 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 140))
ir9504 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 1, 141))
bridge = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 3))
repeater = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 4))
rpMx = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 4, 1))
rpN9 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 4, 2))
bridgeRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 5))
bridgeRouterMx = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 5, 1))
bridgeRouterN9 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 5, 2))
bridgeRouterN3 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 5, 3))
bridgeRouterN2 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 5, 4))
bridgeRouterEB = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 5, 5))
bridgeRouterRepeater = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 7))
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 8))
oem = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 9))
netVantage = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 9, 1))
nv8516TT = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 9, 1, 1))
nv8516FF = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 9, 1, 2))
nbase = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 10))
nbaseSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 10, 1))
nbaseSwitchN9 = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 8, 10, 1, 1))
mibBuilder.exportSymbols("ITOUCH-MIB", switch=switch, irMGR0AC_IN=irMGR0AC_IN, irMgr0=irMgr0, bridgeRouter=bridgeRouter, bridgeRouterN2=bridgeRouterN2, ir8020=ir8020, em1608=em1608, tsPrint=tsPrint, tsMxBox1M=tsMxBox1M, SoftwareType=SoftwareType, ir9020=ir9020, bridge=bridge, nbaseSwitchN9=nbaseSwitchN9, AddressType=AddressType, bridgeRouterN3=bridgeRouterN3, ir7520=ir7520, agent=agent, ir9040=ir9040, netVantage=netVantage, bridgeRouterMx=bridgeRouterMx, ir7008=ir7008, tsMxCard=tsMxCard, bridgeRouterN9=bridgeRouterN9, bridgeRouterEB=bridgeRouterEB, iTouch=iTouch, irM900=irM900, nv8516FF=nv8516FF, ir9008=ir9008, ChassisType=ChassisType, rpMx=rpMx, nv8516TT=nv8516TT, HardwareType=HardwareType, tsMxCard1M=tsMxCard1M, rpN9=rpN9, bridgeRouterRepeater=bridgeRouterRepeater, nbaseSwitch=nbaseSwitch, nbase=nbase, tsN9=tsN9, ir7040=ir7040, irM800=irM800, ir8008=ir8008, irMGR0AC=irMGR0AC, DateTime=DateTime, TypedAddress=TypedAddress, repeater=repeater, ir8004=ir8004, irM700=irM700, ir9504=ir9504, irMgr0Rdc=irMgr0Rdc, tsX25=tsX25, ir9004=ir9004, IOType=IOType, oem=oem, terminalServer=terminalServer, tsMxBox=tsMxBox, ir8040=ir8040, ir7020=ir7020, ir7004=ir7004)
