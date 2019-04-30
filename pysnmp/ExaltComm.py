#
# PySNMP MIB module ExaltComm (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ExaltComm
# Produced by pysmi-0.3.4 at Mon Apr 29 18:52:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, Counter32, Unsigned32, enterprises, Bits, ObjectIdentity, Gauge32, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "Counter32", "Unsigned32", "enterprises", "Bits", "ObjectIdentity", "Gauge32", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "IpAddress", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class RadioSourceT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("radioA", 1), ("radioB", 2))

class BandwidthT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1750, 3500, 5000, 7000, 8000, 10000, 12500, 13750, 14000, 16000, 20000, 25000, 27500, 28000, 29650, 30000, 32000, 40000, 50000, 55000, 56000, 59300, 60000, 64000, 80000))
    namedValues = NamedValues(("khz1750", 1750), ("khz3500", 3500), ("khz5000", 5000), ("khz7000", 7000), ("khz8000", 8000), ("khz10000", 10000), ("khz12500", 12500), ("khz13750", 13750), ("khz14000", 14000), ("khz16000", 16000), ("khz20000", 20000), ("kgz25000", 25000), ("khz27500", 27500), ("khz28000", 28000), ("khz29650", 29650), ("khz30000", 30000), ("khz32000", 32000), ("khz40000", 40000), ("khz50000", 50000), ("khz55000", 55000), ("khz56000", 56000), ("khz59300", 59300), ("khz60000", 60000), ("khz64000", 64000), ("khz80000", 80000))

class ModulationT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 5, 2, 3, 4, 6))
    namedValues = NamedValues(("mQPSK", 0), ("m16QAM", 1), ("m32QAM", 5), ("m64QAM", 2), ("m128QAM", 3), ("m256QAM", 4), ("m512QAM", 6))

class LinkDistanceT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 5, 10, 20, 50))
    namedValues = NamedValues(("under2", 2), ("under5", 5), ("under10", 10), ("under20", 20), ("under50", 50))

class TddFrameSizeT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(5, 10, 20, 25, 40, 50))
    namedValues = NamedValues(("tdd05", 5), ("tdd10", 10), ("tdd20", 20), ("tdd25", 25), ("tdd40", 40), ("tdd50", 50))

class ExtAlarmsT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("alarmOnCLOSE", 1), ("alarmOnOPEN", 2))

class EthMainStatusT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("enableWithMute", 0), ("enableNOmute", 1), ("disableAlarm", 2))

class EthAuxStatusT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("enableAlarm", 0), ("disableAlarm", 1))

class EthPortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("full100", 0), ("full10", 1), ("half100", 2), ("half10", 3), ("auto", 4))

class GbeEthPortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("full1000", 1), ("half1000", 2), ("full100", 3), ("half100", 4), ("full10", 5), ("half10", 6), ("auto", 7))

class AuxNmsMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("inBand", 1), ("outBand", 2))

class EnableStatusT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disable", 0), ("enable", 1))

class EthernetMgmtTypeT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("inBand", 0), ("outOfBand", 1), ("portToPort", 2), ("legacy", 3), ("advanced", 4))

class MhsRoleT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notDefined", 0), ("primary", 1), ("secondary", 2))

class MhsLockOnT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("noLock", 0), ("lockOnline", 1), ("lockStandby", 2))

class MhsTimeoutT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("infinite", 0), ("twentySeconds", 1), ("tenMinutes", 2))

class Te1StatusT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class Te1LboT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4))
    namedValues = NamedValues(("notAvail", -1), ("lbo0to133", 0), ("lbo133to266", 1), ("lbo266to399", 2), ("lbo399to533", 3), ("lbo533to655", 4))

class Te1LineCodeT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1))
    namedValues = NamedValues(("notAvail", -1), ("b8zs", 0), ("ami", 1))

class Te1LoopBackModeT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("lbDisabled", 0), ("lbExtLocal", 1), ("lbExtRemote", 2), ("lbInternal", 3))

class AlarmLevelT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("almNORMAL", 0), ("almMINOR", 1), ("almMAJOR", 2), ("almDisable", 3), ("almNotAvailable", 4), ("almClearChanel", 5), ("almNonOccupant", 6))

class BandSelectT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("ghz53", 0), ("ghz54", 1), ("ghz58", 2))

