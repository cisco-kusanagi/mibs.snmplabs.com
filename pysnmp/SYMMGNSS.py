#
# PySNMP MIB module SYMMGNSS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMGNSS
# Produced by pysmi-0.3.4 at Tue Jul 30 11:34:22 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifIndex, ifNumber = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifNumber")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, IpAddress, MibIdentifier, Unsigned32, ModuleIdentity, iso, NotificationType, Counter64, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "MibIdentifier", "Unsigned32", "ModuleIdentity", "iso", "NotificationType", "Counter64", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
YESVALUETYPE, GNSSHealthStatus, symmPhysicalSignal, GNSSPositionMode, GNSSReceiverMode = mibBuilder.importSymbols("SYMM-COMMON-SMI", "YESVALUETYPE", "GNSSHealthStatus", "symmPhysicalSignal", "GNSSPositionMode", "GNSSReceiverMode")
symmGNSS = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1))
if mibBuilder.loadTexts: symmGNSS.setLastUpdated('201808230822Z')
if mibBuilder.loadTexts: symmGNSS.setOrganization('Symmetricom')
class GNSSCURPOSITIONMODE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("surveying", 1), ("positionHold", 2), ("manual", 3))

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

gnssStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1))
gnssPortStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 1), )
if mibBuilder.loadTexts: gnssPortStatusTable.setStatus('current')
gnssPortStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMGNSS", "gnssPortStatusIndex"))
if mibBuilder.loadTexts: gnssPortStatusEntry.setStatus('current')
gnssPortStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: gnssPortStatusIndex.setStatus('current')
gnssPortStatusPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssPortStatusPortName.setStatus('current')
gnssPortCurrentGNSS = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 1, 1, 3), YESVALUETYPE()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssPortCurrentGNSS.setStatus('current')
gnssPortCurrentPosMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 1, 1, 4), GNSSCURPOSITIONMODE()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssPortCurrentPosMode.setStatus('current')
gnssSatTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2), )
if mibBuilder.loadTexts: gnssSatTable.setStatus('current')
gnssSatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMGNSS", "gnssSatIndex"))
if mibBuilder.loadTexts: gnssSatEntry.setStatus('current')
gnssSatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 125))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssSatIndex.setStatus('current')
gnssSatNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssSatNum.setStatus('current')
gnssSatSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssSatSNR.setStatus('current')
gnssSatHealth = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 4), GNSSHealthStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssSatHealth.setStatus('current')
gnssSatAzimuth = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 360))).setUnits('degrees').setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssSatAzimuth.setStatus('current')
gnssSatElevation = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 360))).setUnits('degrees').setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssSatElevation.setStatus('current')
gnssSatPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssSatPortName.setStatus('current')
gnssPresentPosTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 3), )
if mibBuilder.loadTexts: gnssPresentPosTable.setStatus('current')
gnssPresentPosEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMGNSS", "gnssPresentPosIndex"))
if mibBuilder.loadTexts: gnssPresentPosEntry.setStatus('current')
gnssPresentPosIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: gnssPresentPosIndex.setStatus('current')
gnssPresentPosLat = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssPresentPosLat.setStatus('current')
gnssPresentPosLong = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssPresentPosLong.setStatus('current')
gnssPresentPosHeight = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssPresentPosHeight.setStatus('current')
gnssConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2))
gnssConfigurationTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1), )
if mibBuilder.loadTexts: gnssConfigurationTable.setStatus('current')
gnssConfigurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMGNSS", "gnssConfigurationIndex"))
if mibBuilder.loadTexts: gnssConfigurationEntry.setStatus('current')
gnssConfigurationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: gnssConfigurationIndex.setStatus('current')
gnssConfigurationPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssConfigurationPortName.setStatus('current')
gnssConfigurationTrackMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 3), GNSSReceiverMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gnssConfigurationTrackMode.setStatus('current')
gnssConfigurationPosMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 4), GNSSPositionMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gnssConfigurationPosMode.setStatus('current')
gnssConfigurationElevMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 45))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gnssConfigurationElevMask.setStatus('current')
gnssConfigurationCableDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gnssConfigurationCableDelay.setStatus('current')
gnssConfigurationLeapSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gnssConfigurationLeapSeconds.setStatus('current')
gnssPosSettingTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 2), )
if mibBuilder.loadTexts: gnssPosSettingTable.setStatus('current')
gnssPosSettingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMGNSS", "gnssPosSettingIndex"))
if mibBuilder.loadTexts: gnssPosSettingEntry.setStatus('current')
gnssPosSettingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: gnssPosSettingIndex.setStatus('current')
gnssPosSettingLat = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 2, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gnssPosSettingLat.setStatus('current')
gnssPosSettingLong = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gnssPosSettingLong.setStatus('current')
gnssPosSettingHeight = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 2, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gnssPosSettingHeight.setStatus('current')
gnssConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3))
if mibBuilder.loadTexts: gnssConformance.setStatus('current')
gnssCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 1))
gnssBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 1, 1)).setObjects(("SYMMGNSS", "gnssStatusGroup"), ("SYMMGNSS", "gnssConfigGroup"), ("SYMMGNSS", "gnssSVGroup"), ("SYMMGNSS", "gnssConfigPosGroup"), ("SYMMGNSS", "gnssCurrentPosGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gnssBasicCompliance = gnssBasicCompliance.setStatus('current')
gnssUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 2))
gnssStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 2, 1)).setObjects(("SYMMGNSS", "gnssPortStatusPortName"), ("SYMMGNSS", "gnssPortCurrentGNSS"), ("SYMMGNSS", "gnssPortCurrentPosMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gnssStatusGroup = gnssStatusGroup.setStatus('current')
gnssConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 2, 2)).setObjects(("SYMMGNSS", "gnssConfigurationPortName"), ("SYMMGNSS", "gnssConfigurationTrackMode"), ("SYMMGNSS", "gnssConfigurationPosMode"), ("SYMMGNSS", "gnssConfigurationElevMask"), ("SYMMGNSS", "gnssConfigurationCableDelay"), ("SYMMGNSS", "gnssConfigurationLeapSeconds"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gnssConfigGroup = gnssConfigGroup.setStatus('current')
gnssSVGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 2, 3)).setObjects(("SYMMGNSS", "gnssSatIndex"), ("SYMMGNSS", "gnssSatNum"), ("SYMMGNSS", "gnssSatSNR"), ("SYMMGNSS", "gnssSatHealth"), ("SYMMGNSS", "gnssSatAzimuth"), ("SYMMGNSS", "gnssSatElevation"), ("SYMMGNSS", "gnssSatPortName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gnssSVGroup = gnssSVGroup.setStatus('current')
gnssConfigPosGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 2, 4)).setObjects(("SYMMGNSS", "gnssPosSettingLat"), ("SYMMGNSS", "gnssPosSettingLong"), ("SYMMGNSS", "gnssPosSettingHeight"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gnssConfigPosGroup = gnssConfigPosGroup.setStatus('current')
gnssCurrentPosGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 2, 5)).setObjects(("SYMMGNSS", "gnssPresentPosLat"), ("SYMMGNSS", "gnssPresentPosLong"), ("SYMMGNSS", "gnssPresentPosHeight"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gnssCurrentPosGroup = gnssCurrentPosGroup.setStatus('current')
mibBuilder.exportSymbols("SYMMGNSS", gnssPortStatusIndex=gnssPortStatusIndex, gnssPortStatusTable=gnssPortStatusTable, TSsm=TSsm, gnssPresentPosTable=gnssPresentPosTable, gnssPresentPosLat=gnssPresentPosLat, PYSNMP_MODULE_ID=symmGNSS, gnssPosSettingLat=gnssPosSettingLat, gnssPortStatusPortName=gnssPortStatusPortName, gnssBasicCompliance=gnssBasicCompliance, gnssPortCurrentGNSS=gnssPortCurrentGNSS, gnssConfigurationTrackMode=gnssConfigurationTrackMode, gnssSatPortName=gnssSatPortName, gnssCurrentPosGroup=gnssCurrentPosGroup, gnssConfig=gnssConfig, gnssSatAzimuth=gnssSatAzimuth, gnssPosSettingHeight=gnssPosSettingHeight, gnssStatusGroup=gnssStatusGroup, gnssPosSettingIndex=gnssPosSettingIndex, gnssConfigGroup=gnssConfigGroup, gnssConfigPosGroup=gnssConfigPosGroup, gnssConfigurationPosMode=gnssConfigurationPosMode, DateAndTime=DateAndTime, gnssConfigurationCableDelay=gnssConfigurationCableDelay, gnssSatElevation=gnssSatElevation, gnssPresentPosHeight=gnssPresentPosHeight, gnssPresentPosIndex=gnssPresentPosIndex, gnssPresentPosEntry=gnssPresentPosEntry, gnssConfigurationTable=gnssConfigurationTable, gnssConfigurationEntry=gnssConfigurationEntry, gnssConfigurationElevMask=gnssConfigurationElevMask, gnssPosSettingEntry=gnssPosSettingEntry, symmGNSS=symmGNSS, gnssSatHealth=gnssSatHealth, gnssConformance=gnssConformance, gnssSatEntry=gnssSatEntry, gnssPosSettingTable=gnssPosSettingTable, gnssConfigurationIndex=gnssConfigurationIndex, gnssSVGroup=gnssSVGroup, gnssSatSNR=gnssSatSNR, gnssPosSettingLong=gnssPosSettingLong, TAntHeight=TAntHeight, TLocalTimeOffset=TLocalTimeOffset, GNSSCURPOSITIONMODE=GNSSCURPOSITIONMODE, gnssStatus=gnssStatus, gnssPortStatusEntry=gnssPortStatusEntry, gnssConfigurationPortName=gnssConfigurationPortName, gnssConfigurationLeapSeconds=gnssConfigurationLeapSeconds, gnssUocGroups=gnssUocGroups, gnssPortCurrentPosMode=gnssPortCurrentPosMode, gnssSatIndex=gnssSatIndex, gnssPresentPosLong=gnssPresentPosLong, gnssSatTable=gnssSatTable, gnssCompliances=gnssCompliances, TLatAndLon=TLatAndLon, gnssSatNum=gnssSatNum)
