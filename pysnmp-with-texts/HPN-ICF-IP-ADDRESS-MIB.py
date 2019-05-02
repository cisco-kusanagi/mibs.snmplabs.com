#
# PySNMP MIB module HPN-ICF-IP-ADDRESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-IP-ADDRESS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:39:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Gauge32, Integer32, Counter32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Unsigned32, TimeTicks, Counter64, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Integer32", "Counter32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Unsigned32", "TimeTicks", "Counter64", "IpAddress", "NotificationType")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hpnicfIpAddrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67))
hpnicfIpAddrMIB.setRevisions(('2005-11-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfIpAddrMIB.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hpnicfIpAddrMIB.setLastUpdated('200511220000Z')
if mibBuilder.loadTexts: hpnicfIpAddrMIB.setOrganization('')
if mibBuilder.loadTexts: hpnicfIpAddrMIB.setContactInfo('')
if mibBuilder.loadTexts: hpnicfIpAddrMIB.setDescription('The MIB module for managing IPv4 address.')
hpnicfIpAddressObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1))
hpnicfIpAddressConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1))
hpnicfIpAddrSetTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1), )
if mibBuilder.loadTexts: hpnicfIpAddrSetTable.setReference('RFC 2011')
if mibBuilder.loadTexts: hpnicfIpAddrSetTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrSetTable.setDescription("The table of address information is relevant to this entity's IPv4 addresses for setting. The address information that can be read and set in this table is a subset of the address information that can be read in hpnicfIpAddrReadTable and ipAddrTable in IP-MIB. This table is used to configure IPv4 addresses of an interface identified by hpnicfIpAddrSetIfIndex. When users create or delete an entry in this table, the agent also increases or reduces a corresponding entry in the hpnicfIpAddrReadTable and ipAddrTable in IP-MIB. When an interface which has been assigned IPv6 address is deleted, the agent also deletes the entry corresponding to the interface in this table and hpnicfIpAddrReadTable. All IPv4 addresses in this table will also show in ipAddrTable in IP-MIB. ")
hpnicfIpAddrSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrSetIfIndex"), (0, "HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrSetAddrType"), (0, "HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrSetAddr"))
if mibBuilder.loadTexts: hpnicfIpAddrSetEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrSetEntry.setDescription('Define the IPv4 address information. ')
hpnicfIpAddrSetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpnicfIpAddrSetIfIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrSetIfIndex.setDescription("The index value which uniquely identifies the interface to which this entry is applicable. The interface identified by a particular value of this index is the same interface as identified by the same value of RFC 1573's ifIndex. ")
hpnicfIpAddrSetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 2), InetAddressType())
if mibBuilder.loadTexts: hpnicfIpAddrSetAddrType.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrSetAddrType.setDescription("The IP address type to which this entry's address information pertains. The value must be ipv4. ")
hpnicfIpAddrSetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 3), InetAddress())
if mibBuilder.loadTexts: hpnicfIpAddrSetAddr.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrSetAddr.setDescription("The IPv4 address to which this entry's address information pertains. ")
hpnicfIpAddrSetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIpAddrSetMask.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrSetMask.setDescription('The subnet mask associated with the IPv4 address of this entry. The value of the mask is an IPv4 address with all the network bits set to 1 and all the hosts bits set to 0. ')
hpnicfIpAddrSetSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("assignedIp", 1))).clone('assignedIp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIpAddrSetSourceType.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrSetSourceType.setDescription('Indicate the type of source of the IPv4 address.')
hpnicfIpAddrSetCatalog = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("sub", 2))).clone('primary')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIpAddrSetCatalog.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrSetCatalog.setDescription('Indicate the category of the IPv4 address.')
hpnicfIpAddrSetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIpAddrSetRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrSetRowStatus.setDescription('This object is used to create a new row or delete an existing row in this table, only support active, createAndGo and destroy. ')
hpnicfIpAddrReadTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2), )
if mibBuilder.loadTexts: hpnicfIpAddrReadTable.setReference('RFC 2011')
if mibBuilder.loadTexts: hpnicfIpAddrReadTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrReadTable.setDescription("The table of address information is relevant to this entity's IP addresses for reading. This is the extension of the ipAddrTable in IP-MIB. All IPv4 addresses in this table will also show in ipAddrTable in IP-MIB. ")
hpnicfIpAddrReadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrReadIfIndex"), (0, "HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrReadAddrType"), (0, "HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrReadAddr"))
if mibBuilder.loadTexts: hpnicfIpAddrReadEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrReadEntry.setDescription('Define the IPv4 address information. ')
hpnicfIpAddrReadIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpnicfIpAddrReadIfIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrReadIfIndex.setDescription("The index value which uniquely identifies the interface to which this entry is applicable. The interface identified by a particular value of this index is the same interface as identified by the same value of RFC 1573's ifIndex. ")
hpnicfIpAddrReadAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1, 2), InetAddressType())
if mibBuilder.loadTexts: hpnicfIpAddrReadAddrType.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrReadAddrType.setDescription("The IP address type to which this entry's address information pertains. The value must be ipv4. ")
hpnicfIpAddrReadAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1, 3), InetAddress())
if mibBuilder.loadTexts: hpnicfIpAddrReadAddr.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrReadAddr.setDescription("The IPv4 address to which this entry's address information pertains. ")
hpnicfIpAddrReadMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpAddrReadMask.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrReadMask.setDescription('The subnet mask associated with the IPv4 address of this entry. The value of the mask is an IPv4 address with all the network bits set to 1 and all the hosts bits set to 0. ')
hpnicfIpAddrReadSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("assignedIp", 1), ("cluster", 2), ("dhcp", 3), ("bootp", 4), ("negotiate", 5), ("unnumbered", 6), ("vrrp", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpAddrReadSourceType.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrReadSourceType.setDescription('Indicate the type of source of the IPv4 address.')
hpnicfIpAddrReadCatalog = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("primary", 1), ("sub", 2), ("cluster", 3), ("vrrp", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfIpAddrReadCatalog.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrReadCatalog.setDescription('Indicate the category of the IPv4 address.')
hpnicfIpv4AddrTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 3), )
if mibBuilder.loadTexts: hpnicfIpv4AddrTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpv4AddrTable.setDescription('This table is used to configure primary IPv4 address of an interface identified by ifIndex.')
hpnicfIpv4AddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfIpv4AddrEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpv4AddrEntry.setDescription('Define the IPv4 address information. ')
hpnicfIpv4AddrAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 3, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIpv4AddrAddr.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpv4AddrAddr.setDescription("The IPv4 address to which this entry's address information pertains. ")
hpnicfIpv4AddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 3, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIpv4AddrMask.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpv4AddrMask.setDescription('The subnet mask associated with the IPv4 address of this entry. The value of the mask is an IPv4 address with all the network bits set to 1 and all the hosts bits set to 0. ')
hpnicfIpv4AddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIpv4AddrRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpv4AddrRowStatus.setDescription('This object is used to create a new row or delete an existing row in this table, only support active, notInService, createAndGo and destroy. ')
hpnicfIpAddrNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2))
hpnicfIpAddrNotifyScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 1))
hpnicfIpAddrNotifyIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIpAddrNotifyIfIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrNotifyIfIndex.setDescription('The IP address IfIndex of specified interface on the device.')
hpnicfIpAddrOldIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 1, 2), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIpAddrOldIpAddress.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrOldIpAddress.setDescription('The Old IP address of specified interface on the device.')
hpnicfIpAddrNewIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 1, 3), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIpAddrNewIpAddress.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrNewIpAddress.setDescription('The New IP address of specified interface on the device.')
hpnicfIpAddrFirstTrapTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 1, 4), TimeTicks()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfIpAddrFirstTrapTime.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddrFirstTrapTime.setDescription('Represents the first trap time.')
hpnicfIpAddrNotifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 2))
hpnicfIpAddrNotifyObjectsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 2, 0))
hpnicfIpAddressChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 2, 0, 1)).setObjects(("HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrNotifyIfIndex"), ("HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrOldIpAddress"), ("HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrNewIpAddress"), ("HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrFirstTrapTime"))
if mibBuilder.loadTexts: hpnicfIpAddressChangeNotify.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpAddressChangeNotify.setDescription('This notification will be generated when the IP address of interface is changed. The change maybe originate from NMS, DHCP server or administrator. This notification announces useful IP address change. So it is triggered by significative IP address change.')
mibBuilder.exportSymbols("HPN-ICF-IP-ADDRESS-MIB", hpnicfIpv4AddrTable=hpnicfIpv4AddrTable, hpnicfIpAddressConfig=hpnicfIpAddressConfig, hpnicfIpAddrReadMask=hpnicfIpAddrReadMask, hpnicfIpAddrReadAddrType=hpnicfIpAddrReadAddrType, hpnicfIpAddrReadSourceType=hpnicfIpAddrReadSourceType, PYSNMP_MODULE_ID=hpnicfIpAddrMIB, hpnicfIpAddrReadAddr=hpnicfIpAddrReadAddr, hpnicfIpAddrMIB=hpnicfIpAddrMIB, hpnicfIpAddrSetMask=hpnicfIpAddrSetMask, hpnicfIpAddrSetTable=hpnicfIpAddrSetTable, hpnicfIpAddrNotifyObjects=hpnicfIpAddrNotifyObjects, hpnicfIpAddrSetSourceType=hpnicfIpAddrSetSourceType, hpnicfIpv4AddrEntry=hpnicfIpv4AddrEntry, hpnicfIpAddrNotifyScalarObjects=hpnicfIpAddrNotifyScalarObjects, hpnicfIpAddrReadCatalog=hpnicfIpAddrReadCatalog, hpnicfIpv4AddrAddr=hpnicfIpv4AddrAddr, hpnicfIpAddressChangeNotify=hpnicfIpAddressChangeNotify, hpnicfIpAddrFirstTrapTime=hpnicfIpAddrFirstTrapTime, hpnicfIpAddrReadIfIndex=hpnicfIpAddrReadIfIndex, hpnicfIpAddrSetCatalog=hpnicfIpAddrSetCatalog, hpnicfIpv4AddrMask=hpnicfIpv4AddrMask, hpnicfIpAddrNotifyObjectsPrefix=hpnicfIpAddrNotifyObjectsPrefix, hpnicfIpAddrSetIfIndex=hpnicfIpAddrSetIfIndex, hpnicfIpAddrSetAddr=hpnicfIpAddrSetAddr, hpnicfIpAddressObjects=hpnicfIpAddressObjects, hpnicfIpAddrNotify=hpnicfIpAddrNotify, hpnicfIpAddrNewIpAddress=hpnicfIpAddrNewIpAddress, hpnicfIpAddrSetEntry=hpnicfIpAddrSetEntry, hpnicfIpv4AddrRowStatus=hpnicfIpv4AddrRowStatus, hpnicfIpAddrOldIpAddress=hpnicfIpAddrOldIpAddress, hpnicfIpAddrNotifyIfIndex=hpnicfIpAddrNotifyIfIndex, hpnicfIpAddrSetRowStatus=hpnicfIpAddrSetRowStatus, hpnicfIpAddrReadTable=hpnicfIpAddrReadTable, hpnicfIpAddrReadEntry=hpnicfIpAddrReadEntry, hpnicfIpAddrSetAddrType=hpnicfIpAddrSetAddrType)
