#
# PySNMP MIB module ADSL2-LINE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADSL2-LINE-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:13:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Unsigned32, Integer32, transmission, Bits, IpAddress, TimeTicks, Gauge32, NotificationType, MibIdentifier, Counter32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "Integer32", "transmission", "Bits", "IpAddress", "TimeTicks", "Gauge32", "NotificationType", "MibIdentifier", "Counter32", "iso", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adsl2TCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 238, 2))
adsl2TCMIB.setRevisions(('2006-10-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adsl2TCMIB.setRevisionsDescriptions(('Initial version, published as RFC 4706.',))
if mibBuilder.loadTexts: adsl2TCMIB.setLastUpdated('200610040000Z')
if mibBuilder.loadTexts: adsl2TCMIB.setOrganization('ADSLMIB Working Group')
if mibBuilder.loadTexts: adsl2TCMIB.setContactInfo('WG-email: adslmib@ietf.org Info: https://www1.ietf.org/mailman/listinfo/adslmib Chair: Mike Sneed Sand Channel Systems Postal: P.O. Box 37324 Raleigh NC 27627-732 Email: sneedmike@hotmail.com Phone: +1 206 600 7022 Co-Chair & Co-editor: Menachem Dodge ECI Telecom Ltd. Postal: 30 Hasivim St. Petach Tikva 49517, Israel. Email: mbdodge@ieee.org Phone: +972 3 926 8421 Co-editor: Moti Morgenstern ECI Telecom Ltd. Postal: 30 Hasivim St. Petach Tikva 49517, Israel. Email: moti.morgenstern@ecitele.com Phone: +972 3 926 6258 Co-editor: Scott Baillie NEC Australia Postal: 649-655 Springvale Road, Mulgrave, Victoria 3170, Australia. Email: scott.baillie@nec.com.au Phone: +61 3 9264 3986 Co-editor: Umberto Bonollo NEC Australia Postal: 649-655 Springvale Road, Mulgrave, Victoria 3170, Australia. Email: umberto.bonollo@nec.com.au Phone: +61 3 9264 3385 ')
if mibBuilder.loadTexts: adsl2TCMIB.setDescription('This MIB Module provides Textual Conventions to be used by the ADSL2-LINE-MIB module for the purpose of managing ADSL, ADSL2, and ADSL2+ lines. Copyright (C) The Internet Society (2006). This version of this MIB module is part of RFC 4706: see the RFC itself for full legal notices.')
class Adsl2Unit(TextualConvention, Integer32):
    description = 'Identifies a transceiver as being either an ATU-C or an ATU-R. An ADSL line consists of two transceivers, an ATU-C and an ATU-R. Attributes with this syntax reference the two sides of a line. Specified as an INTEGER, the two values are: atuc(1) -- Central office ADSL terminal unit (ATU-C). atur(2) -- Remote ADSL terminal unit (ATU-R).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("atuc", 1), ("atur", 2))

class Adsl2Direction(TextualConvention, Integer32):
    description = 'Identifies the direction of a band as being either upstream or downstream. Specified as an INTEGER, the two values are: upstream(1), and downstream(2).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("upstream", 1), ("downstream", 2))

class Adsl2TransmissionModeType(TextualConvention, Bits):
    description = 'A set of ADSL2 line transmission modes, with one bit per mode. The notes (F) and (L) denote Full-Rate and Lite/splitterless, respectively: Bit 00 : Regional Std. (ANSI T1.413) (F) Bit 01 : Regional Std. (ETSI DTS/TM06006) (F) Bit 02 : G.992.1 POTS non-overlapped (F) Bit 03 : G.992.1 POTS overlapped (F) Bit 04 : G.992.1 ISDN non-overlapped (F) Bit 05 : G.992.1 ISDN overlapped (F) Bit 06 : G.992.1 TCM-ISDN non-overlapped (F) Bit 07 : G.992.1 TCM-ISDN overlapped (F) Bit 08 : G.992.2 POTS non-overlapped (L) Bit 09 : G.992.2 POTS overlapped (L) Bit 10 : G.992.2 with TCM-ISDN non-overlapped (L) Bit 11 : G.992.2 with TCM-ISDN overlapped (L) Bit 12 : G.992.1 TCM-ISDN symmetric (F) -- not in G.997.1 Bit 13-17: Reserved Bit 18 : G.992.3 POTS non-overlapped (F) Bit 19 : G.992.3 POTS overlapped (F) Bit 20 : G.992.3 ISDN non-overlapped (F) Bit 21 : G.992.3 ISDN overlapped (F) Bit 22-23: Reserved Bit 24 : G.992.4 POTS non-overlapped (L) Bit 25 : G.992.4 POTS overlapped (L) Bit 26-27: Reserved Bit 28 : G.992.3 Annex I All-Digital non-overlapped (F) Bit 29 : G.992.3 Annex I All-Digital overlapped (F) Bit 30 : G.992.3 Annex J All-Digital non-overlapped (F) Bit 31 : G.992.3 Annex J All-Digital overlapped (F) Bit 32 : G.992.4 Annex I All-Digital non-overlapped (L) Bit 33 : G.992.4 Annex I All-Digital overlapped (L) Bit 34 : G.992.3 Annex L POTS non-overlapped, mode 1, wide U/S (F) Bit 35 : G.992.3 Annex L POTS non-overlapped, mode 2, narrow U/S(F) Bit 36 : G.992.3 Annex L POTS overlapped, mode 3, wide U/S (F) Bit 37 : G.992.3 Annex L POTS overlapped, mode 4, narrow U/S (F) Bit 38 : G.992.3 Annex M POTS non-overlapped (F) Bit 39 : G.992.3 Annex M POTS overlapped (F) Bit 40 : G.992.5 POTS non-overlapped (F) Bit 41 : G.992.5 POTS overlapped (F) Bit 42 : G.992.5 ISDN non-overlapped (F) Bit 43 : G.992.5 ISDN overlapped (F) Bit 44-45: Reserved Bit 46 : G.992.5 Annex I All-Digital non-overlapped (F) Bit 47 : G.992.5 Annex I All-Digital overlapped (F) Bit 48 : G.992.5 Annex J All-Digital non-overlapped (F) Bit 49 : G.992.5 Annex J All-Digital overlapped (F) Bit 50 : G.992.5 Annex M POTS non-overlapped (F) Bit 51 : G.992.5 Annex M POTS overlapped (F) Bit 52-55: Reserved'
    status = 'current'
    namedValues = NamedValues(("ansit1413", 0), ("etsi", 1), ("g9921PotsNonOverlapped", 2), ("g9921PotsOverlapped", 3), ("g9921IsdnNonOverlapped", 4), ("g9921isdnOverlapped", 5), ("g9921tcmIsdnNonOverlapped", 6), ("g9921tcmIsdnOverlapped", 7), ("g9922potsNonOverlapped", 8), ("g9922potsOverlapped", 9), ("g9922tcmIsdnNonOverlapped", 10), ("g9922tcmIsdnOverlapped", 11), ("g9921tcmIsdnSymmetric", 12), ("reserved1", 13), ("reserved2", 14), ("reserved3", 15), ("reserved4", 16), ("reserved5", 17), ("g9923PotsNonOverlapped", 18), ("g9923PotsOverlapped", 19), ("g9923IsdnNonOverlapped", 20), ("g9923isdnOverlapped", 21), ("reserved6", 22), ("reserved7", 23), ("g9924potsNonOverlapped", 24), ("g9924potsOverlapped", 25), ("reserved8", 26), ("reserved9", 27), ("g9923AnnexIAllDigNonOverlapped", 28), ("g9923AnnexIAllDigOverlapped", 29), ("g9923AnnexJAllDigNonOverlapped", 30), ("g9923AnnexJAllDigOverlapped", 31), ("g9924AnnexIAllDigNonOverlapped", 32), ("g9924AnnexIAllDigOverlapped", 33), ("g9923AnnexLMode1NonOverlapped", 34), ("g9923AnnexLMode2NonOverlapped", 35), ("g9923AnnexLMode3Overlapped", 36), ("g9923AnnexLMode4Overlapped", 37), ("g9923AnnexMPotsNonOverlapped", 38), ("g9923AnnexMPotsOverlapped", 39), ("g9925PotsNonOverlapped", 40), ("g9925PotsOverlapped", 41), ("g9925IsdnNonOverlapped", 42), ("g9925isdnOverlapped", 43), ("reserved10", 44), ("reserved11", 45), ("g9925AnnexIAllDigNonOverlapped", 46), ("g9925AnnexIAllDigOverlapped", 47), ("g9925AnnexJAllDigNonOverlapped", 48), ("g9925AnnexJAllDigOverlapped", 49), ("g9925AnnexMPotsNonOverlapped", 50), ("g9925AnnexMPotsOverlapped", 51), ("reserved12", 52), ("reserved13", 53), ("reserved14", 54), ("reserved15", 55))

class Adsl2RaMode(TextualConvention, Integer32):
    description = 'Specifies the rate adaptation behavior for the line. The three possible behaviors are: manual(1) - No Rate-Adaptation. The initialization process attempts to synchronize to a specified rate. raInit(2) - Rate-Adaptation during initialization process only, which attempts to synchronize to a rate between minimum and maximum specified values. dynamicRa(3) - Dynamic Rate-Adaptation during initialization process as well as during SHOWTIME.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("manual", 1), ("raInit", 2), ("dynamicRa", 3))

class Adsl2InitResult(TextualConvention, Integer32):
    description = 'Specifies the result of a full initialization attempt; the six possible result values are: noFail(0) - Successful initialization. configError(1) - Configuration failure. configNotFeasible(2) - Configuration details not supported. commFail(3) - Communication failure. noPeerAtu(4) - Peer ATU not detected. otherCause(5) - Other initialization failure reason. The values used are as defined in ITU-T G.997.1, paragraph 7.5.1.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("noFail", 0), ("configError", 1), ("configNotFeasible", 2), ("commFail", 3), ("noPeerAtu", 4), ("otherCause", 5))

class Adsl2OperationModes(TextualConvention, Integer32):
    description = 'The ADSL2 management model specified includes an ADSL Mode attribute that identifies an instance of ADSL Mode-Specific PSD Configuration object in the ADSL Line Profile. The following classes of ADSL operating mode are defined. The notes (F) and (L) denote Full-Rate and Lite/splitterless respectively: +-------+--------------------------------------------------+ | Value | ADSL operation mode description | +-------+--------------------------------------------------+ 1 - The default/generic PSD configuration. Default configuration will be used when no other matching mode-specific configuration can be found. 2 - ADSL family. The attributes included in the Mode- Specific PSD Configuration are irrelevant for ITU-T G.992.1 and G.992.2 ADSL modes. Hence, it is possible to map those modes to this generic class. 3-7 - Unused. Reserved for future ITU-T specification. 8 - G.992.3 POTS non-overlapped (F) 9 - G.992.3 POTS overlapped (F) 10 - G.992.3 ISDN non-overlapped (F) 11 - G.992.3 ISDN overlapped (F) 12-13 - Unused. Reserved for future ITU-T specification. 14 - G.992.4 POTS non-overlapped (L) 15 - G.992.4 POTS overlapped (L) 16-17 - Unused. Reserved for future ITU-T specification. 18 - G.992.3 Annex I All-Digital non-overlapped (F) 19 - G.992.3 Annex I All-Digital overlapped (F) 20 - G.992.3 Annex J All-Digital non-overlapped (F) 21 - G.992.3 Annex J All-Digital overlapped (F) 22 - G.992.4 Annex I All-Digital non-overlapped (L) 23 - G.992.4 Annex I All-Digital overlapped (L) 24 - G.992.3 Annex L POTS non-overlapped, mode 1, wide U/S (F) 25 - G.992.3 Annex L POTS non-overlapped, mode 2, narrow U/S(F) 26 - G.992.3 Annex L POTS overlapped, mode 3, wide U/S (F) 27 - G.992.3 Annex L POTS overlapped, mode 4, narrow U/S (F) 28 - G.992.3 Annex M POTS non-overlapped (F) 29 - G.992.3 Annex M POTS overlapped (F) 30 - G.992.5 POTS non-overlapped (F) 31 - G.992.5 POTS overlapped (F) 32 - G.992.5 ISDN non-overlapped (F) 33 - G.992.5 ISDN overlapped (F) 34-35 - Unused. Reserved for future ITU-T specification. 36 - G.992.5 Annex I All-Digital non-overlapped (F) 37 - G.992.5 Annex I All-Digital overlapped (F) 38 - G.992.5 Annex J All-Digital non-overlapped (F) 39 - G.992.5 Annex J All-Digital overlapped (F) 40 - G.992.5 Annex M POTS non-overlapped (F) 41 - G.992.5 Annex M POTS overlapped (F) '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 8, 9, 10, 11, 14, 15, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 36, 37, 38, 39, 40, 41))
    namedValues = NamedValues(("defMode", 1), ("adsl", 2), ("g9923PotsNonOverlapped", 8), ("g9923PotsOverlapped", 9), ("g9923IsdnNonOverlapped", 10), ("g9923isdnOverlapped", 11), ("g9924potsNonOverlapped", 14), ("g9924potsOverlapped", 15), ("g9923AnnexIAllDigNonOverlapped", 18), ("g9923AnnexIAllDigOverlapped", 19), ("g9923AnnexJAllDigNonOverlapped", 20), ("g9923AnnexJAllDigOverlapped", 21), ("g9924AnnexIAllDigNonOverlapped", 22), ("g9924AnnexIAllDigOverlapped", 23), ("g9923AnnexLMode1NonOverlapped", 24), ("g9923AnnexLMode2NonOverlapped", 25), ("g9923AnnexLMode3Overlapped", 26), ("g9923AnnexLMode4Overlapped", 27), ("g9923AnnexMPotsNonOverlapped", 28), ("g9923AnnexMPotsOverlapped", 29), ("g9925PotsNonOverlapped", 30), ("g9925PotsOverlapped", 31), ("g9925IsdnNonOverlapped", 32), ("g9925isdnOverlapped", 33), ("g9925AnnexIAllDigNonOverlapped", 36), ("g9925AnnexIAllDigOverlapped", 37), ("g9925AnnexJAllDigNonOverlapped", 38), ("g9925AnnexJAllDigOverlapped", 39), ("g9925AnnexMPotsNonOverlapped", 40), ("g9925AnnexMPotsOverlapped", 41))

