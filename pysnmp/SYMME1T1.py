#
# PySNMP MIB module SYMME1T1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMME1T1
# Produced by pysmi-0.3.4 at Tue Jul 30 11:34:19 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifIndex, ifNumber = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifNumber")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, iso, MibIdentifier, NotificationType, ObjectIdentity, Counter64, Bits, Counter32, Gauge32, IpAddress, Unsigned32, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "MibIdentifier", "NotificationType", "ObjectIdentity", "Counter64", "Bits", "Counter32", "Gauge32", "IpAddress", "Unsigned32", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
EnableValue, ONVALUETYPE, symmPhysicalSignal = mibBuilder.importSymbols("SYMM-COMMON-SMI", "EnableValue", "ONVALUETYPE", "symmPhysicalSignal")
symmE1T1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2))
symmE1T1.setRevisions(('2011-03-18 17:06',))
if mibBuilder.loadTexts: symmE1T1.setLastUpdated('201103181705Z')
if mibBuilder.loadTexts: symmE1T1.setOrganization('Symmetricom.')
class TP5000PQLVALUE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 15)

class INPUTE1T1FRAMETYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("freq1544khz", 1), ("freq2048khz", 2), ("ccs", 3), ("cas", 4), ("d4", 5), ("esf", 6))

class PORTSTATETYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class OUTPUTE1T1FRAMETYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("freq1544khz", 1), ("freq2048khz", 2), ("ccs", 3), ("cas", 4), ("d4", 5), ("esf", 6))

