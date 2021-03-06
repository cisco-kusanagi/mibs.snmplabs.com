#
# PySNMP MIB module ZYXEL-VLAN-COUNTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-VLAN-COUNTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:52:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Integer32, MibIdentifier, iso, Gauge32, NotificationType, Counter32, Unsigned32, TimeTicks, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "MibIdentifier", "iso", "Gauge32", "NotificationType", "Counter32", "Unsigned32", "TimeTicks", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelVlanCounter = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87))
if mibBuilder.loadTexts: zyxelVlanCounter.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelVlanCounter.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelVlanCounter.setContactInfo('')
if mibBuilder.loadTexts: zyxelVlanCounter.setDescription('The subtree for VLAN counter')
zyxelVlanCounterSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 1))
zyxelVlanCounterStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2))
zyxelVlanCounterTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 1, 1), )
if mibBuilder.loadTexts: zyxelVlanCounterTable.setStatus('current')
if mibBuilder.loadTexts: zyxelVlanCounterTable.setDescription('Defines the Vlan Counter Table for providing, via SNMP, the capability of performing vlan counting operations at a remote host and having their results of these operations are stored in the table.')
zyxelVlanCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 1, 1, 1), ).setIndexNames((0, "ZYXEL-VLAN-COUNTER-MIB", "zyVlanCounterVid"))
if mibBuilder.loadTexts: zyxelVlanCounterEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelVlanCounterEntry.setDescription('Defines an entry in the zyxelVlanCounterTable.')
zyVlanCounterVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: zyVlanCounterVid.setStatus('current')
if mibBuilder.loadTexts: zyVlanCounterVid.setDescription('VLAN ID where the VLAN counter applies.')
zyVlanCounterTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyVlanCounterTimeout.setStatus('current')
if mibBuilder.loadTexts: zyVlanCounterTimeout.setDescription('Specifies the time-out value, in seconds, for a VLAN counter operation.')
zyVlanCounterPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 1, 1, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyVlanCounterPorts.setStatus('current')
if mibBuilder.loadTexts: zyVlanCounterPorts.setDescription('Specify the port for a VLAN counter operation.')
zyVlanCounterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyVlanCounterRowStatus.setStatus('current')
if mibBuilder.loadTexts: zyVlanCounterRowStatus.setDescription('This object allows to create and delete a VLAN counter entry.')
zyxelVlanCounterInfoTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1), )
if mibBuilder.loadTexts: zyxelVlanCounterInfoTable.setStatus('current')
if mibBuilder.loadTexts: zyxelVlanCounterInfoTable.setDescription('The table that show incoming packet statistics on individual VLAN')
zyxelVlanCounterInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1), ).setIndexNames((0, "ZYXEL-VLAN-COUNTER-MIB", "zyVlanCounterInfoVid"))
if mibBuilder.loadTexts: zyxelVlanCounterInfoEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelVlanCounterInfoEntry.setDescription('Incoming packet statistics information for a particular VLAN.')
zyVlanCounterInfoVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: zyVlanCounterInfoVid.setStatus('current')
if mibBuilder.loadTexts: zyVlanCounterInfoVid.setDescription('VLAN ID where the VLAN counter applies.')
zyVlanCounterInfoHCOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 2), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: zyVlanCounterInfoHCOctets.setStatus('current')
if mibBuilder.loadTexts: zyVlanCounterInfoHCOctets.setDescription('Average receive Octets')
zyVlanCounterInfoHCPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyVlanCounterInfoHCPackets.setStatus('current')
if mibBuilder.loadTexts: zyVlanCounterInfoHCPackets.setDescription('Total received number of good packets flowing trhough this VLAN.')
zyVlanCounterInfoHCMulticastPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyVlanCounterInfoHCMulticastPackets.setStatus('current')
if mibBuilder.loadTexts: zyVlanCounterInfoHCMulticastPackets.setDescription('Total received number of good multicast packets flowing through this VLAN.')
zyVlanCounterInfoHCBroadcastPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyVlanCounterInfoHCBroadcastPackets.setStatus('current')
if mibBuilder.loadTexts: zyVlanCounterInfoHCBroadcastPackets.setDescription('Total received number of good broadcast packets flowing through this VLAN.')
zyVlanCounterInfoHCTaggedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyVlanCounterInfoHCTaggedPackets.setStatus('current')
if mibBuilder.loadTexts: zyVlanCounterInfoHCTaggedPackets.setDescription('Total received number of VLAN-tagged packets flowing through this VLAN.')
zyVlanCounterInfoHCPackets64Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyVlanCounterInfoHCPackets64Octets.setStatus('current')
if mibBuilder.loadTexts: zyVlanCounterInfoHCPackets64Octets.setDescription('Total received number of packets that were 64 octets in length.')
zyVlanCounterInfoHCPackets65to127Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyVlanCounterInfoHCPackets65to127Octets.setStatus('current')
if mibBuilder.loadTexts: zyVlanCounterInfoHCPackets65to127Octets.setDescription('Total received number of packets that were between 65 and 127 octets in length.')
zyVlanCounterInfoHCPackets128to255Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyVlanCounterInfoHCPackets128to255Octets.setStatus('current')
if mibBuilder.loadTexts: zyVlanCounterInfoHCPackets128to255Octets.setDescription('Total received number of packets that were between 128 and 255 octets in length.')
zyVlanCounterInfoHCPackets256to511Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyVlanCounterInfoHCPackets256to511Octets.setStatus('current')
if mibBuilder.loadTexts: zyVlanCounterInfoHCPackets256to511Octets.setDescription('Total received number of packets that were between 256 and 511 octets in length.')
zyVlanCounterInfoHCPackets512to1023Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyVlanCounterInfoHCPackets512to1023Octets.setStatus('current')
if mibBuilder.loadTexts: zyVlanCounterInfoHCPackets512to1023Octets.setDescription('Total received number of packets that were between 512 and 1023 octets in length ')
zyVlanCounterInfoHCPackets1024to1518Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyVlanCounterInfoHCPackets1024to1518Octets.setStatus('current')
if mibBuilder.loadTexts: zyVlanCounterInfoHCPackets1024to1518Octets.setDescription('Total received number of packets that were between 1024 and 1518 octets in length ')
zyVlanCounterInfoHCOversizePackets = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 87, 2, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyVlanCounterInfoHCOversizePackets.setStatus('current')
if mibBuilder.loadTexts: zyVlanCounterInfoHCOversizePackets.setDescription('Total received number of packets that were between 1519 octets and the maximun frame size. The maximun frame size varies depending on your switch model')
mibBuilder.exportSymbols("ZYXEL-VLAN-COUNTER-MIB", zyVlanCounterTimeout=zyVlanCounterTimeout, zyVlanCounterInfoHCPackets64Octets=zyVlanCounterInfoHCPackets64Octets, zyVlanCounterInfoHCPackets512to1023Octets=zyVlanCounterInfoHCPackets512to1023Octets, zyxelVlanCounterTable=zyxelVlanCounterTable, zyVlanCounterInfoHCPackets1024to1518Octets=zyVlanCounterInfoHCPackets1024to1518Octets, zyVlanCounterVid=zyVlanCounterVid, zyVlanCounterInfoHCBroadcastPackets=zyVlanCounterInfoHCBroadcastPackets, zyVlanCounterInfoHCTaggedPackets=zyVlanCounterInfoHCTaggedPackets, zyVlanCounterInfoHCOversizePackets=zyVlanCounterInfoHCOversizePackets, zyxelVlanCounterEntry=zyxelVlanCounterEntry, zyVlanCounterInfoHCPackets=zyVlanCounterInfoHCPackets, zyVlanCounterInfoHCOctets=zyVlanCounterInfoHCOctets, PYSNMP_MODULE_ID=zyxelVlanCounter, zyVlanCounterInfoHCPackets256to511Octets=zyVlanCounterInfoHCPackets256to511Octets, zyVlanCounterRowStatus=zyVlanCounterRowStatus, zyxelVlanCounterInfoEntry=zyxelVlanCounterInfoEntry, zyVlanCounterInfoHCPackets65to127Octets=zyVlanCounterInfoHCPackets65to127Octets, zyVlanCounterInfoHCPackets128to255Octets=zyVlanCounterInfoHCPackets128to255Octets, zyxelVlanCounterInfoTable=zyxelVlanCounterInfoTable, zyxelVlanCounterStatus=zyxelVlanCounterStatus, zyVlanCounterPorts=zyVlanCounterPorts, zyVlanCounterInfoVid=zyVlanCounterInfoVid, zyxelVlanCounterSetup=zyxelVlanCounterSetup, zyxelVlanCounter=zyxelVlanCounter, zyVlanCounterInfoHCMulticastPackets=zyVlanCounterInfoHCMulticastPackets)