class FreqGroupT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("all", 0), ("preferred", 1))

class Led4ColorT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 85, 102, 119, 153, 170, 187, 221, 238, 255))
    namedValues = NamedValues(("ledOFF", 0), ("redSlowBlink", 85), ("yellowSlowBlink", 102), ("greenSlowBlink", 119), ("redFastBlink", 153), ("yellowFastBlink", 170), ("greenFastBlink", 187), ("redON", 221), ("yellowON", 238), ("greenON", 255))

class RadioFreq24T(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(2406, 2468)

class RadioFreq5gT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(5260, 5332), ValueRangeConstraint(5731, 5844), )
class RadioTxPwr24T(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(70, 270)

class RadioTxPwr5gT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-70, 240)

class RadioTxPwr7gT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(30, 260)

class RadioTxPwr8gT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(30, 260)

class RadioTxPwr11gT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 260)

class RadioTxPwrHP11gT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(100, 290)

class RadioTxPwr13gT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 260)

class RadioTxPwr15gT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 260)

class RadioTxPwr18gT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 230)

class RadioTxPwr23gT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 230)

class RadioTxPwr28gT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 230)

class RadioTxPwr38gT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 210)

class RadioTxPwr42gT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 230)

class DiplexerConfigG2T(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 7))
    namedValues = NamedValues(("unconfigured", 0), ("diplexer701", 701), ("diplexer702", 702), ("diplexer703", 703), ("diplexer704", 704), ("diplexer705", 705), ("diplexer706", 706), ("diplexer707", 707), ("diplexer708", 708), ("diplexer709", 709), ("diplexer710", 710), ("diplexer711", 711), ("diplexer712", 712), ("diplexer713", 713), ("diplexer714", 714), ("diplexer715", 715), ("diplexer716", 716), ("diplexer717", 717), ("diplexer718", 718), ("diplexer719", 719), ("diplexer720", 720), ("diplexer721", 721), ("diplexer722", 722), ("diplexer723", 723), ("diplexer724", 724), ("diplexer725", 725), ("diplexer726", 726), ("diplexer727", 727), ("diplexer728", 728), ("diplexer729", 729), ("diplexer730", 730), ("diplexer731", 731), ("diplexer732", 732), ("diplexer733", 733), ("diplexer734", 734), ("diplexer735", 735), ("diplexer736", 736), ("diplexer737", 737), ("diplexer738", 738), ("diplexer739", 739), ("diplexer740", 740), ("diplexer741", 741), ("diplexer742", 742), ("diplexer743", 743), ("diplexer744", 744), ("diplexer745", 745), ("diplexer746", 746), ("diplexer747", 747), ("diplexer748", 748), ("diplexer749", 749), ("diplexer750", 750), ("diplexer751", 751), ("diplexer752", 752), ("diplexer753", 753), ("diplexer754", 754), ("diplexer755", 755), ("diplexer756", 756), ("diplexer757", 757), ("diplexer758", 758), ("diplexer759", 759), ("diplexer760", 760), ("diplexer761", 761), ("diplexer762", 762), ("diplexer763", 763), ("diplexer764", 764), ("diplexer765", 765), ("diplexer766", 766), ("diplexer767", 767), ("diplexer768", 768), ("diplexer769", 769), ("diplexer770", 770), ("diplexer771", 771), ("diplexer772", 772), ("diplexer773", 773), ("diplexer774", 774), ("diplexer775", 775), ("diplexer776", 776), ("diplexer777", 777), ("diplexer778", 778), ("diplexer779", 779), ("diplexer780", 780), ("diplexer781", 781), ("diplexer782", 782), ("diplexer783", 783), ("diplexer784", 784), ("diplexer785", 785), ("diplexer786", 786), ("diplexer787", 787), ("diplexer788", 788), ("diplexer789", 789), ("diplexer790", 790), ("diplexer791", 791), ("diplexer792", 792), ("diplexer793", 793), ("diplexer794", 794), ("diplexer795", 795), ("diplexer796", 796), ("diplexer797", 797), ("diplexer798", 798), ("diplexer799", 799), ("diplexer800", 800), ("diplexer801", 801), ("diplexer802", 802), ("diplexer803", 803), ("diplexer804", 804), ("diplexer805", 805), ("diplexer806", 806), ("diplexer807", 807), ("diplexer808", 808), ("diplexer809", 809), ("diplexer810", 810), ("diplexer811", 811), ("diplexer812", 812), ("diplexer813", 813), ("diplexer814", 814), ("diplexer815", 815), ("diplexer816", 816), ("diplexer817", 817), ("diplexer818", 818), ("diplexer819", 819), ("diplexer820", 820), ("diplexer821", 821), ("diplexer822", 822), ("diplexer823", 823), ("diplexer824", 824), ("diplexer825", 825), ("diplexer826", 826), ("diplexer827", 827), ("diplexer828", 828), ("diplexer829", 829), ("diplexer830", 830), ("diplexer831", 831), ("diplexer832", 832), ("diplexer833", 833), ("diplexer834", 834), ("diplexer835", 835), ("diplexer836", 836), ("diplexer837", 837), ("diplexer838", 838), ("diplexer839", 839), ("diplexer840", 840), ("diplexer841", 841), ("diplexer842", 842), ("diplexer843", 843), ("diplexer844", 844), ("diplexer845", 845), ("diplexer846", 846), ("diplexer847", 847), ("diplexer848", 848), ("diplexer849", 849), ("diplexer850", 850), ("diplexer851", 851), ("diplexer852", 852), ("diplexer853", 853), ("diplexer854", 854), ("diplexer855", 855), ("diplexer856", 856), ("diplexer857", 857), ("diplexer858", 858), ("diplexer859", 859), ("diplexer860", 860), ("diplexer861", 861), ("diplexer862", 862), ("diplexer863", 863), ("diplexer864", 864), ("diplexer865", 865), ("diplexer866", 866), ("other", 7))

