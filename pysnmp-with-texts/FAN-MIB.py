#
# PySNMP MIB module FAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:11:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Bits, TimeTicks, ObjectIdentity, Counter64, IpAddress, ModuleIdentity, Counter32, Unsigned32, Integer32, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Bits", "TimeTicks", "ObjectIdentity", "Counter64", "IpAddress", "ModuleIdentity", "Counter32", "Unsigned32", "Integer32", "NotificationType", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpicfFanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54))
hpicfFanMIB.setRevisions(('2008-08-27 10:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfFanMIB.setRevisionsDescriptions(('Revision 01.',))
if mibBuilder.loadTexts: hpicfFanMIB.setLastUpdated('200808271030Z')
if mibBuilder.loadTexts: hpicfFanMIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfFanMIB.setContactInfo('Hewlett-Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfFanMIB.setDescription('The MIB module is for representing switch fan entity.')
class HpicfDcFanIndex(TextualConvention, Unsigned32):
    description = 'A unique value that serves as an index to identify the fan.'
    status = 'current'
    displayHint = 'd'

class HpicfDcFanType(TextualConvention, Integer32):
    description = 'An enumerated value that indications the fan types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("mm", 1), ("fm", 2), ("im", 3), ("ps", 4), ("rollup", 5), ("maxtype", 6))

class HpicfDcFanAirflowDirection(TextualConvention, Integer32):
    description = 'An enumerated value which provides an indication of the fan airflow direction. The Physical fan airflow direction could be either from the port towards the power supply module i.e. portToPower(1), or from the power supply module towards the port i.e. powerToPort(2)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("portToPower", 1), ("powerToPort", 2))

class HpicfDcFanState(TextualConvention, Integer32):
    description = 'An enumerated value which provides an indication of the fan state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("failed", 0), ("removed", 1), ("off", 2), ("underspeed", 3), ("overspeed", 4), ("ok", 5), ("maxstate", 6))

hpicfFanScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 1))
hpicfFanUserPrefAirflowDir = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("portToPower", 1), ("powerToPort", 2))).clone('powerToPort')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFanUserPrefAirflowDir.setStatus('current')
if mibBuilder.loadTexts: hpicfFanUserPrefAirflowDir.setDescription('The user preferred fan airflow direction. The direction could be powerToPort or portToPower. The actual fan direction has to be changed manually, this will be used to indicate to the user when when the actual fan airflow direction is different from the user preferred airflow direction.')
hpicfEntityFan = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2))
hpicfFanTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1), )
if mibBuilder.loadTexts: hpicfFanTable.setStatus('current')
if mibBuilder.loadTexts: hpicfFanTable.setDescription('This table contains one row for every fan in the switch entity.')
hpicfFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1), ).setIndexNames((0, "FAN-MIB", "hpicfFanIndex"))
if mibBuilder.loadTexts: hpicfFanEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfFanEntry.setDescription('Information about fan entity table.')
hpicfFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 1), HpicfDcFanIndex())
if mibBuilder.loadTexts: hpicfFanIndex.setStatus('current')
if mibBuilder.loadTexts: hpicfFanIndex.setDescription('The index that is used to access the switch fan entry table.')
hpicfFanTray = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFanTray.setStatus('current')
if mibBuilder.loadTexts: hpicfFanTray.setDescription('The tray number in which the fan is docked.')
hpicfFanType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 3), HpicfDcFanType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFanType.setStatus('current')
if mibBuilder.loadTexts: hpicfFanType.setDescription('An indication of the vendor-specific fan.')
hpicfFanState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 4), HpicfDcFanState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFanState.setStatus('current')
if mibBuilder.loadTexts: hpicfFanState.setDescription('The current state of the fan.')
hpicfFanRecovering = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFanRecovering.setStatus('current')
if mibBuilder.loadTexts: hpicfFanRecovering.setDescription('An indication that the switch fan entity is faulty. Before declaring a fan to be good after a failure is detected, the same good indication must happen five (5) times in a row. A failure indication is always TRUE, while a good indication could be FALSE, hence this parameter is used to count the repeated good indications before declaring the fan to be good ')
hpicfFanNumFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFanNumFailures.setStatus('current')
if mibBuilder.loadTexts: hpicfFanNumFailures.setDescription('The number of times the fan has failed.')
hpicfFanAirflowDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 7), HpicfDcFanAirflowDirection()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFanAirflowDirection.setStatus('current')
if mibBuilder.loadTexts: hpicfFanAirflowDirection.setDescription('Indication of the fan air flow direction, either from Power supply towards the port or from the port towards the power supply.')
hpicfFanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 3))
hpicfFanCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 3, 1))
hpicfFanGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 3, 2))
hpicfDcFanCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 3, 1, 1)).setObjects(("FAN-MIB", "hpicfFanScalarsGroup"), ("FAN-MIB", "hpicfFanGroup"), ("FAN-MIB", "hpicfFanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDcFanCompliance = hpicfDcFanCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfDcFanCompliance.setDescription('The compliance statement for entries which implement the FAN MIB.')
hpicfFanScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 3, 2, 1)).setObjects(("FAN-MIB", "hpicfFanUserPrefAirflowDir"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFanScalarsGroup = hpicfFanScalarsGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfFanScalarsGroup.setDescription('Basic Scalars required in FAN MIB implementation.')
hpicfFanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 3, 2, 2)).setObjects(("FAN-MIB", "hpicfFanTray"), ("FAN-MIB", "hpicfFanType"), ("FAN-MIB", "hpicfFanState"), ("FAN-MIB", "hpicfFanRecovering"), ("FAN-MIB", "hpicfFanNumFailures"), ("FAN-MIB", "hpicfFanAirflowDirection"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFanGroup = hpicfFanGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfFanGroup.setDescription('FAN MIB parameters ')
mibBuilder.exportSymbols("FAN-MIB", HpicfDcFanState=HpicfDcFanState, hpicfEntityFan=hpicfEntityFan, hpicfFanUserPrefAirflowDir=hpicfFanUserPrefAirflowDir, hpicfFanGroups=hpicfFanGroups, HpicfDcFanAirflowDirection=HpicfDcFanAirflowDirection, hpicfFanTray=hpicfFanTray, hpicfFanMIB=hpicfFanMIB, hpicfFanAirflowDirection=hpicfFanAirflowDirection, hpicfFanState=hpicfFanState, hpicfDcFanCompliance=hpicfDcFanCompliance, hpicfFanTable=hpicfFanTable, hpicfFanScalars=hpicfFanScalars, hpicfFanType=hpicfFanType, hpicfFanConformance=hpicfFanConformance, hpicfFanRecovering=hpicfFanRecovering, PYSNMP_MODULE_ID=hpicfFanMIB, hpicfFanEntry=hpicfFanEntry, hpicfFanScalarsGroup=hpicfFanScalarsGroup, hpicfFanNumFailures=hpicfFanNumFailures, HpicfDcFanIndex=HpicfDcFanIndex, hpicfFanIndex=hpicfFanIndex, HpicfDcFanType=HpicfDcFanType, hpicfFanGroup=hpicfFanGroup, hpicfFanCompliance=hpicfFanCompliance)
