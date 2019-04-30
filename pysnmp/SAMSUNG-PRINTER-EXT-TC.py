#
# PySNMP MIB module SAMSUNG-PRINTER-EXT-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SAMSUNG-PRINTER-EXT-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 20:52:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
samsungCommonMIB, = mibBuilder.importSymbols("SAMSUNG-COMMON-MIB", "samsungCommonMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Counter64, Unsigned32, Gauge32, Bits, ModuleIdentity, iso, Integer32, NotificationType, ObjectIdentity, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Counter64", "Unsigned32", "Gauge32", "Bits", "ModuleIdentity", "iso", "Integer32", "NotificationType", "ObjectIdentity", "Counter32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
scmPrintTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54))
if mibBuilder.loadTexts: scmPrintTC.setLastUpdated('0407170000Z')
if mibBuilder.loadTexts: scmPrintTC.setOrganization('Samsung Common Management Interface Working Group')
class ScmPrtAuxSheetContent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notSpecified", 3), ("concise", 5), ("verbose", 6))

class ScmPrtAuxSheetType(TextualConvention, Integer32):
    reference = ' ISO/IEC 10175-1:1996(E) Section 9.10.2.2: Delivery-methods for hardcopy output logs Section 9.11.1: Auxiliary-sheet-package identifier'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, -2, -3, 1, 2, 101, 102))
    namedValues = NamedValues(("other", -1), ("unknown", -2), ("notSpecified", -3), ("jobSetStart", 1), ("jobSetEnd", 2), ("printerStartupSheet", 101), ("jobErrorSheet", 102))

class ScmPrtChannelType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 26, 27, 28, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43))
    namedValues = NamedValues(("other", 1), ("chSerialPort", 3), ("chParallelPort", 4), ("chIEEE1284Port", 5), ("chSCSIPort", 6), ("chAppleTalkPAP", 7), ("chLPDServer", 8), ("chNetwareRPrinter", 9), ("chNetwarePServer", 10), ("chPort9100", 11), ("chAppSocket", 12), ("chFTP", 13), ("chTFTP", 14), ("chDLCLLCPort", 15), ("chIBM3270", 16), ("chIBM5250", 17), ("chFax", 18), ("chIEEE1394", 19), ("chTransport1", 20), ("chCPAP", 21), ("chPCPrint", 26), ("chServerMessageBlock", 27), ("chPSM", 28), ("chSystemObjectManager", 31), ("chDECLAT", 32), ("chNPAP", 33), ("chUSB", 34), ("chIRDA", 35), ("chPrintXChange", 36), ("chPortTCP", 37), ("chBidirPortTCP", 38), ("chUNPP", 39), ("chAppleTalkADSP", 40), ("chPortSPX", 41), ("chPortHTTP", 42), ("chNDPS", 43))

class ScmPrtGroupSupport(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ScmPrtIETFPrintMIBGroupSupport(TextualConvention, Integer32):
    reference = 'See: IETF Printer MIB'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ScmPrtInterpreterLangFamily(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("langPCL", 3), ("langHPGL", 4), ("langPJL", 5), ("langPS", 6), ("langIPDS", 7), ("langPPDS", 8), ("langEscapeP", 9), ("langEpson", 10), ("langDDIF", 11), ("langInterpress", 12), ("langISO6429", 13), ("langLineData", 14), ("langMODCA", 15), ("langREGIS", 16), ("langSCS", 17), ("langSPDL", 18), ("langTEK4014", 19), ("langPDS", 20), ("langIGP", 21), ("langCodeV", 22), ("langDSCDSE", 23), ("langWPS", 24), ("langLN03", 25), ("langCCITT", 26), ("langQUIC", 27), ("langCPAP", 28), ("langDecPPL", 29), ("langSimpleText", 30), ("langNPAP", 31), ("langDOC", 32), ("langimPress", 33), ("langPinwriter", 34), ("langNPDL", 35), ("langNEC201PL", 36), ("langAutomatic", 37), ("langPages", 38), ("langLIPS", 39), ("langTIFF", 40), ("langDiagnostic", 41), ("langPSPrinter", 42), ("langCaPSL", 43), ("langEXCL", 44), ("langLCDS", 45), ("langXES", 46), ("langPCLXL", 47), ("langART", 48), ("langTIPSI", 49), ("langPrescribe", 50), ("langLinePrinter", 51), ("langIDP", 52), ("langXJCL", 53), ("langPDF", 54), ("langRPDL", 55), ("langIntermecIPL", 56), ("langUBIFingerprint", 57), ("langUBIDirectProtocol", 58))

class ScmPrtMediaTypeErrorPolicy(TextualConvention, Integer32):
    reference = ' See: ScmPrtPageSizeErrorPolicy'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 11))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notSpecified", 3), ("abortJob", 4), ("ignore", 5), ("interactWithOperator", 6), ("ignoreAfterTimeout", 11))