class DiplexerConfigT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 125, 126, 127, 128, 129, 130, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 377, 378, 379, 380, 381, 382, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 7))
    namedValues = NamedValues(("unconfigured", 0), ("diplexer125", 125), ("diplexer126", 126), ("diplexer127", 127), ("diplexer128", 128), ("diplexer129", 129), ("diplexer130", 130), ("diplexer301", 301), ("diplexer302", 302), ("diplexer303", 303), ("diplexer304", 304), ("diplexer305", 305), ("diplexer306", 306), ("diplexer307", 307), ("diplexer308", 308), ("diplexer309", 309), ("diplexer310", 310), ("diplexer311", 311), ("diplexer312", 312), ("diplexer313", 313), ("diplexer314", 314), ("diplexer315", 315), ("diplexer316", 316), ("diplexer317", 317), ("diplexer318", 318), ("diplexer319", 319), ("diplexer320", 320), ("diplexer321", 321), ("diplexer322", 322), ("diplexer323", 323), ("diplexer324", 324), ("diplexer325", 325), ("diplexer326", 326), ("diplexer327", 327), ("diplexer328", 328), ("diplexer329", 329), ("diplexer330", 330), ("diplexer331", 331), ("diplexer332", 332), ("diplexer333", 333), ("diplexer334", 334), ("diplexer335", 335), ("diplexer336", 336), ("diplexer337", 337), ("diplexer338", 338), ("diplexer339", 339), ("diplexer340", 340), ("diplexer341", 341), ("diplexer342", 342), ("diplexer343", 343), ("diplexer344", 344), ("diplexer345", 345), ("diplexer346", 346), ("diplexer347", 347), ("diplexer348", 348), ("diplexer349", 349), ("diplexer350", 350), ("diplexer351", 351), ("diplexer352", 352), ("diplexer353", 353), ("diplexer354", 354), ("diplexer355", 355), ("diplexer356", 356), ("diplexer357", 357), ("diplexer358", 358), ("diplexer359", 359), ("diplexer360", 360), ("diplexer361", 361), ("diplexer362", 362), ("diplexer363", 363), ("diplexer364", 364), ("diplexer365", 365), ("diplexer366", 366), ("diplexer367", 367), ("diplexer368", 368), ("diplexer377", 377), ("diplexer378", 378), ("diplexer379", 379), ("diplexer380", 380), ("diplexer381", 381), ("diplexer382", 382), ("diplexer389", 389), ("diplexer390", 390), ("diplexer391", 391), ("diplexer392", 392), ("diplexer393", 393), ("diplexer394", 394), ("diplexer395", 395), ("diplexer396", 396), ("diplexer397", 397), ("diplexer398", 398), ("diplexer399", 399), ("diplexer400", 400), ("diplexer401", 401), ("diplexer402", 402), ("diplexer403", 403), ("diplexer404", 404), ("diplexer405", 405), ("diplexer406", 406), ("diplexer407", 407), ("diplexer408", 408), ("diplexer409", 409), ("diplexer410", 410), ("diplexer411", 411), ("diplexer412", 412), ("diplexer413", 413), ("diplexer414", 414), ("diplexer415", 415), ("diplexer416", 416), ("other", 7))

