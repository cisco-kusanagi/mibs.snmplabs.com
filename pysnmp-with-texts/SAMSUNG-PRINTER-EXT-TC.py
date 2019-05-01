#
# PySNMP MIB module SAMSUNG-PRINTER-EXT-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SAMSUNG-PRINTER-EXT-TC
# Produced by pysmi-0.3.4 at Wed May  1 15:00:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
samsungCommonMIB, = mibBuilder.importSymbols("SAMSUNG-COMMON-MIB", "samsungCommonMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, TimeTicks, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, Unsigned32, ModuleIdentity, Gauge32, ObjectIdentity, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "TimeTicks", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "Unsigned32", "ModuleIdentity", "Gauge32", "ObjectIdentity", "NotificationType", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
scmPrintTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54))
if mibBuilder.loadTexts: scmPrintTC.setLastUpdated('0407170000Z')
if mibBuilder.loadTexts: scmPrintTC.setOrganization('Samsung Common Management Interface Working Group')
if mibBuilder.loadTexts: scmPrintTC.setContactInfo(' SCMI Editors E-Mail: wono.song@samsung.com -- -- ')
if mibBuilder.loadTexts: scmPrintTC.setDescription(' Version: 1.00 SCMI Extensions to Printer MIB Textual Conventions. This Module provides Samsung extensions of the IETF Printer MIB. Copyright (C) 2003-2004 Samsung Corporation. All Rights Reserved.')
class ScmPrtAuxSheetContent(TextualConvention, Integer32):
    description = ' Auxiliary sheets are added by the printing system and are not part of the actual print job. Examples include error pages and banner pages. This textual convention is used to specify the information content of auxiliary sheets.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notSpecified", 3), ("concise", 5), ("verbose", 6))

class ScmPrtAuxSheetType(TextualConvention, Integer32):
    reference = ' ISO/IEC 10175-1:1996(E) Section 9.10.2.2: Delivery-methods for hardcopy output logs Section 9.11.1: Auxiliary-sheet-package identifier'
    description = " Auxiliary sheets are added by the printing system and are not part of the actual print job. This attribute uniquely identifies an auxiliary-sheet, which includes the types jobErrorSheet and printerStartupSheet. 'printerStartupSheet' is a sheet printed shortly after power-up when the device is ready. Typical startup pages include test patterns and/or printer configuration information. 'jobErrorSheet' is a sheet printed with error messages generated during the printing of a job-result-set that is to be printed with the hardcopy output of that job-result-set, and should be printed on an ending sheet of the job-result-set, or some similar sheet. These sheets are not a part of any job-copy. If no error messages have been generated, the device need not print an extra page. The default for this page type should be 'On'. The following Auxiliary-sheet-package types can be specified either for a job component (job result set or job copy) or document (document result set or document copy). For now, only the jobSetStart package has been enumerated. 'jobSetStart' - Auxiliary-sheet starts each result-set Sometimes referred to as a jobBanner sheet 'jobSetEnd' - Auxiliary-sheet at the end of a result set "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, -2, -3, 1, 2, 101, 102))
    namedValues = NamedValues(("other", -1), ("unknown", -2), ("notSpecified", -3), ("jobSetStart", 1), ("jobSetEnd", 2), ("printerStartupSheet", 101), ("jobErrorSheet", 102))

class ScmPrtChannelType(TextualConvention, Integer32):
    description = ' This enumeration indicates the type of channel that is receiving jobs. This enumeration is being added to the IETF Printer MIB. This is an IETF type 2 enum.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 26, 27, 28, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43))
    namedValues = NamedValues(("other", 1), ("chSerialPort", 3), ("chParallelPort", 4), ("chIEEE1284Port", 5), ("chSCSIPort", 6), ("chAppleTalkPAP", 7), ("chLPDServer", 8), ("chNetwareRPrinter", 9), ("chNetwarePServer", 10), ("chPort9100", 11), ("chAppSocket", 12), ("chFTP", 13), ("chTFTP", 14), ("chDLCLLCPort", 15), ("chIBM3270", 16), ("chIBM5250", 17), ("chFax", 18), ("chIEEE1394", 19), ("chTransport1", 20), ("chCPAP", 21), ("chPCPrint", 26), ("chServerMessageBlock", 27), ("chPSM", 28), ("chSystemObjectManager", 31), ("chDECLAT", 32), ("chNPAP", 33), ("chUSB", 34), ("chIRDA", 35), ("chPrintXChange", 36), ("chPortTCP", 37), ("chBidirPortTCP", 38), ("chUNPP", 39), ("chAppleTalkADSP", 40), ("chPortSPX", 41), ("chPortHTTP", 42), ("chNDPS", 43))

