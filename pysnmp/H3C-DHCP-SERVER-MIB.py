#
# PySNMP MIB module H3C-DHCP-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-DHCP-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:08:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, ObjectIdentity, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, Gauge32, IpAddress, Integer32, NotificationType, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Gauge32", "IpAddress", "Integer32", "NotificationType", "Counter64", "Bits")
DisplayString, TextualConvention, MacAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress", "RowStatus")
h3cDHCPServer = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101))
h3cDHCPServer.setRevisions(('2009-05-06 00:00',))
if mibBuilder.loadTexts: h3cDHCPServer.setLastUpdated('200905060000Z')
if mibBuilder.loadTexts: h3cDHCPServer.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
h3cDHCPServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 1))
h3cDHCPServerIPPoolUsage = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPServerIPPoolUsage.setStatus('current')
h3cDHCPServerReqTimes = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPServerReqTimes.setStatus('current')
h3cDHCPServerReqSuccessTimes = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPServerReqSuccessTimes.setStatus('current')
h3cDHCPServerAvgIpUseThreshold = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPServerAvgIpUseThreshold.setStatus('current')
h3cDHCPServerMaxIpUseThreshold = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPServerMaxIpUseThreshold.setStatus('current')
h3cDHCPServerAllocateThreshold = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPServerAllocateThreshold.setStatus('current')
h3cDHCPServerTables = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2))
h3cDHCPServerPoolName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDHCPServerPoolName.setStatus('current')
h3cDHCPSrvGlobalPoolTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 2), )
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolTable.setStatus('current')
h3cDHCPSrvGlobalPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 2, 1), ).setIndexNames((0, "H3C-DHCP-SERVER-MIB", "h3cDHCPSrvGlobalPoolName"))
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolEntry.setStatus('current')
h3cDHCPSrvGlobalPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolName.setStatus('current')
h3cDHCPSrvGlobalPoolRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolRowStatus.setStatus('current')
h3cDHCPSrvGlobalPoolConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3), )
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolConfigTable.setStatus('current')
h3cDHCPSrvGlobalPoolConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3, 1), ).setIndexNames((0, "H3C-DHCP-SERVER-MIB", "h3cDHCPSrvGlobalPoolName"))
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolConfigEntry.setStatus('current')
h3cDHCPSrvGlobalPoolType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("null", 0), ("host", 1), ("network", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolType.setStatus('current')
h3cDHCPSrvGlobalPoolNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolNetwork.setStatus('current')
h3cDHCPSrvGlobalPoolNetworkMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolNetworkMask.setStatus('current')
h3cDHCPSrvGlobalPoolHostIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolHostIPAddr.setStatus('current')
h3cDHCPSrvGlobalPoolHostMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolHostMask.setStatus('current')
h3cDHCPSrvGlobalPoolHostHAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3, 1, 6), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolHostHAddr.setStatus('current')
h3cDHCPSrvGlobalPoolCfgUndoFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("undonetworkip", 1), ("undohostip", 2), ("undohosthaddr", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolCfgUndoFlag.setStatus('current')
h3cDHCPSrvGlobalPoolStartAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolStartAddr.setStatus('current')
h3cDHCPSrvGlobalPoolEndAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 3, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolEndAddr.setStatus('current')
h3cDHCPSrvGlobalPoolParaTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4), )
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolParaTable.setStatus('current')
h3cDHCPSrvGlobalPoolParaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1), ).setIndexNames((0, "H3C-DHCP-SERVER-MIB", "h3cDHCPSrvGlobalPoolName"))
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolParaEntry.setStatus('current')
h3cDHCPSrvGlbPoolLeaseDay = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 365)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolLeaseDay.setStatus('current')
h3cDHCPSrvGlbPoolLeaseHour = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolLeaseHour.setStatus('current')
h3cDHCPSrvGlbPoolLeaseMinute = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolLeaseMinute.setStatus('current')
h3cDHCPSrvGlbPoolLeaseUnlimited = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("invalid", 0), ("unlimited", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolLeaseUnlimited.setStatus('current')
h3cDHCPSrvGlbPoolDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolDomainName.setStatus('current')
h3cDHCPSrvGlbPoolCliGWIPStr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 129))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliGWIPStr.setStatus('current')
h3cDHCPSrvGlbPoolCliGWIPUndo = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliGWIPUndo.setStatus('current')
h3cDHCPSrvGlbPoolCliDNSIPStr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 129))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliDNSIPStr.setStatus('current')
h3cDHCPSrvGlbPoolCliDNSIPUndo = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliDNSIPUndo.setStatus('current')
h3cDHCPSrvGlbPoolCliNetbiosType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8))).clone(namedValues=NamedValues(("null", 0), ("bnode", 1), ("pnode", 2), ("mnode", 4), ("hnode", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliNetbiosType.setStatus('current')
h3cDHCPSrvGlbPoolCliNbnsIPStr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 129))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliNbnsIPStr.setStatus('current')
h3cDHCPSrvGlbPoolCliNbnsIPUndo = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolCliNbnsIPUndo.setStatus('current')
h3cDHCPSrvGlbPoolParaUndoFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("undoDomain", 1), ("undoLease", 2), ("undoGateway", 3), ("undoDns", 4), ("undoNbns", 5), ("undoNbType", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolParaUndoFlag.setStatus('current')
h3cDHCPSrvGlbPoolIPInUseReset = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolIPInUseReset.setStatus('current')
h3cDHCPSrvGlbPoolLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 15), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolLeaseTime.setStatus('current')
h3cDHCPSrvGlbPoolPrimaryDNSIP = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 16), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolPrimaryDNSIP.setStatus('current')
h3cDHCPSrvGlbPoolSecondaryDNSIP = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 17), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolSecondaryDNSIP.setStatus('current')
h3cDHCPSrvGlbPoolLeaseSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 4, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolLeaseSecond.setStatus('current')
h3cDHCPSrvGlobalPoolOptionTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 5), )
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolOptionTable.setStatus('current')
h3cDHCPSrvGlobalPoolOptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 5, 1), ).setIndexNames((0, "H3C-DHCP-SERVER-MIB", "h3cDHCPSrvGlobalPoolName"), (0, "H3C-DHCP-SERVER-MIB", "h3cDHCPSrvGlbPoolOptCode"))
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolOptionEntry.setStatus('current')
h3cDHCPSrvGlbPoolOptCode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolOptCode.setStatus('current')
h3cDHCPSrvGlbPoolOptType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ascii", 1), ("hex", 2), ("ip", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolOptType.setStatus('current')
h3cDHCPSrvGlbPoolOptAscii = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 5, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolOptAscii.setStatus('current')
h3cDHCPSrvGlbPoolOptHexString = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 5, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 143))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolOptHexString.setStatus('current')
h3cDHCPSrvGlbPoolOptIPString = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 5, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 129))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolOptIPString.setStatus('current')
h3cDHCPSrvGlbPoolOptRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolOptRowStatus.setStatus('current')
h3cDHCPSrvGlobalPoolStatTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 6), )
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolStatTable.setStatus('current')
h3cDHCPSrvGlobalPoolStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 6, 1), ).setIndexNames((0, "H3C-DHCP-SERVER-MIB", "h3cDHCPSrvGlobalPoolName"))
if mibBuilder.loadTexts: h3cDHCPSrvGlobalPoolStatEntry.setStatus('current')
h3cDHCPSrvGlbPoolIPPoolUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolIPPoolUsage.setStatus('current')
h3cDHCPSrvGlbPoolReqTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolReqTimes.setStatus('current')
h3cDHCPSrvGlbPoolSuccessTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 2, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDHCPSrvGlbPoolSuccessTimes.setStatus('current')
h3cDHCPServerTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 3))
h3cDHCPServerTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 3, 0))
h3cDHCPServerAddrExhaust = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 3, 0, 1)).setObjects(("H3C-DHCP-SERVER-MIB", "h3cDHCPServerPoolName"))
if mibBuilder.loadTexts: h3cDHCPServerAddrExhaust.setStatus('current')
h3cDHCPServerAddrExhaustRecover = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 3, 0, 2)).setObjects(("H3C-DHCP-SERVER-MIB", "h3cDHCPServerPoolName"))
if mibBuilder.loadTexts: h3cDHCPServerAddrExhaustRecover.setStatus('current')
h3cDHCPServerAvgIpUsageOverflow = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 3, 0, 3)).setObjects(("H3C-DHCP-SERVER-MIB", "h3cDHCPServerPoolName"))
if mibBuilder.loadTexts: h3cDHCPServerAvgIpUsageOverflow.setStatus('current')
h3cDHCPServerMaxIpUsageOverflow = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 3, 0, 4)).setObjects(("H3C-DHCP-SERVER-MIB", "h3cDHCPServerPoolName"))
if mibBuilder.loadTexts: h3cDHCPServerMaxIpUsageOverflow.setStatus('current')
h3cDHCPServerAllocateOverflow = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 101, 3, 0, 5))
if mibBuilder.loadTexts: h3cDHCPServerAllocateOverflow.setStatus('current')
mibBuilder.exportSymbols("H3C-DHCP-SERVER-MIB", h3cDHCPSrvGlobalPoolNetworkMask=h3cDHCPSrvGlobalPoolNetworkMask, h3cDHCPServerMaxIpUsageOverflow=h3cDHCPServerMaxIpUsageOverflow, h3cDHCPSrvGlbPoolCliGWIPUndo=h3cDHCPSrvGlbPoolCliGWIPUndo, h3cDHCPSrvGlbPoolPrimaryDNSIP=h3cDHCPSrvGlbPoolPrimaryDNSIP, h3cDHCPServerAddrExhaust=h3cDHCPServerAddrExhaust, h3cDHCPSrvGlobalPoolStartAddr=h3cDHCPSrvGlobalPoolStartAddr, h3cDHCPSrvGlbPoolOptCode=h3cDHCPSrvGlbPoolOptCode, h3cDHCPSrvGlbPoolLeaseHour=h3cDHCPSrvGlbPoolLeaseHour, h3cDHCPServerTables=h3cDHCPServerTables, h3cDHCPSrvGlbPoolOptRowStatus=h3cDHCPSrvGlbPoolOptRowStatus, h3cDHCPSrvGlobalPoolEntry=h3cDHCPSrvGlobalPoolEntry, h3cDHCPSrvGlbPoolCliGWIPStr=h3cDHCPSrvGlbPoolCliGWIPStr, h3cDHCPSrvGlobalPoolStatEntry=h3cDHCPSrvGlobalPoolStatEntry, h3cDHCPSrvGlobalPoolTable=h3cDHCPSrvGlobalPoolTable, h3cDHCPSrvGlbPoolLeaseTime=h3cDHCPSrvGlbPoolLeaseTime, h3cDHCPSrvGlobalPoolNetwork=h3cDHCPSrvGlobalPoolNetwork, h3cDHCPSrvGlobalPoolConfigEntry=h3cDHCPSrvGlobalPoolConfigEntry, h3cDHCPSrvGlobalPoolHostMask=h3cDHCPSrvGlobalPoolHostMask, h3cDHCPSrvGlbPoolLeaseSecond=h3cDHCPSrvGlbPoolLeaseSecond, h3cDHCPSrvGlobalPoolHostIPAddr=h3cDHCPSrvGlobalPoolHostIPAddr, h3cDHCPServerMaxIpUseThreshold=h3cDHCPServerMaxIpUseThreshold, h3cDHCPSrvGlobalPoolOptionEntry=h3cDHCPSrvGlobalPoolOptionEntry, h3cDHCPServerAllocateOverflow=h3cDHCPServerAllocateOverflow, h3cDHCPSrvGlobalPoolConfigTable=h3cDHCPSrvGlobalPoolConfigTable, h3cDHCPSrvGlobalPoolType=h3cDHCPSrvGlobalPoolType, h3cDHCPServerObjects=h3cDHCPServerObjects, h3cDHCPSrvGlobalPoolStatTable=h3cDHCPSrvGlobalPoolStatTable, h3cDHCPServerAvgIpUseThreshold=h3cDHCPServerAvgIpUseThreshold, h3cDHCPSrvGlbPoolCliDNSIPUndo=h3cDHCPSrvGlbPoolCliDNSIPUndo, h3cDHCPServerTraps=h3cDHCPServerTraps, h3cDHCPSrvGlbPoolCliNbnsIPStr=h3cDHCPSrvGlbPoolCliNbnsIPStr, h3cDHCPServerTrapPrefix=h3cDHCPServerTrapPrefix, h3cDHCPServerAllocateThreshold=h3cDHCPServerAllocateThreshold, h3cDHCPSrvGlbPoolCliNetbiosType=h3cDHCPSrvGlbPoolCliNetbiosType, h3cDHCPSrvGlobalPoolOptionTable=h3cDHCPSrvGlobalPoolOptionTable, h3cDHCPSrvGlbPoolParaUndoFlag=h3cDHCPSrvGlbPoolParaUndoFlag, h3cDHCPSrvGlobalPoolHostHAddr=h3cDHCPSrvGlobalPoolHostHAddr, h3cDHCPSrvGlobalPoolCfgUndoFlag=h3cDHCPSrvGlobalPoolCfgUndoFlag, h3cDHCPSrvGlbPoolOptHexString=h3cDHCPSrvGlbPoolOptHexString, h3cDHCPServerReqSuccessTimes=h3cDHCPServerReqSuccessTimes, h3cDHCPSrvGlbPoolIPInUseReset=h3cDHCPSrvGlbPoolIPInUseReset, h3cDHCPServerIPPoolUsage=h3cDHCPServerIPPoolUsage, h3cDHCPSrvGlobalPoolEndAddr=h3cDHCPSrvGlobalPoolEndAddr, h3cDHCPSrvGlbPoolLeaseUnlimited=h3cDHCPSrvGlbPoolLeaseUnlimited, PYSNMP_MODULE_ID=h3cDHCPServer, h3cDHCPServerAddrExhaustRecover=h3cDHCPServerAddrExhaustRecover, h3cDHCPSrvGlobalPoolName=h3cDHCPSrvGlobalPoolName, h3cDHCPSrvGlbPoolLeaseMinute=h3cDHCPSrvGlbPoolLeaseMinute, h3cDHCPSrvGlobalPoolParaEntry=h3cDHCPSrvGlobalPoolParaEntry, h3cDHCPSrvGlbPoolDomainName=h3cDHCPSrvGlbPoolDomainName, h3cDHCPSrvGlobalPoolParaTable=h3cDHCPSrvGlobalPoolParaTable, h3cDHCPSrvGlbPoolOptType=h3cDHCPSrvGlbPoolOptType, h3cDHCPServer=h3cDHCPServer, h3cDHCPSrvGlbPoolCliDNSIPStr=h3cDHCPSrvGlbPoolCliDNSIPStr, h3cDHCPServerReqTimes=h3cDHCPServerReqTimes, h3cDHCPSrvGlbPoolReqTimes=h3cDHCPSrvGlbPoolReqTimes, h3cDHCPSrvGlobalPoolRowStatus=h3cDHCPSrvGlobalPoolRowStatus, h3cDHCPSrvGlbPoolOptIPString=h3cDHCPSrvGlbPoolOptIPString, h3cDHCPSrvGlbPoolSecondaryDNSIP=h3cDHCPSrvGlbPoolSecondaryDNSIP, h3cDHCPSrvGlbPoolSuccessTimes=h3cDHCPSrvGlbPoolSuccessTimes, h3cDHCPServerAvgIpUsageOverflow=h3cDHCPServerAvgIpUsageOverflow, h3cDHCPSrvGlbPoolOptAscii=h3cDHCPSrvGlbPoolOptAscii, h3cDHCPSrvGlbPoolCliNbnsIPUndo=h3cDHCPSrvGlbPoolCliNbnsIPUndo, h3cDHCPSrvGlbPoolLeaseDay=h3cDHCPSrvGlbPoolLeaseDay, h3cDHCPSrvGlbPoolIPPoolUsage=h3cDHCPSrvGlbPoolIPPoolUsage, h3cDHCPServerPoolName=h3cDHCPServerPoolName)