class Adsl2PowerMngState(TextualConvention, Integer32):
    description = 'Attributes with this syntax uniquely identify each power management state defined for the ADSL/ADSL2 or ADSL2+ link. The possible values are: l0(1) - L0 - Full power management state. l1(2) - L1 - Low power management state (for G.992.2). l2(3) - L2 - Low power management state (for G.992.3, G.992.4, and G.992.5). l3(4) - L3 - Idle power management state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("l0", 1), ("l1", 2), ("l2", 3), ("l3", 4))

class Adsl2ConfPmsForce(TextualConvention, Integer32):
    description = 'Attributes with this syntax are configuration parameters that reference the desired power management state for the ADSL/ADSL2 or ADSL2+ link: l3toL0(0) - Perform a transition from L3 to L0 (Full power management state). l0toL2(2) - Perform a transition from L0 to L2 (Low power management state). l0orL2toL3(3) - Perform a transition into L3 (Idle power management state). The values used are as defined in ITU-T G.997.1, paragraph 7.3.1.1.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 3))
    namedValues = NamedValues(("l3toL0", 0), ("l0toL2", 2), ("l0orL2toL3", 3))

class Adsl2LConfProfPmMode(TextualConvention, Bits):
    description = 'Attributes with this syntax are configuration parameters that reference the power modes/states into which the ATU-C or ATU-R may autonomously transit. It is a BITS structure that allows control of the following transit options: allowTransitionsToIdle(0) - XTU may autonomously transit to idle (L3) state. allowTransitionsToLowPower(1) - XTU may autonomously transit to low-power (L2) state.'
    status = 'current'
    namedValues = NamedValues(("allowTransitionsToIdle", 0), ("allowTransitionsToLowPower", 1))