class ScmPrtMediumClassType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notSpecified", 3), ("northAmerica", 4), ("iso", 5), ("jis", 6))

class ScmPrtMediumSize(TextualConvention, Integer32):
    reference = 'ISO/IEC 10175-1:1996(E), Section 9.6.5: Medium-size'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 10, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1063, 1064, 1065, 1066, 1067, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1100, 1101, 1102, 1103, 1104))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notSpecified", 3), ("mediumSize13x18", 10), ("naLetter", 1000), ("naLegal", 1001), ("na10x13Envelope", 1002), ("na9x12Envelope", 1003), ("naNumber10Envelope", 1004), ("na7x9Envelope", 1005), ("na9x11Envelope", 1006), ("na10x14Envelope", 1007), ("naNumber9Envelope", 1008), ("na6x9Envelope", 1009), ("na10x15Envelope", 1010), ("a", 1011), ("b", 1012), ("c", 1013), ("d", 1014), ("e", 1015), ("monarchEnvelope", 1016), ("isoA0", 1020), ("isoA1", 1021), ("isoA2", 1022), ("isoA3", 1023), ("isoA4", 1024), ("isoA5", 1025), ("isoA6", 1026), ("isoA7", 1027), ("isoA8", 1028), ("isoA9", 1029), ("isoA10", 1030), ("isoB0", 1040), ("isoB1", 1041), ("isoB2", 1042), ("isoB3", 1043), ("isoB4", 1044), ("isoB5", 1045), ("isoB6", 1046), ("isoB7", 1047), ("isoB8", 1048), ("isoB9", 1049), ("isoB10", 1050), ("isoC3", 1063), ("isoC4", 1064), ("isoC5", 1065), ("isoC6", 1066), ("isoDesignatedLong", 1067), ("jisB0", 1080), ("jisB1", 1081), ("jisB2", 1082), ("jisB3", 1083), ("jisB4", 1084), ("jisB5", 1085), ("jisB6", 1086), ("jisB7", 1087), ("jisB8", 1088), ("jisB9", 1089), ("jisB10", 1090), ("executive", 1100), ("folio", 1101), ("invoice", 1102), ("ledger", 1103), ("quarto", 1104))

class ScmPrtOutputOffsetStackingType(TextualConvention, Integer32):
    reference = 'Printer MIB prtOutputOffsetStacking object'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notSpecified", 3), ("noOffset", 4), ("offsetOnJob", 5), ("offsetOnJobandCopy", 6))

class ScmPrtOutputStaplePosition(TextualConvention, Integer32):
    reference = " See: 'scmPrtOutputStaplePosDefault' See: 'scmPrtOutputStaplePosSupported'"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class ScmPrtPageSizeErrorPolicy(TextualConvention, Integer32):
    reference = ' PostScript Language Reference Manual, second edition, Adobe Systems Incorporated, pp 239-249. See: ScmPrtMediaTypeErrorPolicy'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notSpecified", 3), ("abortJob", 4), ("ignore", 5), ("interactWithOperator", 6), ("useNearestAndAdjust", 7), ("useNextLargerAndAdjust", 8), ("useNearest", 9), ("useNextLarger", 10), ("ignoreAfterTimeout", 11))

class ScmPrtPCLFontSource(TextualConvention, Integer32):
    reference = ' See: PJL Technical Reference Manual- FONTSOURCE'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 20, 41, 42, 43, 44, 45, 46, 47, 48, 49, 61, 62, 63, 64, 65, 66, 67, 68, 69, 80))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notSpecified", 3), ("internal", 20), ("romSimm1", 41), ("romSimm2", 42), ("romSimm3", 43), ("romSimm4", 44), ("romSimm5", 45), ("romSimm6", 46), ("romSimm7", 47), ("romSimm8", 48), ("romSimm9", 49), ("cartridge1", 61), ("cartridge2", 62), ("cartridge3", 63), ("cartridge4", 64), ("cartridge5", 65), ("cartridge6", 66), ("cartridge7", 67), ("cartridge8", 68), ("cartridge9", 69), ("permanentSoft", 80))