class ScmPrtGroupSupport(TextualConvention, Integer32):
    description = ' The terse conformance statement of ALL mandatory, conditionally mandatory, and optional Printer MIB Extension object groups, specified in a bit-mask. The current set of values (which may be extended in the future) is given below: 1 : scmPrtBaseGroup -- 2**0 2 : scmPrtGeneralGroup -- 2**1 4 : scmPrtInputGroup -- 2**2 8 : scmPrtOutputGroup -- 2**3 16 : scmPrtChannelGroup -- 2**4 32 : scmPrtInterpreterGroup -- 2**5 64 : scmPrtInputAliasGroup -- 2**6 128 : scmPrtGeneralAuxSheetGroup -- 2**7 256 : scmPrtGeneralProdSpecificGroup -- 2**8 512 : scmPrtAuxPackageGroup -- 2**9 1024 : scmPrtChannelProdSpecificGroup -- 2**10 2048 : scmPrtInterpProdSpecificGroup -- 2**11 4096 : scmPrtInterpPCLGroup -- 2**12 8192 : scmPrtInterpPCLProdSpecificGroup -- 2**13 16384 : scmPrtMediumTypeSupportedGroup -- 2**14 Usage: Conforming management agents shall ALWAYS accurately report their support for SCMI Printer MIB Extensions object groups.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ScmPrtIETFPrintMIBGroupSupport(TextualConvention, Integer32):
    reference = 'See: IETF Printer MIB'
    description = ' The terse conformance statement of ALL mandatory, conditionally mandatory, and optional IETF Printer MIB object groups, specified in a bit-mask. The current set of values (which may be extended in the future) is given below: 1 : prtGeneralGroup -- 2**0 (mandatory) 2 : prtResponsiblePartyGroup -- 2**1 4 : prtInputGroup -- 2**2 (mandatory) 8 : prtExtendedInputGroup -- 2**3 16 : prtInputMediaGroup -- 2**4 32 : prtOutputGroup -- 2**5 (mandatory) 64 : prtExtendedOutputGroup -- 2**6 128 : prtOutputDimensionsGroup -- 2**7 256 : prtOutputFeaturesGroup -- 2**8 512 : prtMarkerGroup -- 2**9 (mandatory) 1024 : prtMarkerSuppliesGroup -- 2**10 2048 : prtMarkerColorantGroup -- 2**11 4096 : prtMediaPathGroup -- 2**12 (mandatory) 8192 : prtChannelGroup -- 2**13 (mandatory) 16384 : prtInterpreterGroup -- 2**14 (mandatory) 32768 : prtConsoleGroup -- 2**15 (mandatory) 65536 : prtAlertTableGroup -- 2**16 (mandatory) 131072 : prtAuxiliarySheetGroup -- 2**17 262144 : prtInputSwitchingGroup -- 2**18 Usage: Conforming management agents shall ALWAYS accurately report their support for IETF Printer MIB object groups.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ScmPrtInterpreterLangFamily(TextualConvention, Integer32):
    description = ' This enumeration indicates the type of interpreter that is receiving jobs. This enumeration is being added to the IETF Printer MIB. This value is an IETF type 2 enumeration.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("langPCL", 3), ("langHPGL", 4), ("langPJL", 5), ("langPS", 6), ("langIPDS", 7), ("langPPDS", 8), ("langEscapeP", 9), ("langEpson", 10), ("langDDIF", 11), ("langInterpress", 12), ("langISO6429", 13), ("langLineData", 14), ("langMODCA", 15), ("langREGIS", 16), ("langSCS", 17), ("langSPDL", 18), ("langTEK4014", 19), ("langPDS", 20), ("langIGP", 21), ("langCodeV", 22), ("langDSCDSE", 23), ("langWPS", 24), ("langLN03", 25), ("langCCITT", 26), ("langQUIC", 27), ("langCPAP", 28), ("langDecPPL", 29), ("langSimpleText", 30), ("langNPAP", 31), ("langDOC", 32), ("langimPress", 33), ("langPinwriter", 34), ("langNPDL", 35), ("langNEC201PL", 36), ("langAutomatic", 37), ("langPages", 38), ("langLIPS", 39), ("langTIFF", 40), ("langDiagnostic", 41), ("langPSPrinter", 42), ("langCaPSL", 43), ("langEXCL", 44), ("langLCDS", 45), ("langXES", 46), ("langPCLXL", 47), ("langART", 48), ("langTIPSI", 49), ("langPrescribe", 50), ("langLinePrinter", 51), ("langIDP", 52), ("langXJCL", 53), ("langPDF", 54), ("langRPDL", 55), ("langIntermecIPL", 56), ("langUBIFingerprint", 57), ("langUBIDirectProtocol", 58))

