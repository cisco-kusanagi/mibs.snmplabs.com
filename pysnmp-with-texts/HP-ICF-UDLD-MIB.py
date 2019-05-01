#
# PySNMP MIB module HP-ICF-UDLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-UDLD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:35:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, IpAddress, iso, MibIdentifier, Counter32, Integer32, Unsigned32, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "iso", "MibIdentifier", "Counter32", "Integer32", "Unsigned32", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "NotificationType", "TimeTicks")
MacAddress, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString", "TruthValue")
hpicfUdldMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33))
hpicfUdldMIB.setRevisions(('2014-06-15 00:00', '2009-08-07 00:00', '2006-04-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfUdldMIB.setRevisionsDescriptions(('Added hpicfUdldConfigForwardMode, hpicfUdldConfigTimeIntervalMs.', 'Added hpicfUdldStatsClearAll - used to clear UDLD transmit, receive and state change statistics.', 'Initial revision.',))
if mibBuilder.loadTexts: hpicfUdldMIB.setLastUpdated('201406150000Z')
if mibBuilder.loadTexts: hpicfUdldMIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfUdldMIB.setContactInfo('Hewlett-Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfUdldMIB.setDescription('This MIB module describes objects to configure the UniDirectional Link Detection (UDLD) feature.')
hpicfUdldNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 0))
hpicfUdldObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1))
hpicfUdldConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2))
hpicfUdldConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1))
hpicfUdldStats = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2))
hpicfUdldConfigTimeInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 100)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUdldConfigTimeInterval.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldConfigTimeInterval.setDescription('The interval in deciseconds between UDLD packets. The same interval can also be set in milliseconds with hpicfUdldConfigTimeIntervalMs.')
hpicfUdldConfigMaxRetries = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(3, 10)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUdldConfigMaxRetries.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldConfigMaxRetries.setDescription('The number of unanswered UDLD packets allowed before declaring the link faulty.')
hpicfUdldConfigForwardMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("verifyThenForward", 1), ("forwardThenVerify", 2))).clone('forwardThenVerify')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUdldConfigForwardMode.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldConfigForwardMode.setDescription("The port transmission mode while UDLD verification is in progress. The value 'verifyThenForward' will block ports until a successful UDLD exchange is established. The value forwardThenVerify will forward traffic normally while UDLD link verification is in progress and ports will not be blocked until the UDLD retry count is exceeded.")
hpicfUdldConfigTimeIntervalMs = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000)).clone(5000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUdldConfigTimeIntervalMs.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldConfigTimeIntervalMs.setDescription('The interval in milliseconds between sending UDLD packets. The default is 5 seconds. Some devices may not allow values less than 1 second due to the load it puts on the CPU. Devices that do allow values less than 1 second may restrict the number of ports that can have UDLD enabled. Some devices may also round the value up to a multiple of their clock granularity, for example 33ms.')
hpicfUdldPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 3), )
if mibBuilder.loadTexts: hpicfUdldPortConfigTable.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldPortConfigTable.setDescription('The table that controls UDLD status on individual ports.')
hpicfUdldPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfUdldPortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldPortConfigEntry.setDescription('An entry in the hpicfUdldPortConfigTable.')
hpicfUdldPortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUdldPortAdminStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldPortAdminStatus.setDescription('The hpicfUdldPortAdminStatus can be enabled/disabled The value enable(1) means that UDLD is enabled. the value disable(2) means that UDLD is disabled.')
hpicfUdldPortVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUdldPortVlanId.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldPortVlanId.setDescription('The vlan id associated with tagged UDLD control packets. The value of 0 indicates that UDLD control packets are untagged.')
hpicfUdldPortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1), )
if mibBuilder.loadTexts: hpicfUdldPortStatsTable.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldPortStatsTable.setDescription('A table containing UDLD statistics for individual ports.')
hpicfUdldPortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfUdldPortStatsEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldPortStatsEntry.setDescription('UDLD statistics for a particular physical port.')
hpicfUdldStatsPortCurrentState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("offline", 1), ("failure", 2), ("up", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUdldStatsPortCurrentState.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldStatsPortCurrentState.setDescription("The desired status of UDLD on a port. If the associated hpicfUdldStatsPortCurrentState object has a value of 'offline(1)', then the port or udld is administratively disabled. If the associated hpicfUdldStatsPortCurrentState object has a value of 'failure(2)', then the port and udld are administratively enabled, but udld packets are not being received successfully. Link may or may not be present. If the associated hpicfUdldStatsPortCurrentState object has a value of 'up(3)', then udld is enabled and udld packets are being received successfully in both directions.")
hpicfUdldStatsPortNeighborMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUdldStatsPortNeighborMAC.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldStatsPortNeighborMAC.setDescription('The MAC address of the adjacent switch.')
hpicfUdldStatsPortNeighborPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUdldStatsPortNeighborPort.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldStatsPortNeighborPort.setDescription('The port number of the adjacent switch.')
hpicfUdldStatsPortTotalTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUdldStatsPortTotalTx.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldStatsPortTotalTx.setDescription('The number of UDLD control packets sent from this port.')
hpicfUdldStatsPortTotalRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUdldStatsPortTotalRx.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldStatsPortTotalRx.setDescription('The number of UDLD control packets received on this port.')
hpicfUdldStatsPortNumStateChange = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUdldStatsPortNumStateChange.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldStatsPortNumStateChange.setDescription('The number of state transitions.')
hpicfUdldStatsPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUdldStatsPortStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldStatsPortStatus.setDescription('The value of this object indicates whether the port is blocked by UDLD or not.')
hpicfUdldStatsClearAll = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUdldStatsClearAll.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldStatsClearAll.setDescription('When the value of this object is set to TRUE, the UDLD transmit, receive and state change statistics are cleared. A get request for this object always returns FALSE.')
hpicfUdldNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 0, 0))
hpicfUdldLinkfault = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 0, 0, 1)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfUdldLinkfault.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldLinkfault.setDescription('This notification is generated when the link failure occurs.')
hpicfUdldLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 0, 0, 2)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfUdldLinkUp.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldLinkUp.setDescription('This notification is generated when UDLD link goes from down to up.')
hpicfUdldCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 1))
hpicfUdldGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 2))
hpicfUdldCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 1, 1)).setObjects(("HP-ICF-UDLD-MIB", "hpicfUdldPortConfigGroup"), ("HP-ICF-UDLD-MIB", "hpicfUdldPortStatsGroup"), ("HP-ICF-UDLD-MIB", "hpicfUdldNotificationGroup"), ("HP-ICF-UDLD-MIB", "hpicfUdldNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUdldCompliance = hpicfUdldCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfUdldCompliance.setDescription('The compliance statement for SNMP entities which implement the UDLD MIB.')
hpicfUdldCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 1, 2)).setObjects(("HP-ICF-UDLD-MIB", "hpicfUdldStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUdldCompliance2 = hpicfUdldCompliance2.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldCompliance2.setDescription('The compliance statement for SNMP entities that implement the UDLD MIB.')
hpicfUdldCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 1, 3)).setObjects(("HP-ICF-UDLD-MIB", "hpicfUdldPortConfigGroup1"), ("HP-ICF-UDLD-MIB", "hpicfUdldPortStatsGroup"), ("HP-ICF-UDLD-MIB", "hpicfUdldNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUdldCompliance3 = hpicfUdldCompliance3.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldCompliance3.setDescription('The compliance statement for SNMP entities that implement the UDLD MIB.')
hpicfUdldPortConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 2, 1)).setObjects(("HP-ICF-UDLD-MIB", "hpicfUdldConfigTimeInterval"), ("HP-ICF-UDLD-MIB", "hpicfUdldConfigMaxRetries"), ("HP-ICF-UDLD-MIB", "hpicfUdldPortAdminStatus"), ("HP-ICF-UDLD-MIB", "hpicfUdldPortVlanId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUdldPortConfigGroup = hpicfUdldPortConfigGroup.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfUdldPortConfigGroup.setDescription('The collection of objects which are used to configure the UDLD implementation behavior. This group is mandatory for ports which implement the UDLD.')
hpicfUdldPortStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 2, 2)).setObjects(("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortCurrentState"), ("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortNeighborMAC"), ("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortNeighborPort"), ("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortTotalTx"), ("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortTotalRx"), ("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortNumStateChange"), ("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUdldPortStatsGroup = hpicfUdldPortStatsGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldPortStatsGroup.setDescription('The collection of objects which are used to represent UDLD statistics. This group is mandatory for ports which implement the UDLD.')
hpicfUdldNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 2, 3)).setObjects(("HP-ICF-UDLD-MIB", "hpicfUdldLinkfault"), ("HP-ICF-UDLD-MIB", "hpicfUdldLinkUp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUdldNotificationGroup = hpicfUdldNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldNotificationGroup.setDescription('Notification used for signaling change in Link state.')
hpicfUdldStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 2, 4)).setObjects(("HP-ICF-UDLD-MIB", "hpicfUdldStatsClearAll"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUdldStatsGroup = hpicfUdldStatsGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldStatsGroup.setDescription('The collection of objects that are used to perform operations on UDLD related statistics.')
hpicfUdldPortConfigGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 2, 5)).setObjects(("HP-ICF-UDLD-MIB", "hpicfUdldConfigTimeInterval"), ("HP-ICF-UDLD-MIB", "hpicfUdldConfigMaxRetries"), ("HP-ICF-UDLD-MIB", "hpicfUdldPortAdminStatus"), ("HP-ICF-UDLD-MIB", "hpicfUdldPortVlanId"), ("HP-ICF-UDLD-MIB", "hpicfUdldConfigForwardMode"), ("HP-ICF-UDLD-MIB", "hpicfUdldConfigTimeIntervalMs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUdldPortConfigGroup1 = hpicfUdldPortConfigGroup1.setStatus('current')
if mibBuilder.loadTexts: hpicfUdldPortConfigGroup1.setDescription('The collection of objects which are used to configure the UDLD implementation behavior. This group is mandatory for ports which implement the UDLD.')
mibBuilder.exportSymbols("HP-ICF-UDLD-MIB", hpicfUdldLinkfault=hpicfUdldLinkfault, hpicfUdldGroups=hpicfUdldGroups, hpicfUdldCompliance3=hpicfUdldCompliance3, hpicfUdldConfigMaxRetries=hpicfUdldConfigMaxRetries, hpicfUdldNotificationGroup=hpicfUdldNotificationGroup, hpicfUdldConfig=hpicfUdldConfig, hpicfUdldNotificationPrefix=hpicfUdldNotificationPrefix, hpicfUdldPortConfigTable=hpicfUdldPortConfigTable, hpicfUdldConformance=hpicfUdldConformance, hpicfUdldPortConfigGroup=hpicfUdldPortConfigGroup, hpicfUdldStatsGroup=hpicfUdldStatsGroup, hpicfUdldConfigTimeInterval=hpicfUdldConfigTimeInterval, hpicfUdldLinkUp=hpicfUdldLinkUp, hpicfUdldPortStatsEntry=hpicfUdldPortStatsEntry, hpicfUdldPortAdminStatus=hpicfUdldPortAdminStatus, hpicfUdldStatsPortNeighborMAC=hpicfUdldStatsPortNeighborMAC, hpicfUdldPortStatsGroup=hpicfUdldPortStatsGroup, hpicfUdldStatsClearAll=hpicfUdldStatsClearAll, hpicfUdldPortStatsTable=hpicfUdldPortStatsTable, hpicfUdldConfigForwardMode=hpicfUdldConfigForwardMode, hpicfUdldCompliance2=hpicfUdldCompliance2, hpicfUdldStats=hpicfUdldStats, hpicfUdldPortConfigEntry=hpicfUdldPortConfigEntry, hpicfUdldStatsPortNumStateChange=hpicfUdldStatsPortNumStateChange, hpicfUdldConfigTimeIntervalMs=hpicfUdldConfigTimeIntervalMs, hpicfUdldCompliance=hpicfUdldCompliance, PYSNMP_MODULE_ID=hpicfUdldMIB, hpicfUdldObjects=hpicfUdldObjects, hpicfUdldStatsPortCurrentState=hpicfUdldStatsPortCurrentState, hpicfUdldStatsPortStatus=hpicfUdldStatsPortStatus, hpicfUdldCompliances=hpicfUdldCompliances, hpicfUdldStatsPortTotalTx=hpicfUdldStatsPortTotalTx, hpicfUdldPortConfigGroup1=hpicfUdldPortConfigGroup1, hpicfUdldNotifications=hpicfUdldNotifications, hpicfUdldMIB=hpicfUdldMIB, hpicfUdldStatsPortTotalRx=hpicfUdldStatsPortTotalRx, hpicfUdldPortVlanId=hpicfUdldPortVlanId, hpicfUdldStatsPortNeighborPort=hpicfUdldStatsPortNeighborPort)