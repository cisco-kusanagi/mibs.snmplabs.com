#
# PySNMP MIB module HP-ICF-BYOD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-BYOD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:20:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, IpAddress, Integer32, Gauge32, Counter32, TimeTicks, MibIdentifier, ObjectIdentity, NotificationType, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Integer32", "Gauge32", "Counter32", "TimeTicks", "MibIdentifier", "ObjectIdentity", "NotificationType", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
hpicfByodMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106))
hpicfByodMIB.setRevisions(('2014-05-19 09:00',))
if mibBuilder.loadTexts: hpicfByodMIB.setLastUpdated('201405190900Z')
if mibBuilder.loadTexts: hpicfByodMIB.setOrganization('HP Networking')
hpicfByodNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 0))
hpicfByodObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1))
hpicfByodConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 2))
hpicfByodConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1))
hpicfByodStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 2))
hpicfByodScalarConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 1))
hpicfByodPortalTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 2), )
if mibBuilder.loadTexts: hpicfByodPortalTable.setStatus('current')
hpicfByodPortalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 2, 1), ).setIndexNames((0, "HP-ICF-BYOD-MIB", "hpicfByodPortalName"))
if mibBuilder.loadTexts: hpicfByodPortalEntry.setStatus('current')
hpicfByodPortalName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: hpicfByodPortalName.setStatus('current')
hpicfByodPortalVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfByodPortalVlanId.setStatus('current')
hpicfByodPortalUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 127))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfByodPortalUrl.setStatus('current')
hpicfByodPortalInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 2, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfByodPortalInetAddrType.setStatus('current')
hpicfByodPortalInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 2, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfByodPortalInetAddr.setStatus('current')
hpicfByodPortalDnsCacheTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 2, 1, 6), TimeTicks().clone(15)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfByodPortalDnsCacheTime.setStatus('current')
hpicfByodPortalRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfByodPortalRowStatus.setStatus('current')
hpicfByodFreeRuleTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3), )
if mibBuilder.loadTexts: hpicfByodFreeRuleTable.setStatus('current')
hpicfByodFreeRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1), ).setIndexNames((0, "HP-ICF-BYOD-MIB", "hpicfByodFreeRuleNumber"))
if mibBuilder.loadTexts: hpicfByodFreeRuleEntry.setStatus('current')
hpicfByodFreeRuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 59)))
if mibBuilder.loadTexts: hpicfByodFreeRuleNumber.setStatus('current')
hpicfByodFreeRuleSourceProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tcp", 1), ("udp", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfByodFreeRuleSourceProtocol.setStatus('current')
hpicfByodFreeRuleSourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfByodFreeRuleSourcePort.setStatus('current')
hpicfByodFreeRuleSourceVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfByodFreeRuleSourceVlanId.setStatus('current')
hpicfByodFreeRuleSourceInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 5), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfByodFreeRuleSourceInetAddrType.setStatus('current')
hpicfByodFreeRuleSourceInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 6), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfByodFreeRuleSourceInetAddr.setStatus('current')
hpicfByodFreeRuleSourceInetAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 7), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfByodFreeRuleSourceInetAddrMask.setStatus('current')
hpicfByodFreeRuleDestinationProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tcp", 1), ("udp", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfByodFreeRuleDestinationProtocol.setStatus('current')
hpicfByodFreeRuleDestinationPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfByodFreeRuleDestinationPort.setStatus('current')
hpicfByodFreeRuleDestinationInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 10), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfByodFreeRuleDestinationInetAddrType.setStatus('current')
hpicfByodFreeRuleDestinationInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 11), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfByodFreeRuleDestinationInetAddr.setStatus('current')
hpicfByodFreeRuleDestinationInetAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 12), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfByodFreeRuleDestinationInetAddrMask.setStatus('current')
hpicfByodFreeRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfByodFreeRuleRowStatus.setStatus('current')
hpicfByodScalarStats = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 2, 1))
hpicfByodTcpStatsTotalOpen = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfByodTcpStatsTotalOpen.setStatus('current')
hpicfByodTcpStatsResetConn = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfByodTcpStatsResetConn.setStatus('current')
hpicfByodTcpStatsCurrentOpen = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfByodTcpStatsCurrentOpen.setStatus('current')
hpicfByodTcpStatsPktsReceived = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfByodTcpStatsPktsReceived.setStatus('current')
hpicfByodTcpStatsPktsSent = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfByodTcpStatsPktsSent.setStatus('current')
hpicfByodTcpStatsHttpPktsSent = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfByodTcpStatsHttpPktsSent.setStatus('current')
hpicfByodTcpStatsStateSynRcvd = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfByodTcpStatsStateSynRcvd.setStatus('current')
hpicfByodTcpStatsStateEstablished = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfByodTcpStatsStateEstablished.setStatus('current')
hpicfByodCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 2, 1))
hpicfByodGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 2, 2))
hpicfByodCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 2, 1, 1)).setObjects(("HP-ICF-BYOD-MIB", "hpicfByodConfigGroup"), ("HP-ICF-BYOD-MIB", "hpicfByodStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfByodCompliance1 = hpicfByodCompliance1.setStatus('current')
hpicfByodConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 2, 2, 1)).setObjects(("HP-ICF-BYOD-MIB", "hpicfByodPortalVlanId"), ("HP-ICF-BYOD-MIB", "hpicfByodPortalUrl"), ("HP-ICF-BYOD-MIB", "hpicfByodPortalInetAddrType"), ("HP-ICF-BYOD-MIB", "hpicfByodPortalInetAddr"), ("HP-ICF-BYOD-MIB", "hpicfByodPortalDnsCacheTime"), ("HP-ICF-BYOD-MIB", "hpicfByodPortalRowStatus"), ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleSourceProtocol"), ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleSourcePort"), ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleSourceVlanId"), ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleSourceInetAddrType"), ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleSourceInetAddr"), ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleSourceInetAddrMask"), ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleDestinationProtocol"), ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleDestinationPort"), ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleDestinationInetAddrType"), ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleDestinationInetAddr"), ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleDestinationInetAddrMask"), ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfByodConfigGroup = hpicfByodConfigGroup.setStatus('current')
hpicfByodStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 2, 2, 2)).setObjects(("HP-ICF-BYOD-MIB", "hpicfByodTcpStatsTotalOpen"), ("HP-ICF-BYOD-MIB", "hpicfByodTcpStatsResetConn"), ("HP-ICF-BYOD-MIB", "hpicfByodTcpStatsCurrentOpen"), ("HP-ICF-BYOD-MIB", "hpicfByodTcpStatsPktsReceived"), ("HP-ICF-BYOD-MIB", "hpicfByodTcpStatsPktsSent"), ("HP-ICF-BYOD-MIB", "hpicfByodTcpStatsHttpPktsSent"), ("HP-ICF-BYOD-MIB", "hpicfByodTcpStatsStateSynRcvd"), ("HP-ICF-BYOD-MIB", "hpicfByodTcpStatsStateEstablished"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfByodStatsGroup = hpicfByodStatsGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-BYOD-MIB", hpicfByodNotifications=hpicfByodNotifications, hpicfByodObjects=hpicfByodObjects, hpicfByodPortalUrl=hpicfByodPortalUrl, hpicfByodPortalDnsCacheTime=hpicfByodPortalDnsCacheTime, hpicfByodFreeRuleSourcePort=hpicfByodFreeRuleSourcePort, hpicfByodScalarStats=hpicfByodScalarStats, hpicfByodPortalRowStatus=hpicfByodPortalRowStatus, hpicfByodPortalEntry=hpicfByodPortalEntry, hpicfByodTcpStatsTotalOpen=hpicfByodTcpStatsTotalOpen, hpicfByodConfigGroup=hpicfByodConfigGroup, PYSNMP_MODULE_ID=hpicfByodMIB, hpicfByodFreeRuleEntry=hpicfByodFreeRuleEntry, hpicfByodFreeRuleSourceProtocol=hpicfByodFreeRuleSourceProtocol, hpicfByodFreeRuleDestinationPort=hpicfByodFreeRuleDestinationPort, hpicfByodTcpStatsResetConn=hpicfByodTcpStatsResetConn, hpicfByodPortalTable=hpicfByodPortalTable, hpicfByodFreeRuleDestinationInetAddr=hpicfByodFreeRuleDestinationInetAddr, hpicfByodFreeRuleSourceInetAddr=hpicfByodFreeRuleSourceInetAddr, hpicfByodConfigObjects=hpicfByodConfigObjects, hpicfByodTcpStatsStateSynRcvd=hpicfByodTcpStatsStateSynRcvd, hpicfByodTcpStatsPktsSent=hpicfByodTcpStatsPktsSent, hpicfByodFreeRuleDestinationInetAddrType=hpicfByodFreeRuleDestinationInetAddrType, hpicfByodCompliance1=hpicfByodCompliance1, hpicfByodCompliances=hpicfByodCompliances, hpicfByodPortalVlanId=hpicfByodPortalVlanId, hpicfByodFreeRuleDestinationProtocol=hpicfByodFreeRuleDestinationProtocol, hpicfByodFreeRuleRowStatus=hpicfByodFreeRuleRowStatus, hpicfByodTcpStatsPktsReceived=hpicfByodTcpStatsPktsReceived, hpicfByodTcpStatsHttpPktsSent=hpicfByodTcpStatsHttpPktsSent, hpicfByodFreeRuleTable=hpicfByodFreeRuleTable, hpicfByodPortalName=hpicfByodPortalName, hpicfByodStatsGroup=hpicfByodStatsGroup, hpicfByodPortalInetAddr=hpicfByodPortalInetAddr, hpicfByodFreeRuleSourceInetAddrType=hpicfByodFreeRuleSourceInetAddrType, hpicfByodTcpStatsStateEstablished=hpicfByodTcpStatsStateEstablished, hpicfByodFreeRuleSourceVlanId=hpicfByodFreeRuleSourceVlanId, hpicfByodFreeRuleSourceInetAddrMask=hpicfByodFreeRuleSourceInetAddrMask, hpicfByodFreeRuleDestinationInetAddrMask=hpicfByodFreeRuleDestinationInetAddrMask, hpicfByodMIB=hpicfByodMIB, hpicfByodFreeRuleNumber=hpicfByodFreeRuleNumber, hpicfByodTcpStatsCurrentOpen=hpicfByodTcpStatsCurrentOpen, hpicfByodGroups=hpicfByodGroups, hpicfByodPortalInetAddrType=hpicfByodPortalInetAddrType, hpicfByodConformance=hpicfByodConformance, hpicfByodScalarConfig=hpicfByodScalarConfig, hpicfByodStatsObjects=hpicfByodStatsObjects)