class ScmPrtMediaTypeErrorPolicy(TextualConvention, Integer32):
    reference = ' See: ScmPrtPageSizeErrorPolicy'
    description = " Controls interpreter behavior when the requested Media Type is not currently available. * The values 'other' and 'unknown' are deprecated for conforming implementations. * 'abortJob' will cause the interpreter to abort the job with an appropriate error condition. * 'ignore' will cause the job to be printed on the default media as specified by scmPrtInterpInputIndexDefault OR scmPrtInterpPaperSizeDefault OR any available media deemed appropriate by the implementation. No adjustment will be made to the image size. Exact semantics of this setting are product specific. * 'interactWithOperator' will cause the printer to interact with the operator to determine what to do. For example, display a message at the operator console requesting the desired media. The semantics of this policy vary among different products and environments. * 'ignoreAfterTimeout' will cause the job to be ignored same as 'ignore' above, but not till after scmPrtInterpErrorPolicyTimeout expires."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 11))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notSpecified", 3), ("abortJob", 4), ("ignore", 5), ("interactWithOperator", 6), ("ignoreAfterTimeout", 11))

class ScmPrtMediumClassType(TextualConvention, Integer32):
    description = ' Paper size classes for a printer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notSpecified", 3), ("northAmerica", 4), ("iso", 5), ("jis", 6))

class ScmPrtMediumSize(TextualConvention, Integer32):
    reference = 'ISO/IEC 10175-1:1996(E), Section 9.6.5: Medium-size'
    description = ' This attribute specifies the size of this medium by means of a pre-defined value. The medium size specified in this manner may be one of the standard sizes to which object identifiers have been assigned in ISO/IEC 10175 (DPA), or another applicable standard, or for which a value has been created. Enumerations for DPA defined medium sizes are derived by adding 1000 to the ISO/IEC 10175 enumerations. SCMI defined enumerations start at 10.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 10, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1063, 1064, 1065, 1066, 1067, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1100, 1101, 1102, 1103, 1104))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notSpecified", 3), ("mediumSize13x18", 10), ("naLetter", 1000), ("naLegal", 1001), ("na10x13Envelope", 1002), ("na9x12Envelope", 1003), ("naNumber10Envelope", 1004), ("na7x9Envelope", 1005), ("na9x11Envelope", 1006), ("na10x14Envelope", 1007), ("naNumber9Envelope", 1008), ("na6x9Envelope", 1009), ("na10x15Envelope", 1010), ("a", 1011), ("b", 1012), ("c", 1013), ("d", 1014), ("e", 1015), ("monarchEnvelope", 1016), ("isoA0", 1020), ("isoA1", 1021), ("isoA2", 1022), ("isoA3", 1023), ("isoA4", 1024), ("isoA5", 1025), ("isoA6", 1026), ("isoA7", 1027), ("isoA8", 1028), ("isoA9", 1029), ("isoA10", 1030), ("isoB0", 1040), ("isoB1", 1041), ("isoB2", 1042), ("isoB3", 1043), ("isoB4", 1044), ("isoB5", 1045), ("isoB6", 1046), ("isoB7", 1047), ("isoB8", 1048), ("isoB9", 1049), ("isoB10", 1050), ("isoC3", 1063), ("isoC4", 1064), ("isoC5", 1065), ("isoC6", 1066), ("isoDesignatedLong", 1067), ("jisB0", 1080), ("jisB1", 1081), ("jisB2", 1082), ("jisB3", 1083), ("jisB4", 1084), ("jisB5", 1085), ("jisB6", 1086), ("jisB7", 1087), ("jisB8", 1088), ("jisB9", 1089), ("jisB10", 1090), ("executive", 1100), ("folio", 1101), ("invoice", 1102), ("ledger", 1103), ("quarto", 1104))

