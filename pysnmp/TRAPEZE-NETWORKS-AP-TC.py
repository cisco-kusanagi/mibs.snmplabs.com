#
# PySNMP MIB module TRAPEZE-NETWORKS-AP-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-AP-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, IpAddress, Bits, MibIdentifier, TimeTicks, iso, Unsigned32, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "IpAddress", "Bits", "MibIdentifier", "TimeTicks", "iso", "Unsigned32", "Integer32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzApTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 3))
trpzApTc.setRevisions(('2011-10-05 02:32', '2011-01-28 02:20', '2011-01-28 02:10', '2010-11-30 02:01', '2010-11-29 01:31', '2009-07-21 01:03', '2008-12-02 01:01', '2008-11-27 01:00', '2008-11-26 00:51', '2008-10-06 00:50', '2008-05-07 00:41', '2008-02-14 00:32', '2007-12-03 00:30', '2007-07-06 00:23', '2007-07-05 00:22', '2006-07-10 00:15', '2006-03-30 00:14',))
if mibBuilder.loadTexts: trpzApTc.setLastUpdated('201110050232Z')
if mibBuilder.loadTexts: trpzApTc.setOrganization('Trapeze Networks')
class TrpzAccessType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ap", 1), ("dap", 2), ("wired", 3))

class TrpzApAttachType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("directAttach", 1), ("networkAttach", 2))

class TrpzApPortOrDapNum(TextualConvention, Unsigned32):
    status = 'obsolete'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 1000)

class TrpzApNum(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 9999)

class TrpzApState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 10, 20))
    namedValues = NamedValues(("cleared", 1), ("init", 2), ("bootStarted", 3), ("imageDownloaded", 4), ("connectFailed", 5), ("configuring", 6), ("operational", 7), ("redundant", 10), ("connOutage", 20))

class TrpzApTransition(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 10, 11, 20, 21, 22))
    namedValues = NamedValues(("clear", 1), ("timeout", 2), ("reset", 3), ("bootSuccess", 4), ("startConfiguring", 5), ("connectFail", 6), ("setBackupConn", 10), ("startHandoverReconfiguring", 11), ("connLost", 20), ("connRestored", 21), ("connOutageExtendedTimeout", 22))

class TrpzApFailDetail(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 11, 12, 91, 92, 99))
    namedValues = NamedValues(("secureHandshakeFailure", 2), ("fingerprintRequired", 3), ("fingerprintMismatch", 4), ("portLinkUp", 11), ("portLinkDown", 12), ("normalTransition", 91), ("adminRequest", 92), ("failUnknown", 99))

class TrpzApConnectSecurityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("secure", 1), ("insecure", 2), ("auto", 3))

class TrpzApServiceAvailability(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("fullService", 1), ("noService", 2), ("degradedService", 3))

class TrpzApBias(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("high", 1), ("low", 2), ("sticky", 3))

class TrpzApSerialNum(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class TrpzApFingerprint(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(16, 16), )
class TrpzRadioNum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("radio-1", 1), ("radio-2", 2), ("not-applicable", 3))

class TrpzApRadioIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TrpzApRadioIndexOrZero(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
class TrpzPowerLevel(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class TrpzRadioPowerChangeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("dup-pkts-threshold-exceed", 1), ("retransmit-threshold-exceed", 2), ("clients-optimal-performance-reached", 3), ("def-power-threshold-exceed", 4))

class TrpzChannelChangeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("util-index", 1), ("rexmit-pkt-offset", 2), ("noise-offset", 3), ("noise", 4), ("utilization", 5), ("phy-error-offset", 6), ("crc-errors-offset", 7), ("radar-detected", 8))

class TrpzChannelNum(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1024)

class TrpzRadioEnable(TextualConvention, Integer32):
    status = 'obsolete'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class TrpzRadioMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("sentry", 3))

class TrpzRadioConfigState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("configInit", 1), ("configFail", 2), ("configOk", 3))

