#
# PySNMP MIB module STATICFDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STATICFDB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:11:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, ObjectIdentity, TimeTicks, Gauge32, Unsigned32, MibIdentifier, Bits, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "ObjectIdentity", "TimeTicks", "Gauge32", "Unsigned32", "MibIdentifier", "Bits", "Integer32", "Counter64")
MacAddress, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString", "RowStatus")
swStaticFdbMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 70))
if mibBuilder.loadTexts: swStaticFdbMIB.setLastUpdated('0811180000Z')
if mibBuilder.loadTexts: swStaticFdbMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: swStaticFdbMIB.setContactInfo('http://support.dlink.com')
if mibBuilder.loadTexts: swStaticFdbMIB.setDescription('This MIB defines a Table for Static Fdb.')
swStaticFdbMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 70, 1))
swStaticFdbMgmtTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 70, 1, 1), )
if mibBuilder.loadTexts: swStaticFdbMgmtTable.setStatus('current')
if mibBuilder.loadTexts: swStaticFdbMgmtTable.setDescription('A table that contains the information of each static fdb.')
swStaticFdbMgmtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 70, 1, 1, 1), ).setIndexNames((0, "STATICFDB-MIB", "swStaticFdbMgmtVlanID"), (0, "STATICFDB-MIB", "swStaticFdbMgmtMacAddr"))
if mibBuilder.loadTexts: swStaticFdbMgmtEntry.setStatus('current')
if mibBuilder.loadTexts: swStaticFdbMgmtEntry.setDescription('A list of information for each static fdb.')
swStaticFdbMgmtVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 70, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStaticFdbMgmtVlanID.setStatus('current')
if mibBuilder.loadTexts: swStaticFdbMgmtVlanID.setDescription('The VLAN ID of the static fdb.')
swStaticFdbMgmtMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 70, 1, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStaticFdbMgmtMacAddr.setStatus('current')
if mibBuilder.loadTexts: swStaticFdbMgmtMacAddr.setDescription('The MAC address of the static fdb.')
swStaticFdbMgmtVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 70, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStaticFdbMgmtVlanName.setStatus('current')
if mibBuilder.loadTexts: swStaticFdbMgmtVlanName.setDescription('The VLAN name of the static fdb.')
swStaticFdbMgmtType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 70, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("self", 1), ("permanent", 2), ("permanentdrop", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swStaticFdbMgmtType.setStatus('current')
if mibBuilder.loadTexts: swStaticFdbMgmtType.setDescription("This object indicates the status of this entry. self(1) - This entry is currently in use by the device's MAC address, it can not be created. permanent(2) - This entry is currently in use and will remain so until after the next reset of the bridge, it can not be created. permanentdrop(3) - This entry will filter the packet with the specified MAC address as the source MAC or as the destination MAC. The entry is currently in use and will remain so after the next reboot of the bridge. The value of this object MUST be retained across reinitializations of the management system.")
swStaticFdbMgmtPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 70, 1, 1, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swStaticFdbMgmtPortNum.setStatus('current')
if mibBuilder.loadTexts: swStaticFdbMgmtPortNum.setDescription('The port number of the static fdb. Port 0 represents the CPU port. Port -1 represents all the all ports in The VLAN of the MAC filter entry.')
swStaticFdbMgmtRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 70, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swStaticFdbMgmtRowStatus.setStatus('current')
if mibBuilder.loadTexts: swStaticFdbMgmtRowStatus.setDescription('This object indicates the RowStatus of this entry.')
mibBuilder.exportSymbols("STATICFDB-MIB", swStaticFdbMIB=swStaticFdbMIB, swStaticFdbMgmtMacAddr=swStaticFdbMgmtMacAddr, PYSNMP_MODULE_ID=swStaticFdbMIB, swStaticFdbMgmtType=swStaticFdbMgmtType, swStaticFdbMgmtEntry=swStaticFdbMgmtEntry, swStaticFdbMgmtTable=swStaticFdbMgmtTable, swStaticFdbMgmtPortNum=swStaticFdbMgmtPortNum, swStaticFdbMgmtVlanID=swStaticFdbMgmtVlanID, swStaticFdbMgmt=swStaticFdbMgmt, swStaticFdbMgmtVlanName=swStaticFdbMgmtVlanName, swStaticFdbMgmtRowStatus=swStaticFdbMgmtRowStatus)
