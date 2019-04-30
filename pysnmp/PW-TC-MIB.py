#
# PySNMP MIB module PW-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PW-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:34:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
experimental, Bits, iso, MibIdentifier, ModuleIdentity, Integer32, NotificationType, Counter64, Unsigned32, IpAddress, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "experimental", "Bits", "iso", "MibIdentifier", "ModuleIdentity", "Integer32", "NotificationType", "Counter64", "Unsigned32", "IpAddress", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
pwTCMIB = ModuleIdentity((1, 3, 6, 1, 3, 8888, 1))
pwTCMIB.setRevisions(('2003-07-28 12:00', '2003-05-01 12:00', '1902-05-28 12:00', '1902-01-30 12:00', '2001-12-20 12:00', '2001-07-12 12:00',))
if mibBuilder.loadTexts: pwTCMIB.setLastUpdated('200307281200Z')
if mibBuilder.loadTexts: pwTCMIB.setOrganization('Pseudo Wire Edge to Edge Emulation (PWE3) Working Group')
pwMIB = MibIdentifier((1, 3, 6, 1, 3, 8888))
class PwGroupID(TextualConvention, Unsigned32):
    status = 'current'

class PwVcIDType(TextualConvention, Unsigned32):
    status = 'current'

class PwVcIndexType(TextualConvention, Unsigned32):
    status = 'current'

class PwVcVlanCfg(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4097)

class PwOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7))

class PwVcType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("other", 0), ("frameRelayDlci", 1), ("atmAal5SduVcc", 2), ("atmTransparent", 3), ("ethernetTagged", 4), ("ethernet", 5), ("hdlc", 6), ("ppp", 7), ("cem", 8), ("atmCellNto1Vcc", 9), ("atmCellNto1Vpc", 10), ("ipLayer2Transport", 11), ("atmCell1to1Vcc", 12), ("atmCell1to1Vpc", 13), ("atmAal5PduVcc", 14), ("frameRelayPortMode", 15), ("cep", 16))

class PwVcAttachmentIdentifierType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class PwVcCw(TruthValue):
    status = 'current'

class PwVcRemoteCwStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("notApplicable", 0), ("waitingForNextMsg", 1), ("sentWrongBitErrorCode", 2), ("rxWithdrawWithWrongBitErrorCode", 3), ("illegalRecievedBit", 4), ("sameAsSent", 5), ("notYetKnown", 6))

class PwVcCapabilities(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("pwStatusIndication", 0))

class PwVcStatus(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("pwNotForwarding", 0), ("customerFacingPwRxFault", 1), ("customerFacingPwTxFault", 2), ("psnFacingPwRxFault", 3), ("psnFacingPwTxFault", 4))

class PwVcFragSize(TextualConvention, Unsigned32):
    status = 'current'

class PwVcFragStatus(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("noFragmantation", 0), ("cfgFragGreaterThanPsnMtu", 1), ("cfgFragButRemoteIncapable", 2), ("remoteFragCapable", 3), ("fragmantationEnabled", 4))

mibBuilder.exportSymbols("PW-TC-MIB", pwTCMIB=pwTCMIB, PYSNMP_MODULE_ID=pwTCMIB, PwVcVlanCfg=PwVcVlanCfg, PwVcAttachmentIdentifierType=PwVcAttachmentIdentifierType, PwVcCw=PwVcCw, PwVcIDType=PwVcIDType, PwVcStatus=PwVcStatus, PwVcFragStatus=PwVcFragStatus, pwMIB=pwMIB, PwVcRemoteCwStatus=PwVcRemoteCwStatus, PwOperStatus=PwOperStatus, PwVcFragSize=PwVcFragSize, PwVcType=PwVcType, PwVcIndexType=PwVcIndexType, PwVcCapabilities=PwVcCapabilities, PwGroupID=PwGroupID)
