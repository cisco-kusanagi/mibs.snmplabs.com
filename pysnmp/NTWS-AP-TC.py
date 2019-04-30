#
# PySNMP MIB module NTWS-AP-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-AP-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 20:15:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, NotificationType, MibIdentifier, ObjectIdentity, Counter64, TimeTicks, Gauge32, Unsigned32, Bits, iso, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "MibIdentifier", "ObjectIdentity", "Counter64", "TimeTicks", "Gauge32", "Unsigned32", "Bits", "iso", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsApTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 3))
ntwsApTc.setRevisions(('2009-07-21 01:03', '2008-12-02 01:01', '2008-11-27 01:00', '2008-11-26 00:51', '2008-10-06 00:50', '2008-05-07 00:41', '2008-02-14 00:32', '2007-12-03 00:30', '2007-09-25 00:24', '2007-07-06 00:23', '2007-07-05 00:22', '2006-07-10 00:15', '2006-03-30 00:14',))
if mibBuilder.loadTexts: ntwsApTc.setLastUpdated('200907210103Z')
if mibBuilder.loadTexts: ntwsApTc.setOrganization('Nortel Networks')
class NtwsAccessType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ap", 1), ("dap", 2), ("wired", 3))

class NtwsApAttachType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("directAttach", 1), ("networkAttach", 2))

class NtwsApPortOrDapNum(TextualConvention, Unsigned32):
    status = 'obsolete'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 1000)

class NtwsApNum(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 9999)

class NtwsApState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("cleared", 1), ("init", 2), ("bootStarted", 3), ("imageDownloaded", 4), ("connectFailed", 5), ("configuring", 6), ("configured", 7))

class NtwsApTransition(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("clear", 1), ("timeout", 2), ("reset", 3), ("bootSuccess", 4), ("startConfiguring", 5), ("connectFail", 6))

class NtwsApFailDetail(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 11, 12, 91, 99))
    namedValues = NamedValues(("secureHandshakeFailure", 2), ("fingerprintRequired", 3), ("fingerprintMismatch", 4), ("portLinkUp", 11), ("portLinkDown", 12), ("normalTransition", 91), ("failUnknown", 99))

class NtwsApConnectSecurityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("secure", 1), ("insecure", 2), ("auto", 3))

class NtwsApServiceAvailability(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("fullService", 1), ("noService", 2), ("degradedService", 3))

class NtwsApBias(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("high", 1), ("low", 2), ("sticky", 3))

class NtwsApSerialNum(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class NtwsApFingerprint(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(16, 16), )
class NtwsRadioNum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("radio-1", 1), ("radio-2", 2), ("not-applicable", 3))

class NtwsApRadioIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class NtwsApRadioIndexOrZero(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
class NtwsPowerLevel(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class NtwsRadioPowerChangeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("dup-pkts-threshold-exceed", 1), ("retransmit-threshold-exceed", 2), ("clients-optimal-performance-reached", 3), ("def-power-threshold-exceed", 4))

class NtwsChannelChangeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("util-index", 1), ("rexmit-pkt-offset", 2), ("noise-offset", 3), ("noise", 4), ("utilization", 5), ("phy-error-offset", 6), ("crc-errors-offset", 7), ("radar-detected", 8))

class NtwsChannelNum(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1024)

class NtwsRadioEnable(TextualConvention, Integer32):
    status = 'obsolete'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class NtwsRadioMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("sentry", 3))

class NtwsRadioConfigState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("configInit", 1), ("configFail", 2), ("configOk", 3))

class NtwsRadioRate(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(10, 540), )
class NtwsRadioRateEx(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35))
    namedValues = NamedValues(("rateUnknown", 1), ("rate1", 2), ("rate2", 3), ("rate5-5", 4), ("rate6", 5), ("rate9", 6), ("rate11", 7), ("rate12", 8), ("rate18", 9), ("rate24", 10), ("rate36", 11), ("rate48", 12), ("rate54", 13), ("rateMCS0", 20), ("rateMCS1", 21), ("rateMCS2", 22), ("rateMCS3", 23), ("rateMCS4", 24), ("rateMCS5", 25), ("rateMCS6", 26), ("rateMCS7", 27), ("rateMCS8", 28), ("rateMCS9", 29), ("rateMCS10", 30), ("rateMCS11", 31), ("rateMCS12", 32), ("rateMCS13", 33), ("rateMCS14", 34), ("rateMCS15", 35))

class NtwsRadioType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("typeUnknown", 1), ("typeA", 2), ("typeB", 3), ("typeG", 4), ("typeNA", 5), ("typeNG", 6))

class NtwsRssi(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-100, 0)

class NtwsApWasOperational(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("oper", 1), ("nonOper", 2))

class NtwsRadioChannelWidth(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("channelWidth20MHz", 1), ("channelWidth40MHz", 2))

class NtwsRadioMimoState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("mimoOther", 1), ("mimo1x1", 2), ("mimo2x3", 3), ("mimo3x3", 4))

class NtwsApPowerMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("auto", 1), ("high", 2))

class NtwsApLedMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("auto", 1), ("static", 2), ("off", 3))

class NtwsRadioAntennaLocation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("indoors", 1), ("outdoors", 2))

class NtwsCryptoType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("clear", 2), ("wep", 3), ("wep40", 4), ("wep104", 5), ("tkip", 6), ("aesCcmp", 7))

mibBuilder.exportSymbols("NTWS-AP-TC", NtwsApRadioIndex=NtwsApRadioIndex, NtwsApFailDetail=NtwsApFailDetail, NtwsRadioNum=NtwsRadioNum, ntwsApTc=ntwsApTc, NtwsCryptoType=NtwsCryptoType, PYSNMP_MODULE_ID=ntwsApTc, NtwsRadioEnable=NtwsRadioEnable, NtwsRadioMimoState=NtwsRadioMimoState, NtwsRadioType=NtwsRadioType, NtwsApNum=NtwsApNum, NtwsApSerialNum=NtwsApSerialNum, NtwsApPortOrDapNum=NtwsApPortOrDapNum, NtwsRadioAntennaLocation=NtwsRadioAntennaLocation, NtwsApConnectSecurityType=NtwsApConnectSecurityType, NtwsRadioConfigState=NtwsRadioConfigState, NtwsChannelChangeType=NtwsChannelChangeType, NtwsRadioRateEx=NtwsRadioRateEx, NtwsPowerLevel=NtwsPowerLevel, NtwsApPowerMode=NtwsApPowerMode, NtwsApBias=NtwsApBias, NtwsApTransition=NtwsApTransition, NtwsApState=NtwsApState, NtwsApServiceAvailability=NtwsApServiceAvailability, NtwsRadioChannelWidth=NtwsRadioChannelWidth, NtwsApRadioIndexOrZero=NtwsApRadioIndexOrZero, NtwsApLedMode=NtwsApLedMode, NtwsRadioPowerChangeType=NtwsRadioPowerChangeType, NtwsRssi=NtwsRssi, NtwsAccessType=NtwsAccessType, NtwsApAttachType=NtwsApAttachType, NtwsApFingerprint=NtwsApFingerprint, NtwsApWasOperational=NtwsApWasOperational, NtwsChannelNum=NtwsChannelNum, NtwsRadioRate=NtwsRadioRate, NtwsRadioMode=NtwsRadioMode)