class Adsl2LineLdsf(TextualConvention, Integer32):
    description = 'Attributes with this syntax are configuration parameters that control the Loop Diagnostic mode for the ADSL/ADSL2 or ADSL2+ link. The possible values are: inhibit(0) - Inhibit Loop Diagnostic mode. force(1) - Force/Initiate Loop Diagnostic mode. The values used are as defined in ITU-T G.997.1, paragraph 7.3.1.1.8'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("inhibit", 0), ("force", 1))

class Adsl2LdsfResult(TextualConvention, Integer32):
    description = "Possible failure reasons associated with performing a Dual Ended Loop Test (DELT) on a DSL line. Possible values are: none(1) - The default value in case LDSF was never requested for the associated line. success(2) - The recent command completed successfully. inProgress(3) - The Loop Diagnostics process is in progress. unsupported(4) - The NE or the line card doesn't support LDSF. cannotRun(5) - The NE cannot initiate the command, due to a nonspecific reason. aborted(6) - The Loop Diagnostics process aborted. failed(7) - The Loop Diagnostics process failed. illegalMode(8) - The NE cannot initiate the command, due to the specific mode of the relevant line. adminUp(9) - The NE cannot initiate the command, as the relevant line is administratively 'Up'. tableFull(10) - The NE cannot initiate the command, due to reaching the maximum number of rows in the results table. noResources(11) - The NE cannot initiate the command, due to lack of internal memory resources."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("none", 1), ("success", 2), ("inProgress", 3), ("unsupported", 4), ("cannotRun", 5), ("aborted", 6), ("failed", 7), ("illegalMode", 8), ("adminUp", 9), ("tableFull", 10), ("noResources", 11))