class ScmPrtOutputOffsetStackingType(TextualConvention, Integer32):
    reference = 'Printer MIB prtOutputOffsetStacking object'
    description = ' Offset stacking types further refining that specified by the object prtOutputOffsetStacking in the Printer MIB. - offsetOnJob means that each job is offset but copies within the job are not offset. - offsetOnJobAndCopy means that there is an offset on job and copy boundaries.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notSpecified", 3), ("noOffset", 4), ("offsetOnJob", 5), ("offsetOnJobandCopy", 6))

class ScmPrtOutputStaplePosition(TextualConvention, Integer32):
    reference = " See: 'scmPrtOutputStaplePosDefault' See: 'scmPrtOutputStaplePosSupported'"
    description = " This Textual Convention enumerates possible staple positions. The staple positions enumerated are relative to the physical layout of the finishing device. The observer is on the front side of the finisher which is defined as for sheets passing through the finisher. The 'front' side is the side from which staples are pushed. The physical corners of the finishing device are specified by designating the corner of the finisher where a portrait long-edge fed sheet with english/left-to-right text is stapled as staplePosCorner1, and then the other corners are numbered in a counter-clockwise direction with the observer on the front side of the finisher. 'staplePosCorner1', 'staplePosCorner2', 'staplePosCorner3', and 'staplePosCorner4' indicate a single staple in the specified corner. This object does not specify the angle of the staple, e.g. 90, 45 or zero degrees. 'stapleEdge...' indicates multiple staples on the edge specified. 'stapleEdge12' is the edge which include Corner1 and Corner2. The current set of values (which may be extended in the future) is given below: 1 : staplePosCorner1 -- 2**0 2 : staplePosCorner2 -- 2**1 4 : staplePosCorner3 -- 2**2 8 : staplePosCorner4 -- 2**3 16 : stapleEdge12 -- 2**4 32 : stapleEdge23 -- 2**5 64 : stapleEdge34 -- 2**6 128 : stapleEdge14 -- 2**7"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class ScmPrtPageSizeErrorPolicy(TextualConvention, Integer32):
    reference = ' PostScript Language Reference Manual, second edition, Adobe Systems Incorporated, pp 239-249. See: ScmPrtMediaTypeErrorPolicy'
    description = " Controls interpreter behavior when the requested Page Size is not currently available. * The values 'other' and 'unknown' are deprecated for conforming implementations. * 'abortJob' will cause the interpreter to abort the job with an appropriate error condition. * 'ignore' will cause the job to be printed on the default media as specified by scmPrtInterpInputIndexDefault OR scmPrtInterpPaperSizeDefault OR any available media deemed appropriate by the implementation. No adjustment will be made to the image size. Exact semantics of this setting are product specific. * 'interactWithOperator' will cause the printer to interact with the operator to determine what to do. For example, display a message at the operator console requesting the desired media. The semantics of this policy vary among different products and environments. * 'useNearestAndAdjust' will cause the job to be printed on the nearest available media (as described below). The interpreter will adjust the image size (by scaling and centering) to fit. * 'useNextLargerAndAdjust' will cause the job to be printed on the next larger available media (as described below). The interpreter will adjust the image size (by scaling and centering) to fit. * 'useNearest' will cause the job to be printed on the nearest available media (as described below). No adjustment will be made to the image size. * 'useNextLarger' will cause the job to be printed on the next larger available media (as described below). No adjustment will be made to the image size. * 'ignoreAfterTimeout' will cause the job to be ignored same as ignore' above, but not till after scmPrtInterpErrorPolicyTimeout expires. In the above descriptions, nearest size is defined as the one closest in area to the requested size. The next larger size is the one that is at least as large as the requested size in both width and height and is smallest in area. To adjust the page means to scale the page image (if necessary) to fit the medium, then center the image on the medium."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notSpecified", 3), ("abortJob", 4), ("ignore", 5), ("interactWithOperator", 6), ("useNearestAndAdjust", 7), ("useNextLargerAndAdjust", 8), ("useNearest", 9), ("useNextLarger", 10), ("ignoreAfterTimeout", 11))

