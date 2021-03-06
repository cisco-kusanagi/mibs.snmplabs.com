#
# PySNMP MIB module HP-ICF-DHCPv6-RELAY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-DHCPv6-RELAY
# Produced by pysmi-0.3.4 at Mon Apr 29 19:21:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, IpAddress, NotificationType, Counter32, ObjectIdentity, ModuleIdentity, Counter64, Bits, MibIdentifier, Integer32, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "IpAddress", "NotificationType", "Counter32", "ObjectIdentity", "ModuleIdentity", "Counter64", "Bits", "MibIdentifier", "Integer32", "iso", "TimeTicks")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hpicfDhcpv6Relay = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50))
hpicfDhcpv6Relay.setRevisions(('2014-02-12 00:00', '2012-04-24 00:00', '2008-04-08 06:05',))
if mibBuilder.loadTexts: hpicfDhcpv6Relay.setLastUpdated('201402120000Z')
if mibBuilder.loadTexts: hpicfDhcpv6Relay.setOrganization('HP Networking')
hpicfDhcpv6RelayAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDhcpv6RelayAdminStatus.setStatus('current')
hpicfDhcpRelayHelperAddressTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 2), )
if mibBuilder.loadTexts: hpicfDhcpRelayHelperAddressTable.setStatus('current')
hpicfDhcpRelayHelperAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayHelperAddressType"), (0, "HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayHelperAddress"))
if mibBuilder.loadTexts: hpicfDhcpRelayHelperAddressEntry.setStatus('current')
hpicfDhcpRelayHelperAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hpicfDhcpRelayHelperAddressType.setStatus('current')
hpicfDhcpRelayHelperAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 2, 1, 2), InetAddress())
if mibBuilder.loadTexts: hpicfDhcpRelayHelperAddress.setStatus('current')
hpicfDhcpRelayHelperAddressEgressInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 2, 1, 3), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfDhcpRelayHelperAddressEgressInterface.setStatus('current')
hpicfDhcpRelayHelperAddressStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfDhcpRelayHelperAddressStatus.setStatus('current')
hpicfDhcpRelayPerInterfaceStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 3), )
if mibBuilder.loadTexts: hpicfDhcpRelayPerInterfaceStatsTable.setStatus('current')
hpicfDhcpRelayPerInterfaceStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfDhcpRelayPerInterfaceStatsEntry.setStatus('current')
hpicfDhcpRelayPerInterfaceClientPktsRecd = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayPerInterfaceClientPktsRecd.setStatus('current')
hpicfDhcpRelayPerInterfaceClientPktsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayPerInterfaceClientPktsDropped.setStatus('current')
hpicfDhcpRelayPerInterfaceClientPktsXmitFail = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayPerInterfaceClientPktsXmitFail.setStatus('current')
hpicfDhcpRelayPerInterfaceServerPktsRecd = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayPerInterfaceServerPktsRecd.setStatus('current')
hpicfDhcpRelayPerInterfaceServerPktsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayPerInterfaceServerPktsDropped.setStatus('current')
hpicfDhcpRelayPerInterfaceServerPktsXmitFail = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayPerInterfaceServerPktsXmitFail.setStatus('current')
hpicfDhcpRelayGlobalStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5))
hpicfDhcpv6RelayOptions = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 6))
hpicfDhcpRelayPktsDropped = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayPktsDropped.setStatus('current')
hpicfDhcpRelayErrorPktsDropped = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayErrorPktsDropped.setStatus('current')
hpicfDhcpRelayTotalPktsReceived = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayTotalPktsReceived.setStatus('current')
hpicfDhcpRelaySolicitPktsReceived = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelaySolicitPktsReceived.setStatus('current')
hpicfDhcpRelayRequestPktsReceived = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayRequestPktsReceived.setStatus('current')
hpicfDhcpRelayConfirmPktsReceived = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayConfirmPktsReceived.setStatus('current')
hpicfDhcpRelayRenewPktsReceived = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayRenewPktsReceived.setStatus('current')
hpicfDhcpRelayRebindPktsReceived = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayRebindPktsReceived.setStatus('current')
hpicfDhcpRelayReleasePktsReceived = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayReleasePktsReceived.setStatus('current')
hpicfDhcpRelayDeclinePktsReceived = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayDeclinePktsReceived.setStatus('current')
hpicfDhcpRelayInformationReqPktsReceived = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayInformationReqPktsReceived.setStatus('current')
hpicfDhcpRelayRelayForwardPktsReceived = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayRelayForwardPktsReceived.setStatus('current')
hpicfDhcpRelayRelayReplyPktsReceived = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayRelayReplyPktsReceived.setStatus('current')
hpicfDhcpRelayTotalPktsSent = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayTotalPktsSent.setStatus('current')
hpicfDhcpRelayAdvertisePktsSent = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayAdvertisePktsSent.setStatus('current')
hpicfDhcpRelayReconfigurePktsSent = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayReconfigurePktsSent.setStatus('current')
hpicfDhcpRelayReplyPktsSent = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayReplyPktsSent.setStatus('current')
hpicfDhcpRelayRelayForwardPktsSent = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayRelayForwardPktsSent.setStatus('current')
hpicfDhcpRelayRelayReplyPktsSent = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpRelayRelayReplyPktsSent.setStatus('current')
hpicfDhcpv6RelayOption79Status = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDhcpv6RelayOption79Status.setStatus('current')
hpicfDhcpRelayConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 4))
hpicfDhcpRelayGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 4, 1))
hpicfDhcpRelayCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 4, 2))
hpicfDhcpRelayConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 4, 1, 1)).setObjects(("HP-ICF-DHCPv6-RELAY", "hpicfDhcpv6RelayAdminStatus"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayHelperAddressEgressInterface"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayHelperAddressStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDhcpRelayConfigGroup = hpicfDhcpRelayConfigGroup.setStatus('deprecated')
hpicfDhcpRelayConfigGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 4, 1, 4)).setObjects(("HP-ICF-DHCPv6-RELAY", "hpicfDhcpv6RelayAdminStatus"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayHelperAddressEgressInterface"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayHelperAddressStatus"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpv6RelayOption79Status"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDhcpRelayConfigGroup1 = hpicfDhcpRelayConfigGroup1.setStatus('current')
hpicfDhcpRelayStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 4, 1, 2)).setObjects(("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceClientPktsRecd"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceClientPktsDropped"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceClientPktsXmitFail"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceServerPktsRecd"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceServerPktsDropped"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceServerPktsXmitFail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDhcpRelayStatsGroup = hpicfDhcpRelayStatsGroup.setStatus('deprecated')
hpicfDhcpRelayStatsGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 4, 1, 3)).setObjects(("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceClientPktsRecd"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceClientPktsDropped"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceClientPktsXmitFail"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceServerPktsRecd"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceServerPktsDropped"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceServerPktsXmitFail"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPktsDropped"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayErrorPktsDropped"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayTotalPktsReceived"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelaySolicitPktsReceived"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayRequestPktsReceived"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayConfirmPktsReceived"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayRenewPktsReceived"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayRebindPktsReceived"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayReleasePktsReceived"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayDeclinePktsReceived"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayInformationReqPktsReceived"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayRelayForwardPktsReceived"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayRelayReplyPktsReceived"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayTotalPktsSent"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayAdvertisePktsSent"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayReconfigurePktsSent"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayReplyPktsSent"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayRelayForwardPktsSent"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayRelayReplyPktsSent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDhcpRelayStatsGroup1 = hpicfDhcpRelayStatsGroup1.setStatus('current')
hpicfDhcpRelayCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 4, 2, 1)).setObjects(("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayConfigGroup"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDhcpRelayCompliance = hpicfDhcpRelayCompliance.setStatus('deprecated')
hpicfDhcpRelayCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 4, 2, 2)).setObjects(("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayConfigGroup"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayStatsGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDhcpRelayCompliance1 = hpicfDhcpRelayCompliance1.setStatus('deprecated')
hpicfDhcpRelayCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 4, 2, 3)).setObjects(("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayConfigGroup1"), ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayStatsGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDhcpRelayCompliance2 = hpicfDhcpRelayCompliance2.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-DHCPv6-RELAY", hpicfDhcpRelayCompliance2=hpicfDhcpRelayCompliance2, hpicfDhcpRelayRebindPktsReceived=hpicfDhcpRelayRebindPktsReceived, hpicfDhcpRelayTotalPktsReceived=hpicfDhcpRelayTotalPktsReceived, hpicfDhcpRelayPerInterfaceClientPktsDropped=hpicfDhcpRelayPerInterfaceClientPktsDropped, hpicfDhcpRelayPerInterfaceClientPktsXmitFail=hpicfDhcpRelayPerInterfaceClientPktsXmitFail, hpicfDhcpRelayHelperAddress=hpicfDhcpRelayHelperAddress, hpicfDhcpRelayTotalPktsSent=hpicfDhcpRelayTotalPktsSent, hpicfDhcpRelayCompliance=hpicfDhcpRelayCompliance, hpicfDhcpv6Relay=hpicfDhcpv6Relay, hpicfDhcpv6RelayOption79Status=hpicfDhcpv6RelayOption79Status, hpicfDhcpv6RelayAdminStatus=hpicfDhcpv6RelayAdminStatus, hpicfDhcpRelayReconfigurePktsSent=hpicfDhcpRelayReconfigurePktsSent, hpicfDhcpRelayConfirmPktsReceived=hpicfDhcpRelayConfirmPktsReceived, hpicfDhcpRelayStatsGroup1=hpicfDhcpRelayStatsGroup1, hpicfDhcpRelayRelayReplyPktsReceived=hpicfDhcpRelayRelayReplyPktsReceived, hpicfDhcpRelayConfigGroup=hpicfDhcpRelayConfigGroup, hpicfDhcpRelayGlobalStatistics=hpicfDhcpRelayGlobalStatistics, hpicfDhcpRelayHelperAddressEgressInterface=hpicfDhcpRelayHelperAddressEgressInterface, hpicfDhcpRelayDeclinePktsReceived=hpicfDhcpRelayDeclinePktsReceived, hpicfDhcpRelayPerInterfaceStatsTable=hpicfDhcpRelayPerInterfaceStatsTable, hpicfDhcpRelayAdvertisePktsSent=hpicfDhcpRelayAdvertisePktsSent, hpicfDhcpRelayRelayForwardPktsReceived=hpicfDhcpRelayRelayForwardPktsReceived, hpicfDhcpRelayHelperAddressStatus=hpicfDhcpRelayHelperAddressStatus, hpicfDhcpRelayPerInterfaceServerPktsDropped=hpicfDhcpRelayPerInterfaceServerPktsDropped, hpicfDhcpRelayPerInterfaceServerPktsRecd=hpicfDhcpRelayPerInterfaceServerPktsRecd, hpicfDhcpRelayCompliance1=hpicfDhcpRelayCompliance1, hpicfDhcpRelayGroups=hpicfDhcpRelayGroups, hpicfDhcpRelayRelayReplyPktsSent=hpicfDhcpRelayRelayReplyPktsSent, hpicfDhcpRelayConformance=hpicfDhcpRelayConformance, PYSNMP_MODULE_ID=hpicfDhcpv6Relay, hpicfDhcpRelayRequestPktsReceived=hpicfDhcpRelayRequestPktsReceived, hpicfDhcpRelayHelperAddressEntry=hpicfDhcpRelayHelperAddressEntry, hpicfDhcpRelayHelperAddressTable=hpicfDhcpRelayHelperAddressTable, hpicfDhcpRelayRenewPktsReceived=hpicfDhcpRelayRenewPktsReceived, hpicfDhcpRelayConfigGroup1=hpicfDhcpRelayConfigGroup1, hpicfDhcpRelayInformationReqPktsReceived=hpicfDhcpRelayInformationReqPktsReceived, hpicfDhcpRelaySolicitPktsReceived=hpicfDhcpRelaySolicitPktsReceived, hpicfDhcpRelayStatsGroup=hpicfDhcpRelayStatsGroup, hpicfDhcpRelayPktsDropped=hpicfDhcpRelayPktsDropped, hpicfDhcpRelayCompliances=hpicfDhcpRelayCompliances, hpicfDhcpRelayPerInterfaceServerPktsXmitFail=hpicfDhcpRelayPerInterfaceServerPktsXmitFail, hpicfDhcpRelayReleasePktsReceived=hpicfDhcpRelayReleasePktsReceived, hpicfDhcpRelayPerInterfaceClientPktsRecd=hpicfDhcpRelayPerInterfaceClientPktsRecd, hpicfDhcpRelayHelperAddressType=hpicfDhcpRelayHelperAddressType, hpicfDhcpRelayReplyPktsSent=hpicfDhcpRelayReplyPktsSent, hpicfDhcpv6RelayOptions=hpicfDhcpv6RelayOptions, hpicfDhcpRelayRelayForwardPktsSent=hpicfDhcpRelayRelayForwardPktsSent, hpicfDhcpRelayPerInterfaceStatsEntry=hpicfDhcpRelayPerInterfaceStatsEntry, hpicfDhcpRelayErrorPktsDropped=hpicfDhcpRelayErrorPktsDropped)