class Adsl2SymbolProtection(TextualConvention, Integer32):
    description = 'Attributes with this syntax are configuration parameters that reference the minimum-length impulse noise protection (INP) in terms of number of symbols. The possible values are: noProtection (i.e., INP not required), halfSymbol (i.e., INP length is 1/2 symbol), and 1-16 symbols in steps of 1 symbol.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("noProtection", 1), ("halfSymbol", 2), ("singleSymbol", 3), ("twoSymbols", 4), ("threeSymbols", 5), ("fourSymbols", 6), ("fiveSymbols", 7), ("sixSymbols", 8), ("sevenSymbols", 9), ("eightSymbols", 10), ("nineSymbols", 11), ("tenSymbols", 12), ("elevenSymbols", 13), ("twelveSymbols", 14), ("thirteeSymbols", 15), ("fourteenSymbols", 16), ("fifteenSymbols", 17), ("sixteenSymbols", 18))

class Adsl2MaxBer(TextualConvention, Integer32):
    description = 'Attributes with this syntax are configuration parameters that reference the maximum Bit Error Rate (BER). The possible values are: eminus3(1) - Maximum BER=E^-3 eminus5(2) - Maximum BER=E^-5 eminus7(3) - Maximum BER=E^-7'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("eminus3", 1), ("eminus5", 2), ("eminus7", 3))