class ScmPrtPlex(TextualConvention, Integer32):
    reference = ' See: ISO/IEC 10175-1:1996(E) Section 9.3.2.16.2: Plex Section 9.3.2.19: Sides See: PostScript Language Reference Manual (2nd Edition) - PageSize, Duplex, Tumble See: PCL 5 Printer Language Technical Reference Manual Simplex/Duplex Print Command'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class ScmPrtPrintQuality(TextualConvention, Integer32):
    reference = ' ISO/IEC 10175-1:1996(E) Section 9.3.2.17: Print-quality'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notSpecified", 3), ("draft", 4), ("normal", 5), ("high", 6))

class ScmPrtPrintScreen(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notSpecified", 3), ("off", 4), ("mode850", 5), ("mode852", 6))

class ScmPrtTraySwitch(TextualConvention, Integer32):
    reference = ' See: scmPrtInterpTraySwitch See: scmPrtInputNextPrtInputIndex See: scmPrtInputAliasTable'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notSpecified", 3), ("off", 4), ("useScmPrtInputNextPrtInputIndex", 5), ("useScmPrtInputAliasTable", 6))

class ScmPrtGeneralMonoPrintOpt(TextualConvention, Integer32):
    reference = ' See: Phaser 7750 User Guide... for more information '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("optimizeForSpeed", 3), ("optimizeForEconomy", 4), ("notPresent", 5))