class RadioCollocSyncSourceT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("syncOFF", 0), ("syncGPS", 1), ("syncINTERNAL", 2))

class RadioCollocSyncTypeT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("syncAuto", 1), ("syncSrc", 2), ("syncSink", 3), ("syncNone", 4))

class VlanStatusT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("disabled", 0), ("enableBlkUtag", 1), ("enablePassUtag", 2), ("enableTagUtag", 3), ("enableMgmtOnly", 4))

class VlanIdT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4095)

class VlanGroupT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("groupNONE", 0), ("groupETH2", 1), ("groupPoE1", 2), ("groupETH2andPoE1", 3))

class TxOffsetT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 5000)

class AntPortT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("portONE", 1), ("portTWO", 2))

class PolarizationT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("portV", 1), ("portH", 2), ("portVplusH", 3))

class RslPortT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("portV", 1), ("portH", 2))

class BuzTimeoutT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("buzzerOFF", 0), ("buzzerTenMinute", 1), ("buzzerTwoHour", 2))

class FlyWheelT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("fwNormal", 0), ("fwInfinite", 1))

class TxDcycleT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("t20r80", 1), ("t35r65", 2), ("t50r50", 3), ("t65r35", 4), ("t80r20", 5))

class DfsEnableT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disable", 0), ("enable", 1))

class DfsAntGainT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(18, 38)

class QosModeT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("disable", 0), ("qos-mode-mac-da", 1), ("qos-mode-mac-sa", 2), ("qos-mode-vlan-id", 3), ("qos-mode-802-1p", 4), ("qos-mode-port", 5))

class QosTagT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class QosPriorityT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("priority0", 0), ("priority1", 1), ("priority2", 2), ("priority3", 3), ("priority4", 4), ("priority5", 5), ("priority6", 6), ("priority7", 7))

class QosQueueSizePercentT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 100)

class QosQueueSizeByteT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2097152)

class QosTtlT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(100, 100000)

class V35StatusT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class V35RateT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("v35Rate56K", 0), ("v35Rate64K", 1), ("v35Rate128K", 2), ("v35Rate256K", 3), ("v35Rate384K", 4), ("v35Rate512K", 5), ("v35Rate768K", 6), ("v35Rate1024K", 7), ("v35Rate1544K", 8), ("v35Rate2048K", 9))

class V35ClockInversionT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("txNormalRxNormal", 0), ("txInvertRxNormal", 1), ("txNormalRxInvert", 2), ("txInvertRxInvert", 3))

class V35TxClockT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("rxClock", 0), ("externalTxClock", 1), ("internalGenerator", 2))

class V35CTSHandshakeT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("handshakeAlwaysOn", 0), ("handshakeFollowRTS", 1))

class V35LoopBackModeT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("lbDisabled", 0), ("lbExtLocal", 1), ("lbExtRemote", 2), ("lbInternal", 3))

class DS3StatusT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class DS3LineCodeT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1))
    namedValues = NamedValues(("notAvail", -1), ("b8zs", 0), ("ami", 1))

class DS3LoopBackModeT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("lbDisabled", 0), ("lbExtLocal", 1), ("lbExtRemote", 2), ("lbInternal", 3))

class ExaltEnableT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disable", 0), ("enable", 1))

class AcmPolicyT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("conservative", 0), ("agressive", 1))

class AcmBaseModulationT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 6, 1, 5, 2, 3, 4))
    namedValues = NamedValues(("mQPSK", 0), ("m8PSK", 6), ("m16QAM", 1), ("m32QAM", 5), ("m64QAM", 2), ("m128QAM", 3), ("m256QAM", 4))