class Adsl2ScMaskDs(TextualConvention, OctetString):
    description = 'Each one of the 512 bits in this OCTET STRING array represents the corresponding bin in the downstream direction. A value of one indicates that the bin is not in use.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class Adsl2ScMaskUs(TextualConvention, OctetString):
    description = 'Each one of the 64 bits in this OCTET STRING array represents the corresponding bin in the upstream direction. A value of one indicates that the bin is not in use.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class Adsl2RfiDs(TextualConvention, OctetString):
    description = 'Each one of the 512 bits in this OCTET STRING array represents the corresponding bin in the downstream direction. A value of one indicates that the bin is part of a notch filter.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class Adsl2PsdMaskDs(TextualConvention, OctetString):
    description = 'This is a structure that represents up to 32 PSD Mask breakpoints. Each breakpoint occupies 3 octets: The first two octets hold the index of the sub-carrier associated with the breakpoint. The third octet holds the PSD reduction at the breakpoint from 0 (0 dBm/Hz) to 255 (-127.5 dBm/Hz) using units of 0.5 dBm/Hz.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 96)

class Adsl2PsdMaskUs(TextualConvention, OctetString):
    description = 'This is a structure that represents up to 4 PSD Mask breakpoints. Each breakpoint occupies 3 octets: The first two octets hold the index of the sub-carrier associated with the breakpoint. The third octet holds the PSD reduction at the breakpoint from 0 (0 dBm/Hz) to 255 (-127.5 dBm/Hz) using units of 0.5 dBm/Hz.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 12)

