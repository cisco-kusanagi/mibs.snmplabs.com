#
# PySNMP MIB module A3COM-HUAWEI-DHCP-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-DHCP-SERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:04:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ModuleIdentity, Bits, ObjectIdentity, iso, MibIdentifier, NotificationType, Integer32, IpAddress, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Bits", "ObjectIdentity", "iso", "MibIdentifier", "NotificationType", "Integer32", "IpAddress", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32")
RowStatus, MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "MacAddress", "TextualConvention", "DisplayString")
h3cDHCPServer = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101))
h3cDHCPServer.setRevisions(('2009-05-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cDHCPServer.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: h3cDHCPServer.setLastUpdated('200905060000Z')
if mibBuilder.loadTexts: h3cDHCPServer.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cDHCPServer.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip: 100085')
if mibBuilder.loadTexts: h3cDHCPServer.setDescription('The MIB module is used for DHCP server.')
h3cDHCPServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 1))
h3cDHCPServerIPPoolUsage = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPServerIPPoolUsage.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPServerIPPoolUsage.setDescription('Usage factor of DHCP server ip pool.')
h3cDHCPServerReqTimes = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPServerReqTimes.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPServerReqTimes.setDescription('Number of requests received by the DHCP server.')
h3cDHCPServerReqSuccessTimes = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPServerReqSuccessTimes.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPServerReqSuccessTimes.setDescription('Number of requests success responses sent by the DHCP server.')
h3cDHCPServerAvgIpUseThreshold = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPServerAvgIpUseThreshold.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPServerAvgIpUseThreshold.setDescription('Threshold of average IP useage of a DHCP server pool in 5 minutes.')
h3cDHCPServerMaxIpUseThreshold = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPServerMaxIpUseThreshold.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPServerMaxIpUseThreshold.setDescription('Threshold of maximum IP useage of a DHCP server pool in 5 minutes.')
h3cDHCPServerAllocateThreshold = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPServerAllocateThreshold.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPServerAllocateThreshold.setDescription('Threshold of DHCP server allocated IP address in 5 minutes.')
h3cDHCPServerTables = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2))
h3cDHCPServerPoolName = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDHCPServerPoolName.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPServerPoolName.setDescription('DHCP server pool name.')
h3cDHCPSrvGlobalPoolTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 2), )
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolTable.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolTable.setDescription('A table for creating DHCP server global pools.')
h3cDHCPSrvGlobalPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-DHCP-SERVER-MIB", "h3cDHCPSrvGlobalPoolName"))
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolEntry.setDescription('An entry containing objects for creating or deleting a global pool for the DHCP server.')
h3cDHCPSrvGlobalPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolName.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolName.setDescription('DHCP server global pool name.')
h3cDHCPSrvGlobalPoolRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolRowStatus.setDescription('RowStatus. Three actions are used: active, createAndGo, destroy.')
h3cDHCPSrvGlobalPoolConfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 3), )
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolConfigTable.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolConfigTable.setDescription('A table containing the configurations of dhcp server global pools.')
h3cDHCPSrvGlobalPoolConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-DHCP-SERVER-MIB", "h3cDHCPSrvGlobalPoolName"))
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolConfigEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolConfigEntry.setDescription('An entry containing the objects for configuring the network ip or host ip etc. to global pools for DHCP server.')
h3cDHCPSrvGlobalPoolType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("null", 0), ("host", 1), ("network", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolType.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolType.setDescription('Type of a DHCP global pool. Any operations of this object will be bound with the operations of h3cDHCPSrvGlobalPoolNetwork, h3cDHCPSrvGlobalPoolHostIPAddr, or h3cDHCPSrvGlobalPoolHostHAddr. That means any operation of this object alone will be regarded as invalid operation.')
h3cDHCPSrvGlobalPoolNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolNetwork.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolNetwork.setDescription('Network ip of a DHCP global pool. To delete a configured network ip, please set h3cDHCPSrvGlobalPoolCfgUndoFlag to 1.')
h3cDHCPSrvGlobalPoolNetworkMask = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 3, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolNetworkMask.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolNetworkMask.setDescription('Net mask of a DHCP global pool(network). The SET operation to this object ought to be with the SET of h3cDHCPSrvGlobalPoolNetwork together, and any SET operation alone to this object will be regarded as an invalid operation. When a network ip of a DHCP global pool was deleted, the net mask would also be deleted automatically, and no further operation needed.')
h3cDHCPSrvGlobalPoolHostIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolHostIPAddr.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolHostIPAddr.setDescription('Host ip of a DHCP global pool. To delete a configured network ip, please set h3cDHCPSrvGlobalPoolCfgUndoFlag to 2.')
h3cDHCPSrvGlobalPoolHostMask = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 3, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolHostMask.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolHostMask.setDescription('Net mask of a DHCP global pool(host) The SET operation to this object ought to be with the SET of h3cDHCPSrvGlobalPoolHostIPAddr together, and any SET operation alone to this object will be regarded as an invalid operation. When a host ip of a DHCP global pool was deleted, the net mask would also be deleted automatically, and no further operation needed.')
h3cDHCPSrvGlobalPoolHostHAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 3, 1, 6), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolHostHAddr.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolHostHAddr.setDescription('Hardware address of a DHCP global pool(host). To delete a configured hardware address, please set h3cDHCPSrvGlobalPoolCfgUndoFlag to 3.')
h3cDHCPSrvGlobalPoolCfgUndoFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("undonetworkip", 1), ("undohostip", 2), ("undohosthaddr", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolCfgUndoFlag.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolCfgUndoFlag.setDescription('Flag of undo operation for h3cDHCPSrvGlobalPoolConfigTable.')
h3cDHCPSrvGlobalPoolStartAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 3, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolStartAddr.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolStartAddr.setDescription('Start IP of a DHCP global pool. To delete a configured start IP, please set h3cDHCPSrvGlobalPoolStartAddr to 0. It takes effect only when h3cDHCPSrvGlobalPoolNetwork is set.')
h3cDHCPSrvGlobalPoolEndAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 3, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolEndAddr.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolEndAddr.setDescription('End ip of a DHCP global pool.')
h3cDHCPSrvGlobalPoolParaTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 4), )
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolParaTable.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolParaTable.setDescription('A table for configuring parameters to DHCP global pools.')
h3cDHCPSrvGlobalPoolParaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 4, 1), ).setIndexNames((0, "A3COM-HUAWEI-DHCP-SERVER-MIB", "h3cDHCPSrvGlobalPoolName"))
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolParaEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolParaEntry.setDescription('An entry containing the objects for the configurations of parameters of DHCP global pools.')
h3cDHCPSrvGlbPoolLeaseDay = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 365)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolLeaseDay.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolLeaseDay.setDescription('Number of days of the lease.')
h3cDHCPSrvGlbPoolLeaseHour = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolLeaseHour.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolLeaseHour.setDescription('Number of hours of the lease.')
h3cDHCPSrvGlbPoolLeaseMinute = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolLeaseMinute.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolLeaseMinute.setDescription('Number of minutes of the lease.')
h3cDHCPSrvGlbPoolLeaseUnlimited = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("invalid", 0), ("unlimited", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolLeaseUnlimited.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolLeaseUnlimited.setDescription('A flag denoting if the lease of a pool is unlimited.')
h3cDHCPSrvGlbPoolDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolDomainName.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolDomainName.setDescription('Domain name for DHCP clients.')
h3cDHCPSrvGlbPoolCliGWIPStr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 4, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 129))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliGWIPStr.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliGWIPStr.setDescription('String of gateway ip addresses for DHCP clients. Since mostly 8 ip can be configured for a pool totally, a string is defined to get or configure 8 ip ip at a time.')
h3cDHCPSrvGlbPoolCliGWIPUndo = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 4, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliGWIPUndo.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliGWIPUndo.setDescription('A gateway ip address to delete. This object is only for deleting a given ip of gateway router.')
h3cDHCPSrvGlbPoolCliDNSIPStr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 4, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 129))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliDNSIPStr.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliDNSIPStr.setDescription('String of DNS server ip addresses for DHCP clients. Since mostly 8 ip can be configured for a pool totally, a string is defined to get or configure 8 ip at a time.')
h3cDHCPSrvGlbPoolCliDNSIPUndo = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 4, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliDNSIPUndo.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliDNSIPUndo.setDescription('A DNS server ip address to delete. This object is only for deleting a given ip of DNS server.')
h3cDHCPSrvGlbPoolCliNetbiosType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8))).clone(namedValues=NamedValues(("null", 0), ("bnode", 1), ("pnode", 2), ("mnode", 4), ("hnode", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliNetbiosType.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliNetbiosType.setDescription('NetBios node type for DHCP clients.')
h3cDHCPSrvGlbPoolCliNbnsIPStr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 4, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 129))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliNbnsIPStr.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliNbnsIPStr.setDescription('String of NetBios server ip addresses for DHCP clients. Since mostly 8 ip can be configured for a pool totally, so a string is defined to get or configure 8 ip at a time.')
h3cDHCPSrvGlbPoolCliNbnsIPUndo = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 4, 1, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliNbnsIPUndo.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliNbnsIPUndo.setDescription('A NetBios server ip address to delete. This object is only for deleting a given ip of NetBios server.')
h3cDHCPSrvGlbPoolParaUndoFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 4, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("undoDomain", 1), ("undoLease", 2), ("undoGateway", 3), ("undoDns", 4), ("undoNbns", 5), ("undoNbType", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolParaUndoFlag.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolParaUndoFlag.setDescription('Flag of undo-operation for h3cDHCPSrvGlobalPoolParaTable.')
h3cDHCPSrvGlbPoolIPInUseReset = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 4, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolIPInUseReset.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolIPInUseReset.setDescription('Reset the auto binding ip of the given global pool for DHCP server.')
h3cDHCPSrvGlbPoolLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 4, 1, 15), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolLeaseTime.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolLeaseTime.setDescription('Number of timeticks of the lease.')
h3cDHCPSrvGlbPoolPrimaryDNSIP = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 4, 1, 16), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolPrimaryDNSIP.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolPrimaryDNSIP.setDescription('The Primary DNS server IP address to be assigned to the client. To delete a configured Primary DNS server IP, please set h3cDHCPSrvGlbPoolPrimaryDNSIP to 0. It takes effect only when h3cDHCPSrvGlobalPoolNetwork is set.')
h3cDHCPSrvGlbPoolSecondaryDNSIP = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 4, 1, 17), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolSecondaryDNSIP.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolSecondaryDNSIP.setDescription('The Secondary DNS server IP address to be assigned to the client. To delete a configured Secondary DNS server IP, please set h3cDHCPSrvGlbPoolSecondaryDNSIP to 0. It takes effect only when h3cDHCPSrvGlobalPoolNetwork is set.')
h3cDHCPSrvGlbPoolLeaseSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 4, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolLeaseSecond.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolLeaseSecond.setDescription('Number of seconds of the lease.')
h3cDHCPSrvGlobalPoolOptionTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 5), )
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolOptionTable.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolOptionTable.setDescription('A table for configuring options to DHCP global pools.')
h3cDHCPSrvGlobalPoolOptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 5, 1), ).setIndexNames((0, "A3COM-HUAWEI-DHCP-SERVER-MIB", "h3cDHCPSrvGlobalPoolName"), (0, "A3COM-HUAWEI-DHCP-SERVER-MIB", "h3cDHCPSrvGlbPoolOptCode"))
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolOptionEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolOptionEntry.setDescription('An entry containing the objects for configuring options to DHCP global pools.')
h3cDHCPSrvGlbPoolOptCode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolOptCode.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolOptCode.setDescription('Option code.')
h3cDHCPSrvGlbPoolOptType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ascii", 1), ("hex", 2), ("ip", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolOptType.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolOptType.setDescription('Option type.')
h3cDHCPSrvGlbPoolOptAscii = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 5, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolOptAscii.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolOptAscii.setDescription('Ascii string of an option.')
h3cDHCPSrvGlbPoolOptHexString = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 5, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 143))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolOptHexString.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolOptHexString.setDescription("Hex string of an option. 1st to 16th hex strings, which are 2 bytes, 4 bytes, 6 bytes or 8 bytes, can be configured at most simultaneously. That means the format of each string must be '12', '1234', '123456' or '12345678'.")
h3cDHCPSrvGlbPoolOptIPString = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 5, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 129))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolOptIPString.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolOptIPString.setDescription('Ip string of an option. 1 to 8 ip addresses can be configured at most simultaneously.')
h3cDHCPSrvGlbPoolOptRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolOptRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolOptRowStatus.setDescription('RowStatus. Three actions are used: active, createAndGo, destroy.')
h3cDHCPSrvGlobalPoolStatTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 6), )
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolStatTable.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolStatTable.setDescription('The statistics of each DHCP address pool.')
h3cDHCPSrvGlobalPoolStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 6, 1), ).setIndexNames((0, "A3COM-HUAWEI-DHCP-SERVER-MIB", "h3cDHCPSrvGlobalPoolName"))
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolStatEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolStatEntry.setDescription('An entry containing the statistics of each DHCP address pool.')
h3cDHCPSrvGlbPoolIPPoolUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolIPPoolUsage.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolIPPoolUsage.setDescription('Utilization rate of IP addresses in each DHCP address pool, in percentage.')
h3cDHCPSrvGlbPoolReqTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolReqTimes.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolReqTimes.setDescription('Number of request packets received by each DHCP address pool, including the request packets for an extension of the lease.')
h3cDHCPSrvGlbPoolSuccessTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolSuccessTimes.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolSuccessTimes.setDescription('Number of positive responses sent by each DHCP address pool, including responses to the request for an extension of the lease.')
h3cDHCPSrvGlbPoolDiscoverTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolDiscoverTimes.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolDiscoverTimes.setDescription('Number of discover packets received by each DHCP address pool.')
h3cDHCPSrvGlbPoolOfferTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolOfferTimes.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolOfferTimes.setDescription('Number of offer packets sent by each DHCP address pool.')
h3cDHCPSrvGlbPoolACKTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 2, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolACKTimes.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolACKTimes.setDescription('Number of ACK packets sent by each DHCP address pool.')
h3cDHCPServerTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 3))
h3cDHCPServerTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 3, 0))
h3cDHCPServerAddrExhaust = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 3, 0, 1)).setObjects(("A3COM-HUAWEI-DHCP-SERVER-MIB", "h3cDHCPServerPoolName"), ("A3COM-HUAWEI-DHCP-SERVER-MIB", "h3cDHCPServerFirstTrapTime"))
if mibBuilder.loadTexts: h3cDHCPServerAddrExhaust.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPServerAddrExhaust.setDescription('This trap is generated when the device DHCP server address exhaust.')
h3cDHCPServerAddrExhaustRecover = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 3, 0, 2)).setObjects(("A3COM-HUAWEI-DHCP-SERVER-MIB", "h3cDHCPServerPoolName"), ("A3COM-HUAWEI-DHCP-SERVER-MIB", "h3cDHCPServerFirstTrapTime"))
if mibBuilder.loadTexts: h3cDHCPServerAddrExhaustRecover.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPServerAddrExhaustRecover.setDescription('This trap is generated when the device DHCP server address exhaust recover.')
h3cDHCPServerAvgIpUsageOverflow = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 3, 0, 3)).setObjects(("A3COM-HUAWEI-DHCP-SERVER-MIB", "h3cDHCPServerPoolName"))
if mibBuilder.loadTexts: h3cDHCPServerAvgIpUsageOverflow.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPServerAvgIpUsageOverflow.setDescription('This trap is generated when the average IP address usage of DHCP server pool in 5 minutes overflows.')
h3cDHCPServerMaxIpUsageOverflow = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 3, 0, 4)).setObjects(("A3COM-HUAWEI-DHCP-SERVER-MIB", "h3cDHCPServerPoolName"))
if mibBuilder.loadTexts: h3cDHCPServerMaxIpUsageOverflow.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPServerMaxIpUsageOverflow.setDescription('This trap is generated when the maximun IP address usage of DHCP server pool in 5 minutes overflows.')
h3cDHCPServerAllocateOverflow = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 3, 0, 5))
if mibBuilder.loadTexts: h3cDHCPServerAllocateOverflow.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPServerAllocateOverflow.setDescription('This trap is generated when the number of DHCP server allocated IP address in 5 minutes overflows.')
h3cDHCPServerTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 3, 1))
h3cDHCPServerFirstTrapTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 101, 3, 1, 1), TimeTicks()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDHCPServerFirstTrapTime.setStatus('current')
if mibBuilder.loadTexts: h3cDHCPServerFirstTrapTime.setDescription('Represents the first trap time.')
mibBuilder.exportSymbols("A3COM-HUAWEI-DHCP-SERVER-MIB", h3cDHCPSrvGlbPoolCliNetbiosType=h3cDHCPSrvGlbPoolCliNetbiosType, h3cDHCPServerAllocateThreshold=h3cDHCPServerAllocateThreshold, h3cDHCPServerAllocateOverflow=h3cDHCPServerAllocateOverflow, h3cDHCPSrvGlbPoolLeaseDay=h3cDHCPSrvGlbPoolLeaseDay, h3cDHCPSrvGlbPoolOptAscii=h3cDHCPSrvGlbPoolOptAscii, h3cDHCPSrvGlbPoolCliNbnsIPUndo=h3cDHCPSrvGlbPoolCliNbnsIPUndo, h3cDHCPSrvGlbPoolParaUndoFlag=h3cDHCPSrvGlbPoolParaUndoFlag, h3cDHCPServerMaxIpUsageOverflow=h3cDHCPServerMaxIpUsageOverflow, h3cDHCPServerIPPoolUsage=h3cDHCPServerIPPoolUsage, h3cDHCPSrvGlbPoolOptRowStatus=h3cDHCPSrvGlbPoolOptRowStatus, h3cDHCPServerTraps=h3cDHCPServerTraps, h3cDHCPSrvGlobalPoolNetwork=h3cDHCPSrvGlobalPoolNetwork, h3cDHCPSrvGlobalPoolHostIPAddr=h3cDHCPSrvGlobalPoolHostIPAddr, h3cDHCPSrvGlbPoolCliNbnsIPStr=h3cDHCPSrvGlbPoolCliNbnsIPStr, h3cDHCPSrvGlbPoolReqTimes=h3cDHCPSrvGlbPoolReqTimes, h3cDHCPSrvGlbPoolOptHexString=h3cDHCPSrvGlbPoolOptHexString, h3cDHCPServerMaxIpUseThreshold=h3cDHCPServerMaxIpUseThreshold, h3cDHCPServer=h3cDHCPServer, PYSNMP_MODULE_ID=h3cDHCPServer, h3cDHCPSrvGlobalPoolStartAddr=h3cDHCPSrvGlobalPoolStartAddr, h3cDHCPServerFirstTrapTime=h3cDHCPServerFirstTrapTime, h3cDHCPSrvGlobalPoolHostHAddr=h3cDHCPSrvGlobalPoolHostHAddr, h3cDHCPSrvGlbPoolDomainName=h3cDHCPSrvGlbPoolDomainName, h3cDHCPSrvGlbPoolLeaseTime=h3cDHCPSrvGlbPoolLeaseTime, h3cDHCPSrvGlbPoolLeaseMinute=h3cDHCPSrvGlbPoolLeaseMinute, h3cDHCPSrvGlbPoolOptCode=h3cDHCPSrvGlbPoolOptCode, h3cDHCPSrvGlobalPoolName=h3cDHCPSrvGlobalPoolName, h3cDHCPSrvGlbPoolCliDNSIPUndo=h3cDHCPSrvGlbPoolCliDNSIPUndo, h3cDHCPServerAddrExhaustRecover=h3cDHCPServerAddrExhaustRecover, h3cDHCPSrvGlobalPoolEntry=h3cDHCPSrvGlobalPoolEntry, h3cDHCPSrvGlbPoolCliDNSIPStr=h3cDHCPSrvGlbPoolCliDNSIPStr, h3cDHCPServerTables=h3cDHCPServerTables, h3cDHCPSrvGlbPoolSecondaryDNSIP=h3cDHCPSrvGlbPoolSecondaryDNSIP, h3cDHCPServerAvgIpUsageOverflow=h3cDHCPServerAvgIpUsageOverflow, h3cDHCPSrvGlbPoolOfferTimes=h3cDHCPSrvGlbPoolOfferTimes, h3cDHCPSrvGlbPoolACKTimes=h3cDHCPSrvGlbPoolACKTimes, h3cDHCPServerTrapObjects=h3cDHCPServerTrapObjects, h3cDHCPSrvGlbPoolLeaseUnlimited=h3cDHCPSrvGlbPoolLeaseUnlimited, h3cDHCPSrvGlobalPoolType=h3cDHCPSrvGlobalPoolType, h3cDHCPSrvGlobalPoolConfigEntry=h3cDHCPSrvGlobalPoolConfigEntry, h3cDHCPSrvGlbPoolCliGWIPUndo=h3cDHCPSrvGlbPoolCliGWIPUndo, h3cDHCPSrvGlobalPoolConfigTable=h3cDHCPSrvGlobalPoolConfigTable, h3cDHCPServerObjects=h3cDHCPServerObjects, h3cDHCPServerReqTimes=h3cDHCPServerReqTimes, h3cDHCPSrvGlbPoolLeaseHour=h3cDHCPSrvGlbPoolLeaseHour, h3cDHCPSrvGlbPoolIPInUseReset=h3cDHCPSrvGlbPoolIPInUseReset, h3cDHCPSrvGlbPoolIPPoolUsage=h3cDHCPSrvGlbPoolIPPoolUsage, h3cDHCPSrvGlobalPoolParaTable=h3cDHCPSrvGlobalPoolParaTable, h3cDHCPServerTrapPrefix=h3cDHCPServerTrapPrefix, h3cDHCPSrvGlbPoolSuccessTimes=h3cDHCPSrvGlbPoolSuccessTimes, h3cDHCPSrvGlobalPoolOptionTable=h3cDHCPSrvGlobalPoolOptionTable, h3cDHCPSrvGlobalPoolRowStatus=h3cDHCPSrvGlobalPoolRowStatus, h3cDHCPSrvGlbPoolDiscoverTimes=h3cDHCPSrvGlbPoolDiscoverTimes, h3cDHCPSrvGlobalPoolNetworkMask=h3cDHCPSrvGlobalPoolNetworkMask, h3cDHCPSrvGlbPoolLeaseSecond=h3cDHCPSrvGlbPoolLeaseSecond, h3cDHCPSrvGlobalPoolStatEntry=h3cDHCPSrvGlobalPoolStatEntry, h3cDHCPSrvGlobalPoolEndAddr=h3cDHCPSrvGlobalPoolEndAddr, h3cDHCPSrvGlobalPoolStatTable=h3cDHCPSrvGlobalPoolStatTable, h3cDHCPSrvGlbPoolOptType=h3cDHCPSrvGlbPoolOptType, h3cDHCPSrvGlobalPoolTable=h3cDHCPSrvGlobalPoolTable, h3cDHCPSrvGlbPoolPrimaryDNSIP=h3cDHCPSrvGlbPoolPrimaryDNSIP, h3cDHCPSrvGlbPoolCliGWIPStr=h3cDHCPSrvGlbPoolCliGWIPStr, h3cDHCPSrvGlobalPoolOptionEntry=h3cDHCPSrvGlobalPoolOptionEntry, h3cDHCPServerPoolName=h3cDHCPServerPoolName, h3cDHCPSrvGlbPoolOptIPString=h3cDHCPSrvGlbPoolOptIPString, h3cDHCPSrvGlobalPoolCfgUndoFlag=h3cDHCPSrvGlobalPoolCfgUndoFlag, h3cDHCPServerReqSuccessTimes=h3cDHCPServerReqSuccessTimes, h3cDHCPSrvGlobalPoolHostMask=h3cDHCPSrvGlobalPoolHostMask, h3cDHCPSrvGlobalPoolParaEntry=h3cDHCPSrvGlobalPoolParaEntry, h3cDHCPServerAvgIpUseThreshold=h3cDHCPServerAvgIpUseThreshold, h3cDHCPServerAddrExhaust=h3cDHCPServerAddrExhaust)