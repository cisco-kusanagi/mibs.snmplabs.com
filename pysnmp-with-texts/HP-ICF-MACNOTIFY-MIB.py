#
# PySNMP MIB module HP-ICF-MACNOTIFY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-MACNOTIFY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:34:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
VlanId, PortList = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId", "PortList")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, IpAddress, Integer32, Bits, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Counter32, Counter64, MibIdentifier, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "Integer32", "Bits", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Counter32", "Counter64", "MibIdentifier", "Unsigned32", "ObjectIdentity")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
hpicfMacNotifyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66))
hpicfMacNotifyMIB.setRevisions(('2013-07-18 00:00', '2011-07-21 00:00', '2010-02-08 00:00', '2009-12-11 10:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfMacNotifyMIB.setRevisionsDescriptions(('Added of hpicfMacNotifyAgedPortConfig, hpicfMacNotifyAgedCount, hpicfMacNotifyCompliance2, hpicfMacNotifyStatsGroup2 and hpicfMacNotifyConfigGroup2 objects for mac aged notifications feature', 'Additions for mac count notifications feature', 'Additions for the Clear portion of feature', 'The initial revision.',))
if mibBuilder.loadTexts: hpicfMacNotifyMIB.setLastUpdated('201307180000Z')
if mibBuilder.loadTexts: hpicfMacNotifyMIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfMacNotifyMIB.setContactInfo('Hewlett Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfMacNotifyMIB.setDescription('The MIB module for managing MAC address notifications.')
hpicfMacCountNotifyConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5))
hpicfMacNotifyClearObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 4))
hpicfMacNotifyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3))
hpicfMacNotifyStats = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 2))
hpicfMacNotifyConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1))
hpicfMacNotifyNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 0))
hpicfMacNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyEnable.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyEnable.setDescription('Indicates whether the SNMP entity is permitted to generate learned, moved or removed hpicfMacNotifyMacAddressTableChange trap notifications. Default is disabled.')
hpicfMacNotifyTrapInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 2), Unsigned32().clone(30)).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyTrapInterval.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyTrapInterval.setDescription('Defines the interval in seconds between sending hpicfMacNotifyMacAddressTableChange notifications. The notifications will be buffered on the system until the interval. If the buffer becomes full before the interval, the full buffer will be sent. A value of 0 (zero) indicates MAC address changes will be sent when the event occurs. Default value is 30 seconds.')
hpicfMacNotifyMoveEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyMoveEnable.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyMoveEnable.setDescription('Indicates whether the SNMP entity is permitted to generate hpicfMacNotifyMacAddressTableChange for MAC address moves on the system. Notifications are generated when a MAC address is moved from one port to another port on the system. hpicfMacNotifyEnable must be enabled. Default is disable.')
hpicfMacNotifyLearnedPortConfig = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 4), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyLearnedPortConfig.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyLearnedPortConfig.setDescription("Used to configure the MAC address learned notification traps on specific ports. Each octet within this value specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus, each port is represented by a single bit within the value of this object. If that bit has a value of '1' then that port is enabled to send traps for learned MAC addresses; the port is not enabled if its bit has a value of '0'. Enabling hpicfMacNotifyLearnedPortConfig on a trunk port is permitted but not recommended. hpicfMacNotifyEnable must be enabled for traps to be sent.")
hpicfMacNotifyRemovedPortConfig = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 5), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyRemovedPortConfig.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyRemovedPortConfig.setDescription("Used to configure the MAC address removed notification traps on specific ports. Each octet within this value specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus, each port is represented by a single bit within the value of this object. If that bit has a value of '1' then that port is enabled to send traps for removed MAC addresses; the port is not enabled if its bit has a value of '0'. Enabling hpicfMacNotifyRemovedPortConfig on a trunk port is permitted but not recommended. hpicfMacNotifyEnable must be enabled for traps to be sent.")
hpicfMacNotifyAction = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("learned", 1), ("moved", 2), ("removed", 3), ("aged", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfMacNotifyAction.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyAction.setDescription('Indicate the MAC address table change action for hpicfMacNotifyMacAddress: learned, moved, removed or aged.')
hpicfMacNotifyMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 7), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfMacNotifyMacAddress.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyMacAddress.setDescription('The MAC address that has been learned, moved, removed or aged in the MAC address table.')
hpicfMacNotifyFromPortId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 8), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfMacNotifyFromPortId.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyFromPortId.setDescription('The related from port index of the MAC address hpicfMacNotifyMacAddress. Port index will be determined by the action in hpicfMacNotifyAction. Action: Learned: The value will be zero Moved: The port from which the MAC was moved Removed: The port from which MAC was removed Aged: The port on which the MAC has aged')
hpicfMacNotifyToPortId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 9), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfMacNotifyToPortId.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyToPortId.setDescription('The related port index of the MAC address hpicfMacNotifyMacAddress. Port index will be determined by the action in hpicfMacNotifyAction. Action: Learned: The actual port the MAC was learned Moved: The port to which the MAC was moved Removed: The value will be zero Aged: The value will be zero ')
hpicfMacNotifyVlanId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 10), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfMacNotifyVlanId.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyVlanId.setDescription('The related Vlan ID of the MAC address hpicfMacNotifyMacAddress. Vlan ID will be determined by the action in hpicfMacNotifyAction. Action: Learned: VLAN that the hpicfMacNotifyToPortId belongs to Moved: VLAN that the hpicfMacNotifyToPortId belongs to Removed: VLAN that hpicfMacNotifyFromPortId belongs to Aged: VLAN that hpicfMacNotifyFromPortId belongs to')
hpicfMacNotifyAgedPortConfig = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 1, 11), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyAgedPortConfig.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyAgedPortConfig.setDescription('This object is used to configure the ports for sending traps when MAC addresses age out. Each octet within this value specifies a set of eight ports.The first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16 and so on . Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. A bitvalue of (1) indicates that the corresponding port is enabled to send traps for aged MAC addresses. A bitvalue of (0) indicates that the corresponding port is not enabled to send traps for aged MAC addresses. Enabling hpicfMacNotifyAgedPortConfig on a trunk port is permitted but not recommended. hpicfMacNotifyEnable must be enabled for traps to be sent.')
hpicfMacNotifyPortLearnedCountEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyPortLearnedCountEnable.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyPortLearnedCountEnable.setDescription('Indicates whether or not to generate hpicfMacNotifyPortMacAddressCount trap. Notifications are generated when the MAC address count on a switch port equals the defined MAC count as in hpicfMacNotifyPortLearnedCount object. Default is disabled.')
hpicfMacNotifyPortLearnedCountConfig = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyPortLearnedCountConfig.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyPortLearnedCountConfig.setDescription("Used to config the MAC address learned notification traps on specific ports. Each octet within this value specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus, each port is represented by a single bit within the value of this object. If that bit has a value of '1' then that port is enabled to send traps for learned MAC addresses;the port is not enabled if its bit has a value of '0'. Enabling picfMacNotifyPortLearnedCountConfig on a trunk port is permitted but not recommended. hpicfMacNotifyPortLearnedCountEnable must be enabled for traps to be sent.")
hpicfMacNotifyPortLearnedCountConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5, 3), )
if mibBuilder.loadTexts: hpicfMacNotifyPortLearnedCountConfigTable.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyPortLearnedCountConfigTable.setDescription('Table containing the configured MAC count for sending mac-count-notify traps on a port.')
hpicfMacNotifyPortLearnedCountConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5, 3, 1), ).setIndexNames((0, "HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyPortIndex"))
if mibBuilder.loadTexts: hpicfMacNotifyPortLearnedCountConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyPortLearnedCountConfigEntry.setDescription('An entry in hpicfMacNotifyPortLearnedCountConfigTable containing MAC count for sending mac-count-notify traps for a port.')
hpicfMacNotifyPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hpicfMacNotifyPortIndex.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyPortIndex.setDescription('Indicates the ifIndex of the port')
hpicfMacNotifyPortLearnedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 5, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)).clone(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyPortLearnedCount.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyPortLearnedCount.setDescription('Indicates the count of MAC learns when reached to send the mac-notify traps')
hpicfMacNotifyLearnedCount = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfMacNotifyLearnedCount.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyLearnedCount.setDescription('A count of MAC addresses learned by the MAC Address Table. ')
hpicfMacNotifyRemovedCount = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfMacNotifyRemovedCount.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyRemovedCount.setDescription('A count of MAC addresses removed from the MAC Address Table. ')
hpicfMacNotifyMoveCount = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfMacNotifyMoveCount.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyMoveCount.setDescription(' A count of MAC addresses moved in the MAC Address Table.')
hpicfMacNotifyCount = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfMacNotifyCount.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyCount.setDescription('A count of Mac Address notifications sent. hpicfMacNotifyEnable must be enabled for the counter to be activated. This number is incremented each time a Mac Address Table Change learn/move/remove occurs on a hpicfMacNotifyTrapConfig enabled interface or when hpicfMacNotifyMoveEnable is enabled. This count will include notifications that are dropped due to buffering overflow during high activity. hpicfMacNotifyCount is initialized to zero at boot.')
hpicfMacNotifyAgedCount = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfMacNotifyAgedCount.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyAgedCount.setDescription('A count of MAC addresses agedout from the MAC Address Table. ')
hpicfMacNotifyMacAddressTableChange = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 0, 1)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyAction"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMacAddress"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyFromPortId"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyToPortId"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyVlanId"))
if mibBuilder.loadTexts: hpicfMacNotifyMacAddressTableChange.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyMacAddressTableChange.setDescription('The hpicfMacNotifyMacAddressTableChange notification signifies that hpicfMacNotifyEnable is enabled and either a MAC address table change learn / remove / age occurred on a configured hpicfMacNotifyTrapConfig interface or hpicfMacNotifyMoveEnable is enabled and a MAC address has been moved. Notifications will buffered on the system to be sent on hpicfMacNotifyTrapInterval. During high system activity, notification may be sent before the interval and in some cases, notifications will be dropped. The system will log dropped notification events')
hpicfMacNotifyPortMacAddressCount = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 0, 2)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyToPortId"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyVlanId"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyPortLearnedCount"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMacAddress"))
if mibBuilder.loadTexts: hpicfMacNotifyPortMacAddressCount.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyPortMacAddressCount.setDescription('The hpicfMacNotifyPortMacAddressCount notification signifies that hpicfMacNotifyPortLearnedCountEnable is enabled and the number of MAC address learn has reached the configured MAC count on switch port. The hpicfMacNotifyMacAddress specifies the exceeded MAC learn address.')
hpicfMacNotifyClearMacTableOnPorts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 4, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyClearMacTableOnPorts.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyClearMacTableOnPorts.setDescription("Used to clear the MAC address table on a specific port. Each octet within this value specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus, each port is represented by a single bit within the value of this object. If that bit has a value of '1 then that port is included in the set of ports; the port is not included if its bit has a value of '0'.")
hpicfMacNotifyClearMacTableOnVlan = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 4, 2), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyClearMacTableOnVlan.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyClearMacTableOnVlan.setDescription('Used to clear the MAC address table on a specific VLAN. VLAN ID identifies the VLAN that will be cleared.')
hpicfMacNotifyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 1))
hpicfMacNotifyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2))
hpicfMacNotifyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 1, 1)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyGlobalConfigGroup"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyConfigGroup"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyStatsGroup"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyNotifications"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyClearGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacNotifyCompliance = hpicfMacNotifyCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfMacNotifyCompliance.setDescription('The compliance statement for SNMP entities which implement the MAC Notify MIB.')
hpicfMacCountNotifyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 1, 2)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacCountNotifyConfigGroup"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacCountNotifyNotifications"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacCountNotifyCompliance = hpicfMacCountNotifyCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfMacCountNotifyCompliance.setDescription('The compliance steatement for SNMP entities which implement the mac count notify mib objects.')
hpicfMacNotifyCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 1, 3)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyGlobalConfigGroup"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyConfigGroup2"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyStatsGroup2"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyNotifications"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyClearGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacNotifyCompliance2 = hpicfMacNotifyCompliance2.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyCompliance2.setDescription('The compliance statement for SNMP entities which implement the MAC Notify MIB.')
hpicfMacNotifyGlobalConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 1)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyEnable"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyTrapInterval"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMoveEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacNotifyGlobalConfigGroup = hpicfMacNotifyGlobalConfigGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyGlobalConfigGroup.setDescription(' A collection of objects used to globally configure the SNMP traps used to monitor the MAC address table using the MAC-notify feature')
hpicfMacNotifyConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 2)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyEnable"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyTrapInterval"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMoveEnable"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyLearnedPortConfig"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyRemovedPortConfig"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyAction"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMacAddress"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyFromPortId"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyToPortId"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyVlanId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacNotifyConfigGroup = hpicfMacNotifyConfigGroup.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfMacNotifyConfigGroup.setDescription('A collection of objects used to configure and to monitor, through SNMP traps, for the MAC address table changes (learns/removes).')
hpicfMacNotifyStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 3)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyLearnedCount"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyRemovedCount"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMoveCount"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacNotifyStatsGroup = hpicfMacNotifyStatsGroup.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfMacNotifyStatsGroup.setDescription('A group of counters used to maintain statistics on the number of MAC address table changes and the number of notification packets sent for changes in the MAC address table.')
hpicfMacNotifyNotifications = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 4)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMacAddressTableChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacNotifyNotifications = hpicfMacNotifyNotifications.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyNotifications.setDescription('A group of notifications used to signal changes (learns/moves/removes) in the MAC address table.')
hpicfMacNotifyClearGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 5)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyClearMacTableOnPorts"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyClearMacTableOnVlan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacNotifyClearGroup = hpicfMacNotifyClearGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyClearGroup.setDescription(' A collection of objects used to clear the MAC address tables')
hpicfMacCountNotifyConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 6)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyPortLearnedCountEnable"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyPortLearnedCountConfig"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyPortLearnedCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacCountNotifyConfigGroup = hpicfMacCountNotifyConfigGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfMacCountNotifyConfigGroup.setDescription('A collection of objects used to configure and to montior, through SNMP traps, for the MAC address learn count on the ports.')
hpicfMacCountNotifyNotifications = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 7)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyPortMacAddressCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacCountNotifyNotifications = hpicfMacCountNotifyNotifications.setStatus('current')
if mibBuilder.loadTexts: hpicfMacCountNotifyNotifications.setDescription('A group of notifications used to signal MAC address learn count on a port.')
hpicfMacNotifyStatsGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 8)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyLearnedCount"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyRemovedCount"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMoveCount"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyCount"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyAgedCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacNotifyStatsGroup2 = hpicfMacNotifyStatsGroup2.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyStatsGroup2.setDescription('A collection of counters used to maintain the statistics of MAC address table changes and the notifications sent for each instance of MAC address table change.')
hpicfMacNotifyConfigGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66, 3, 2, 9)).setObjects(("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyEnable"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyTrapInterval"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMoveEnable"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyLearnedPortConfig"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyRemovedPortConfig"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyAction"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyMacAddress"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyFromPortId"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyToPortId"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyVlanId"), ("HP-ICF-MACNOTIFY-MIB", "hpicfMacNotifyAgedPortConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfMacNotifyConfigGroup2 = hpicfMacNotifyConfigGroup2.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyConfigGroup2.setDescription('A collection of objects used to configure and monitor the SNMP traps for the MAC address table changes .')
mibBuilder.exportSymbols("HP-ICF-MACNOTIFY-MIB", hpicfMacNotifyRemovedPortConfig=hpicfMacNotifyRemovedPortConfig, hpicfMacCountNotifyNotifications=hpicfMacCountNotifyNotifications, hpicfMacNotifyTrapInterval=hpicfMacNotifyTrapInterval, hpicfMacNotifyPortLearnedCountEnable=hpicfMacNotifyPortLearnedCountEnable, hpicfMacNotifyClearGroup=hpicfMacNotifyClearGroup, hpicfMacNotifyGlobalConfigGroup=hpicfMacNotifyGlobalConfigGroup, hpicfMacNotifyAgedCount=hpicfMacNotifyAgedCount, PYSNMP_MODULE_ID=hpicfMacNotifyMIB, hpicfMacNotifyConfigObjects=hpicfMacNotifyConfigObjects, hpicfMacNotifyAgedPortConfig=hpicfMacNotifyAgedPortConfig, hpicfMacNotifyNotificationObjects=hpicfMacNotifyNotificationObjects, hpicfMacNotifyPortLearnedCountConfigEntry=hpicfMacNotifyPortLearnedCountConfigEntry, hpicfMacNotifyMIB=hpicfMacNotifyMIB, hpicfMacNotifyPortLearnedCountConfig=hpicfMacNotifyPortLearnedCountConfig, hpicfMacNotifyFromPortId=hpicfMacNotifyFromPortId, hpicfMacNotifyCompliance=hpicfMacNotifyCompliance, hpicfMacNotifyClearMacTableOnPorts=hpicfMacNotifyClearMacTableOnPorts, hpicfMacCountNotifyConfigObjects=hpicfMacCountNotifyConfigObjects, hpicfMacNotifyPortMacAddressCount=hpicfMacNotifyPortMacAddressCount, hpicfMacNotifyMoveEnable=hpicfMacNotifyMoveEnable, hpicfMacNotifyLearnedCount=hpicfMacNotifyLearnedCount, hpicfMacNotifyGroups=hpicfMacNotifyGroups, hpicfMacNotifyStatsGroup2=hpicfMacNotifyStatsGroup2, hpicfMacNotifyStats=hpicfMacNotifyStats, hpicfMacNotifyPortLearnedCountConfigTable=hpicfMacNotifyPortLearnedCountConfigTable, hpicfMacNotifyConformance=hpicfMacNotifyConformance, hpicfMacNotifyEnable=hpicfMacNotifyEnable, hpicfMacNotifyPortLearnedCount=hpicfMacNotifyPortLearnedCount, hpicfMacNotifyCompliances=hpicfMacNotifyCompliances, hpicfMacNotifyConfigGroup=hpicfMacNotifyConfigGroup, hpicfMacNotifyToPortId=hpicfMacNotifyToPortId, hpicfMacNotifyCompliance2=hpicfMacNotifyCompliance2, hpicfMacNotifyAction=hpicfMacNotifyAction, hpicfMacNotifyStatsGroup=hpicfMacNotifyStatsGroup, hpicfMacNotifyVlanId=hpicfMacNotifyVlanId, hpicfMacNotifyLearnedPortConfig=hpicfMacNotifyLearnedPortConfig, hpicfMacNotifyNotifications=hpicfMacNotifyNotifications, hpicfMacNotifyClearObjects=hpicfMacNotifyClearObjects, hpicfMacNotifyCount=hpicfMacNotifyCount, hpicfMacNotifyClearMacTableOnVlan=hpicfMacNotifyClearMacTableOnVlan, hpicfMacNotifyPortIndex=hpicfMacNotifyPortIndex, hpicfMacNotifyRemovedCount=hpicfMacNotifyRemovedCount, hpicfMacCountNotifyCompliance=hpicfMacCountNotifyCompliance, hpicfMacNotifyMoveCount=hpicfMacNotifyMoveCount, hpicfMacNotifyMacAddressTableChange=hpicfMacNotifyMacAddressTableChange, hpicfMacNotifyMacAddress=hpicfMacNotifyMacAddress, hpicfMacCountNotifyConfigGroup=hpicfMacCountNotifyConfigGroup, hpicfMacNotifyConfigGroup2=hpicfMacNotifyConfigGroup2)