class Adsl2Tssi(TextualConvention, OctetString):
    description = 'This is a structure that represents up to 32 transmit spectrum shaping (TSSi) breakpoints. Each breakpoint occupies 3 octets: The first two octets hold the index of the sub-carrier associated with the breakpoint. The third octet holds the shaping parameter at the breakpoint. It is a value from 0 to 127 (units of -0.5 dB). The special value 127 indicates that the sub-carrier is not transmitted.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 96)

class Adsl2LastTransmittedState(TextualConvention, Integer32):
    description = 'This parameter represents the last successfully transmitted initialization state in the last full initialization performed on the line. States are per the specific xDSL technology and are numbered from 0 (if G.994.1 is used) or 1 (if G.994.1 is not used) up to Showtime.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131))
    namedValues = NamedValues(("atucG9941", 0), ("atucQuiet1", 1), ("atucComb1", 2), ("atucQuiet2", 3), ("atucComb2", 4), ("atucIcomb1", 5), ("atucLineprob", 6), ("atucQuiet3", 7), ("atucComb3", 8), ("atucIComb2", 9), ("atucMsgfmt", 10), ("atucMsgpcb", 11), ("atucQuiet4", 12), ("atucReverb1", 13), ("atucTref1", 14), ("atucReverb2", 15), ("atucEct", 16), ("atucReverb3", 17), ("atucTref2", 18), ("atucReverb4", 19), ("atucSegue1", 20), ("atucMsg1", 21), ("atucReverb5", 22), ("atucSegue2", 23), ("atucMedley", 24), ("atucExchmarker", 25), ("atucMsg2", 26), ("atucReverb6", 27), ("atucSegue3", 28), ("atucParams", 29), ("atucReverb7", 30), ("atucSegue4", 31), ("atucShowtime", 32), ("aturG9941", 100), ("aturQuiet1", 101), ("aturComb1", 102), ("aturQuiet2", 103), ("aturComb2", 104), ("aturIcomb1", 105), ("aturLineprob", 106), ("aturQuiet3", 107), ("aturComb3", 108), ("aturIcomb2", 109), ("aturMsgfmt", 110), ("aturMsgpcb", 111), ("aturReverb1", 112), ("aturQuiet4", 113), ("aturReverb2", 114), ("aturQuiet5", 115), ("aturReverb3", 116), ("aturEct", 117), ("aturReverb4", 118), ("aturSegue1", 119), ("aturReverb5", 120), ("aturSegue2", 121), ("aturMsg1", 122), ("aturMedley", 123), ("aturExchmarker", 124), ("aturMsg2", 125), ("aturReverb6", 126), ("aturSegue3", 127), ("aturParams", 128), ("aturReverb7", 129), ("aturSegue4", 130), ("aturShowtime", 131))

