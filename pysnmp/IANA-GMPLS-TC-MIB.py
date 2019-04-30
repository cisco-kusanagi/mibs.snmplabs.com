#
# PySNMP MIB module IANA-GMPLS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IANA-GMPLS-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:06:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibIdentifier, Integer32, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, TimeTicks, Gauge32, Unsigned32, IpAddress, iso, ModuleIdentity, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "Integer32", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "TimeTicks", "Gauge32", "Unsigned32", "IpAddress", "iso", "ModuleIdentity", "Counter64", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaGmpls = ModuleIdentity((1, 3, 6, 1, 2, 1, 152))
ianaGmpls.setRevisions(('2015-11-04 00:00', '2015-09-22 00:00', '2014-05-09 00:00', '2014-03-11 00:00', '2013-12-16 00:00', '2013-11-04 00:00', '2013-10-14 00:00', '2013-10-10 00:00', '2013-10-09 00:00', '2010-04-13 00:00', '2010-02-22 00:00', '2010-02-19 00:00', '2007-02-27 00:00',))
if mibBuilder.loadTexts: ianaGmpls.setLastUpdated('201511040000Z')
if mibBuilder.loadTexts: ianaGmpls.setOrganization('IANA')
class IANAGmplsLSPEncodingTypeTC(TextualConvention, Integer32):
    reference = '1. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, RFC 3471, section 3.1.1. 2. Generalized MPLS Signalling Extensions for G.709 Optical Transport Networks Control, RFC 4328, section 3.1.1.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5, 7, 8, 9, 11, 12, 13, 14))
    namedValues = NamedValues(("tunnelLspNotGmpls", 0), ("tunnelLspPacket", 1), ("tunnelLspEthernet", 2), ("tunnelLspAnsiEtsiPdh", 3), ("tunnelLspSdhSonet", 5), ("tunnelLspDigitalWrapper", 7), ("tunnelLspLambda", 8), ("tunnelLspFiber", 9), ("tunnelLspFiberChannel", 11), ("tunnelDigitalPath", 12), ("tunnelOpticalChannel", 13), ("tunnelLine", 14))

class IANAGmplsSwitchingTypeTC(TextualConvention, Integer32):
    reference = '1. Routing Extensions in Support of Generalized Multi-Protocol Label Switching, RFC 4202, section 2.4. 2. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, RFC 3471, section 3.1.1. 3. Revised Definition of The GMPLS Switching Capability and Type Fields, RFC7074, section 5.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 30, 40, 51, 100, 110, 125, 150, 151, 200))
    namedValues = NamedValues(("unknown", 0), ("psc1", 1), ("psc2", 2), ("psc3", 3), ("psc4", 4), ("evpl", 30), ("pbb", 40), ("l2sc", 51), ("tdm", 100), ("otntdm", 110), ("dcsc", 125), ("lsc", 150), ("wsonlsc", 151), ("fsc", 200))

class IANAGmplsGeneralizedPidTC(TextualConvention, Integer32):
    reference = '1. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, RFC 3471, section 3.1.1. 2. Generalized MPLS Signalling Extensions for G.709 Optical Transport Networks Control, RFC 4328, section 3.1.3. 3. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Extensions for the evolving G.709 Optical Transport Networks Control,[RFC7139], sections 4 and 11.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70))
    namedValues = NamedValues(("unknown", 0), ("asynchE4", 5), ("asynchDS3T3", 6), ("asynchE3", 7), ("bitsynchE3", 8), ("bytesynchE3", 9), ("asynchDS2T2", 10), ("bitsynchDS2T2", 11), ("reservedByRFC3471first", 12), ("asynchE1", 13), ("bytesynchE1", 14), ("bytesynch31ByDS0", 15), ("asynchDS1T1", 16), ("bitsynchDS1T1", 17), ("bytesynchDS1T1", 18), ("vc1vc12", 19), ("reservedByRFC3471second", 20), ("reservedByRFC3471third", 21), ("ds1SFAsynch", 22), ("ds1ESFAsynch", 23), ("ds3M23Asynch", 24), ("ds3CBitParityAsynch", 25), ("vtLovc", 26), ("stsSpeHovc", 27), ("posNoScramble16BitCrc", 28), ("posNoScramble32BitCrc", 29), ("posScramble16BitCrc", 30), ("posScramble32BitCrc", 31), ("atm", 32), ("ethernet", 33), ("sdhSonet", 34), ("digitalwrapper", 36), ("lambda", 37), ("ansiEtsiPdh", 38), ("lapsSdh", 40), ("fddi", 41), ("dqdb", 42), ("fiberChannel3", 43), ("hdlc", 44), ("ethernetV2DixOnly", 45), ("ethernet802dot3Only", 46), ("g709ODUj", 47), ("g709OTUk", 48), ("g709CBRorCBRa", 49), ("g709CBRb", 50), ("g709BSOT", 51), ("g709BSNT", 52), ("gfpIPorPPP", 53), ("gfpEthernetMAC", 54), ("gfpEthernetPHY", 55), ("g709ESCON", 56), ("g709FICON", 57), ("g709FiberChannel", 58), ("framedGFP", 59), ("sTM1", 60), ("sTM4", 61), ("infiniBand", 62), ("sDI", 63), ("sDI1point001", 64), ("dVBASI", 65), ("g709ODU125G", 66), ("g709ODUAny", 67), ("nullTest", 68), ("randomTest", 69), ("sixtyfourB66BGFPFEthernet", 70))

class IANAGmplsAdminStatusInformationTC(TextualConvention, Bits):
    reference = '1. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, RFC 3471, section 8. 2. Generalized MPLS Signaling - RSVP-TE Extensions, RFC 3473, section 7. 3. GMPLS - Communication of Alarm Information, RFC 4783, section 3.2.1.'
    status = 'current'
    namedValues = NamedValues(("reflect", 0), ("reserved1", 1), ("reserved2", 2), ("reserved3", 3), ("reserved4", 4), ("reserved5", 5), ("reserved6", 6), ("reserved7", 7), ("reserved8", 8), ("reserved9", 9), ("reserved10", 10), ("reserved11", 11), ("reserved12", 12), ("reserved13", 13), ("reserved14", 14), ("reserved15", 15), ("reserved16", 16), ("reserved17", 17), ("reserved18", 18), ("reserved19", 19), ("reserved20", 20), ("reserved21", 21), ("reserved22", 22), ("oamFlowsEnabled", 23), ("oamAlarmsEnabled", 24), ("handover", 25), ("lockout", 26), ("inhibitAlarmCommunication", 27), ("callControl", 28), ("testing", 29), ("administrativelyDown", 30), ("deleteInProgress", 31))

mibBuilder.exportSymbols("IANA-GMPLS-TC-MIB", IANAGmplsAdminStatusInformationTC=IANAGmplsAdminStatusInformationTC, PYSNMP_MODULE_ID=ianaGmpls, IANAGmplsSwitchingTypeTC=IANAGmplsSwitchingTypeTC, IANAGmplsGeneralizedPidTC=IANAGmplsGeneralizedPidTC, IANAGmplsLSPEncodingTypeTC=IANAGmplsLSPEncodingTypeTC, ianaGmpls=ianaGmpls)