class ScmPrtPCLFontSource(TextualConvention, Integer32):
    reference = ' See: PJL Technical Reference Manual- FONTSOURCE'
    description = ' '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 20, 41, 42, 43, 44, 45, 46, 47, 48, 49, 61, 62, 63, 64, 65, 66, 67, 68, 69, 80))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notSpecified", 3), ("internal", 20), ("romSimm1", 41), ("romSimm2", 42), ("romSimm3", 43), ("romSimm4", 44), ("romSimm5", 45), ("romSimm6", 46), ("romSimm7", 47), ("romSimm8", 48), ("romSimm9", 49), ("cartridge1", 61), ("cartridge2", 62), ("cartridge3", 63), ("cartridge4", 64), ("cartridge5", 65), ("cartridge6", 66), ("cartridge7", 67), ("cartridge8", 68), ("cartridge9", 69), ("permanentSoft", 80))

class ScmPrtPlex(TextualConvention, Integer32):
    reference = ' See: ISO/IEC 10175-1:1996(E) Section 9.3.2.16.2: Plex Section 9.3.2.19: Sides See: PostScript Language Reference Manual (2nd Edition) - PageSize, Duplex, Tumble See: PCL 5 Printer Language Technical Reference Manual Simplex/Duplex Print Command'
    description = " This Textual Convention enumerates plex modes which may be supported by a printer or interpreter. A plex mode specifies whether pages are to be printed one-sided or two-sided, as well as the content orientation between consecutive pages. For the ScmPrtPlex TC, the following definitions apply: 'one-sided' - Print on only one side of each sheet. 'two-sided' - Print on both sides of each sheet. 'simplex' - The document pages are to be oriented so as to condition them for one-sided printing. 'long-edge-bind' - The document pages are to be oriented so as to condition them for two-sided printing, bound along the length (the longer edge) of the physical page. 'short-edge-bind' - The document pages are to be oriented so as to condition them for two-sided printing, bound along the width (the shorter edge) of the physical page. ScmPrtPlex's representation is bit-encoded, so that a device may show multiple plex modes supported. The value zero shall mean notSpecified. The following ScmPrtPlex values and meanings are defined: 0x001 simplex, one-sided 0X002 simplex, two-sided 0x010 long-edge-bind, one-sided 0x020 long-edge-bind, two-sided 0x040 short-edge-bind, one-sided 0x080 short-edge-bind, two-sided The following describes the relationship of the scmPrtPlex modes to DPA, PostScript and PCL. DPA: In DPA, Plex specifies whether the page images of the output document are to be conditioned for (eventual) one-sided or two-sided printing, and also specifies whether the relative orientation between consecutive page-images is to be altered. In DPA, the Plex modes specified are named 'Simplex', 'Duplex' and 'Tumble'. However, 'Duplex' would more accurately be named bindLongEdge, and 'Tumble' would more accurately be named bindShortEdge. As written in DPA, 'Whether the images are portrait or landscape, the binding edge is parallel to: the y axis for 'duplex', and the x axis for 'tumble'. This last observation is important for understanding when to use 'tumble'. If the binding edge of the document is along the y-axis, the plex is 'duplex', whether the orientation is portrait or landscape, and if the binding-edge is along the x-axis, the plex is 'tumble', whether the orientation is portrait or landscape. In DPA, a separate attribute, 'Sides', specifies 1-sided or 2-sided printing. In DPA, the value of this attribute may also be used by the presentation processes of some document formats to determine whether or not to print certain designated pages (e.g. the extra blank pages needed in two-sided printing to cause sections to begin on the righthand side of a book, or recto page). The following enumerations are relevant to DPA: simplexOneSided, simplexTwoSided, bindLongEdgeOneSided, bindLongEdgeTwoSided, bindShortEdgeOneSided, bindShortEdgeTwoSided. PostScript: In PostScript, the keys 'duplex' and 'tumble' are booleans which specify relative orientation between consecutive pages, and to the number of sides printed. If 'Duplex' is False, pages are printed 1-sided, i.e. 'simplex'. If 'Duplex' is True, pages are printed 2-sided. (For most PostScript interpreters, only when 'Duplex' is set to True) 'Tumble' specifies how the page images on opposite sides of a sheet are oriented with respect to each other. If 'Tumble' is False, the default user spaces of the two pages are oriented such that the highest value of y in the two spaces lie along the same edge of the media. Informally, a Tumble value of False produces output suitable for binding on the left or right. When the default user space is set to a portrait 'pagesize', setting Tumble to false is the same as using the ScmPrtPlex attribute longEdgeBind. When the default user space is set to a landscape 'pagesize', setting Tumble to false is the same as using the ScmPrtPlex attribute shortEdgeBind. If 'Tumble' is True, the default user spaces of the two pages are oriented such that the highest value of y in the two spaces lie along opposite edges of the media. Informally, a Tumble value of True produces output suitable for binding on the top or bottom. When the default user space is set to a landscape 'pagesize', setting Tumble to true is the same as using the ScmPrtPlex attribute shortEdgeBind. When the default user space is set to a landscape 'pagesize', setting Tumble to true is the same as using the ScmPrtPlex attribute longEdgeBind. The following ScmPrtPlex enumerations are relevant to PostScript: bindLongEdgeOneSided, bindLongEdgeTwoSided, bindShortEdgeOneSided, bindShortEdgeTwoSided. Typically (ie, for a Portrait default user space): OneSided maps to the duplex boolean set to false TwoSided maps to the duplex boolean set to true bindEdgeLong maps to the tumble boolean set to false bindEdgeShort maps to the tumble boolean set to true PCL: In PCL, the attributes simplex, duplex long-edge-binding, and duplex short-edge-binding, along with content orientation, landscape or portrait, detail the number of sides to be printed, content orientation, and relative orientation between consecutive pages. The PCL model matches that of DPA. The following ScmPrtPlex enumerations are relevant to PCL: simplexOneSided, bindLongEdgeTwoSided, bindShortEdgeTwoSided."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class ScmPrtPrintQuality(TextualConvention, Integer32):
    reference = ' ISO/IEC 10175-1:1996(E) Section 9.3.2.17: Print-quality'
    description = " These attributes specify the output quality of the printed document. Some printers have programmatically controlled output quality. This attribute allows the user to specify the level of output quality desired from printers. The following standard values are defined: - 'draft' means lowest quality available on the printer. Uses include increasing the printer's speed and saving toner. - 'normal' means normal or intermediate quality on the printer. - 'high' means highest quality available on the printer."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notSpecified", 3), ("draft", 4), ("normal", 5), ("high", 6))