class Adsl2LineStatus(TextualConvention, Bits):
    description = 'Attributes with this syntax are status parameters that reflect the failure status for a given endpoint of ADSL/ADSL2 or ADSL2+ link. This BITS structure can report the following failures: noDefect(0) - This bit position positively reports that no defect or failure exists. lossOfFrame(1) - Loss of frame synchronization. lossOfSignal(2) - Loss of signal. lossOfPower(3) - Loss of power. Usually this failure may be reported for ATU-Rs only. initFailure(4) - Recent initialization process failed. Never active on ATU-R.'
    status = 'current'
    namedValues = NamedValues(("noDefect", 0), ("lossOfFrame", 1), ("lossOfSignal", 2), ("lossOfPower", 3), ("initFailure", 4))

class Adsl2ChAtmStatus(TextualConvention, Bits):
    description = 'Attributes with this syntax are status parameters that reflect the failure status for Transmission Convergence (TC) layer of a given ATM interface (data path over an ADSL/ADSL2 or ADSL2+ link). This BITS structure can report the following failures: noDefect(0) - This bit position positively reports that no defect or failure exists. noCellDelineation(1) - The link was successfully initialized, but cell delineation was never acquired on the associated ATM data path. lossOfCellDelineation(2) - Loss of cell delineation on the associated ATM data path.'
    status = 'current'
    namedValues = NamedValues(("noDefect", 0), ("noCellDelineation", 1), ("lossOfCellDelineation", 2))

class Adsl2ChPtmStatus(TextualConvention, Bits):
    description = 'Attributes with this syntax are status parameters that reflect the failure status for a given PTM interface (packet data path over an ADSL/ADSL2 or ADSL2+ link). This BITS structure can report the following failures: noDefect(0) - This bit position positively reports that no defect or failure exists. outOfSync(1) - Out of synchronization.'
    status = 'current'
    namedValues = NamedValues(("noDefect", 0), ("outOfSync", 1))

mibBuilder.exportSymbols("ADSL2-LINE-TC-MIB", Adsl2LineLdsf=Adsl2LineLdsf, Adsl2LineStatus=Adsl2LineStatus, Adsl2Direction=Adsl2Direction, Adsl2SymbolProtection=Adsl2SymbolProtection, Adsl2ChAtmStatus=Adsl2ChAtmStatus, Adsl2LastTransmittedState=Adsl2LastTransmittedState, Adsl2ConfPmsForce=Adsl2ConfPmsForce, Adsl2Unit=Adsl2Unit, Adsl2PsdMaskUs=Adsl2PsdMaskUs, Adsl2ScMaskUs=Adsl2ScMaskUs, Adsl2InitResult=Adsl2InitResult, Adsl2RaMode=Adsl2RaMode, Adsl2RfiDs=Adsl2RfiDs, Adsl2ScMaskDs=Adsl2ScMaskDs, PYSNMP_MODULE_ID=adsl2TCMIB, Adsl2Tssi=Adsl2Tssi, adsl2TCMIB=adsl2TCMIB, Adsl2MaxBer=Adsl2MaxBer, Adsl2OperationModes=Adsl2OperationModes, Adsl2PowerMngState=Adsl2PowerMngState, Adsl2PsdMaskDs=Adsl2PsdMaskDs, Adsl2ChPtmStatus=Adsl2ChPtmStatus, Adsl2LConfProfPmMode=Adsl2LConfProfPmMode, Adsl2TransmissionModeType=Adsl2TransmissionModeType, Adsl2LdsfResult=Adsl2LdsfResult)