sCmPrintTCDummy = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999))
sCmPrtTCAuxSheetContent = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 1), ScmPrtAuxSheetContent())
if mibBuilder.loadTexts: sCmPrtTCAuxSheetContent.setStatus('current')
sCmPrtTCScmPrtAuxSheetType = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 2), ScmPrtAuxSheetType())
if mibBuilder.loadTexts: sCmPrtTCScmPrtAuxSheetType.setStatus('current')
sCmPrtTCTCChannelType = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 3), ScmPrtChannelType())
if mibBuilder.loadTexts: sCmPrtTCTCChannelType.setStatus('current')
sCmPrtTCGroupSupport = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 4), ScmPrtGroupSupport())
if mibBuilder.loadTexts: sCmPrtTCGroupSupport.setStatus('current')
sCmPrtTCIETFPrintMIBGroupSupport = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 5), ScmPrtIETFPrintMIBGroupSupport())
if mibBuilder.loadTexts: sCmPrtTCIETFPrintMIBGroupSupport.setStatus('current')
sCmPrtTCInterpreterLangFamily = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 6), ScmPrtInterpreterLangFamily())
if mibBuilder.loadTexts: sCmPrtTCInterpreterLangFamily.setStatus('current')
sCmPrtTCMediaTypeErrorPolicy = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 7), ScmPrtMediaTypeErrorPolicy())
if mibBuilder.loadTexts: sCmPrtTCMediaTypeErrorPolicy.setStatus('current')
sCmPrtTCMediumClassType = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 8), ScmPrtMediumClassType())
if mibBuilder.loadTexts: sCmPrtTCMediumClassType.setStatus('current')
sCmPrtTCMediumSize = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 9), ScmPrtMediumSize())
if mibBuilder.loadTexts: sCmPrtTCMediumSize.setStatus('current')
sCmPrtTCOutputOffsetStackingType = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 10), ScmPrtOutputOffsetStackingType())
if mibBuilder.loadTexts: sCmPrtTCOutputOffsetStackingType.setStatus('current')
sCmPrtOutputStaplePosition = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 11), ScmPrtOutputStaplePosition())
if mibBuilder.loadTexts: sCmPrtOutputStaplePosition.setStatus('current')
sCmPrtTCPageSizeErrorPolicy = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 12), ScmPrtPageSizeErrorPolicy())
if mibBuilder.loadTexts: sCmPrtTCPageSizeErrorPolicy.setStatus('current')
sCmPrtTCPCLFontSource = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 13), ScmPrtPCLFontSource())
if mibBuilder.loadTexts: sCmPrtTCPCLFontSource.setStatus('current')
sCmPrtTCPlex = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 14), ScmPrtPlex())
if mibBuilder.loadTexts: sCmPrtTCPlex.setStatus('current')
sCmPrtTCPrintQuality = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 15), ScmPrtPrintQuality())
if mibBuilder.loadTexts: sCmPrtTCPrintQuality.setStatus('current')
sCmPrtTCPrintScreen = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 16), ScmPrtPrintScreen())
if mibBuilder.loadTexts: sCmPrtTCPrintScreen.setStatus('current')
sCmPrtTCTraySwitch = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 17), ScmPrtTraySwitch())
if mibBuilder.loadTexts: sCmPrtTCTraySwitch.setStatus('current')
sCmPrtTCGeneralMonoPrintOpt = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 18), ScmPrtGeneralMonoPrintOpt())
if mibBuilder.loadTexts: sCmPrtTCGeneralMonoPrintOpt.setStatus('current')
mibBuilder.exportSymbols("SAMSUNG-PRINTER-EXT-TC", PYSNMP_MODULE_ID=scmPrintTC, sCmPrtTCPrintQuality=sCmPrtTCPrintQuality, sCmPrtTCTCChannelType=sCmPrtTCTCChannelType, ScmPrtAuxSheetType=ScmPrtAuxSheetType, ScmPrtTraySwitch=ScmPrtTraySwitch, ScmPrtGroupSupport=ScmPrtGroupSupport, ScmPrtMediaTypeErrorPolicy=ScmPrtMediaTypeErrorPolicy, sCmPrtTCGeneralMonoPrintOpt=sCmPrtTCGeneralMonoPrintOpt, sCmPrtTCPlex=sCmPrtTCPlex, sCmPrtOutputStaplePosition=sCmPrtOutputStaplePosition, sCmPrtTCPCLFontSource=sCmPrtTCPCLFontSource, ScmPrtOutputStaplePosition=ScmPrtOutputStaplePosition, ScmPrtMediumSize=ScmPrtMediumSize, sCmPrtTCScmPrtAuxSheetType=sCmPrtTCScmPrtAuxSheetType, ScmPrtInterpreterLangFamily=ScmPrtInterpreterLangFamily, sCmPrtTCInterpreterLangFamily=sCmPrtTCInterpreterLangFamily, ScmPrtMediumClassType=ScmPrtMediumClassType, sCmPrtTCGroupSupport=sCmPrtTCGroupSupport, ScmPrtPrintQuality=ScmPrtPrintQuality, sCmPrtTCMediumSize=sCmPrtTCMediumSize, ScmPrtPageSizeErrorPolicy=ScmPrtPageSizeErrorPolicy, ScmPrtPlex=ScmPrtPlex, ScmPrtPCLFontSource=ScmPrtPCLFontSource, sCmPrtTCOutputOffsetStackingType=sCmPrtTCOutputOffsetStackingType, ScmPrtChannelType=ScmPrtChannelType, ScmPrtAuxSheetContent=ScmPrtAuxSheetContent, ScmPrtIETFPrintMIBGroupSupport=ScmPrtIETFPrintMIBGroupSupport, sCmPrintTCDummy=sCmPrintTCDummy, ScmPrtPrintScreen=ScmPrtPrintScreen, scmPrintTC=scmPrintTC, sCmPrtTCPageSizeErrorPolicy=sCmPrtTCPageSizeErrorPolicy, ScmPrtOutputOffsetStackingType=ScmPrtOutputOffsetStackingType, sCmPrtTCMediumClassType=sCmPrtTCMediumClassType, sCmPrtTCIETFPrintMIBGroupSupport=sCmPrtTCIETFPrintMIBGroupSupport, ScmPrtGeneralMonoPrintOpt=ScmPrtGeneralMonoPrintOpt, sCmPrtTCMediaTypeErrorPolicy=sCmPrtTCMediaTypeErrorPolicy, sCmPrtTCAuxSheetContent=sCmPrtTCAuxSheetContent, sCmPrtTCTraySwitch=sCmPrtTCTraySwitch, sCmPrtTCPrintScreen=sCmPrtTCPrintScreen)
