#
# PySNMP MIB module CYAN-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CYAN-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:18:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
cyanMibModules, = mibBuilder.importSymbols("CYAN-MIB", "cyanMibModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibIdentifier, Unsigned32, NotificationType, Counter32, Gauge32, Counter64, TimeTicks, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "Unsigned32", "NotificationType", "Counter32", "Gauge32", "Counter64", "TimeTicks", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cyanTCModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 28533, 5, 1))
cyanTCModule.setRevisions(('2014-12-07 05:45',))
if mibBuilder.loadTexts: cyanTCModule.setLastUpdated('201412070545Z')
if mibBuilder.loadTexts: cyanTCModule.setOrganization('Cyan, Inc.')
class CyanActvStdbyTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("stdby", 0), ("active", 1))

class CyanAdminStateTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("adminunlocked", 1), ("adminautoinservice", 2), ("adminlockedmat", 3), ("adminlockeddis", 4))

class CyanAugStructureTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 8, 7, 9))
    namedValues = NamedValues(("notconfigured", 0), ("au464c", 8), ("aug16", 7), ("transparent", 9))

class CyanChannelIdTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("protect", 0), ("working", 1))

class CyanEnDisabledTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CyanFecModeTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3))
    namedValues = NamedValues(("fecReedSolomon", 1), ("fecEnhanced", 3))

class CyanFppSubTypeTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unconfigured", 0), ("unitype1", 1), ("unitype2", 2), ("nnipbb", 3), ("nnimpls", 4))

class CyanFppTypeTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("uni", 1), ("nni", 2))

class CyanGfpUpiTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21))
    namedValues = NamedValues(("ethernetframe", 1), ("pppFrame", 2), ("fiberchannelTransparent", 3), ("ficonTransparent", 4), ("esconTransparent", 5), ("gbeTransparent", 6), ("maposFrame", 8), ("dvbAsiTransparent", 9), ("ieee80217RprFrame", 10), ("fiberchannelBbwFrame", 11), ("fiberchannelAsyncTransparent", 12), ("mplsFrame", 13), ("osiFrame", 15), ("ipv4Frame", 16), ("ipv6Frame", 17), ("dvbAsiFrame", 18), ("ethernet64b66bFrame", 19), ("ethernet64b66bOrderedsetFrame", 20), ("fc1200Transparent", 21))

class CyanLEDTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("off", 0), ("redBlinking", 1), ("red", 2), ("greenBlinking", 3), ("green", 4), ("amberBlinking", 5), ("amber", 6), ("blueBlinking", 7), ("blue", 8), ("redBlinkingSlow", 9), ("greenBlinkingSlow", 10), ("amberBlinkingSlow", 11), ("blueBlinkingSlow", 12))

class CyanLayerRateTc(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("na", 0), ("fiber", 1), ("electrical", 2), ("och", 3), ("odu1", 4), ("odu2", 5), ("odu3", 6), ("ethernet", 7), ("gigethernet", 8), ("tengigethernet", 9), ("gfp", 10), ("ethernettunnel", 11), ("ocgfiber", 12), ("odu2e", 13), ("otu2", 14), ("otu2e", 15), ("otu1e", 16), ("odu1e", 17), ("odu0", 18), ("oduflex4", 19), ("otu4", 20), ("vc3", 21), ("vc4", 22), ("vc44c", 23), ("vc416c", 24), ("vc464c", 25), ("odu4", 26), ("odu2f", 27), ("otu2f", 28), ("otu1f", 29), ("cgigethernet", 30), ("stm1ms", 31), ("stm4ms", 32), ("stm16ms", 33), ("stm64ms", 34), ("fiber100g", 40), ("multifiber3", 41), ("multifiber10g10", 42), ("multifiber7", 43), ("fiber100g4", 44), ("fiber100g10", 45))

class CyanLoopbackControlTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 3))
    namedValues = NamedValues(("disabled", 0), ("facilitylpbk", 1), ("terminallpbk", 3))

class CyanNationalizationTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("itu", 1), ("ansi", 2))

class CyanNimTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("terminating", 0), ("monitoring", 1))

class CyanNoYesTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("no", 0), ("yes", 1))

class CyanOffOnTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("off", 0), ("on", 1), ("unknown", 2))

class CyanOpStateQualTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("au", 1), ("ma", 2), ("auma", 3), ("aurst", 4), ("maanr", 5), ("nr", 6), ("anr", 7), ("rst", 8), ("anrst", 9))

class CyanOpStateTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("is", 1), ("oos", 2))

class CyanOpuPayloadTypeTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254), SingleValueConstraint(255, 256, 257, 258))
    namedValues = NamedValues(("experimental", 0), ("expmap", 1), ("asynchcbrmap", 2), ("synchcbrmap", 3), ("atmmap", 4), ("gfpmap", 5), ("vc", 6), ("opu01000bxmap", 7), ("fc1200mapodu2e", 8), ("gfpmapextendedopu2", 9), ("stm1mapodu0", 10), ("stm4mapodu0", 11), ("fc100mapodu0", 12), ("fc200mapodu1", 13), ("fc400mapoduflex", 14), ("fc800mapoduflex", 15), ("bitstreamwithtiming", 16), ("bitstreamwotiming", 17), ("ibSdrIntoOduflex", 18), ("ibDdrIntoOduflex", 19), ("ibQdrIntoOduflex", 20), ("sdiIntoOpu0", 21), ("sdi1g4851g001IntoOpu1", 22), ("sdi1g485IntoOpu1", 23), ("sdi2g9701g001IntoOpuflex", 24), ("sdi2g970IntoOpuflex", 25), ("sbconEsconIntoOpu0", 26), ("dvbAsiIntoOpu0", 27), ("fc1600mapoduflex", 28), ("undef1d", 29), ("undef1e", 30), ("undef1f", 31), ("odumultiplex", 32), ("odumultiplexgmp", 33), ("undef22", 34), ("undef23", 35), ("undef24", 36), ("undef25", 37), ("undef26", 38), ("undef27", 39), ("undef28", 40), ("undef29", 41), ("undef2a", 42), ("undef2b", 43), ("undef2c", 44), ("undef2d", 45), ("undef2e", 46), ("undef2f", 47), ("undef30", 48), ("undef31", 49), ("undef32", 50), ("undef33", 51), ("undef34", 52), ("undef35", 53), ("undef36", 54), ("undef37", 55), ("undef38", 56), ("undef39", 57), ("undef3a", 58), ("undef3b", 59), ("undef3c", 60), ("undef3d", 61), ("undef3e", 62), ("undef3f", 63), ("undef40", 64), ("undef41", 65), ("undef42", 66), ("undef43", 67), ("undef44", 68), ("undef45", 69), ("undef46", 70), ("undef47", 71), ("undef48", 72), ("undef49", 73), ("undef4a", 74), ("undef4b", 75), ("undef4c", 76), ("undef4d", 77), ("undef4e", 78), ("undef4f", 79), ("undef50", 80), ("undef51", 81), ("undef52", 82), ("undef53", 83), ("undef54", 84), ("notavailablelck", 85), ("undef56", 86), ("undef57", 87), ("undef58", 88), ("undef59", 89), ("undef5a", 90), ("undef5b", 91), ("undef5c", 92), ("undef5d", 93), ("undef5e", 94), ("undef5f", 95), ("undef60", 96), ("undef61", 97), ("undef62", 98), ("undef63", 99), ("undef64", 100), ("undef65", 101), ("notavailableoci", 102), ("undef67", 103), ("undef68", 104), ("undef69", 105), ("undef6a", 106), ("undef6b", 107), ("undef6c", 108), ("undef6d", 109), ("undef6e", 110), ("undef6f", 111), ("undef70", 112), ("undef71", 113), ("undef72", 114), ("undef73", 115), ("undef74", 116), ("undef75", 117), ("undef76", 118), ("undef77", 119), ("undef78", 120), ("undef79", 121), ("undef7a", 122), ("undef7b", 123), ("undef7c", 124), ("undef7d", 125), ("undef7e", 126), ("undef7f", 127), ("reserved80", 128), ("reserved81", 129), ("reserved82", 130), ("reserved83", 131), ("reserved84", 132), ("reserved85", 133), ("reserved86", 134), ("reserved87", 135), ("reserved88", 136), ("reserved89", 137), ("reserved8a", 138), ("reserved8b", 139), ("reserved8c", 140), ("reserved8d", 141), ("fc800mapodu2", 142), ("bittransparent", 143), ("undef90", 144), ("undef91", 145), ("undef92", 146), ("undef93", 147), ("undef94", 148), ("undef95", 149), ("undef96", 150), ("undef97", 151), ("undef98", 152), ("undef99", 153), ("undef9a", 154), ("undef9b", 155), ("undef9c", 156), ("undef9d", 157), ("undef9e", 158), ("undef9f", 159), ("undefA0", 160), ("undefA1", 161), ("undefA2", 162), ("undefA3", 163), ("undefA4", 164), ("undefA5", 165), ("undefA6", 166), ("undefA7", 167), ("undefA8", 168), ("undefA9", 169), ("undefAa", 170), ("undefAb", 171), ("undefAc", 172), ("undefAd", 173), ("undefAe", 174), ("undefAf", 175), ("undefB0", 176), ("undefB1", 177), ("undefB2", 178), ("undefB3", 179), ("undefB4", 180), ("undefB5", 181), ("undefB6", 182), ("undefB7", 183), ("undefB8", 184), ("undefB9", 185), ("undefBa", 186), ("undefBb", 187), ("undefBc", 188), ("undefBd", 189), ("undefBe", 190), ("undefBf", 191), ("undefC0", 192), ("undefC1", 193), ("undefC2", 194), ("undefC3", 195), ("undefC4", 196), ("undefC5", 197), ("undefC6", 198), ("undefC7", 199), ("undefC8", 200), ("undefC9", 201), ("undefCa", 202), ("undefCb", 203), ("undefCc", 204), ("undefCd", 205), ("undefCe", 206), ("undefCf", 207), ("undefD0", 208), ("undefD1", 209), ("undefD2", 210), ("undefD3", 211), ("undefD4", 212), ("undefD5", 213), ("undefD6", 214), ("undefD7", 215), ("undefD8", 216), ("undefD9", 217), ("undefDa", 218), ("undefDb", 219), ("undefDc", 220), ("undefDd", 221), ("undefDe", 222), ("undefDf", 223), ("undefE0", 224), ("undefE1", 225), ("undefE2", 226), ("undefE3", 227), ("undefE4", 228), ("undefE5", 229), ("undefE6", 230), ("undefE7", 231), ("undefE8", 232), ("undefE9", 233), ("undefEa", 234), ("undefEb", 235), ("undefEc", 236), ("undefEd", 237), ("undefEe", 238), ("undefEf", 239), ("undefF0", 240), ("undefF1", 241), ("undefF2", 242), ("undefF3", 243), ("undefF4", 244), ("undefF5", 245), ("undefF6", 246), ("undefF7", 247), ("undefF8", 248), ("undefF9", 249), ("undefFa", 250), ("undefFb", 251), ("undefFc", 252), ("nulltest", 253), ("prbstest", 254)) + NamedValues(("notavailableais", 255), ("notavailablefault", 256), ("unstable", 257), ("nim", 258))

class CyanPowerClassTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("powerclass1", 0), ("powerclass2", 1), ("powerclass3", 2), ("powerclass4", 3))

class CyanRelayTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("rsOpen", 0), ("rsClose", 1))

class CyanSdhSnSignalLabelTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 18, 19, 20, 21, 22, 24, 26, 27, 254))
    namedValues = NamedValues(("unequipped", 0), ("equippedNonspecific", 1), ("vtStructured", 2), ("lockedVtMode", 3), ("asyncDs3Mapping", 4), ("asyncDs4naMapping", 18), ("atmMapping", 19), ("dqdbMapping", 20), ("asyncFddiMapping", 21), ("hdlcOverSonetMapping", 22), ("hdlcLapsMapping", 24), ("xgeWan", 26), ("gfp", 27), ("o181TestSignalMapping", 254))

class CyanSecServiceStateTc(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("nalm", 0), ("act", 1), ("ains", 2), ("busy", 3), ("blkd", 4), ("cema", 5), ("discd", 6), ("dsbld", 7), ("ex", 8), ("faf", 9), ("flt", 10), ("frcd", 11), ("idle", 12), ("idlerx", 13), ("idletx", 14), ("inhip", 15), ("lkdo", 16), ("mea", 17), ("mt", 18), ("lpbk", 19), ("sdee", 20), ("sdea", 21), ("sder", 22), ("sdeo", 23), ("sdel", 24), ("sgel", 25), ("sgeo", 26), ("sgea", 27), ("sger", 28), ("swdl", 29), ("swul", 30), ("uas", 31), ("ueq", 32), ("unavail", 33), ("sgml", 41), ("sgmo", 42), ("sgma", 43), ("sgmr", 44))

class CyanSsBitsTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2))
    namedValues = NamedValues(("ss00", 0), ("ss10", 2))

class CyanTPConnectionStateTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("tpcsSourceConnected", 1), ("tpcsSinkConnected", 2), ("tpcsBiConnected", 3), ("tpcsNotConnected", 4))

class CyanTimezoneTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27))
    namedValues = NamedValues(("utc", 0), ("americaNewYork", 1), ("americaDetroit", 2), ("americaKentuckyLouisville", 3), ("americaKentuckyMonticello", 4), ("americaIndianaIndianapolis", 5), ("americaIndianaVincennes", 6), ("americaIndianaKnox", 7), ("americaIndianaWinamac", 8), ("americaIndianaMarengo", 9), ("americaIndianaVevay", 10), ("americaChicago", 11), ("americaIndianaTellCity", 12), ("americaIndianaPetersburg", 13), ("americaMenominee", 14), ("americaNorthDakotaCenter", 15), ("americaNorthDakotaNewSalem", 16), ("americaDenver", 17), ("americaBoise", 18), ("americaShiprock", 19), ("americaPhoenix", 20), ("americaLosAngeles", 21), ("americaAnchorage", 22), ("americaJuneau", 23), ("americaYakutat", 24), ("americaNome", 25), ("americaAdak", 26), ("pacificHonolulu", 27))

class CyanTxControlTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("off", 0), ("on", 1), ("als", 2))

class CyanWdmTypeTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("nonwdm", 0), ("cwdm", 1), ("lanwdm", 2), ("dwdm200gGrid", 3), ("dwdm100gGrid", 4), ("dwdm50gGrid", 5), ("dwdm25gGrid", 6), ("otherwdm", 7))

class CyanXGOSignalTypeTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(32, 33, 34, 22, 23))
    namedValues = NamedValues(("otu2", 32), ("otu2e", 33), ("otu1e", 34), ("tp10gelan", 22), ("tp10gewan", 23))

class CyanXcvrConnectorCodeTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 34, 32, 33))
    namedValues = NamedValues(("unknownorunspecified", 0), ("sc", 1), ("fibrechannelstyle1Copper", 2), ("fibrechannelstyle2Copper", 3), ("bncTnc", 4), ("fibrechannelcoax", 5), ("fiberjack", 6), ("lc", 7), ("mtRj", 8), ("mu", 9), ("sg", 10), ("opticalpigtail", 11), ("mpoParalleloptic", 12), ("rj45", 34), ("hssdcIi", 32), ("copperpigtail", 33))

class CyanXcvrIdentifierTc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("unknownUnspecified", 0), ("gbic", 1), ("modulesolderedtomotherboard", 2), ("sfpOrSfpplus", 3), ("xbi300pin", 4), ("xenpak", 5), ("xfp", 6), ("xff", 7), ("xfpE", 8), ("xpak", 9), ("x2", 10), ("dwdmSfp", 11), ("qsfp", 12), ("qsfpPlus", 13), ("cfp", 14), ("cxp", 15), ("msa100glh", 16), ("cfp2", 17), ("cfp4", 18))

mibBuilder.exportSymbols("CYAN-TC-MIB", CyanOpStateTc=CyanOpStateTc, CyanNoYesTc=CyanNoYesTc, CyanSdhSnSignalLabelTc=CyanSdhSnSignalLabelTc, CyanTPConnectionStateTc=CyanTPConnectionStateTc, CyanChannelIdTc=CyanChannelIdTc, CyanNimTc=CyanNimTc, CyanEnDisabledTc=CyanEnDisabledTc, CyanXGOSignalTypeTc=CyanXGOSignalTypeTc, CyanWdmTypeTc=CyanWdmTypeTc, CyanActvStdbyTc=CyanActvStdbyTc, CyanLEDTc=CyanLEDTc, CyanNationalizationTc=CyanNationalizationTc, CyanXcvrIdentifierTc=CyanXcvrIdentifierTc, cyanTCModule=cyanTCModule, CyanOpuPayloadTypeTc=CyanOpuPayloadTypeTc, CyanGfpUpiTc=CyanGfpUpiTc, CyanTimezoneTc=CyanTimezoneTc, CyanAugStructureTc=CyanAugStructureTc, CyanLoopbackControlTc=CyanLoopbackControlTc, CyanOffOnTc=CyanOffOnTc, CyanTxControlTc=CyanTxControlTc, CyanXcvrConnectorCodeTc=CyanXcvrConnectorCodeTc, CyanFppSubTypeTc=CyanFppSubTypeTc, PYSNMP_MODULE_ID=cyanTCModule, CyanSecServiceStateTc=CyanSecServiceStateTc, CyanOpStateQualTc=CyanOpStateQualTc, CyanPowerClassTc=CyanPowerClassTc, CyanAdminStateTc=CyanAdminStateTc, CyanFppTypeTc=CyanFppTypeTc, CyanRelayTc=CyanRelayTc, CyanSsBitsTc=CyanSsBitsTc, CyanLayerRateTc=CyanLayerRateTc, CyanFecModeTc=CyanFecModeTc)
