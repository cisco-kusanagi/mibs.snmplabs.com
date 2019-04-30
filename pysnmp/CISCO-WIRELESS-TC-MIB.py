#
# PySNMP MIB module CISCO-WIRELESS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WIRELESS-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:05:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, Bits, IpAddress, ModuleIdentity, Integer32, Counter32, NotificationType, ObjectIdentity, Counter64, TimeTicks, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "Bits", "IpAddress", "ModuleIdentity", "Integer32", "Counter32", "NotificationType", "ObjectIdentity", "Counter64", "TimeTicks", "iso", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWirelessTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 137))
ciscoWirelessTextualConventions.setRevisions(('2000-04-03 00:00',))
if mibBuilder.loadTexts: ciscoWirelessTextualConventions.setLastUpdated('200004030000Z')
if mibBuilder.loadTexts: ciscoWirelessTextualConventions.setOrganization('Cisco Systems, Inc.')
class CwrRFZeroIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2)

class CwrCwErrorFreeSecond(TextualConvention, Gauge32):
    status = 'current'

class CwrCwErroredSecond(TextualConvention, Gauge32):
    status = 'current'

class CwrCwSeverelyErroredSecond(TextualConvention, Gauge32):
    status = 'current'

class CwrCwConsecutiveSevErrSecond(TextualConvention, Gauge32):
    status = 'current'

class CwrCwDegradedSecond(TextualConvention, Gauge32):
    status = 'current'

class CwrCwDegradedMinute(TextualConvention, Gauge32):
    status = 'current'

class CwrCollectionAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("actionStop", 1), ("actionStart", 2), ("actionClear", 3), ("actionRestart", 4))

class CwrCollectionStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("statusIdle", 1), ("statusInProgress", 2), ("statusStopped", 3), ("statusCaptured", 4))

class CwrdBm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-80, 33)

class CwrdB(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 16)

class CwrThreshLimitType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("upChange", 1), ("downChange", 2), ("highThresh", 3), ("lowThresh", 4), ("upLimit", 5), ("lowLimit", 6))

class CwrRadioSignalAttribute(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("rsaIN", 1), ("rsaINR", 2), ("rsaConstellationVariance", 3), ("rsaTimingOffset", 4), ("rsaReceivedPower", 5), ("rsaGainSettingsIF", 6), ("rsaGainSettingsRF", 7), ("rsaFreqOffset", 8), ("rsaTotalGain", 9), ("rsaSyncStatus", 10))

class CwrOscState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("oscillatorOk", 1), ("osccillatorBad", 2))

class P2mpRadioSignalAttribute(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("none", 0), ("rsaSinrMainAnt", 1), ("rsaSinrDiversityAnt", 2), ("rsaSinrRatio", 3), ("rsaTimingOffset", 4), ("rsaRxPowerMainAnt", 5), ("rsaRxPowerDiversityAnt", 6), ("rsaChDelaySpreadMainAnt", 7), ("rsaChDelaySpreadDiversityAnt", 8), ("rsaHeAmbientNoise", 9), ("rsaSuRxPowerDeltaMainAnt", 10), ("rsaSuRxPowerDeltaDiversityAnt", 11), ("rsaSuTotalTxPower", 12))

class CwrRfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("main", 0), ("diversity", 1))

class CwrFixedPointScale(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("yocto", 1), ("zepto", 2), ("atto", 3), ("femto", 4), ("pico", 5), ("nano", 6), ("micro", 7), ("milli", 8), ("units", 9), ("kilo", 10), ("mega", 11), ("giga", 12), ("tera", 13), ("exa", 14), ("peta", 15), ("zetta", 16), ("yotta", 17))

class CwrFixedPointPrecision(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 9)

class CwrFixedPointValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483648, 2147483647)

class P2mpSnapshotAttribute(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class CwrPercentageValue(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 10000000)

class CwrUpdateTime(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CwrRfFreqRange(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 60000000)

class WirelessGauge64(TextualConvention, Counter64):
    status = 'current'

mibBuilder.exportSymbols("CISCO-WIRELESS-TC-MIB", CwrThreshLimitType=CwrThreshLimitType, CwrCwErroredSecond=CwrCwErroredSecond, CwrCwSeverelyErroredSecond=CwrCwSeverelyErroredSecond, CwrCwConsecutiveSevErrSecond=CwrCwConsecutiveSevErrSecond, CwrCollectionStatus=CwrCollectionStatus, CwrCwDegradedSecond=CwrCwDegradedSecond, CwrFixedPointPrecision=CwrFixedPointPrecision, CwrdBm=CwrdBm, CwrUpdateTime=CwrUpdateTime, CwrdB=CwrdB, CwrFixedPointScale=CwrFixedPointScale, CwrRFZeroIndex=CwrRFZeroIndex, CwrCollectionAction=CwrCollectionAction, CwrRadioSignalAttribute=CwrRadioSignalAttribute, CwrOscState=CwrOscState, CwrRfType=CwrRfType, CwrFixedPointValue=CwrFixedPointValue, PYSNMP_MODULE_ID=ciscoWirelessTextualConventions, CwrRfFreqRange=CwrRfFreqRange, P2mpSnapshotAttribute=P2mpSnapshotAttribute, CwrCwErrorFreeSecond=CwrCwErrorFreeSecond, WirelessGauge64=WirelessGauge64, ciscoWirelessTextualConventions=ciscoWirelessTextualConventions, P2mpRadioSignalAttribute=P2mpRadioSignalAttribute, CwrCwDegradedMinute=CwrCwDegradedMinute, CwrPercentageValue=CwrPercentageValue)