class TrpzRadioRate(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(10, 540), )
class TrpzRadioRateEx(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43))
    namedValues = NamedValues(("rateUnknown", 1), ("rate1", 2), ("rate2", 3), ("rate5-5", 4), ("rate6", 5), ("rate9", 6), ("rate11", 7), ("rate12", 8), ("rate18", 9), ("rate24", 10), ("rate36", 11), ("rate48", 12), ("rate54", 13), ("rateMCS0", 20), ("rateMCS1", 21), ("rateMCS2", 22), ("rateMCS3", 23), ("rateMCS4", 24), ("rateMCS5", 25), ("rateMCS6", 26), ("rateMCS7", 27), ("rateMCS8", 28), ("rateMCS9", 29), ("rateMCS10", 30), ("rateMCS11", 31), ("rateMCS12", 32), ("rateMCS13", 33), ("rateMCS14", 34), ("rateMCS15", 35), ("rateMCS16", 36), ("rateMCS17", 37), ("rateMCS18", 38), ("rateMCS19", 39), ("rateMCS20", 40), ("rateMCS21", 41), ("rateMCS22", 42), ("rateMCS23", 43))

class TrpzRadioType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("typeUnknown", 1), ("typeA", 2), ("typeB", 3), ("typeG", 4), ("typeNA", 5), ("typeNG", 6))

class TrpzRssi(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-100, 0)

class TrpzApWasOperational(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("oper", 1), ("nonOper", 2))

class TrpzRadioChannelWidth(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("channelWidth20MHz", 1), ("channelWidth40MHz", 2))

class TrpzRadioMimoState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("mimoOther", 1), ("mimo1x1", 2), ("mimo2x3", 3), ("mimo3x3", 4))

class TrpzApPowerMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("auto", 1), ("high", 2))

class TrpzApLedMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("auto", 1), ("static", 2), ("off", 3))

class TrpzRadioAntennaLocation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("indoors", 1), ("outdoors", 2))

class TrpzCryptoType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("other", 1), ("clear", 2), ("wep", 3), ("wep40", 4), ("wep104", 5), ("tkip", 6), ("aesCcmp", 7), ("sms4", 8))

mibBuilder.exportSymbols("TRAPEZE-NETWORKS-AP-TC", TrpzPowerLevel=TrpzPowerLevel, TrpzApRadioIndexOrZero=TrpzApRadioIndexOrZero, TrpzRadioMode=TrpzRadioMode, TrpzApServiceAvailability=TrpzApServiceAvailability, TrpzApPortOrDapNum=TrpzApPortOrDapNum, TrpzApTransition=TrpzApTransition, TrpzApAttachType=TrpzApAttachType, TrpzRadioRate=TrpzRadioRate, trpzApTc=trpzApTc, TrpzRadioEnable=TrpzRadioEnable, TrpzApRadioIndex=TrpzApRadioIndex, TrpzRadioMimoState=TrpzRadioMimoState, TrpzApFailDetail=TrpzApFailDetail, TrpzAccessType=TrpzAccessType, TrpzApFingerprint=TrpzApFingerprint, TrpzApState=TrpzApState, TrpzApNum=TrpzApNum, TrpzChannelChangeType=TrpzChannelChangeType, TrpzRadioNum=TrpzRadioNum, TrpzRadioType=TrpzRadioType, TrpzRadioChannelWidth=TrpzRadioChannelWidth, TrpzApPowerMode=TrpzApPowerMode, TrpzRadioPowerChangeType=TrpzRadioPowerChangeType, TrpzRssi=TrpzRssi, TrpzCryptoType=TrpzCryptoType, PYSNMP_MODULE_ID=trpzApTc, TrpzChannelNum=TrpzChannelNum, TrpzRadioAntennaLocation=TrpzRadioAntennaLocation, TrpzApConnectSecurityType=TrpzApConnectSecurityType, TrpzRadioConfigState=TrpzRadioConfigState, TrpzApBias=TrpzApBias, TrpzApSerialNum=TrpzApSerialNum, TrpzApLedMode=TrpzApLedMode, TrpzApWasOperational=TrpzApWasOperational, TrpzRadioRateEx=TrpzRadioRateEx)
