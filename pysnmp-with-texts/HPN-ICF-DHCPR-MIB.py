#
# PySNMP MIB module HPN-ICF-DHCPR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-DHCPR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:37:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
hpnicfRhw, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfRhw")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
IpAddress, Bits, Unsigned32, NotificationType, MibIdentifier, Integer32, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, TimeTicks, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "Unsigned32", "NotificationType", "MibIdentifier", "Integer32", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "TimeTicks", "Counter64", "ModuleIdentity")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
hpnicfDHCPRelayMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1))
hpnicfDHCPRelayMib.setRevisions(('2003-02-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfDHCPRelayMib.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hpnicfDHCPRelayMib.setLastUpdated('200303010000Z')
if mibBuilder.loadTexts: hpnicfDHCPRelayMib.setOrganization('')
if mibBuilder.loadTexts: hpnicfDHCPRelayMib.setContactInfo('')
if mibBuilder.loadTexts: hpnicfDHCPRelayMib.setDescription('This MIB describes objects used for managing DHCP relay.')
hpnicfDHCPRelayMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1))
hpnicfDHCPRIPTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 1), )
if mibBuilder.loadTexts: hpnicfDHCPRIPTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRIPTable.setDescription('A table for configuring ip addresses for DHCP relay')
hpnicfDHCPRIPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-DHCPR-MIB", "hpnicfDHCPRIPAddr"))
if mibBuilder.loadTexts: hpnicfDHCPRIPEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRIPEntry.setDescription('An entry for configuring ip addresses for DHCP relay')
hpnicfDHCPRIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDHCPRIPAddr.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRIPAddr.setDescription('Ip address for DHCP relay')
hpnicfDHCPRIPRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfDHCPRIPRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRIPRowStatus.setDescription('RowStatus. Three actions are used: active, createAndGo, destroy')
hpnicfDHCPRSeletAllocateModeTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 2), )
if mibBuilder.loadTexts: hpnicfDHCPRSeletAllocateModeTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRSeletAllocateModeTable.setDescription('A table for selecting allocation mode of dhcp service')
hpnicfDHCPRSeletAllocateModeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfDHCPRSeletAllocateModeEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRSeletAllocateModeEntry.setDescription('An entry for configuring the allocation mode of DHCP service')
hpnicfDHCPRSelectAllocateMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("global", 0), ("interface", 1), ("relay", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDHCPRSelectAllocateMode.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRSelectAllocateMode.setDescription('Allocation mode of DHCP service')
hpnicfDHCPRelayCycleStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("on", 0), ("off", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDHCPRelayCycleStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRelayCycleStatus.setDescription('Status of DHCP relay cycle mode')
hpnicfDHCPRRxBadPktNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDHCPRRxBadPktNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRRxBadPktNum.setDescription('The total number of the bad packets received by DHCP relay')
hpnicfDHCPRRxServerPktNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDHCPRRxServerPktNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRRxServerPktNum.setDescription('The total number of the packets received from DHCP servers by DHCP relay module')
hpnicfDHCPRTxServerPktNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDHCPRTxServerPktNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRTxServerPktNum.setDescription('The total number of the packets transmited to DHCP servers by DHCP relay module')
hpnicfDHCPRRxClientPktNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDHCPRRxClientPktNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRRxClientPktNum.setDescription('The total number of the packets received form DHCP clients by DHCP relay')
hpnicfDHCPRTxClientPktNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDHCPRTxClientPktNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRTxClientPktNum.setDescription('The total number of the brodcast packets transmited to DHCP clients by DHCP relay')
hpnicfDHCPRTxClientUniPktNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDHCPRTxClientUniPktNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRTxClientUniPktNum.setDescription('The total number of the unicast packets received form DHCP clients by DHCP relay')
hpnicfDHCPRTxClientBroPktNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDHCPRTxClientBroPktNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRTxClientBroPktNum.setDescription('The total number of the brodcast packets received form DHCP clients by DHCP relay')
hpnicfDHCPRelayDiscoverPktNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDHCPRelayDiscoverPktNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRelayDiscoverPktNum.setDescription('The total number of the DHCP Discover packets handled by DHCP relay')
hpnicfDHCPRelayRequestPktNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDHCPRelayRequestPktNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRelayRequestPktNum.setDescription('The total number of the DHCP Request packets handled by DHCP relay')
hpnicfDHCPRelayDeclinePktNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDHCPRelayDeclinePktNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRelayDeclinePktNum.setDescription('The total number of the DHCP Decline packets handled by DHCP relay')
hpnicfDHCPRelayReleasePktNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDHCPRelayReleasePktNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRelayReleasePktNum.setDescription('The total number of the DHCP Release packets handled by DHCP relay')
hpnicfDHCPRelayInformPktNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDHCPRelayInformPktNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRelayInformPktNum.setDescription('The total number of the DHCP Inform packets handled by DHCP relay')
hpnicfDHCPRelayOfferPktNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDHCPRelayOfferPktNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRelayOfferPktNum.setDescription('The total number of the DHCP Offer packets handled by DHCP server')
hpnicfDHCPRelayAckPktNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDHCPRelayAckPktNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRelayAckPktNum.setDescription('The total number of the DHCP Ack packets handled by DHCP relay')
hpnicfDHCPRelayNakPktNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDHCPRelayNakPktNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRelayNakPktNum.setDescription('The total number of the DHCP Nak packets handled by DHCP relay')
hpnicfDHCPRelayStatisticsReset = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("invalid", 0), ("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDHCPRelayStatisticsReset.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRelayStatisticsReset.setDescription('Reset the above statictics information of handled packets by DHCP relay')
hpnicfDHCPRelayMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 2))
hpnicfDHCPRelayMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 2, 1))
hpnicfDHCPRelayMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 2, 2))
hpnicfDHCPRelayMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 2, 2, 1)).setObjects(("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRIPAddr"), ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRIPRowStatus"), ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRSelectAllocateMode"), ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRelayCycleStatus"), ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRRxBadPktNum"), ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRRxServerPktNum"), ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRTxServerPktNum"), ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRRxClientPktNum"), ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRTxClientPktNum"), ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRTxClientUniPktNum"), ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRTxClientBroPktNum"), ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRelayDiscoverPktNum"), ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRelayRequestPktNum"), ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRelayDeclinePktNum"), ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRelayReleasePktNum"), ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRelayInformPktNum"), ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRelayOfferPktNum"), ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRelayAckPktNum"), ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRelayNakPktNum"), ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRelayStatisticsReset"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDHCPRelayMIBGroup = hpnicfDHCPRelayMIBGroup.setStatus('current')
if mibBuilder.loadTexts: hpnicfDHCPRelayMIBGroup.setDescription('The basic collection of objects providing management of DHCP realy.')
mibBuilder.exportSymbols("HPN-ICF-DHCPR-MIB", hpnicfDHCPRelayOfferPktNum=hpnicfDHCPRelayOfferPktNum, hpnicfDHCPRelayMIBGroup=hpnicfDHCPRelayMIBGroup, hpnicfDHCPRIPEntry=hpnicfDHCPRIPEntry, hpnicfDHCPRelayDiscoverPktNum=hpnicfDHCPRelayDiscoverPktNum, hpnicfDHCPRelayMib=hpnicfDHCPRelayMib, hpnicfDHCPRRxClientPktNum=hpnicfDHCPRRxClientPktNum, hpnicfDHCPRelayDeclinePktNum=hpnicfDHCPRelayDeclinePktNum, hpnicfDHCPRelayMIBCompliances=hpnicfDHCPRelayMIBCompliances, hpnicfDHCPRelayReleasePktNum=hpnicfDHCPRelayReleasePktNum, hpnicfDHCPRelayInformPktNum=hpnicfDHCPRelayInformPktNum, hpnicfDHCPRelayStatisticsReset=hpnicfDHCPRelayStatisticsReset, hpnicfDHCPRRxServerPktNum=hpnicfDHCPRRxServerPktNum, hpnicfDHCPRSeletAllocateModeTable=hpnicfDHCPRSeletAllocateModeTable, hpnicfDHCPRIPTable=hpnicfDHCPRIPTable, hpnicfDHCPRTxClientBroPktNum=hpnicfDHCPRTxClientBroPktNum, hpnicfDHCPRTxServerPktNum=hpnicfDHCPRTxServerPktNum, hpnicfDHCPRelayMibObject=hpnicfDHCPRelayMibObject, hpnicfDHCPRIPRowStatus=hpnicfDHCPRIPRowStatus, hpnicfDHCPRelayMIBConformance=hpnicfDHCPRelayMIBConformance, hpnicfDHCPRTxClientUniPktNum=hpnicfDHCPRTxClientUniPktNum, hpnicfDHCPRSelectAllocateMode=hpnicfDHCPRSelectAllocateMode, hpnicfDHCPRelayCycleStatus=hpnicfDHCPRelayCycleStatus, hpnicfDHCPRTxClientPktNum=hpnicfDHCPRTxClientPktNum, hpnicfDHCPRSeletAllocateModeEntry=hpnicfDHCPRSeletAllocateModeEntry, PYSNMP_MODULE_ID=hpnicfDHCPRelayMib, hpnicfDHCPRelayAckPktNum=hpnicfDHCPRelayAckPktNum, hpnicfDHCPRRxBadPktNum=hpnicfDHCPRRxBadPktNum, hpnicfDHCPRIPAddr=hpnicfDHCPRIPAddr, hpnicfDHCPRelayMIBGroups=hpnicfDHCPRelayMIBGroups, hpnicfDHCPRelayRequestPktNum=hpnicfDHCPRelayRequestPktNum, hpnicfDHCPRelayNakPktNum=hpnicfDHCPRelayNakPktNum)
