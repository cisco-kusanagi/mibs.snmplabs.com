#
# PySNMP MIB module ALCATEL-IND1-GLOBALROUTETABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-GLOBALROUTETABLE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:17:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
routingIND1GlobalRouteTable, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1GlobalRouteTable")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, Unsigned32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, Integer32, Counter32, iso, TimeTicks, Counter64, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "Integer32", "Counter32", "iso", "TimeTicks", "Counter64", "Gauge32", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
alcatelIND1GRTMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1))
alcatelIND1GRTMIB.setRevisions(('2011-04-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1GRTMIB.setRevisionsDescriptions(('The latest version of this MIB Module.',))
if mibBuilder.loadTexts: alcatelIND1GRTMIB.setLastUpdated('201212010000Z')
if mibBuilder.loadTexts: alcatelIND1GRTMIB.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: alcatelIND1GRTMIB.setContactInfo('Please consult with Customer Service to ensure the most appropriate version of this document is used with the products in question: Alcatel-Lucent, Enterprise Solutions Division (Formerly Alcatel Internetworking, Incorporated) 26801 West Agoura Road Agoura Hills, CA 91301-5122 United States Of America Telephone: North America +1 800 995 2696 Latin America +1 877 919 9526 Europe +31 23 556 0100 Asia +65 394 7933 All Other +1 818 878 4507 Electronic Mail: support@ind.alcatel.com World Wide Web: http://alcatel-lucent.com/wps/portal/enterprise File Transfer Protocol: ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1GRTMIB.setDescription('This module describes an authoritative enterprise-specific Simple Network Management Protocol (SNMP) Management Information Base (MIB): This proprietary MIB contains management information for the configuration of the Global Route Table parameters. The right to make changes in specification and other information contained in this document without prior notice is reserved. No liability shall be assumed for any incidental, indirect, special, or consequential damages whatsoever arising from or related to this document or the information contained herein. Vendors, end-users, and other interested parties are granted non-exclusive license to use this specification in connection with management of the products for which it is intended to be used. Copyright (C) 1995-2011 Alcatel-Lucent ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1GRTMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1))
alaGrtConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1))
class AlaGrtRouteDistinguisher(TextualConvention, OctetString):
    description = 'Syntax for a route distinguisher and route target as defined in [RFC4346].'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

alaGrtRouteTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1), )
if mibBuilder.loadTexts: alaGrtRouteTable.setStatus('current')
if mibBuilder.loadTexts: alaGrtRouteTable.setDescription('The Global Routing Table.')
alaGrtRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteDistinguisher"), (0, "ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteDest"), (0, "ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteMaskLen"), (0, "ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteNextHop"))
if mibBuilder.loadTexts: alaGrtRouteEntry.setStatus('current')
if mibBuilder.loadTexts: alaGrtRouteEntry.setDescription('A particular route in the Global Route Table')
alaGrtRouteDistinguisher = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 1), AlaGrtRouteDistinguisher())
if mibBuilder.loadTexts: alaGrtRouteDistinguisher.setStatus('current')
if mibBuilder.loadTexts: alaGrtRouteDistinguisher.setDescription('The route distinguisher of a global route.')
alaGrtRouteDest = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 2), IpAddress())
if mibBuilder.loadTexts: alaGrtRouteDest.setStatus('current')
if mibBuilder.loadTexts: alaGrtRouteDest.setDescription('The destination IP address of this route.')
alaGrtRouteMaskLen = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 3), Unsigned32())
if mibBuilder.loadTexts: alaGrtRouteMaskLen.setStatus('current')
if mibBuilder.loadTexts: alaGrtRouteMaskLen.setDescription('The destination mask length of this route')
alaGrtRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 4), IpAddress())
if mibBuilder.loadTexts: alaGrtRouteNextHop.setStatus('current')
if mibBuilder.loadTexts: alaGrtRouteNextHop.setDescription('The Gateway for this route')
alaGrtRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaGrtRouteMetric.setStatus('current')
if mibBuilder.loadTexts: alaGrtRouteMetric.setDescription('The metric for this route')
alaGrtRouteTag = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaGrtRouteTag.setStatus('current')
if mibBuilder.loadTexts: alaGrtRouteTag.setDescription('The tag for this route')
alaGrtRouteVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaGrtRouteVrfName.setStatus('current')
if mibBuilder.loadTexts: alaGrtRouteVrfName.setDescription('The name of the VRF this route came from')
alaGrtRouteIsid = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaGrtRouteIsid.setStatus('current')
if mibBuilder.loadTexts: alaGrtRouteIsid.setDescription('The isid number this route came from')
alcatelIND1GRTMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 2))
alcatelIND1GRTMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 2, 1))
alcatelIND1GRTMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 2, 2))
alaGrtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaGrtCompliance = alaGrtCompliance.setStatus('current')
if mibBuilder.loadTexts: alaGrtCompliance.setDescription('The compliance statement for routers using the Global Route Manager and implementing the ALCATEL-IND1-GlobalRouteTable MIB.')
alaGrtConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteMetric"), ("ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteTag"), ("ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteVrfName"), ("ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteIsid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaGrtConfigMIBGroup = alaGrtConfigMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alaGrtConfigMIBGroup.setDescription('A collection of objects to support management of the Global Route Table configuration parameters.')
mibBuilder.exportSymbols("ALCATEL-IND1-GLOBALROUTETABLE-MIB", PYSNMP_MODULE_ID=alcatelIND1GRTMIB, alaGrtConfigMIBGroup=alaGrtConfigMIBGroup, alaGrtRouteNextHop=alaGrtRouteNextHop, alaGrtRouteVrfName=alaGrtRouteVrfName, alaGrtConfig=alaGrtConfig, alaGrtRouteMaskLen=alaGrtRouteMaskLen, alcatelIND1GRTMIBCompliances=alcatelIND1GRTMIBCompliances, alaGrtRouteTable=alaGrtRouteTable, alaGrtRouteMetric=alaGrtRouteMetric, alaGrtRouteDistinguisher=alaGrtRouteDistinguisher, alcatelIND1GRTMIBObjects=alcatelIND1GRTMIBObjects, alcatelIND1GRTMIB=alcatelIND1GRTMIB, alaGrtRouteIsid=alaGrtRouteIsid, alaGrtRouteDest=alaGrtRouteDest, alaGrtRouteTag=alaGrtRouteTag, alcatelIND1GRTMIBConformance=alcatelIND1GRTMIBConformance, alaGrtRouteEntry=alaGrtRouteEntry, alcatelIND1GRTMIBGroups=alcatelIND1GRTMIBGroups, alaGrtCompliance=alaGrtCompliance, AlaGrtRouteDistinguisher=AlaGrtRouteDistinguisher)
