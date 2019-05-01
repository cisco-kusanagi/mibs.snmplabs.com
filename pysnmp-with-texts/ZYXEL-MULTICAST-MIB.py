#
# PySNMP MIB module ZYXEL-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-MULTICAST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:50:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, Counter32, NotificationType, IpAddress, ModuleIdentity, Unsigned32, Bits, MibIdentifier, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "Counter32", "NotificationType", "IpAddress", "ModuleIdentity", "Unsigned32", "Bits", "MibIdentifier", "iso", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelMulticast = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54))
if mibBuilder.loadTexts: zyxelMulticast.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelMulticast.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelMulticast.setContactInfo('')
if mibBuilder.loadTexts: zyxelMulticast.setDescription('The subtree for multicast')
zyxelMulticastSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1))
zyMulticastUnknownMulticastFrameForwarding = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("flooding", 1), ("drop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMulticastUnknownMulticastFrameForwarding.setStatus('current')
if mibBuilder.loadTexts: zyMulticastUnknownMulticastFrameForwarding.setDescription('Specify the action to perform when the switch receives an unknown multicast frame. Unknown multicast frames are addressed to multicast groups for which the Switch has not recorded any group members. Select Drop to discard the frame(s). Select Flooding to send the frame(s) to all ports of the same domain.')
zyMulticastReservedMulticastFrameForwarding = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("flooding", 1), ("drop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMulticastReservedMulticastFrameForwarding.setStatus('current')
if mibBuilder.loadTexts: zyMulticastReservedMulticastFrameForwarding.setDescription('The IP address range of 224.0.0.0 to 224.0.0.255 are reserved for multicasting on the local network only. For example, 224.0.0.1 is for all hosts on a local network segment and 224.0.0.9 is used to send RIP routing information to all RIP v2 routers on the same network segment. A multicast router will not forward a packet with the destination IP address within this range to other networks. See the IANA web site for more information. The layer-2 multicast MAC addresses are also included in this group. Specify the action to perform when the Switch receives a frame with a reserved multicast address. Select Drop to discard the frame(s). Select Flooding to send the frame(s) to all ports of the same domain. ')
mibBuilder.exportSymbols("ZYXEL-MULTICAST-MIB", zyMulticastReservedMulticastFrameForwarding=zyMulticastReservedMulticastFrameForwarding, PYSNMP_MODULE_ID=zyxelMulticast, zyMulticastUnknownMulticastFrameForwarding=zyMulticastUnknownMulticastFrameForwarding, zyxelMulticastSetup=zyxelMulticastSetup, zyxelMulticast=zyxelMulticast)