class DateAndTime(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d:1d.1d,1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
class TLatAndLon(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a1d:1d:1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(5, 5)
    fixedLength = 5

class TAntHeight(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a2d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class TLocalTimeOffset(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class TSsm(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

e1T1input = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1))
inputE1T1Status = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 1))
e1T1InputStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 1, 1), )
if mibBuilder.loadTexts: e1T1InputStatusTable.setStatus('current')
e1T1InputStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMME1T1", "e1T1InputStatusIndex"))
if mibBuilder.loadTexts: e1T1InputStatusEntry.setStatus('current')
e1T1InputStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: e1T1InputStatusIndex.setStatus('current')
e1T1InputPQLCurValueV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 1, 1, 1, 3), TP5000PQLVALUE()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1T1InputPQLCurValueV1.setStatus('current')
e1T1InputPortStatusV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1T1InputPortStatusV1.setStatus('current')
e1T1InputConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2))
e1T1InputConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1), )
if mibBuilder.loadTexts: e1T1InputConfigTable.setStatus('current')
e1T1InputConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMME1T1", "e1T1InputConfigIndex"))
if mibBuilder.loadTexts: e1T1InputConfigEntry.setStatus('current')
e1T1InputConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: e1T1InputConfigIndex.setStatus('current')
e1T1InputFrameTypeV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 2), INPUTE1T1FRAMETYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1InputFrameTypeV1.setStatus('current')
e1T1InputCRCStateV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 3), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1InputCRCStateV1.setStatus('current')
e1T1InputSSMStateV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 4), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1InputSSMStateV1.setStatus('current')
e1T1InputSSMBitV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1InputSSMBitV1.setStatus('current')
e1T1InputPQLValueV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 6), TP5000PQLVALUE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1InputPQLValueV1.setStatus('current')
eT1InputZeroSupprV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 7), ONVALUETYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eT1InputZeroSupprV1.setStatus('current')
e1T1Output = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2))
e1T1OutputStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 1))
e1T1OutputStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 1, 1), )
if mibBuilder.loadTexts: e1T1OutputStatusTable.setStatus('current')
e1T1OutputStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMME1T1", "e1T1OutputStatusIndex"))
if mibBuilder.loadTexts: e1T1OutputStatusEntry.setStatus('current')
e1T1OutputStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: e1T1OutputStatusIndex.setStatus('current')
e1T1OutputPortStatusV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1T1OutputPortStatusV1.setStatus('current')
e1T1OutputPQLValueV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 1, 1, 1, 3), TP5000PQLVALUE()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1T1OutputPQLValueV1.setStatus('current')
e1T1OutputConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2))
e1T1OutputConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1), )
if mibBuilder.loadTexts: e1T1OutputConfigTable.setStatus('current')
e1T1OutputConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMME1T1", "e1T1OutputConfigIndex"))
if mibBuilder.loadTexts: e1T1OutputConfigEntry.setStatus('current')
e1T1OutputConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: e1T1OutputConfigIndex.setStatus('current')
e1T1OutputStateV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 2), PORTSTATETYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1OutputStateV1.setStatus('current')
e1T1OutputFrameTypeV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 3), OUTPUTE1T1FRAMETYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1OutputFrameTypeV1.setStatus('current')
e1T1OutputCRCStateV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 4), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1OutputCRCStateV1.setStatus('current')
e1T1OutputSSMStateV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 5), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1OutputSSMStateV1.setStatus('current')
e1T1OutputSSMBitV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1OutputSSMBitV1.setStatus('current')
e1T1OutputZeroSupprV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 7), ONVALUETYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1OutputZeroSupprV1.setStatus('current')
e1T1OutputLengthV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1OutputLengthV1.setStatus('current')
e1T1Conformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3))
if mibBuilder.loadTexts: e1T1Conformance.setStatus('current')
e1T1Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 1))
e1T1BasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 1, 1)).setObjects(("SYMME1T1", "e1T1InputStatusGroup"), ("SYMME1T1", "e11T1InputConfigGroup"), ("SYMME1T1", "e11T1OutputStatusGroup"), ("SYMME1T1", "e11T1OutputConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    e1T1BasicCompliance = e1T1BasicCompliance.setStatus('current')
e1T1UocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 2))
e1T1InputStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 2, 1)).setObjects(("SYMME1T1", "e1T1InputPortStatusV1"), ("SYMME1T1", "e1T1InputPQLCurValueV1"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    e1T1InputStatusGroup = e1T1InputStatusGroup.setStatus('current')
e11T1InputConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 2, 2)).setObjects(("SYMME1T1", "e1T1InputFrameTypeV1"), ("SYMME1T1", "e1T1InputCRCStateV1"), ("SYMME1T1", "e1T1InputSSMStateV1"), ("SYMME1T1", "e1T1InputSSMBitV1"), ("SYMME1T1", "e1T1InputPQLValueV1"), ("SYMME1T1", "eT1InputZeroSupprV1"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    e11T1InputConfigGroup = e11T1InputConfigGroup.setStatus('current')
e11T1OutputStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 2, 3)).setObjects(("SYMME1T1", "e1T1OutputPortStatusV1"), ("SYMME1T1", "e1T1OutputPQLValueV1"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    e11T1OutputStatusGroup = e11T1OutputStatusGroup.setStatus('current')
e11T1OutputConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 2, 4)).setObjects(("SYMME1T1", "e1T1OutputStateV1"), ("SYMME1T1", "e1T1OutputFrameTypeV1"), ("SYMME1T1", "e1T1OutputCRCStateV1"), ("SYMME1T1", "e1T1OutputSSMStateV1"), ("SYMME1T1", "e1T1OutputSSMBitV1"), ("SYMME1T1", "e1T1OutputLengthV1"), ("SYMME1T1", "e1T1OutputZeroSupprV1"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    e11T1OutputConfigGroup = e11T1OutputConfigGroup.setStatus('current')
mibBuilder.exportSymbols("SYMME1T1", e1T1InputSSMBitV1=e1T1InputSSMBitV1, DateAndTime=DateAndTime, e1T1InputConfigIndex=e1T1InputConfigIndex, e1T1InputStatusGroup=e1T1InputStatusGroup, e1T1InputSSMStateV1=e1T1InputSSMStateV1, e1T1OutputConfigIndex=e1T1OutputConfigIndex, e1T1OutputStatus=e1T1OutputStatus, e11T1OutputStatusGroup=e11T1OutputStatusGroup, e1T1InputCRCStateV1=e1T1InputCRCStateV1, e1T1BasicCompliance=e1T1BasicCompliance, e1T1OutputFrameTypeV1=e1T1OutputFrameTypeV1, e1T1OutputLengthV1=e1T1OutputLengthV1, e1T1OutputConfig=e1T1OutputConfig, e11T1OutputConfigGroup=e11T1OutputConfigGroup, inputE1T1Status=inputE1T1Status, e1T1InputStatusEntry=e1T1InputStatusEntry, TSsm=TSsm, PYSNMP_MODULE_ID=symmE1T1, TLocalTimeOffset=TLocalTimeOffset, e1T1InputStatusIndex=e1T1InputStatusIndex, symmE1T1=symmE1T1, TLatAndLon=TLatAndLon, e1T1Compliances=e1T1Compliances, e1T1InputPQLValueV1=e1T1InputPQLValueV1, e1T1OutputSSMStateV1=e1T1OutputSSMStateV1, e1T1InputConfigTable=e1T1InputConfigTable, e1T1OutputConfigEntry=e1T1OutputConfigEntry, OUTPUTE1T1FRAMETYPE=OUTPUTE1T1FRAMETYPE, e1T1OutputCRCStateV1=e1T1OutputCRCStateV1, e1T1InputStatusTable=e1T1InputStatusTable, PORTSTATETYPE=PORTSTATETYPE, e1T1Output=e1T1Output, e1T1OutputStatusIndex=e1T1OutputStatusIndex, e1T1OutputStatusEntry=e1T1OutputStatusEntry, e1T1InputFrameTypeV1=e1T1InputFrameTypeV1, eT1InputZeroSupprV1=eT1InputZeroSupprV1, TP5000PQLVALUE=TP5000PQLVALUE, e1T1InputConfig=e1T1InputConfig, e1T1OutputZeroSupprV1=e1T1OutputZeroSupprV1, e1T1OutputPQLValueV1=e1T1OutputPQLValueV1, e1T1OutputStateV1=e1T1OutputStateV1, e1T1OutputConfigTable=e1T1OutputConfigTable, e1T1Conformance=e1T1Conformance, e1T1UocGroups=e1T1UocGroups, TAntHeight=TAntHeight, INPUTE1T1FRAMETYPE=INPUTE1T1FRAMETYPE, e1T1InputPQLCurValueV1=e1T1InputPQLCurValueV1, e11T1InputConfigGroup=e11T1InputConfigGroup, e1T1OutputStatusTable=e1T1OutputStatusTable, e1T1OutputSSMBitV1=e1T1OutputSSMBitV1, e1T1InputPortStatusV1=e1T1InputPortStatusV1, e1T1input=e1T1input, e1T1OutputPortStatusV1=e1T1OutputPortStatusV1, e1T1InputConfigEntry=e1T1InputConfigEntry)