class ScmPrtPrintScreen(TextualConvention, Integer32):
    description = ' This Textual-Convention enumerates special modes for 80 character screen dumps onto A4 size paper, which is usually 77 characters wide. This function is useful when printing the 80 characters per line width of computer displays. The PrintScreen mode enables characters to be printed as shown on the display when PrintScreen is executed from the host. When mode850 or mode852 is set, the following is done: - Symbol set value changed to PC-850 or PC-852. with the current Symbol set value being stored. - A4 size horizontal printable area expanded to being 80 characters wide. When the special mode is returned to Off, the following is done: - Symbol set value returned to the stored SymbolSet Value. - A4 size horizontal printable area returned to being 77 characters.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notSpecified", 3), ("off", 4), ("mode850", 5), ("mode852", 6))

class ScmPrtTraySwitch(TextualConvention, Integer32):
    reference = ' See: scmPrtInterpTraySwitch See: scmPrtInputNextPrtInputIndex See: scmPrtInputAliasTable'
    description = ' This Textual-Convention enumerates which tray switching declaration mechanism is used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notSpecified", 3), ("off", 4), ("useScmPrtInputNextPrtInputIndex", 5), ("useScmPrtInputAliasTable", 6))

class ScmPrtGeneralMonoPrintOpt(TextualConvention, Integer32):
    reference = ' See: Phaser 7750 User Guide... for more information '
    description = ' These attributes specify the printing performance / economy mode setting.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("optimizeForSpeed", 3), ("optimizeForEconomy", 4), ("notPresent", 5))

