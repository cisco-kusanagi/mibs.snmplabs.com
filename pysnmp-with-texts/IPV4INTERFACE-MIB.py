#
# PySNMP MIB module IPV4INTERFACE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPV4INTERFACE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:56:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
apIpv4Interface, = mibBuilder.importSymbols("APENT-MIB", "apIpv4Interface")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, iso, ModuleIdentity, TimeTicks, NotificationType, Gauge32, Counter32, ObjectIdentity, IpAddress, Unsigned32, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "iso", "ModuleIdentity", "TimeTicks", "NotificationType", "Gauge32", "Counter32", "ObjectIdentity", "IpAddress", "Unsigned32", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "TextualConvention")
apIpv4InterfaceMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 1))
if mibBuilder.loadTexts: apIpv4InterfaceMib.setLastUpdated('9711192000Z')
if mibBuilder.loadTexts: apIpv4InterfaceMib.setOrganization('ArrowPoint Communications Inc.')
if mibBuilder.loadTexts: apIpv4InterfaceMib.setContactInfo('Postal: ArrowPoint Communications Inc. 50 Nagog Park Acton, Massachusetts 01720 Tel: +1 978-206-3000 option 1 E-Mail: support@arrowpoint.com')
if mibBuilder.loadTexts: apIpv4InterfaceMib.setDescription('This MIB module describes the ArrowPoint enterprise MIB support for IPv4 Interfaces')
apIpv4InterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2), )
if mibBuilder.loadTexts: apIpv4InterfaceTable.setStatus('current')
if mibBuilder.loadTexts: apIpv4InterfaceTable.setDescription('A table of IP Interfaces.')
apIpv4InterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1), ).setIndexNames((0, "IPV4INTERFACE-MIB", "apIpv4IfAddress"), (0, "IPV4INTERFACE-MIB", "apIpv4IfCircuitIfIndex"))
if mibBuilder.loadTexts: apIpv4InterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: apIpv4InterfaceEntry.setDescription('ArrowPoint interface table extensions')
apIpv4IfAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4IfAddress.setStatus('current')
if mibBuilder.loadTexts: apIpv4IfAddress.setDescription('The Local Interface IP Address')
apIpv4IfCircuitIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4IfCircuitIfIndex.setStatus('current')
if mibBuilder.loadTexts: apIpv4IfCircuitIfIndex.setDescription('The Circuit ifIndex associated with the local interface')
apIpv4IfNetPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(8, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4IfNetPrefixLen.setStatus('current')
if mibBuilder.loadTexts: apIpv4IfNetPrefixLen.setDescription('The network prefix length associated with this entry')
apIpv4IfDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4IfDisable.setStatus('current')
if mibBuilder.loadTexts: apIpv4IfDisable.setDescription('Used to disable or enable an interface.')
apIpv4IfState = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("disabled", 2), ("noCircuit", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4IfState.setStatus('current')
if mibBuilder.loadTexts: apIpv4IfState.setDescription('Current state of the interface.')
apIpv4IfBroadcastIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4IfBroadcastIpAddress.setStatus('current')
if mibBuilder.loadTexts: apIpv4IfBroadcastIpAddress.setDescription('The broadcast IP Address associated with this entry. If left zero, the all-ones host is used for numbered interfaces. 255.255.255.255 is always used for unnumbered.')
apIpv4IfRedirects = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4IfRedirects.setStatus('current')
if mibBuilder.loadTexts: apIpv4IfRedirects.setDescription('Enable/disable the transmission of ICMP redirect packets.')
apIpv4IfUnreachables = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4IfUnreachables.setStatus('current')
if mibBuilder.loadTexts: apIpv4IfUnreachables.setDescription('Enable/disable the transmission of ICMP unreachable packets.')
apIpv4IfIrdp = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4IfIrdp.setStatus('current')
if mibBuilder.loadTexts: apIpv4IfIrdp.setDescription('Enable/disable router discovery.')
apIpv4IfIrdpUseMulticast = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4IfIrdpUseMulticast.setStatus('obsolete')
if mibBuilder.loadTexts: apIpv4IfIrdpUseMulticast.setDescription('Enable/disable the use of the multicast address 224.0.0.1 for transmission of router discovery packets. Default is disabled (use 255.255.255.255).')
apIpv4IfIrdpMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 11), Integer32().clone(600)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4IfIrdpMax.setStatus('obsolete')
if mibBuilder.loadTexts: apIpv4IfIrdpMax.setDescription('Maximum interval between advertisements (seconds). Default is 600 seconds.')
apIpv4IfIrdpMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4IfIrdpMin.setStatus('obsolete')
if mibBuilder.loadTexts: apIpv4IfIrdpMin.setDescription('Minimum interval between advertisements (seconds). Default (0) is means use 0.75 times max. If non-zero, this value must be less than apIpv4IfIrdpMax.')
apIpv4IfIrdpPref = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 13), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4IfIrdpPref.setStatus('current')
if mibBuilder.loadTexts: apIpv4IfIrdpPref.setDescription('Router preference value to advertise. Default is 0.')
apIpv4IfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4IfStatus.setStatus('current')
if mibBuilder.loadTexts: apIpv4IfStatus.setDescription('(fill in later)')
apIpv4IfRunRedundancyProto = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 15), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4IfRunRedundancyProto.setStatus('current')
if mibBuilder.loadTexts: apIpv4IfRunRedundancyProto.setDescription('Indicates whether a redundancy protocol is run on this interface.')
mibBuilder.exportSymbols("IPV4INTERFACE-MIB", apIpv4IfState=apIpv4IfState, apIpv4IfBroadcastIpAddress=apIpv4IfBroadcastIpAddress, apIpv4IfDisable=apIpv4IfDisable, apIpv4InterfaceEntry=apIpv4InterfaceEntry, apIpv4IfIrdpUseMulticast=apIpv4IfIrdpUseMulticast, apIpv4InterfaceMib=apIpv4InterfaceMib, apIpv4IfNetPrefixLen=apIpv4IfNetPrefixLen, PYSNMP_MODULE_ID=apIpv4InterfaceMib, apIpv4IfIrdpPref=apIpv4IfIrdpPref, apIpv4IfIrdp=apIpv4IfIrdp, apIpv4IfRedirects=apIpv4IfRedirects, apIpv4IfCircuitIfIndex=apIpv4IfCircuitIfIndex, apIpv4IfRunRedundancyProto=apIpv4IfRunRedundancyProto, apIpv4IfStatus=apIpv4IfStatus, apIpv4IfAddress=apIpv4IfAddress, apIpv4IfIrdpMax=apIpv4IfIrdpMax, apIpv4InterfaceTable=apIpv4InterfaceTable, apIpv4IfIrdpMin=apIpv4IfIrdpMin, apIpv4IfUnreachables=apIpv4IfUnreachables)
