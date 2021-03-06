#
# PySNMP MIB module HPN-ICF-MCDR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-MCDR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:40:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, Unsigned32, MibIdentifier, TimeTicks, Bits, Gauge32, IpAddress, Counter64, Integer32, iso, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "MibIdentifier", "TimeTicks", "Bits", "Gauge32", "IpAddress", "Counter64", "Integer32", "iso", "Counter32", "NotificationType")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
hpnicfMultCDR = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86))
hpnicfMultCDR.setRevisions(('2007-12-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfMultCDR.setRevisionsDescriptions(('The multicast call detail record MIB.',))
if mibBuilder.loadTexts: hpnicfMultCDR.setLastUpdated('200712150000Z')
if mibBuilder.loadTexts: hpnicfMultCDR.setOrganization('')
if mibBuilder.loadTexts: hpnicfMultCDR.setContactInfo('')
if mibBuilder.loadTexts: hpnicfMultCDR.setDescription('The initial version of this MIB file.')
hpnicfMultCDRCfgObject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 1))
hpnicfMultCDRStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfMultCDRStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfMultCDRStatus.setDescription('Configure to enable or disable multicast CDR function.')
hpnicfMultCDRReportInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfMultCDRReportInterval.setStatus('current')
if mibBuilder.loadTexts: hpnicfMultCDRReportInterval.setDescription('Configure the multicast CDR report-interval. Unit: second.')
hpnicfMultCDRCacheLimit = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfMultCDRCacheLimit.setStatus('current')
if mibBuilder.loadTexts: hpnicfMultCDRCacheLimit.setDescription('Configure the multicast CDR cache-limit.')
hpnicfMultCDRRecordDelay = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfMultCDRRecordDelay.setStatus('current')
if mibBuilder.loadTexts: hpnicfMultCDRRecordDelay.setDescription('Configure the multicast CDR record-delay. Unit: second')
hpnicfMultCDRRecordSend = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("send", 1), ("caching", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfMultCDRRecordSend.setStatus('current')
if mibBuilder.loadTexts: hpnicfMultCDRRecordSend.setDescription('Send record at once.')
hpnicfMultUserOnlineInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2), )
if mibBuilder.loadTexts: hpnicfMultUserOnlineInfoTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfMultUserOnlineInfoTable.setDescription('Multicast user online information table.')
hpnicfMultUserOnlineInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-MCDR-MIB", "hpnicfMultUserRecordID"))
if mibBuilder.loadTexts: hpnicfMultUserOnlineInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfMultUserOnlineInfoEntry.setDescription('The entry of multicast user online information table.')
hpnicfMultUserRecordID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfMultUserRecordID.setStatus('current')
if mibBuilder.loadTexts: hpnicfMultUserRecordID.setDescription('The index of online record.')
hpnicfMultUserSubIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMultUserSubIfIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfMultUserSubIfIndex.setDescription('The index of sub-interface which is active. If the value is zero, hpnicfMultUserSubIfIndex should be ignored.')
hpnicfMultUserVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 3), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMultUserVlanID.setStatus('current')
if mibBuilder.loadTexts: hpnicfMultUserVlanID.setDescription('The ID of VLAN in which the user joined the multicast group.')
hpnicfMultUserJoinGAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMultUserJoinGAddrType.setStatus('current')
if mibBuilder.loadTexts: hpnicfMultUserJoinGAddrType.setDescription('Type of the multicast group IP address.')
hpnicfMultUserJoinGAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMultUserJoinGAddr.setStatus('current')
if mibBuilder.loadTexts: hpnicfMultUserJoinGAddr.setDescription('The multicast group address which the user joined.')
hpnicfMultUserJoinSAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 6), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMultUserJoinSAddrType.setStatus('current')
if mibBuilder.loadTexts: hpnicfMultUserJoinSAddrType.setDescription('Type of the multicast source IP address.')
hpnicfMultUserJoinSAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 7), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMultUserJoinSAddr.setStatus('current')
if mibBuilder.loadTexts: hpnicfMultUserJoinSAddr.setDescription("The multicast source address which the user joined. If the value is '0.0.0.0'(IPv4) or '::'(IPv6), hpnicfMultUserJoinSAddr should be ignored.")
hpnicfMultUserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("preview", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMultUserStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfMultUserStatus.setDescription('The current status of user. permit - user in permit status. preview - user in preview status.')
hpnicfMultUserJoinTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 9), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMultUserJoinTime.setStatus('current')
if mibBuilder.loadTexts: hpnicfMultUserJoinTime.setDescription('The time when the user joined the multicast group.')
hpnicfMultUserPreviewTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMultUserPreviewTimes.setStatus('current')
if mibBuilder.loadTexts: hpnicfMultUserPreviewTimes.setDescription('The times of multicast preview which the user joined. If hpnicfMultUserStatus is not preview, hpnicfMultUserPreviewTimes should be ignored.')
hpnicfMultUserPreviewRemain = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMultUserPreviewRemain.setStatus('current')
if mibBuilder.loadTexts: hpnicfMultUserPreviewRemain.setDescription('The remanent time slice of multicast preview which the user joined. If hpnicfMultUserStatus is not preview, hpnicfMultUserPreviewRemain should be ignored.')
mibBuilder.exportSymbols("HPN-ICF-MCDR-MIB", hpnicfMultUserJoinTime=hpnicfMultUserJoinTime, hpnicfMultUserRecordID=hpnicfMultUserRecordID, hpnicfMultUserJoinGAddr=hpnicfMultUserJoinGAddr, hpnicfMultCDRRecordSend=hpnicfMultCDRRecordSend, hpnicfMultUserOnlineInfoEntry=hpnicfMultUserOnlineInfoEntry, hpnicfMultUserVlanID=hpnicfMultUserVlanID, hpnicfMultUserOnlineInfoTable=hpnicfMultUserOnlineInfoTable, hpnicfMultCDRRecordDelay=hpnicfMultCDRRecordDelay, hpnicfMultUserJoinGAddrType=hpnicfMultUserJoinGAddrType, hpnicfMultCDRCacheLimit=hpnicfMultCDRCacheLimit, hpnicfMultUserJoinSAddr=hpnicfMultUserJoinSAddr, hpnicfMultUserPreviewTimes=hpnicfMultUserPreviewTimes, PYSNMP_MODULE_ID=hpnicfMultCDR, hpnicfMultCDRReportInterval=hpnicfMultCDRReportInterval, hpnicfMultCDR=hpnicfMultCDR, hpnicfMultUserStatus=hpnicfMultUserStatus, hpnicfMultUserJoinSAddrType=hpnicfMultUserJoinSAddrType, hpnicfMultUserPreviewRemain=hpnicfMultUserPreviewRemain, hpnicfMultUserSubIfIndex=hpnicfMultUserSubIfIndex, hpnicfMultCDRStatus=hpnicfMultCDRStatus, hpnicfMultCDRCfgObject=hpnicfMultCDRCfgObject)