class AcmTargetModulationT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 5, 2, 3, 4, 6))
    namedValues = NamedValues(("m16QAM", 1), ("m32QAM", 5), ("m64QAM", 2), ("m128QAM", 3), ("m256QAM", 4), ("m512QAM", 6))

class AcmModulationT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-9999, 0, 7, 1, 5, 2, 3, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("notAvailable", -9999), ("mQPSK", 0), ("m8PSK", 7), ("m16QAM", 1), ("m32QAM", 5), ("m64QAM", 2), ("m128QAM", 3), ("m256QAM", 4), ("m512QAM", 6), ("mBPSK", 8), ("mQPSK", 9), ("m8PSK", 10), ("m32QAM", 11), ("m64QAM", 12), ("m128QAM", 13), ("m16QAM", 14), ("m512QAM", 15), ("mQPSK", 16), ("mBPSK", 17))

class TcmModulationT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-9999, 0, 1, 5, 2, 3, 4, 8, 9, 13, 10, 11, 12, 16, 17, 21, 18, 19, 20))
    namedValues = NamedValues(("notAvailable", -9999), ("mQPSKThru", 0), ("m16QAMThru", 1), ("m32QAMThru", 5), ("m64QAMThru", 2), ("m128QAMThru", 3), ("m256QAMThru", 4), ("mQPSKBase", 8), ("m16QAMBase", 9), ("m32QAMBase", 13), ("m64QAMBase", 10), ("m128QAMBase", 11), ("m256QAMBase", 12), ("mQPSKSysG", 16), ("m16QAMSysG", 17), ("m32QAMSysG", 21), ("m64QAMSysG", 18), ("m128QAMSysG", 19), ("m256QAMSysG", 20))

class FileTransferTypeT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("uploadFirmware", 0), ("uploadConfig", 1), ("uploadRDD", 2), ("downloadFirmware", 3), ("downloadConfig", 4), ("downloadMIBs", 5), ("downloadEventLogs", 6))

class FileTransferStartT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("noAction", 0), ("startTransfer", 1))

class PerformanceModeT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("maxThroughputMinLatency", 0), ("maxSystemGain", 1), ("balancedPerformance", 2))

class NtpClientEnableT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("disable", 0), ("enableWith1Server", 1), ("enableWith2Servers", 2), ("enableWith3Servers", 3), ("enableWith4Servers", 4))

class TimeZoneT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28))
    namedValues = NamedValues(("samoa", 0), ("hawaii", 1), ("alaska", 2), ("pacific", 3), ("arizona", 4), ("mountain", 5), ("central", 6), ("eastern", 7), ("east-Indiana", 8), ("atlantic", 9), ("uTC", 10), ("london", 11), ("berlin", 12), ("belgrade", 13), ("paris", 14), ("cairo", 15), ("helsinki", 16), ("baghdad", 17), ("moscow", 18), ("tehran", 19), ("kabul", 20), ("karachi", 21), ("bangkok", 22), ("shanghai", 23), ("taipei", 24), ("tokyo", 25), ("seoul", 26), ("sydney", 27), ("vladivostok", 28))

class SyslogEnableT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class SyslogFilterSelectT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("all", 0), ("minor", 1), ("minorMajorCritical", 2), ("major", 3), ("majorCritical", 4), ("critical", 5))

class DualRadioXpicEnableT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disable", 0), ("vertical", 1), ("horizontal", 2))

class MefEnableT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class MefMasterModeT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("auto", 0), ("forceMaster", 1), ("forceSlave", 2), ("notPresent", 3))

class MefIrgT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("r64kbps", 0), ("r128kbps", 1), ("r256kbps", 2), ("r512kbps", 3), ("r1000kbps", 4))

class MefMacT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("discard", 0), ("forward", 1))

class MefRateLimitTypeT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("kbps", 0), ("mbps", 1))

class MefRateLimitValueT(TextualConvention, Integer32):
    status = 'current'

