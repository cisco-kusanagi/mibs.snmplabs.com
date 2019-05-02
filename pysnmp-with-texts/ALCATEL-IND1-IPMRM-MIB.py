#
# PySNMP MIB module ALCATEL-IND1-IPMRM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-IPMRM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:18:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
routingIND1Ipmrm, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1Ipmrm")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, iso, IpAddress, Gauge32, NotificationType, Integer32, TimeTicks, MibIdentifier, Counter32, ObjectIdentity, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "iso", "IpAddress", "Gauge32", "NotificationType", "Integer32", "TimeTicks", "MibIdentifier", "Counter32", "ObjectIdentity", "ModuleIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alcatelIND1IPMRMMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1))
alcatelIND1IPMRMMIB.setRevisions(('2012-04-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1IPMRMMIB.setRevisionsDescriptions(('The latest version of this MIB Module.',))
if mibBuilder.loadTexts: alcatelIND1IPMRMMIB.setLastUpdated('201204030000Z')
if mibBuilder.loadTexts: alcatelIND1IPMRMMIB.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: alcatelIND1IPMRMMIB.setContactInfo('Please consult with Customer Service to ensure the most appropriate version of this document is used with the products in question: Alcatel-Lucent, Enterprise Solutions Division (Formerly Alcatel Internetworking, Incorporated) 26801 West Agoura Road Agoura Hills, CA 91301-5122 United States Of America Telephone: North America +1 800 995 2696 Latin America +1 877 919 9526 Europe +31 23 556 0100 Asia +65 394 7933 All Other +1 818 878 4507 Electronic Mail: support@ind.alcatel.com World Wide Web: http://alcatel-lucent.com/wps/portal/enterprise File Transfer Protocol: ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1IPMRMMIB.setDescription('This module describes an authoritative enterprise-specific Simple Network Management Protocol (SNMP) Management Information Base (MIB): This proprietary MIB contains management information for the configuration of IPMRM (IP Multicast Route Manager) global configuration parameters. The right to make changes in specification and other information contained in this document without prior notice is reserved. No liability shall be assumed for any incidental, indirect, special, or consequential damages whatsoever arising from or related to this document or the information contained herein. Vendors, end-users, and other interested parties are granted non-exclusive license to use this specification in connection with management of the products for which it is intended to be used. Copyright (C) 1995-2007 Alcatel-Lucent ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1IPMRMMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 1))
alaIpmrmGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 1, 1))
alaIpmrmMbrStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaIpmrmMbrStatus.setStatus('current')
if mibBuilder.loadTexts: alaIpmrmMbrStatus.setDescription('Administratively enables/disables the Multicast Border Router (MBR) functionality on this router.')
alaIpmrmMbrProtocolApps = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 1, 1, 2), Bits().clone(namedValues=NamedValues(("dvmrp", 0), ("pim", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIpmrmMbrProtocolApps.setStatus('current')
if mibBuilder.loadTexts: alaIpmrmMbrProtocolApps.setDescription('Bit map object to reflect the multicast protocols that are currently registered with IPMRM. Bits 0 - 1 are currently in use, and if set, indicate that the respective application is currently active: bit 0 - DVMRP bit 1 - PIM ')
alcatelIND1IPMRMMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 2))
alcatelIND1IPMRMMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 2, 1))
alcatelIND1IPMRMMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 2, 2))
alaIpmrmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaIpmrmCompliance = alaIpmrmCompliance.setStatus('current')
if mibBuilder.loadTexts: alaIpmrmCompliance.setDescription('The compliance statement for routers running IP Multicast and implementing the ALCATEL-IND1-IPMRM MIB.')
alaIpmrmConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmMbrStatus"), ("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmMbrProtocolApps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaIpmrmConfigMIBGroup = alaIpmrmConfigMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alaIpmrmConfigMIBGroup.setDescription('A collection of objects to support management of global configuration parameters for IP Multicast Routing')
mibBuilder.exportSymbols("ALCATEL-IND1-IPMRM-MIB", PYSNMP_MODULE_ID=alcatelIND1IPMRMMIB, alcatelIND1IPMRMMIBConformance=alcatelIND1IPMRMMIBConformance, alaIpmrmMbrStatus=alaIpmrmMbrStatus, alaIpmrmConfigMIBGroup=alaIpmrmConfigMIBGroup, alaIpmrmCompliance=alaIpmrmCompliance, alaIpmrmMbrProtocolApps=alaIpmrmMbrProtocolApps, alcatelIND1IPMRMMIBCompliances=alcatelIND1IPMRMMIBCompliances, alcatelIND1IPMRMMIBGroups=alcatelIND1IPMRMMIBGroups, alcatelIND1IPMRMMIB=alcatelIND1IPMRMMIB, alcatelIND1IPMRMMIBObjects=alcatelIND1IPMRMMIBObjects, alaIpmrmGlobalConfig=alaIpmrmGlobalConfig)
