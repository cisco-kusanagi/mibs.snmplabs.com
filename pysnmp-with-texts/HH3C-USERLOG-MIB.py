#
# PySNMP MIB module HH3C-USERLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-USERLOG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:30:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
hh3cRhw, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cRhw")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, Unsigned32, Gauge32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, IpAddress, Counter32, iso, NotificationType, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "Gauge32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "IpAddress", "Counter32", "iso", "NotificationType", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3cUserLogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 18))
if mibBuilder.loadTexts: hh3cUserLogMIB.setLastUpdated('200304100000Z')
if mibBuilder.loadTexts: hh3cUserLogMIB.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cUserLogMIB.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cUserLogMIB.setDescription('The HH3C-USERLOG-MIB contains objects to Manage configuration and Monitor running state for userlog feature.')
hh3cUserlogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1))
hh3cUserlogNatObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1))
hh3cUserlogNatVersion = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogNatVersion.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogNatVersion.setDescription('NAT LOG version. Currently only version 1 is developed.')
hh3cUserlogNatSyslog = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogNatSyslog.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogNatSyslog.setDescription(' NAT LOG format. If 1, LOG format is sysLog. If 0, LOG format is UDP packet. UDP packet is the default format, and is recommended. ')
hh3cUserlogNatSourceIP = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogNatSourceIP.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogNatSourceIP.setDescription('The Source IP address of NAT LOG UDP packet.')
hh3cUserlogNatFlowBegin = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogNatFlowBegin.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogNatFlowBegin.setDescription(' Log the NAT flow when it is created. If 1, this function is enabled. If 0, this function is disabled. This function will be used when real-time monitor required. ')
hh3cUserlogNatActiveTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogNatActiveTime.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogNatActiveTime.setDescription(' The active time for long-time existed NAT flow. Unit: minute. Range: 10 minutes ~ 120 minutes. When setting it, NAT flow can be logged after an interval of active time. This function will be used when real-time monitor required. The default value 0 means real-time monitor function is disabled. ')
hh3cUserlogNatSlotCfgInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6), )
if mibBuilder.loadTexts: hh3cUserlogNatSlotCfgInfoTable.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogNatSlotCfgInfoTable.setDescription('A table of NAT LOG configuration information for the specified slot.')
hh3cUserlogNatSlotCfgInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6, 1), ).setIndexNames((0, "HH3C-USERLOG-MIB", "hh3cUserlogNatCfgSlotNumber"))
if mibBuilder.loadTexts: hh3cUserlogNatSlotCfgInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogNatSlotCfgInfoEntry.setDescription('NAT LOG Configuration Information Entry for a slot.')
hh3cUserlogNatCfgSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogNatCfgSlotNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogNatCfgSlotNumber.setDescription('Slot number. Specify which slot is configured with NAT LOG. ')
hh3cUserlogNatEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogNatEnable.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogNatEnable.setDescription(' The NAT LOG feature Enable status. If 1, NAT LOG is enbled. If 0, NAT LOG is disabled. ')
hh3cUserlogNatAclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogNatAclNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogNatAclNumber.setDescription(' Access-list number. The value 0 means no ACL is specified. Only when NAT LOG is enabled, can ACL be configured. Only NAT flow which match the ACL will be logged. ')
hh3cUserlogNatHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogNatHostAddress.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogNatHostAddress.setDescription('The IP address of NAT LOG server. ')
hh3cUserlogNatUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogNatUdpPort.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogNatUdpPort.setDescription('The UDP Port Number of NAT LOG UDP packet.')
hh3cUserlogNatSlotRunInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7), )
if mibBuilder.loadTexts: hh3cUserlogNatSlotRunInfoTable.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogNatSlotRunInfoTable.setDescription('A table of NAT LOG running information for the specified slot.')
hh3cUserlogNatSlotRunInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1), ).setIndexNames((0, "HH3C-USERLOG-MIB", "hh3cUserlogNatRunSlotNumber"))
if mibBuilder.loadTexts: hh3cUserlogNatSlotRunInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogNatSlotRunInfoEntry.setDescription('NAT LOG Running Information Entry for a slot.')
hh3cUserlogNatRunSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogNatRunSlotNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogNatRunSlotNumber.setDescription('Slot number. Specify on which slot the NAT LOG statistics displayed.')
hh3cUserlogNatTotalEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogNatTotalEntries.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogNatTotalEntries.setDescription('The total number of NAT flow entries which are logged.')
hh3cUserlogNatTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogNatTotalPackets.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogNatTotalPackets.setDescription('The total number of NAT LOG UDP packets generated by the router.')
hh3cUserlogNatFailedEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogNatFailedEntries.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogNatFailedEntries.setDescription('The total number of NAT flow entries failed in outputting.')
hh3cUserlogNatFailedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogNatFailedPackets.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogNatFailedPackets.setDescription('The total number of NAT LOG UDP packets failed in outputting.')
hh3cUserlogNatClearRunStat = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 1, 7, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogNatClearRunStat.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogNatClearRunStat.setDescription(' Clear the running statistics for NAT LOG. Write-only. If 1, the running statistics for NAT LOG is resetted. Other value is invalid. ')
hh3cUserlogFlowObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2))
hh3cUserlogFlowVersion = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogFlowVersion.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogFlowVersion.setDescription('BAS FLOW LOG version. Currently only version 1 is developed.')
hh3cUserlogFlowSyslog = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogFlowSyslog.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogFlowSyslog.setDescription(' BAS FLOW LOG format. If 1, LOG format is sysLog. If 0, LOG format is UDP packet. UDP packet is the default format, and is recommended. ')
hh3cUserlogFlowSourceIP = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogFlowSourceIP.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogFlowSourceIP.setDescription('The Source IP address of BAS FLOW LOG UDP packet.')
hh3cUserlogFlowFlowBegin = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogFlowFlowBegin.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogFlowFlowBegin.setDescription(' Log the BAS flow when it is created. If 1, this function is enabled. If 0, this function is disabled. This function will be used when real-time monitor required. ')
hh3cUserlogFlowActiveTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogFlowActiveTime.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogFlowActiveTime.setDescription(' The active time for long-time existed BAS flow. Unit: minute. Range: 10 minutes ~ 120 minutes. When setting it, BAS flow can be logged after an internal of active time. This function will be used when real-time monitor required. The default value 0 means real-time monitor function is disabled. ')
hh3cUserlogFlowSlotCfgInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6), )
if mibBuilder.loadTexts: hh3cUserlogFlowSlotCfgInfoTable.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogFlowSlotCfgInfoTable.setDescription('A table of BAS FLOW LOG configuration information for the specified slot.')
hh3cUserlogFlowSlotCfgInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6, 1), ).setIndexNames((0, "HH3C-USERLOG-MIB", "hh3cUserlogFlowCfgSlotNumber"))
if mibBuilder.loadTexts: hh3cUserlogFlowSlotCfgInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogFlowSlotCfgInfoEntry.setDescription('BAS FLOW LOG Configuration Information Entry for a slot.')
hh3cUserlogFlowCfgSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogFlowCfgSlotNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogFlowCfgSlotNumber.setDescription('Slot number. Specify which slot is configured with BAS FLOW LOG.')
hh3cUserlogFlowEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogFlowEnable.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogFlowEnable.setDescription(' The BAS FLOW LOG feature Enable status. If 1, BAS FLOW LOG is enbled. If 0, BAS FLOW LOG is disabled. ')
hh3cUserlogFlowAclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogFlowAclNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogFlowAclNumber.setDescription(' Access-list number. The value 0 means no ACL is specified. Only when BAS FLOW LOG is enabled, can ACL be configured. Only BAS flow which match the ACL will be logged. ')
hh3cUserlogFlowHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogFlowHostAddress.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogFlowHostAddress.setDescription('The IP address of BAS FLOW LOG server. ')
hh3cUserlogFlowUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogFlowUdpPort.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogFlowUdpPort.setDescription('The UDP Port Number of BAS FLOW LOG UDP packet.')
hh3cUserlogFlowSlotRunInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7), )
if mibBuilder.loadTexts: hh3cUserlogFlowSlotRunInfoTable.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogFlowSlotRunInfoTable.setDescription('A table of BAS FLOW LOG running information for the specified slot.')
hh3cUserlogFlowSlotRunInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1), ).setIndexNames((0, "HH3C-USERLOG-MIB", "hh3cUserlogFlowRunSlotNumber"))
if mibBuilder.loadTexts: hh3cUserlogFlowSlotRunInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogFlowSlotRunInfoEntry.setDescription('Running Information Entry for a slot.')
hh3cUserlogFlowRunSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogFlowRunSlotNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogFlowRunSlotNumber.setDescription('Slot number. Specify on which slot the BAS FLOW LOG statistics displayed.')
hh3cUserlogFlowTotalEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogFlowTotalEntries.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogFlowTotalEntries.setDescription('The total number of BAS FLOW Entries which are logged.')
hh3cUserlogFlowTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogFlowTotalPackets.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogFlowTotalPackets.setDescription('The total number of FLOW LOG UDP packet generated by the router.')
hh3cUserlogFlowFailedEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogFlowFailedEntries.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogFlowFailedEntries.setDescription('The total number of BAS FLOW entries failed in outputting. ')
hh3cUserlogFlowFailedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogFlowFailedPackets.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogFlowFailedPackets.setDescription('The total number of BAS FLOW LOG UDP packet failed in outputting.')
hh3cUserlogFlowClearRunStat = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 2, 7, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogFlowClearRunStat.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogFlowClearRunStat.setDescription(' Clear the running statistics for FLOW LOG. Write-only. If 1, the running statistics for FLOW LOG is resetted. Other value is invalid. ')
hh3cUserlogAccessObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3))
hh3cUserlogAccessVersion = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogAccessVersion.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogAccessVersion.setDescription('BAS ACCESS LOG version. Currently only version 1 is developed.')
hh3cUserlogAccessSyslog = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogAccessSyslog.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogAccessSyslog.setDescription(' BAS ACCESS LOG format. If 1, LOG format is sysLog; If 0, LOG format is UDP packet. UDP packet is the default format, and is recommended. ')
hh3cUserlogAccessSourceIP = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogAccessSourceIP.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogAccessSourceIP.setDescription('The Source IP address of BAS ACCESS LOG UDP packet.')
hh3cUserlogAccessSlotCfgInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 4), )
if mibBuilder.loadTexts: hh3cUserlogAccessSlotCfgInfoTable.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogAccessSlotCfgInfoTable.setDescription('A table of BAS ACCESS LOG configuration information for the specified slot.')
hh3cUserlogAccessSlotCfgInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 4, 1), ).setIndexNames((0, "HH3C-USERLOG-MIB", "hh3cUserlogAccessCfgSlotNumber"))
if mibBuilder.loadTexts: hh3cUserlogAccessSlotCfgInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogAccessSlotCfgInfoEntry.setDescription('BAS ACCESS LOG Configuration Information Entry for a slot.')
hh3cUserlogAccessCfgSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogAccessCfgSlotNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogAccessCfgSlotNumber.setDescription('Slot number. Specify which slot is configured with BAS ACCESS LOG.')
hh3cUserlogAccessEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 4, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogAccessEnable.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogAccessEnable.setDescription(' The BAS ACCESS LOG feature Enable status. If 1, BAS ACCESS LOG is enbled. If 0, BAS ACCESS LOG is disabled. ')
hh3cUserlogAccessHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 4, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogAccessHostAddress.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogAccessHostAddress.setDescription('The IP address of BAS ACCESS LOG server.')
hh3cUserlogAccessUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogAccessUdpPort.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogAccessUdpPort.setDescription('The UDP Port Number of BAS ACCESS LOG UDP packet.')
hh3cUserlogAccessSlotRunInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5), )
if mibBuilder.loadTexts: hh3cUserlogAccessSlotRunInfoTable.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogAccessSlotRunInfoTable.setDescription('A table of BAS ACCESS LOG running information for the specified slot.')
hh3cUserlogAccessSlotRunInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1), ).setIndexNames((0, "HH3C-USERLOG-MIB", "hh3cUserlogAccessRunSlotNumber"))
if mibBuilder.loadTexts: hh3cUserlogAccessSlotRunInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogAccessSlotRunInfoEntry.setDescription('Running Information Entry for a slot.')
hh3cUserlogAccessRunSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogAccessRunSlotNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogAccessRunSlotNumber.setDescription('Slot number. Specify on which slot the BAS ACCESS LOG statistics displayed.')
hh3cUserlogAccessTotalEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogAccessTotalEntries.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogAccessTotalEntries.setDescription('The total number of BAS ACCESS Records which are logged.')
hh3cUserlogAccessTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogAccessTotalPackets.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogAccessTotalPackets.setDescription('The total number of ACCESS LOG UDP packet generated by the router.')
hh3cUserlogAccessFailedEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogAccessFailedEntries.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogAccessFailedEntries.setDescription('The total number of BAS ACCESS entries failed in outputting.')
hh3cUserlogAccessFailedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUserlogAccessFailedPackets.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogAccessFailedPackets.setDescription('The total number of BAS ACCESS LOG UDP packet failed in outputting.')
hh3cUserlogAccessClearRunStat = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 18, 1, 3, 5, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUserlogAccessClearRunStat.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogAccessClearRunStat.setDescription(' Clear the running statistics for ACCESS LOG. Write-only. If 1, the running statistics for ACCESS LOG is resetted. Other value is invalid. ')
hh3cUserlogNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 18, 2))
hh3cUserlogConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 18, 3))
hh3cUserlogCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 18, 3, 1))
hh3cUserlogCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25506, 8, 18, 3, 1, 1)).setObjects(("HH3C-USERLOG-MIB", "hh3cUserlogMandatoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cUserlogCompliance = hh3cUserlogCompliance.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogCompliance.setDescription('The compliance statement for entities which implement the H3C Userlog mib.')
hh3cUserlogGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 18, 3, 2))
hh3cUserlogMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 8, 18, 3, 2, 1)).setObjects(("HH3C-USERLOG-MIB", "hh3cUserlogNatEnable"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatHostAddress"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatUdpPort"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowEnable"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowHostAddress"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowUdpPort"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessEnable"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessHostAddress"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessUdpPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cUserlogMandatoryGroup = hh3cUserlogMandatoryGroup.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogMandatoryGroup.setDescription('A collection of objects providing mandatory Userlog information.')
hh3cUserlogConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 8, 18, 3, 2, 2)).setObjects(("HH3C-USERLOG-MIB", "hh3cUserlogNatVersion"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatSyslog"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatSourceIP"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatFlowBegin"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatActiveTime"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatCfgSlotNumber"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatEnable"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatAclNumber"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatHostAddress"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatUdpPort"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowVersion"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowSyslog"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowSourceIP"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowFlowBegin"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowActiveTime"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowCfgSlotNumber"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowEnable"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowAclNumber"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowHostAddress"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowUdpPort"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessVersion"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessSyslog"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessSourceIP"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessCfgSlotNumber"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessEnable"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessHostAddress"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessUdpPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cUserlogConfigGroup = hh3cUserlogConfigGroup.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogConfigGroup.setDescription('All configurable parameters of Userlog feature.')
hh3cUserlogInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 8, 18, 3, 2, 3)).setObjects(("HH3C-USERLOG-MIB", "hh3cUserlogNatTotalEntries"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatTotalPackets"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatFailedEntries"), ("HH3C-USERLOG-MIB", "hh3cUserlogNatFailedPackets"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowTotalEntries"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowTotalPackets"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowFailedEntries"), ("HH3C-USERLOG-MIB", "hh3cUserlogFlowFailedPackets"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessTotalEntries"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessTotalPackets"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessFailedEntries"), ("HH3C-USERLOG-MIB", "hh3cUserlogAccessFailedPackets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cUserlogInfoGroup = hh3cUserlogInfoGroup.setStatus('current')
if mibBuilder.loadTexts: hh3cUserlogInfoGroup.setDescription('All running information of Userlog feature.')
mibBuilder.exportSymbols("HH3C-USERLOG-MIB", hh3cUserlogNatFailedPackets=hh3cUserlogNatFailedPackets, hh3cUserlogNatActiveTime=hh3cUserlogNatActiveTime, hh3cUserlogFlowSlotCfgInfoTable=hh3cUserlogFlowSlotCfgInfoTable, hh3cUserlogFlowSyslog=hh3cUserlogFlowSyslog, hh3cUserlogFlowTotalPackets=hh3cUserlogFlowTotalPackets, hh3cUserlogAccessHostAddress=hh3cUserlogAccessHostAddress, hh3cUserlogNatVersion=hh3cUserlogNatVersion, hh3cUserlogAccessTotalEntries=hh3cUserlogAccessTotalEntries, hh3cUserlogNatRunSlotNumber=hh3cUserlogNatRunSlotNumber, hh3cUserlogConfigGroup=hh3cUserlogConfigGroup, hh3cUserlogNatHostAddress=hh3cUserlogNatHostAddress, hh3cUserlogFlowActiveTime=hh3cUserlogFlowActiveTime, hh3cUserlogNatFlowBegin=hh3cUserlogNatFlowBegin, hh3cUserlogAccessEnable=hh3cUserlogAccessEnable, hh3cUserlogAccessSourceIP=hh3cUserlogAccessSourceIP, hh3cUserlogAccessFailedPackets=hh3cUserlogAccessFailedPackets, hh3cUserlogNatClearRunStat=hh3cUserlogNatClearRunStat, hh3cUserlogAccessSyslog=hh3cUserlogAccessSyslog, hh3cUserlogNatSourceIP=hh3cUserlogNatSourceIP, hh3cUserlogNatTotalEntries=hh3cUserlogNatTotalEntries, hh3cUserlogFlowEnable=hh3cUserlogFlowEnable, hh3cUserlogNatSlotRunInfoEntry=hh3cUserlogNatSlotRunInfoEntry, hh3cUserlogFlowFailedPackets=hh3cUserlogFlowFailedPackets, hh3cUserlogFlowSlotRunInfoEntry=hh3cUserlogFlowSlotRunInfoEntry, hh3cUserlogAccessCfgSlotNumber=hh3cUserlogAccessCfgSlotNumber, hh3cUserlogConformance=hh3cUserlogConformance, hh3cUserlogAccessSlotRunInfoEntry=hh3cUserlogAccessSlotRunInfoEntry, hh3cUserlogAccessVersion=hh3cUserlogAccessVersion, hh3cUserlogCompliances=hh3cUserlogCompliances, hh3cUserlogAccessObjects=hh3cUserlogAccessObjects, hh3cUserlogAccessClearRunStat=hh3cUserlogAccessClearRunStat, hh3cUserlogFlowVersion=hh3cUserlogFlowVersion, hh3cUserlogFlowSourceIP=hh3cUserlogFlowSourceIP, hh3cUserlogAccessUdpPort=hh3cUserlogAccessUdpPort, hh3cUserlogNotifications=hh3cUserlogNotifications, hh3cUserlogNatEnable=hh3cUserlogNatEnable, hh3cUserlogFlowSlotCfgInfoEntry=hh3cUserlogFlowSlotCfgInfoEntry, hh3cUserLogMIB=hh3cUserLogMIB, hh3cUserlogFlowFailedEntries=hh3cUserlogFlowFailedEntries, hh3cUserlogAccessFailedEntries=hh3cUserlogAccessFailedEntries, hh3cUserlogMandatoryGroup=hh3cUserlogMandatoryGroup, hh3cUserlogFlowTotalEntries=hh3cUserlogFlowTotalEntries, hh3cUserlogAccessTotalPackets=hh3cUserlogAccessTotalPackets, hh3cUserlogNatObjects=hh3cUserlogNatObjects, hh3cUserlogAccessRunSlotNumber=hh3cUserlogAccessRunSlotNumber, PYSNMP_MODULE_ID=hh3cUserLogMIB, hh3cUserlogFlowHostAddress=hh3cUserlogFlowHostAddress, hh3cUserlogAccessSlotRunInfoTable=hh3cUserlogAccessSlotRunInfoTable, hh3cUserlogGroups=hh3cUserlogGroups, hh3cUserlogNatCfgSlotNumber=hh3cUserlogNatCfgSlotNumber, hh3cUserlogFlowUdpPort=hh3cUserlogFlowUdpPort, hh3cUserlogObjects=hh3cUserlogObjects, hh3cUserlogNatSlotRunInfoTable=hh3cUserlogNatSlotRunInfoTable, hh3cUserlogFlowObjects=hh3cUserlogFlowObjects, hh3cUserlogFlowCfgSlotNumber=hh3cUserlogFlowCfgSlotNumber, hh3cUserlogNatFailedEntries=hh3cUserlogNatFailedEntries, hh3cUserlogNatUdpPort=hh3cUserlogNatUdpPort, hh3cUserlogFlowFlowBegin=hh3cUserlogFlowFlowBegin, hh3cUserlogFlowRunSlotNumber=hh3cUserlogFlowRunSlotNumber, hh3cUserlogNatSlotCfgInfoEntry=hh3cUserlogNatSlotCfgInfoEntry, hh3cUserlogFlowAclNumber=hh3cUserlogFlowAclNumber, hh3cUserlogNatAclNumber=hh3cUserlogNatAclNumber, hh3cUserlogCompliance=hh3cUserlogCompliance, hh3cUserlogAccessSlotCfgInfoEntry=hh3cUserlogAccessSlotCfgInfoEntry, hh3cUserlogAccessSlotCfgInfoTable=hh3cUserlogAccessSlotCfgInfoTable, hh3cUserlogFlowClearRunStat=hh3cUserlogFlowClearRunStat, hh3cUserlogNatSyslog=hh3cUserlogNatSyslog, hh3cUserlogFlowSlotRunInfoTable=hh3cUserlogFlowSlotRunInfoTable, hh3cUserlogInfoGroup=hh3cUserlogInfoGroup, hh3cUserlogNatTotalPackets=hh3cUserlogNatTotalPackets, hh3cUserlogNatSlotCfgInfoTable=hh3cUserlogNatSlotCfgInfoTable)