exaltcommunications = MibIdentifier((1, 3, 6, 1, 4, 1, 25651))
mibBuilder.exportSymbols("ExaltComm", TddFrameSizeT=TddFrameSizeT, BuzTimeoutT=BuzTimeoutT, RadioFreq5gT=RadioFreq5gT, QosModeT=QosModeT, RadioTxPwr23gT=RadioTxPwr23gT, BandwidthT=BandwidthT, ExaltEnableT=ExaltEnableT, ExtAlarmsT=ExtAlarmsT, DfsAntGainT=DfsAntGainT, MefIrgT=MefIrgT, DfsEnableT=DfsEnableT, AlarmLevelT=AlarmLevelT, RslPortT=RslPortT, V35ClockInversionT=V35ClockInversionT, RadioTxPwr13gT=RadioTxPwr13gT, RadioTxPwr28gT=RadioTxPwr28gT, GbeEthPortMode=GbeEthPortMode, AuxNmsMode=AuxNmsMode, LinkDistanceT=LinkDistanceT, QosTagT=QosTagT, MefRateLimitValueT=MefRateLimitValueT, RadioCollocSyncTypeT=RadioCollocSyncTypeT, DiplexerConfigT=DiplexerConfigT, Led4ColorT=Led4ColorT, MhsTimeoutT=MhsTimeoutT, QosTtlT=QosTtlT, FlyWheelT=FlyWheelT, RadioTxPwr7gT=RadioTxPwr7gT, PolarizationT=PolarizationT, DS3StatusT=DS3StatusT, RadioTxPwr42gT=RadioTxPwr42gT, AcmTargetModulationT=AcmTargetModulationT, RadioTxPwr11gT=RadioTxPwr11gT, RadioSourceT=RadioSourceT, MefMasterModeT=MefMasterModeT, RadioTxPwr24T=RadioTxPwr24T, V35StatusT=V35StatusT, VlanIdT=VlanIdT, AcmPolicyT=AcmPolicyT, V35LoopBackModeT=V35LoopBackModeT, TimeZoneT=TimeZoneT, QosQueueSizePercentT=QosQueueSizePercentT, EthernetMgmtTypeT=EthernetMgmtTypeT, DiplexerConfigG2T=DiplexerConfigG2T, QosQueueSizeByteT=QosQueueSizeByteT, V35CTSHandshakeT=V35CTSHandshakeT, FreqGroupT=FreqGroupT, MefEnableT=MefEnableT, RadioTxPwr15gT=RadioTxPwr15gT, DS3LineCodeT=DS3LineCodeT, AntPortT=AntPortT, Te1LoopBackModeT=Te1LoopBackModeT, BandSelectT=BandSelectT, RadioTxPwrHP11gT=RadioTxPwrHP11gT, RadioTxPwr38gT=RadioTxPwr38gT, EnableStatusT=EnableStatusT, ModulationT=ModulationT, EthMainStatusT=EthMainStatusT, V35RateT=V35RateT, DualRadioXpicEnableT=DualRadioXpicEnableT, SyslogFilterSelectT=SyslogFilterSelectT, Te1LineCodeT=Te1LineCodeT, RadioTxPwr18gT=RadioTxPwr18gT, FileTransferTypeT=FileTransferTypeT, V35TxClockT=V35TxClockT, RadioTxPwr8gT=RadioTxPwr8gT, AcmBaseModulationT=AcmBaseModulationT, DS3LoopBackModeT=DS3LoopBackModeT, MefRateLimitTypeT=MefRateLimitTypeT, FileTransferStartT=FileTransferStartT, QosPriorityT=QosPriorityT, Te1StatusT=Te1StatusT, SyslogEnableT=SyslogEnableT, MefMacT=MefMacT, MhsRoleT=MhsRoleT, exaltcommunications=exaltcommunications, EthAuxStatusT=EthAuxStatusT, RadioFreq24T=RadioFreq24T, AcmModulationT=AcmModulationT, TxDcycleT=TxDcycleT, MhsLockOnT=MhsLockOnT, Te1LboT=Te1LboT, RadioCollocSyncSourceT=RadioCollocSyncSourceT, VlanStatusT=VlanStatusT, RadioTxPwr5gT=RadioTxPwr5gT, VlanGroupT=VlanGroupT, EthPortMode=EthPortMode, TcmModulationT=TcmModulationT, TxOffsetT=TxOffsetT, PerformanceModeT=PerformanceModeT, NtpClientEnableT=NtpClientEnableT)