sCmPrintTCDummy = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999))
sCmPrtTCAuxSheetContent = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 1), ScmPrtAuxSheetContent())
if mibBuilder.loadTexts: sCmPrtTCAuxSheetContent.setStatus('current')
if mibBuilder.loadTexts: sCmPrtTCAuxSheetContent.setDescription('Dummy - DO NOT USE')
sCmPrtTCScmPrtAuxSheetType = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 2), ScmPrtAuxSheetType())
if mibBuilder.loadTexts: sCmPrtTCScmPrtAuxSheetType.setStatus('current')
if mibBuilder.loadTexts: sCmPrtTCScmPrtAuxSheetType.setDescription('Dummy - DO NOT USE')
sCmPrtTCTCChannelType = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 3), ScmPrtChannelType())
if mibBuilder.loadTexts: sCmPrtTCTCChannelType.setStatus('current')
if mibBuilder.loadTexts: sCmPrtTCTCChannelType.setDescription('Dummy - DO NOT USE')
sCmPrtTCGroupSupport = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 4), ScmPrtGroupSupport())
if mibBuilder.loadTexts: sCmPrtTCGroupSupport.setStatus('current')
if mibBuilder.loadTexts: sCmPrtTCGroupSupport.setDescription('Dummy - DO NOT USE')
sCmPrtTCIETFPrintMIBGroupSupport = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 5), ScmPrtIETFPrintMIBGroupSupport())
if mibBuilder.loadTexts: sCmPrtTCIETFPrintMIBGroupSupport.setStatus('current')
if mibBuilder.loadTexts: sCmPrtTCIETFPrintMIBGroupSupport.setDescription('Dummy - DO NOT USE')
sCmPrtTCInterpreterLangFamily = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 6), ScmPrtInterpreterLangFamily())
if mibBuilder.loadTexts: sCmPrtTCInterpreterLangFamily.setStatus('current')
if mibBuilder.loadTexts: sCmPrtTCInterpreterLangFamily.setDescription('Dummy - DO NOT USE')
sCmPrtTCMediaTypeErrorPolicy = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 7), ScmPrtMediaTypeErrorPolicy())
if mibBuilder.loadTexts: sCmPrtTCMediaTypeErrorPolicy.setStatus('current')
if mibBuilder.loadTexts: sCmPrtTCMediaTypeErrorPolicy.setDescription('Dummy - DO NOT USE')
sCmPrtTCMediumClassType = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 8), ScmPrtMediumClassType())
if mibBuilder.loadTexts: sCmPrtTCMediumClassType.setStatus('current')
if mibBuilder.loadTexts: sCmPrtTCMediumClassType.setDescription('Dummy - DO NOT USE')
sCmPrtTCMediumSize = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 9), ScmPrtMediumSize())
if mibBuilder.loadTexts: sCmPrtTCMediumSize.setStatus('current')
if mibBuilder.loadTexts: sCmPrtTCMediumSize.setDescription('Dummy - DO NOT USE')
sCmPrtTCOutputOffsetStackingType = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 10), ScmPrtOutputOffsetStackingType())
if mibBuilder.loadTexts: sCmPrtTCOutputOffsetStackingType.setStatus('current')
if mibBuilder.loadTexts: sCmPrtTCOutputOffsetStackingType.setDescription('Dummy - DO NOT USE')
sCmPrtOutputStaplePosition = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 11), ScmPrtOutputStaplePosition())
if mibBuilder.loadTexts: sCmPrtOutputStaplePosition.setStatus('current')
if mibBuilder.loadTexts: sCmPrtOutputStaplePosition.setDescription('Dummy - DO NOT USE')
sCmPrtTCPageSizeErrorPolicy = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 12), ScmPrtPageSizeErrorPolicy())
if mibBuilder.loadTexts: sCmPrtTCPageSizeErrorPolicy.setStatus('current')
if mibBuilder.loadTexts: sCmPrtTCPageSizeErrorPolicy.setDescription('Dummy - DO NOT USE')
sCmPrtTCPCLFontSource = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 13), ScmPrtPCLFontSource())
if mibBuilder.loadTexts: sCmPrtTCPCLFontSource.setStatus('current')
if mibBuilder.loadTexts: sCmPrtTCPCLFontSource.setDescription('Dummy - DO NOT USE')
sCmPrtTCPlex = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 14), ScmPrtPlex())
if mibBuilder.loadTexts: sCmPrtTCPlex.setStatus('current')
if mibBuilder.loadTexts: sCmPrtTCPlex.setDescription('Dummy - DO NOT USE')
sCmPrtTCPrintQuality = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 15), ScmPrtPrintQuality())
if mibBuilder.loadTexts: sCmPrtTCPrintQuality.setStatus('current')
if mibBuilder.loadTexts: sCmPrtTCPrintQuality.setDescription('Dummy - DO NOT USE')
sCmPrtTCPrintScreen = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 16), ScmPrtPrintScreen())
if mibBuilder.loadTexts: sCmPrtTCPrintScreen.setStatus('current')
if mibBuilder.loadTexts: sCmPrtTCPrintScreen.setDescription('Dummy - DO NOT USE')
sCmPrtTCTraySwitch = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 17), ScmPrtTraySwitch())
if mibBuilder.loadTexts: sCmPrtTCTraySwitch.setStatus('current')
if mibBuilder.loadTexts: sCmPrtTCTraySwitch.setDescription('Dummy - DO NOT USE')
sCmPrtTCGeneralMonoPrintOpt = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 54, 999, 18), ScmPrtGeneralMonoPrintOpt())
if mibBuilder.loadTexts: sCmPrtTCGeneralMonoPrintOpt.setStatus('current')
if mibBuilder.loadTexts: sCmPrtTCGeneralMonoPrintOpt.setDescription('Dummy - DO NOT USE')
mibBuilder.exportSymbols("SAMSUNG-PRINTER-EXT-TC", ScmPrtOutputOffsetStackingType=ScmPrtOutputOffsetStackingType, sCmPrtTCMediaTypeErrorPolicy=sCmPrtTCMediaTypeErrorPolicy, sCmPrtOutputStaplePosition=sCmPrtOutputStaplePosition, scmPrintTC=scmPrintTC, sCmPrtTCOutputOffsetStackingType=sCmPrtTCOutputOffsetStackingType, ScmPrtPlex=ScmPrtPlex, ScmPrtTraySwitch=ScmPrtTraySwitch, ScmPrtPrintScreen=ScmPrtPrintScreen, sCmPrtTCGroupSupport=sCmPrtTCGroupSupport, sCmPrtTCPlex=sCmPrtTCPlex, sCmPrtTCTCChannelType=sCmPrtTCTCChannelType, sCmPrtTCPageSizeErrorPolicy=sCmPrtTCPageSizeErrorPolicy, ScmPrtPrintQuality=ScmPrtPrintQuality, sCmPrtTCInterpreterLangFamily=sCmPrtTCInterpreterLangFamily, sCmPrtTCTraySwitch=sCmPrtTCTraySwitch, ScmPrtIETFPrintMIBGroupSupport=ScmPrtIETFPrintMIBGroupSupport, ScmPrtMediumSize=ScmPrtMediumSize, sCmPrtTCIETFPrintMIBGroupSupport=sCmPrtTCIETFPrintMIBGroupSupport, sCmPrtTCPCLFontSource=sCmPrtTCPCLFontSource, sCmPrtTCPrintScreen=sCmPrtTCPrintScreen, ScmPrtGroupSupport=ScmPrtGroupSupport, PYSNMP_MODULE_ID=scmPrintTC, ScmPrtChannelType=ScmPrtChannelType, ScmPrtInterpreterLangFamily=ScmPrtInterpreterLangFamily, ScmPrtAuxSheetContent=ScmPrtAuxSheetContent, ScmPrtMediumClassType=ScmPrtMediumClassType, ScmPrtPageSizeErrorPolicy=ScmPrtPageSizeErrorPolicy, sCmPrtTCAuxSheetContent=sCmPrtTCAuxSheetContent, ScmPrtAuxSheetType=ScmPrtAuxSheetType, sCmPrintTCDummy=sCmPrintTCDummy, sCmPrtTCGeneralMonoPrintOpt=sCmPrtTCGeneralMonoPrintOpt, ScmPrtPCLFontSource=ScmPrtPCLFontSource, sCmPrtTCMediumSize=sCmPrtTCMediumSize, sCmPrtTCPrintQuality=sCmPrtTCPrintQuality, ScmPrtGeneralMonoPrintOpt=ScmPrtGeneralMonoPrintOpt, ScmPrtMediaTypeErrorPolicy=ScmPrtMediaTypeErrorPolicy, sCmPrtTCMediumClassType=sCmPrtTCMediumClassType, sCmPrtTCScmPrtAuxSheetType=sCmPrtTCScmPrtAuxSheetType, ScmPrtOutputStaplePosition=ScmPrtOutputStaplePosition)
