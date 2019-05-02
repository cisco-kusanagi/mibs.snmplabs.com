#
# PySNMP MIB module BAY-STACK-SOURCE-GUARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAY-STACK-SOURCE-GUARD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:36:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, TimeTicks, ModuleIdentity, IpAddress, iso, Counter64, Integer32, NotificationType, Bits, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "ModuleIdentity", "IpAddress", "iso", "Counter64", "Integer32", "NotificationType", "Bits", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackSourceGuardMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 20))
bayStackSourceGuardMib.setRevisions(('2008-10-30 00:00', '2008-03-31 00:00', '2007-05-07 00:00', '2007-03-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bayStackSourceGuardMib.setRevisionsDescriptions(('Ver 4: Added new notification types.', 'Ver 3: Added statistics table.', 'Ver 2: Fixed some DESCRIPTION clauses.', 'Ver 1: Initial version.',))
if mibBuilder.loadTexts: bayStackSourceGuardMib.setLastUpdated('200810300000Z')
if mibBuilder.loadTexts: bayStackSourceGuardMib.setOrganization('Nortel Ltd.')
if mibBuilder.loadTexts: bayStackSourceGuardMib.setContactInfo('nortel.com')
if mibBuilder.loadTexts: bayStackSourceGuardMib.setDescription("This MIB module is used for IP Source Guard settings in Nortel's software and products.")
bsSourceGuardNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 20, 0))
bsSourceGuardObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 20, 1))
bsSourceGuardConfigTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 1), )
if mibBuilder.loadTexts: bsSourceGuardConfigTable.setStatus('current')
if mibBuilder.loadTexts: bsSourceGuardConfigTable.setDescription('This table is used to configure IP Source Guard per port.')
bsSourceGuardConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 1, 1), ).setIndexNames((0, "BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardConfigIfIndex"))
if mibBuilder.loadTexts: bsSourceGuardConfigEntry.setStatus('current')
if mibBuilder.loadTexts: bsSourceGuardConfigEntry.setDescription('An entry containing objects for configuring IP Source Guard settings for a port.')
bsSourceGuardConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: bsSourceGuardConfigIfIndex.setStatus('current')
if mibBuilder.loadTexts: bsSourceGuardConfigIfIndex.setDescription('The interface on which Source Guard configuration setting apply.')
bsSourceGuardConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("ip", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsSourceGuardConfigMode.setStatus('current')
if mibBuilder.loadTexts: bsSourceGuardConfigMode.setDescription('This object is used to control the Source Guard mode on an interface. The values are as follows: disabled(1) - Source Guard is disabled on this interface. ip(2) - Source Guard only allows traffic from a list of IP addresses on this interface.')
bsSourceGuardAddrTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2), )
if mibBuilder.loadTexts: bsSourceGuardAddrTable.setStatus('current')
if mibBuilder.loadTexts: bsSourceGuardAddrTable.setDescription('This table contains a list of internet and/or MAC addresses allowed by Source Guard on an interface. An entry in this table must indicate either a valid internet address and/or a valid MAC address. This means that an entry may not exist where the value of bsSourceGuardAddrType is unknown(0) and the value of bsSourceGuardAddrMACAddr is 00:00:00:00:00:00. If an entry indicates only an internet address, Source Guard will allow that address regardless of MAC address. Note that currently, MAC addresses are not supported. This means that currently, the value of bsSourceGuardAddrMACAddr must always by 00:00:00:00:00:00, and the value of bsSourceGuardAddrType must not be unknown(0).')
bsSourceGuardAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2, 1), ).setIndexNames((0, "BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardAddrIndex"), (0, "BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardAddrType"), (0, "BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardAddrAddress"), (0, "BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardAddrMACAddr"))
if mibBuilder.loadTexts: bsSourceGuardAddrEntry.setStatus('current')
if mibBuilder.loadTexts: bsSourceGuardAddrEntry.setDescription('An entry containing an address allowed by Source Guard on an interface.')
bsSourceGuardAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: bsSourceGuardAddrIndex.setStatus('current')
if mibBuilder.loadTexts: bsSourceGuardAddrIndex.setDescription('The ifIndex value of the interface.')
bsSourceGuardAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2, 1, 2), InetAddressType())
if mibBuilder.loadTexts: bsSourceGuardAddrType.setStatus('current')
if mibBuilder.loadTexts: bsSourceGuardAddrType.setDescription('The type of internet address contained in the corresponding instance of bsSourceGuardAddrAddress. If the value of this object is other(0), then the corresponding instance of bsSourceGuardAddrAddress must be a zero length value.')
bsSourceGuardAddrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2, 1, 3), InetAddress())
if mibBuilder.loadTexts: bsSourceGuardAddrAddress.setStatus('current')
if mibBuilder.loadTexts: bsSourceGuardAddrAddress.setDescription('The internet address allowed by Source Guard on this interface. If this object contains a zero length value, then the Source Guard feature will not use the value.')
bsSourceGuardAddrMACAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2, 1, 4), MacAddress())
if mibBuilder.loadTexts: bsSourceGuardAddrMACAddr.setStatus('current')
if mibBuilder.loadTexts: bsSourceGuardAddrMACAddr.setDescription('The ethernet MAC address allowed by Source Guard on this interface. If this object contains the value 00:00:00:00:00:00, then the Source Guard feature will not use the value.')
bsSourceGuardAddrSource = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("dhcpSnooping", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsSourceGuardAddrSource.setStatus('current')
if mibBuilder.loadTexts: bsSourceGuardAddrSource.setDescription('The source of the address(es). Currently, the only source is from dhcp snooping. In the future, static addresses will be allowed.')
bsSourceGuardStatsTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 3), )
if mibBuilder.loadTexts: bsSourceGuardStatsTable.setStatus('current')
if mibBuilder.loadTexts: bsSourceGuardStatsTable.setDescription('Per-interface IP Source Guard statistics.')
bsSourceGuardStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 3, 1), ).setIndexNames((0, "BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardStatsIfIndex"))
if mibBuilder.loadTexts: bsSourceGuardStatsEntry.setStatus('current')
if mibBuilder.loadTexts: bsSourceGuardStatsEntry.setDescription('An entry containing Source Guard statistics for an interface.')
bsSourceGuardStatsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: bsSourceGuardStatsIfIndex.setStatus('current')
if mibBuilder.loadTexts: bsSourceGuardStatsIfIndex.setDescription('The ifIndex value of the interface.')
bsSourceGuardStatsDroppedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsSourceGuardStatsDroppedPackets.setStatus('current')
if mibBuilder.loadTexts: bsSourceGuardStatsDroppedPackets.setDescription('The number of received packets on this interface that were dropped due to IP source guard filtering.')
bsSourceGuardReachedMaxIpEntries = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 20, 0, 1)).setObjects(("BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardConfigMode"))
if mibBuilder.loadTexts: bsSourceGuardReachedMaxIpEntries.setStatus('current')
if mibBuilder.loadTexts: bsSourceGuardReachedMaxIpEntries.setDescription('This notification is generated when the maximum number of IP entries on a port has been reached. The port is identified by the instance of bssourceGuardConfigMode included in the notification.')
bsSourceGuardCannotEnablePort = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 20, 0, 2)).setObjects(("BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardConfigMode"))
if mibBuilder.loadTexts: bsSourceGuardCannotEnablePort.setStatus('current')
if mibBuilder.loadTexts: bsSourceGuardCannotEnablePort.setDescription('This notification is generated when there are insufficient resources available to enable IP source guard checking on a port. Note that this notification will *not* be generated as the result of a management operation, but rather only as a result of internal state changes within the system (for example, system initialization). The port for which the notification is generated is identified by the instance of bsSourceGuardConfigMode included in the notification.')
mibBuilder.exportSymbols("BAY-STACK-SOURCE-GUARD-MIB", bsSourceGuardAddrEntry=bsSourceGuardAddrEntry, bsSourceGuardObjects=bsSourceGuardObjects, bsSourceGuardAddrIndex=bsSourceGuardAddrIndex, bsSourceGuardReachedMaxIpEntries=bsSourceGuardReachedMaxIpEntries, bsSourceGuardCannotEnablePort=bsSourceGuardCannotEnablePort, bsSourceGuardConfigEntry=bsSourceGuardConfigEntry, bsSourceGuardConfigMode=bsSourceGuardConfigMode, bsSourceGuardNotifications=bsSourceGuardNotifications, bsSourceGuardStatsEntry=bsSourceGuardStatsEntry, bsSourceGuardStatsDroppedPackets=bsSourceGuardStatsDroppedPackets, bsSourceGuardAddrAddress=bsSourceGuardAddrAddress, bsSourceGuardAddrType=bsSourceGuardAddrType, bayStackSourceGuardMib=bayStackSourceGuardMib, bsSourceGuardConfigIfIndex=bsSourceGuardConfigIfIndex, bsSourceGuardAddrSource=bsSourceGuardAddrSource, bsSourceGuardStatsTable=bsSourceGuardStatsTable, bsSourceGuardStatsIfIndex=bsSourceGuardStatsIfIndex, bsSourceGuardAddrTable=bsSourceGuardAddrTable, bsSourceGuardAddrMACAddr=bsSourceGuardAddrMACAddr, PYSNMP_MODULE_ID=bayStackSourceGuardMib, bsSourceGuardConfigTable=bsSourceGuardConfigTable)
