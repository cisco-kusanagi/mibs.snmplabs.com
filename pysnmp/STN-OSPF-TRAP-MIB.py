#
# PySNMP MIB module STN-OSPF-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STN-OSPF-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:03:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ospfExtLsdbLimit, ospfAddressLessIf, ospfIfState, ospfNbrAddressLessIndex, ospf, ospfLsdbLsid, ospfVirtNbrArea, ospfNbrState, ospfNbrRtrId, ospfIfIpAddress, ospfLsdbRouterId, ospfVirtNbrState, ospfVirtIfNeighbor, ospfVirtIfState, ospfNbrIpAddr, ospfRouterId, ospfVirtIfAreaId, ospfLsdbAreaId, ospfVirtNbrRtrId, ospfLsdbType = mibBuilder.importSymbols("OSPF-MIB", "ospfExtLsdbLimit", "ospfAddressLessIf", "ospfIfState", "ospfNbrAddressLessIndex", "ospf", "ospfLsdbLsid", "ospfVirtNbrArea", "ospfNbrState", "ospfNbrRtrId", "ospfIfIpAddress", "ospfLsdbRouterId", "ospfVirtNbrState", "ospfVirtIfNeighbor", "ospfVirtIfState", "ospfNbrIpAddr", "ospfRouterId", "ospfVirtIfAreaId", "ospfLsdbAreaId", "ospfVirtNbrRtrId", "ospfLsdbType")
ospfConfigErrorType, ospfPacketSrc, ospfPacketType = mibBuilder.importSymbols("OSPF-TRAP-MIB", "ospfConfigErrorType", "ospfPacketSrc", "ospfPacketType")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, Gauge32, MibIdentifier, Integer32, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, TimeTicks, Counter32, ModuleIdentity, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "MibIdentifier", "Integer32", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "TimeTicks", "Counter32", "ModuleIdentity", "Counter64", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stnNotification, = mibBuilder.importSymbols("SPRING-TIDE-NETWORKS-SMI", "stnNotification")
stnOspfTraps, = mibBuilder.importSymbols("STN-IPROUTING-MIB", "stnOspfTraps")
stnRouterIndex, = mibBuilder.importSymbols("STN-ROUTER-MIB", "stnRouterIndex")
stnOspfTrap = ModuleIdentity((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1))
if mibBuilder.loadTexts: stnOspfTrap.setLastUpdated('0002160000Z')
if mibBuilder.loadTexts: stnOspfTrap.setOrganization('Spring Tide Networks, Inc.')
stnOspfTrapVars = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 1))
stnOspfNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2))
stnOspfNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0))
stnOspfVirtIfStateChange = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 1)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-MIB", "ospfVirtIfState"))
if mibBuilder.loadTexts: stnOspfVirtIfStateChange.setStatus('current')
stnOspfNbrStateChange = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 2)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfNbrIpAddr"), ("OSPF-MIB", "ospfNbrAddressLessIndex"), ("OSPF-MIB", "ospfNbrRtrId"), ("OSPF-MIB", "ospfNbrState"))
if mibBuilder.loadTexts: stnOspfNbrStateChange.setStatus('current')
stnOspfVirtNbrStateChange = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 3)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtNbrArea"), ("OSPF-MIB", "ospfVirtNbrRtrId"), ("OSPF-MIB", "ospfVirtNbrState"))
if mibBuilder.loadTexts: stnOspfVirtNbrStateChange.setStatus('current')
stnOspfIfConfigError = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 4)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-TRAP-MIB", "ospfPacketSrc"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: stnOspfIfConfigError.setStatus('current')
stnOspfVirtIfConfigError = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 5)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: stnOspfVirtIfConfigError.setStatus('current')
stnOspfIfAuthFailure = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 6)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-TRAP-MIB", "ospfPacketSrc"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: stnOspfIfAuthFailure.setStatus('current')
stnOspfVirtIfAuthFailure = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 7)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: stnOspfVirtIfAuthFailure.setStatus('current')
stnOspfIfRxBadPacket = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 8)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-TRAP-MIB", "ospfPacketSrc"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: stnOspfIfRxBadPacket.setStatus('current')
stnOspfVirtIfRxBadPacket = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 9)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: stnOspfVirtIfRxBadPacket.setStatus('current')
stnOspfTxRetransmit = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 10)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-MIB", "ospfNbrRtrId"), ("OSPF-TRAP-MIB", "ospfPacketType"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: stnOspfTxRetransmit.setStatus('current')
stnOspfVirtIfTxRetransmit = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 11)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-TRAP-MIB", "ospfPacketType"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: stnOspfVirtIfTxRetransmit.setStatus('current')
stnOspfOriginateLsa = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 12)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfLsdbAreaId"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: stnOspfOriginateLsa.setStatus('current')
stnOspfMaxAgeLsa = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 13)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfLsdbAreaId"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: stnOspfMaxAgeLsa.setStatus('current')
stnOspfLsdbOverflow = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 14)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfExtLsdbLimit"))
if mibBuilder.loadTexts: stnOspfLsdbOverflow.setStatus('current')
stnOspfLsdbApproachingOverflow = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 15)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfExtLsdbLimit"))
if mibBuilder.loadTexts: stnOspfLsdbApproachingOverflow.setStatus('current')
stnOspfIfStateChange = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 16)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-MIB", "ospfIfState"))
if mibBuilder.loadTexts: stnOspfIfStateChange.setStatus('current')
mibBuilder.exportSymbols("STN-OSPF-TRAP-MIB", stnOspfVirtIfAuthFailure=stnOspfVirtIfAuthFailure, stnOspfVirtIfConfigError=stnOspfVirtIfConfigError, stnOspfNotificationPrefix=stnOspfNotificationPrefix, stnOspfNbrStateChange=stnOspfNbrStateChange, stnOspfVirtIfStateChange=stnOspfVirtIfStateChange, stnOspfLsdbOverflow=stnOspfLsdbOverflow, stnOspfVirtIfTxRetransmit=stnOspfVirtIfTxRetransmit, stnOspfTxRetransmit=stnOspfTxRetransmit, stnOspfVirtIfRxBadPacket=stnOspfVirtIfRxBadPacket, stnOspfIfAuthFailure=stnOspfIfAuthFailure, stnOspfIfStateChange=stnOspfIfStateChange, stnOspfOriginateLsa=stnOspfOriginateLsa, stnOspfLsdbApproachingOverflow=stnOspfLsdbApproachingOverflow, stnOspfNotification=stnOspfNotification, stnOspfTrapVars=stnOspfTrapVars, PYSNMP_MODULE_ID=stnOspfTrap, stnOspfVirtNbrStateChange=stnOspfVirtNbrStateChange, stnOspfIfRxBadPacket=stnOspfIfRxBadPacket, stnOspfMaxAgeLsa=stnOspfMaxAgeLsa, stnOspfTrap=stnOspfTrap, stnOspfIfConfigError=stnOspfIfConfigError)
